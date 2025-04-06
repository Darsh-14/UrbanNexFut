const userInput = document.getElementById("userInput");
const sendButton = document.getElementById("sendButton");
const chatBox = document.getElementById("chatBox");

// Function to send message and get AI response
async function getAIResponse(message) {
    try {
        const response = await fetch("http://localhost:5001/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message }),
        });
        

        const data = await response.json();
        return data.reply;
    } catch (error) {
        console.error("Error fetching AI response:", error);
        return "Error getting response!";
    }
}

// Handle user input and display AI response
sendButton.addEventListener("click", async () => {
    const message = userInput.value.trim();
    if (!message) return;

    chatBox.innerHTML += `<p><strong>You:</strong> ${message}</p>`;
    userInput.value = "";

    const botReply = await getAIResponse(message);
    chatBox.innerHTML += `<p><strong>Bot:</strong> ${botReply}</p>`;
});