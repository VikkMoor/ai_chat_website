import config

from flask import Flask, render_template, request, jsonify, session
import ai_logic

import sheets

from datetime import datetime

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


    if "[COMPLETE]" in reply:

        order_data = ai_logic.extract_order(history)

        order_data["created_at"] = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        order_data["source"] = "website"

        sheets.save_order(order_data)

        session["history"] = []

        reply = (
            "Спасибо! Ваш заказ успешно оформлен.\n"
            "Мы свяжемся с вами в ближайшее время."
        )


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