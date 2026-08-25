#!/usr/bin/env bun
/**
 * Alexander polynomial of a braid closure, from the reduced Burau matrix.
 *
 * The closure-component check in `braid-word-closure-check.ts` cannot see a
 * word that closes to the WRONG KNOT while still closing to a knot. The case
 * that motivated this: a block stated the figure-eight as the commutator
 * `s0 s1^-1 s0^-1 s1`, whose closure has one component — and is the unknot.
 * Component count passes it; the Alexander polynomial does not.
 *
 * Exact integer Laurent arithmetic throughout — no floats, per the repo's
 * precision discipline. The polynomial is computed as
 *
 *     det(Burau_reduced(b) - I) * (t - 1) = Delta(t) * (t^n - 1)
 *
 * and normalised by stripping units (+- t^k) and fixing the sign, so it can
 * be compared against a table of known values.
 *
 * Caveat worth stating: the Alexander polynomial does not detect the unknot
 * in general. It is decisive for everything this corpus names, and a
 * mismatch is always a real disagreement; a match is strong evidence, not
 * proof.
 *
 * USE IT ON A WORD YOU NAME, NOT AS A CORPUS SCANNER. A line-level sweep
 * over `content/` was built and thrown away: at line granularity nothing
 * distinguishes a braid word from stray generator symbols, so a proof block
 * that *constructs the matrices* of sigma_1 and sigma_2 reads as two
 * one-letter words, and a file mixing 0-based and 1-based indexing defeats
 * any per-file convention guess. Two successive versions reported 58 and 61
 * disagreements out of 76 lines; every one inspected was the scanner's
 * fault, not the corpus's. The arithmetic here is exact and was decisive
 * when pointed at a specific claim — that is the supported use.
 *
 * @module content/pipeline/braid-alexander
 */

/** Laurent polynomial over Z: exponent -> coefficient. */
export type Lau = Map<number, bigint>;

export const lau = (pairs: [number, bigint][] = []): Lau => {
  const m = new Map<number, bigint>();
  for (const [e, c] of pairs) if (c !== 0n) m.set(e, (m.get(e) ?? 0n) + c);
  for (const [e, c] of [...m]) if (c === 0n) m.delete(e);
  return m;
};
export const ZERO = (): Lau => new Map();
export const ONE = (): Lau => lau([[0, 1n]]);

export function add(a: Lau, b: Lau): Lau {
  const m = new Map(a);
  for (const [e, c] of b) {
    const v = (m.get(e) ?? 0n) + c;
    if (v === 0n) m.delete(e); else m.set(e, v);
  }
  return m;
}
export function neg(a: Lau): Lau {
  const m = new Map<number, bigint>();
  for (const [e, c] of a) m.set(e, -c);
  return m;
}
export function mul(a: Lau, b: Lau): Lau {
  const m = new Map<number, bigint>();
  for (const [e1, c1] of a) for (const [e2, c2] of b) {
    const e = e1 + e2, v = (m.get(e) ?? 0n) + c1 * c2;
    if (v === 0n) m.delete(e); else m.set(e, v);
  }
  return m;
}
export const isZero = (a: Lau) => a.size === 0;

/** Exact division; returns null when b does not divide a. */
export function div(a: Lau, b: Lau): Lau | null {
  if (isZero(b)) return null;
  let rem = new Map(a);
  const q: Lau = new Map();
  const bHi = Math.max(...b.keys()), bLead = b.get(bHi)!;
  let guard = 0;
  while (!isZero(rem)) {
    if (++guard > 10000) return null;
    const rHi = Math.max(...rem.keys()), rLead = rem.get(rHi)!;
    if (rLead % bLead !== 0n) return null;
    const term = lau([[rHi - bHi, rLead / bLead]]);
    q.set(rHi - bHi, rLead / bLead);
    rem = add(rem, neg(mul(term, b)));
    if (!isZero(rem) && Math.max(...rem.keys()) >= rHi) return null;
  }
  return q;
}

/** Strip units: shift to exponent 0 and force a positive leading coefficient. */
export function normalise(a: Lau): Lau {
  if (isZero(a)) return ZERO();
  const lo = Math.min(...a.keys());
  let out = lau([...a].map(([e, c]) => [e - lo, c] as [number, bigint]));
  const hi = Math.max(...out.keys());
  if (out.get(hi)! < 0n) out = neg(out);
  // canonical under t -> 1/t as well (Alexander is defined up to that)
  const rev = lau([...out].map(([e, c]) => [hi - e, c] as [number, bigint]));
  const revNorm = rev.get(Math.max(...rev.keys()))! < 0n ? neg(rev) : rev;
  return str(out) <= str(revNorm) ? out : revNorm;
}
export const str = (a: Lau): string =>
  isZero(a) ? "0" : [...a].sort((x, y) => x[0] - y[0]).map(([e, c]) => `${c}t^${e}`).join(" + ");

