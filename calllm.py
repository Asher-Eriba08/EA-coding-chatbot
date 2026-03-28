import requests

def callOLLAMA(user_message):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "deepseek-r1:1.5b",
                "prompt": f"""
You are a helpful and precise assistant.

Rules:
- Give clear and direct answers
- Do NOT over-explain
- Do NOT analyze symbols or unrelated text
- If the task is coding, return ONLY the code
- Keep responses simple and correct
- Follow the user request exactly

Task: {user_message}
""",
                "stream": False,
                "max_tokens": 250,
                "temperature": 0.2
            },
            timeout=120
        )

        response.raise_for_status()

        result = response.json()
        return result.get("response", "Sorry, no response from model.").strip()

    except requests.exceptions.ConnectionError:
        return "❌ Cannot connect to Ollama. Make sure Ollama is running."

    except requests.exceptions.Timeout:
        return "⏱️ Ollama is taking too long to respond."

    except Exception as e:
        return f"⚠️ Unexpected error: {e}"