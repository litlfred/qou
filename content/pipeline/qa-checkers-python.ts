/**
 * Script-quality checkers for Python source files.
 *
 * Implements the 8 criteria in the script-quality axis:
 *   - `does_not_default_to_float`     — bare floats / casts
 *   - `respects_archimedean_wall`     — `math.sqrt`/`numpy.float64`/…
 *   - `code_is_commented`             — module docstring or ≥10% comments
 *   - `variables_typed`               — function parameter annotations
 *   - `has_references_to_paper`       — `# Ref: [key]` markers
 *   - `connected_to_ci_pipeline`      — referenced from a workflow
 *   - `deprecated`                    — path / marker / docstring
 *   - `uses_library_framework_appropriately` — `WitnessBuilder` import
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

import { readFileSync, existsSync, readdirSync, statSync } from "fs";
import { join, basename, dirname, relative } from "path";
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
// The lookbehind class blocks identifier chars, digits, dots, AND
// `:` — the `:` exclusion prevents false positives in f-string
// format specs like `{x:.2f}` / `{x:0.4f}` / `{x:10.5f}`, where
// the digit+dot sequence after `:` is a width/precision specifier,
// not a code literal.
//
// Alternatives are ordered specific→general: the exponent form
// matches before the dot-only form so `1.5e10` matches as the full
// e-literal, not just `1.5` (the original regex stopped at the
// dot and missed the exponent suffix).
const BARE_FLOAT_LITERAL_RE =
  /(?<![A-Za-z_0-9.:])(?:\d[\d_]*(?:\.[\d_]*)?[eE][+-]?\d[\d_]*|\d[\d_]*\.[\d_]*|\.\d[\d_]*)(?![jJ])/g;

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
// Sentinel allow-list: case-insensitive `inf`/`-inf`/`nan`/`infinity`/
// `-infinity`, optional trailing comma (`float("inf",)` is valid
// Python and is the form Black produces for multiline single-arg
// calls).
const FLOAT_CALL_SENTINEL_RE =
  /^\s*['"](?:inf|-inf|nan|infinity|-infinity)['"]\s*,?\s*$/i;

// Known heuristic limitations (documented; not bugs to file):
//   - f-string expression regions are currently masked uniformly
//     with their text portions, so bare floats inside `f'{1.0}'`
//     are false negatives. Naïve unmasking introduces false
//     positives on format specs (`{x:>10.4f}`) and literal text
//     (`f'value 1.0'`); proper f-string expression scanning needs
//     a tokeniser and lands in a follow-up PR.
//   - 2+ levels of nested parens inside `float(...)` (e.g.
//     `float(int(int(x)))`) — the outer call is missed but each
//     inner `float(...)` is caught via its own `\bfloat` anchor.

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
          })\` cast — use \`mpmath.mpf("...")\` / \`Decimal("...")\` ` +
          `to preserve substrate precision`,
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

// ─── respects_archimedean_wall ─────────────────────────────────

/**
 * Archimedean-realization functions that should NOT appear in
 * categorical / algebraic / substrate-precision code paths.
 * Per CLAUDE.md §7c, these belong in `descartes-universe/` or
 * `observations/` archimedean-specialised modules, not in the
 * generic-R compute layer.
 *
 * The mpmath equivalents (`mp.sqrt`, `mp.log`, `mp.exp`, …) are
 * the correct substrate-precision substitutes.
 */
const ARCHIMEDEAN_FUNCTION_RE =
  /\b(?:math|numpy|np)\.(?:sqrt|log|log2|log10|log1p|exp|expm1|cos|sin|tan|acos|asin|atan|atan2|sinh|cosh|tanh|asinh|acosh|atanh|pow|hypot|erf|erfc|gamma|lgamma|floor|ceil|trunc)\b/g;
const NUMPY_FLOAT64_RE = /\bnumpy\.float64\b|\bnp\.float64\b/g;

/**
 * Flag archimedean-floating-point operations (`math.sqrt`,
 * `numpy.cos`, `np.float64`, …) in Python source. These should
 * not appear in substrate-precision code paths — the mpmath
 * equivalents preserve the 50-digit working precision the rest
 * of the framework relies on.
 *
 * Strings and comments are masked before scanning so `# uses
 * math.sqrt for archimedean realization` style narrative does
 * not produce false positives.
 */
