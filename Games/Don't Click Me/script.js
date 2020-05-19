var $counter = document.querySelector('#js-counter');

var $clickBtn = document.querySelector('#js-click');
$clickBtn.onclick = clickHandler;

window.countdown_delay = 333;
window.countdown_accel = 1.28;

window.warmer = [2, 15, 25, 40, 60, 80, 100];

// Function called each time button is clicked
// also called again to go back down after MS_DELAY
function clickHandler()
{
  // cancel countdown timer
  clearInterval(window.countdownId);

  // Get current counter value
  var $counter = document.querySelector('#js-counter');
  var numClicks = parseInt($counter.innerHTML);

  // Reached end, WINNER!
  if (numClicks >= window.warmer[ window.warmer.length-1 ]) {
    $counter.classList.add('winner');

    $clickBtn = document.querySelector('#js-click');
    $clickBtn.classList.add('disabled');
    $clickBtn.innerHTML = 'You won!';

    $playAgain = document.querySelector('#js-playAgain');
    $playAgain.style.visibility = 'inherit';

    return;
  }

  // Add warmer CSS class
  var i = window.warmer.length - 2;
  for (i; i >= 0; i--) {
    if (numClicks >= window.warmer[i]) {
      $counter.classList.add('warmer'+(i+1));
      break;
    }
  }

  // Update counter value
  $counter.innerHTML = numClicks + 1;

  // set countdown timer
  window.countdownId = setInterval(countdown, countdown_delay - (numClicks * countdown_accel));
}

function countdown()
{
  // Get current counter value
  var $counter = document.querySelector('#js-counter');
  var numClicks = parseInt($counter.innerHTML);

  // remove warmer CSS class
  var i = window.warmer.length - 2;
  for (i; i >= 0; i--) {
    if (numClicks < window.warmer[i]) {
      $counter.classList.remove('warmer'+(i+1));
    }
  }
  
  // Stop at 0 and finsh
  if (numClicks == 0 || numClicks == window.warmer[window.warmer.length - 1]) {
    clearInterval(window.countdownId);
    return;
  }

  // Update counter value
  $counter.innerHTML = numClicks - 1;
}
