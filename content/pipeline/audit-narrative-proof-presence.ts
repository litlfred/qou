#!/usr/bin/env bun
/**
 * audit-narrative-proof-presence.ts
 *
 * Corpus audit: does every provable content block (theorem / lemma /
 * proposition / corollary) have a *narrative* proof a human reader can
 * follow — i.e. a linked `proof` block — rather than only a Lean `.lean`
 * formalization or only a bare statement?
 *
 * Mechanism (already in the platform). A narrative proof is its own
 * content block of kind `proof`: a `<name>-proof.ts` + `<name>-proof.md`
 * triple with `label: "prf:<name>"` and `uses: ["<parent-label>"]`. The
 * parent provable block links it via `proofs: ["prf:<name>"]`, and the
 * chapter manifest lists `"<name>-proof"` in its block array. The render
 * pipeline emits the `<name>-proof.md` body inside a proof environment
 * after the statement. ~170 such proof blocks already exist.
 *
 * A provable block is COVERED iff it has a linked, non-trivial proof
 * block — detected either from the parent's `proofs: [...]` field or from
 * a `proof` block whose `uses: [...]` names the parent's label. Otherwise
 * it is a GAP: the proof, if it exists at all, lives only in Lean or in
 * inline parent prose, and is not separately tracked.
 *
 * Motivation. The QA sidecar registry §PROOF tracks proof quality on the
 * *Lean* side only; none of its criteria assert "a provable block must
 * carry a separately-tracked narrative proof block." This script surfaces
 * that backlog (the proposed `proof-narrative-present` QA criterion) so it
 * is visible while the criterion is wired into the folio-assistant
 * qa-criteria-registry.
 *
 * Heuristic at the margin: a definitional proposition may need no proof,
 * and an external/axiomatic result is deliberately a cited black-box. Each
 * flagged block needs a human pass to confirm the disposition (author a
 * proof block / mark external / demote).
 *
 * Usage:
 *   bun run content/pipeline/audit-narrative-proof-presence.ts [content-root]
 *   bun run content/pipeline/audit-narrative-proof-presence.ts --json
 */
import { readFileSync, existsSync, readdirSync, statSync } from "fs";
import { join } from "path";

const PROVABLE = new Set(["theorem", "lemma", "proposition", "corollary"]);

/** Non-trivial = has some real prose, not an empty/placeholder stub. */
function nonTrivial(s: string): boolean {
  return s.replace(/\s+/g, " ").trim().length > 20;
}

function field(txt: string, name: string): string[] {
  const m = txt.match(new RegExp(`${name}:\\s*\\[([^\\]]*)\\]`));
  if (!m) return [];
  return [...m[1].matchAll(/["'`]([^"'`]+)["'`]/g)].map((x) => x[1]);
}

function label(txt: string): string {
  return (txt.match(/label:\s*["'`]([^"'`]+)["'`]/) ?? [, "?"])[1];
}

function walk(dir: string, out: string[] = []): string[] {
  for (const e of readdirSync(dir)) {
    const p = join(dir, e);
    const s = statSync(p);
    if (s.isDirectory()) {
      if (e === "node_modules" || e === "lean" || e === ".lake") continue;
      walk(p, out);
    } else if (e.endsWith(".ts")) {
      out.push(p);
    }
  }
  return out;
}

interface Gap {
  ts: string;
  label: string;
  kind: string;
  chapter: string;
}

function main() {
  const args = process.argv.slice(2);
  const asJson = args.includes("--json");
  const root = args.find((a) => !a.startsWith("--")) ?? "content";

  const files = walk(root).filter(
    (f) => !f.includes("/schema/") && !f.includes("/pipeline/"),
  );

  // Pass 1: index non-trivial proof blocks and which parent labels they prove.
  const prfOk = new Set<string>();
  const provesParent = new Set<string>();
  for (const ts of files) {
    const txt = readFileSync(ts, "utf-8");
    if (!/export default proof\(/.test(txt)) continue;
    const md = ts.slice(0, -3) + ".md";
    const body = existsSync(md) ? readFileSync(md, "utf-8") : "";
    if (!nonTrivial(body)) continue;
    prfOk.add(label(txt));
    for (const u of field(txt, "uses")) provesParent.add(u);
  }

  // Pass 2: classify provable blocks.
  const gaps: Gap[] = [];
  let total = 0,
    covered = 0;
  for (const ts of files) {
    const txt = readFileSync(ts, "utf-8");
    const m = txt.match(/export default (\w+)\(/);
    if (!m || !PROVABLE.has(m[1])) continue;
    total++;
    const lab = label(txt);
    const linked =
      field(txt, "proofs").some((r) => prfOk.has(r)) || provesParent.has(lab);
    if (linked) {
      covered++;
    } else {
      const parts = ts.split("/");
      gaps.push({ ts, label: lab, kind: m[1], chapter: parts[2] ?? parts[1] ?? "?" });
    }
  }

  if (asJson) {
    console.log(
      JSON.stringify({ total, covered, gaps: gaps.length, items: gaps }, null, 2),
    );
    return;
  }

  const byChap = new Map<string, number>();
  for (const g of gaps) byChap.set(g.chapter, (byChap.get(g.chapter) ?? 0) + 1);

  console.log(`Provable blocks scanned:            ${total}`);
  console.log(`  with a linked proof block:        ${covered}`);
  console.log(`  NO proof block (gaps):            ${gaps.length}`);
  console.log("\nGaps by chapter:");
  for (const [c, n] of [...byChap.entries()].sort((a, b) => b[1] - a[1])) {
    console.log(`  ${String(n).padStart(3)}  ${c}`);
  }
  if (gaps.length) process.exitCode = 1;
}

main();
