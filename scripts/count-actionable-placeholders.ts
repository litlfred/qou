#!/usr/bin/env bun
/**
 * count-actionable-placeholders.ts — honest placeholder/TODO counter.
 *
 * Standalone (no folio-assistant platform dependency): plain `node:fs` +
 * regex, so it runs in any sandbox with `bun`.
 *
 * WHY THIS EXISTS
 * ---------------
 * The 2026-06-22 bean sweep created ~40 "Resolve N placeholders/TODOs in
 * qou/<area>" beans whose counts were produced by a naive marker grep. An
 * audit of bean `aj81` (qou/stochastic-mechanics, claimed "5") found the
 * count was almost entirely FALSE POSITIVES — and, worse, some "markers"
 * were legitimate §3b conjecture-class `sorry`s that MUST NOT be removed.
 * Draining such beans blindly is busywork at best and a §3b violation at
 * worst. This counter applies the filter the sweep lacked.
 *
 * FALSE-POSITIVE CLASSES EXCLUDED (the noise that inflated the sweep):
 *   1. `.qa.json` / `.witness.json` sidecars — reviewer notes routinely
 *      contain the words "sorry"/"placeholder" ("No unexpected … sorryAx",
 *      "Placeholder stub is unformalised") but are not actionable source.
 *   2. The word `sorry` appearing only in COMMENTS / docstrings / strings
 *      (e.g. the phrase "sorry-free", "no `sorry`", "sorry = conjecture").
 *      We strip Lean comments/strings before counting, so these vanish.
 *   3. A real `sorry` token carrying a `-- Ref:` citation on the same or
 *      preceding two lines — a legitimately-deferred / conjectural witness
 *      per AGENTS.md §1 and §3b. Not a missing proof.
 *   4. `.md` prose mentions of "sorry"/"placeholder" (narrative, not a
 *      work marker). In `.md` we count only explicit TODO/FIXME markers.
 *
 * COUNTED AS GENUINELY ACTIONABLE:
 *   - An un-cited `sorry` token in compiled Lean code (no `-- Ref:` nearby).
 *     (An un-Ref'd conjectural sorry is itself a §1 violation, so flagging
 *      it is correct — it needs a `-- Ref:` even if it stays conjectural.)
 *   - A bare TODO / FIXME / XXX marker in source comments (.lean/.ts/.py).
 *   - A `\TODO` / `TODO:` / `FIXME` marker in `.md`.
 *
 * USAGE:
 *   bun scripts/count-actionable-placeholders.ts [dir ...] [--list]
 * Defaults to scanning content/quantum-observable-universe.
 */

import { readFileSync, existsSync, readdirSync, statSync } from "node:fs";
import { resolve, relative, join, extname, basename } from "node:path";

const REPO_ROOT = resolve(new URL(".", import.meta.url).pathname, "..");

const SKIP_DIRS = new Set([
  "node_modules",
  ".git",
  ".lake",
  "build",
  "lake-packages",
]);
const SKIP_FILE_SUFFIXES = [".qa.json", ".witness.json"];

interface FileCount {
  file: string;
  sorryNoRef: number;
  todo: number;
}

/** Strip Lean line/block comments and string literals → spaces, so token
 *  scans never see `sorry`/TODO that live only in prose. */
function stripLeanComments(src: string): string {
  const out: string[] = [];
  let depth = 0;
  let inString = false;
  for (const line of src.split("\n")) {
    let res = "";
    let i = 0;
    while (i < line.length) {
      if (depth > 0) {
        if (line.startsWith("-/", i)) { depth--; res += "  "; i += 2; }
        else if (line.startsWith("/-", i)) { depth++; res += "  "; i += 2; }
        else { res += " "; i++; }
      } else if (inString) {
        if (line.startsWith('\\"', i) || line.startsWith("\\\\", i)) { res += "  "; i += 2; }
        else if (line[i] === '"') { inString = false; res += " "; i++; }
        else { res += " "; i++; }
      } else if (line.startsWith("/-", i)) { depth++; res += "  "; i += 2; }
      else if (line.startsWith("--", i)) { res += " ".repeat(line.length - i); break; }
      else if (line[i] === '"') { inString = true; res += " "; i++; }
      else { res += line[i]; i++; }
    }
    out.push(res);
  }
  return out.join("\n");
}

const SORRY_TOKEN = /\bsorry\b/;
const REF_NEARBY = /--\s*Ref:/;
// Bare work markers in comments (word-boundary; avoids matching e.g. "fixme"
// inside an identifier). PLACEHOLDER only when standalone caps marker.
const TODO_MARKER = /\b(TODO|FIXME|XXX)\b|\\TODO\b|\bPLACEHOLDER\b/;
// Declaration head — used to associate a `sorry` with its enclosing decl so
// the `-- Ref:` that precedes a MULTI-LINE signature is still credited.
const DECL_START =
  /^\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+|nonrec\s+|scoped\s+|partial\s+|unsafe\s+)*(?:theorem|lemma|proposition|corollary|example|def|abbrev|instance|axiom|structure|class)\s+/;

