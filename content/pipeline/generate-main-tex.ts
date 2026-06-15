/**
 * Generate a per-paper main.tex from the shared preamble template
 * and the paper's .ts manifest.
 *
 * Paper-specific parts generated from manifest:
 *   - Custom macros (\newcommand)
 *   - Title page with CC license
 *   - hypersetup (PDF metadata)
 *   - Abstract
 *   - Chapter \input lines (excluding standalone appendices)
 *   - Appendix B: Bibliography (BibTeX)
 *
 * Standalone appendices (chapters with tabLabel other than "I") are
 * excluded from the main paper and get their own .tex files via
 * generateStandaloneAppendixTex().
 *
 * Usage:
 *   bun run pipeline/generate-main-tex.ts <paper.ts> [--preamble preamble.tex] [--out main.tex] [--chapters-dir chapters/]
 *
 * @module content/pipeline/generate-main-tex
 */

import { readFileSync, writeFileSync } from "fs";
import { join, resolve } from "path";
import type { Paper } from "../schema/types";
import { escapeLatex } from "./render-latex";

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
  /** Chapter indices to exclude from the main paper (standalone appendices). */
  excludeChapterIndices?: Set<number>;
  /** Labels from excluded appendix chapters to declare as phantom anchors. */
  phantomLabels?: string[];
  /**
   * If set, the shared preamble is assumed precompiled into a `<useFormat>.fmt`
   * format file (see scripts/build-fmt.sh). Instead of inlining the preamble,
   * emit a `%&<useFormat>` reference as the first line. The per-document tail
   * (paper macros + print-mode read) is always emitted live. Default
   * (undefined) keeps the full inline-preamble behavior.
   */
  useFormat?: string;
  /**
   * If true, load the `memoize` package live (per-render, never dumped into a
   * `.fmt`) so tikz / tikz-cd pictures are cached to per-box PDFs keyed on box
   * source. Requires the compile to pass `-shell-escape`. Default off.
   */
  memoize?: boolean;
}

/**
 * Emit shared preamble + paper-specific macros (used by both main and standalone).
 */
/**
 * Per-document preamble tail: paper macros + the per-render print-mode read.
 * Emitted live in BOTH the inline-preamble path and the precompiled-format
 * path, because these are per-paper / per-render and must never be baked into
 * a shared `.fmt` format.
 */
function emitPerDocPreambleTail(paper: Paper, memoize?: boolean): string[] {
  const lines: string[] = [];

  // Paper-specific macros (per-paper, not shared → stay live).
  if (paper.macros && Object.keys(paper.macros).length > 0) {
    lines.push("% ── Paper macros (generated from manifest) ────────────────────────────────");
    for (const [name, macro] of Object.entries(paper.macros)) {
      const comment = macro.unicode ? `  % ${macro.unicode}` : "";
      lines.push(`\\newcommand{\\${name}}{${macro.tex}}${comment}`);
    }
    lines.push("");
  }

  // Diagram memoization (opt-in; requires -shell-escape). Loaded LIVE here —
  // never dumped into a `.fmt` — so the cache toggle is per-render. memoize
  // auto-caches tikz / tikz-cd pictures to per-box PDFs keyed on box source.
  if (memoize) {
    lines.push("% ── Diagram memoization (per-render; needs -shell-escape) ───────────────────");
    // Resilient load: skip gracefully if memoize.sty is absent (older TeX
    // distributions predate it) rather than aborting the compile.
    // Direct memoize's cache files to .memo/ (matches the actions/cache path;
    // default is CWD → clutter + CI miss) and register tikzcd (not auto-
    // memoized; only tikzpicture is). Gemini #2310. Verified against the
    // installed memoize on the first TeX run.
    lines.push("\\IfFileExists{memoize.sty}{%");
    lines.push("  \\usepackage[dir=.memo]{memoize}%");
    lines.push("  \\memoizeenvironment{tikzcd}%");
    lines.push("}{}% memoize.sty absent -> diagram caching disabled (compile continues)");
    lines.push("");
  }

  // Per-render print-mode flag — kept live, NOT dumped into a `.fmt` format.
  // `\newif\ifshowaffiliations` stays in the shared preamble (dumpable); only
  // this file-read is per-document, since print-mode.tex is written per render
  // by the MCP render tool. Lands after the preamble (where `\newif` is
  // defined) and before `\begin{document}` / the title page (which consumes
  // `\ifshowaffiliations`).
  lines.push("% ── Print mode (per-render; lives outside any dumped format) ────────────────");
  lines.push("\\IfFileExists{print-mode.tex}{\\input{print-mode.tex}}{}");
  lines.push("");

  return lines;
}

/**
 * Emit the document preamble: either the full shared preamble inlined
 * (default), or a `%&<format>` reference to a precompiled `.fmt` that already
 * contains it (when `useFormat` is set — see scripts/build-fmt.sh). The
 * per-document tail (paper macros + print-mode) is always emitted live.
 */
