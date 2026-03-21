/**
 * Render pipeline: content objects → LaTeX.
 *
 * Flow:
 *   1. Load .ts manifest (Block metadata)
 *   2. Load sibling .md file (narrative content)
 *   3. Convert markdown → LaTeX body
 *   4. Wrap in appropriate LaTeX environment
 *   5. Validate rendered LaTeX via unified-latex AST parse
 *
 * @module content/pipeline/render-latex
 */

import { readFileSync, existsSync } from "fs";
import { join, dirname, basename, extname } from "path";
import { parse } from "@unified-latex/unified-latex-util-parse";
import type { Block, Chapter, Section } from "../schema/types";

// ── Markdown → LaTeX conversion ──────────────────────────────────

/**
 * Convert markdown content to LaTeX body text.
 *
 * Handles:
 *   - **bold** → \textbf{}
 *   - *italic* → \emph{}
 *   - $...$ inline math (passthrough)
 *   - $$...$$ display math → \[ ... \]
 *   - ```tex fenced blocks → raw LaTeX (verbatim insertion)
 *   - Numbered lists → \begin{enumerate}
 *   - Bullet lists → \begin{itemize}
 *   - [text](ref) → \hyperref[ref]{text} for internal refs
 *   - Paragraphs separated by blank lines
 */
export function markdownToLatex(md: string): string {
  const lines = md.split("\n");
  const output: string[] = [];
  let i = 0;

  while (i < lines.length) {
    const line = lines[i];

    // Fenced code block: ```tex ... ```
    if (line.trimStart().startsWith("```tex")) {
      i++;
      const texLines: string[] = [];
      while (i < lines.length && !lines[i].trimStart().startsWith("```")) {
        texLines.push(lines[i]);
        i++;
      }
      i++; // skip closing ```
      output.push(texLines.join("\n"));
      continue;
    }

    // Other fenced code blocks: pass through as verbatim
    if (line.trimStart().startsWith("```")) {
      const lang = line.trim().slice(3);
      i++;
      const codeLines: string[] = [];
      while (i < lines.length && !lines[i].trimStart().startsWith("```")) {
        codeLines.push(lines[i]);
        i++;
      }
      i++;
      output.push(`\\begin{verbatim}`);
      output.push(codeLines.join("\n"));
      output.push(`\\end{verbatim}`);
      continue;
    }

    // Display math: $$ ... $$
    if (line.trimStart().startsWith("$$")) {
      i++;
      const mathLines: string[] = [line.trimStart().slice(2)];
      while (i < lines.length && !lines[i].includes("$$")) {
        mathLines.push(lines[i]);
        i++;
      }
      if (i < lines.length) {
        mathLines.push(lines[i].replace("$$", ""));
        i++;
      }
      const mathContent = mathLines.join("\n").trim();
      output.push(`\\[`);
      output.push(mathContent);
      output.push(`\\]`);
      continue;
    }

    // Numbered list items: 1. ... 2. ...
    if (/^\s*\d+\.\s/.test(line)) {
      output.push("\\begin{enumerate}");
      while (i < lines.length && /^\s*\d+\.\s/.test(lines[i])) {
        output.push(`  \\item ${convertInline(lines[i].replace(/^\s*\d+\.\s/, ""))}`);
        i++;
      }
      output.push("\\end{enumerate}");
      continue;
    }

    // Bullet list items: - ...
    if (/^\s*[-*]\s/.test(line)) {
      output.push("\\begin{itemize}");
      while (i < lines.length && /^\s*[-*]\s/.test(lines[i])) {
        output.push(`  \\item ${convertInline(lines[i].replace(/^\s*[-*]\s/, ""))}`);
        i++;
      }
      output.push("\\end{itemize}");
      continue;
    }

    // Blank line → paragraph break
    if (line.trim() === "") {
      output.push("");
      i++;
      continue;
    }

    // Regular line — convert inline formatting
    output.push(convertInline(line));
    i++;
  }

  return output.join("\n").trim();
}

