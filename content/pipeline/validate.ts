/**
 * Validation pipeline for content objects.
 *
 * Runs three levels of validation:
 *   1. Zod schema validation (shape + types)
 *   2. Constraint rules (file existence, cross-refs, lean requirements)
 *   3. AST validation (rendered LaTeX parses cleanly)
 *
 * Supports two modes:
 *   - Paper directory: detects paper manifest, recurses into chapter dirs
 *   - Flat directory: validates all .ts files as blocks (legacy)
 *
 * Usage:
 *   bun run pipeline/validate.ts [paper-dir-or-objects-dir]
 *
 * @module content/pipeline/validate
 */

import { readdirSync, readFileSync, existsSync, statSync } from "fs";
import { resolve, join, basename, extname } from "path";
import {
  BlockSchema,
  PaperSchema,
  ChapterSchema,
  CONSTRAINT_RULES,
  type ConstraintContext,
} from "../schema/constraints";
import type { Block, Paper, Chapter, Section, ValidationIssue, ValidationResult } from "../schema/types";
import { renderBlock, validateLatexAst, markdownToLatex } from "./render-latex";

// ── File discovery ───────────────────────────────────────────────

/** Find all .ts manifest files in a directory (excluding index, pipeline). */
function discoverManifests(dir: string): string[] {
  if (!existsSync(dir)) return [];
  return readdirSync(dir)
    .filter(f => f.endsWith(".ts") && !f.startsWith("index") && !f.startsWith("_"))
    .map(f => basename(f, ".ts"));
}

/** Get root name from a file path. */
function rootName(file: string): string {
  return basename(file, extname(file));
}

/**
 * Detect if a directory contains a paper manifest.
 * Convention: paper manifest has the same name as its directory.
 */
function detectPaperManifest(dir: string): string | null {
  const dirName = basename(dir);
  const manifestPath = join(dir, `${dirName}.ts`);
  return existsSync(manifestPath) ? manifestPath : null;
}

// ── Validation ───────────────────────────────────────────────────

/**
 * Validate a single directory of block .ts files.
 * Returns blocks map and issues; caller aggregates labels across chapters.
 */
async function loadBlocksFromDir(
  dir: string,
  blockNames: string[] | null,
  issues: ValidationIssue[],
): Promise<Map<string, Block>> {
  const blocks = new Map<string, Block>();
  const names = blockNames ?? discoverManifests(dir);

  for (const name of names) {
    const tsPath = join(dir, `${name}.ts`);
    if (!existsSync(tsPath)) {
      issues.push({
        level: "error",
        block: name,
        message: `Block manifest not found: ${tsPath}`,
        file: `${name}.ts`,
      });
      continue;
    }

    try {
      const mod = await import(tsPath);
      const block: Block = mod.default;

      const result = BlockSchema.safeParse(block);
      if (!result.success) {
        for (const err of result.error.issues) {
          issues.push({
            level: "error",
            block: name,
            message: `Schema: ${err.path.join(".")}: ${err.message}`,
            file: `${name}.ts`,
          });
        }
        continue;
      }

      blocks.set(name, block);
    } catch (e) {
      issues.push({
        level: "error",
        block: name,
        message: `Import error: ${e instanceof Error ? e.message : String(e)}`,
        file: `${name}.ts`,
      });
    }
  }

  return blocks;
}

/**
 * Validate all content objects in a paper or flat directory.
 *
 * If the directory contains a paper manifest (same name as dir),
 * loads chapters and validates blocks within each chapter directory.
 * Otherwise falls back to flat-directory validation.
 *
 * @param objectsDir - Paper directory or flat directory with .ts + .md + .lean files
 * @returns Validation result with issues
 */
