const quizId = 1;
const socket = new WebSocket(`ws://${window.location.host}/ws/quiz/${quizId}/`);

socket.onmessage = (event) => {
    const data = JSON.parse(event.data);
    // Handle data recieved from the websocket
}