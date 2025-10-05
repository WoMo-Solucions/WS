document.getElementById('ping').addEventListener('click', async () => {
  const out = document.getElementById('out');
  const base = (window.CONFIG && window.CONFIG.BACKEND_URL) ? window.CONFIG.BACKEND_URL : '';
  if (!base) {
    out.textContent = 'Falta configurar BACKEND_URL en config.js';
    return;
  }
  try {
    const r = await fetch(`${base}/health`, { mode: 'cors' });
    const j = await r.json();
    out.textContent = JSON.stringify(j, null, 2);
  } catch (e) {
    out.textContent = `No se pudo conectar a ${base}/health`;
  }
});
