// document.addEventListener("DOMContentLoaded", function () {
//     document.getElementById("user-input").addEventListener("keypress", function (e) {
//         if (e.key === "Enter") {
//             sendMessage();
//         }
//     });
// });

// function sendMessage() {
//     let inputField = document.getElementById("user-input");
//     let message = inputField.value.trim();
//     if (message === "") return;

//     let chatbox = document.getElementById("chatbox");
//     let userMessage = document.createElement("p");
//     userMessage.textContent = "You: " + message;
//     chatbox.appendChild(userMessage);

//     // Send to Flask Backend
//     fetch("/chat-response", {
//         method: "POST",
//         headers: { "Content-Type": "application/json" },
//         body: JSON.stringify({ message: message })
//     })
//     .then(response => response.json())
//     .then(data => {
//         let botMessage = document.createElement("p");
//         botMessage.textContent = "Bot: " + data.response;
//         chatbox.appendChild(botMessage);
//     });

//     inputField.value = "";
// }

document.addEventListener("DOMContentLoaded", function () {
    const chatBox = document.getElementById("chat-box");
    const userInput = document.getElementById("user-input");

    window.sendMessage = async function () {
        let message = userInput.value.trim();
        if (!message) return;

        // Display user message
        chatBox.innerHTML += `<p><strong>You:</strong> ${message}</p>`;
        userInput.value = "";

        try {
            let response = await fetch("/ai-chat", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ message: message }),
            });

            let data = await response.json();

            // Display AI response
            chatBox.innerHTML += `<p><strong>AI:</strong> ${data.response}</p>`;
        } catch (error) {
            console.error("Chatbot Error:", error);
            chatBox.innerHTML += `<p><strong>AI:</strong> ❌ Error connecting to AI!</p>`;
        }
    };
});
