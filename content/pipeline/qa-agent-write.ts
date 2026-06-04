/**
 * Shared agent/human QA-entry writer.
 *
 * Centralises the staleness-stamping that every audit (script, agent,
 * human) must perform, so it is *transparent to the audit*: a reviewer
 * supplies only the verdict (result / severity / evidence); this helper
 * captures the `field_hash` (current md/ts/lean source hashes),
 * `reviewed_at`, and `reviewed_sha` uniformly — identical to the
 * provenance `qa-sweep.ts` stamps on script entries.
 *
 * This is the write path used by the parallel agent-drain campaign:
 * a sub-agent evaluates one criterion on one block, then calls
 *
 *   bun run content/pipeline/qa-agent-write.ts \
 *     --block <base-path-without-extension> \
 *     --criterion <criterion-id> \
 *     --result pass|fail|warn|n/a \
 *     [--severity critical|major|minor] \
 *     [--evidence "file:line — verbatim quote"] \
 *     [--notes "..."] \
 *     [--model claude-opus-4-8] [--skill local/qa-agent-drain]
 *
 * Idempotent per (block, criterion, agent): any prior *stale* agent
 * entry for the same criterion (field_hash.md != current) is dropped
 * before the fresh one is appended; script + human + already-fresh
 * agent entries are preserved.
 *
 * @module content/pipeline/qa-agent-write
 */
import { existsSync } from "node:fs";
import { resolve, relative } from "node:path";
import {
  hashBlockFiles,
  gitHeadSha,
  loadQaReport,
  saveQaReport,
  readBlockManifest,
} from "./qa-utils";
import type {
  BlockQaReport,
  QaCriterionEntry,
} from "../../folio-assistant/schemas/block-qa";

const REPO_ROOT = resolve(import.meta.dir, "../..");

function arg(name: string): string | undefined {
  const i = process.argv.indexOf(`--${name}`);
  return i >= 0 ? process.argv[i + 1] : undefined;
}

function fail(msg: string): never {
  console.error(`qa-agent-write: ${msg}`);
  process.exit(2);
}

const blockArg = arg("block");
const criterion = arg("criterion");
const result = arg("result") as QaCriterionEntry["result"] | undefined;
if (!blockArg || !criterion || !result) {
  fail(
    "required: --block <base-path> --criterion <id> --result pass|fail|warn|n/a",
  );
}
const VALID_RESULTS = ["pass", "fail", "warn", "n/a"];
if (!VALID_RESULTS.includes(result!)) {
  fail(`--result must be one of ${VALID_RESULTS.join("|")} (got ${result})`);
}

const severity = arg("severity") as
  | "critical"
  | "major"
  | "minor"
  | undefined;
if (severity && !["critical", "major", "minor"].includes(severity)) {
  fail("--severity must be critical|major|minor");
}
const evidence = arg("evidence");
const notes = arg("notes");
const model = arg("model") ?? "claude-opus-4-8";
const skill = arg("skill") ?? "local/qa-agent-drain";

// Resolve the block triple from the base path (no extension).
const base = blockArg!.replace(/\.(ts|md|lean|qa\.json)$/, "");
const tsPath = `${base}.ts`;
if (!existsSync(tsPath)) fail(`block manifest not found: ${tsPath}`);
const mdPath = existsSync(`${base}.md`) ? `${base}.md` : undefined;
const leanPath = existsSync(`${base}.lean`) ? `${base}.lean` : undefined;
const qaPath = `${base}.qa.json`;

const paths = { ts: tsPath, md: mdPath, lean: leanPath };
const currentHashes = hashBlockFiles(paths);
const headSha = gitHeadSha();
const nowIso = new Date().toISOString();
const today = nowIso.slice(0, 10);

const manifest = readBlockManifest(tsPath);
const label = manifest?.label ?? base.split("/").pop()!;
const kind = manifest?.kind ?? "unknown";

const relPaths = {
  ts: relative(REPO_ROOT, tsPath),
  md: mdPath ? relative(REPO_ROOT, mdPath) : undefined,
  lean: leanPath ? relative(REPO_ROOT, leanPath) : undefined,
};

let report: BlockQaReport | undefined = loadQaReport(qaPath);
if (!report) {
  report = {
    $schema: "block-qa/v1",
    label,
    kind,
    paths: relPaths,
    source_hashes: currentHashes,
    criteria: {},
    updated_at: nowIso,
  };
}

// Refresh top-level provenance.
report.source_hashes = currentHashes;
report.updated_at = nowIso;

const entry: QaCriterionEntry = {
  field_hash: currentHashes,
  result: result!,
  ...(severity ? { severity } : {}),
  ...(evidence ? { evidence } : {}),
  reviewer: {
    kind: "agent",
    id: skill,
    agent_model: model,
    agent_date: today,
    agent_skill: skill,
  },
  reviewed_at: nowIso,
  reviewed_sha: headSha,
  ...(notes ? { notes } : {}),
};

const existing = report.criteria[criterion] ?? [];
// Drop prior *stale* agent entries for this criterion (same agent role);
// keep script, human, and already-fresh agent entries.
const kept = existing.filter((e) => {
  if (e.reviewer.kind !== "agent") return true;
  return (e.field_hash?.md ?? null) === (currentHashes.md ?? null);
});
report.criteria[criterion] = [...kept, entry];

saveQaReport(qaPath, report);
console.log(
  `qa-agent-write: ${criterion} = ${result}${severity ? ` (${severity})` : ""}  -> ${relative(REPO_ROOT, qaPath)}`,
);