export async function validateObjects(objectsDir: string): Promise<ValidationResult> {
  const issues: ValidationIssue[] = [];

  // Detect paper manifest
  const paperManifestPath = detectPaperManifest(objectsDir);

  // Collect all blocks across all chapter directories (or flat dir)
  const allBlocks = new Map<string, { block: Block; dir: string }>();
  const allLabels = new Set<string>();

  if (paperManifestPath) {
    // ── Paper mode: validate paper manifest, then recurse into chapters ──
    try {
      const paperMod = await import(paperManifestPath);
      const paper: Paper = paperMod.default;

      const paperResult = PaperSchema.safeParse(paper);
      if (!paperResult.success) {
        for (const err of paperResult.error.issues) {
          issues.push({
            level: "error",
            block: basename(paperManifestPath, ".ts"),
            message: `Paper schema: ${err.path.join(".")}: ${err.message}`,
            file: basename(paperManifestPath),
          });
        }
        // Paper manifest is invalid — can't recurse
        return { valid: false, issues };
      }

      // Validate each chapter
      for (const chRef of paper.chapters) {
        const chDir = join(objectsDir, chRef.dir);
        const chPath = join(chDir, `${chRef.dir}.ts`);

        if (!existsSync(chPath)) {
          issues.push({
            level: "error",
            block: chRef.dir,
            message: `Chapter manifest not found: ${chPath}`,
          });
          continue;
        }

        try {
          const chMod = await import(chPath);
          const chapter: Chapter = chMod.default;

          const chResult = ChapterSchema.safeParse(chapter);
          if (!chResult.success) {
            for (const err of chResult.error.issues) {
              issues.push({
                level: "error",
                block: chRef.dir,
                message: `Chapter schema: ${err.path.join(".")}: ${err.message}`,
                file: `${chRef.dir}.ts`,
              });
            }
            continue;
          }

          // Collect block names from sections
          const blockNames: string[] = [];
          for (const sec of chapter.sections) {
            if ("blocks" in sec) {
              blockNames.push(...(sec as Section).blocks);
            }
          }

          // Load and validate blocks in this chapter dir
          const chBlocks = await loadBlocksFromDir(chDir, blockNames, issues);
          for (const [name, block] of chBlocks) {
            allBlocks.set(name, { block, dir: chDir });
            if ("label" in block && block.label) {
              allLabels.add(block.label);
            }
          }
        } catch (e) {
          issues.push({
            level: "error",
            block: chRef.dir,
            message: `Chapter import error: ${e instanceof Error ? e.message : String(e)}`,
          });
        }
      }
    } catch (e) {
      issues.push({
        level: "error",
        block: basename(paperManifestPath, ".ts"),
        message: `Paper import error: ${e instanceof Error ? e.message : String(e)}`,
        file: basename(paperManifestPath),
      });
      return { valid: issues.every(i => i.level !== "error"), issues };
    }
  } else {
    // ── Flat mode: validate all .ts files as blocks (legacy) ──
    const blocks = await loadBlocksFromDir(objectsDir, null, issues);
    for (const [name, block] of blocks) {
      allBlocks.set(name, { block, dir: objectsDir });
      if ("label" in block && block.label) {
        allLabels.add(block.label);
      }
    }

    if (allBlocks.size === 0 && issues.length === 0) {
      issues.push({
        level: "warning",
        block: "(none)",
        message: `No content manifests found in ${objectsDir}`,
      });
      return { valid: true, issues };
    }
  }

  // Phase 2: Constraint rules
  for (const [name, { block, dir }] of allBlocks) {
    const ctx: ConstraintContext = {
      rootName: name,
      dir,
      allLabels,
      fileExists: (p: string) => existsSync(p),
    };

    for (const rule of CONSTRAINT_RULES) {
      if (!rule.appliesTo.includes(block.kind)) continue;
      const msg = rule.check(block as any, ctx);
      if (msg) {
        const isWarning = msg.startsWith("[warning]");
        issues.push({
          level: isWarning ? "warning" : "error",
          block: name,
          message: isWarning ? msg.slice(10) : msg,
        });
      }
    }
  }

  // Phase 3: AST validation (render → parse)
  for (const [name, { block, dir }] of allBlocks) {
    const mdPath = join(dir, `${name}.md`);
    const mdContent = existsSync(mdPath) ? readFileSync(mdPath, "utf-8") : "";

    try {
      const latex = renderBlock(block, mdContent);
      const astResult = validateLatexAst(latex);
      if (!astResult.valid) {
        for (const err of astResult.errors) {
          issues.push({
            level: "error",
            block: name,
            message: `LaTeX AST: ${err}`,
            file: `${name}.md`,
          });
        }
      }
    } catch (e) {
      issues.push({
        level: "error",
        block: name,
        message: `Render error: ${e instanceof Error ? e.message : String(e)}`,
      });
    }
  }

  const hasErrors = issues.some(i => i.level === "error");
  return { valid: !hasErrors, issues };
}

// ── CLI entry point ──────────────────────────────────────────────

if (import.meta.main) {
  const dir = resolve(process.argv[2] || join(import.meta.dir, "../objects"));
  console.log(`Validating content objects in: ${dir}\n`);

  const result = await validateObjects(dir);

  for (const issue of result.issues) {
    const icon = issue.level === "error" ? "✗" : issue.level === "warning" ? "⚠" : "ℹ";
    const file = issue.file ? ` (${issue.file})` : "";
    console.log(`  ${icon} [${issue.block}]${file}: ${issue.message}`);
  }

  console.log(`\n${result.valid ? "✓ Valid" : "✗ Invalid"} — ${result.issues.length} issue(s)`);
  process.exit(result.valid ? 0 : 1);
}
