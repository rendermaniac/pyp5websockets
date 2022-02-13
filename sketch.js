var websocket;

function setup() {
  createCanvas(400, 400);
  websocket = new WebSocket("ws://localhost:5678/");
  websocket.onmessage = drawSphere;
}

function drawSphere(message) {
  noStroke();
  fill(0, 255, 100);
  coords = JSON.parse(message.data)
  ellipse(coords[0], coords[1], 36, 36);
  console.log("got coords: " + coords[0] + " " + coords[1])
}
