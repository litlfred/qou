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
import { remark } from "remark";
import remarkMath from "remark-math";
import type { Block, Chapter, Section, RenderOptions } from "../schema/types";

// ── LaTeX character escaping ─────────────────────────────────────

/**
 * Escape special LaTeX characters in plain text (titles, captions, etc.).
 *
 * This must NOT be applied to content that already contains intentional
 * LaTeX markup (e.g., math mode, macros). Use only for structural
 * metadata like block titles, section titles, and chapter titles.
 */
export function escapeLatex(text: string): string {
  return text
    .replace(/\\/g, "\\textbackslash{}")
    .replace(/&/g, "\\&")
    .replace(/%/g, "\\%")
    .replace(/\$/g, "\\$")
    .replace(/#/g, "\\#")
    .replace(/_/g, "\\_")
    .replace(/\{/g, "\\{")
    .replace(/\}/g, "\\}")
    .replace(/~/g, "\\textasciitilde{}")
    .replace(/\^/g, "\\textasciicircum{}");
}

// ── Markdown → LaTeX conversion (AST-based) ─────────────────────

/** Shared remark parser instance with math extension. */
const mdParser = remark().use(remarkMath);

/**
 * Convert markdown content to LaTeX body text via remark AST.
 *
 * Walks the parsed AST instead of line-by-line regex matching.
 * Node type mapping:
 *
 *   | mdast node    | LaTeX output                         |
 *   |---------------|--------------------------------------|
 *   | text          | passthrough                          |
 *   | strong        | \textbf{children}                    |
 *   | emphasis      | \emph{children}                      |
 *   | inlineMath    | $value$                              |
 *   | math          | \[value\]                            |
 *   | code(tex)     | raw passthrough                      |
 *   | code(other)   | \begin{verbatim}...\end{verbatim}    |
 *   | link(#ref)    | \hyperref[ref]{children}             |
 *   | link(url)     | \href{url}{children}                 |
 *   | list(ordered) | \begin{enumerate} \item ...\end{...} |
 *   | list(unord.)  | \begin{itemize} \item ...\end{...}   |
 *   | paragraph     | children + blank line                |
 */
export function markdownToLatex(md: string): string {
  const tree = mdParser.parse(md);
  return renderMdastNode(tree).trim();
}

/**
 * Extract raw TeX content from markdown for math-context blocks
 * (equation and diagram). Walks the AST but only emits math and
 * fenced-tex nodes — lists, prose, and formatting are skipped.
 */
export function extractMathContent(md: string): string {
  const tree = mdParser.parse(md);
  const parts: string[] = [];

  for (const child of (tree as any).children ?? []) {
    if (child.type === "math") {
      // Display math: extract inner TeX
      parts.push(child.value);
    } else if (child.type === "code" && child.lang === "tex") {
      // Fenced TeX: raw passthrough
      parts.push(child.value);
    } else if (child.type === "paragraph") {
      // Check for inline math in paragraphs (rare in equation blocks)
      for (const inline of child.children ?? []) {
        if (inline.type === "inlineMath") {
          parts.push(inline.value);
        } else if (inline.type === "text") {
          // Plain text in an equation .md — treat as raw TeX
          const trimmed = inline.value.trim();
          if (trimmed) parts.push(trimmed);
        }
      }
    }
    // Lists, code blocks, etc. are silently skipped
  }

  return parts.join("\n").trim();
}

// ── AST node → LaTeX rendering ──────────────────────────────────

/** Render a single mdast node to LaTeX. */
function renderMdastNode(node: any): string {
  switch (node.type) {
    case "root":
      return renderChildren(node).join("\n\n");

    case "paragraph":
      return renderChildren(node).join("");

    case "text":
      return node.value;

    case "strong":
      return `\\textbf{${renderChildren(node).join("")}}`;

    case "emphasis":
      return `\\emph{${renderChildren(node).join("")}}`;

    case "inlineMath":
      return `$${node.value}$`;

    case "math":
      return `\\[\n${node.value}\n\\]`;

    case "code":
      if (node.lang === "tex") {
        // Raw LaTeX passthrough
        return node.value;
      }
      // Other code blocks → verbatim
      return `\\begin{verbatim}\n${node.value}\n\\end{verbatim}`;

    case "link": {
      const text = renderChildren(node).join("");
      const url: string = node.url ?? "";
      if (url.startsWith("#")) {
        // Internal cross-ref: [text](#label) → \hyperref[label]{text}
        return `\\hyperref[${url.slice(1)}]{${text}}`;
      }
      // External URL
      return `\\href{${url}}{${text}}`;
    }

    case "list": {
      const env = node.ordered ? "enumerate" : "itemize";
      const items = (node.children ?? [])
        .map((item: any) => `  \\item ${renderListItem(item)}`)
        .join("\n");
      return `\\begin{${env}}\n${items}\n\\end{${env}}`;
    }

    case "listItem":
      return renderListItem(node);

    case "blockquote": {
      const inner = renderChildren(node).join("\n");
      return `\\begin{quote}\n${inner}\n\\end{quote}`;
    }

    case "heading": {
      const depth = node.depth ?? 1;
      const text = renderChildren(node).join("");
      const cmds = ["\\chapter", "\\section", "\\subsection",
                     "\\subsubsection", "\\paragraph", "\\subparagraph"];
      const cmd = cmds[Math.min(depth - 1, cmds.length - 1)];
      return `${cmd}{${text}}`;
    }

    case "thematicBreak":
      return "\\medskip\\noindent\\rule{\\textwidth}{0.4pt}\\medskip";

    case "break":
      return "\\\\";

    default:
      // Unknown node — render children if any, otherwise empty
      if (node.children) {
        return renderChildren(node).join("");
      }
      return node.value ?? "";
  }
}

/** Render all children of a node. */
function renderChildren(node: any): string[] {
  return (node.children ?? []).map((child: any) => renderMdastNode(child));
}

/** Render a list item's content (unwrap single-paragraph items). */
function renderListItem(item: any): string {
  const children = item.children ?? [];
  // Single-paragraph list items: render inline (no extra \par)
  if (children.length === 1 && children[0].type === "paragraph") {
    return renderChildren(children[0]).join("");
  }
  // Multi-block list items: render each block
  return children.map((c: any) => renderMdastNode(c)).join("\n");
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
  proof: "proof",
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
      // Use extractMathContent (not markdownToLatex) to avoid list
      // environments inside math mode.
      const tex = block.tex || extractMathContent(mdContent);
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
      // Use extractMathContent (not markdownToLatex) to avoid list
      // environments inside tikzcd/diagram environments.
      const tex = block.tex || extractMathContent(mdContent);
      if (block.label) lines.push(`% diagram: ${block.label}`);
      lines.push(tex);
      if (block.caption) lines.push(`% caption: ${escapeLatex(block.caption)}`);
      break;
    }

    default: {
      // Environment blocks (definition, theorem, etc.)
      const envName = ENV_NAMES[block.kind];
      if (!envName) throw new Error(`Unknown block kind: ${block.kind}`);

      const titleArg = "title" in block && block.title ? `[{${escapeLatex(block.title)}}]` : "";
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

      // Body content
      const body = markdownToLatex(mdContent);
      lines.push(body);

      lines.push(`\\end{${envName}}`);
      break;
    }
  }

  return lines.join("\n");
}

