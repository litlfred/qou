/**
 * Shared utilities for QA sidecar tooling.
 *
 * @module content/pipeline/qa-utils
 */

import { createHash } from "crypto";
import {
  readFileSync,
  writeFileSync,
  existsSync,
  readdirSync,
  statSync,
} from "fs";
import { execSync } from "child_process";
import { join } from "path";
import type {
  BlockQaReport,
  QaFieldHash,
  QaCriterionEntry,
  QaScriptSidecar,
} from "../../folio-assistant/schemas/block-qa";
import { QA_CRITERIA_BY_ID } from "./qa-criteria-registry";

// ── Hashing ─────────────────────────────────────────────────────

/**
 * 12-char SHA-256 prefix of a file's UTF-8 bytes — mirrors
 * `folio-assistant/computations/witness_staleness_tracker.py`.
 */
export function hashFile(path: string): string | undefined {
  if (!existsSync(path)) return undefined;
  const buf = readFileSync(path);
  return createHash("sha256").update(buf).digest("hex").slice(0, 12);
}

/** Build a {md, ts, lean} hash bundle, omitting absent files. */
export function hashBlockFiles(paths: {
  md?: string;
  ts?: string;
  lean?: string;
}): QaFieldHash {
  const out: QaFieldHash = {};
  if (paths.md) {
    const h = hashFile(paths.md);
    if (h) out.md = h;
  }
  if (paths.ts) {
    const h = hashFile(paths.ts);
    if (h) out.ts = h;
  }
  if (paths.lean) {
    const h = hashFile(paths.lean);
    if (h) out.lean = h;
  }
  return out;
}

// ── Repo info ───────────────────────────────────────────────────

/** Current HEAD SHA (full). Returns empty string outside a git repo. */
export function gitHeadSha(): string {
  try {
    return execSync("git rev-parse HEAD", { stdio: ["ignore", "pipe", "ignore"] })
      .toString()
      .trim();
  } catch {
    return "";
  }
}

/**
 * Full git SHA of the most recent commit touching `path` (or empty
 * string if `path` is not tracked / outside a git repo). Used to
 * record `script_commit_sha` on each script-kind reviewer entry.
 */
export function gitFileCommitSha(path: string): string {
  try {
    return execSync(`git log -n 1 --format=%H -- "${path}"`, {
      stdio: ["ignore", "pipe", "ignore"],
    })
      .toString()
      .trim();
  } catch {
    return "";
  }
}

// ── Script-hash helpers ─────────────────────────────────────────

/**
 * 12-char SHA-256 prefix of the concatenated content of `paths`,
 * in the order given. Used for `deps_hash` on reviewer entries
 * (multiple extra inputs roll up into one fingerprint).
 */
export function hashFiles(paths: string[]): string | undefined {
  if (paths.length === 0) return undefined;
  const h = createHash("sha256");
  for (const p of paths) {
    if (!existsSync(p)) {
      h.update(`__absent__:${p}\n`);
      continue;
    }
    h.update(`__file__:${p}\n`);
    h.update(readFileSync(p));
    h.update("\n");
  }
  return h.digest("hex").slice(0, 12);
}

/**
 * Cache key for the script-hash bundle attached to one criterion.
 * Computed once per qa-sweep run and reused for every block under
 * sweep.
 */
export interface CriterionScriptHashes {
  /** Criterion id. */
  criterion_id: string;
  /** Path to checker source file (may not exist on disk). */
  source_file: string;
  /** 12-char SHA-256 of the source file. Empty if absent. */
  script_hash: string;
  /** Full git SHA of the file's most recent commit. */
  script_commit_sha: string;
  /** Resolved extra-input paths, in declared order. */
  extra_inputs: string[];
  /** 12-char SHA-256 over concat(extra_inputs). Undefined if no extras. */
  deps_hash?: string;
}

/**
 * Build the script-hash bundle for one criterion: hash its source
 * file + its extra-input files (if any). Pure read of disk; no
 * caching here — callers should memoize across the sweep run.
 *
 * `sourceFile` and `extraInputs` are repo-relative paths. `repoRoot`
 * is the absolute directory they should be resolved against — this
 * decouples the helper from `process.cwd()`, since qa-sweep runs
 * with cwd inside `content/`.
 */
export function computeCriterionScriptHashes(
  criterionId: string,
  sourceFile: string,
  extraInputs: string[] = [],
  repoRoot: string = process.cwd(),
): CriterionScriptHashes {
  const absSource = join(repoRoot, sourceFile);
  const absExtras = extraInputs.map((p) => join(repoRoot, p));
  return {
    criterion_id: criterionId,
    source_file: sourceFile,
    script_hash: hashFile(absSource) ?? "",
    script_commit_sha: gitFileCommitSha(absSource),
    extra_inputs: extraInputs,
    deps_hash: extraInputs.length > 0 ? hashFiles(absExtras) : undefined,
  };
}

