#!/usr/bin/env bun
/**
 * Validate bibliography data and cross-references.
 *
 * Checks:
 *   1. Schema validation — every entry passes CSLEntrySchema
 *   2. Uniqueness — no duplicate ids
 *   3. Completeness — required fields per type (author, year, DOI where expected)
 *   4. DOI format — syntactically valid DOIs
 *   5. Lean cross-refs — every `-- Ref: [key]` in .lean files resolves
 *   6. LaTeX cross-refs — every `\cite{key}` in .tex/.md files resolves
 *   7. Orphan detection — entries not cited anywhere
 *
 * Usage:
 *   bun run pipeline/validate-references.ts
 *   bun run pipeline/validate-references.ts --strict   (exit 1 on warnings)
 *   bun run pipeline/validate-references.ts --fix      (auto-fix what's possible)
 *
 * @module content/pipeline/validate-references
 */

import { readFileSync, existsSync, readdirSync } from "fs";
import { resolve, join } from "path";
import { references, referenceMap, CSLEntrySchema } from "../schema/references";
import type { Data as CSLData } from "csl-json";

const REPO_ROOT = resolve(import.meta.dir, "../..");
const args = process.argv.slice(2);
const strict = args.includes("--strict");

// ── Issue tracking ──────────────────────────────────────────────

interface Issue {
  level: "error" | "warning" | "info";
  ref?: string;
  message: string;
}

const issues: Issue[] = [];
function error(ref: string | undefined, msg: string) { issues.push({ level: "error", ref, message: msg }); }
function warn(ref: string | undefined, msg: string) { issues.push({ level: "warning", ref, message: msg }); }
function info(ref: string | undefined, msg: string) { issues.push({ level: "info", ref, message: msg }); }

// ── 1. Schema validation ────────────────────────────────────────

console.log("Validating bibliography schema...");
for (const entry of references) {
  const result = CSLEntrySchema.safeParse(entry);
  if (!result.success) {
    for (const issue of result.error.issues) {
      error(entry.id, `Schema: ${issue.path.join(".")}: ${issue.message}`);
    }
  }
}

// ── 2. Uniqueness ───────────────────────────────────────────────

console.log("Checking for duplicate ids...");
const seen = new Set<string>();
for (const entry of references) {
  if (seen.has(entry.id)) {
    error(entry.id, `Duplicate reference id: "${entry.id}"`);
  }
  seen.add(entry.id);
}

// ── 3. Completeness checks ──────────────────────────────────────

console.log("Checking required fields per type...");

const ARTICLE_TYPES = new Set(["article-journal", "article-magazine", "article-newspaper"]);

for (const entry of references) {
  // All entries should have a year
  if (!entry.issued) {
    warn(entry.id, "Missing issued date");
  }

  // Articles should have container-title
  if (ARTICLE_TYPES.has(entry.type) && !entry["container-title"]) {
    warn(entry.id, `${entry.type} missing container-title (journal name)`);
  }

  // Books should have publisher
  if (entry.type === "book" && !entry.publisher) {
    warn(entry.id, "Book missing publisher");
  }

  // Published articles should have DOI
  if (ARTICLE_TYPES.has(entry.type) && !entry.DOI) {
    // Only warn if it's a real journal (not arXiv preprint)
    const isPreprint = entry["container-title"]?.toLowerCase().includes("arxiv") ||
                       entry.note?.toLowerCase().includes("arxiv");
    if (!isPreprint) {
      info(entry.id, "Journal article without DOI");
    }
  }

  // Author should exist for almost everything
  if (!entry.author?.length && entry.type !== "dataset") {
    warn(entry.id, "No authors listed");
  }
}

// ── 4. DOI format validation ────────────────────────────────────

console.log("Validating DOI formats...");
const DOI_REGEX = /^10\.\d{4,}\/\S+$/;
for (const entry of references) {
  if (entry.DOI && !DOI_REGEX.test(entry.DOI)) {
    warn(entry.id, `Suspicious DOI format: "${entry.DOI}"`);
  }
}

// ── 5. Lean cross-reference check ───────────────────────────────

console.log("Cross-checking Lean -- Ref: citations...");
const REF_PATTERN = /--\s*Ref:\s*\[([^\]]+)\]/g;
const leanCitations = new Set<string>();

// Scan .lean files for -- Ref: [key] patterns
const leanDir = join(REPO_ROOT, "lean");
const contentDir = join(REPO_ROOT, "content");
const leanArchiveDir = join(REPO_ROOT, "content/quantum-observable-universe/lean");

