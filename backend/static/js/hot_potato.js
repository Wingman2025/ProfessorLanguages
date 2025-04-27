const nextBtn = document.getElementById("next-word");
const wordEl = document.getElementById("word");
const phraseForm = document.getElementById("phrase-form");

nextBtn.onclick = async () => {
  const res = await fetch('/api/hot_potato/word');
  const { word } = await res.json();
  wordEl.textContent = word;
  phraseForm.classList.remove('d-none');
};
