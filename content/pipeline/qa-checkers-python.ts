/**
 * Script-quality checkers for Python source files.
 *
 * Currently implements the `does_not_default_to_float` criterion;
 * other criteria from the script-quality axis (commented,
 * variables_typed, has_references_to_paper, connected_to_ci_pipeline,
 * deprecated, uses_library_framework_appropriately, plus the
 * type-discipline pair `respects_archimedean_wall`) will land here
 * as separate checkers in follow-up PRs.
 *
 * Checkers in this file are **regex-based heuristics**, not full
 * AST scans. The trade-off is accept some false positives in
 * exchange for not adding a Python runtime dependency to the QA
 * sweep. When a heuristic produces too many false positives in
 * practice, the right escalation path is to port the checker to a
 * subprocess that runs Python's `ast` module — separate PR.
 *
 * @module content/pipeline/qa-checkers-python
 */

import { readFileSync, existsSync } from "fs";
import type { CheckerResult, CheckerHit } from "./qa-checkers-voice";

// ─── does_not_default_to_float ─────────────────────────────────

/**
 * Allow-list of patterns where a float literal is acceptable:
 *
 * - String args to high-precision constructors:
 *   `mpf("1.5")`, `Decimal("0.5")`, `mpmath.mpf("3.14")` —
 *   the float-looking content is a string, not a Python float.
 * - Sentinel values: `float("inf")`, `float("-inf")`, `float("nan")`,
 *   `float("infinity")` (Python's float() accepts the long form too;
 *   matching is case-insensitive).
 * - Comments / docstrings: anywhere after `#` or inside `""" ... """`
 *   / `''' ... '''` — narrative, not code.
 *
 * Implementation: strip these regions before scanning for bare
 * float literals.
 */
const PY_STRING_RE = /"""[\s\S]*?"""|'''[\s\S]*?'''|"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'/g;
const PY_COMMENT_RE = /#[^\n]*/g;

// A "bare float literal" is a numeric token that contains a `.`
// or exponent and is NOT immediately followed by `j`/`J` (complex)
// or another identifier char. PEP 515 numeric underscores (`1_000.5`,
// `1.5_5e1_0`) are accepted between digits.
//
// Alternatives are ordered specific→general: the exponent form
// matches before the dot-only form so `1.5e10` matches as the full
// e-literal, not just `1.5` (the original regex stopped at the
// dot and missed the exponent suffix).
const BARE_FLOAT_LITERAL_RE =
  /(?<![A-Za-z_0-9.])(?:\d[\d_]*(?:\.[\d_]*)?[eE][+-]?\d[\d_]*|\d[\d_]*\.[\d_]*|\.\d[\d_]*)(?![jJ])/g;

// A `float(...)` cast call. The inner `(?:[^()]|\([^()]*\))*`
// alternation allows one level of nested parens — `float(int(x))`
// matches as a single call. Two or more levels of nesting
// (`float(int(int(x)))`) remain a known heuristic limitation; the
// inner `float(...)` calls are still caught via the recursive scan
// because each is a separate `\bfloat` anchor. `[^()]` matches
// newlines by default in JS regex, so multiline casts like
// `float(\n  "inf"\n)` are handled by the same pattern.
const FLOAT_CALL_RE =
  /\bfloat\s*\((?:[^()]|\([^()]*\))*\)/g;
