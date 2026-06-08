from flask import Flask, render_template, request, jsonify
import ai_logic

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat/message", methods=["POST"])
def chat_message():
    data = request.get_json()

    user_message = data.get("message", "")

    history = [
        {"role": "user", "content": user_message}
    ]

    reply = ai_logic.get_ai_reply(history)

    return jsonify({
        "reply": reply
    })


if __name__ == "__main__":
    app.run(debug=True)