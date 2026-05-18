# 🏎️ AutoGPT — Car Expert Chatbot

A minimal, sleek AI-powered car expert chatbot built with Flask + Anthropic Claude.

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Add your API key
Open `app.py` and replace `YOUR_API_KEY_HERE` with your Anthropic API key:
```python
client = anthropic.Anthropic(api_key="sk-ant-...")
```

Or set it as an environment variable (recommended):
```bash
# Windows
set ANTHROPIC_API_KEY=sk-ant-your-key-here

# Mac/Linux
export ANTHROPIC_API_KEY=sk-ant-your-key-here
```

### 3. Run the app
```bash
python app.py
```

### 4. Open in browser
Visit: **http://localhost:5000**

---

## Features
- 🏎️ Expert car knowledge — specs, buying advice, repairs, comparisons
- 💬 Multi-turn conversation memory (within a session)
- 🔄 "New Chat" button to reset conversation
- ⚡ Quick suggestion chips on startup
- 📱 Clean dark automotive-themed UI
