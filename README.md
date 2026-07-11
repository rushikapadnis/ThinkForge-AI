# 🚀 ThinkForge-AI – AI Research Automation System

**ThinkForge-AI** is an AI-powered multi-agent research automation platform built with **FastAPI**, **LangGraph**, and **LLMs**. It transforms a single user query into a structured research report by coordinating specialized AI agents that plan, research, analyze, write, and review information automatically.

> **Tech Focus:** AI Agents • Generative AI • LangGraph • FastAPI • LangChain • LLM Orchestration • Async Python

---

## ✨ Key Highlights

- 🤖 Built an end-to-end multi-agent AI workflow using LangGraph.
- ⚡ Developed REST APIs with FastAPI for seamless integration.
- 🔍 Automated research by combining web search with LLM reasoning.
- 🧠 Implemented Planner, Researcher, Analyst, Writer, and Reviewer agents.
- 🚀 Used asynchronous execution for parallel research tasks.
- 📄 Generated structured, review-ready research reports automatically.

---

# 🏗️ Architecture

```text
                User Query
                     │
                     ▼
            ┌────────────────┐
            │ Planner Agent  │
            └────────────────┘
                     │
                     ▼
      ┌───────────────────────────┐
      │ Parallel Research Agents  │
      └───────────────────────────┘
                     │
                     ▼
            ┌────────────────┐
            │ Analyst Agent  │
            └────────────────┘
                     │
                     ▼
            ┌────────────────┐
            │ Writer Agent   │
            └────────────────┘
                     │
                     ▼
            ┌────────────────┐
            │ Reviewer Agent │
            └────────────────┘
                     │
                     ▼
              Final Research Report
```

---

# 🛠️ Tech Stack

- **Backend:** FastAPI
- **AI Framework:** LangGraph, LangChain
- **LLM:** Groq API / OpenAI
- **Search:** DuckDuckGo Search
- **Programming:** Python
- **Concurrency:** AsyncIO
- **Configuration:** Python Dotenv

---

# ✨ Features

- Multi-Agent AI Architecture
- Agent-based Task Planning
- Automated Web Research
- Parallel Information Gathering
- LLM-powered Report Generation
- Self Review & Revision Loop
- REST APIs with FastAPI
- Modular & Scalable Codebase
- Environment-based Configuration

---

# 📂 Project Structure

```text
AgentFlow/
│
├── agents/
│   ├── planner.py
│   ├── researcher.py
│   ├── analyst.py
│   ├── writer.py
│   └── reviewer.py
│
├── graph/
│   └── workflow.py
│
├── api/
│   └── routes.py
│
├── models/
├── utils/
├── main.py
├── requirements.txt
└── .env
```

---

# 🔑 Environment Variables

Create a `.env` file.

```env
MAX_REVISIONS=2
MAX_SUBTOPICS=4

LLM_PROVIDER=groq
GROQ_API_KEY=YOUR_API_KEY
```

---

# 📦 Installation

```bash
git clone https://github.com/your-username/AgentFlow.git

cd AgentFlow

pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
uvicorn main:app --reload
```

The application will start at:

```
http://127.0.0.1:8000
```

---

# 📡 API Endpoints

## 🔍 Run Research

**POST** `/api/research`

### Request

```json
{
  "query": "Applications of AI in Healthcare",
  "max_subtopics": 4
}
```

---

## ❤️ Health Check

**GET** `/health`

### Response

```json
{
  "status": "ok",
  "service": "AgentFlow"
}
```

---

# 🔄 Workflow

```text
User Query
      │
      ▼
Planner
      │
      ▼
Research (Parallel)
      │
      ▼
Analysis
      │
      ▼
Report Generation
      │
      ▼
Review & Refinement
      │
      ▼
Final Research Report
```

---

# 💼 Skills Demonstrated

- Generative AI
- AI Agent Development
- LangGraph
- LangChain
- Prompt Engineering
- FastAPI
- REST API Development
- LLM Integration
- Async Python
- Workflow Orchestration
- Modular Software Architecture

---

# 🚀 Future Enhancements

- Streaming Responses (SSE)
- Multi-LLM Support
- Vector Database Integration
- Retrieval-Augmented Generation (RAG)
- Persistent Memory
- Authentication & User Management
- Docker Deployment
- CI/CD Pipeline

---

