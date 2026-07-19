# 🚀 Multi-Agent PPT Generator

An AI-powered **multi-agent presentation generation system** that automatically converts a **Topic / Text / Document** into a professional **PowerPoint Presentation (.pptx)** with minimal human intervention.

Built using **LangGraph + LangChain + Groq + ChromaDB + FastAPI**.

---

## 📌 Project Overview

Creating presentations manually takes time.

This project uses an **Agentic AI workflow** where multiple intelligent agents collaborate to:

✅ Understand the topic or uploaded document  
✅ Plan presentation structure  
✅ Research content  
✅ Generate concise slide bullets  
✅ Improve slide quality  
✅ Build downloadable PowerPoint automatically

---

## 🧠 Multi-Agent Workflow

```text
User Input
   ↓
Router Agent
   ↓
Parser Agent
   ↓
RAG Agent
   ↓
Planner Agent
   ↓
Research Agent
   ↓
Structure Agent
   ↓
Content Agent
   ↓
Design Agent
   ↓
PPT Builder Agent
   ↓
Reviewer Agent
   ↓
Final PPT Output
```

---

## ⚙️ Key Features

* 📄 Topic / Text / Document to PPT
* 🤖 Multi-Agent AI Workflow
* 🧠 RAG with ChromaDB
* 📊 Automatic PowerPoint Generation
* 🖥️ Simple Web UI
* ⚡ Fast Cloud LLM Inference using Groq (with Gemini as fallback)
* 🔐 Free-tier API keys, no local GPU required
* 📥 Download Generated PPT

---

## 🛠️ Tech Stack

| Category       | Tools                            |
| -------------- | -------------------------------- |
| Backend        | Python, FastAPI                  |
| AI Framework   | LangChain, LangGraph             |
| LLM            | Groq (Llama 3.3) / Gemini fallback |
| Vector DB      | ChromaDB                         |
| PPT Generation | python-pptx                      |
| Frontend       | HTML, CSS, JavaScript            |

---

## � Docker + Render Deployment

This project includes a `Dockerfile` so you can deploy the backend to any container-friendly host.

### Local Docker run

```bash
docker build -t genai-ppt-agent .
docker run -p 8000:8000 -e GROQ_API_KEY=your_groq_api_key_here genai-ppt-agent
```

Then open:

```text
http://127.0.0.1:8000
```

### Deploy to Render

1. Push your repo to GitHub.
2. Create a new **Web Service** on Render.
3. Select **Docker** as the environment (Render auto-detects the `Dockerfile`).
4. Use this repo and the `main` branch.
5. Leave the start command blank — the Dockerfile's `CMD` already binds to whatever port Render assigns via `$PORT`.
6. Add environment variables (see below), then deploy.

Render gives you a public URL like `https://your-service.onrender.com`. Point your separately-deployed frontend's API calls at that URL — CORS is already open to all origins in `api/server.py`.

### Environment variables

Set your secrets in Render's dashboard (or via `-e` on `docker run`):

- `GROQ_API_KEY` (required — get one free at https://console.groq.com)
- `GROQ_MODEL` (optional, defaults to `llama-3.3-70b-versatile`)
- `GEMINI_API_KEY` (optional fallback if Groq isn't configured)

---

## �📁 Project Structure

```text
genai-ppt-agent/
│
├── agents/
├── graph/
├── tools/
├── llm/
├── api/
├── frontend/
├── output/
└── requirements.txt
```

---

## 🤖 Agents Used

### 1️⃣ Router Agent

Detects input type (topic / text / document)

### 2️⃣ Parser Agent

Extracts usable content from uploaded files

### 3️⃣ RAG Agent

Stores and retrieves relevant chunks using ChromaDB

### 4️⃣ Planner Agent

Creates slide outline

### 5️⃣ Research Agent

Generates content for each slide

### 6️⃣ Structure Agent

Organizes presentation flow

### 7️⃣ Content Agent

Improves bullets, grammar, clarity

### 8️⃣ Design Agent

Applies presentation style metadata

### 9️⃣ PPT Builder Agent

Creates `.pptx` file

### 🔟 Reviewer Agent

Final quality checks

---

## 🚀 Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/multi-agent-ppt-generator.git
cd multi-agent-ppt-generator
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set your Groq API key

Get a free API key from [https://console.groq.com](https://console.groq.com), then create a `.env` file in the project root:

```bash
GROQ_API_KEY=your_groq_api_key_here
```

---

## ▶️ Run Project

```bash
uvicorn api.server:app --reload
```

Then open browser:

```text
http://127.0.0.1:8000
```

---

## 📷 Sample Use Case

### Input

```text
Topic: Retrieval Augmented Generation
```

### Output

✅ Auto-generated professional PPT

---

## 🎯 Resume Value

This project demonstrates:

* Agentic AI Systems
* Multi-Agent Orchestration
* RAG Architecture
* Cloud LLM Integration (Groq)
* Real-world Automation
* FastAPI Deployment Skills

---

## 🔮 Future Enhancements

* 🎨 Premium Slide Templates
* 🖼️ Auto Images / Icons
* 📊 Charts Generation
* 🌐 Cloud Deployment
* 👥 Multi-user Login
* 📈 Analytics Dashboard

---

## 👨‍💻 Author

**Teeguri Prasanna Kumar Reddy**
AI / GenAI Developer

LinkedIn: [https://linkedin.com/in/teeguri-prasanna-kumar-reddy](https://linkedin.com/in/teeguri-prasanna-kumar-reddy)

---

## ⭐ If you like this project, give it a star!


>>>>>>> bcede9b922143e29a6a4d2bb4575db39e2205e33
