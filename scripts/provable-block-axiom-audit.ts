#!/usr/bin/env bun
/**
 * Provable-kind blocks whose Lean formalisation is a bare global `axiom`.
 *
 * Why
 * ---
 * AGENTS.md §"Axiomatization is NOT a Proof": creating an `axiom` and
 * consuming it downstream is not proving anything, it is assuming it. §1a's
 * honest dispositions for an unproved claim are: prove it, state it with
 * `sorry` + a `-- Ref:` citation, or demote it to `conjecture`. A block
 * labelled `theorem`/`proposition`/`lemma`/`corollary` whose `lean.ref`
 * resolves to a bare `axiom` is none of those — the label claims the status
 * the Lean declines to establish.
 *
 * Nothing measured this before. The four found on 2026-09-03 were reached
 * incidentally, from the sibling/library divergence audit.
 *
 * Method, and what it cannot see
 * ------------------------------
 * Blocks come from the pipeline's own `loadBlocksUnder`, so the block set and
 * kinds are authoritative — NOT a regex over `.ts`. (Note the loader returns a
 * lightweight record with the manifest under `.block`; reading `b.lean`
 * directly yields `undefined` for every block, which is how this script first
 * reported 0 of 3516.)
 *
 * The Lean side IS a regex: every `.lean` under the paper is indexed by the
 * final segment of its declaration names, and a ref is resolved by that final
 * segment, sibling-first (AGENTS.md §0a candidate order). So:
 *
 *   * matching on the final segment alone is GENEROUS — it will find a
 *     same-named declaration in the wrong namespace, so `unresolved` is a
 *     count of names declared NOWHERE in the paper and is a solid lower bound
 *     on dangling refs;
 *   * a declaration whose `axiom` keyword is produced by a macro, or which
 *     lives outside the paper tree, is invisible.
 *
 * A clean run is evidence about the `axiom` KEYWORD, not about proof status in
 * general: a `theorem` closed by `sorry`, or by projecting a hypothesis it was
 * handed, is not an axiom and is not reported here. Use the vacuity audit for
 * those.
 */
import { loadBlocksUnder } from "../folio-assistant/cat-harness/content/pipeline/block-module";
import { readFileSync, readdirSync, statSync } from "node:fs";
import { join, resolve } from "node:path";

const REPO = resolve(import.meta.dir, "..");
const ROOT = join(REPO, "content/quantum-observable-universe");
const LIB = join(ROOT, "lean");
const PROVABLE = new Set(["theorem", "proposition", "lemma", "corollary"]);
const KINDS = ["axiom", "theorem", "lemma", "def", "abbrev", "class",
               "structure", "instance", "opaque", "inductive"];
const DECL = new RegExp(
  String.raw`^\s*(?:@\[[^\]]*\]\s*)?` +
  String.raw`(?:noncomputable\s+|private\s+|protected\s+|scoped\s+|partial\s+)*` +
  `(${KINDS.join("|")})\\s+([A-Za-z_][A-Za-z0-9_'!?.]*)`, "gm");

function walk(d: string, out: string[] = []): string[] {
  for (const e of readdirSync(d)) {
    if (e === ".lake" || e === "build") continue;
    const p = join(d, e);
    if (statSync(p).isDirectory()) walk(p, out);
    else if (e.endsWith(".lean")) out.push(p);
  }
  return out;
}

const index = new Map<string, { kind: string; file: string }[]>();
for (const f of walk(ROOT)) {
  const txt = readFileSync(f, "utf8")
    .replace(/\/-[\s\S]*?-\//g, " ")
    .replace(/--[^\n]*/g, " ");
  for (const m of txt.matchAll(DECL)) {
    // A Lean declaration name may itself be dotted (`CategoricalProton.exists`).
    // Index the full name AND its final segment: a ref's final segment alone
    // would otherwise miss every dotted declaration, which is exactly how this
    // script first reported 68 dangling refs against a true 25.
    for (const key of new Set([m[2], m[2].split(".").pop()!])) {
      const arr = index.get(key) ?? [];
      arr.push({ kind: m[1], file: f });
      index.set(key, arr);
    }
  }
}

const r: any = await loadBlocksUnder(ROOT);
const blocks: Map<string, any> = r.blocks;
const hits: { label: string; kind: string; decl: string; where: string[] }[] = [];
const dangling: { label: string; kind: string; decl: string }[] = [];
let checked = 0;

for (const [label, b] of blocks) {
  if (!PROVABLE.has(b.kind)) continue;
  const ref: string | undefined = (b.block ?? b).lean?.ref;
  if (!ref) continue;
  const decl = ref.split(":")[1];
  if (!decl) continue;
  checked++;
  const cands = index.get(decl) ?? index.get(decl.split(".").slice(-2).join("."))
             ?? index.get(decl.split(".").pop()!);
  if (!cands?.length) { dangling.push({ label, kind: b.kind, decl }); continue; }
  const sib = cands.filter((c) => !c.file.startsWith(LIB));
  const chosen = sib.length ? sib : cands;
  const ax = chosen.filter((c) => c.kind === "axiom");
  if (ax.length) {
    hits.push({ label, kind: b.kind, decl,
      where: ax.map((c) => c.file.replace(REPO + "/", "")) });
  }
}

console.log(`provable blocks with a lean.ref  : ${checked}`);
console.log(`  ref's final segment declared nowhere : ${dangling.length}`);
console.log(`  ref resolves to a bare AXIOM         : ${hits.length}`);
console.log();
for (const h of hits.sort((a, b) => a.label.localeCompare(b.label))) {
  console.log(`[${h.kind}] ${h.label}`);
  console.log(`    -> axiom ${h.decl}`);
  for (const w of h.where) console.log(`       ${w}`);
}
if (process.argv.includes("--dangling")) {
  console.log(`\n--- refs declared nowhere in the paper (${dangling.length}) ---`);
  for (const d of dangling.sort((a, b) => a.label.localeCompare(b.label)))
    console.log(`[${d.kind}] ${d.label} -> ${d.decl}`);
}