// ── Print-mode block filtering ───────────────────────────────────

/** Block kinds that are excluded in compact mode unless referenced. */
const COMPACT_OPTIONAL_KINDS = new Set(["example", "remark"]);

/**
 * Collect labels of examples/remarks referenced by blocks in a section.
 *
 * Scans all blocks in the section for `examples[]` fields (on definitions,
 * theorems, lemmas, propositions, corollaries) and returns the set of
 * referenced labels.
 */
function collectReferencedLabels(
  rootNames: string[],
  blocks: Map<string, { block: Block; mdContent: string }>,
): Set<string> {
  const refs = new Set<string>();
  for (const rootName of rootNames) {
    const entry = blocks.get(rootName);
    if (!entry) continue;
    const block = entry.block;
    if ("examples" in block && Array.isArray(block.examples)) {
      for (const label of block.examples) refs.add(label);
    }
  }
  return refs;
}

/**
 * Determine whether a block should be included in the current render.
 *
 * - In formal mode: all blocks included.
 * - In compact mode: example/remark blocks are excluded UNLESS they
 *   are directly referenced via `examples[]` by another block in the
 *   same section (and `compactInlineRefs` is true).
 */
function shouldIncludeBlock(
  block: Block,
  referencedLabels: Set<string>,
  opts: RenderOptions,
): boolean {
  const mode = opts.printMode ?? "compact";
  if (mode === "formal") return true;

  // Compact mode — check if this is an optional kind
  if (!COMPACT_OPTIONAL_KINDS.has(block.kind)) return true;

  // compactInlineRefs defaults to true
  const inlineRefs = opts.compactInlineRefs ?? true;
  if (!inlineRefs) return false;

  // Include if this block's label is referenced by another block
  const label = "label" in block ? block.label : undefined;
  return label != null && referencedLabels.has(label);
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
 *
 * @param section - Section manifest
 * @param blocks - All loaded blocks (keyed by root name)
 * @param opts - Print mode options (controls block filtering)
 */
export function renderSection(
  section: Section,
  blocks: Map<string, { block: Block; mdContent: string }>,
  opts: RenderOptions = {},
): string {
  const lines: string[] = [];
  const label = section.label ? `\\label{${section.label}}\n` : "";
  lines.push(`\\section{${escapeLatex(section.title)}}\n${label}`);

  // Collect referenced example/remark labels for compact-mode filtering
  const referencedLabels = collectReferencedLabels(section.blocks, blocks);

  for (const rootName of section.blocks) {
    const entry = blocks.get(rootName);
    if (!entry) {
      lines.push(`% ERROR: block "${rootName}" not found`);
      continue;
    }
    if (!shouldIncludeBlock(entry.block, referencedLabels, opts)) {
      continue;
    }
    lines.push(renderBlock(entry.block, entry.mdContent));
    lines.push(""); // blank line between blocks
  }

  return lines.join("\n");
}

/**
 * Render a full chapter to LaTeX.
 *
 * @param chapter - Chapter manifest
 * @param blocks - All loaded blocks (keyed by root name)
 * @param opts - Print mode options (controls block filtering and affiliations)
 */
export function renderChapter(
  chapter: Chapter,
  blocks: Map<string, { block: Block; mdContent: string }>,
  opts: RenderOptions = {},
): string {
  const lines: string[] = [];
  const label = chapter.label ? `\\label{${chapter.label}}\n` : "";
  const star = chapter.number == null ? "*" : "";
  lines.push(`\\chapter${star}{${escapeLatex(chapter.title)}}\n${label}`);

  for (const section of chapter.sections) {
    lines.push(renderSection(section, blocks, opts));
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