export function checkRespectsArchimedeanWall(
  scriptPath: string,
): CheckerResult {
  if (!existsSync(scriptPath)) return { result: "n/a", hits: [] };
  const src = readFileSync(scriptPath, "utf-8");
  const masked = maskStringsAndComments(src);
  const lines = masked.split("\n");
  const hits: CheckerHit[] = [];

  for (let i = 0; i < lines.length; i++) {
    if (!lines[i].trim()) continue;
    for (const m of lines[i].matchAll(ARCHIMEDEAN_FUNCTION_RE)) {
      hits.push({
        file: scriptPath,
        line: i + 1,
        text:
          `archimedean call \`${m[0]}\` — use the mpmath equivalent ` +
          `(\`mp.${m[0].split(".")[1]}\`) for substrate-precision ` +
          `values, or move this code to an archimedean-realization ` +
          `module under \`descartes-universe/\` / \`observations/\``,
      });
    }
    for (const m of lines[i].matchAll(NUMPY_FLOAT64_RE)) {
      hits.push({
        file: scriptPath,
        line: i + 1,
        text:
          `numpy.float64 type — use \`mpmath.mpf\` for ` +
          `substrate-precision values; numpy.float64 truncates to ` +
          `IEEE-754 double precision (~15 decimal digits)`,
      });
    }
  }

  return {
    result: hits.length > 0 ? "fail" : "pass",
    hits,
  };
}

// ─── code_is_commented ─────────────────────────────────────────

const MODULE_DOCSTRING_RE =
  /^(?:\s*\n)*\s*(?:from\s+__future__\s+import[^\n]*\n\s*)*("""[\s\S]*?"""|'''[\s\S]*?''')/;

/**
 * Pass if either:
 *   - A module docstring exists at the top of the file
 *     (allowing `from __future__ import …` to precede it), OR
 *   - Comment-line density is ≥ 10% of non-blank lines.
 *
 * Fail otherwise (suggests adding a `"""docstring"""` at the
 * module top). Authors override with a `human` reviewer entry.
 */
export function checkCodeIsCommented(scriptPath: string): CheckerResult {
  if (!existsSync(scriptPath)) return { result: "n/a", hits: [] };
  const src = readFileSync(scriptPath, "utf-8");
  if (MODULE_DOCSTRING_RE.test(src)) return { result: "pass", hits: [] };
  const lines = src.split("\n");
  let nonBlank = 0;
  let comments = 0;
  for (const line of lines) {
    const t = line.trim();
    if (!t) continue;
    nonBlank++;
    if (t.startsWith("#")) comments++;
  }
  if (nonBlank === 0) return { result: "n/a", hits: [] };
  const ratio = comments / nonBlank;
  if (ratio >= 0.1) return { result: "pass", hits: [] };
  return {
    result: "fail",
    hits: [
      {
        file: scriptPath,
        line: 1,
        text:
          `script lacks both a module docstring and ≥10% comment ` +
          `density (got ${comments}/${nonBlank} = ` +
          `${(ratio * 100).toFixed(1)}%) — add a top-of-file ` +
          `\`"""…"""\` docstring describing purpose and inputs / ` +
          `outputs, or increase inline commentary`,
      },
    ],
  };
}

// ─── variables_typed ───────────────────────────────────────────

const FUNCTION_DEF_RE = /^\s*(?:async\s+)?def\s+(\w+)\s*\(([^)]*)\)/gm;

/**
 * Pass if every function-definition parameter list has type
 * annotations (`def foo(x: int, y: str)`). Excludes `self`,
 * `cls`, `*args`, `**kwargs`, and `_` (unused). Defaults without
 * type annotations are flagged.
 *
 * Heuristic — does not parse Python. Multi-line `def` signatures
 * with line breaks inside the parameter list are skipped (the
 * regex requires the `(…)` to fit on one logical line); those
 * are uncommon enough that the false-negative rate is acceptable.
 */