function emitPreambleAndMacros(
  paper: Paper,
  preamblePath: string,
  useFormat?: string,
  memoize?: boolean,
): string[] {
  const lines: string[] = [];

  if (useFormat) {
    // Shared preamble is precompiled into <useFormat>.fmt. Reference it as the
    // VERY FIRST line of the file (TeX `%&format` mechanism) and do not inline
    // the preamble — pdflatex resumes in the post-preamble state.
    lines.push(`%&${useFormat}`);
    lines.push("");
  } else {
    // Inline the full shared preamble (default behavior).
    const preamble = readFileSync(preamblePath, "utf-8");
    lines.push(preamble.trimEnd());
    lines.push("");
  }

  lines.push(...emitPerDocPreambleTail(paper, memoize));
  return lines;
}

/**
 * Generate a complete main.tex for a paper.
 *
 * Chapters listed in `opts.excludeChapterIndices` are omitted from the
 * main PDF (they become standalone appendix PDFs instead).
 */
export function generateMainTex(
  paper: Paper,
  opts: GenerateMainTexOptions,
): string {
  const lines: string[] = [];

  // 1. Preamble + macros
  lines.push(...emitPreambleAndMacros(paper, opts.preamblePath, opts.useFormat, opts.memoize));

  // 2. Metadata (for hypersetup PDF fields)
  lines.push("% ── Metadata (generated from manifest) ────────────────────────────────────");
  const authorName = escapeLatexMeta(paper.authors[0] || "");
  lines.push(`\\title{${escapeLatexMeta(paper.title)}}`);
  lines.push(`\\author{${authorName}}`);
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

  // 3. Begin document
  lines.push("% ──────────────────────────────────────────────────────────────────────────────");
  lines.push("\\begin{document}");
  lines.push("");

  // Title page — title, author, date only. Centered, vertically balanced.
  // The CC license + copyright notice now lives on its own page (front matter
  // book convention).
  lines.push("% ── Title page ────────────────────────────────────────────────────────────");
  lines.push("\\begin{titlepage}");
  lines.push("\\centering");
  lines.push("\\vspace*{3cm}");
  lines.push(`{\\LARGE\\bfseries ${escapeLatexMeta(paper.title)}}\\\\[2em]`);
  if (paper.affiliations?.length) {
    lines.push("\\ifshowaffiliations");
    lines.push(`  {\\large ${authorName}\\thanks{${escapeLatexMeta(paper.affiliations[0])}}}\\\\[1em]`);
    lines.push("\\else");
    lines.push(`  {\\large ${authorName}}\\\\[1em]`);
    lines.push("\\fi");
  } else {
    lines.push(`{\\large ${authorName}}\\\\[1em]`);
  }
  lines.push(`{\\large ${paper.date ? escapeLatexMeta(paper.date) : "\\today"}}`);
  lines.push("\\vfill");
  lines.push("\\end{titlepage}");
  lines.push("");

  // Copyright page — CC license notice on its own page.
  lines.push("% ── Copyright page ────────────────────────────────────────────────────────");
  lines.push("\\thispagestyle{empty}");
  lines.push("\\null\\vfill");
  lines.push("\\begin{center}{\\small");
  lines.push("  \\ccby\\\\[0.5em]");
  lines.push("  This work is licensed under a");
  lines.push("  \\href{https://creativecommons.org/licenses/by/4.0/}{%");
  lines.push("    Creative Commons Attribution 4.0 International License}.\\\\[0.3em]");
  lines.push("  You are free to share and adapt this material for any purpose,\\\\");
  lines.push("  provided appropriate credit is given, a link to the license is provided,\\\\");
  lines.push("  and any changes made are indicated.");
  lines.push("}\\end{center}");
  lines.push("\\vfill\\null");
  lines.push("\\clearpage");
  lines.push("");

  // Abstract — placed before TOC, book-style.
  if (paper.abstract) {
    lines.push("% ── Abstract ──────────────────────────────────────────────────────────────");
    lines.push("\\begin{abstract}");
    lines.push(paper.abstract);
    lines.push("\\end{abstract}");
    lines.push("");
  }

  lines.push("\\proofstatuslegend");
  lines.push("\\clearpage");
  lines.push("");

  // Introduction (if present) is emitted before the TOC per chapter-reorg
  // intent, so readers see framing before navigation.
  const sortedEntries = [...opts.chapterSlugs.entries()].sort(
    ([a], [b]) => a - b,
  );
  const introEntry = sortedEntries.find(
    ([num, slug]) => slug === "introduction" && !opts.excludeChapterIndices?.has(num),
  );
  if (introEntry) {
    lines.push("% ── Introduction (pre-TOC) ───────────────────────────────────────────────");
    lines.push(`\\input{${opts.chaptersDir}${introEntry[1]}}`);
    lines.push("");
  }

  // Table of contents — depth limited to chapters + sections by preamble.
  // The renderer prepends \clearpage to every chapter (see render-latex.ts
  // renderChapter), so no extra \clearpage is needed here.
  lines.push("% ── Table of contents ─────────────────────────────────────────────────────");
  lines.push("\\tableofcontents");
  lines.push("");

  // 4. Chapter includes (excluding standalone appendices)
  // Emits an optional `\part{...}` banner before any chapter whose
  // ChapterRef carries a `partTitle` (groups subsequent chapters
  // visually until the next `partTitle` or end-of-paper).
  lines.push("% ── Chapters (generated from manifest) ────────────────────────────────────");
  for (const [num, slug] of sortedEntries) {
    if (opts.excludeChapterIndices?.has(num)) continue;
    if (introEntry && num === introEntry[0]) continue; // already emitted pre-TOC
    const partTitle = paper.chapters[num]?.partTitle;
    if (partTitle) {
      lines.push(`\\part{${escapeLatex(partTitle)}}`);
    }
    lines.push(`\\input{${opts.chaptersDir}${slug}}`);
  }
  lines.push("");

  // 5. Appendix B: Bibliography (BibTeX)
  lines.push("% ── Appendix B: References ─────────────────────────────────────────────────");
  lines.push("\\clearpage");
  lines.push("\\chapter*{Appendix B. References}");
  lines.push("\\addcontentsline{toc}{chapter}{Appendix B. References}");
  lines.push("\\bibliographystyle{plain}");
  lines.push("\\bibliography{references}");
  lines.push("");

  // 6. Phantom labels for excluded appendix chapters.
  // Blocks in standalone appendices (glossary, knot table, etc.) are not
  // compiled into the main PDF, but may be referenced via \hyperref from
  // the main body. Declaring phantom labels prevents "Hyper reference
  // undefined" warnings without including the full appendix content.
  if (opts.phantomLabels?.length) {
    lines.push("% ── Phantom labels (excluded appendix blocks) ─────────────────────────────");
    lines.push("% These labels are defined in standalone appendix PDFs but referenced from");
    lines.push("% the main paper body. Phantom declarations prevent hyperref warnings.");
    for (const label of opts.phantomLabels) {
      lines.push(`\\phantomsection\\label{${label}}`);
    }
    lines.push("");
  }

  lines.push("\\end{document}");

  return lines.join("\n") + "\n";
}

