#!/usr/bin/env bun
/**
 * audit-narrative-proof-presence.ts
 *
 * Corpus audit: does every provable content block (theorem / lemma /
 * proposition / corollary) carry a *narrative* proof in its `.md`
 * sibling — i.e. an argument the human reader can follow in prose, not
 * only a Lean `.lean` formalization and not only a bare statement?
 *
 * Motivation. The QA sidecar (`<block>.qa.json`) registry §PROOF tracks
 * proof quality on the *Lean* side only: `proof-no-bare-sorries`,
 * `proof-lean-compiles`, `proof-no-axiom-growth`, `proof-narrative-lean-equiv`
 * (equivalence, gated on `.lean` existing), the vacuity family, the rater
 * scores. None of them assert the *positive* requirement "a provable block
 * must contain a narrative proof in prose." This script fills that gap as a
 * standalone, registry-independent audit so the backlog is visible while the
 * `proof-narrative-present` QA criterion is wired into the folio-assistant
 * qa-criteria-registry (separate repo).
 *
 * Canonical signal (target architecture). A provable block's narrative
 * proof lives in a dedicated **`<root>.proof.md` sibling file**, parallel
 * to `<root>.md` (statement) and `<root>.lean` (formalization). Presence
 * of a non-trivial `<root>.proof.md` ⇒ the block HAS a narrative proof,
 * trackable by file existence alone. This is the convention requested by
 * the author (2026-06-24) and specified in
 * `docs/conventions/narrative-proof-sidecar.md`.
 *
 * Legacy signal (transitional). Until every block is migrated, a block
 * also counts as HAVING a narrative proof if its `<root>.md` contains a
 * recognizable proof cue inline (a "Proof" heading/word, "we
 * prove/show/establish", an induction/construction phrase, ∎/QED). The
 * audit reports the migration split (sidecar vs inline-only) so progress
 * toward the target architecture is visible.
 *
 * A block is EXEMPT (not a gap) when its narrative explicitly defers the
 * proof to an external/axiomatic source ("external-proof" tag, "standard
 * result", "take as axiomatic", …) — those are deliberate, cited
 * black-boxes, not missing proofs.
 *
 * This is a heuristic surfacing tool, not a gate: a human still confirms
 * each flagged block genuinely lacks a proof versus being definitional or
 * trivially self-evident.
 *
 * Usage:
 *   bun run content/pipeline/audit-narrative-proof-presence.ts [content-root]
 *   bun run content/pipeline/audit-narrative-proof-presence.ts --json
 */
import { readFileSync, existsSync, readdirSync, statSync } from "fs";
import { join } from "path";

const PROVABLE = new Set(["theorem", "lemma", "proposition", "corollary"]);

const PROOF_CUE =
  /\bproof\b|\bwe (?:prove|show|establish|verify|argue|claim|deduce|conclude)\b|∎|\bq\.?e\.?d\.?\b|\bby (?:induction|construction|definition|hypothesis|cases)\b|\bsuppose\b.*\bthen\b/is;

const EXTERNAL_CUE =
  /external[-\s]proof|as axiomatic|take[^.]*as (?:an )?axiom|standard result|axiomati[sz]ed|cited (?:as|external)|proof occupies|due to [A-Z]/s;

interface Gap {
  ts: string;
  label: string;
  kind: string;
  chapter: string;
}

/** Non-trivial = has some real prose, not an empty/placeholder stub. */
function nonTrivial(s: string): boolean {
  return s.replace(/\s+/g, " ").trim().length > 20;
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

function main() {
  const args = process.argv.slice(2);
  const asJson = args.includes("--json");
  const root = args.find((a) => !a.startsWith("--")) ?? "content";

  const gaps: Gap[] = [];
  let total = 0,
    sidecar = 0,
    inlineOnly = 0,
    external = 0;

  for (const ts of walk(root)) {
    if (ts.includes("/schema/") || ts.includes("/pipeline/")) continue;
    const txt = readFileSync(ts, "utf-8");
    const m = txt.match(/export default (\w+)\(/);
    if (!m || !PROVABLE.has(m[1])) continue;
    total++;
    const kind = m[1];
    const label = (txt.match(/label:\s*["'`]([^"'`]+)["'`]/) ?? [, "?"])[1];
    const root3 = ts.slice(0, -3);
    const md = root3 + ".md";
    const proofMd = root3 + ".proof.md";
    const body = existsSync(md) ? readFileSync(md, "utf-8") : "";
    const haystack = txt + "\n" + body;

    // Canonical signal: a non-trivial `.proof.md` sidecar.
    if (existsSync(proofMd) && nonTrivial(readFileSync(proofMd, "utf-8"))) {
      sidecar++;
      continue;
    }
    // Legacy signal: an inline proof cue in `.md`.
    if (PROOF_CUE.test(body)) {
      inlineOnly++;
      continue;
    }
    if (EXTERNAL_CUE.test(haystack)) {
      external++;
      continue;
    }
    const parts = ts.split("/");
    gaps.push({ ts, label, kind, chapter: parts[2] ?? parts[1] ?? "?" });
  }

  if (asJson) {
    console.log(
      JSON.stringify(
        { total, sidecar, inlineOnly, external, gaps: gaps.length, items: gaps },
        null,
        2,
      ),
    );
    return;
  }

  const byChap = new Map<string, number>();
  for (const g of gaps) byChap.set(g.chapter, (byChap.get(g.chapter) ?? 0) + 1);

  console.log(`Provable blocks scanned:           ${total}`);
  console.log(`  proof in .proof.md sidecar:      ${sidecar}   (target architecture)`);
  console.log(`  proof inline in .md (legacy):    ${inlineOnly}   (migrate → .proof.md)`);
  console.log(`  external / axiomatic:            ${external}`);
  console.log(`  NO narrative proof (gaps):       ${gaps.length}`);
  console.log("\nGaps by chapter:");
  for (const [c, n] of [...byChap.entries()].sort((a, b) => b[1] - a[1])) {
    console.log(`  ${String(n).padStart(3)}  ${c}`);
  }
  if (gaps.length) process.exitCode = 1;
}

main();
