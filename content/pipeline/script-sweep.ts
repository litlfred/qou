/**
 * CLI driver for the script-QA pipeline.
 *
 * Walks every script under `SCRIPT_ROOTS` (currently
 * `folio-assistant/computations/*.py`), runs every automated
 * criterion in the `script-quality` domain, and writes one
 * `<basename>.script-qa.json` sidecar per audited script under the
 * `script-qa/` subdirectory of the script's parent dir.
 *
 * Usage:
 *
 *   bun run content/pipeline/script-sweep.ts [--dry-run] [--json]
 *                                            [--only ID[,ID]]
 *                                            [--filter REGEX]
 *
 * `--only` restricts to the listed criterion ids (default: every
 * `domain: "script-quality"` criterion). `--filter REGEX` matches
 * against repo-relative script paths.
 *
 * @module content/pipeline/script-sweep
 */

import { writeFileSync, existsSync, mkdirSync, readFileSync } from "fs";
import { dirname, relative, resolve } from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const REPO_ROOT = resolve(dirname(__filename), "..", "..");

import {
  QA_CRITERIA_REGISTRY,
  QA_CRITERIA_BY_ID,
  SCRIPT_QUALITY_CRITERIA,
  getCriterionSourceFile,
  getCriterionExtraInputs,
} from "./qa-criteria-registry";
import {
  gitHeadSha,
  computeCriterionScriptHashes,
  entryIsFresh,
  saveQaScriptSidecar,
  type CriterionScriptHashes,
} from "./qa-utils";
import { walkScripts, type ScriptTarget } from "./script-walker";
import { checkDoesNotDefaultToFloat } from "./qa-checkers-python";
import type { CheckerResult } from "./qa-checkers-voice";
import type {
  ScriptQaReport,
  ScriptLanguage,
} from "../../folio-assistant/schemas/script-qa";
import type {
  QaCriterionEntry,
  QaScriptSidecar,
} from "../../folio-assistant/schemas/block-qa";

// ─── Dispatch ──────────────────────────────────────────────────

/**
 * Dispatch from criterion id + script target to a `CheckerResult`.
 * Each criterion knows which languages it supports; out-of-band
 * combinations return `n/a`.
 */
const SCRIPT_CHECKERS: Record<
  string,
  (target: ScriptTarget) => CheckerResult
> = {
  does_not_default_to_float: (t) => {
    if (t.language !== "python") return { result: "n/a", hits: [] };
    return checkDoesNotDefaultToFloat(t.abs);
  },
};

// ─── CLI ───────────────────────────────────────────────────────

interface Args {
  dryRun: boolean;
  json: boolean;
  only?: string[];
  filter?: RegExp;
}

function parseArgs(argv: string[]): Args {
  const out: Args = { dryRun: false, json: false };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--dry-run") out.dryRun = true;
    else if (a === "--json") out.json = true;
    else if (a === "--only") {
      out.only = (argv[++i] ?? "").split(",").filter(Boolean);
    } else if (a === "--filter") {
      out.filter = new RegExp(argv[++i] ?? "");
    }
  }
  return out;
}

// ─── Sweep ─────────────────────────────────────────────────────

interface ScriptSweepResult {
  script_path: string;
  language: ScriptLanguage;
  criteria_run: number;
  criteria_skipped_fresh: number;
  fail_critical: number;
  fail_major: number;
  fail_minor: number;
  first_hit?: string;
}

function loadScriptQa(path: string): ScriptQaReport | undefined {
  if (!existsSync(path)) return undefined;
  try {
    return JSON.parse(readFileSync(path, "utf-8")) as ScriptQaReport;
  } catch {
    return undefined;
  }
}

function saveScriptQa(path: string, report: ScriptQaReport): void {
  mkdirSync(dirname(path), { recursive: true });
  writeFileSync(path, JSON.stringify(report, null, 2) + "\n");
}

