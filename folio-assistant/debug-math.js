const rmin=0.25, rmax=3.2, dr=0.08, dzeta=0.15, qN=12, mode='sp1';

function qInt(n, q) {
  if (Math.abs(q - 1) < 1e-9) return n;
  return (1 - Math.pow(q, n)) / (1 - q);
}

function qFact(n, q) {
  let f = 1;
  for (let k = 1; k <= n; k++) f *= qInt(k, q);
  return f;
}

function expQ(x, q, N) {
  let sum = 1, xn = x;
  for (let n = 1; n <= N; n++) {
    const qf = qFact(n, q);
    if (Math.abs(qf) < 1e-15) break;
    const t = xn / qf;
    if (!isFinite(t)) break;
    sum += t;
    if (n > 4 && Math.abs(t) < 1e-14 * (1 + Math.abs(sum))) break;
    xn *= x;
  }
  return sum;
}

function lnQ(x, q, N) {
  let sum = 0, xn = x;
  for (let n = 1; n <= N; n++) {
    const qn = qInt(n, q);
    if (Math.abs(qn) < 1e-15) break;
    const t = xn / (n * qn);
    if (!isFinite(t)) break;
    sum += (n % 2 === 1 ? t : -t);
    if (n > 4 && Math.abs(t) < 1e-14 * (1 + Math.abs(sum))) break;
    xn *= x;
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
    if (!isFinite(t)) break;
    sum += t;
    if (n > 4 && Math.abs(t) < 1e-14 * (1 + Math.abs(sum))) break;
  }
  return sum;
}

function bringXj(z, j, q, N) {
  const x = Math.PI * z * z;
  const t1 = Math.pow(q, j/2) * cosQ(x, q, N);
  const t2 = Math.pow(q, -j/2) * lnQ(x, q, N);
  return t1 + t2;
}

function point3D(r, a, b, GF, qN) {
  const q = Math.exp(-r / 2);
  const z1 = Math.cos(a) * Math.cos(b);
  const z2 = Math.sin(a) * Math.cos(b);
  const z3 = Math.sin(b);

  const x1 = bringXj(z1, 1, q, qN);
  const y1 = bringXj(z2, 2, q, qN);
  const z_coord = bringXj(z3, 3, q, qN);

  return {x: x1, y: y1, z: z_coord};
}

console.time('math');
let nR = Math.floor((rmax - rmin) / dr);
let nAlpha = Math.floor(2 * Math.PI / dzeta);
let count = 0;
for (let r=0; r<=nR; r++) {
  for (let a=0; a<=nAlpha; a++) {
    point3D(rmin + r*dr, a*dzeta, 1.0, null, qN);
    count++;
  }
}
console.timeEnd('math');
console.log('points:', count);
