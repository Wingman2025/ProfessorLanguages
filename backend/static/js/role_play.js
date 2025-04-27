document.addEventListener("DOMContentLoaded", () => {
  const genBtn = document.getElementById("gen-scenario");
  const scenarioEl = document.getElementById("scenario");
  genBtn.addEventListener("click", async () => {
    const res = await fetch("/api/role_play");
    const data = await res.json();
    scenarioEl.textContent = data.result;
  });
});