export function checkVariablesTyped(scriptPath: string): CheckerResult {
  if (!existsSync(scriptPath)) return { result: "n/a", hits: [] };
  const src = readFileSync(scriptPath, "utf-8");
  const masked = maskStringsAndComments(src);
  const hits: CheckerHit[] = [];
  const newlines: number[] = [];
  for (let i = 0; i < masked.length; i++)
    if (masked[i] === "\n") newlines.push(i);
  const lineFor = (off: number): number => {
    let lo = 0, hi = newlines.length;
    while (lo < hi) {
      const mid = (lo + hi) >>> 1;
      if (newlines[mid] < off) lo = mid + 1; else hi = mid;
    }
    return lo + 1;
  };

  for (const m of masked.matchAll(FUNCTION_DEF_RE)) {
    const fnName = m[1];
    const argsStr = (m[2] ?? "").trim();
    if (!argsStr) continue; // no-arg function is trivially typed
    const args = argsStr.split(",").map((a) => a.trim()).filter(Boolean);
    const untyped: string[] = [];
    for (const a of args) {
      // Strip default value if present (`x=5` → `x`).
      const beforeEq = a.split("=")[0].trim();
      // Exempt parameter forms.
      if (beforeEq === "self" || beforeEq === "cls" ||
          beforeEq === "_" ||
          beforeEq.startsWith("*") || beforeEq.startsWith("**") ||
          beforeEq === "/") {
        continue;
      }
      if (!beforeEq.includes(":")) untyped.push(beforeEq);
    }
    if (untyped.length > 0) {
      hits.push({
        file: scriptPath,
        line: lineFor(m.index!),
        text:
          `\`def ${fnName}(…)\` has ${untyped.length} parameter` +
          `${untyped.length === 1 ? "" : "s"} without type ` +
          `annotation: ${untyped.slice(0, 5).join(", ")}` +
          `${untyped.length > 5 ? ", …" : ""} — add \`: type\` ` +
          `(or \`: Any\` if the type genuinely is untyped)`,
      });
    }
  }

  return {
    result: hits.length > 0 ? "fail" : "pass",
    hits,
  };
}

// ─── has_references_to_paper ───────────────────────────────────

const PAPER_REF_RE = /^\s*#\s*Ref:\s*\[[^\]]+\]/m;

/**
 * Pass if the script contains at least one `# Ref: [key] …`
 * comment line citing a bibliography key. Mirrors the Lean
 * convention from CLAUDE.md §1 ("Every `sorry` requires a
 * bibliographic citation").
 *
 * Fails for scripts that derive content from the paper but cite
 * nothing — the citation should let a reviewer trace the script
 * back to the proposition / theorem it computes. Authors who
 * deliberately ship an uncited utility (e.g. pure infrastructure)
 * override with a `human` reviewer `result: "n/a"` entry.
 */
export function checkHasReferencesToPaper(
  scriptPath: string,
): CheckerResult {
  if (!existsSync(scriptPath)) return { result: "n/a", hits: [] };
  const src = readFileSync(scriptPath, "utf-8");
  if (PAPER_REF_RE.test(src)) return { result: "pass", hits: [] };
  return {
    result: "fail",
    hits: [
      {
        file: scriptPath,
        line: 1,
        text:
          `script contains no \`# Ref: [key] …\` citation. Add a ` +
          `bibliographic citation pointing to the proposition / ` +
          `theorem / paper section this script computes (matching ` +
          `the entries in \`content/schema/references.ts\`), or ` +
          `override with a \`human\` reviewer \`result: "n/a"\` entry ` +
          `if the script is pure infrastructure`,
      },
    ],
  };
}

// ─── connected_to_ci_pipeline ──────────────────────────────────

let _workflowsCache: string | null = null;
let _workflowsCacheRepoRoot = "";

/**
 * Lazily-loaded concatenation of every `.github/workflows/*.yml`
 * file's content. The checker scans this string for the script's
 * basename — if found, the script is connected to the CI pipeline.
 */
function loadWorkflows(repoRoot: string): string {
  if (_workflowsCache !== null && _workflowsCacheRepoRoot === repoRoot) {
    return _workflowsCache;
  }
  const dir = join(repoRoot, ".github", "workflows");
  if (!existsSync(dir)) {
    _workflowsCache = "";
    _workflowsCacheRepoRoot = repoRoot;
    return "";
  }
  const parts: string[] = [];
  for (const entry of readdirSync(dir)) {
    if (!entry.endsWith(".yml") && !entry.endsWith(".yaml")) continue;
    const p = join(dir, entry);
    if (!statSync(p).isFile()) continue;
    parts.push(readFileSync(p, "utf-8"));
  }
  _workflowsCache = parts.join("\n");
  _workflowsCacheRepoRoot = repoRoot;
  return _workflowsCache;
}