// ── Block discovery ─────────────────────────────────────────────

export interface BlockPaths {
  /** Block label (e.g. `def:carbon-valence`). Read from the .ts file. */
  label: string;
  /** Block kind (`definition`, `proposition`, `remark`, …). */
  kind: string;
  /** Root name shared by all sibling files (e.g. `carbon-valence`). */
  root: string;
  /** Absolute paths to present sibling files. */
  ts: string;
  md?: string;
  lean?: string;
  qa?: string;
}

/**
 * Read `export default <kind>({ ... label: "...", ... })` from a .ts
 * manifest. Returns the block's kind + label, or `undefined` if the
 * file is not a single-block manifest (chapter, paper, etc.).
 *
 * Robust to surrounding fields; uses naive regex (no TypeScript
 * loader needed for this scan).
 */
export function readBlockManifest(
  tsPath: string,
): { kind: string; label: string } | undefined {
  if (!existsSync(tsPath)) return undefined;
  const src = readFileSync(tsPath, "utf-8");
  const kindMatch = src.match(
    /export\s+default\s+(definition|theorem|lemma|proposition|corollary|conjecture|example|remark|proof|prose|equation|diagram|simulator)\s*\(/,
  );
  if (!kindMatch) return undefined;
  const labelMatch = src.match(/\blabel\s*:\s*"([^"]+)"/);
  if (!labelMatch) return undefined;
  return { kind: kindMatch[1], label: labelMatch[1] };
}

/**
 * Walk a content directory (recursively) and yield every block
 * triple. Skips chapter manifests, paper manifests, and any .ts
 * file that is not a single-block manifest.
 */
export function* walkBlocks(rootDir: string): Generator<BlockPaths> {
  function* recurse(d: string): Generator<BlockPaths> {
    if (!existsSync(d)) return;
    for (const entry of readdirSync(d)) {
      if (entry.startsWith(".") || entry === "node_modules" || entry === "lean")
        continue;
      const full = join(d, entry);
      const st = statSync(full);
      if (st.isDirectory()) {
        yield* recurse(full);
      } else if (entry.endsWith(".ts")) {
        // Skip chapter / paper manifests by checking the export shape.
        const manifest = readBlockManifest(full);
        if (!manifest) continue;
        const root = full.slice(0, -3); // strip ".ts"
        const md = root + ".md";
        const lean = root + ".lean";
        const qa = root + ".qa.json";
        yield {
          label: manifest.label,
          kind: manifest.kind,
          root,
          ts: full,
          md: existsSync(md) ? md : undefined,
          lean: existsSync(lean) ? lean : undefined,
          qa: existsSync(qa) ? qa : undefined,
        };
      }
    }
  }
  yield* recurse(rootDir);
}

// ── QA report IO ────────────────────────────────────────────────

export function loadQaReport(path: string): BlockQaReport | undefined {
  if (!existsSync(path)) return undefined;
  try {
    const raw = JSON.parse(readFileSync(path, "utf-8"));
    if (raw?.$schema !== "block-qa/v1") return undefined;
    return raw as BlockQaReport;
  } catch {
    return undefined;
  }
}

export function saveQaReport(path: string, report: BlockQaReport): void {
  writeFileSync(path, JSON.stringify(report, null, 2) + "\n");
}

// ── Staleness check ─────────────────────────────────────────────

/**
 * A criterion entry is "fresh" iff every file the criterion depends
 * on has the same current hash as the entry's field_hash. Otherwise
 * the entry is stale (the source files have changed since the audit).
 *
 * An `n/a` entry is fresh iff the not-applicable condition still
 * holds: the file the entry was missing is still missing AND the
 * files the entry DID see have not changed.
 */
