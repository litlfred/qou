/**
 * Build pipeline: content objects → LaTeX chapters.
 *
 * Loads a document manifest, resolves all blocks, renders to LaTeX,
 * validates AST integrity, writes output.
 *
 * Usage:
 *   bun run pipeline/build.ts [document.ts] [--out-dir chapters/]
 *
 * @module content/pipeline/build
 */

import { readFileSync, writeFileSync, existsSync, mkdirSync } from "fs";
import { join, dirname } from "path";
import type { Document, Block, Chapter } from "../schema/types";
import { renderBlock, renderChapter, validateLatexAst } from "./render-latex";
import { validateObjects } from "./validate";

// ── Build ────────────────────────────────────────────────────────

export interface BuildResult {
  /** Rendered LaTeX per chapter (keyed by chapter number). */
  chapters: Map<number, string>;
  /** Validation issues encountered. */
  issues: { level: string; message: string }[];
  /** Whether all rendered LaTeX passes AST validation. */
  astValid: boolean;
}

/**
 * Build a document from its manifest.
 *
 * @param docPath - Path to the document .ts manifest
 * @param objectsDir - Directory containing block .ts + .md files
 */
export async function buildDocument(
  docPath: string,
  objectsDir: string,
): Promise<BuildResult> {
  const issues: { level: string; message: string }[] = [];

  // 1. Validate all objects first
  const validation = await validateObjects(objectsDir);
  issues.push(
    ...validation.issues.map(i => ({ level: i.level, message: `[${i.block}] ${i.message}` })),
  );

  // 2. Load document manifest
  const docMod = await import(docPath);
  const doc: Document = docMod.default;

  // 3. Load all blocks
  const blocks = new Map<string, { block: Block; mdContent: string }>();

  for (const chapter of doc.chapters) {
    for (const section of chapter.sections) {
      for (const rootName of section.blocks) {
        if (blocks.has(rootName)) continue;

        const tsPath = join(objectsDir, `${rootName}.ts`);
        const mdPath = join(objectsDir, `${rootName}.md`);

        try {
          const mod = await import(tsPath);
          const block: Block = mod.default;
          const mdContent = existsSync(mdPath) ? readFileSync(mdPath, "utf-8") : "";
          blocks.set(rootName, { block, mdContent });
        } catch (e) {
          issues.push({
            level: "error",
            message: `Failed to load block "${rootName}": ${e instanceof Error ? e.message : String(e)}`,
          });
        }
      }
    }
  }

  // 4. Render chapters
  const chapters = new Map<number, string>();
  let astValid = true;

  for (const chapter of doc.chapters) {
    const latex = renderChapter(chapter, blocks);
    chapters.set(chapter.number, latex);

    // AST validation
    const ast = validateLatexAst(latex);
    if (!ast.valid) {
      astValid = false;
      for (const err of ast.errors) {
        issues.push({ level: "error", message: `Chapter ${chapter.number} AST: ${err}` });
      }
    }
  }

  return { chapters, issues, astValid };
}

// ── CLI entry point ──────────────────────────────────────────────

if (import.meta.main) {
  const args = process.argv.slice(2);
  const docPath = args[0] || join(import.meta.dir, "../chapters/document.ts");
  const outDirIdx = args.indexOf("--out-dir");
  const outDir = outDirIdx >= 0 ? args[outDirIdx + 1] : join(import.meta.dir, "../../chapters");
  const objectsDir = join(import.meta.dir, "../objects");

  console.log(`Building document: ${docPath}`);
  console.log(`Objects dir: ${objectsDir}`);
  console.log(`Output dir: ${outDir}\n`);

  const result = await buildDocument(docPath, objectsDir);

  // Print issues
  for (const issue of result.issues) {
    const icon = issue.level === "error" ? "✗" : issue.level === "warning" ? "⚠" : "ℹ";
    console.log(`  ${icon} ${issue.message}`);
  }

  // Write output
  if (!existsSync(outDir)) mkdirSync(outDir, { recursive: true });

  for (const [num, latex] of result.chapters) {
    const outPath = join(outDir, `chapter-${num}.tex`);
    writeFileSync(outPath, latex);
    console.log(`  → ${outPath}`);
  }

  console.log(`\nAST validation: ${result.astValid ? "✓ pass" : "✗ fail"}`);
  const errorCount = result.issues.filter(i => i.level === "error").length;
  console.log(`Issues: ${errorCount} error(s), ${result.issues.length - errorCount} warning(s)`);

  process.exit(errorCount > 0 ? 1 : 0);
}
