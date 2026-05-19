#!/usr/bin/env bun
/**
 * QA sweep CLI — run automated criteria on every block under a path
 * and write / update per-block `<block>.qa.json` audit reports.
 *
 * Usage:
 *
 *   # Sweep one section (relative to repo root)
 *   bun run pipeline/qa-sweep.ts \
 *     content/quantum-observable-universe/organic-chemistry
 *
 *   # Sweep the whole paper
 *   bun run pipeline/qa-sweep.ts content/quantum-observable-universe
 *
 *   # Restrict to a single criterion
 *   bun run pipeline/qa-sweep.ts \
 *     content/.../organic-chemistry \
 *     --only voice-status-leak,voice-ai-slop
 *
 *   # Show what would change, write nothing
 *   bun run pipeline/qa-sweep.ts content/.../organic-chemistry --dry-run
 *
 *   # Emit a structured JSON summary to stdout (machine-readable)
 *   bun run pipeline/qa-sweep.ts content/... --json
 *
 * Behaviour:
 *
 *   - For each block triple under <root>, computes the current
 *     md/ts/lean SHA-256 prefixes.
 *   - Loads the existing <block>.qa.json (if any).
 *   - For each automated criterion:
 *       - If a fresh entry exists (field_hash matches current),
 *         skip — no need to re-audit.
 *       - Otherwise, run the checker and append a new reviewer
 *         entry with reviewer.kind="script", reviewer.id="qa-sweep".
 *   - Non-automated criteria (scholarly-default, ai-slop, fit-...)
 *     are reported as `needs-agent` in the summary but NOT written
 *     to the sidecar — the watcher dispatches an agent to fill those.
 *   - Writes the updated sidecar (unless --dry-run).
 *
 * Exit codes:
 *   0 — sweep complete, no critical findings
 *   1 — at least one critical finding (use in --ci)
 *   2 — invocation error
 *
 * @module content/pipeline/qa-sweep
 */

import { existsSync } from "fs";
import { resolve, relative } from "path";
import {
  hashBlockFiles,
  gitHeadSha,
  walkBlocks,
  loadQaReport,
  saveQaReport,
  entryIsFresh,
} from "./qa-utils";
import {
  QA_CRITERIA_REGISTRY,
  QA_CRITERIA_BY_ID,
  ONE_VOICE_WATCHER_CRITERIA,
} from "./qa-criteria-registry";
import { AUTOMATED_CHECKERS } from "./qa-checkers-voice";
import type {
  BlockQaReport,
  QaCriterionEntry,
} from "../../folio-assistant/schemas/block-qa";

// ── CLI parsing ─────────────────────────────────────────────────

interface Args {
  root: string;
  only?: string[];
  dryRun: boolean;
  json: boolean;
  ci: boolean;
}

function parseArgs(argv: string[]): Args {
  const out: Args = { root: "", dryRun: false, json: false, ci: false };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--dry-run") out.dryRun = true;
    else if (a === "--json") out.json = true;
    else if (a === "--ci") out.ci = true;
    else if (a === "--only") {
      out.only = (argv[++i] ?? "").split(",").filter(Boolean);
    } else if (!a.startsWith("--")) {
      if (!out.root) out.root = a;
    }
  }
  if (!out.root) {
    console.error(
      "usage: qa-sweep.ts <content-root> [--only ID,ID] [--dry-run] [--json] [--ci]",
    );
    process.exit(2);
  }
  return out;
}

// ── Sweep ───────────────────────────────────────────────────────

interface BlockSweepResult {
  label: string;
  kind: string;
  md?: string;
  ts: string;
  lean?: string;
  qa_path: string;
  criteria_run: number;
  criteria_skipped_fresh: number;
  criteria_needs_agent: number;
  fail_critical: number;
  fail_major: number;
  fail_minor: number;
  details: Array<{
    criterion: string;
    outcome:
      | "fresh-skip"
      | "pass"
      | "fail"
      | "needs-agent"
      | "n/a-no-md"
      | "n/a-no-lean";
    severity?: "critical" | "major" | "minor";
    hits?: number;
    first_hit?: string;
  }>;
}

