# 🏎️ AutoGPT — Car Expert Chatbot

A minimal, sleek AI-powered car expert chatbot built with Flask and the OpenRouter API (using Meta Llama 3.3 70B).

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Set your API key
Get your API key from [OpenRouter](https://openrouter.ai/).
Set it as an environment variable before running the app:

```bash
# Windows
set OPENROUTER_API_KEY=sk-or-v1-...

# Mac/Linux
export OPENROUTER_API_KEY=sk-or-v1-...
```

Alternatively, you can create a `.env` file in the root directory (see `.env.example`). Note that to use `.env` files automatically, you may need to install `python-dotenv` and load it in `app.py`.

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