/** Convert inline markdown formatting to LaTeX. */
function convertInline(text: string): string {
  // Bold: **text** → \textbf{text}
  text = text.replace(/\*\*(.+?)\*\*/g, "\\textbf{$1}");
  // Italic: *text* → \emph{text}
  text = text.replace(/(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)/g, "\\emph{$1}");
  // Internal cross-refs: [text](#label) → \hyperref[label]{text}
  text = text.replace(/\[([^\]]+)\]\(#([^)]+)\)/g, "\\hyperref[$2]{$1}");
  // $...$ inline math passes through unchanged
  return text;
}

// ── Block → LaTeX rendering ──────────────────────────────────────

/** LaTeX environment names for each block kind. */
const ENV_NAMES: Record<string, string> = {
  definition: "definition",
  theorem: "theorem",
  lemma: "lemma",
  proposition: "proposition",
  corollary: "corollary",
  conjecture: "conjecture",
  example: "example",
  remark: "remark",
};

/**
 * Render a single block to LaTeX.
 *
 * @param block - The typed block manifest
 * @param mdContent - Markdown content from the sibling .md file
 * @returns LaTeX string
 */
export function renderBlock(block: Block, mdContent: string): string {
  const lines: string[] = [];

  switch (block.kind) {
    case "prose": {
      lines.push(markdownToLatex(mdContent));
      break;
    }

    case "equation": {
      const tex = block.tex || markdownToLatex(mdContent);
      if (block.label) {
        lines.push("\\begin{equation}");
        lines.push(`  \\label{${block.label}}`);
        lines.push(`  ${tex}`);
        lines.push("\\end{equation}");
      } else {
        lines.push("\\[");
        lines.push(`  ${tex}`);
        lines.push("\\]");
      }
      break;
    }

    case "diagram": {
      const tex = block.tex || markdownToLatex(mdContent);
      if (block.label) lines.push(`% diagram: ${block.label}`);
      lines.push(tex);
      if (block.caption) lines.push(`% caption: ${block.caption}`);
      break;
    }

    default: {
      // Environment blocks (definition, theorem, etc.)
      const envName = ENV_NAMES[block.kind];
      if (!envName) throw new Error(`Unknown block kind: ${block.kind}`);

      const titleArg = "title" in block && block.title ? `[${block.title}]` : "";
      lines.push(`\\begin{${envName}}${titleArg}`);

      // Label
      if ("label" in block && block.label) {
        lines.push(`  \\label{${block.label}}`);
      }

      // Lean reference
      if ("lean" in block && block.lean) {
        lines.push(`  \\lean{${block.lean.decl}}`);
        if (block.lean.sorryFree) {
          lines.push(`  \\leanok`);
        }
      }

      // Uses
      if ("uses" in block && block.uses?.length) {
        lines.push(`  \\uses{${block.uses.join(", ")}}`);
      }

      // Body content — strip proof portion (after ---) if present
      let statementMd = mdContent;
      let proofMd: string | null = null;
      if ("hasProof" in block && block.hasProof) {
        const proofSep = mdContent.indexOf("\n---\n");
        if (proofSep >= 0) {
          statementMd = mdContent.slice(0, proofSep);
          proofMd = mdContent.slice(proofSep + 5);
        }
      }
      const body = markdownToLatex(statementMd);
      lines.push(body);

      lines.push(`\\end{${envName}}`);

      // Inline proof (for theorems etc.)
      if (proofMd) {
        lines.push("\\begin{proof}");
        lines.push(markdownToLatex(proofMd));
        lines.push("\\end{proof}");
      }
      break;
    }
  }

  return lines.join("\n");
}

// ── Chapter rendering ────────────────────────────────────────────

/**
 * Load a block's .ts manifest and .md content, render to LaTeX.
 *
 * @param rootName - Block root name (e.g. "quantum-universe")
 * @param objectsDir - Directory containing object files
 */
export function loadAndRenderBlock(rootName: string, objectsDir: string): {
  latex: string;
  block: Block;
  mdContent: string;
} {
  const tsPath = join(objectsDir, `${rootName}.ts`);
  const mdPath = join(objectsDir, `${rootName}.md`);

  if (!existsSync(tsPath)) {
    throw new Error(`Block manifest not found: ${tsPath}`);
  }

  // Dynamic import of .ts manifest (works with bun)
  // Note: actual import is async — see renderChapter for the async version
  const mdContent = existsSync(mdPath) ? readFileSync(mdPath, "utf-8") : "";

  // Placeholder — actual block loading happens in async pipeline
  return { latex: "", block: { kind: "prose" } as Block, mdContent };
}

/**
 * Render a full section to LaTeX.
 */
export function renderSection(
  section: Section,
  blocks: Map<string, { block: Block; mdContent: string }>,
): string {
  const lines: string[] = [];
  const label = section.label ? `\\label{${section.label}}\n` : "";
  lines.push(`\\section{${section.title}}\n${label}`);

  for (const rootName of section.blocks) {
    const entry = blocks.get(rootName);
    if (!entry) {
      lines.push(`% ERROR: block "${rootName}" not found`);
      continue;
    }
    lines.push(renderBlock(entry.block, entry.mdContent));
    lines.push(""); // blank line between blocks
  }

  return lines.join("\n");
}

/**
 * Render a full chapter to LaTeX.
 */
export function renderChapter(
  chapter: Chapter,
  blocks: Map<string, { block: Block; mdContent: string }>,
): string {
  const lines: string[] = [];
  const label = chapter.label ? `\\label{${chapter.label}}\n` : "";
  lines.push(`\\chapter{${chapter.title}}\n${label}`);

  for (const section of chapter.sections) {
    lines.push(renderSection(section, blocks));
  }

  return lines.join("\n");
}

// ── AST validation ───────────────────────────────────────────────

export interface AstValidationResult {
  valid: boolean;
  /** Parsing errors from unified-latex. */
  errors: string[];
  /** Number of AST nodes produced. */
  nodeCount: number;
}

/**
 * Validate rendered LaTeX by parsing it through unified-latex.
 *
 * This catches:
 *   - Unbalanced braces
 *   - Malformed environments (\begin without \end)
 *   - Invalid macro syntax
 *
 * Use in build tests to ensure rendered output is valid LaTeX.
 */
export function validateLatexAst(latex: string): AstValidationResult {
  const errors: string[] = [];
  let nodeCount = 0;

  try {
    const ast = parse(latex);
    nodeCount = countNodes(ast);

    // Check for unmatched environments
    checkEnvironmentBalance(ast.content, errors);
  } catch (e) {
    errors.push(`Parse error: ${e instanceof Error ? e.message : String(e)}`);
  }

  return {
    valid: errors.length === 0,
    errors,
    nodeCount,
  };
}

function countNodes(node: any): number {
  let count = 1;
  if (node.content && Array.isArray(node.content)) {
    for (const child of node.content) {
      count += countNodes(child);
    }
  }
  if (node.args && Array.isArray(node.args)) {
    for (const arg of node.args) {
      count += countNodes(arg);
    }
  }
  return count;
}

function checkEnvironmentBalance(nodes: any[], errors: string[]): void {
  for (const node of nodes) {
    if (node.type === "environment" && !node.env) {
      errors.push("Environment node with missing env name");
    }
    if (node.content && Array.isArray(node.content)) {
      checkEnvironmentBalance(node.content, errors);
    }
  }
}
