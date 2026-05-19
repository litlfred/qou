/**
 * Per-content-block QA report schema.
 *
 * Each content block (a `.ts` + `.md` + optional `.lean` triple under
 * `content/`) may have a sibling `<block>.qa.json` audit-report file.
 * The report records, per QA criterion, the result of an audit pass
 * along with the source-file hashes at audit time so staleness can
 * be detected when a sibling file is later edited.
 *
 * Multiple reviewer entries per criterion are allowed (script +
 * agent + human adjudication). The first entry whose `field_hash`
 * still matches the current source files is the "fresh" entry for
 * that criterion.
 *
 * Authoritative reference for the architecture: the integration-
 * watcher skill family — see
 * `.claude/skills/local/one-voice-integration-watcher.md`.
 *
 * @module schemas/block-qa
 */

/**
 * The kind of reviewer that produced this finding.
 *
 * - `script`: a deterministic CLI (e.g. `qa-sweep.ts`) ran a grep /
 *   AST check. Reproducible. `id` is the script name + version.
 * - `agent`: an LLM-driven sub-agent (Claude, Copilot, Gemini) read
 *   the block and adjudicated. Not deterministic. `id` names the
 *   model + skill that called it.
 * - `human`: the repo owner (or a human collaborator) adjudicated.
 *   Final authority. `id` is the GitHub login.
 */
export type QaReviewerKind = "script" | "agent" | "human";

/**
 * Identity + provenance of a single QA reviewer entry.
 */
export interface QaReviewer {
  kind: QaReviewerKind;
  /** Stable identifier — script path, agent name, GitHub login. */
  id: string;
  /** Optional version pin (script revision, model id). */
  version?: string;
}

/**
 * Hash of the source files at the moment a criterion was audited.
 *
 * Each entry is a 12-char prefix of the SHA-256 of the file's
 * UTF-8 bytes — same convention as
 * `folio-assistant/computations/witness_staleness_tracker.py`.
 *
 * Absent fields mean the criterion's audit did not depend on that
 * file (or the file did not exist at audit time).
 */
export interface QaFieldHash {
  md?: string;
  ts?: string;
  lean?: string;
}

/**
 * The outcome of one reviewer evaluating one criterion on one block.
 *
 * `result: "pass"` — criterion satisfied. `evidence` may be empty.
 * `result: "fail"` — criterion violated. `evidence` must cite
 *   file:line + a verbatim quote of the offending text.
 * `result: "warn"` — borderline; reviewer flags but does not block.
 * `result: "n/a"` — criterion does not apply to this block kind.
 */
export interface QaCriterionEntry {
  /** Source-file hashes captured at audit time. */
  field_hash: QaFieldHash;
  /** Outcome. */
  result: "pass" | "fail" | "warn" | "n/a";
  /** Severity if `result` is `"fail"` or `"warn"`. */
  severity?: "critical" | "major" | "minor";
  /** Evidence: file:line + verbatim quote (for fail/warn). */
  evidence?: string;
  /** Reviewer identity + provenance. */
  reviewer: QaReviewer;
  /** When the audit ran (ISO-8601 UTC). */
  reviewed_at: string;
  /** Repo HEAD at audit time (full git SHA). */
  reviewed_sha: string;
  /** Free-form notes. */
  notes?: string;
}

/**
 * The full per-block QA report file shape.
 *
 * Filename: `<block-root>.qa.json` (sibling of `<block-root>.md`).
 *
 * `criteria` maps each named criterion to an **array** of reviewer
 * entries. Multiple entries are allowed; the criterion's "current
 * verdict" is the most recent entry whose `field_hash` matches the
 * present source files. If no entry matches, the criterion is
 * stale and requires re-audit.
 */
export interface BlockQaReport {
  /** Schema marker — value: `block-qa/v1`. */
  $schema: "block-qa/v1";
  /** Block label (e.g. `def:carbon-valence`, `rem:carbon-valence`). */
  label: string;
  /** Block kind (mirror of the .ts manifest's discriminator). */
  kind: string;
  /** Paths to source files, relative to repo root. */
  paths: {
    ts: string;
    md?: string;
    lean?: string;
  };
  /** Hashes of present source files (refreshed on every write). */
  source_hashes: QaFieldHash;
  /**
   * Per-criterion reviewer entries. Multiple reviewers (script +
   * agent + human) may co-exist; they are NOT deduplicated.
   */
  criteria: Record<string, QaCriterionEntry[]>;
  /** Report creation / last-update timestamp (ISO-8601 UTC). */
  updated_at: string;
}

/**
 * Definition of a single QA criterion — registered ahead of time
 * by the watcher's criterion catalog.
 */
export interface QaCriterionDefinition {
  /** Stable identifier (e.g. `voice-status-leak`). */
  id: string;
  /** Domain bucket — `voice`, `fit`, `framework`, `wall`, etc. */
  domain: string;
  /** Human-readable one-liner. */
  description: string;
  /** Default severity when the criterion fails. */
  default_severity: "critical" | "major" | "minor";
  /**
   * Which source files this criterion depends on.
   * Used to compute staleness: criterion is fresh iff every listed
   * file's current hash equals the reviewer entry's `field_hash`.
   */
  depends_on: Array<"md" | "ts" | "lean">;
  /**
   * Whether a deterministic script can run this criterion (true) or
   * it requires agent / human adjudication (false).
   */
  automated: boolean;
  /**
   * Optional gating: block kinds the criterion applies to.
   * Empty / undefined means "all kinds".
   */
  applies_to?: string[];
}
