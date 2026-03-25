/**
 * Build pipeline: content objects → LaTeX chapters.
 *
 * Loads a paper manifest (with ChapterRef[]), resolves chapter .ts files,
 * loads all blocks from chapter directories, renders to LaTeX,
 * validates AST integrity, writes output.
 *
 * Usage:
 *   bun run pipeline/build.ts [paper.ts] [--out-dir chapters/]
 *
 * @module content/pipeline/build
 */

import { readFileSync, writeFileSync, existsSync, mkdirSync } from "fs";
import { join, dirname, resolve } from "path";
import type { Paper, Chapter, Section, Block, RenderOptions } from "../schema/types";
import { renderChapter, validateLatexAst } from "./render-latex";
import { generateMainTex } from "./generate-main-tex";

// ── Build ────────────────────────────────────────────────────────

export interface BuildResult {
  /** Rendered LaTeX per chapter (keyed by chapter number). */
  chapters: Map<number, string>;
  /** Chapter slug names derived from directory names (e.g. "quantum-observable-universe"). */
  chapterSlugs: Map<number, string>;
  /** Validation issues encountered. */
  issues: { level: string; message: string }[];
  /** Whether all rendered LaTeX passes AST validation. */
  astValid: boolean;
}

/**
 * Build a paper from its manifest.
 *
 * Resolves ChapterRef[] → Chapter[] by importing chapter .ts manifests
 * from their directories, then loads block .ts + .md pairs from the
 * same chapter directories.
 *
 * @param paperPath - Path to the paper .ts manifest
 * @param opts - Render options (print mode, compact inline refs)
 */
export async function buildPaper(
  paperPath: string,
  opts: RenderOptions = {},
): Promise<BuildResult> {
  const issues: { level: string; message: string }[] = [];
  const paperDir = dirname(paperPath);

  // 1. Load paper manifest
  const paperMod = await import(paperPath);
  const paper: Paper = paperMod.default;

  // 2. Resolve chapters and load all blocks
  const resolvedChapters: Chapter[] = [];
  const chapterSlugs = new Map<number, string>();
  const blocks = new Map<string, { block: Block; mdContent: string }>();

  for (const chRef of paper.chapters) {
    const chDir = join(paperDir, chRef.dir);
    const chPath = join(chDir, `${chRef.dir}.ts`);

    if (!existsSync(chPath)) {
      issues.push({ level: "error", message: `Chapter manifest not found: ${chPath}` });
      continue;
    }

    try {
      const chMod = await import(chPath);
      const chapter: Chapter = chMod.default;
      resolvedChapters.push(chapter);

      // Extract slug from dir name: "ch1-quantum-observable-universe" → "quantum-observable-universe"
      const slug = chRef.dir.replace(/^ch\d+-/, "");
      const key = chapter.number ?? -(resolvedChapters.length);
      chapterSlugs.set(key, slug);

      // Load blocks from the chapter directory
      for (const sec of chapter.sections) {
        if (!("blocks" in sec)) continue;
        const section = sec as Section;
        for (const rootName of section.blocks) {
          if (blocks.has(rootName)) continue;

          const tsPath = join(chDir, `${rootName}.ts`);
          const mdPath = join(chDir, `${rootName}.md`);

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
    } catch (e) {
      issues.push({
        level: "error",
        message: `Failed to load chapter "${chRef.dir}": ${e instanceof Error ? e.message : String(e)}`,
      });
    }
  }

  // 3. Render chapters
  const chapters = new Map<number, string>();
  let astValid = true;

  for (const chapter of resolvedChapters) {
    const latex = renderChapter(chapter, blocks, opts);
    const chKey = chapter.number ?? -(resolvedChapters.indexOf(chapter) + 1);
    chapters.set(chKey, latex);

    // AST validation
    const ast = validateLatexAst(latex);
    if (!ast.valid) {
      astValid = false;
      for (const err of ast.errors) {
        issues.push({ level: "error", message: `Chapter ${chapter.number ?? chapter.title} AST: ${err}` });
      }
    }
  }

  return { chapters, chapterSlugs, issues, astValid };
}

// ── CLI entry point ──────────────────────────────────────────────

if (import.meta.main) {
  const args = process.argv.slice(2);
  const defaultPaper = join(import.meta.dir, "../quantum-observable-universe/quantum-observable-universe.ts");
  // Resolve relative paths against cwd so `bun run pipeline/build.ts rel/path` works
  const paperPath = resolve(args[0] || defaultPaper);
  const outDirIdx = args.indexOf("--out-dir");
  const outDir = resolve(outDirIdx >= 0 ? args[outDirIdx + 1] : join(import.meta.dir, "../../chapters"));

  // Parse print mode options
  const printModeIdx = args.indexOf("--print-mode");
  const printMode = printModeIdx >= 0 ? args[printModeIdx + 1] as "formal" | "compact" : "compact";
  const noInlineRefs = args.includes("--no-inline-refs");

  console.log(`Building paper: ${paperPath}`);
  console.log(`Output dir: ${outDir}`);
  console.log(`Print mode: ${printMode}${noInlineRefs ? " (inline refs disabled)" : ""}\n`);

  const result = await buildPaper(paperPath, {
    printMode,
    compactInlineRefs: !noInlineRefs,
  });

  // Print issues
  for (const issue of result.issues) {
    const icon = issue.level === "error" ? "✗" : issue.level === "warning" ? "⚠" : "ℹ";
    console.log(`  ${icon} ${issue.message}`);
  }

  // Write chapter output
  if (!existsSync(outDir)) mkdirSync(outDir, { recursive: true });

  for (const [num, latex] of result.chapters) {
    const slug = result.chapterSlugs.get(num);
    const filename = slug ? `${slug}.tex` : `chapter-${num}.tex`;
    const outPath = join(outDir, filename);
    writeFileSync(outPath, latex);
    console.log(`  → ${outPath}`);
  }

  // Generate main.tex from paper manifest + shared preamble
  if (args.includes("--generate-main")) {
    const mainOutIdx = args.indexOf("--main-out");
    const mainOutPath = resolve(mainOutIdx >= 0 ? args[mainOutIdx + 1] : "main.tex");
    const preambleIdx = args.indexOf("--preamble");
    const preamblePath = resolve(
      preambleIdx >= 0 ? args[preambleIdx + 1] : join(import.meta.dir, "../../latex/preamble.tex"),
    );
    // Compute relative chapters dir from the main.tex output location
    const chaptersDirIdx = args.indexOf("--chapters-dir");
    const chaptersDir = chaptersDirIdx >= 0 ? args[chaptersDirIdx + 1] : "chapters/";

    const paperMod = await import(paperPath);
    const paperData: Paper = paperMod.default;

    const mainTex = generateMainTex(paperData, {
      preamblePath,
      chaptersDir,
      chapterSlugs: result.chapterSlugs,
    });
    writeFileSync(mainOutPath, mainTex);
    console.log(`\n  → main.tex: ${mainOutPath}`);
  }

  console.log(`\nAST validation: ${result.astValid ? "✓ pass" : "✗ fail"}`);
  const errorCount = result.issues.filter(i => i.level === "error").length;
  console.log(`Issues: ${errorCount} error(s), ${result.issues.length - errorCount} warning(s)`);

  process.exit(errorCount > 0 ? 1 : 0);
}
