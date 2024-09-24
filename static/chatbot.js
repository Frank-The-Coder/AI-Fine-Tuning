document.addEventListener('DOMContentLoaded', function() {
document.getElementById('messageInput').addEventListener('keydown', function(event) {
    if (event.key === "Enter") {
        sendMessage();
        event.preventDefault(); // To prevent the default action (form submission, new line, etc.)
    }
});


function appendToChatbox(message, sender) {
    const chatbox = document.getElementById('chatbox');
    const messageDiv = document.createElement('div');
    messageDiv.textContent = sender + ": " + message;
    chatbox.appendChild(messageDiv);
    chatbox.scrollTop = chatbox.scrollHeight;
}

function sendMessage() {
    const inputElement = document.getElementById('messageInput');
    const userMessage = inputElement.value;

    if (userMessage.trim() === "") return; // Avoid empty messages

    appendToChatbox(userMessage, "You");

    fetch('/ask', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userMessage })  // Send as a JSON object
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        const botReply = data.reply;
        appendToChatbox(botReply, "Chatbot");
    })
    .catch(error => {
        console.error("Error sending message:", error);
    });

    inputElement.value = ""; // Clear input field
}

});