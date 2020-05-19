// Get form HTML element from DOM
var form = document.querySelector("form");

// Add event handler to form submit event
form.onsubmit = function(event)
{
  // Prevent reloading page
  event.preventDefault();

  // Get num1
  var $num1 = document.querySelector("#num1");
  var num1 = parseFloat($num1.value);

  // Get num2
  var $num2 = document.querySelector("#num2");
  var num2 = parseFloat($num2.value);

  // Setup result variable
  var result = 0;

  // Get selected operation
  var $operation = document.querySelector("input[name='operation']:checked");
  var operation = $operation.value;
  switch(operation) {
    case "+":
      result = num1 + num2;
      break;
    case "-":
      result = num1 - num2;
      break;
    case "*":
      result = num1 * num2;
      break;
    case "/":
      result = num1 / num2;
      break;
    default:
  }

  // Display result
  var $result = document.querySelector("#result");
  $result.innerHTML = result;
  document.querySelector(".result-text").style.display = "inline";
}
