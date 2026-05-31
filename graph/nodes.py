
import asyncio             # used to run multiple task at the same time
import json                # used to convert text into structure data

from langchain_core.messages import HumanMessage, SystemMessage  # import msg type used to talk to the ai model
from config import get_llm, MAX_SUBTOPICS                        # import fun get ai model and a constant value
from graph.state import ResearchState                            # import the shared state structure that holds all data in worksflow


# -----------------------------
# SAFE LLM CALL
# -----------------------------
# create this function to safely call ai model
# if something break (network issue, api error), it should not crash the system
# async means it can run without blocking other task
async def _llm(messages: list) -> str:                          
    llm = get_llm()                                              # get the ai model
    try:
        res = await asyncio.to_thread(llm.invoke, messages)      #  run the model in a seprate  thread so it does not block other task
        return (res.content or "").strip()                       # return text response, remove extra space
    except Exception:
        return ""


# -----------------------------
# 1. PLANNER
# -----------------------------
async def planner_node(state: ResearchState) -> dict:
    query = state.get("query", "")
    n = state.get("max_subtopics", MAX_SUBTOPICS)

# ask ai to generate sbtopic in json formate
    raw = await _llm([
        SystemMessage(content=f"Return ONLY a JSON list of {n} subtopics."),
        HumanMessage(content=query)
    ])

    plan = [query] # fallback: if ai fails , at least keep the original query as the only topic to explore

    try:
        clean = raw.replace("```json", "").replace("```", "").strip()    # clean unwanted formating from ai response, so it can be parsed as json
        parsed = json.loads(clean)                                       # convert text into python list

        if isinstance(parsed, list) and parsed:
            plan = parsed[:n]                                            # limit to max_subtopic
    except Exception:
        pass   

    return {
        "plan": plan,
        "status": "running"
    }

# -----------------------------
# 2. SEARCH
# -----------------------------
async def _search(subtopic: str):
    llm = get_llm()

    # try duckduckgo first
    try:
        from duckduckgo_search import DDGS

        with DDGS() as ddgs:
            results = list(ddgs.text(subtopic, max_results=3))

        if results:
            text = " | ".join(
                r.get("body", "")[:250] for r in results if r.get("body")
            )
            if text.strip():
                return subtopic, text, []

    except Exception:
        pass

    # fallback to LLM
    # if real search fails we use ai to generate information
    try:
        res = await asyncio.to_thread(
            llm.invoke,
            [
                SystemMessage(content="Give factual, structured explanation."),
                HumanMessage(content=subtopic)
            ]
        )
        return subtopic, (res.content or "").strip(), []
    except Exception:
        return subtopic, "", []

# -----------------------------
# 3. RESEARCHER
# -----------------------------
async def researcher_node(state: ResearchState) -> dict:
    plan = state.get("plan", [])

    results = await asyncio.gather(*[_search(p) for p in plan])

    search_results = {}
    citations = []

    for topic, text, urls in results:
        search_results[topic] = text
        citations.extend(urls)

    return {
        "search_results": search_results,
        "citations": list(set(citations))
    }


# -----------------------------
# 4. ANALYST
# -----------------------------
async def analyst_node(state: ResearchState) -> dict:
    data = state.get("search_results", {})

    formatted = "\n\n".join(f"{k}\n{v}" for k, v in data.items())

    analysis = await _llm([
        SystemMessage(content="Summarize into 5-7 clear bullet points. No fluff."),
        HumanMessage(content=formatted)
    ])

    return {"analysis": analysis}


# -----------------------------
# 5. WRITER
# -----------------------------
async def writer_node(state: ResearchState) -> dict:
    content = state.get("analysis", "")

    feedback = state.get("review_feedback")
    if feedback:
        content += "\nFix feedback:\n" + feedback

    report = await _llm([
        SystemMessage(content="""
Write a clean markdown report.

Rules:
- max 6 bullets OR 2 short sections
- no intro phrases
- no repetition
- keep it concise
"""),
        HumanMessage(content=content)
    ])

    return {"report": report}


# -----------------------------
# 6. REVIEWER (FIXED + SAFE JSON)
# -----------------------------
async def reviewer_node(state: ResearchState) -> dict:
    revision = state.get("revision_count", 0)
    max_rev = state.get("max_revisions", 2)

    raw = await _llm([
        SystemMessage(content='Return ONLY JSON: {"verdict":"approved|revise","feedback":"..."}'),
        HumanMessage(content=state.get("report", ""))
    ])

    verdict = "approved"
    feedback = ""

    try:
        clean = raw.replace("```json", "").replace("```", "").strip()
        parsed = json.loads(clean)

        verdict = parsed.get("verdict", "approved")
        feedback = parsed.get("feedback", "")

    except Exception:
        pass

    if verdict == "revise" and revision < max_rev:
        return {
            "verdict": "revise",
            "review_feedback": feedback,
            "revision_count": revision + 1,
            "status": "running"
        }

    return {
        "verdict": "approved",
        "status": "completed"
    }


# -----------------------------
# FLOW CONTROL
# -----------------------------
def should_continue(state: ResearchState) -> str:
    return state.get("verdict", "approved")
