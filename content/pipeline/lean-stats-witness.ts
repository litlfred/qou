#!/usr/bin/env bun
/**
 * Lean formalization statistics — witness producer.
 *
 * Derives the paper-level Lean proved-count statistics quoted in prose
 * (introduction author's note) from the content blocks themselves, so
 * the paper cannot drift from the actual formalization state.  The
 * numbers flow:
 *
 *   block manifests + .lean sources + .qa.json sidecars
 *     → this script
 *     → folio-assistant/computations/lean-formalization-stats.witness.json
 *     → content/values/registry.ts entries (lean_provable_total, …)
 *     → `:val[…]` directives in .md prose
 *     → rendered LaTeX
 *
 * Counted statistics (per paper):
 *   - provable claims (theorem | lemma | proposition | corollary):
 *     total, with .lean sibling, sorry-free (comment-stripped scan),
 *     and the sorry-free percentage;
 *   - conjectures: total, class-axiomatised in Lean (CLAUDE.md §3b
 *     conditional-class convention), and the percentage;
 *   - per-kind totals (theorem/lemma/proposition/corollary/definition);
 *   - supplementary QA-sidecar aggregate: latest `proof-lean-compiles`
 *     result counts (pass/fail/warn/missing) so the witness records the
 *     compile-side view alongside the source-side sorry scan.
 *
 * Sorry detection matches proof-axis-dashboard.ts: block comments
 * `/- … -/` and line comments `-- …` are stripped before scanning for
 * `\bsorry\b`, so a cited `-- Ref: … sorry` comment does not count.
 *
 * Usage (from content/):
 *   bun run pipeline/lean-stats-witness.ts [paper-dir]            # dry run
 *   bun run pipeline/lean-stats-witness.ts [paper-dir] --write    # write witness
 *   bun run pipeline/lean-stats-witness.ts [paper-dir] --check    # CI drift gate
 *
 * `--check` exits 1 when the committed witness's `data` section
 * disagrees with a fresh recount; the fix is always
 * `bun run pipeline/lean-stats-witness.ts --write`.
 *
 * @module content/pipeline/lean-stats-witness
 */

import { existsSync, readFileSync, writeFileSync } from "fs";
import { resolve, relative } from "path";
import { fileURLToPath } from "url";
import { execFileSync } from "child_process";
import {
  walkBlocks,
  loadQaReport,
  hashFile,
  gitFileCommitSha,
} from "./qa-utils";

const __filename = fileURLToPath(import.meta.url);
const REPO_ROOT = resolve(__filename, "..", "..", "..");
const SCRIPT_REL = relative(REPO_ROOT, __filename);
const WITNESS_REL =
  "folio-assistant/computations/lean-formalization-stats.witness.json";

/** Block kinds that make a provable logical claim (CLAUDE.md §3b). */
const PROVABLE_KINDS = new Set([
  "theorem",
  "lemma",
  "proposition",
  "corollary",
]);

// ── CLI args ─────────────────────────────────────────────────────

interface Args {
  root: string;
  mode: "dry" | "write" | "check";
}

function parseArgs(argv: string[]): Args {
  const out: Args = { root: "quantum-observable-universe", mode: "dry" };
  for (const a of argv) {
    if (a === "--write") out.mode = "write";
    else if (a === "--check") out.mode = "check";
    else if (!a.startsWith("-")) out.root = a;
  }
  return out;
}

// ── Lean source scanning ─────────────────────────────────────────

/**
 * Strip Lean block comments (`/- … -/`, including `/-- … -/` and
 * `/-! … -/`) and line comments (`-- …`), preserving line structure.
 * Same approach as proof-axis-dashboard.ts.
 */
