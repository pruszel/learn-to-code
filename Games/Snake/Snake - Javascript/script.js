var STEP  = 20; // distance between snake body parts
var SIZE  = 10;  // size of snake body
var SPEED = 1;  // how fast snake moves, from 1 - 10

var canvas = document.getElementById('snake');
var context = canvas.getContext('2d');

var snake = {
  x: canvas.width/2,
  y: canvas.height/2,

  direction: 'r',
  switchDirection: false,

  l: 2,
  body: [
    {'x': this.x - STEP, 'y': this.y},
    {'x': this.x - (STEP*2), 'y': this.y}
  ]
};

var apple = getApplePosition();



// The maximum is exclusive and the minimum is inclusive
function getRandom(min, max, inc) {
  return Math.floor(Math.random() * (max - min) / inc) * inc + min;
}

// Gets position for apple close but not too close to snake
function getApplePosition() {
  var x, y;
  do {
    x = getRandom(STEP, canvas.width - STEP, STEP);
    y = getRandom(STEP, canvas.height - STEP, STEP);
  } while(Math.abs(snake.x - x) <= 20 || Math.abs(snake.y - y) <= 20);

  return {'x': x, 'y': y};
}

// keeps track of animation frames for skipping to slow game down
var count;
var gameOver = false;
function mainLoop()
{
  requestAnimationFrame(mainLoop);

  // slow down animation
  if (++count < -SPEED-4+20) {
    return;
  }
  count = 0;
  
  // Update debug info
  var debug = document.getElementById('debug');
  debug.innerHTML  = "snake.x: "+snake.x+" snake.y: "+snake.y;
  debug.innerHTML += "<br>";
  debug.innerHTML += "apple.x: "+apple.x+" apple.y: "+apple.y; 


  var canvas = document.getElementById('snake');
  var context = canvas.getContext('2d');

  // Clear canvas
  context.clearRect(0, 0, canvas.width, canvas.height);

  // Draw apple
  context.fillStyle = "green";
  context.fillRect(apple.x, apple.y, SIZE, SIZE);
  context.fillStyle = "black";

  // Draw snake head
  context.fillRect(snake.x, snake.y, SIZE, SIZE);

  // Draw snake body parts
  for (var i=0; i < snake.l; i++) {
    var part = snake.body[i];
    context.fillRect(part.x, part.y, SIZE, SIZE);
  
    // Check if snake runs into itself
    if (snake.x == part.x && snake.y == part.y) {
      gameOver = true;
    }
  }

  if (gameOver) {
      drawEndScreen(context);
      return;
  }

  // Add body part for where he was
  snake.body.unshift({'x': snake.x, 'y': snake.y});

  // Check if snake eats apple
  if (snake.x == apple.x && snake.y == apple.y) {
    snake.l++;
    apple = getApplePosition();
  }
  // Remove tail body part
  else {
    snake.body.pop();
  }

  // Move snake head in direction
  switch(snake.direction) {
    case 'r':
      snake.x += STEP;
      break;
    case 'u':
      snake.y -= STEP;
      break;
    case 'l':
      snake.x -= STEP;
      break;
    case 'd':
      snake.y += STEP;
      break;
  }
  if (snake.switchDirection) {
    snake.switchDirection = false;
  }

  // Wrap snake around edges
  if (snake.x <= 0) {
    snake.x = canvas.width;
  }
  else if (snake.x >= canvas.width) {
    snake.x = 0;
  }
  if (snake.y <= 0) {
    snake.y = canvas.height;
  }
  else if (snake.y >= canvas.height) {
    snake.y = 0;
  }
}

// Snake controls
document.addEventListener('keydown', function(e) {
  // left arrow
  if(e.keyCode == 37 && snake.direction != 'r' && !snake.switchDirection) {
    snake.direction = 'l';
    snake.switchDirection = true;
  }
  // up arrow
  else if(e.keyCode == 38 && snake.direction != 'd' && !snake.switchDirection) {
    snake.direction = 'u';
    snake.switchDirection = true;
  }
  // right arrow
  else if(e.keyCode == 39 && snake.direction != 'l' && !snake.switchDirection) {
    snake.direction = 'r';
    snake.switchDirection = true;
  }
  // down arrow
  else if(e.keyCode == 40 && snake.direction != 'u' && !snake.switchDirection) {
    snake.direction = 'd';
    snake.switchDirection = true;
  }
});


function drawStartScreen(context) {
  context.font = "28px sans-serif";
  context.textAlign = "center";
  context.fillText('Click to Start', canvas.width/2, canvas.height/2);
}
drawStartScreen(context);

function drawEndScreen(context) {
  context.font = "28px sans-serif";
  context.textAlign = "center";
  context.fillText('Game Over', canvas.width/2, canvas.height/2);
}

// Start game by clicking on canvas
canvas.addEventListener('click', function startGame() {
  requestAnimationFrame(mainLoop);

  this.removeEventListener('click', startGame);
});
