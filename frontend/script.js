const sessionId = "demo-session";
const socket = new WebSocket(`ws://localhost:8000/ws/session/${sessionId}`);

const chatBox = document.getElementById("chat-box");

socket.onmessage = (event) => {
    chatBox.innerHTML += `<div>AI: ${event.data}</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;
};

function sendMessage() {
    const input = document.getElementById("message");
    socket.send(input.value);
    chatBox.innerHTML += `<div>You: ${input.value}</div>`;
    input.value = "";
}
