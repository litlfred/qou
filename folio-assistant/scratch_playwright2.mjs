import fs from 'fs';
const TAU = 2 * Math.PI;
const SQRT5 = Math.sqrt(5);

const BETAS = [
  a => Math.PI - 3 * a,
  a => (Math.PI + a) / 3,
  a => (3 * Math.PI + a) / 3,
  a => (5 * Math.PI + a) / 3,
];

function qInt(n, q) {
  if (Math.abs(1 - q) < 1e-10) return n;
  return (1 - Math.pow(q, n)) / (1 - q);
}

function qFact(n, q) {
  let f = 1;
  for (let k = 1; k <= n; k++) f *= qInt(k, q);
  return f;
}

function expQ(x, q, N) {
  let sum = 1, xn = 1;
  for (let n = 1; n <= N; n++) {
    xn *= x;
    const qf = qFact(n, q);
    if (Math.abs(qf) < 1e-15) break;
    const t = xn / qf;
    sum += t;
    if (n > 6 && Math.abs(t) < 1e-14 * (1 + Math.abs(sum))) break;
  }
  return sum;
}

function lnQ(x, q, N) {
  const xc = Math.min(Math.abs(x), 1.8) * Math.sign(x + 1e-30);
  let sum = 0, xn = 1;
  for (let n = 1; n <= N; n++) {
    xn *= xc;
    const qn = qInt(n, q);
    if (Math.abs(qn) < 1e-15) break;
    const t = Math.pow(-1, n + 1) * xn / qn;
    sum += t;
    if (n > 8 && Math.abs(t) < 1e-13 * (1 + Math.abs(sum))) break;
  }
  return sum;
}

function cosQ(x, q, N) {
  let sum = 1, xn = 1, x2 = x * x;
  for (let n = 1; n <= N; n++) {
    xn *= -x2;
    const qf = qFact(2 * n, q);
    if (Math.abs(qf) < 1e-15) break;
    const t = xn / qf;
    sum += t;
    if (n > 4 && Math.abs(t) < 1e-14 * (1 + Math.abs(sum))) break;
  }
  return sum;
}

function sinQ(x, q, N) {
  let sum = x, xn = x, x2 = x * x;
  for (let n = 1; n <= N; n++) {
    xn *= -x2;
    const qf = qFact(2 * n + 1, q);
    if (Math.abs(qf) < 1e-15) break;
    const t = xn / qf;
    sum += t;
    if (n > 4 && Math.abs(t) < 1e-14 * (1 + Math.abs(sum))) break;
  }
  return sum;
}

const MAX_G = 45;
function growthFactors(r, N) {
  const q  = Math.exp(-r);
  const lv = lnQ(r, q, N);
  const ev = expQ(r, q, N);
  const cq = cosQ(r, q, N);
  const g1 = Math.abs(lv) < 1e-9 ? MAX_G : Math.max(-MAX_G, Math.min(MAX_G, 1 / lv));
  const g2 = Math.max(-MAX_G, Math.min(MAX_G, ev - 1));
  const th = (Math.PI / 2) * Math.exp(-r);
  return { q, g1, g2, th, cq, lv, ev };
}

function wk(xs, k) {
  let re = 0, im = 0;
  for (let j = 0; j < 5; j++) {
    const a = TAU * k * j / 5;
    re += xs[j] * Math.cos(a);
    im += xs[j] * Math.sin(a);
  }
  return { re: re / SQRT5, im: im / SQRT5 };
}

function bringXj(r, alpha, beta, q, N) {
  const xs = new Array(5);
  for (let j = 0; j < 5; j++)
    xs[j] = (2 * r / SQRT5) * (
      cosQ(alpha - TAU * j / 5,     q, N) +
      cosQ(beta  - TAU * 2 * j / 5, q, N)
    );
  return xs;
}

function point3D(r, alpha, b, gf, N) {
  const beta    = BETAS[b](alpha);
  const resolved = gf || growthFactors(r, N);
  const { g1, g2, th, q } = resolved;
  const xs = bringXj(r, alpha, beta, q, N);

  const W1 = wk(xs, 1);
  const W2 = wk(xs, 2);
  const W3 = wk(xs, 3);

  W1.im += 1.0;
  W2.im += 1.0;
  W3.im += 1.0;

  const p_i = g1 * W1.re;
  const p_j = g2 * (W2.re + W3.im);
  const p_k = g2 * (W3.re - W2.im);

  return { x: p_i, y: p_j, z: p_k };
}

  const rmin   = 0.12;
  const rmax   = 2.5;
  const dr     = 0.14;
  const dz     = 0.09;
  const qN     = 18;

  const rs = [];
  for (let r = rmin; r <= rmax + 1e-9; r += dr) {
    rs.push(Math.min(r, rmax));
    if (rs.length > 700) break;
  }
  if (rs[rs.length - 1] < rmax - dr * .45) rs.push(rmax);

  const nA     = Math.max(6, Math.min(700, Math.round(TAU / dz)));
  const alphas = Array.from({ length: nA + 1 }, (_, i) => i * TAU / nA);
  const nR     = rs.length;
  const nAlpha = alphas.length;

  const GF = rs.map(r => growthFactors(r, qN));

  let nans = 0;
  for (let b = 0; b < 4; b++) {
    for (let i = 0; i < nR; i++) {
      const gf     = GF[i];
      for (let j = 0; j < nAlpha; j++) {
        const a   = alphas[j];
        const p   = point3D(rs[i], a, b, gf, qN);
        if (!isFinite(p.x) || !isFinite(p.y) || !isFinite(p.z)) {
          console.log(`NaN found!`);
          nans++;
        }
      }
    }
  }
  console.log(`Finished checking EXACT loop. NaNs: ${nans}`);
