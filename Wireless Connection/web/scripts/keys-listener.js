const serverSocket = new WebSocket('ws://127.0.0.1:25563');

serverSocket.onopen = function() {
  console.log('Web> WebSocket connected');
};

let keyState = {
  'w': 0,
  'a': 0,
  's': 0,
  'd': 0
};

function handleKeyDown(event) {
  const key = event.key.toLowerCase();
  if (key in keyState) {
    keyState[key] = 1;
    serverSocket.send(JSON.stringify({ key: key, status: 1 }));
  }
}

function handleKeyUp(event) {
  const key = event.key.toLowerCase();
  if (key in keyState) {
    keyState[key] = 0;
    serverSocket.send(JSON.stringify({ key: key, status: 0 }));
  }
}

document.addEventListener('keydown', handleKeyDown);
document.addEventListener('keyup', handleKeyUp);
