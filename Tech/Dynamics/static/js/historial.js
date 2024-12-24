function renderActivities(filteredActivities = activities) {
  const activitiesContainer = document.getElementById('activities');
  activitiesContainer.innerHTML = filteredActivities.map(activity => createActivityCard(activity)).join('');
}
function sortActivities(direction) {
  const sorted = [...activities].sort((a, b) => {
    const dateA = new Date(a.fecha);
    const dateB = new Date(b.fecha);
    return direction === 'asc' ? dateA - dateB : dateB - dateA;
  });
  renderActivities(sorted);
}
function filterByDate(date) {
  if (!date) {
    renderActivities();
    return;
  }
  const filtered = activities.filter(activity => {
    const activityDate = new Date(activity.fecha).toISOString().split('T')[0];
    return activityDate === date;
  });
  renderActivities(filtered);
}
document.querySelector('.search-bar').addEventListener('input', e => {
  const searchTerm = e.target.value.toLowerCase();
  const filtered = activities.filter(activity => activity.solicitud.toLowerCase().includes(searchTerm) || activity.descripcion.toLowerCase().includes(searchTerm));
  renderActivities(filtered);
});
function openChat(serverName) {
  const chatModal = document.getElementById('chatModal');
  chatModal.style.display = 'block';
  document.getElementById('chatMessages').innerHTML = `<p style="text-align: center">Conectado con ${serverName}</p>`;
}
function closeChat() {
  document.getElementById('chatModal').style.display = 'none';
}
function sendMessage() {
  const input = document.getElementById('messageInput');
  const message = input.value.trim();
  if (message) {
    const messagesContainer = document.getElementById('chatMessages');
    messagesContainer.innerHTML += `
      <p style="background: #e3f2fd; padding: 8px; border-radius: 8px; margin: 5px;">
        <strong>Tú:</strong> ${message}
      </p>
    `;
    input.value = '';
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
  }
}
document.querySelectorAll('.star').forEach(star => {
  star.addEventListener('click', e => {
    const rating = e.target.dataset.rating;
    document.querySelectorAll('.star').forEach(s => {
      s.classList.remove('active');
      if (s.dataset.rating <= rating) {
        s.classList.add('active');
      }
    });
  });
});
function reportServer(serverName) {
  openReportModal(serverName);
}
function openReportModal(serverName) {
  const modal = document.getElementById('reportModal');
  modal.style.display = 'flex';
  modal.dataset.serverName = serverName;
}
function closeReportModal() {
  document.getElementById('reportModal').style.display = 'none';
  document.getElementById('reportForm').reset();
  document.getElementById('fileList').innerHTML = '';
}
function handleFiles(files) {
  const fileList = document.getElementById('fileList');
  fileList.innerHTML = '';
  Array.from(files).forEach(file => {
    const fileItem = document.createElement('div');
    fileItem.textContent = `📄 ${file.name}`;
    fileList.appendChild(fileItem);
  });
}
function submitReport(event) {
  event.preventDefault();
  const serverName = document.getElementById('reportModal').dataset.serverName;
  const description = document.getElementById('reportDescription').value;
  const files = document.getElementById('reportFiles').files;
  console.log('Report submitted:', {
    serverName,
    description,
    files: Array.from(files).map(f => f.name)
  });
  showNotification('Reporte enviado exitosamente');
  closeReportModal();
}
function showNotification(message) {
  const notification = document.createElement('div');
  notification.className = 'notification';
  notification.textContent = message;
  document.body.appendChild(notification);
  setTimeout(() => {
    document.body.removeChild(notification);
  }, 3000);
}
renderActivities();

