export function stripLeanComments(src: string): string {
  return src
    .replace(/\/-[\s\S]*?-\//g, (m) => "\n".repeat(m.split("\n").length - 1))
    .replace(/--[^\n]*/g, "");
}

/** Count code-level `sorry` tokens (comments stripped). */
export function countCodeSorries(src: string): number {
  return (stripLeanComments(src).match(/\bsorry\b/g) ?? []).length;
}

/** Does the Lean source declare a `class` (conditional-class axiom)? */
export function declaresClass(src: string): boolean {
  return /\bclass\b/.test(stripLeanComments(src));
}

// ── Statistics ───────────────────────────────────────────────────

/**
 * The witness `data` section.  Counts are JSON numbers; percentages
 * are decimal strings at 6 significant digits so the `:val[…]`
 * renderer (string-surgery formatter) controls display precision.
 */
export interface LeanStats {
  blocks_total: number;
  blocks_with_lean: number;
  theorem_total: number;
  lemma_total: number;
  proposition_total: number;
  corollary_total: number;
  definition_total: number;
  provable_total: number;
  provable_with_lean: number;
  provable_sorry_free: number;
  provable_sorry_free_pct: string;
  conjecture_total: number;
  conjecture_class_axiomatised: number;
  conjecture_class_axiomatised_pct: string;
  qa_lean_compiles_pass: number;
  qa_lean_compiles_fail: number;
  qa_lean_compiles_warn: number;
  qa_lean_compiles_na: number;
  qa_lean_compiles_missing: number;
}

/** Percentage a/b·100 as a decimal string (6 significant digits). */
function pctString(a: number, b: number): string {
  if (b === 0) return "0";
  return Number(((a / b) * 100).toPrecision(6)).toString();
}

export function computeStats(rootAbs: string): LeanStats {
  const s: LeanStats = {
    blocks_total: 0,
    blocks_with_lean: 0,
    theorem_total: 0,
    lemma_total: 0,
    proposition_total: 0,
    corollary_total: 0,
    definition_total: 0,
    provable_total: 0,
    provable_with_lean: 0,
    provable_sorry_free: 0,
    provable_sorry_free_pct: "0",
    conjecture_total: 0,
    conjecture_class_axiomatised: 0,
    conjecture_class_axiomatised_pct: "0",
    qa_lean_compiles_pass: 0,
    qa_lean_compiles_fail: 0,
    qa_lean_compiles_warn: 0,
    qa_lean_compiles_na: 0,
    qa_lean_compiles_missing: 0,
  };

  for (const block of walkBlocks(rootAbs)) {
    s.blocks_total++;

    const leanAbs =
      block.lean && existsSync(block.lean) ? block.lean : undefined;
    if (leanAbs) s.blocks_with_lean++;

    const leanSrc = leanAbs ? readFileSync(leanAbs, "utf-8") : undefined;

    switch (block.kind) {
      case "theorem": s.theorem_total++; break;
      case "lemma": s.lemma_total++; break;
      case "proposition": s.proposition_total++; break;
      case "corollary": s.corollary_total++; break;
      case "definition": s.definition_total++; break;
    }

    if (PROVABLE_KINDS.has(block.kind)) {
      s.provable_total++;
      if (leanSrc !== undefined) {
        s.provable_with_lean++;
        // A provable claim "carries a full Lean proof" iff its Lean
        // sibling exists and has no code-level sorry.  Blocks without
        // a .lean sibling count against the sorry-free total.
        if (countCodeSorries(leanSrc) === 0) s.provable_sorry_free++;
      }

      // QA-sidecar compile aggregate (supplementary): the latest
      // `proof-lean-compiles` entry per provable block.
      const report = block.qa ? loadQaReport(block.qa) : undefined;
      const entries = report?.criteria?.["proof-lean-compiles"] ?? [];
      const latest = entries.length > 0 ? entries[entries.length - 1] : undefined;
      if (!latest) s.qa_lean_compiles_missing++;
      else if (latest.result === "pass") s.qa_lean_compiles_pass++;
      else if (latest.result === "fail") s.qa_lean_compiles_fail++;
      else if (latest.result === "warn") s.qa_lean_compiles_warn++;
      else if (latest.result === "n/a") s.qa_lean_compiles_na++;
      else s.qa_lean_compiles_missing++;
    }

    if (block.kind === "conjecture") {
      s.conjecture_total++;
      if (leanSrc !== undefined && declaresClass(leanSrc)) {
        s.conjecture_class_axiomatised++;
      }
    }
  }

  s.provable_sorry_free_pct = pctString(s.provable_sorry_free, s.provable_total);
  s.conjecture_class_axiomatised_pct = pctString(
    s.conjecture_class_axiomatised,
    s.conjecture_total,
  );
  return s;
}

// ── Witness I/O ──────────────────────────────────────────────────

interface LeanStatsWitness {
  computation: "lean-formalization-stats";
  description: string;
  paper: string;
  scriptFile: string;
  scriptHash: string;
  scriptCommitSha: string;
  computedAt: string;
  commitSha: string;
  data: LeanStats;
}

function repoHeadSha(): string {
  try {
    return execFileSync("git", ["-C", REPO_ROOT, "rev-parse", "HEAD"], {
      stdio: ["ignore", "pipe", "ignore"],
    })
      .toString()
      .trim();
  } catch {
    return "unknown";
  }
}

function buildWitness(paper: string, data: LeanStats): LeanStatsWitness {
  return {
    computation: "lean-formalization-stats",
    description:
      "Paper-level Lean formalization statistics derived from content " +
      "block manifests, .lean sources (comment-stripped sorry scan), " +
      "and .qa.json sidecars (proof-lean-compiles aggregate). Consumed " +
      "by content/values/registry.ts lean_* entries via :val[…] prose " +
      "directives. Regenerate: bun run pipeline/lean-stats-witness.ts --write",
    paper,
    scriptFile: SCRIPT_REL,
    scriptHash: hashFile(__filename) ?? "",
    scriptCommitSha: gitFileCommitSha(SCRIPT_REL, REPO_ROOT),
    computedAt: new Date().toISOString(),
    commitSha: repoHeadSha(),
    data,
  };
}

// ── Main ─────────────────────────────────────────────────────────

function main(): void {
  const args = parseArgs(process.argv.slice(2));
  const rootAbs = resolve(REPO_ROOT, "content", args.root);
  if (!existsSync(rootAbs)) {
    console.error(`[lean-stats] paper directory not found: ${rootAbs}`);
    process.exit(2);
  }

  const data = computeStats(rootAbs);
  const witnessAbs = resolve(REPO_ROOT, WITNESS_REL);

  if (args.mode === "check") {
    if (!existsSync(witnessAbs)) {
      console.error(
        `[lean-stats] DRIFT: ${WITNESS_REL} missing — run\n` +
          `  bun run pipeline/lean-stats-witness.ts --write`,
      );
      process.exit(1);
    }
    let onDisk: LeanStatsWitness;
    try {
      onDisk = JSON.parse(readFileSync(witnessAbs, "utf-8"));
    } catch {
      console.error(`[lean-stats] DRIFT: ${WITNESS_REL} unparseable`);
      process.exit(1);
      return;
    }
    const drift: string[] = [];
    for (const key of Object.keys(data) as Array<keyof LeanStats>) {
      const fresh = data[key];
      const stored = onDisk.data?.[key];
      if (String(fresh) !== String(stored)) {
        drift.push(`  ${key}: witness=${stored} actual=${fresh}`);
      }
    }
    if (onDisk.paper !== args.root) {
      drift.push(`  paper: witness=${onDisk.paper} actual=${args.root}`);
    }
    if (drift.length > 0) {
      console.error(
        `[lean-stats] DRIFT: ${WITNESS_REL} disagrees with a fresh recount:\n` +
          drift.join("\n") +
          `\nFix: bun run pipeline/lean-stats-witness.ts --write`,
      );
      process.exit(1);
    }
    console.log(`[lean-stats] OK — witness matches recount (${args.root})`);
    return;
  }

  if (args.mode === "write") {
    const witness = buildWitness(args.root, data);
    writeFileSync(witnessAbs, JSON.stringify(witness, null, 2) + "\n");
    console.log(`[lean-stats] wrote ${WITNESS_REL}`);
  }

  // Summary table (all modes).
  console.log(`\nLean formalization statistics — ${args.root}`);
  console.log(`  blocks total:                  ${data.blocks_total}`);
  console.log(`  blocks with .lean:             ${data.blocks_with_lean}`);
  console.log(
    `  provable claims:               ${data.provable_total}` +
      ` (thm ${data.theorem_total} / lem ${data.lemma_total}` +
      ` / prop ${data.proposition_total} / cor ${data.corollary_total})`,
  );
  console.log(`  provable with .lean:           ${data.provable_with_lean}`);
  console.log(
    `  provable sorry-free:           ${data.provable_sorry_free}` +
      ` (${data.provable_sorry_free_pct}%)`,
  );
  console.log(`  definitions:                   ${data.definition_total}`);
  console.log(`  conjectures:                   ${data.conjecture_total}`);
  console.log(
    `  conjectures class-axiomatised: ${data.conjecture_class_axiomatised}` +
      ` (${data.conjecture_class_axiomatised_pct}%)`,
  );
  console.log(
    `  qa proof-lean-compiles:        pass ${data.qa_lean_compiles_pass}` +
      ` / fail ${data.qa_lean_compiles_fail}` +
      ` / warn ${data.qa_lean_compiles_warn}` +
      ` / n-a ${data.qa_lean_compiles_na}` +
      ` / missing ${data.qa_lean_compiles_missing}\n`,
  );
}

main();