async function run(): Promise<void> {
  const args = parseArgs(process.argv.slice(2));
  const nowIso = new Date().toISOString();
  const headSha = gitHeadSha();

  // Resolve criteria under sweep — default to every script-quality
  // criterion that has a registered checker.
  const requestedIds = args.only ?? SCRIPT_QUALITY_CRITERIA;
  const runnableIds = requestedIds.filter(
    (id) => QA_CRITERIA_BY_ID[id]?.automated && SCRIPT_CHECKERS[id],
  );

  // Precompute the script-hash bundle per criterion (mirrors
  // qa-sweep tranche-1 plumbing).
  const scriptHashesByCriterion: Record<string, CriterionScriptHashes> = {};
  for (const id of runnableIds) {
    scriptHashesByCriterion[id] = computeCriterionScriptHashes(
      id,
      getCriterionSourceFile(id),
      getCriterionExtraInputs(id),
      REPO_ROOT,
    );
  }
  const engineVersion = `bun-${Bun.version}`;

  const results: ScriptSweepResult[] = [];
  let totalScripts = 0;
  let totalCritical = 0;
  let totalMajor = 0;
  let totalMinor = 0;

  for (const target of walkScripts(REPO_ROOT)) {
    if (args.filter && !args.filter.test(target.rel)) continue;
    totalScripts++;

    const existing = loadScriptQa(target.sidecar_abs);
    const report: ScriptQaReport = existing ?? {
      $schema: "script-qa/v1",
      script_path: target.rel,
      language: target.language,
      source_hash: target.source_hash,
      updated_at: nowIso,
      criteria: {},
    };
    const metadataDrifted =
      !!existing &&
      (existing.script_path !== target.rel ||
        existing.language !== target.language ||
        existing.source_hash !== target.source_hash);
    report.script_path = target.rel;
    report.language = target.language;
    report.source_hash = target.source_hash;

    // Per-target field hash. `"ts"` is the QaFieldHash convention
    // for the primary source file across every QA axis; in the
    // script-quality axis it carries the audited script's content
    // hash regardless of extension (`.py`, `.rs`, …).
    const currentHashes = { ts: target.source_hash };

    const sweepRow: ScriptSweepResult = {
      script_path: target.rel,
      language: target.language,
      criteria_run: 0,
      criteria_skipped_fresh: 0,
      fail_critical: 0,
      fail_major: 0,
      fail_minor: 0,
    };

    let anyChange = false;
    for (const cid of runnableIds) {
      const def = QA_CRITERIA_BY_ID[cid];
      const checker = SCRIPT_CHECKERS[cid];
      if (!def || !checker) continue;

      // Freshness short-circuit (mirrors qa-sweep.ts:266-282). Skip
      // the checker entirely when a prior entry's `field_hash` +
      // checker `script_hash` still match — prevents unbounded
      // sidecar growth and constant git churn on `updated_at`.
      const sh = scriptHashesByCriterion[cid];
      const prevEntries = report.criteria[cid] ?? [];
      const freshExisting = prevEntries.find((e) =>
        entryIsFresh(e, currentHashes, def.depends_on, sh),
      );
      if (freshExisting) {
        sweepRow.criteria_skipped_fresh++;
        continue;
      }

      const checkRes = checker(target);
      const entry: QaCriterionEntry = {
        field_hash: currentHashes,
        result: checkRes.result,
        reviewer: {
          kind: "script",
          id: sh?.source_file ?? "content/pipeline/script-sweep.ts",
          version: "v1",
          script_hash: sh?.script_hash || undefined,
          script_commit_sha: sh?.script_commit_sha || undefined,
          deps_hash: sh?.deps_hash,
        },
        reviewed_at: nowIso,
        reviewed_sha: headSha,
      };
      if (checkRes.result === "fail") {
        entry.severity = def.default_severity;
        entry.evidence = checkRes.hits
          .slice(0, 5)
          .map((h) => `${relative(REPO_ROOT, h.file)}:${h.line}: ${h.text}`)
          .join(" | ");
        if (def.default_severity === "critical") {
          sweepRow.fail_critical++;
          totalCritical++;
        } else if (def.default_severity === "major") {
          sweepRow.fail_major++;
          totalMajor++;
        } else {
          sweepRow.fail_minor++;
          totalMinor++;
        }
        sweepRow.first_hit ??= entry.evidence?.slice(0, 80);
      }
      report.criteria[cid] = [...prevEntries, entry];
      sweepRow.criteria_run++;
      anyChange = true;
    }

    const wroteSomething = anyChange || metadataDrifted || !existing;
    if (!args.dryRun && wroteSomething) {
      report.updated_at = nowIso;
      saveScriptQa(target.sidecar_abs, report);
    }
    if (
      sweepRow.criteria_run > 0 ||
      sweepRow.criteria_skipped_fresh > 0
    ) {
      results.push(sweepRow);
    }
  }

  // Refresh per-criterion script sidecars (same convention as
  // qa-sweep) so consumers can ask "is this checker stale?" in one
  // lookup.
  if (!args.dryRun) {
    for (const [id, sh] of Object.entries(scriptHashesByCriterion)) {
      if (!sh.script_hash) continue;
      const sidecar: QaScriptSidecar = {
        $schema: "qa-script/v1",
        criterion_id: id,
        source_file: sh.source_file,
        script_hash: sh.script_hash,
        script_commit_sha: sh.script_commit_sha,
        extra_inputs:
          sh.extra_inputs.length > 0 ? sh.extra_inputs : undefined,
        deps_hash: sh.deps_hash,
        last_run_at: nowIso,
        last_run_sha: headSha,
        engine_version: engineVersion,
      };
      saveQaScriptSidecar(sidecar, REPO_ROOT);
    }
  }

  if (args.json) {
    console.log(
      JSON.stringify(
        {
          generated_at: nowIso,
          head: headSha,
          totals: {
            scripts: totalScripts,
            fail_critical: totalCritical,
            fail_major: totalMajor,
            fail_minor: totalMinor,
          },
          results,
        },
        null,
        2,
      ),
    );
  } else {
    console.log(`script-sweep: ${totalScripts} script(s) audited`);
    console.log(`           HEAD: ${headSha.slice(0, 12) || "(no git)"}`);
    console.log(`           criteria: ${runnableIds.join(", ")}`);
    console.log(
      `           findings: ${totalCritical} critical, ${totalMajor} major, ${totalMinor} minor`,
    );
    if (results.length > 0) {
      console.log("");
      // Show top 15 failing scripts only, to keep output scannable.
      const failing = results.filter(
        (r) => r.fail_critical + r.fail_major + r.fail_minor > 0,
      );
      console.log(`           ${failing.length} script(s) with findings:`);
      for (const r of failing.slice(0, 15)) {
        const totalFails =
          r.fail_critical + r.fail_major + r.fail_minor;
        console.log(`             ${r.script_path}  (${totalFails} hit${totalFails > 1 ? "s" : ""})`);
      }
      if (failing.length > 15) {
        console.log(`             … ${failing.length - 15} more`);
      }
    }
  }
}

run();
