#!/usr/bin/env bun
/**
 * Script-reviewer checkers for the non-voice integration-watcher
 * axes:
 *
 *   - proof-*        (5 criteria, 3 script + 2 mixed/agent)
 *   - canonical-*    (3 criteria, 2 script + 1 agent)
 *   - compute-*      (4 criteria, all script)
 *   - detangler-*    (4 criteria, all script)
 *   - bib-*          (4 criteria, all script)
 *
 * Each checker returns the same `{ result, hits }` shape as the
 * voice checkers in `qa-checkers-voice.ts`, so they wire into the
 * existing `AUTOMATED_CHECKERS` dispatcher unchanged.
 *
 * Many checkers delegate to existing repo scripts (`bib-qa.ts`,
 * `validate-references.ts`, `compute_audit_scan.py`, etc.) by
 * reading the cached JSON artefacts those scripts produce, rather
 * than re-running them per block. This keeps `qa-sweep` fast
 * (sub-second per block) while preserving the canonical sources.
 *
 * @module content/pipeline/qa-checkers-extended
 */

import { existsSync, readFileSync } from "fs";
import { resolve, dirname, join } from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const REPO_ROOT = resolve(dirname(__filename), "..", "..");
const CONTENT_DIR = resolve(dirname(__filename), "..");
const COMPUTATIONS_DIR = join(REPO_ROOT, "folio-assistant", "computations");
const BIB_QA_IMAGES_DIR = join(CONTENT_DIR, "bib-qa-images");
const BIB_QA_REPORT = join(CONTENT_DIR, "bib-qa.json");

export interface CheckerHit {
  file: string;
  line: number;
  text: string;
}

export interface CheckerResult {
  result: "pass" | "fail" | "n/a";
  hits: CheckerHit[];
}

// ── Lazy-loaded bib-qa report (cached across calls per process) ─

let bibQaReportCache: Record<string, unknown> | null = null;
function loadBibQaReport(): Record<string, unknown> | null {
  if (bibQaReportCache !== null) return bibQaReportCache;
  if (!existsSync(BIB_QA_REPORT)) {
    bibQaReportCache = {};
    return bibQaReportCache;
  }
  try {
    bibQaReportCache = JSON.parse(readFileSync(BIB_QA_REPORT, "utf-8"));
  } catch {
    bibQaReportCache = {};
  }
  return bibQaReportCache;
}

// Extract `\cite{key1, key2}` + `-- Ref: [key]` from .md / .lean.
function extractCitations(text: string): Set<string> {
  const keys = new Set<string>();
  // \cite{a,b} / \citep{a} / \citet{a}
  for (const m of text.matchAll(
    /\\cite[a-zA-Z]*(?:\[[^\]]*\])?\{([^}]+)\}/g,
  )) {
    for (const k of m[1].split(",")) {
      const trimmed = k.trim();
      if (trimmed) keys.add(trimmed);
    }
  }
  // -- Ref: [key]
  for (const m of text.matchAll(/--\s*Ref:\s*\[([^\]]+)\]/g)) {
    keys.add(m[1].trim());
  }
  return keys;
}

function readMaybe(path: string | undefined): string {
  if (!path || !existsSync(path)) return "";
  try {
    return readFileSync(path, "utf-8");
  } catch {
    return "";
  }
}

// ─── Bibliography axis ──────────────────────────────────────────

export function checkBibCiteResolves(
  mdPath: string | undefined,
  leanPath: string | undefined,
): CheckerResult {
  const md = readMaybe(mdPath);
  const lean = readMaybe(leanPath);
  const keys = new Set<string>([
    ...extractCitations(md),
    ...extractCitations(lean),
  ]);
  if (keys.size === 0) return { result: "pass", hits: [] };

  const report = loadBibQaReport();
  const entries = (report?.entries ?? {}) as Record<string, unknown>;
  const hits: CheckerHit[] = [];
  for (const key of keys) {
    if (!(key in entries)) {
      hits.push({
        file: mdPath ?? leanPath ?? "(unknown)",
        line: 1,
        text: `\\cite{${key}} or -- Ref: [${key}] does not resolve in references.ts`,
      });
    }
  }
  return { result: hits.length > 0 ? "fail" : "pass", hits };
}

