console.log("Todos app.js");
// JavaScript code to handle the timer functionality
let day = 1;
let seconds = 60;
let minutes = 60;
let hour = 24
const timerDisplay = document.getElementById("timer");
const interval = setInterval(() => {
  seconds--;
  if (seconds === 0) {
    seconds = 60;
    minutes--;
    timerDisplay.textContent = "<b>Times Up</b>"
  }

  if (minutes === 0) {
    minutes = 60;
    hour--;
  }

  if (hour === 0) {
    day--;
  }

  if (day === 0) {
    console.log("time completed");
    timerDisplay.textContent = "<b>Times Up</b>"
  }

  timerDisplay.textContent = `Timer: ${hour}:${minutes}:${seconds}`;
}, 1000);

timerDisplay.addEventListener("click", () => {
  console.log("interval", interval);
  clearInterval(interval);
});
