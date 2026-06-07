#!/usr/bin/env bun
/**
 * LaTeX preflight linter — catches the recurring pdflatex-compile bug
 * classes that the permissive unified-latex AST parser (validateLatexAst
 * in render-latex.ts) does NOT catch, WITHOUT needing a TeX install.
 *
 * Motivation
 * ----------
 * The content pipeline's AST validation parses rendered LaTeX through
 * unified-latex, which builds a syntax tree from *any* well-bracketed
 * input. It never resolves macros, so three whole classes of fatal
 * pdflatex errors pass it silently and only surface in the expensive
 * `paper-pdf` job (which is slow, and a no-op when GitHub Actions is
 * billing-blocked). Historically those bugs landed on `main` and needed
 * a manual `fix(latex): …` commit each time. This linter is the fast,
 * always-run safety net for the cheap content-pipeline job.
 *
 * Compile unit
 * ------------
 * It reads the GENERATED `main.tex` AND every `\input`/`\include` file it
 * pulls in (chapters/*.tex) — i.e. the exact text pdflatex compiles
 * (preamble inlined + manifest-generated macros + every chapter body).
 * Before scanning, comments and verbatim/code contexts (verbatim,
 * lstlisting, minted, \verb, …) are stripped so a backslash shown
 * *literally* in documentation is not mistaken for a macro use.
 *
 * Checks
 * ------
 *   A. duplicate-newcommand  — a control sequence defined more than once
 *      by a definer that ERRORS on redefinition (\newcommand,
 *      \DeclareMathOperator, \DeclarePairedDelimiter, \NewDocumentCommand)
 *      → "! LaTeX Error: Command \X already defined." Definers that
 *      silently overwrite (\renewcommand, \providecommand, \def, \let,
 *      \DeclareRobustCommand, \DeclareDocumentCommand) are deliberately
 *      excluded — redefining via those is legal. Canonical instance: the
 *      manifest re-emitting \newcommand{\pp}{\mathfrak{p}} while the
 *      preamble already defined \pp = p (fix b9e19df6).
 *
 *   B. undefined-macro — a control sequence USED that is neither defined
 *      in the compile unit nor in the seeded standard-command allowlist
 *      (latex-known-macros.json) → "! Undefined control sequence."
 *      (e.g. bare \tr). The allowlist is SEEDED from a clean-compiling
 *      compile unit via `--seed`, so every standard / package command in
 *      actual use is captured: a clean seed yields no false positives,
 *      and a re-introduced undefined macro is then flagged.
 *
 *   C. fragile-accent-script — a math accent (\check, \hat, …) used as the
 *      bare argument of a sub/superscript, e.g. `Q^\check{q}`. The
 *      accent's \mathpalette expansion breaks as a sole script token
 *      ("! Missing { inserted."). Fix: brace it — `Q^{\check{q}}`.
 *
 *   D. missing-input — an unconditional \input/\include target that does
 *      not exist on disk → pdflatex "! LaTeX Error: File `…' not found."
 *      Conditional includes (\IfFileExists / \InputIfFileExists, e.g.
 *      print-mode.tex) are exempt.
 *
 * Usage
 * -----
 *   bun run pipeline/latex-preflight.ts [main.tex]        # gate (exit 1 on error)
 *   bun run pipeline/latex-preflight.ts --json            # machine-readable
 *   bun run pipeline/latex-preflight.ts --seed [main.tex] # (re)write allowlist
 *   bun run pipeline/latex-preflight.ts --warn            # never exit 1
 *
 * Default target: ../main.tex relative to content/.
 *
 * @module content/pipeline/latex-preflight
 */

import { readFileSync, writeFileSync, existsSync } from "fs";
import { dirname, join, resolve, isAbsolute } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const ALLOWLIST_PATH = join(__dirname, "latex-known-macros.json");

// ── Math accents that break as bare sub/superscript arguments ────────
const MATH_ACCENTS = [
  "check", "hat", "tilde", "bar", "vec", "dot", "ddot", "dddot",
  "acute", "grave", "breve", "mathring", "widehat", "widetilde",
  "overline", "underline", "overrightarrow", "overleftarrow",
];

