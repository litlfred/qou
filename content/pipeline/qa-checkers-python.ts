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
 * - Sentinel values: `float("inf")`, `float("nan")`, `float("-inf")`.
 * - Comments / docstrings: anywhere after `#` or inside `""" ... """`
 *   / `''' ... '''` — narrative, not code.
 *
 * Implementation: strip these regions before scanning for bare
 * float literals.
 */
const PY_STRING_RE = /"""[\s\S]*?"""|'''[\s\S]*?'''|"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'/g;
const PY_COMMENT_RE = /#[^\n]*/g;

// A "bare float literal" is a numeric token that contains a `.`
// or exponent and is NOT immediately followed by a string (already
// stripped) or `j` (complex). We also require word-boundary on
// the left to avoid matching attribute-style identifiers like
// `obj.5x` (which Python wouldn't parse anyway).
const BARE_FLOAT_LITERAL_RE =
  /(?<![A-Za-z_0-9.])(?:\d+\.\d*|\.\d+|\d+(?:\.\d*)?[eE][+-]?\d+)(?![jJ])/g;

// A `float(...)` cast call. We allow `float("inf")` etc. via a
// secondary check on the captured arg.
const FLOAT_CALL_RE = /\bfloat\s*\(\s*([^)]*?)\s*\)/g;
const FLOAT_CALL_SENTINEL_RE =
  /^\s*['"](?:inf|-inf|nan|infinity)['"]\s*$/i;

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
  const lines = masked.split("\n");
  // `maskStringsAndComments` blanks string/comment regions in place
  // (same length, same line breaks), so column offsets in the masked
  // text align with the original text and we can recover sentinel
  // arguments from `origLines` using indices computed against
  // `maskedLine`.
  const origLines = src.split("\n");
  const hits: CheckerHit[] = [];

  for (let i = 0; i < lines.length; i++) {
    const maskedLine = lines[i];
    const origLine = origLines[i];
    // Skip lines that are entirely whitespace once strings + comments
    // are stripped — purely commented or string-literal lines.
    if (!maskedLine.trim()) continue;

    // Scan for `float(...)` casts first and blank the matched region
    // in a working copy of the line so the bare-literal scan below
    // does NOT double-flag literals that appear inside the cast
    // (`float(1.0)` would otherwise be reported twice).
    let lineForLiterals = maskedLine;
    for (const m of maskedLine.matchAll(FLOAT_CALL_RE)) {
      // Test the sentinel against the ORIGINAL source slice (the
      // masked line has `float("inf")` blanked to `float(    )`,
      // which never matches `FLOAT_CALL_SENTINEL_RE` — Gemini
      // r3276657081).
      const startOfArg = m.index! + m[0].indexOf("(") + 1;
      const endOfArg = m.index! + m[0].lastIndexOf(")");
      const rawArg = origLine.slice(startOfArg, endOfArg);
      const isSentinel = FLOAT_CALL_SENTINEL_RE.test(rawArg);

      if (!isSentinel) {
        const trimmed = rawArg.trim();
        hits.push({
          file: scriptPath,
          line: i + 1,
          text:
            `bare \`float(${trimmed.slice(0, 40)}${
              trimmed.length > 40 ? "…" : ""
            })\` cast — use \`mpmath.mpf(...)\` / \`Decimal(...)\` ` +
            `for substrate-precision values, or string-quote the ` +
            `literal if intentional`,
        });
      }
      // Blank the cast region in `lineForLiterals` regardless of
      // sentinel status — the inner literal (if any) is either
      // already reported via the cast hit above or is a sentinel arg
      // that should never be reported.
      lineForLiterals =
        lineForLiterals.substring(0, m.index!) +
        " ".repeat(m[0].length) +
        lineForLiterals.substring(m.index! + m[0].length);
    }

    // Bare float literals in the region not consumed by a `float()`
    // cast.
    for (const m of lineForLiterals.matchAll(BARE_FLOAT_LITERAL_RE)) {
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