function countLean(raw: string): { sorryNoRef: number; todo: number } {
  const rawLines = raw.split("\n");
  const codeLines = stripLeanComments(raw).split("\n");
  // Declaration-start lines (top-level indentation), for Ref association.
  const declStarts: number[] = [];
  for (let i = 0; i < codeLines.length; i++) {
    if (DECL_START.test(codeLines[i]) && /^\s{0,2}\S/.test(codeLines[i])) declStarts.push(i);
  }
  const enclosingStart = (i: number): number => {
    let s = 0;
    for (const d of declStarts) { if (d <= i) s = d; else break; }
    return s;
  };
  // A `sorry` is cited if `-- Ref:` appears anywhere from the start of its
  // enclosing decl's leading comment block through the sorry line. This credits
  // the conventional `-- Ref:` that sits just above a multi-line signature
  // (which a fixed 2-line lookback would miss).
  const cited = (i: number): boolean => {
    let start = enclosingStart(i);
    while (start - 1 >= 0 && codeLines[start - 1].trim() === "") start--;
    for (let k = start; k <= i; k++) if (REF_NEARBY.test(rawLines[k] ?? "")) return true;
    return false;
  };
  let sorryNoRef = 0;
  for (let i = 0; i < codeLines.length; i++) {
    if (SORRY_TOKEN.test(codeLines[i]) && !cited(i)) sorryNoRef++;
  }
  // TODO/FIXME markers: count in raw (they live in comments and ARE actionable).
  let todo = 0;
  for (const l of rawLines) if (TODO_MARKER.test(l)) todo++;
  return { sorryNoRef, todo };
}

function countTextMarkers(raw: string): number {
  let todo = 0;
  for (const l of raw.split("\n")) if (TODO_MARKER.test(l)) todo++;
  return todo;
}

function walk(dir: string, acc: FileCount[]): void {
  if (!existsSync(dir)) return;
  for (const entry of readdirSync(dir)) {
    if (SKIP_DIRS.has(entry)) continue;
    const full = join(dir, entry);
    const st = statSync(full);
    if (st.isDirectory()) { walk(full, acc); continue; }
    if (SKIP_FILE_SUFFIXES.some((s) => entry.endsWith(s))) continue;
    const ext = extname(entry);
    let raw: string;
    try { raw = readFileSync(full, "utf-8"); } catch { continue; }
    const rel = relative(REPO_ROOT, full);
    if (ext === ".lean") {
      const { sorryNoRef, todo } = countLean(raw);
      if (sorryNoRef || todo) acc.push({ file: rel, sorryNoRef, todo });
    } else if (ext === ".ts" || ext === ".py") {
      const todo = countTextMarkers(raw);
      if (todo) acc.push({ file: rel, sorryNoRef: 0, todo });
    } else if (ext === ".md") {
      const todo = countTextMarkers(raw);
      if (todo) acc.push({ file: rel, sorryNoRef: 0, todo });
    }
  }
}

function main(): void {
  const args = process.argv.slice(2);
  const list = args.includes("--list");
  const dirs = args.filter((a) => !a.startsWith("--"));
  const scopes = dirs.length
    ? dirs.map((d) => resolve(REPO_ROOT, d))
    : [resolve(REPO_ROOT, "content/quantum-observable-universe")];

  let grandSorry = 0;
  let grandTodo = 0;
  for (const scope of scopes) {
    const acc: FileCount[] = [];
    walk(scope, acc);
    const s = acc.reduce((n, f) => n + f.sorryNoRef, 0);
    const t = acc.reduce((n, f) => n + f.todo, 0);
    grandSorry += s;
    grandTodo += t;
    console.log(
      `\n${relative(REPO_ROOT, scope) || basename(scope)}: ` +
        `${s + t} actionable (${s} uncited-sorry + ${t} TODO/FIXME) ` +
        `across ${acc.length} files`,
    );
    if (list) {
      for (const f of acc.sort((a, b) => b.sorryNoRef + b.todo - (a.sorryNoRef + a.todo))) {
        console.log(`    ${f.sorryNoRef + f.todo}  ${f.file}  [sorry:${f.sorryNoRef} todo:${f.todo}]`);
      }
    }
  }
  console.log(`\nTOTAL: ${grandSorry + grandTodo} actionable (${grandSorry} uncited-sorry + ${grandTodo} TODO/FIXME)`);
}

main();
