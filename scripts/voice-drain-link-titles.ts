#!/usr/bin/env bun
/**
 * Mechanical slice of the voice-leak drain (epic qou-d4kh, option 1): a link
 * whose visible text is the raw label of a block (`[`rem:x`](#rem:x)`) gets
 * that block's own title, from its .ts manifest, as its text. The target is
 * untouched. Only links whose text label equals a label the paper defines are
 * rewritten; everything else is left alone and counted.
 *
 *   bun run scripts/voice-drain-link-titles.ts [--apply] [--exclude dir,dir]
 */
import { readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { readingOrder } from "../folio/pipeline/voice-leak-audit";

const PAPER = "folio/quantum-observable-universe";
const args = process.argv.slice(2);
const apply = args.includes("--apply");
const ei = args.indexOf("--exclude");
const exclude = new Set(ei >= 0 ? args[ei + 1]!.split(",") : []);
const MAX = 70;

/** Short form: a title longer than MAX is cut at its first ': ' / ' — ' / ', '. */
export function shortTitle(t: string): string {
  // A title that itself talks about the formalisation would carry the leak
  // into the prose: drop a parenthetical or trailing clause that does.
  let s = t.replace(/\s+/g, " ").trim().replace(/\.$/, "")
    .replace(/\s*\([^()]*\b(?:Lean|Mathlib|formali[sz]\w*|axiomati[sz]\w*|class)\b[^()]*\)/g, "")
    .replace(/\s*(?:—|--|:|;)\s*[^—:;]*\b(?:Lean|Mathlib)\b.*$/, "");
  s = s.replace(/\s+in Lean\b.*$/, "").replace(/;[^;]*`[^;]*$/, "");
  if (s.length > MAX)
    for (const sep of [": ", " — ", " -- ", "; ", ", "]) {
      const i = s.indexOf(sep);
      if (i > 15 && i <= MAX && (s.slice(0, i).split("$").length - 1) % 2 === 0) { s = s.slice(0, i); break; }
    }
  return s;
}

const order = await readingOrder(PAPER);
const title = new Map<string, string>();
for (const b of order) {
  if (!b.label) continue;
  try {
    const m: any = (await import(join(process.cwd(), b.md.replace(/\.md$/, ".ts")))).default;
    if (typeof m?.title === "string" && m.title.trim()) title.set(b.label, m.title);
  } catch {}
}
const LINK = /\[`((?:def|thm|lem|prop|cor|conj|rem|ex|sim|alg|obs|defn):[\w.:-]+)`\]\(([^)\s]+)\)/g;
let changed = 0, files = 0, noTitle = 0;
const skipped: string[] = [];
for (const b of order) {
  if (exclude.has(b.chapter)) continue;
  let src: string;
  try { src = readFileSync(b.md, "utf8"); } catch { continue; }
  let inFence = false, n = 0;
  const out = src.split("\n").map((line) => {
    if (/^\s*(```|~~~)/.test(line)) { inFence = !inFence; return line; }
    if (inFence) return line;
    return line.replace(LINK, (all, label: string, target: string) => {
      const t = title.get(label);
      if (!t) { noTitle++; skipped.push(`${b.md}: ${label}`); return all; }
      n++;
      return `[${shortTitle(t)}](${target})`;
    });
  });
  if (n) { files++; changed += n; if (apply) writeFileSync(b.md, out.join("\n")); }
}
console.log(`voice-drain-link-titles: ${changed} link(s) in ${files} file(s) ${apply ? "rewritten" : "would be rewritten"}; ${noTitle} left (label has no title)`);
if (skipped.length) console.log(skipped.slice(0, 40).join("\n"));