/** Reduced Burau matrix of a braid word on `n` strands (generators 0-based). */
export function burau(word: number[], signs: number[], n: number): Lau[][] {
  const d = n - 1;
  let M: Lau[][] = Array.from({ length: d }, (_, i) =>
    Array.from({ length: d }, (_, j) => (i === j ? ONE() : ZERO())));
  const gen = (i: number, inv: boolean): Lau[][] => {
    const g: Lau[][] = Array.from({ length: d }, (_, r) =>
      Array.from({ length: d }, (_, c) => (r === c ? ONE() : ZERO())));
    const t = lau([[1, 1n]]), mt = lau([[1, -1n]]);
    if (!inv) {
      g[i][i] = mt;
      if (i > 0) g[i][i - 1] = ONE();
      if (i < d - 1) g[i][i + 1] = t;
    } else {
      const ti = lau([[-1, 1n]]), mti = lau([[-1, -1n]]);
      g[i][i] = mti;
      if (i > 0) g[i][i - 1] = ti;
      if (i < d - 1) g[i][i + 1] = ONE();
    }
    return g;
  };
  const matmul = (A: Lau[][], B: Lau[][]): Lau[][] =>
    A.map((row) => B[0].map((_, j) => row.reduce((s, a, k) => add(s, mul(a, B[k][j])), ZERO())));
  word.forEach((g, k) => { M = matmul(M, gen(g, signs[k] < 0)); });
  return M;
}

/** Determinant by cofactor expansion (matrices here are tiny). */
export function det(M: Lau[][]): Lau {
  const n = M.length;
  if (n === 0) return ONE();
  if (n === 1) return M[0][0];
  let out = ZERO();
  for (let j = 0; j < n; j++) {
    const minor = M.slice(1).map((row) => row.filter((_, c) => c !== j));
    const term = mul(M[0][j], det(minor));
    out = add(out, j % 2 === 0 ? term : neg(term));
  }
  return out;
}

/** Alexander polynomial of the closure, normalised; null if it does not divide. */
export function alexander(word: number[], signs: number[], n: number): Lau | null {
  const d = n - 1;
  const B = burau(word, signs, n);
  const BmI: Lau[][] = B.map((row, i) => row.map((x, j) => (i === j ? add(x, neg(ONE())) : x)));
  const D = det(BmI);
  if (isZero(D)) return ZERO();
  // det(B - I) * (t - 1) = Delta(t) * (t^n - 1)
  const num = mul(D, lau([[1, 1n], [0, -1n]]));
  const q = div(num, lau([[n, 1n], [0, -1n]]));
  return q ? normalise(q) : null;
}

/** Alexander polynomials of what this corpus names, normalised. */
export const KNOWN: Record<string, string> = {
  unknot: str(normalise(ONE())),
  "3_1": str(normalise(lau([[0, 1n], [1, -1n], [2, 1n]]))),
  "4_1": str(normalise(lau([[0, 1n], [1, -3n], [2, 1n]]))),
  "5_1": str(normalise(lau([[0, 1n], [1, -1n], [2, 1n], [3, -1n], [4, 1n]]))),
  "7_1": str(normalise(lau([[0, 1n], [1, -1n], [2, 1n], [3, -1n], [4, 1n], [5, -1n], [6, 1n]]))),
};

/** Parse a signed braid word, honouring group exponents.
 *
 * `(\sigma_1\sigma_2^{-1})^2` is TWO copies of the group, and a parser that
 * ignores the `)^2` reads it as one — which reports every correct
 * figure-eight in the corpus as an unknot. That false-positive rate (58 of
 * 76 lines) is what caught the bug; a detector this noisy is a bug report
 * about itself, not a finding list.
 *
 * Returns null when the word is not fully explicit, e.g. `4_1 = w^2` where
 * `w` was bound earlier in the prose. Guessing there is how the same false
 * positive comes back. */
export function parseWord(s: string): [number[], number[]] | null {
  let x = s.replace(/\s|\\!|\\,/g, "");
  const out: number[] = [], sg: number[] = [];
  while (x.length) {
    let m = /^\(([^()]*)\)\^\{?(-?\d+)\}?/.exec(x);
    if (m) {
      const inner = parseWord(m[1]);
      if (!inner) return null;
      const k = Number(m[2]);
      for (let i = 0; i < Math.abs(k); i++) {
        if (k > 0) { out.push(...inner[0]); sg.push(...inner[1]); }
        else {
          for (let j = inner[0].length - 1; j >= 0; j--) { out.push(inner[0][j]); sg.push(-inner[1][j]); }
        }
      }
      x = x.slice(m[0].length); continue;
    }
    m = /^\\sigma_\{?(\d+)\}?\^\{?(-?\d+)\}?/.exec(x);
    if (m) {
      const k = Number(m[2]);
      for (let i = 0; i < Math.abs(k); i++) { out.push(Number(m[1])); sg.push(k < 0 ? -1 : 1); }
      x = x.slice(m[0].length); continue;
    }
    m = /^\\sigma_\{?(\d+)\}?/.exec(x);
    if (m) { out.push(Number(m[1])); sg.push(1); x = x.slice(m[0].length); continue; }
    return null;                       // a symbol, an ellipsis, anything else
  }
  return out.length ? [out, sg] : null;
}

if (import.meta.main) {
  const parse = (s: string): [number[], number[]] => parseWord(s) ?? [[], []];
  const arg = process.argv[2] ?? "";
  const n = Number(process.argv[3] ?? 3);
  const [w, sg] = parse(arg);
  const a = alexander(w, sg, n);
  console.log(`word: ${arg}\nstrands: ${n}\nAlexander: ${a ? str(a) : "(no exact division)"}`);
  for (const [k, v] of Object.entries(KNOWN)) if (a && str(a) === v) console.log(`  matches: ${k}`);
}
