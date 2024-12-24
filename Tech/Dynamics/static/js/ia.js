  const chatButton = document.getElementById('chatButton');
  const chatWindow = document.getElementById('chatWindow');
  const chatMessages = document.getElementById('chatMessages');
  const userInput = document.getElementById('userInput');
  
  let isOpen = false;
  
  function toggleChat() {
    isOpen = !isOpen;
    chatWindow.classList.toggle('active');
    if (isOpen) {
      userInput.focus();
    }
  }
  
  chatButton.addEventListener('click', toggleChat);
  
  function addMessage(message, isUser = false) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${isUser ? 'user-message' : 'bot-message'}`;
    messageDiv.textContent = message;
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }
  
  async function getAIResponse(message) {
    try {
      // Normalizar el mensaje (eliminar acentos, convertir a minúsculas)
      const normalizeMessage = message
        .normalize("NFD")
        .replace(/[\u0300-\u036f]/g, "")
        .toLowerCase();
  
      // Conjuntos de palabras clave
      const keywordSets = {
        greetings: ['hola', 'buenos dias', 'buenas tardes', 'buenas noches', 'hi', 'hello', 'hey', 'que tal'],
        howAreYou: ['como estas', 'que tal', 'como te encuentras', 'todo bien'],
        interestingFacts: ['sabes algo interesante', 'dime algo curioso', 'cuentame algo nuevo'],
        jokes: ['cuentame un chiste', 'dime algo gracioso', 'hazme reir'],
        compliments: ['eres genial', 'me encantas', 'eres increible', 'que amable', 'me gusta hablar contigo'],
        time: ['que hora es', 'me dices la hora', 'hora actual']
      };
  
      // Respuestas predefinidas
      const predefinedReplies = {
        greetings: [
          "¡Hola! Soy TESSA. ¿Cómo puedo ayudarte hoy?",
          "¡Hola! Soy TESSA, ¿qué tal? ¿En qué te puedo asistir?",
          "¡Buenas! Soy TESSA, ¿cómo estás? ¿Qué puedo hacer por ti?"
        ],
        howAreYou: [
          "Estoy bien, gracias por preguntar. ¿Y tú cómo estás?",
          "Todo bien por aquí. ¿Y tú, qué tal?",
          "Estoy en óptimas condiciones, ¡gracias por preguntar! ¿Y tú?",
          "¡Estoy bien! ¿Cómo te encuentras tú?"
        ],
        interestingFacts: [
          "¿Sabías que las abejas pueden reconocer rostros humanos?",
          "El corazón de una ballena azul pesa tanto como un automóvil pequeño.",
          "Los rayos caen con más frecuencia en los hombres que en las mujeres.",
          "Un día en Venus dura más que un año en ese planeta."
        ],
        jokes: [
          "¿Por qué las focas del circo miran siempre hacia arriba? ¡Porque es donde están los focos!",
          "¿Qué le dice un semáforo a otro? No me mires que me estoy cambiando.",
          "¿Por qué los peces no usan Facebook? Porque le tienen miedo a la red."
        ],
        compliments: [
          "¡Gracias! Tú también eres genial. Me encanta charlar contigo.",
          "Aw, me haces sonrojar (si pudiera). ¡Eres muy amable!",
          "¡Qué amable eres! Espero estar a la altura de tus expectativas."
        ],
        default: [
          "Lo siento, no estoy seguro de cómo responder eso. ¿Puedes intentarlo de otra manera?",
          "No entendí eso, pero estoy aquí para ayudarte. ¿Qué necesitas?",
          "Hmmm... no tengo esa información ahora mismo, ¿algo más en lo que pueda ayudarte?"
        
        ]
      };
  
      // Respuesta para la hora actual
      if (keywordSets.time.some(keyword => normalizeMessage.includes(keyword))) {
        const currentTime = new Date();
        const hours = currentTime.getHours();
        const minutes = currentTime.getMinutes();
        return `La hora actual es ${hours}:${minutes < 10 ? '0' + minutes : minutes}.`;
      }
  
      // Analizar el mensaje para determinar el tipo
      for (const [type, keywords] of Object.entries(keywordSets)) {
        if (keywords.some(keyword => normalizeMessage.includes(keyword))) {
          return predefinedReplies[type][Math.floor(Math.random() * predefinedReplies[type].length)];
        }
      }
  
      // Respuesta predeterminada si no se encuentra coincidencia
      return predefinedReplies.default[Math.floor(Math.random() * predefinedReplies.default.length)];
  
    } catch (error) {
      // Respuesta rápida en caso de error
      console.error('Error en getAIResponse:', error);
      return "Lo siento, hubo un error al procesar tu mensaje. ¿Podrías intentarlo de nuevo?";
    }
  }
  
  
  
  
  
  async function sendMessage() {
    const message = userInput.value.trim();
    if (!message) return;
  
    addMessage(message, true);
    userInput.value = '';
  
    // Show typing indicator
    const typingDiv = document.createElement('div');
    typingDiv.className = 'message bot-message';
    typingDiv.textContent = 'Escribiendo...';
    chatMessages.appendChild(typingDiv);
  
    // Get AI response
    const response = await getAIResponse(message);
    chatMessages.removeChild(typingDiv);
    addMessage(response);
  }
  
  function handleKeyPress(event) {
    if (event.key === 'Enter') {
      sendMessage();
    }
  }
  
  // Add bounce animation to chat button periodically
  setInterval(() => {
    chatButton.classList.add('bounce');
    setTimeout(() => chatButton.classList.remove('bounce'), 2000);
  }, 10000);
