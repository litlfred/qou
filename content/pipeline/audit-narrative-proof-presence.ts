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
 * A block is counted as HAVING a narrative proof if its `.md` contains a
 * recognizable proof cue (a "Proof" heading/word, a first-person "we
 * prove/show/establish", an induction/construction phrase, a QED mark, …).
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
    withProof = 0,
    external = 0;

  for (const ts of walk(root)) {
    if (ts.includes("/schema/") || ts.includes("/pipeline/")) continue;
    const txt = readFileSync(ts, "utf-8");
    const m = txt.match(/export default (\w+)\(/);
    if (!m || !PROVABLE.has(m[1])) continue;
    total++;
    const kind = m[1];
    const label = (txt.match(/label:\s*["'`]([^"'`]+)["'`]/) ?? [, "?"])[1];
    const md = ts.slice(0, -3) + ".md";
    const body = existsSync(md) ? readFileSync(md, "utf-8") : "";
    const haystack = txt + "\n" + body;
    if (PROOF_CUE.test(body)) {
      withProof++;
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
        { total, withProof, external, gaps: gaps.length, items: gaps },
        null,
        2,
      ),
    );
    return;
  }

  const byChap = new Map<string, number>();
  for (const g of gaps) byChap.set(g.chapter, (byChap.get(g.chapter) ?? 0) + 1);

  console.log(`Provable blocks scanned:      ${total}`);
  console.log(`  with narrative proof:       ${withProof}`);
  console.log(`  external / axiomatic:       ${external}`);
  console.log(`  NO narrative proof (gaps):  ${gaps.length}`);
  console.log("\nGaps by chapter:");
  for (const [c, n] of [...byChap.entries()].sort((a, b) => b[1] - a[1])) {
    console.log(`  ${String(n).padStart(3)}  ${c}`);
  }
  if (gaps.length) process.exitCode = 1;
}

main();
