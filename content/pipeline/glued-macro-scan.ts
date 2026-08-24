#!/usr/bin/env bun
/**
 * Find control sequences glued to the token that follows them.
 *
 * `\pi c_s` written without the space is `\pic_s`, a single control sequence
 * named `pic`. LaTeX matches the longest name, so the `c` is gone before
 * anything can complain, and what happens next depends entirely on whether
 * `\pic` is defined:
 *
 *   - undefined -> the build stops. Loud, and therefore harmless.
 *   - defined   -> the page compiles and prints the wrong mathematics.
 *
 * The second case is the reason this exists. main.tex carried sixteen
 * `\newcommand`s under the heading "Stubs for compound macros (missing
 * spaces in source content)" — each one a glued typo promoted to a macro so
 * the page would build. Two printed wrong maths for months: `\pic` expanded
 * to `\pi`, silently deleting a sound speed from a Hawking-temperature
 * denominator that the same block's prose wrote correctly; `\xid` expanded
 * to `\xi_d`, turning `\mathcal{L}_\xi d\alpha` into a Lie derivative along
 * a subscripted field with no argument. Three of them were even commented
 * as "Reeb vector field variants", documenting typos as notation.
 *
 * So: never define the glued name. Fix the `.md`, and let the undefined
 * control sequence be the error it should be.
 *
 * Detection needs no macro dictionary. Control sequences used often across
 * the corpus are the vocabulary; a rare one whose prefix is in that
 * vocabulary and whose remainder is a letter or two is a glue candidate.
 * That deliberately admits false positives — `\rightarrow` is `\right` plus
 * `arrow` — so the suffix cap keeps them few and each hit is a judgement,
 * not a verdict.
 *
 *   bun run content/pipeline/glued-macro-scan.ts [path ...]
 *
 * Exits 1 when any candidate is found, so it can gate a commit.
 *
 * @module content/pipeline/glued-macro-scan
 */
import { readFileSync, globSync } from "node:fs";

/** How often a name must appear before it counts as corpus vocabulary. */
const VOCAB_MIN = 8;
/** A rarer name than this is not a candidate — it is simply in use. */
const RARE_MAX = 3;
/** A glued variable is a letter or two, not a word. */
const SUFFIX_MAX = 2;

export interface Hit {
  name: string;
  prefix: string;
  suffix: string;
  count: number;
  sites: { file: string; line: number }[];
}

export function scan(files: string[]): Hit[] {
  const count = new Map<string, number>();
  const sites = new Map<string, { file: string; line: number }[]>();

  for (const file of files) {
    let text: string;
    try { text = readFileSync(file, "utf8"); } catch { continue; }
    text.split("\n").forEach((line, i) => {
      for (const m of line.matchAll(/\\([A-Za-z]+)/g)) {
        const n = m[1];
        count.set(n, (count.get(n) ?? 0) + 1);
        const at = sites.get(n) ?? [];
        if (at.length < 4) at.push({ file, line: i + 1 });
        sites.set(n, at);
      }
    });
  }

  const vocab = new Set([...count].filter(([, c]) => c >= VOCAB_MIN).map(([n]) => n));
  const hits: Hit[] = [];
  for (const [name, c] of count) {
    if (c > RARE_MAX || vocab.has(name)) continue;
    // Longest prefix first: `\varepsilonq` should report `\varepsilon` + "q",
    // not some shorter accidental prefix.
    for (let k = name.length - 1; k >= 2; k--) {
      const prefix = name.slice(0, k), suffix = name.slice(k);
      if (suffix.length > SUFFIX_MAX) continue;
      if (!vocab.has(prefix)) continue;
      hits.push({ name, prefix, suffix, count: c, sites: sites.get(name) ?? [] });
      break;
    }
  }
  return hits.sort((a, b) => a.name.localeCompare(b.name));
}

if (import.meta.main) {
  const args = process.argv.slice(2);
  const files = args.length ? args : globSync("content/**/*.md");
  const hits = scan(files);

  if (!hits.length) {
    console.log(`no glued control sequences in ${files.length} files`);
    process.exit(0);
  }
  console.log(`${hits.length} candidate glued control sequences:\n`);
  for (const h of hits) {
    console.log(`\\${h.name}  = \\${h.prefix} + "${h.suffix}"   (x${h.count})`);
    for (const s of h.sites) console.log(`      ${s.file}:${s.line}`);
  }
  console.log(
    `\nEach is a candidate, not a verdict: a real macro whose name happens to` +
    `\nextend a common one (\\rightarrow, \\coloneqq, \\dotsb) lands here too.` +
    `\nFor a real one, insert the space in the .md. Never define the glued name.`,
  );
  process.exit(1);
}