export function entryIsFresh(
  entry: QaCriterionEntry,
  current: QaFieldHash,
  depends_on: Array<"md" | "ts" | "lean">,
  current_script_hashes?: CriterionScriptHashes,
): boolean {
  // Uniform rule for every result kind: a file the criterion
  // depends on is "stable" iff (a) it was absent at audit AND is
  // absent now (the criterion's lean-side / md-side did not apply
  // then and still does not), OR (b) the hashes match.
  for (const k of depends_on) {
    const expected = entry.field_hash[k];
    const actual = current[k];
    if (!expected && !actual) continue; // both absent — still inapplicable
    if (!expected && actual) return false; // file appeared since audit
    if (expected && !actual) return false; // file removed since audit
    if (expected !== actual) return false; // file changed since audit
  }
  // Script-side staleness — only applies to `kind: "script"` entries
  // that were written by a sweep aware of the script-hash convention.
  // Legacy entries lacking these fields are treated as fresh: missing
  // metadata is not an invalidation signal.
  if (entry.reviewer.kind === "script" && current_script_hashes) {
    if (
      entry.reviewer.script_hash &&
      current_script_hashes.script_hash &&
      entry.reviewer.script_hash !== current_script_hashes.script_hash
    ) {
      return false; // checker source file changed
    }
    const recordedDepsHash = entry.reviewer.deps_hash;
    const currentDepsHash = current_script_hashes.deps_hash;
    if (
      recordedDepsHash &&
      currentDepsHash &&
      recordedDepsHash !== currentDepsHash
    ) {
      return false; // one of the extra inputs changed
    }
    // Asymmetry case: entry never recorded deps_hash but the
    // current criterion now declares extra_inputs. Treat as stale —
    // the new dep declaration must propagate.
    if (!recordedDepsHash && currentDepsHash) return false;
  }
  return true;
}

/**
 * Per-criterion freshness summary for one block.
 *
 * - `fresh-entries`: reviewer entries whose field_hash matches.
 * - `stale-entries`: reviewer entries whose field_hash does not match.
 * - `most_recent`: the newest entry (by reviewed_at), regardless of
 *   freshness; used by the watcher to surface "last result was X but
 *   it's stale" diagnostics.
 */
export interface CriterionFreshness {
  criterion: string;
  fresh_entries: QaCriterionEntry[];
  stale_entries: QaCriterionEntry[];
  most_recent?: QaCriterionEntry;
  is_fresh: boolean;
}

export function summariseFreshness(
  report: BlockQaReport,
  current: QaFieldHash,
  scriptHashesByCriterion?: Record<string, CriterionScriptHashes>,
): CriterionFreshness[] {
  const out: CriterionFreshness[] = [];
  for (const [criterion, entries] of Object.entries(report.criteria)) {
    const def = QA_CRITERIA_BY_ID[criterion];
    const dependsOn = def?.depends_on ?? ["md"];
    const sh = scriptHashesByCriterion?.[criterion];
    const fresh: QaCriterionEntry[] = [];
    const stale: QaCriterionEntry[] = [];
    for (const e of entries) {
      if (entryIsFresh(e, current, dependsOn, sh)) fresh.push(e);
      else stale.push(e);
    }
    const sorted = [...entries].sort((a, b) =>
      b.reviewed_at.localeCompare(a.reviewed_at),
    );
    out.push({
      criterion,
      fresh_entries: fresh,
      stale_entries: stale,
      most_recent: sorted[0],
      is_fresh: fresh.length > 0,
    });
  }
  return out;
}

// ── Script sidecar IO ──────────────────────────────────────────

/**
 * Repo-relative directory where per-criterion script sidecars live.
 * One file per automated criterion: `<criterion-id>.script.json`.
 */
export const SCRIPT_SIDECAR_DIR = "content/pipeline/script-sidecars";

/**
 * Resolve a criterion's script-sidecar path. `repoRoot` should be
 * the absolute path to the repo root; the sidecar lives under
 * `<repoRoot>/content/pipeline/script-sidecars/<id>.script.json`.
 */
export function scriptSidecarPath(
  criterionId: string,
  repoRoot: string = process.cwd(),
): string {
  return join(repoRoot, SCRIPT_SIDECAR_DIR, `${criterionId}.script.json`);
}

/** Load a script sidecar by criterion id; returns undefined if absent. */
export function loadQaScriptSidecar(
  criterionId: string,
  repoRoot: string = process.cwd(),
): QaScriptSidecar | undefined {
  const p = scriptSidecarPath(criterionId, repoRoot);
  if (!existsSync(p)) return undefined;
  try {
    return JSON.parse(readFileSync(p, "utf-8")) as QaScriptSidecar;
  } catch {
    return undefined;
  }
}

/** Write a script sidecar; deterministic JSON formatting. */
export function saveQaScriptSidecar(
  sidecar: QaScriptSidecar,
  repoRoot: string = process.cwd(),
): void {
  const p = scriptSidecarPath(sidecar.criterion_id, repoRoot);
  const dir = join(p, "..");
  if (!existsSync(dir)) {
    // Lazy mkdir; rely on the directory existing in the committed
    // tree under normal use, but tolerate a fresh checkout.
    execSync(`mkdir -p "${dir}"`);
  }
  writeFileSync(p, JSON.stringify(sidecar, null, 2) + "\n");
}
