/**
 * Validation pipeline for content objects.
 *
 * Runs three levels of validation:
 *   1. Zod schema validation (shape + types)
 *   2. Constraint rules (file existence, cross-refs, lean requirements)
 *   3. AST validation (rendered LaTeX parses cleanly)
 *
 * Usage:
 *   bun run pipeline/validate.ts [objects-dir]
 *
 * @module content/pipeline/validate
 */

import { readdirSync, readFileSync, existsSync } from "fs";
import { join, basename, extname } from "path";
import {
  BlockSchema,
  CONSTRAINT_RULES,
  type ConstraintContext,
} from "../schema/constraints";
import type { Block, ValidationIssue, ValidationResult } from "../schema/types";
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

// ── Validation ───────────────────────────────────────────────────

/**
 * Validate all content objects in a directory.
 *
 * @param objectsDir - Directory containing .ts + .md + .lean files
 * @returns Validation result with issues
 */
export async function validateObjects(objectsDir: string): Promise<ValidationResult> {
  const issues: ValidationIssue[] = [];
  const manifests = discoverManifests(objectsDir);

  if (manifests.length === 0) {
    issues.push({
      level: "warning",
      block: "(none)",
      message: `No content manifests found in ${objectsDir}`,
    });
    return { valid: true, issues };
  }

  // Phase 1: Load all blocks and collect labels
  const blocks = new Map<string, Block>();
  const allLabels = new Set<string>();

  for (const name of manifests) {
    const tsPath = join(objectsDir, `${name}.ts`);
    try {
      const mod = await import(tsPath);
      const block: Block = mod.default;

      // Zod validation
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
      if ("label" in block && block.label) {
        allLabels.add(block.label);
      }
    } catch (e) {
      issues.push({
        level: "error",
        block: name,
        message: `Import error: ${e instanceof Error ? e.message : String(e)}`,
        file: `${name}.ts`,
      });
    }
  }

  // Phase 2: Constraint rules
  for (const [name, block] of blocks) {
    const ctx: ConstraintContext = {
      rootName: name,
      dir: objectsDir,
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
  for (const [name, block] of blocks) {
    const mdPath = join(objectsDir, `${name}.md`);
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
  const dir = process.argv[2] || join(import.meta.dir, "../objects");
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