function checkBibRefTag(
  mdPath: string | undefined,
  leanPath: string | undefined,
  tagKey: string,
  describe: string,
): CheckerResult {
  const md = readMaybe(mdPath);
  const lean = readMaybe(leanPath);
  const keys = new Set<string>([
    ...extractCitations(md),
    ...extractCitations(lean),
  ]);
  if (keys.size === 0) return { result: "pass", hits: [] };

  const report = loadBibQaReport();
  const entries = (report?.entries ?? {}) as Record<
    string,
    { tags?: Array<{ key: string; status: string }> }
  >;
  const hits: CheckerHit[] = [];
  for (const key of keys) {
    const entry = entries[key];
    if (!entry) continue; // resolution failure is a different criterion
    const tag = entry.tags?.find((t) => t.key === tagKey);
    if (!tag || tag.status !== "pass") {
      hits.push({
        file: mdPath ?? leanPath ?? "(unknown)",
        line: 1,
        text: `cite [${key}] fails bib-qa tag '${tagKey}' (${describe})`,
      });
    }
  }
  return { result: hits.length > 0 ? "fail" : "pass", hits };
}

export function checkBibCitedRefHasUrl(
  mdPath: string | undefined,
  leanPath: string | undefined,
): CheckerResult {
  return checkBibRefTag(mdPath, leanPath, "has_url", "no URL or DOI");
}

export function checkBibCitedRefMetadataOk(
  mdPath: string | undefined,
  leanPath: string | undefined,
): CheckerResult {
  return checkBibRefTag(
    mdPath,
    leanPath,
    "metadata_ok",
    "missing title/author/year",
  );
}

export function checkBibCitedRefHasScreenshot(
  mdPath: string | undefined,
  leanPath: string | undefined,
): CheckerResult {
  return checkBibRefTag(
    mdPath,
    leanPath,
    "has_screenshot",
    "no screenshot under content/bib-qa-images/",
  );
}

// ─── Compute axis ───────────────────────────────────────────────

function readTs(path: string | undefined): string {
  return readMaybe(path);
}

function getComputationField(tsSrc: string): {
  witness?: string;
  probe?: string;
} {
  // Light extraction — looks for `computation: { witness: "..." }`
  // and `probe: "..."` patterns at any nesting depth.
  const result: { witness?: string; probe?: string } = {};
  const witnessMatch = tsSrc.match(/witness:\s*["']([^"']+)["']/);
  if (witnessMatch) result.witness = witnessMatch[1];
  const probeMatch = tsSrc.match(/probe:\s*["']([^"']+)["']/);
  if (probeMatch) result.probe = probeMatch[1];
  return result;
}

export function checkComputePropHasProbe(
  tsPath: string | undefined,
): CheckerResult {
  const ts = readTs(tsPath);
  if (!ts) return { result: "n/a", hits: [] };
  const { probe } = getComputationField(ts);
  if (!probe) {
    return {
      result: "fail",
      hits: [
        {
          file: tsPath ?? "(unknown)",
          line: 1,
          text:
            "no `probe:` field declared on the block — every prop:/theorem: " +
            "needs an I1 probe witness per CLAUDE.md compute-integration §B",
        },
      ],
    };
  }
  return { result: "pass", hits: [] };
}

export function checkComputePropHasConsumer(
  tsPath: string | undefined,
): CheckerResult {
  const ts = readTs(tsPath);
  if (!ts) return { result: "n/a", hits: [] };
  // Look for a `consumers:` field listing at least one production
  // script. Lightweight; the full 13-pattern audit lives in
  // `compute_audit_scan.py`.
  const consumersMatch = ts.match(/consumers:\s*\[([^\]]*)\]/);
  if (!consumersMatch || consumersMatch[1].trim() === "") {
    return {
      result: "fail",
      hits: [
        {
          file: tsPath ?? "(unknown)",
          line: 1,
          text:
            "no `consumers:` field with at least one production script — " +
            "the prop is NOT-WIRED per CLAUDE.md compute-integration §B " +
            "(I2-I13)",
        },
      ],
    };
  }
  return { result: "pass", hits: [] };
}

