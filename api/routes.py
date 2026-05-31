from fastapi import APIRouter
from graph.workflow import research_graph
from models import ResearchRequest, new_task

router = APIRouter()


@router.post("/research")
async def run_research(req: ResearchRequest):
    task = new_task(req.query)

    state = {
        "task_id": task.task_id,
        "query": req.query,
        "max_subtopics": req.max_subtopics or 4,
        "plan": [],
        "search_results": {},
        "analysis": "",
        "report": "",
        "citations": [],
        "review_feedback": "",
        "revision_count": 0,
        "max_revisions": 2,
        "verdict": "",
        "logs": [],
        "status": "running",
        "error": None,
    }

    result = await research_graph.ainvoke(state)

    return result