# 🧠 AI Blog Generator with CrewAI + Gemini

This project demonstrates how to build a multi-agent system using [CrewAI](https://github.com/joaomdmoura/crewAI) and Google's Gemini (`gemini-1.5-flash`) via LangChain to research and write insightful articles on emerging technology topics.

---

## 🚀 Project Overview

We define two AI agents:

1. **Senior Researcher Agent**  
   - Gathers and analyzes information about a given tech topic.
   - Provides a structured summary of pros, cons, market trends, and risks.

2. **Writer Agent**  
   - Crafts a compelling, human-readable article based on the research.
   - Outputs a markdown file with structured insights.

Agents are coordinated using `CrewAI` with a **sequential task process**.

---

## 🧰 Tech Stack

| Component         | Library / Tool                       |
|------------------|--------------------------------------|
| Agent Framework   | [CrewAI](https://github.com/joaomdmoura/crewAI) |
| LLM               | [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/overview) via LangChain |
| LLM Wrapper       | [LangChain Google GenAI](https://python.langchain.com/docs/integrations/chat/google_genai/) |
| Tool Integration  | Custom Tool via `tools.py` (can be extended) |
| Environment       | Python 3.10+, `venv` for isolation   |

---

## 📁 Project Structure
📦 crewai_gemini
├── agents.py # Agent setup (roles, goals, LLM)
├── tasks.py # Task definitions
├── tools.py # Tool used by both agents
├── crew.py # Execution logic
├── .env # API keys (not committed)
└── README.md # This file