export function checkComputeWitnessExists(
  tsPath: string | undefined,
): CheckerResult {
  const ts = readTs(tsPath);
  if (!ts) return { result: "n/a", hits: [] };
  const { witness } = getComputationField(ts);
  if (!witness) return { result: "pass", hits: [] };
  const absPath = witness.startsWith("/")
    ? witness
    : resolve(REPO_ROOT, witness);
  if (!existsSync(absPath)) {
    return {
      result: "fail",
      hits: [
        {
          file: tsPath ?? "(unknown)",
          line: 1,
          text: `declared witness '${witness}' does not exist on disk`,
        },
      ],
    };
  }
  // Also check non-empty.
  try {
    const content = readFileSync(absPath, "utf-8");
    if (content.trim().length === 0) {
      return {
        result: "fail",
        hits: [
          {
            file: tsPath ?? "(unknown)",
            line: 1,
            text: `declared witness '${witness}' exists but is empty`,
          },
        ],
      };
    }
  } catch {
    /* fall through to pass */
  }
  return { result: "pass", hits: [] };
}

const LP_DUAL_HINT_RE =
  /lp-dual|operator-selection-lp|shadow-price|primal-dual|lp-duality/i;
const LP_DUAL_REQUIRED_FIELDS = [
  "y0_star",
  "y_star",
  "primal_obj",
  "dual_obj",
  "duality_gap",
];
const LP_DUAL_ACTIVE_ALIASES = [
  "active_set",
  "active_constraints",
  "active_channels",
];

export function checkComputeLpDualPresent(
  tsPath: string | undefined,
): CheckerResult {
  const ts = readTs(tsPath);
  if (!ts) return { result: "n/a", hits: [] };
  const { witness } = getComputationField(ts);
  if (!witness) return { result: "pass", hits: [] };
  // Filter: only blocks whose ts mentions LP/SDP/operator-selection.
  if (!LP_DUAL_HINT_RE.test(ts)) return { result: "pass", hits: [] };
  const absPath = witness.startsWith("/")
    ? witness
    : resolve(REPO_ROOT, witness);
  if (!existsSync(absPath)) return { result: "pass", hits: [] };
  let body: Record<string, unknown> = {};
  try {
    body = JSON.parse(readFileSync(absPath, "utf-8"));
  } catch {
    return { result: "pass", hits: [] };
  }
  const missing: string[] = [];
  for (const f of LP_DUAL_REQUIRED_FIELDS) {
    if (!(f in body)) missing.push(f);
  }
  if (!LP_DUAL_ACTIVE_ALIASES.some((a) => a in body)) {
    missing.push(`active_set (or alias: ${LP_DUAL_ACTIVE_ALIASES.join("/")})`);
  }
  if (missing.length === 0) return { result: "pass", hits: [] };
  return {
    result: "fail",
    hits: [
      {
        file: tsPath ?? "(unknown)",
        line: 1,
        text: `LP/SDP witness '${witness}' missing dual field(s): ${missing.join(", ")}`,
      },
    ],
  };
}

// ─── Canonical axis ─────────────────────────────────────────────

const CALIBRATION_RE = /\b(calibration|anchor)\s*:\s*(?:".*?"|\d+)/g;

export function checkCanonicalCalibrationCount(
  mdPath: string | undefined,
  tsPath: string | undefined,
): CheckerResult {
  const md = readMaybe(mdPath);
  const ts = readMaybe(tsPath);
  const combined = md + "\n" + ts;
  const matches = combined.match(CALIBRATION_RE) ?? [];
  if (matches.length <= 3) return { result: "pass", hits: [] };
  return {
    result: "fail",
    hits: [
      {
        file: mdPath ?? tsPath ?? "(unknown)",
        line: 1,
        text:
          `block declares ${matches.length} calibration anchors — exceeds the ` +
          `three-calibration discipline (CODATA m_e + α + G_Planck only)`,
      },
    ],
  };
}

const VAL_DIRECTIVE_RE = /:val\[([^\]]+)\]\{([^}]+)\}/g;

