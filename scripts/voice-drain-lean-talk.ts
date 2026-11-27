#!/usr/bin/env bun
/**
 * Semi-mechanical slice of option 3 of the voice-leak drain (epic qou-d4kh):
 * three forms of Lean talk in reader prose that can be removed without
 * judgement, outside Chapters 1-2.
 *
 *   section   a `## Lean …` / `### Lean …` section is moved VERBATIM into the
 *             block's .ts `authorNotes` (kind "note"), so no provenance is lost;
 *   label     "(Lean: `decl`)" in a statement/proof label is dropped;
 *   paren     a parenthetical holding only backticked identifiers that
 *             voice-leak-audit classifies as Lean/repository identifiers is
 *             dropped (the declaration name stays in the .ts `lean` field).
 *
 * Everything else (sentences that talk about the formalisation) is left for
 * a hand pass and counted by voice-leak-audit.
 *
 *   bun run scripts/voice-drain-lean-talk.ts [--apply] [--exclude dir,dir] [--only dir,dir]
 */
import { existsSync, readFileSync, writeFileSync } from "node:fs";
import { classifyCode, readingOrder } from "../folio/pipeline/voice-leak-audit";

const args = process.argv.slice(2);
const apply = args.includes("--apply");
const opt = (k: string) => { const i = args.indexOf(k); return i >= 0 ? new Set(args[i + 1]!.split(",")) : null; };
const exclude = opt("--exclude") ?? new Set(["quantum-universes", "quantum-observable-universes"]);
const only = opt("--only");

const LABEL_RE = /\s*\((?:Lean|Lean\s+[\w-]+)\s*:\s*`[^`]+`(?:\s*(?:,|and|\/|;)\s*`[^`]+`)*\s*\)/g;
const PAREN_RE = /\s*\(\s*(`[^`]+`(?:\s*(?:,|;|and|\/|,\s*and)\s*`[^`]+`)*)\s*\)/g;

function notesEntry(body: string): string {
  return `    { kind: "note", date: "2026-11-20", body: ${JSON.stringify("Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): " + body)} },\n`;
}
function addNote(ts: string, body: string): string | null {
  const k = "authorNotes: [\n";
  // function replacer: a body may contain "$`" / "$'", which a string replacement would expand
  if (ts.includes(k)) return ts.replace(k, () => k + notesEntry(body));
  const end = ts.lastIndexOf("});");
  if (end < 0) return null;
  const before = ts.slice(0, end).replace(/,?\s*$/, ",\n");
  return before + "  authorNotes: [\n" + notesEntry(body) + "  ],\n" + ts.slice(end);
}

const stats = { section: 0, sectionKept: 0, label: 0, paren: 0, files: 0, tsFail: 0 };
const order = await readingOrder("folio/quantum-observable-universe");
for (const b of order) {
  if (exclude.has(b.chapter) || (only && !only.has(b.chapter)) || !existsSync(b.md)) continue;
  const src = readFileSync(b.md, "utf8");
  const lines = src.split("\n");
  const moved: string[] = [];
  const keep: string[] = [];
  let inFence = false;
  for (let i = 0; i < lines.length; i++) {
    const l = lines[i]!;
    if (/^\s*(```|~~~)/.test(l)) inFence = !inFence;
    const h = !inFence && l.match(/^(#{2,4})\s*Lean\b/);
    if (h) {
      const lvl = h[1]!.length;
      let j = i + 1, f = false;
      for (; j < lines.length; j++) {
        if (/^\s*(```|~~~)/.test(lines[j]!)) f = !f;
        const m = !f && lines[j]!.match(/^(#{1,6})\s/);
        if (m && m[1]!.length <= lvl) break;
      }
      const sec = lines.slice(i, j).join("\n").trim();
      const body = sec.split("\n").slice(1).filter((x) => x.trim());
      const leanish = body.filter((x) => /`|\bLean\b|Mathlib|\bsorry\b|\btheorem\b|\blemma\b/.test(x)).length;
      // Move only a section that is ABOUT the formalisation. One carrying a
      // scope caveat or mathematics of its own stays for a hand pass, where
      // the caveat is restated in mathematical terms rather than hidden.
      if (body.length && leanish / body.length < 0.8 ||
          /\b(?:gap|not derived|conjectur\w*|caveat|open|assum\w*|empirical|fit\w*)\b/i.test(sec)) {
        stats.sectionKept++;
        keep.push(l);
        continue;
      }
      moved.push(sec);
      stats.section++;
      while (keep.length && keep[keep.length - 1] === "") keep.pop();
      if (j < lines.length) keep.push("");
      i = j - 1;
      continue;
    }
    if (inFence) { keep.push(l); continue; }
    let out = l.replace(LABEL_RE, () => { stats.label++; return ""; });
    out = out.replace(PAREN_RE, (all, inner: string) => {
      const ids = [...inner.matchAll(/`([^`]+)`/g)].map((m) => m[1]!);
      if (ids.length && ids.every((s) => classifyCode(s) && classifyCode(s) !== "block-id")) { stats.paren++; return ""; }
      return all;
    });
    keep.push(out);
  }
  let next = keep.join("\n");
  if (!src.endsWith("\n") || next.endsWith("\n")) {} else next += "\n";
  if (next === src) continue;
  stats.files++;
  if (!apply) continue;
  if (moved.length) {
    const tsPath = b.md.replace(/\.md$/, ".ts");
    const ts = existsSync(tsPath) ? addNote(readFileSync(tsPath, "utf8"), moved.join("\n\n")) : null;
    if (!ts) { stats.tsFail++; continue; } // never drop a section we cannot relocate
    writeFileSync(tsPath, ts);
  }
  writeFileSync(b.md, next);
}
console.log(`voice-drain-lean-talk: ${apply ? "applied" : "dry run"} ${JSON.stringify(stats)}`);
