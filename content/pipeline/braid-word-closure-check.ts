#!/usr/bin/env bun
/**
 * Check braid words in content tables against the columns beside them.
 *
 * A table row that gives a braid word usually also gives the knot's crossing
 * number, its component count, or a T(p,q) symbol. Those columns are three
 * independent statements about the same object, so they check each other:
 *
 *   - letters in the word      must equal the declared Crossings
 *   - cycles of the closure    must equal the declared Components
 *   - a T(p,q) symbol          must be a word on p strands, i.e. in B_p
 *
 * This exists because a whole family of rows was wrong in one direction:
 * torus words written with p generators instead of p-1, so T(2,n) appeared
 * in B_3 and T(3,n) in B_4. Every such row still had the right crossing
 * number in its own table, which is what makes the check possible.
 *
 * Component count alone is NOT sufficient: `(s0 s1 s2)^5` in B_4 closes to a
 * knot, one component, and is caught only by its 15 letters against a
 * declared 10 crossings. Both tests are needed.
 *
 *   bun run content/pipeline/braid-word-closure-check.ts [path ...]
 *
 * @module content/pipeline/braid-word-closure-check
 */
import { readFileSync } from "node:fs";
import { globSync } from "node:fs";

interface Row { file: string; line: number; word: string; strands?: number;
                crossings?: number; components?: number; symbol?: string }

/** Expand a word like `(\sigma_0\sigma_1)^4\sigma_0` into generator indices. */
export function expand(tex: string): number[] | null {
  let s = tex.replace(/\s|\\!|\\,|\{|\}/g, "");
  const out: number[] = [];
  // repeatedly consume  (group)^k  |  \sigma_i^k  |  \sigma_i
  while (s.length) {
    let m = /^\(([^()]*)\)\^(-?\d+)/.exec(s);
    if (m) {
      const inner = expand(m[1]);
      if (!inner) return null;
      const k = Math.abs(Number(m[2]));
      for (let i = 0; i < k; i++) out.push(...inner);
      s = s.slice(m[0].length); continue;
    }
    m = /^\\sigma_(\d+)\^(?:\{)?(-?\d+)(?:\})?/.exec(s);
    if (m) {
      const k = Math.abs(Number(m[2]));
      for (let i = 0; i < k; i++) out.push(Number(m[1]));
      s = s.slice(m[0].length); continue;
    }
    m = /^\\sigma_(\d+)(?:\^\{?-1\}?)?/.exec(s);
    if (m) { out.push(Number(m[1])); s = s.slice(m[0].length); continue; }
    m = /^\\mathbf1|^1/.exec(s);
    if (m) { s = s.slice(m[0].length); continue; }
    return null;                       // anything else: not a plain braid word
  }
  return out;
}

/** Cycles of the closure permutation of a word on `n` strands. */
export function components(word: number[], n: number): number {
  const p = [...Array(n).keys()];
  for (const i of word) { const t = p[i]; p[i] = p[i + 1]; p[i + 1] = t; }
  const seen = new Set<number>(); let c = 0;
  for (let s = 0; s < n; s++) {
    if (seen.has(s)) continue;
    c++; let x = s;
    while (!seen.has(x)) { seen.add(x); x = p[x]; }
  }
  return c;
}

const num = (c: string) => { const m = /\$?(\d+)\$?/.exec(c.trim()); return m ? Number(m[1]) : undefined; };

