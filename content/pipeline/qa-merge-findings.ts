#!/usr/bin/env bun
/**
 * Merge a batch of agent / human QA findings into the per-block
 * `<block>.qa.json` sidecars. Each finding appends a new entry to
 * the named criterion's reviewer-entry array. Prior entries are
 * NEVER deleted — multi-reviewer history is preserved.
 *
 * Input format (JSON, via stdin or `--file <path>`):
 *
 *   {
 *     "reviewer": { "kind": "agent", "id": "<agent-name>", "version": "<model-id>" },
 *     "findings": [
 *       {
 *         "block_md": "content/.../carbon-valence.md",
 *         "criterion": "voice-scholarly-default",
 *         "result": "pass" | "fail" | "warn" | "n/a",
 *         "severity": "critical" | "major" | "minor",   // omit on pass / n/a
 *         "evidence": "<file:line: quote>",             // omit on pass / n/a
 *         "notes": "<free-form rationale>"
 *       },
 *       ...
 *     ]
 *   }
 *
 * Usage:
 *
 *   bun run pipeline/qa-merge-findings.ts --file findings.json
 *   bun run pipeline/qa-merge-findings.ts < findings.json
 *
 * @module content/pipeline/qa-merge-findings
 */

import { readFileSync, existsSync } from "fs";
import { resolve, relative } from "path";
import {
  hashBlockFiles,
  gitHeadSha,
  loadQaReport,
  saveQaReport,
} from "./qa-utils";
import { QA_CRITERIA_BY_ID } from "./qa-criteria-registry";
import type {
  BlockQaReport,
  QaCriterionEntry,
  QaReviewer,
} from "../../folio-assistant/schemas/block-qa";

interface FindingInput {
  block_md?: string;
  block_ts?: string;
  block_root?: string;
  criterion: string;
  result: "pass" | "fail" | "warn" | "n/a";
  severity?: "critical" | "major" | "minor";
  evidence?: string;
  notes?: string;
}

interface BatchInput {
  reviewer: QaReviewer;
  findings: FindingInput[];
}

function readStdin(): string {
  return readFileSync(0, "utf-8");
}

function parseArgs(argv: string[]): { file?: string } {
  for (let i = 0; i < argv.length; i++) {
    if (argv[i] === "--file" && argv[i + 1]) return { file: argv[i + 1] };
  }
  return {};
}

function blockRootFromInput(f: FindingInput): string | undefined {
  if (f.block_root) return f.block_root;
  if (f.block_md) return f.block_md.replace(/\.md$/, "");
  if (f.block_ts) return f.block_ts.replace(/\.ts$/, "");
  return undefined;
}

function run(): void {
  const args = parseArgs(process.argv.slice(2));
  const raw = args.file ? readFileSync(args.file, "utf-8") : readStdin();
  const batch: BatchInput = JSON.parse(raw);
  if (!batch.reviewer || !Array.isArray(batch.findings)) {
    console.error("input must have { reviewer, findings: [] }");
    process.exit(2);
  }
  if (batch.reviewer.kind !== "agent" && batch.reviewer.kind !== "human") {
    console.error("reviewer.kind must be 'agent' or 'human' (use qa-sweep.ts for scripts)");
    process.exit(2);
  }

  const headSha = gitHeadSha();
  const nowIso = new Date().toISOString();
  let added = 0;
  let skipped = 0;

  for (const f of batch.findings) {
    const root = blockRootFromInput(f);
    if (!root) {
      console.error("finding missing block_md / block_ts / block_root:", f);
      skipped++;
      continue;
    }
    const rootAbs = resolve(root);
    const tsPath = rootAbs + ".ts";
    const mdPath = rootAbs + ".md";
    const leanPath = rootAbs + ".lean";
    const qaPath = rootAbs + ".qa.json";
    if (!existsSync(tsPath)) {
      console.error(`no .ts manifest at ${tsPath}`);
      skipped++;
      continue;
    }
    const def = QA_CRITERIA_BY_ID[f.criterion];
    if (!def) {
      console.error(`unknown criterion: ${f.criterion}`);
      skipped++;
      continue;
    }

    const currentHashes = hashBlockFiles({
      md: existsSync(mdPath) ? mdPath : undefined,
      ts: tsPath,
      lean: existsSync(leanPath) ? leanPath : undefined,
    });

    let report: BlockQaReport | undefined = loadQaReport(qaPath);
    if (!report) {
      // Bootstrap a fresh sidecar — agent can write the first
      // entry even if qa-sweep hasn't run yet.
      const label = (() => {
        const src = readFileSync(tsPath, "utf-8");
        const m = src.match(/\blabel\s*:\s*"([^"]+)"/);
        return m?.[1] ?? "unknown";
      })();
      const kind = (() => {
        const src = readFileSync(tsPath, "utf-8");
        const m = src.match(
          /export\s+default\s+(definition|theorem|lemma|proposition|corollary|conjecture|example|remark|proof|prose|equation|diagram|simulator)\s*\(/,
        );
        return m?.[1] ?? "unknown";
      })();
      report = {
        $schema: "block-qa/v1",
        label,
        kind,
        paths: {
          ts: relative(process.cwd(), tsPath),
          md: existsSync(mdPath) ? relative(process.cwd(), mdPath) : undefined,
          lean: existsSync(leanPath)
            ? relative(process.cwd(), leanPath)
            : undefined,
        },
        source_hashes: currentHashes,
        criteria: {},
        updated_at: nowIso,
      };
    }
    // Refresh source hashes (best-effort).
    report.source_hashes = currentHashes;

    const entry: QaCriterionEntry = {
      field_hash: currentHashes,
      result: f.result,
      reviewer: batch.reviewer,
      reviewed_at: nowIso,
      reviewed_sha: headSha,
    };
    if (f.severity) entry.severity = f.severity;
    if (f.evidence) entry.evidence = f.evidence;
    if (f.notes) entry.notes = f.notes;

    const existing = report.criteria[f.criterion] ?? [];
    report.criteria[f.criterion] = [...existing, entry];
    report.updated_at = nowIso;
    saveQaReport(qaPath, report);
    added++;
  }

  console.log(
    JSON.stringify(
      {
        added,
        skipped,
        reviewer: batch.reviewer,
        head: headSha,
      },
      null,
      2,
    ),
  );
}

run();
