async function sendMessage() {
    const userInput = document.getElementById('userInput');
    const message = userInput.value.trim();
    if (!message) return;

    // Display user message
    const chatbox = document.getElementById('chatbox');
    const userMessageDiv = document.createElement('div');
    userMessageDiv.className = 'message user';
    userMessageDiv.textContent = message;
    chatbox.appendChild(userMessageDiv);

    // Clear input
    userInput.value = '';

    // Send to backend
    try {
        const response = await fetch('http://localhost:8000/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message, user_id: 'user1' }),
        });
        const data = await response.json();
        
        // Display bot message
        const botMessageDiv = document.createElement('div');
        botMessageDiv.className = 'message bot';
        botMessageDiv.textContent = data.response;
        chatbox.appendChild(botMessageDiv);

        // If the message is about an image, generate one
        if (message.toLowerCase().includes('image') || message.toLowerCase().includes('picture')) {
            const imageResponse = await fetch('http://localhost:8000/generate_image', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ prompt: message }),
            });
            const imageData = await imageResponse.json();
            const img = document.createElement('img');
            img.src = imageData.image_url;
            document.getElementById('imageContainer').appendChild(img);
        }
    } catch (error) {
        console.error('Error:', error);
        const errorDiv = document.createElement('div');
        errorDiv.className = 'message bot error';
        errorDiv.textContent = 'Sorry, an error occurred.';
        chatbox.appendChild(errorDiv);
    }

    // Scroll to bottom
    chatbox.scrollTop = chatbox.scrollHeight;
}

// Allow sending message with Enter key
document.getElementById('userInput').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});
