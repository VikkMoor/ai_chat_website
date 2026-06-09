const sendButton = document.getElementById("send-button");
const messageInput = document.getElementById("message-input");
const chatMessages = document.getElementById("chat-messages");

function addMessage(text, sender) {
    const message = document.createElement("div");

    message.textContent = text;
    message.classList.add(sender);

    chatMessages.appendChild(message);

    chatMessages.scrollTop = chatMessages.scrollHeight;
}

async function sendMessageToServer(text) {
    const response = await fetch("/chat/message", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: text
        })
    });

    return await response.json();
}

sendButton.addEventListener("click", async () => {
    const text = messageInput.value.trim();

    if (!text) {
        return;
    }

    addMessage(text, "user");

    messageInput.value = "";

    const data = await sendMessageToServer(text);

    addMessage(data.reply, "assistant");
});


messageInput.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
        sendButton.click();
    }
});