// ── Verbatim-like environments whose bodies are literal (skip them) ──
const VERBATIM_ENVS = new Set([
  "verbatim", "verbatim*", "lstlisting", "minted", "alltt",
  "Verbatim", "BVerbatim", "LVerbatim", "comment",
]);

export interface PreflightIssue {
  check:
    | "duplicate-newcommand"
    | "undefined-macro"
    | "fragile-accent-script"
    | "missing-input";
  macro: string;
  file: string;
  line: number;
  message: string;
}

export interface PreflightResult {
  ok: boolean;
  issues: PreflightIssue[];
  definedCount: number;
  usedCount: number;
  allowlistCount: number;
  filesScanned: number;
}

/** One source line, already cleaned (comment + verbatim stripped). */
interface LineRecord {
  file: string;
  line: number;
  text: string;
}

/** Count the run of backslashes immediately preceding position `i`. */
function precedingBackslashes(s: string, i: number): number {
  let n = 0;
  for (let j = i - 1; j >= 0 && s[j] === "\\"; j--) n++;
  return n;
}

/**
 * Strip a TeX line/percent comment. A `%` starts a comment unless it is
 * escaped — and it is escaped iff preceded by an ODD number of
 * backslashes (`\%` literal; `\\%` is a line-break then a comment).
 */
export function stripComment(line: string): string {
  for (let i = 0; i < line.length; i++) {
    if (line[i] === "%" && precedingBackslashes(line, i) % 2 === 0) {
      return line.slice(0, i);
    }
  }
  return line;
}

/**
 * Remove inline verbatim spans `\verb<d>…<d>` / `\verb*<d>…<d>` /
 * `\lstinline<d>…<d>` from a (comment-stripped) line so their literal
 * backslashes are not read as macro uses. The delimiter `<d>` is the
 * first non-space char after the command.
 */
function stripInlineVerb(line: string): string {
  let out = line;
  const re = /\\(?:verb\*?|lstinline)(\S)/g;
  let m: RegExpExecArray | null;
  // Rebuild left-to-right to avoid index drift.
  let result = "";
  let last = 0;
  re.lastIndex = 0;
  while ((m = re.exec(out)) !== null) {
    const delim = m[1];
    const close = out.indexOf(delim, re.lastIndex);
    result += out.slice(last, m.index);
    if (close === -1) {
      // Unterminated — drop the rest of the line conservatively.
      last = out.length;
      re.lastIndex = out.length;
      break;
    }
    last = close + 1;
    re.lastIndex = close + 1;
  }
  result += out.slice(last);
  return result;
}

/**
 * Build the cleaned compile unit: main.tex plus every `\input`/`\include`
 * file it references, recursively. `\input` paths are resolved relative
 * to the directory of the file CURRENTLY being walked (so a nested
 * include with a relative path resolves correctly), with `.tex` appended
 * when missing. Each retained line is comment- and verbatim-stripped and
 * tagged with its real source file + 1-based line number. Unconditional
 * includes whose target is missing are reported as `missing-input`;
 * conditional includes (\IfFileExists / \InputIfFileExists) are exempt.
 */
