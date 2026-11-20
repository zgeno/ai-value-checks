// Fails if any [data-fit] block's text overflows its box (the design gate checks width only).
// Usage: node check_fit.cjs <page.html>
const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  await p.goto('file://' + path.resolve(process.argv[2])); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300);
  const bad = await p.evaluate(() => [...document.querySelectorAll('[data-fit]')].map((e, i) => [i, e.scrollHeight, e.clientHeight, e.textContent.slice(0, 40)]).filter(x => x[1] > x[2] + 1));
  const dek = await p.evaluate(() => { const d = document.querySelector('.dek'); const f = [...document.querySelectorAll('[data-fit]')]; if (!d || !f.length) return null; const t = Math.min(...f.map(e => e.getBoundingClientRect().top)); return [Math.round(d.getBoundingClientRect().bottom), Math.round(t)]; });
  if (dek && dek[0] > dek[1] - 30) bad.push(['dek too close to the diagram', dek[0], dek[1] - 30]);
  await b.close(); console.log(bad.length ? 'FIT FAIL ' + JSON.stringify(bad) : 'FIT PASS'); if (bad.length) process.exit(1);
})();
