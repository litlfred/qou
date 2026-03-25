/**
 * Generate a per-paper main.tex from the shared preamble template
 * and the paper's .ts manifest.
 *
 * Paper-specific parts generated from manifest:
 *   - Custom macros (\newcommand)
 *   - Title, author, affiliations, date
 *   - hypersetup (PDF metadata)
 *   - Abstract
 *   - Chapter \input lines
 *   - Bibliography
 *
 * Usage:
 *   bun run pipeline/generate-main-tex.ts <paper.ts> [--preamble preamble.tex] [--out main.tex] [--chapters-dir chapters/]
 *
 * @module content/pipeline/generate-main-tex
 */

import { readFileSync, writeFileSync, existsSync } from "fs";
import { join, dirname, resolve } from "path";
import type { Paper } from "../schema/types";

/**
 * Escape text for use in LaTeX metadata fields (title, author, etc.).
 * Does NOT escape math or other intentional LaTeX — only structural chars.
 */
function escapeLatexMeta(text: string): string {
  return text
    .replace(/&/g, "\\&")
    .replace(/#/g, "\\#")
    .replace(/%/g, "\\%")
    .replace(/_/g, "\\_");
}

export interface GenerateMainTexOptions {
  /** Path to the shared preamble.tex template. */
  preamblePath: string;
  /** Directory where chapter .tex files live (for \input paths). */
  chaptersDir: string;
  /** Chapter slugs keyed by chapter number (from BuildResult). */
  chapterSlugs: Map<number, string>;
}

/**
 * Generate a complete main.tex for a paper.
 */
export function generateMainTex(
  paper: Paper,
  opts: GenerateMainTexOptions,
): string {
  const preamble = readFileSync(opts.preamblePath, "utf-8");

  const lines: string[] = [];

  // 1. Shared preamble (everything up to and including \IfFileExists)
  lines.push(preamble.trimEnd());
  lines.push("");

  // 2. Paper-specific macros
  if (paper.macros && Object.keys(paper.macros).length > 0) {
    lines.push("% ── Paper macros (generated from manifest) ────────────────────────────────");
    for (const [name, macro] of Object.entries(paper.macros)) {
      const comment = macro.unicode ? `  % ${macro.unicode}` : "";
      lines.push(`\\newcommand{\\${name}}{${macro.tex}}${comment}`);
    }
    lines.push("");
  }

  // 3. Metadata
  lines.push("% ── Metadata (generated from manifest) ────────────────────────────────────");
  lines.push(`\\title{${escapeLatexMeta(paper.title)}}`);

  // Author with optional affiliations
  const authorName = escapeLatexMeta(paper.authors[0] || "");
  if (paper.affiliations?.length) {
    lines.push("\\ifshowaffiliations");
    lines.push(`  \\author{${authorName}\\thanks{${escapeLatexMeta(paper.affiliations[0])}}}`);
    lines.push("\\else");
    lines.push(`  \\author{${authorName}}`);
    lines.push("\\fi");
  } else {
    lines.push(`\\author{${authorName}}`);
  }
  // Multi-author support (if needed in the future, extend here)

  lines.push(`\\date{${paper.date ? escapeLatexMeta(paper.date) : "\\today"}}`);
  lines.push("");

  // hypersetup
  lines.push("\\hypersetup{");
  lines.push(`  pdftitle  = {${escapeLatexMeta(paper.title)}},`);
  lines.push(`  pdfauthor = {${escapeLatexMeta(paper.authors.join(", "))}},`);
  lines.push("  colorlinks = true,");
  lines.push("  linkcolor  = blue,");
  lines.push("  citecolor  = blue,");
  lines.push("  urlcolor   = blue,");
  lines.push("}");
  lines.push("");

  // 4. Begin document
  lines.push("% ──────────────────────────────────────────────────────────────────────────────");
  lines.push("\\begin{document}");
  lines.push("");
  lines.push("\\maketitle");
  lines.push("");

  // License notice
  lines.push("% ── License notice ────────────────────────────────────────────────────────");
  lines.push("\\thispagestyle{empty}");
  lines.push("\\vspace*{\\fill}");
  lines.push("\\begin{center}");
  lines.push("  \\ccby\\\\[0.5em]");
  lines.push("  This work is licensed under a");
  lines.push("  \\href{https://creativecommons.org/licenses/by/4.0/}{%");
  lines.push("    Creative Commons Attribution 4.0 International License}.\\\\[0.3em]");
  lines.push("  You are free to share and adapt this material for any purpose,\\\\");
  lines.push("  provided appropriate credit is given, a link to the license is provided,\\\\");
  lines.push("  and any changes made are indicated.");
  lines.push("\\end{center}");
  lines.push("\\vspace*{\\fill}");
  lines.push("");

  // Table of contents
  lines.push("% ── Table of contents ─────────────────────────────────────────────────────");
  lines.push("\\tableofcontents");
  lines.push("");

  // Abstract
  if (paper.abstract) {
    lines.push("% ── Abstract ──────────────────────────────────────────────────────────────");
    lines.push("\\begin{abstract}");
    lines.push(paper.abstract);
    lines.push("\\end{abstract}");
    lines.push("");
  }

  lines.push("\\proofstatuslegend");
  lines.push("");

  // 5. Chapter includes
  lines.push("% ── Chapters (generated from manifest) ────────────────────────────────────");
  // Sort by chapter number, then emit \input lines
  const sortedEntries = [...opts.chapterSlugs.entries()].sort(
    ([a], [b]) => a - b,
  );
  for (const [num, slug] of sortedEntries) {
    lines.push(`\\input{${opts.chaptersDir}${slug}}`);
  }
  lines.push("");

  // 6. Bibliography
  lines.push("% ── Bibliography ──────────────────────────────────────────────────────────");
  lines.push("\\bibliographystyle{plain}");
  lines.push("\\bibliography{references}");
  lines.push("");
  lines.push("\\end{document}");

  return lines.join("\n") + "\n";
}

// ── CLI entry point ──────────────────────────────────────────────

if (import.meta.main) {
  const args = process.argv.slice(2);
  const defaultPaper = join(
    import.meta.dir,
    "../quantum-observable-universe/quantum-observable-universe.ts",
  );
  const paperPath = resolve(args[0] || defaultPaper);

  const preambleIdx = args.indexOf("--preamble");
  const preamblePath = resolve(
    preambleIdx >= 0 ? args[preambleIdx + 1] : join(import.meta.dir, "../../latex/preamble.tex"),
  );

  const outIdx = args.indexOf("--out");
  const outPath = resolve(outIdx >= 0 ? args[outIdx + 1] : "main.tex");

  const chaptersDirIdx = args.indexOf("--chapters-dir");
  const chaptersDir = chaptersDirIdx >= 0 ? args[chaptersDirIdx + 1] : "chapters/";

  console.log(`Generating main.tex for: ${paperPath}`);
  console.log(`Preamble: ${preamblePath}`);
  console.log(`Output: ${outPath}`);

  // Import paper manifest
  const paperMod = await import(paperPath);
  const paper: Paper = paperMod.default;

  // Import build to get chapter slugs
  const { buildPaper } = await import("./build");
  const result = await buildPaper(paperPath);

  const tex = generateMainTex(paper, {
    preamblePath,
    chaptersDir,
    chapterSlugs: result.chapterSlugs,
  });

  writeFileSync(outPath, tex);
  console.log(`✓ main.tex written to ${outPath}`);
}
