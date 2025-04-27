document.addEventListener("DOMContentLoaded", () => {
  const genBtn = document.getElementById("gen-topic");
  const topicEl = document.getElementById("topic");
  const notesForm = document.getElementById("notes-form");
  genBtn.addEventListener("click", async () => {
    const res = await fetch("/api/one_minute");
    const data = await res.json();
    topicEl.textContent = data.result;
    notesForm.classList.remove("d-none");
  });

  const startBtn = document.getElementById("start");
  const timerEl = document.getElementById("timer");
  let interval;
  startBtn.addEventListener("click", () => {
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
});