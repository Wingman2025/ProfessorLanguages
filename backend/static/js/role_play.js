const genBtn = document.getElementById("gen-scenario");
const scenarioEl = document.getElementById("scenario");

genBtn.onclick = async () => {
  const res = await fetch('/api/role_play/scenario');
  const { scenario } = await res.json();
  scenarioEl.textContent = scenario;
};
