document.addEventListener('click', (e) => {
  const btn = e.target.closest('.btn-conocer');
  if (!btn) return;

  const nombre = btn.dataset.animal;
  const info   = btn.dataset.info;
  const desc   = btn.dataset.desc;

  alert(`Conocer a ${nombre}: ${info}\n${desc}`);
});