export function loadCompileUnit(mainTexPath: string): {
  records: LineRecord[];
  missing: { file: string; line: number; target: string }[];
} {
  const records: LineRecord[] = [];
  const missing: { file: string; line: number; target: string }[] = [];
  const seen = new Set<string>();

  const walk = (filePath: string) => {
    const abs = resolve(filePath);
    if (seen.has(abs)) return;
    seen.add(abs);
    if (!existsSync(abs)) return;
    const fileDir = dirname(abs);
    const rawLines = readFileSync(abs, "utf8").split("\n");
    let inVerbatim: string | null = null;

    for (let i = 0; i < rawLines.length; i++) {
      const raw = rawLines[i];

      // Verbatim env tracking (before comment stripping — \end may be on
      // the same line as content, but envs are line-oriented in practice).
      if (inVerbatim) {
        if (new RegExp(`\\\\end\\{${inVerbatim}\\}`).test(raw)) {
          inVerbatim = null;
        }
        records.push({ file: abs, line: i + 1, text: "" });
        continue;
      }
      const begin = raw.match(/\\begin\{([A-Za-z*]+)\}/);
      if (begin && VERBATIM_ENVS.has(begin[1])) {
        // Single-line \begin{verbatim}…\end{verbatim} guard.
        if (!new RegExp(`\\\\end\\{${begin[1]}\\}`).test(raw)) {
          inVerbatim = begin[1];
        }
        records.push({ file: abs, line: i + 1, text: "" });
        continue;
      }

      const cleaned = stripInlineVerb(stripComment(raw));
      records.push({ file: abs, line: i + 1, text: cleaned });

      // Follow \input{...} / \include{...}.
      const conditional = /\\(?:IfFileExists|InputIfFileExists)\b/.test(cleaned);
      const inputRe = /\\(?:input|include)\s*\{([^}]+)\}/g;
      let m: RegExpExecArray | null;
      while ((m = inputRe.exec(cleaned)) !== null) {
        let target = m[1].trim();
        if (!/\.[A-Za-z]+$/.test(target)) target += ".tex";
        const resolved = isAbsolute(target) ? target : join(fileDir, target);
        if (existsSync(resolved)) {
          walk(resolved);
        } else if (!conditional) {
          missing.push({ file: abs, line: i + 1, target: m[1].trim() });
        }
      }
    }
  };

  walk(resolve(mainTexPath));
  return { records, missing };
}

/** Definers that ERROR on redefinition → a second one is fatal. */
const FATAL_DEFINERS = new Set([
  "newcommand", "DeclareMathOperator", "DeclarePairedDelimiter",
  "NewDocumentCommand",
]);

/**
 * Extract macro names DEFINED across the compile unit, plus every
 * fatal-on-redefinition definition occurrence (for the duplicate check).
 */
