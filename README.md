# AI-Powered Learning Platform

Analyze community issues and get AI-powered mentorship for solving problems.

## Features

- **Problem Analysis**: Detect and classify community issues from images or text
- **AI Mentor**: Get guidance through critical thinking or solution templates
  - Critical Thinking Mode: Socratic questions to explore problems deeply
  - Solution Mode: Quick templates (SWOT, Budget, Action Plans, etc.)
  - Interactive Chat: Conversational guidance

## How to Run

### 1. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate # On Linux/Mac use: source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up API Key

Create a `.env` file:

```bash
GEMINI_API_KEY=your_gemini_api_key_here
```

Get your free API key: https://aistudio.google.com/app/apikey

### 4. Run the Application

```bash
streamlit run app.py
```

Open your browser at: http://localhost:8501
