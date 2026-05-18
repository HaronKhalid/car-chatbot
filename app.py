from flask import Flask, render_template, request, jsonify
import requests
import json
import os

app = Flask(__name__)

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "paste your openrouter api key here")

SYSTEM_PROMPT = """You are AutoGPT, an elite automotive expert with decades of experience across all aspects of the car industry. You have deep knowledge of:

- All car brands, models, and their specifications (past and present)
- Engine types, transmissions, drivetrains (ICE, hybrid, electric, hydrogen)
- Car buying advice, pricing, depreciation, and resale value
- Maintenance, repairs, and common issues for specific models
- Performance tuning, modifications, and upgrades
- Racing, motorsport, and high-performance vehicles
- Car history, classic cars, and automotive culture
- Safety ratings, reliability data, and owner reviews
- Fuel efficiency, emissions, and environmental impact
- Insurance, financing, and ownership costs

You give precise, expert answers. When recommending cars, always consider the user's needs. Be enthusiastic about cars but also honest about flaws. Use technical terms when appropriate but explain them clearly. Keep responses concise but thorough."""

conversation_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    global conversation_history
    
    data = request.json
    user_message = data.get("message", "").strip()
    
    if not user_message:
        return jsonify({"error": "Empty message"}), 400
    
    conversation_history.append({
        "role": "user",
        "content": user_message
    })
    
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "HTTP-Referer": "http://localhost:5000",
                "X-Title": "AutoGPT Car Expert"
            },
            data=json.dumps({
                "model": "meta-llama/llama-3.3-70b-instruct",
                "messages": conversation_history
            })
        )
        
        response_data = response.json()
        
        if "error" in response_data:
            raise Exception(response_data["error"].get("message", "Unknown error from OpenRouter"))
            
        assistant_message = response_data["choices"][0]["message"]["content"]
        
        conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })
        
        return jsonify({"response": assistant_message})
    
    except Exception as e:
        conversation_history.pop() # Remove the user message that caused the error
        return jsonify({"error": str(e)}), 500

@app.route("/reset", methods=["POST"])
def reset():
    global conversation_history
    conversation_history = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
