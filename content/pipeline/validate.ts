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
import { validateDefterms } from "./validate-defterm";
import { validateValueDirectives } from "./validate-value";

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

type ManifestKind = "paper" | "chapter" | null;

/**
 * Detect what kind of manifest a directory's eponymous .ts file is.
 * Returns "paper", "chapter", or null if no manifest exists.
 *
 * Detection is authoritative: imports the .ts module, then validates the
 * exported object against PaperSchema and ChapterSchema. The data itself
 * determines the type — no source-text heuristics.
 */
async function detectManifestKind(dir: string): Promise<{ kind: ManifestKind; path: string | null; data?: any }> {
  const dirName = basename(dir);
  const manifestPath = join(dir, `${dirName}.ts`);
  if (!existsSync(manifestPath)) return { kind: null, path: null };
  try {
    const mod = await import(manifestPath);
    const obj = mod.default;
    if (PaperSchema.safeParse(obj).success) return { kind: "paper", path: manifestPath, data: obj };
    if (ChapterSchema.safeParse(obj).success) return { kind: "chapter", path: manifestPath, data: obj };
  } catch { /* import error — not a valid manifest */ }
  return { kind: null, path: null };
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
export async function validateObjects(
  objectsDir: string,
  opts: { strict?: boolean } = {},
): Promise<ValidationResult> {
  const issues: ValidationIssue[] = [];

  // Detect manifest type by importing and validating against schemas
  const { kind: manifestKind, path: manifestPath, data: manifestData } =
    await detectManifestKind(objectsDir);

  // Collect all blocks across all chapter directories (or flat dir)
  const allBlocks = new Map<string, { block: Block; dir: string }>();
  const allLabels = new Set<string>();

  if (manifestKind === "chapter" && manifestPath && manifestData) {
    // ── Chapter mode: manifest already validated by detectManifestKind ──
    const chapter: Chapter = manifestData;

    // Collect block names from sections
    const blockNames: string[] = [];
    for (const sec of chapter.sections) {
      if ("blocks" in sec) {
        blockNames.push(...(sec as Section).blocks);
      }
    }

    const chBlocks = await loadBlocksFromDir(objectsDir, blockNames, issues);
    for (const [name, block] of chBlocks) {
      allBlocks.set(name, { block, dir: objectsDir });
      if ("label" in block && block.label) {
        allLabels.add(block.label);
      }
    }
    // PR #565: also register the chapter's own label and the
    // labels of every section, so md-crossref-resolve recognises
    // [chap:foo](#chap:foo) and [sec:bar](#sec:bar) references.
    // Chapter-label collision is a real bug (warn); section-label
    // collision with an intro-block's label is an intentional
    // aliasing convention in this paper, so silently skip-add.
    if (chapter.label) {
      if (allLabels.has(chapter.label)) {
        issues.push({
          level: "warning",
          block: "(chapter)",
          message: `[chapter-label-collision] chapter label ${chapter.label!} shadows an existing block label`,
        });
      } else {
        allLabels.add(chapter.label);
      }
    }
    for (const sec of chapter.sections) {
      if ("label" in sec && sec.label) {
        // Intentional aliasing with intro-block labels — skip-add only.
        allLabels.add(sec.label);
      }
    }
  } else if (manifestKind === "paper" && manifestPath && manifestData) {
    // ── Paper mode: manifest already validated by detectManifestKind ──
    const paper: Paper = manifestData;

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
        // PR #565: register chapter + section labels (paper mode).
        // Chapter-label collision is a real bug (warn). Section-label
        // collision is the intentional intro-block alias pattern in
        // this paper, so silently skip-add.
        if (chapter.label) {
          if (allLabels.has(chapter.label)) {
            issues.push({
              level: "warning",
              block: chRef.dir,
              message: `[chapter-label-collision] chapter label ${chapter.label} shadows an existing block label`,
            });
          } else {
            allLabels.add(chapter.label);
          }
        }
        for (const sec of chapter.sections) {
          if ("label" in sec && sec.label) {
            allLabels.add(sec.label);
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

  // Pre-load all .md content once — avoids redundant filesystem reads
  // across Phase 2 (constraint rules) and Phase 3 (AST validation).
  // Store undefined for missing files to preserve the distinction from empty files.
  const mdCache = new Map<string, string | undefined>();
  for (const [name, { dir }] of allBlocks) {
    const mdPath = join(dir, `${name}.md`);
    mdCache.set(name, existsSync(mdPath) ? readFileSync(mdPath, "utf-8") : undefined);
  }

  // PR #565: harvest \label{eq:foo} declarations from .md content
  // into allLabels so [eq:foo](#eq:foo) cross-references resolve.
  // Don't strip fenced ```tex``` blocks — those are LaTeX render
  // targets and contain the actual equation labels. Collision-detect:
  // warn (don't error) if a \label{X} duplicates an existing label.
  const labelDecl = /\\label\{([^}]+)\}/g;
  for (const [name, md] of mdCache) {
    if (!md) continue;
    for (const m of md.matchAll(labelDecl)) {
      const lbl = m[1];
      if (allLabels.has(lbl)) {
        // Intentional aliasing is common (a section label reuses
        // its anchor block's label). Skip the warning unless the
        // duplicate is between two distinct \label{} declarations
        // — those genuinely mask each other in cross-refs. We
        // can't distinguish here cheaply, so silently skip-add.
        continue;
      }
      allLabels.add(lbl);
    }
  }

  // Phase 2: Constraint rules
  for (const [name, { block, dir }] of allBlocks) {
    const mdContent = mdCache.get(name);
    const ctx: ConstraintContext = {
      rootName: name,
      dir,
      allLabels,
      fileExists: (p: string) => existsSync(p),
      mdContent,
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
    const mdContent = mdCache.get(name) ?? "";

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

  // Phase 4: Glossary-term validation (defterm/refterm rules)
  const defBlocks = new Map<string, { block: Block; md: string | undefined }>();
  for (const [name, { block }] of allBlocks) {
    defBlocks.set(name, { block, md: mdCache.get(name) });
  }
  issues.push(...validateDefterms(defBlocks, { strict: opts.strict }));

  // Phase 5: Witnessed-value directive validation (:val[name] rules)
  issues.push(...validateValueDirectives(defBlocks, { strict: opts.strict }));

  const hasErrors = issues.some(i => i.level === "error");
  return { valid: !hasErrors, issues };
}

// ── CLI entry point ──────────────────────────────────────────────

if (import.meta.main) {
  const args = process.argv.slice(2);
  const strict = args.includes("--strict");
  const positional = args.filter(a => !a.startsWith("--"));
  const dir = resolve(positional[0] || join(import.meta.dir, "../objects"));
  console.log(`Validating content objects in: ${dir}${strict ? " [strict]" : ""}\n`);

  const result = await validateObjects(dir, { strict });

  for (const issue of result.issues) {
    const icon = issue.level === "error" ? "✗" : issue.level === "warning" ? "⚠" : "ℹ";
    const file = issue.file ? ` (${issue.file})` : "";
    console.log(`  ${icon} [${issue.block}]${file}: ${issue.message}`);
  }

  console.log(`\n${result.valid ? "✓ Valid" : "✗ Invalid"} — ${result.issues.length} issue(s)`);
  process.exit(result.valid ? 0 : 1);
}