function rowsOf(file: string): Row[] {
  const lines = readFileSync(file, "utf8").split("\n");
  const rows: Row[] = [];
  let head: string[] = [];
  lines.forEach((ln, i) => {
    if (!ln.trim().startsWith("|")) { head = []; return; }
    const cells = ln.split("|").slice(1, -1).map((c) => c.trim());
    if (cells.every((c) => /^:?-+:?$/.test(c))) return;
    if (!head.length) { head = cells.map((c) => c.toLowerCase()); return; }
    const at = (name: string) => { const k = head.findIndex((h) => h.includes(name)); return k < 0 ? undefined : cells[k]; };
    const wcell = at("braid");
    if (!wcell) return;
    const wm = /\$([^$]*)\$/.exec(wcell);
    if (!wm) return;
    const bm = /B_\{?(\d+)/.exec(wcell);
    const sym = (at("symbol") ?? at("knot") ?? at("link") ?? "");
    const tm = /T[_(]?\{?\(?(\d+),\s*(\d+)/.exec(sym);
    rows.push({ file, line: i + 1, word: wm[1].split("\\in")[0],
      strands: bm ? Number(bm[1]) : undefined,
      crossings: num(at("crossing") ?? ""), components: num(at("component") ?? ""),
      symbol: tm ? `T(${tm[1]},${tm[2]})` : undefined });
  });
  return rows;
}

/** Generator indices are 0-based in some chapters and 1-based in others.
 * A file that never writes `\sigma_0` is read as 1-based and shifted down,
 * so `\sigma_1^3` is a 2-strand word there and a 3-strand word elsewhere.
 * The convention is a real divergence in this corpus, not an artefact. */
function zeroBased(file: string): boolean {
  return /\\sigma_0/.test(readFileSync(file, "utf8"));
}

/** True when one file uses both conventions, so no single reading is right.
 * `fundamental-knots-operator-basis` does this inside a single table: its
 * knot rows are 1-based (`\sigma_1^3` for the trefoil, a 2-strand word)
 * while its photon row expands the 0-based H_3(q) basis
 * (`\varphi_0\sigma_0 + \varphi_1\sigma_1`). The same glyph is the first
 * generator in one row and the second in the next. */
function mixedIndexing(file: string): boolean {
  const s = readFileSync(file, "utf8");
  if (!/\\sigma_0/.test(s)) return false;
  // a T(p,q) row whose word's lowest index is 1 reads as 1-based
  return rowsOf(file).some((r) => {
    if (!r.symbol) return false;
    const w = expand(r.word);
    return !!w && w.length > 0 && Math.min(...w) >= 1
      && Number(r.symbol.slice(2).split(",")[0]) === Math.max(...w) + 1;
  });
}

const targets = process.argv.slice(2).length
  ? process.argv.slice(2)
  : globSync("content/**/*.md");
let bad = 0, checked = 0;
for (const f of targets) {
  if (mixedIndexing(f)) {
    bad++;
    console.log(`${f}`);
    console.log("    mixed generator indexing in one file: knot rows read as 1-based, "
      + "H_n(q) basis rows as 0-based, so the same sigma index means two things");
    continue;
  }
  const shift = zeroBased(f) ? 0 : 1;
  for (const r of rowsOf(f)) {
    const w0 = expand(r.word);
    if (!w0) continue;
    const w = w0.map((i) => i - shift);
    // The empty word is a word in every B_n; it constrains nothing.
    if (!w.length) continue;
    checked++;
    const msgs: string[] = [];
    if (r.symbol) {
      const p = Number(r.symbol.slice(2).split(",")[0]);
      const need = r.strands ?? Math.max(...w) + 2;
      if (need !== p) msgs.push(`${r.symbol} is a word on ${p} strands, but this one is in B_${need}`);
    }
    if (r.crossings !== undefined && w.length !== r.crossings)
      msgs.push(`word has ${w.length} letters, table says ${r.crossings} crossings`);
    const n = r.strands ?? Math.max(...w) + 2;
    if (r.components !== undefined) {
      const c = components(w, n);
      if (c !== r.components) msgs.push(`closure has ${c} component(s), table says ${r.components}`);
    }
    if (msgs.length) { bad++; console.log(`${r.file}:${r.line}  $${r.word}$`); msgs.forEach((m) => console.log(`    ${m}`)); }
  }
}
console.log(`\nbraid-word rows checked: ${checked}; inconsistent: ${bad}`);
process.exit(bad ? 1 : 0);
