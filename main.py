import config

from flask import Flask, render_template, request, jsonify, session
import ai_logic

app = Flask(__name__)
app.secret_key = config.FLASK_SECRET_KEY


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat/message", methods=["POST"])
def chat_message():
    data = request.get_json()

    user_message = data.get("message", "")

    history = session.get("history", [])

    history.append({
        "role": "user",
        "content": user_message
    })

    reply = ai_logic.get_ai_reply(history)

    history.append({
        "role": "assistant",
        "content": reply
    })

    session["history"] = history

    return jsonify({
        "reply": reply
    })


if __name__ == "__main__":
    app.run(debug=True)