/**
 * Pass if the script's basename appears in at least one
 * `.github/workflows/*.yml` file. Used to flag scripts that are
 * never exercised in CI (likely candidates for `_deprecated/`).
 *
 * `__init__.py`, `conftest.py`, library / helper modules imported
 * from other scripts, and scripts under `_deprecated/` get an
 * `n/a` so they don't pollute the failure count.
 */
export function checkConnectedToCiPipeline(
  scriptPath: string,
  repoRoot: string,
): CheckerResult {
  if (!existsSync(scriptPath)) return { result: "n/a", hits: [] };
  const base = basename(scriptPath);
  if (
    base === "__init__.py" ||
    base === "conftest.py" ||
    scriptPath.includes("/_deprecated/")
  ) {
    return { result: "n/a", hits: [] };
  }
  const workflows = loadWorkflows(repoRoot);
  if (workflows.includes(base)) return { result: "pass", hits: [] };
  // Also check whether the script is imported as a module by any
  // other script (library / helper pattern). If so, it's "connected"
  // transitively through whichever script CI runs.
  const modName = base.replace(/\.py$/, "");
  // Crude probe: does the modName appear in any other .py under
  // computations as `from <modName> import` or `import <modName>`?
  // We don't recurse — a single grep against the parent dir suffices
  // for the common case.
  const parent = dirname(scriptPath);
  if (existsSync(parent)) {
    const importRe = new RegExp(
      `(?:^|\\s)(?:from\\s+${modName}\\s+import|import\\s+${modName}(?:\\s|$))`,
      "m",
    );
    for (const entry of readdirSync(parent)) {
      if (!entry.endsWith(".py")) continue;
      if (entry === base) continue;
      const p = join(parent, entry);
      try {
        const s = readFileSync(p, "utf-8");
        if (importRe.test(s)) return { result: "pass", hits: [] };
      } catch {
        // Skip unreadable
      }
    }
  }
  return {
    result: "fail",
    hits: [
      {
        file: scriptPath,
        line: 1,
        text:
          `script \`${base}\` is not referenced from any ` +
          `\`.github/workflows/*.yml\` and is not imported by any ` +
          `sibling script — likely never exercised in CI. Either ` +
          `add a workflow invocation, mark as a library by adding ` +
          `\`from <this-module> import\` somewhere, or move to ` +
          `\`_deprecated/\``,
      },
    ],
  };
}

// ─── deprecated ────────────────────────────────────────────────

const DEPRECATED_MARKER_RE = /^\s*#\s*DEPRECATED\b/m;
const DEPRECATED_DOCSTRING_RE = /\bDEPRECATED\b/;

/**
 * Flag the script as deprecated when ANY of:
 *   - Path contains `/_deprecated/`
 *   - File contains a `# DEPRECATED` comment line
 *   - Module docstring (first triple-quoted block) contains the
 *     word "DEPRECATED" verbatim (case-sensitive — narrative use
 *     of "deprecated" in prose doesn't trigger)
 *
 * Severity is `minor` — deprecation is a status flag, not a
 * correctness bug. A `human` reviewer entry can move a deprecated
 * script to `pass` if it's intentionally retained for reference.
 */
export function checkDeprecated(scriptPath: string): CheckerResult {
  if (!existsSync(scriptPath)) return { result: "n/a", hits: [] };
  if (scriptPath.includes("/_deprecated/")) {
    return {
      result: "fail",
      hits: [
        {
          file: scriptPath,
          line: 1,
          text:
            `script lives under \`_deprecated/\` — consumers must ` +
            `not depend on its output. Move to the canonical path ` +
            `if still active, or delete if truly retired`,
        },
      ],
    };
  }
  const src = readFileSync(scriptPath, "utf-8");
  if (DEPRECATED_MARKER_RE.test(src)) {
    return {
      result: "fail",
      hits: [
        {
          file: scriptPath,
          line: 1,
          text:
            `\`# DEPRECATED\` marker present — move script to ` +
            `\`_deprecated/\` to align path and content, or remove ` +
            `the marker if no longer deprecated`,
        },
      ],
    };
  }
  // Check just the first triple-quoted block (module docstring) for
  // a verbatim "DEPRECATED" — avoids matching prose use further
  // down.
  const docstringMatch = src.match(MODULE_DOCSTRING_RE);
  if (
    docstringMatch &&
    DEPRECATED_DOCSTRING_RE.test(docstringMatch[1])
  ) {
    return {
      result: "fail",
      hits: [
        {
          file: scriptPath,
          line: 1,
          text:
            `module docstring contains "DEPRECATED" — move script ` +
            `to \`_deprecated/\` to align path and content, or ` +
            `rephrase the docstring if no longer deprecated`,
        },
      ],
    };
  }
  return { result: "pass", hits: [] };
}