/**
 * Generate a standalone .tex file for a single appendix chapter.
 *
 * Produces a self-contained document that can be compiled independently.
 */
export function generateStandaloneAppendixTex(
  paper: Paper,
  chapterSlug: string,
  chapterTitle: string,
  opts: { preamblePath: string; chaptersDir: string; useFormat?: string; memoize?: boolean },
): string {
  const lines: string[] = [];

  // 1. Preamble + macros (same as main paper)
  lines.push(...emitPreambleAndMacros(paper, opts.preamblePath, opts.useFormat, opts.memoize));

  // 2. Metadata
  const authorName = escapeLatexMeta(paper.authors[0] || "");
  lines.push("% ── Metadata ──────────────────────────────────────────────────────────────");
  lines.push(`\\title{${escapeLatexMeta(chapterTitle)}}`);
  lines.push(`\\author{${authorName}}`);
  lines.push(`\\date{${paper.date ? escapeLatexMeta(paper.date) : "\\today"}}`);
  lines.push("");

  lines.push("\\hypersetup{");
  lines.push(`  pdftitle  = {${escapeLatexMeta(chapterTitle)}},`);
  lines.push(`  pdfauthor = {${escapeLatexMeta(paper.authors.join(", "))}},`);
  lines.push("  colorlinks = true,");
  lines.push("  linkcolor  = blue,");
  lines.push("  citecolor  = blue,");
  lines.push("  urlcolor   = blue,");
  lines.push("}");
  lines.push("");

  // 3. Begin document
  lines.push("\\begin{document}");
  lines.push("\\maketitle");
  lines.push("");

  // 4. Include the chapter
  lines.push(`\\input{${opts.chaptersDir}${chapterSlug}}`);
  lines.push("");

  // 5. Bibliography (if the chapter has citations)
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

  // --use-format <name>: emit a `%&<name>` reference instead of inlining the
  // shared preamble (the preamble must be precompiled via scripts/build-fmt.sh).
  const useFormatIdx = args.indexOf("--use-format");
  const useFormat = useFormatIdx >= 0 ? args[useFormatIdx + 1] : undefined;
  // --memoize: load memoize live to cache tikz/tikz-cd boxes (needs -shell-escape).
  const memoize = args.includes("--memoize");

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
    useFormat,
    memoize,
  });

  writeFileSync(outPath, tex);
  console.log(`✓ main.tex written to ${outPath}`);
}