export function extractDefinedMacros(records: LineRecord[]): {
  defined: Set<string>;
  definitions: Map<string, { file: string; line: number }[]>;
} {
  const defined = new Set<string>();
  const definitions = new Map<string, { file: string; line: number }[]>();

  const defRe =
    /\\(newcommand|renewcommand|providecommand|DeclareRobustCommand|DeclareMathOperator\*?|DeclarePairedDelimiter|DeclareDocumentCommand|NewDocumentCommand|RenewDocumentCommand|ProvideDocumentCommand|def|edef|gdef|xdef|let)\s*\*?\s*\{?\s*(\\[a-zA-Z@]+)/g;
  const ifRe = /\\newif\s*\\(if[a-zA-Z@]+)/g;

  for (const rec of records) {
    if (!rec.text) continue;
    let m: RegExpExecArray | null;
    defRe.lastIndex = 0;
    while ((m = defRe.exec(rec.text)) !== null) {
      const definer = m[1].replace(/\*$/, "");
      const name = m[2];
      defined.add(name);
      if (FATAL_DEFINERS.has(definer)) {
        const arr = definitions.get(name) ?? [];
        arr.push({ file: rec.file, line: rec.line });
        definitions.set(name, arr);
      }
    }
    ifRe.lastIndex = 0;
    while ((m = ifRe.exec(rec.text)) !== null) {
      const base = m[1].slice(2);
      defined.add("\\" + m[1]);
      defined.add("\\" + base + "true");
      defined.add("\\" + base + "false");
    }
  }
  return { defined, definitions };
}

/** Extract every multi-letter control-word USE, with file + line. */
export function extractUsedMacros(
  records: LineRecord[],
): { name: string; file: string; line: number }[] {
  const used: { name: string; file: string; line: number }[] = [];
  for (const rec of records) {
    if (!rec.text) continue;
    // Multi-letter control words only. Single-char control symbols
    // (\&, \%, \\, \{, \|, …) are always defined and never the culprit.
    const re = /\\([a-zA-Z@]+)/g;
    let m: RegExpExecArray | null;
    while ((m = re.exec(rec.text)) !== null) {
      used.push({ name: "\\" + m[1], file: rec.file, line: rec.line });
    }
  }
  return used;
}

function loadAllowlist(): Set<string> {
  if (!existsSync(ALLOWLIST_PATH)) return new Set();
  try {
    const raw = JSON.parse(readFileSync(ALLOWLIST_PATH, "utf8")) as
      | string[]
      | { macros: string[] };
    const list = Array.isArray(raw) ? raw : raw.macros;
    return new Set(list);
  } catch {
    return new Set();
  }
}

/** TeX/LaTeX core control words always present regardless of allowlist. */
const CORE_ALWAYS: Set<string> = new Set([
  "\\begin", "\\end", "\\left", "\\right", "\\input", "\\include",
  "\\item", "\\par", "\\relax", "\\noindent", "\\centering",
]);

function relPath(file: string): string {
  const root = resolve(__dirname, "..", "..");
  return file.startsWith(root) ? file.slice(root.length + 1) : file;
}

export function runPreflight(mainTexPath: string): PreflightResult {
  const { records, missing } = loadCompileUnit(mainTexPath);
  const filesScanned = new Set(records.map((r) => r.file)).size;
  const { defined, definitions } = extractDefinedMacros(records);
  const used = extractUsedMacros(records);
  const allowlist = loadAllowlist();
  const issues: PreflightIssue[] = [];

  // ── Check D: missing \input target ─────────────────────────────────
  for (const miss of missing) {
    issues.push({
      check: "missing-input",
      macro: miss.target,
      file: miss.file,
      line: miss.line,
      message:
        `Unconditional \\input/\\include target "${miss.target}" does ` +
        `not exist (${relPath(miss.file)}:${miss.line}). pdflatex aborts ` +
        `with "File \`${miss.target}' not found". Generate the file, fix ` +
        `the path, or guard with \\IfFileExists if it is optional.`,
    });
  }

  // ── Check A: duplicate fatal-on-redefinition definition ────────────
  for (const [name, locs] of definitions) {
    if (locs.length > 1) {
      const where = locs.map((l) => `${relPath(l.file)}:${l.line}`).join(", ");
      issues.push({
        check: "duplicate-newcommand",
        macro: name,
        file: locs[1].file,
        line: locs[1].line,
        message:
          `Command ${name} defined ${locs.length}× by a ` +
          `fatal-on-redefinition definer (${where}). pdflatex aborts ` +
          `with "Command ${name} already defined". Define it once ` +
          `(preamble OR manifest macros, not both); use ` +
          `\\providecommand / \\renewcommand for an intentional override.`,
      });
    }
  }

  // ── Check B: undefined control sequence ────────────────────────────
  const known = (n: string) =>
    defined.has(n) || allowlist.has(n) || CORE_ALWAYS.has(n);
  const reported = new Set<string>();
  for (const u of used) {
    if (known(u.name) || reported.has(u.name)) continue;
    reported.add(u.name);
    issues.push({
      check: "undefined-macro",
      macro: u.name,
      file: u.file,
      line: u.line,
      message:
        `Undefined control sequence ${u.name} (first use ` +
        `${relPath(u.file)}:${u.line}). pdflatex aborts with ` +
        `"! Undefined control sequence". Define it in latex/preamble.tex ` +
        `/ the manifest macros, use an existing command (e.g. ` +
        `\\mathrm{tr} not \\tr), or — if it is a genuine standard/package ` +
        `command whose package is loaded in the preamble — add it to ` +
        `content/pipeline/latex-known-macros.json (re-seed with --seed).`,
    });
  }

  // ── Check C: fragile math-accent as bare sub/superscript ───────────
  const accentRe = new RegExp(
    "[\\^_]\\\\(" + MATH_ACCENTS.join("|") + ")(?![a-zA-Z])",
    "g",
  );
  for (const rec of records) {
    if (!rec.text) continue;
    accentRe.lastIndex = 0;
    let m: RegExpExecArray | null;
    while ((m = accentRe.exec(rec.text)) !== null) {
      // Skip if the ^/_ is itself escaped (\^ text-circumflex, \_ underscore).
      if (precedingBackslashes(rec.text, m.index) % 2 !== 0) continue;
      const accent = "\\" + m[1];
      const ctx = rec.text.slice(Math.max(0, m.index - 4), m.index + 14);
      issues.push({
        check: "fragile-accent-script",
        macro: accent,
        file: rec.file,
        line: rec.line,
        message:
          `Math accent ${accent} used as a bare sub/superscript ` +
          `(${relPath(rec.file)}:${rec.line}: …${ctx}…). Its ` +
          `\\mathpalette expansion breaks as a sole script token ` +
          `("! Missing { inserted"). Brace it: X^{${accent}{q}} not ` +
          `X^${accent}{q}.`,
      });
    }
  }

  return {
    ok: issues.length === 0,
    issues,
    definedCount: defined.size,
    usedCount: new Set(used.map((u) => u.name)).size,
    allowlistCount: allowlist.size,
    filesScanned,
  };
}

/** Seed/refresh the standard-command allowlist from a clean compile unit. */
export function seedAllowlist(mainTexPath: string): string[] {
  const { records } = loadCompileUnit(mainTexPath);
  const { defined } = extractDefinedMacros(records);
  const used = new Set(extractUsedMacros(records).map((u) => u.name));
  // Allowlist = everything USED that is not locally DEFINED and not a
  // core-always token. Since the seed compile unit compiles clean, every
  // such token resolves to a standard / package command.
  const allow = [...used]
    .filter((n) => !defined.has(n) && !CORE_ALWAYS.has(n))
    .sort();
  const payload = {
    _comment:
      "Seeded standard/package LaTeX control sequences in actual use " +
      "across main.tex + chapters/*.tex (comment + verbatim contexts " +
      "stripped). Regenerate with: bun run pipeline/latex-preflight.ts " +
      "--seed. Adding a name asserts it is a real standard/package " +
      "command whose package is loaded in latex/preamble.tex.",
    macros: allow,
  };
  writeFileSync(ALLOWLIST_PATH, JSON.stringify(payload, null, 2) + "\n");
  return allow;
}

// ── CLI ──────────────────────────────────────────────────────────────
if (import.meta.main) {
  const args = process.argv.slice(2);
  const json = args.includes("--json");
  const warn = args.includes("--warn");
  const seed = args.includes("--seed");
  const positional = args.filter((a) => !a.startsWith("--"));
  const mainTex = resolve(
    positional[0] ?? join(__dirname, "..", "..", "main.tex"),
  );

  if (!existsSync(mainTex)) {
    console.error(
      `[latex-preflight] main.tex not found at ${mainTex}.\n` +
        `  Generate it first: bun run pipeline/build.ts ` +
        `<paper>.ts --generate-main --main-out ../main.tex`,
    );
    process.exit(2);
  }

  if (seed) {
    const allow = seedAllowlist(mainTex);
    console.log(
      `[latex-preflight] seeded allowlist with ${allow.length} ` +
        `standard control sequences → ${ALLOWLIST_PATH}`,
    );
    process.exit(0);
  }

  const result = runPreflight(mainTex);

  if (json) {
    console.log(JSON.stringify(result, null, 2));
  } else {
    console.log(
      `[latex-preflight] ${mainTex} (+${result.filesScanned - 1} \\input files)\n` +
        `  defined macros: ${result.definedCount}  ` +
        `used: ${result.usedCount}  allowlist: ${result.allowlistCount}`,
    );
    if (result.ok) {
      console.log("  ✓ no fatal LaTeX patterns detected");
    } else {
      const byCheck = new Map<string, PreflightIssue[]>();
      for (const iss of result.issues) {
        const arr = byCheck.get(iss.check) ?? [];
        arr.push(iss);
        byCheck.set(iss.check, arr);
      }
      for (const [check, arr] of byCheck) {
        console.log(`\n  ✗ ${check} (${arr.length}):`);
        for (const iss of arr.slice(0, 50)) {
          console.log(`    ${iss.message}`);
        }
        if (arr.length > 50) console.log(`    … and ${arr.length - 50} more`);
      }
    }
  }

  if (!result.ok && !warn) process.exit(1);
}
