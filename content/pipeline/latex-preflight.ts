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
 * Macro DEFINITIONS live in main.tex's inlined preamble; macro USES and
 * fragile constructs live mostly in the chapter bodies, so both must be
 * scanned together.
 *
 * Checks
 * ------
 *   A. duplicate-newcommand  — a control sequence defined by \newcommand /
 *      \DeclareMathOperator / … more than once → "! LaTeX Error: Command
 *      \X already defined." Canonical instance: the manifest re-emitting
 *      \newcommand{\pp}{\mathfrak{p}} while the preamble already defined
 *      \pp = p (fix b9e19df6). Zero false positives by construction.
 *
 *   B. undefined-macro — a control sequence USED that is neither defined
 *      in the compile unit nor in the seeded standard-command allowlist
 *      (latex-known-macros.json) → "! Undefined control sequence."
 *      (e.g. bare \tr). The allowlist is SEEDED from a clean-compiling
 *      compile unit via `--seed`, so every standard / package command in
 *      actual use is captured: zero false positives at seed time;
 *      re-introducing an undefined macro is then flagged.
 *
 *   C. fragile-accent-script — a math accent (\check, \hat, …) used as the
 *      bare argument of a sub/superscript, e.g. `Q^\check{q}`. The
 *      accent's \mathpalette expansion breaks as a sole script token
 *      ("! Missing { inserted."). Fix: brace it — `Q^{\check{q}}`.
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

export interface PreflightIssue {
  check: "duplicate-newcommand" | "undefined-macro" | "fragile-accent-script";
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

/** One source line tagged with its originating file + line number. */
interface LineRecord {
  file: string;
  line: number;
  text: string;
}

/** Strip TeX line/percent comments (a `%` not preceded by a backslash). */
function stripComment(line: string): string {
  let out = "";
  for (let i = 0; i < line.length; i++) {
    if (line[i] === "%" && (i === 0 || line[i - 1] !== "\\")) break;
    out += line[i];
  }
  return out;
}

/**
 * Build the full compile unit: main.tex plus every `\input`/`\include`
 * file it references, recursively. Each line keeps its source file +
 * 1-based line number so issues point at the real location an author
 * edits. `\input` paths are resolved relative to the repo root (the
 * parent of the directory holding main.tex is the repo root here, but
 * the generated `\input{chapters/foo}` paths are relative to main.tex's
 * directory), with a `.tex` extension added when missing.
 */
export function loadCompileUnit(mainTexPath: string): LineRecord[] {
  const records: LineRecord[] = [];
  const seen = new Set<string>();
  const baseDir = dirname(resolve(mainTexPath));

  const walk = (filePath: string) => {
    const abs = resolve(filePath);
    if (seen.has(abs)) return;
    seen.add(abs);
    if (!existsSync(abs)) return;
    const lines = readFileSync(abs, "utf8").split("\n");
    for (let i = 0; i < lines.length; i++) {
      const text = lines[i];
      records.push({ file: abs, line: i + 1, text });
      // Follow \input{...} / \include{...} (single arg, no comment).
      const stripped = stripComment(text);
      const inputRe = /\\(?:input|include)\s*\{([^}]+)\}/g;
      let m: RegExpExecArray | null;
      while ((m = inputRe.exec(stripped)) !== null) {
        let target = m[1].trim();
        if (!/\.tex$/.test(target)) target += ".tex";
        const resolved = isAbsolute(target) ? target : join(baseDir, target);
        walk(resolved);
      }
    }
  };

  walk(resolve(mainTexPath));
  return records;
}

/**
 * Extract macro names DEFINED across the compile unit, plus every
 * \newcommand-family definition occurrence (for the duplicate check).
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
    const line = stripComment(rec.text);
    let m: RegExpExecArray | null;
    defRe.lastIndex = 0;
    while ((m = defRe.exec(line)) !== null) {
      const definer = m[1].replace(/\*$/, "");
      const name = m[2];
      defined.add(name);
      // Only \newcommand-family collisions are fatal ("already defined").
      // \renewcommand / \def / \let intentionally overwrite.
      const isNewcommand =
        definer === "newcommand" ||
        definer === "DeclareMathOperator" ||
        definer === "DeclarePairedDelimiter" ||
        definer === "NewDocumentCommand";
      if (isNewcommand) {
        const arr = definitions.get(name) ?? [];
        arr.push({ file: rec.file, line: rec.line });
        definitions.set(name, arr);
      }
    }
    ifRe.lastIndex = 0;
    while ((m = ifRe.exec(line)) !== null) {
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
    const line = stripComment(rec.text);
    // Multi-letter control words only. Single-char control symbols
    // (\&, \%, \\, \{, \|, …) are always defined and never the culprit.
    const re = /\\([a-zA-Z@]+)/g;
    let m: RegExpExecArray | null;
    while ((m = re.exec(line)) !== null) {
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
  const records = loadCompileUnit(mainTexPath);
  const filesScanned = new Set(records.map((r) => r.file)).size;
  const { defined, definitions } = extractDefinedMacros(records);
  const used = extractUsedMacros(records);
  const allowlist = loadAllowlist();
  const issues: PreflightIssue[] = [];

  // ── Check A: duplicate \newcommand ─────────────────────────────────
  for (const [name, locs] of definitions) {
    if (locs.length > 1) {
      const where = locs.map((l) => `${relPath(l.file)}:${l.line}`).join(", ");
      issues.push({
        check: "duplicate-newcommand",
        macro: name,
        file: locs[1].file,
        line: locs[1].line,
        message:
          `Command ${name} defined ${locs.length}× via \\newcommand ` +
          `(${where}). pdflatex aborts with "Command ${name} already ` +
          `defined". Define it once (preamble OR manifest macros, not ` +
          `both); use \\providecommand / \\renewcommand for an override.`,
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
    const line = stripComment(rec.text);
    accentRe.lastIndex = 0;
    let m: RegExpExecArray | null;
    while ((m = accentRe.exec(line)) !== null) {
      const accent = "\\" + m[1];
      const ctx = line.slice(Math.max(0, m.index - 4), m.index + 14);
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
  const records = loadCompileUnit(mainTexPath);
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
      "across main.tex + chapters/*.tex. Regenerate with: " +
      "bun run pipeline/latex-preflight.ts --seed. Adding a name asserts " +
      "it is a real standard/package command whose package is loaded in " +
      "latex/preamble.tex.",
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