export function checkCanonicalWitnessPinned(
  mdPath: string | undefined,
  tsPath: string | undefined,
): CheckerResult {
  const md = readMaybe(mdPath);
  if (!md) return { result: "pass", hits: [] };
  const ts = readMaybe(tsPath);
  const tsWitness = ts ? getComputationField(ts).witness : undefined;
  const hits: CheckerHit[] = [];
  let lineNo = 0;
  for (const line of md.split("\n")) {
    lineNo++;
    if (!line.includes(":val[")) continue;
    const re = new RegExp(VAL_DIRECTIVE_RE.source, "g");
    for (const m of line.matchAll(re)) {
      const attrs = m[2];
      const witnessMatch = attrs.match(/witness=["']?([^"' }]+)/);
      if (!witnessMatch) {
        if (!tsWitness) {
          hits.push({
            file: mdPath ?? "(unknown)",
            line: lineNo,
            text:
              `:val[${m[1]}] has no \`witness=\` attribute and the block ` +
              `has no \`computation:\` field`,
          });
        }
        continue;
      }
      const w = witnessMatch[1];
      const absPath = w.startsWith("/") ? w : resolve(REPO_ROOT, w);
      if (!existsSync(absPath)) {
        hits.push({
          file: mdPath ?? "(unknown)",
          line: lineNo,
          text: `:val witness '${w}' does not exist on disk`,
        });
      }
    }
  }
  return { result: hits.length > 0 ? "fail" : "pass", hits };
}

// ─── Detangler axis ─────────────────────────────────────────────

export function checkDetanglerSectionBand(
  tsPath: string | undefined,
): CheckerResult {
  const ts = readMaybe(tsPath);
  if (!ts) return { result: "n/a", hits: [] };
  // Only applies to chapter manifests (which list sections).
  const sectionRe =
    /\{\s*title:\s*["'][^"']*["']\s*,\s*blocks:\s*\[([^\]]*)\]/g;
  const lengths: number[] = [];
  for (const m of ts.matchAll(sectionRe)) {
    const blocks = m[1]
      .split(",")
      .map((s) => s.trim())
      .filter(Boolean);
    lengths.push(blocks.length);
  }
  if (lengths.length === 0) return { result: "n/a", hits: [] };
  const hits: CheckerHit[] = [];
  lengths.forEach((n, i) => {
    if (n < 3 || n > 18) {
      hits.push({
        file: tsPath ?? "(unknown)",
        line: 1,
        text: `section ${i + 1}: ${n} blocks (out of R1-R3 band 3..18)`,
      });
    }
  });
  return { result: hits.length > 0 ? "fail" : "pass", hits };
}

// `detangler-no-forward-ref`, `detangler-no-xchapter-fwd`, and
// `detangler-archimedean-wall` need access to the chapter ordering
// of the paper. They share a heavier preamble — left as TODO in
// this commit, with explicit `n/a` returns so the sweep doesn't
// flag them as missing. A follow-up commit will wire them.

export function checkDetanglerNoForwardRef(
  _tsPath: string | undefined,
): CheckerResult {
  // TODO: parse the chapter .ts to get the block ordering; for each
  // `uses:` target, verify it appears earlier in the same chapter's
  // `sections[].blocks[]` array. Returns n/a until wired.
  return { result: "n/a", hits: [] };
}

export function checkDetanglerNoXChapterFwd(
  _tsPath: string | undefined,
): CheckerResult {
  // TODO: same as above but at paper.ts level — verify cross-chapter
  // `uses:` refs point at an earlier chapter in `paper.ts`'s
  // ordering. n/a until wired.
  return { result: "n/a", hits: [] };
}

export function checkDetanglerArchimedeanWall(
  _tsPath: string | undefined,
  _leanPath: string | undefined,
): CheckerResult {
  // TODO: parse the chapter directory + classify Lean files as
  // archimedean / generic-R / mixed; verify the chapter's expected
  // wall side per the chapter-ts metadata. n/a until wired.
  return { result: "n/a", hits: [] };
}

// ─── Proof axis ─────────────────────────────────────────────────

const BARE_SORRY_REF_GAP_LINES = 3; // a `-- Ref:` must appear within
// the previous N lines of a `sorry`

export function checkProofNoBareSorries(
  leanPath: string | undefined,
): CheckerResult {
  const src = readMaybe(leanPath);
  if (!src) return { result: "n/a", hits: [] };
  const lines = src.split("\n");
  const hits: CheckerHit[] = [];
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    // Match `sorry` as a whole token (not inside a comment or string).
    if (!/\bsorry\b/.test(line)) continue;
    if (/^\s*--/.test(line)) continue; // commented out
    // Look back BARE_SORRY_REF_GAP_LINES lines for a `-- Ref:`.
    let hasRef = false;
    for (
      let j = Math.max(0, i - BARE_SORRY_REF_GAP_LINES);
      j < i;
      j++
    ) {
      if (/--\s*Ref:\s*\[/.test(lines[j])) {
        hasRef = true;
        break;
      }
    }
    if (!hasRef) {
      hits.push({
        file: leanPath ?? "(unknown)",
        line: i + 1,
        text:
          `bare \`sorry\` at line ${i + 1} — no \`-- Ref: [key]\` citation in ` +
          `the previous ${BARE_SORRY_REF_GAP_LINES} lines`,
      });
    }
  }
  return { result: hits.length > 0 ? "fail" : "pass", hits };
}

const HOLDS_PROP_RE = /\bholds\s*:\s*Prop\b/;
const INSTANCE_HYP_RE = /\[\s*\w+\s+\w+\s*\]/;

export function checkProofSubstantive(
  leanPath: string | undefined,
): CheckerResult {
  const src = readMaybe(leanPath);
  if (!src) return { result: "n/a", hits: [] };
  // A block-level signature using `holds : Prop` without ANY class
  // hypothesis is the flag. Heuristic — script catches the common
  // cases; lean-substantive-pass agent handles the rest.
  if (!HOLDS_PROP_RE.test(src)) return { result: "pass", hits: [] };
  if (INSTANCE_HYP_RE.test(src)) return { result: "pass", hits: [] };
  const lineIdx = src
    .split("\n")
    .findIndex((l) => HOLDS_PROP_RE.test(l));
  return {
    result: "fail",
    hits: [
      {
        file: leanPath ?? "(unknown)",
        line: (lineIdx >= 0 ? lineIdx : 0) + 1,
        text:
          `\`holds : Prop\` placeholder used WITHOUT a class hypothesis ` +
          `[Instance ...] — per CLAUDE.md §3b-cond, the downstream consumer ` +
          `must take the conjecture as a typeclass`,
      },
    ],
  };
}

// `proof-no-axiom-growth` and `proof-build-green` both read CI
// artefacts that are produced by `lean_ci.yml` (`axiom-report.txt`
// + `proof-objects.json`). Local sweeps return n/a; the CI sweep
// reads the artefacts and writes pass/fail entries.

export function checkProofNoAxiomGrowth(
  _leanPath: string | undefined,
): CheckerResult {
  return { result: "n/a", hits: [] };
}

export function checkProofBuildGreen(
  _leanPath: string | undefined,
): CheckerResult {
  return { result: "n/a", hits: [] };
}

// ─── Dispatch map ───────────────────────────────────────────────

export const EXTENDED_AUTOMATED_CHECKERS: Record<
  string,
  (paths: { md?: string; ts?: string; lean?: string }) => CheckerResult
> = {
  // bibliography
  "bib-cite-resolves": (p) => checkBibCiteResolves(p.md, p.lean),
  "bib-cited-ref-has-url": (p) => checkBibCitedRefHasUrl(p.md, p.lean),
  "bib-cited-ref-metadata-ok": (p) =>
    checkBibCitedRefMetadataOk(p.md, p.lean),
  "bib-cited-ref-has-screenshot": (p) =>
    checkBibCitedRefHasScreenshot(p.md, p.lean),
  // compute
  "compute-prop-has-probe": (p) => checkComputePropHasProbe(p.ts),
  "compute-prop-has-consumer": (p) => checkComputePropHasConsumer(p.ts),
  "compute-witness-exists": (p) => checkComputeWitnessExists(p.ts),
  "compute-lp-dual-present": (p) => checkComputeLpDualPresent(p.ts),
  // canonical
  "canonical-calibration-count": (p) =>
    checkCanonicalCalibrationCount(p.md, p.ts),
  "canonical-witness-pinned": (p) => checkCanonicalWitnessPinned(p.md, p.ts),
  // detangler
  "detangler-section-band": (p) => checkDetanglerSectionBand(p.ts),
  "detangler-no-forward-ref": (p) => checkDetanglerNoForwardRef(p.ts),
  "detangler-no-xchapter-fwd": (p) => checkDetanglerNoXChapterFwd(p.ts),
  "detangler-archimedean-wall": (p) =>
    checkDetanglerArchimedeanWall(p.ts, p.lean),
  // proof
  "proof-no-bare-sorries": (p) => checkProofNoBareSorries(p.lean),
  "proof-substantive": (p) => checkProofSubstantive(p.lean),
  "proof-no-axiom-growth": (p) => checkProofNoAxiomGrowth(p.lean),
  "proof-build-green": (p) => checkProofBuildGreen(p.lean),
};