const FLOAT_CALL_SENTINEL_RE =
  /^\s*['"](?:inf|-inf|nan|infinity|-infinity)['"]\s*$/i;

const blankNonNewline = (m: string) => m.replace(/[^\n]/g, " ");

/**
 * Mask Python string literals and comments with same-length blanks,
 * preserving line numbers so hit locations remain accurate.
 */
function maskStringsAndComments(src: string): string {
  return src
    .replace(PY_STRING_RE, blankNonNewline)
    .replace(PY_COMMENT_RE, blankNonNewline);
}

/**
 * Flag bare float literals (`1.0`, `0.5`, `3.14e-10`, …) and
 * `float(...)` casts in Python source. Strings, comments, and
 * `float("inf"|"nan"|…)` sentinels are exempt.
 *
 * Heuristic — does not parse Python. Produces some false positives
 * (e.g. floats embedded in conditional blocks that the author knows
 * are safe). Authors override with a `human` reviewer entry in the
 * script's sidecar.
 */
export function checkDoesNotDefaultToFloat(
  scriptPath: string,
): CheckerResult {
  if (!existsSync(scriptPath)) return { result: "n/a", hits: [] };
  const src = readFileSync(scriptPath, "utf-8");
  const masked = maskStringsAndComments(src);
  // `maskStringsAndComments` blanks string/comment regions in place
  // (same length, same line breaks), so offsets in the masked text
  // align with the original text — we can recover sentinel
  // arguments from `src` using indices computed against `masked`.
  const hits: CheckerHit[] = [];

  // Precompute newline offsets so we can map a char offset back to a
  // 1-indexed line number in O(log n) per lookup. Whole-source scan
  // (rather than per-line) lets us catch multiline `float(\n ...)`
  // casts that Black-formatted code may produce.
  const newlineOffsets: number[] = [];
  for (let i = 0; i < masked.length; i++) {
    if (masked[i] === "\n") newlineOffsets.push(i);
  }
  const lineForOffset = (offset: number): number => {
    let lo = 0;
    let hi = newlineOffsets.length;
    while (lo < hi) {
      const mid = (lo + hi) >>> 1;
      if (newlineOffsets[mid] < offset) lo = mid + 1;
      else hi = mid;
    }
    return lo + 1;
  };

  // Phase 1 — whole-source scan for `float(...)` casts. For each
  // match, recover the original arg from `src` (since the masked
  // copy has string contents blanked), test the sentinel allow-list,
  // and blank the matched region in a working copy so the literal
  // scan below does not double-flag arguments like `float(1.0)`.
  let workingSource = masked;
  for (const m of masked.matchAll(FLOAT_CALL_RE)) {
    const startOfArg = m.index! + m[0].indexOf("(") + 1;
    const endOfArg = m.index! + m[0].lastIndexOf(")");
    const rawArg = src.slice(startOfArg, endOfArg);
    const isSentinel = FLOAT_CALL_SENTINEL_RE.test(rawArg.trim());

    if (!isSentinel) {
      const display = rawArg.trim().replace(/\s+/g, " ");
      hits.push({
        file: scriptPath,
        line: lineForOffset(m.index!),
        text:
          `bare \`float(${display.slice(0, 40)}${
            display.length > 40 ? "…" : ""
          })\` cast — use \`mpmath.mpf(...)\` / \`Decimal(...)\` ` +
          `for substrate-precision values, or string-quote the ` +
          `literal if intentional`,
      });
    }
    // Blank the cast region (newlines preserved) so the per-line
    // literal scan below does not see the cast's interior.
    const blanked = m[0].replace(/[^\n]/g, " ");
    workingSource =
      workingSource.substring(0, m.index!) +
      blanked +
      workingSource.substring(m.index! + m[0].length);
  }

  // Phase 2 — bare float literals in regions not consumed by a
  // `float(...)` cast. Per-line scan is fine here; literals do not
  // span lines.
  const workingLines = workingSource.split("\n");
  for (let i = 0; i < workingLines.length; i++) {
    if (!workingLines[i].trim()) continue;
    for (const m of workingLines[i].matchAll(BARE_FLOAT_LITERAL_RE)) {
      hits.push({
        file: scriptPath,
        line: i + 1,
        text:
          `bare float literal \`${m[0]}\` — wrap in ` +
          `\`mpmath.mpf("${m[0]}")\` / \`Decimal("${m[0]}")\` to ` +
          `preserve substrate precision, or move to a string constant ` +
          `if it's an input parameter`,
      });
    }
  }

  return {
    result: hits.length > 0 ? "fail" : "pass",
    hits,
  };
}