function scanFilesRecursive(dir: string, ext: string): string[] {
  if (!existsSync(dir)) return [];
  const results: string[] = [];
  function walk(d: string) {
    for (const entry of readdirSync(d, { withFileTypes: true })) {
      const full = join(d, entry.name);
      if (entry.isDirectory()) {
        if (entry.name === "node_modules" || entry.name === ".lake" || entry.name === "build") continue;
        walk(full);
      } else if (entry.name.endsWith(ext)) {
        results.push(full);
      }
    }
  }
  walk(dir);
  return results;
}

const leanFiles = [
  ...scanFilesRecursive(leanDir, ".lean"),
  ...scanFilesRecursive(leanArchiveDir, ".lean"),
  ...scanFilesRecursive(contentDir, ".lean"),
];

const unresolvedLeanRefs = new Map<string, string[]>();
for (const file of leanFiles) {
  const content = readFileSync(file, "utf-8");
  let match;
  const pattern = new RegExp(REF_PATTERN.source, REF_PATTERN.flags);
  while ((match = pattern.exec(content)) !== null) {
    const key = match[1];
    leanCitations.add(key);
    // Skip cross-paper refs (paper-dir:label format) and manuscript self-refs
    if (!referenceMap.has(key) && key !== "manuscript" && !key.includes(":")) {
      if (!unresolvedLeanRefs.has(key)) unresolvedLeanRefs.set(key, []);
      unresolvedLeanRefs.get(key)!.push(file.replace(REPO_ROOT + "/", ""));
    }
  }
}

for (const [key, files] of unresolvedLeanRefs) {
  error(key, `Lean -- Ref: [${key}] not found in references. Used in: ${files.join(", ")}`);
}

// ── 6. LaTeX / Markdown citation check ──────────────────────────

console.log("Cross-checking LaTeX \\cite{} citations...");
const CITE_PATTERN = /\\cite(?:\[[^\]]*\])?\{([^}]+)\}/g;
const texFiles = [
  ...scanFilesRecursive(join(REPO_ROOT, "chapters"), ".tex"),
  ...scanFilesRecursive(contentDir, ".md"),
  join(REPO_ROOT, "main.tex"),
  join(REPO_ROOT, "blueprint/src/content.tex"),
].filter(existsSync);

const texCitations = new Set<string>();
for (const file of texFiles) {
  const content = readFileSync(file, "utf-8");
  let match;
  const pattern = new RegExp(CITE_PATTERN.source, CITE_PATTERN.flags);
  while ((match = pattern.exec(content)) !== null) {
    // \cite{a,b,c} → split on commas
    for (const key of match[1].split(",").map((k: string) => k.trim())) {
      texCitations.add(key);
      if (!referenceMap.has(key)) {
        warn(key, `\\cite{${key}} in ${file.replace(REPO_ROOT + "/", "")} not found in references`);
      }
    }
  }
}

// ── 7. Orphan detection ─────────────────────────────────────────

console.log("Checking for uncited references...");
const allCitations = new Set([...leanCitations, ...texCitations]);
for (const entry of references) {
  if (!allCitations.has(entry.id)) {
    info(entry.id, "Reference not cited in any .lean or .tex/.md file");
  }
}

// ── Report ──────────────────────────────────────────────────────

console.log("\n" + "=".repeat(60));
console.log(`Bibliography validation: ${references.length} references\n`);

const errors = issues.filter(i => i.level === "error");
const warnings = issues.filter(i => i.level === "warning");
const infos = issues.filter(i => i.level === "info");

for (const i of errors) {
  console.log(`  [ERROR]   ${i.ref ? `[${i.ref}] ` : ""}${i.message}`);
}
for (const i of warnings) {
  console.log(`  [WARN]    ${i.ref ? `[${i.ref}] ` : ""}${i.message}`);
}
for (const i of infos) {
  console.log(`  [INFO]    ${i.ref ? `[${i.ref}] ` : ""}${i.message}`);
}

console.log(`\n  ${errors.length} errors, ${warnings.length} warnings, ${infos.length} info`);
console.log(`  Lean citations found: ${leanCitations.size}`);
console.log(`  LaTeX citations found: ${texCitations.size}`);
console.log("=".repeat(60));

const exitCode = errors.length > 0 ? 1 : (strict && warnings.length > 0 ? 1 : 0);
process.exit(exitCode);

export { issues, type Issue };
