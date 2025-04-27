// Debug: ensure script loaded
console.log('one_minute.js loaded');

const genBtn = document.getElementById("gen-topic");
const topicEl = document.getElementById("topic");
const notesForm = document.getElementById("notes-form");
if (genBtn) {
  genBtn.addEventListener("click", async () => {
    console.log('gen-topic clicked');
    try {
      const res = await fetch("/api/one_minute");
      const data = await res.json();
      topicEl.textContent = data.result;
      notesForm.classList.remove("d-none");
    } catch (e) {
      console.error(e);
    }
  });
} else {
  console.warn('gen-topic button not found');
}

const startBtn = document.getElementById("start");
const timerEl = document.getElementById("timer");
let interval;
if (startBtn) {
  startBtn.addEventListener("click", () => {
    console.log('start clicked');
    let time = 60;
    timerEl.textContent = time;
    startBtn.disabled = true;
    interval = setInterval(() => {
      time -= 1;
      timerEl.textContent = time;
      if (time <= 0) {
        clearInterval(interval);
        startBtn.disabled = false;
      }
    }, 1000);
  });
} else {
  console.warn('start button not found');
}