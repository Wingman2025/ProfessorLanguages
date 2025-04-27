document.addEventListener("DOMContentLoaded", () => {
  const nextBtn = document.getElementById("next-word");
  const wordEl = document.getElementById("word");
  const phraseForm = document.getElementById("phrase-form");

  nextBtn.addEventListener("click", async () => {
    const res = await fetch("/api/hot_potato");
    const data = await res.json();
    wordEl.textContent = data.result;
    phraseForm.classList.remove("d-none");
  });
});
