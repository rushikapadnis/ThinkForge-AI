

# 🚀 AgentFlow – FastAPI AI Agent System

AgentFlow is a FastAPI-powered autonomous AI research system that plans, researches, analyzes, and generates structured reports using a multi-agent workflow built with LangGraph and LLMs.

---

## 🧠 What It Does

AgentFlow takes a simple query and turns it into a full research workflow:

1. Breaks query into subtopics (Planner)
2. Collects data from web / LLM (Researcher)
3. Extracts key insights (Analyst)
4. Generates structured report (Writer)
5. Reviews and improves output (Reviewer)

---

## ⚙️ Tech Stack

- FastAPI (Backend API)
- LangGraph (Agent workflow orchestration)
- LangChain (LLM integration)
- Groq / OpenAI (LLM providers)
- DuckDuckGo Search (real-time data)
- Python Async (concurrent execution)

---

## 🔑 Environment Setup

Create a `.env` file:

```env
MAX_REVISIONS=2
MAX_SUBTOPICS=4

LLM_PROVIDER=groq
GROQ_API_KEY=your_api_key_here

📦 Installation
git clone https://github.com/your-username/fastapi-ai-agentflow.git
cd fastapi-ai-agentflow

pip install -r requirements.txt

▶️ Run Server
uvicorn main:app --reload

Server will start at:

http://127.0.0.1:8000
📡 API Endpoints
🔍 Run Research
POST /api/research

Request Body:

{
  "query": "AI in healthcare",
  "max_subtopics": 4
}
❤️ Health Check
GET /health

Response:

{
  "status": "ok",
  "service": "AgentFlow"
}

🔄 Workflow Overview
User Query
   ↓
Planner
   ↓
Researcher
   ↓
Analyst
   ↓
Writer
   ↓
Reviewer
   ↓
Final Output

✨ Features
Multi-agent AI pipeline
Real-time + LLM fallback search
Self-review & revision loop
Async parallel execution
Clean modular architecture


🧠 Future Improvements
Streaming responses (SSE)
UI dashboard
Multi-model support
Persistent memory (vector DB)