// ─── uses_library_framework_appropriately ─────────────────────

const WITNESS_WRITE_RE = /["']\S*\.witness\.json["']/;
const WITNESS_BUILDER_IMPORT_RE =
  /from\s+witness_base\s+import[^\n]*\bWitnessBuilder\b|import\s+witness_base\b/;
const HARDCODED_PI_RE = /\bpi\s*=\s*3\.14\d*/;
const HARDCODED_E_RE = /\be\s*=\s*2\.71\d*/;

/**
 * Pass if the script consumes the standard library framework
 * appropriately:
 *
 *   - If the script writes a `.witness.json`, it must import
 *     `WitnessBuilder` from `witness_base` (provenance + script-
 *     hash metadata stamping).
 *   - No hardcoded mathematical constants (`pi = 3.14…`,
 *     `e = 2.71…`) — use `mpmath.mp.pi` / `mpmath.mp.e`.
 *
 * Strings and comments are masked before scanning so that
 * documentation strings like `"Generates foo.witness.json"` do
 * not produce false positives.
 */
export function checkUsesLibraryFrameworkAppropriately(
  scriptPath: string,
): CheckerResult {
  if (!existsSync(scriptPath)) return { result: "n/a", hits: [] };
  const src = readFileSync(scriptPath, "utf-8");
  const masked = maskStringsAndComments(src);
  const hits: CheckerHit[] = [];

  // Witness-write requires WitnessBuilder import. The witness path
  // is a STRING LITERAL in code (not a comment); `maskStringsAndComments`
  // blanks BOTH, so to detect string literals in code-not-comment
  // regions we need a comment-only mask that keeps string contents
  // intact.
  const srcWithoutComments = src.replace(PY_COMMENT_RE, blankNonNewline);
  const writesWitness = WITNESS_WRITE_RE.test(srcWithoutComments);
  const importsWitnessBuilder = WITNESS_BUILDER_IMPORT_RE.test(src);
  if (writesWitness && !importsWitnessBuilder) {
    const m = srcWithoutComments.match(WITNESS_WRITE_RE);
    const line =
      m?.index !== undefined
        ? srcWithoutComments.slice(0, m.index).split("\n").length
        : 1;
    hits.push({
      file: scriptPath,
      line,
      text:
        `script writes \`.witness.json\` (${m?.[0] ?? "?"}) but does ` +
        `not import \`WitnessBuilder\` from \`witness_base\` — add ` +
        `\`from witness_base import WitnessBuilder\` and stamp the ` +
        `payload via \`WitnessBuilder.stamp_staleness_metadata(...)\` ` +
        `for provenance / staleness tracking`,
    });
  }

  // Hardcoded math constants — scan the masked copy so comments
  // don't trigger.
  const lines = masked.split("\n");
  for (let i = 0; i < lines.length; i++) {
    if (HARDCODED_PI_RE.test(lines[i])) {
      hits.push({
        file: scriptPath,
        line: i + 1,
        text:
          `hardcoded \`pi = 3.14…\` constant — use \`mpmath.mp.pi\` ` +
          `(50-digit substrate precision) or accept the precision ` +
          `loss explicitly`,
      });
    }
    if (HARDCODED_E_RE.test(lines[i])) {
      hits.push({
        file: scriptPath,
        line: i + 1,
        text:
          `hardcoded \`e = 2.71…\` constant — use \`mpmath.mp.e\` ` +
          `(50-digit substrate precision)`,
      });
    }
  }

  return {
    result: hits.length > 0 ? "fail" : "pass",
    hits,
  };
}