function run(): void {
  const args = parseArgs(process.argv.slice(2));
  const rootAbs = resolve(args.root);
  if (!existsSync(rootAbs)) {
    console.error(`qa-sweep: root not found: ${rootAbs}`);
    process.exit(2);
  }

  const headSha = gitHeadSha();
  const nowIso = new Date().toISOString();
  const criteriaToRun =
    args.only && args.only.length > 0
      ? args.only.filter((id) => QA_CRITERIA_BY_ID[id])
      : ONE_VOICE_WATCHER_CRITERIA;

  const results: BlockSweepResult[] = [];

  let totalBlocks = 0;
  let totalCritical = 0;
  let totalMajor = 0;
  let totalMinor = 0;
  let totalNeedsAgent = 0;

  for (const block of walkBlocks(rootAbs)) {
    totalBlocks++;
    const paths = { md: block.md, ts: block.ts, lean: block.lean };
    const currentHashes = hashBlockFiles(paths);

    // Load or initialise report.
    const qaPath = block.root + ".qa.json";
    let report: BlockQaReport = loadQaReport(qaPath) ?? {
      $schema: "block-qa/v1",
      label: block.label,
      kind: block.kind,
      paths: {
        ts: relative(process.cwd(), block.ts),
        md: block.md ? relative(process.cwd(), block.md) : undefined,
        lean: block.lean ? relative(process.cwd(), block.lean) : undefined,
      },
      source_hashes: currentHashes,
      criteria: {},
      updated_at: nowIso,
    };

    // Refresh top-level metadata (paths / hashes may have shifted).
    report.label = block.label;
    report.kind = block.kind;
    report.paths = {
      ts: relative(process.cwd(), block.ts),
      md: block.md ? relative(process.cwd(), block.md) : undefined,
      lean: block.lean ? relative(process.cwd(), block.lean) : undefined,
    };
    report.source_hashes = currentHashes;

    const sweepResult: BlockSweepResult = {
      label: block.label,
      kind: block.kind,
      md: block.md ? relative(process.cwd(), block.md) : undefined,
      ts: relative(process.cwd(), block.ts),
      lean: block.lean ? relative(process.cwd(), block.lean) : undefined,
      qa_path: relative(process.cwd(), qaPath),
      criteria_run: 0,
      criteria_skipped_fresh: 0,
      criteria_needs_agent: 0,
      fail_critical: 0,
      fail_major: 0,
      fail_minor: 0,
      details: [],
    };

    for (const criterionId of criteriaToRun) {
      const def = QA_CRITERIA_BY_ID[criterionId];
      if (!def) continue;

      // Applicability gate.
      if (def.applies_to && !def.applies_to.includes(block.kind)) {
        continue;
      }

      // Skip if a fresh entry already exists.
      const existing = report.criteria[criterionId] ?? [];
      const freshExisting = existing.find((e) =>
        entryIsFresh(e, currentHashes, def.depends_on),
      );
      if (freshExisting) {
        sweepResult.criteria_skipped_fresh++;
        sweepResult.details.push({
          criterion: criterionId,
          outcome: "fresh-skip",
        });
        continue;
      }

      // If non-automated, mark as needing agent and continue.
      const checker = AUTOMATED_CHECKERS[criterionId];
      if (!def.automated || !checker) {
        sweepResult.criteria_needs_agent++;
        totalNeedsAgent++;
        sweepResult.details.push({
          criterion: criterionId,
          outcome: "needs-agent",
        });
        continue;
      }

      // If the criterion depends on a file the block doesn't have,
      // write an explicit n/a entry so the staleness scanner knows
      // the criterion was considered and judged not-applicable.
      if (def.depends_on.includes("md") && !block.md) {
        const naEntry: QaCriterionEntry = {
          field_hash: currentHashes,
          result: "n/a",
          reviewer: {
            kind: "script",
            id: "content/pipeline/qa-sweep.ts",
            version: "v1",
          },
          reviewed_at: nowIso,
          reviewed_sha: headSha,
          notes: "block has no .md sibling",
        };
        report.criteria[criterionId] = [...existing, naEntry];
        sweepResult.details.push({
          criterion: criterionId,
          outcome: "n/a-no-md",
        });
        continue;
      }
      if (def.depends_on.includes("lean") && !block.lean) {
        const naEntry: QaCriterionEntry = {
          field_hash: currentHashes,
          result: "n/a",
          reviewer: {
            kind: "script",
            id: "content/pipeline/qa-sweep.ts",
            version: "v1",
          },
          reviewed_at: nowIso,
          reviewed_sha: headSha,
          notes: "block has no .lean sibling",
        };
        report.criteria[criterionId] = [...existing, naEntry];
        sweepResult.details.push({
          criterion: criterionId,
          outcome: "n/a-no-lean",
        });
        continue;
      }

      // Run the automated checker.
      sweepResult.criteria_run++;
      const checkRes = checker(paths);
      const entry: QaCriterionEntry = {
        field_hash: currentHashes,
        result: checkRes.result,
        reviewer: {
          kind: "script",
          id: "content/pipeline/qa-sweep.ts",
          version: "v1",
        },
        reviewed_at: nowIso,
        reviewed_sha: headSha,
      };
      if (checkRes.result === "fail") {
        entry.severity = def.default_severity;
        entry.evidence = checkRes.hits
          .slice(0, 5)
          .map((h) => `${relative(process.cwd(), h.file)}:${h.line}: ${h.text}`)
          .join(" | ");
        if (def.default_severity === "critical") {
          sweepResult.fail_critical++;
          totalCritical++;
        } else if (def.default_severity === "major") {
          sweepResult.fail_major++;
          totalMajor++;
        } else {
          sweepResult.fail_minor++;
          totalMinor++;
        }
      }

      // Append the new entry (multiple reviewer entries co-exist).
      report.criteria[criterionId] = [...existing, entry];

      sweepResult.details.push({
        criterion: criterionId,
        outcome: checkRes.result,
        severity: entry.severity,
        hits: checkRes.hits.length,
        first_hit: checkRes.hits[0]
          ? `${relative(process.cwd(), checkRes.hits[0].file)}:${
              checkRes.hits[0].line
            }`
          : undefined,
      });
    }

    report.updated_at = nowIso;
    // Save if any criterion entry was added or refreshed (including n/a).
    const wroteSomething =
      sweepResult.criteria_run > 0 ||
      sweepResult.details.some(
        (d) => d.outcome === "n/a-no-md" || d.outcome === "n/a-no-lean",
      );
    if (!args.dryRun && wroteSomething) {
      saveQaReport(qaPath, report);
    }
    results.push(sweepResult);
  }

  // ── Output ────────────────────────────────────────────────────

  if (args.json) {
    console.log(
      JSON.stringify(
        {
          root: relative(process.cwd(), rootAbs),
          head: headSha,
          generated_at: nowIso,
          criteria: criteriaToRun,
          totals: {
            blocks: totalBlocks,
            fail_critical: totalCritical,
            fail_major: totalMajor,
            fail_minor: totalMinor,
            needs_agent: totalNeedsAgent,
          },
          results,
        },
        null,
        2,
      ),
    );
  } else {
    console.log(`qa-sweep: ${relative(process.cwd(), rootAbs)}`);
    console.log(`         HEAD: ${headSha.slice(0, 12) || "(no git)"}`);
    console.log(
      `         criteria: ${criteriaToRun.length}, blocks: ${totalBlocks}`,
    );
    console.log(
      `         findings: ${totalCritical} critical, ${totalMajor} major, ${totalMinor} minor; needs-agent: ${totalNeedsAgent}`,
    );
    console.log("");

    // Per-block summary, only show blocks with findings or needs-agent.
    for (const r of results) {
      if (
        r.fail_critical === 0 &&
        r.fail_major === 0 &&
        r.fail_minor === 0 &&
        r.criteria_needs_agent === 0
      ) {
        continue;
      }
      console.log(
        `  ${r.label}  (${r.kind})  → ${r.qa_path}`,
      );
      for (const d of r.details) {
        if (d.outcome === "fail") {
          console.log(
            `    [${d.severity}] ${d.criterion}: ${d.hits} hit(s)${
              d.first_hit ? `  first @ ${d.first_hit}` : ""
            }`,
          );
        } else if (d.outcome === "needs-agent") {
          console.log(`    [needs-agent] ${d.criterion}`);
        }
      }
    }
  }

  if (args.ci && totalCritical > 0) {
    process.exit(1);
  }
}

run();
