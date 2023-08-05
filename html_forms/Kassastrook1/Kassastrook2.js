// Add event listeners to all input fields in the form
const inputElements = document.querySelectorAll('input[type="text"]');
const sumDisplay = document.getElementById("sumDisplay");
let sumValue = 0;

// Function to calculate and display the sum
function calculateSum() {
  let sum = 0;
  inputElements.forEach(input => {
    const amount = parseFloat(input.value);
    if (!isNaN(amount)) {
      sum += amount;
    }
  });
  sumValue = sum; // Optionally, update the sumValue dynamically.
  sumDisplay.textContent = `Sum: ${sum.toFixed(2)}`; // Display the sum with two decimal places
}

// Function to add the "filled" class to the input fields that have a value filled
function checkInput(input) {
  if (input.value.trim() !== "") {
    input.classList.add("filled");
  } else {
    input.classList.remove("filled");
  }
}

inputElements.forEach(input => {
  input.addEventListener('input', () => {
    checkInput(input); // Check if the input is filled on each input event
    calculateSum(); // Recalculate the sum when any input changes
  });
});

// Initial calculation when the page loads
calculateSum();
