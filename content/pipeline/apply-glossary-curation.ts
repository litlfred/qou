/**
 * Glossary curation applier (Phase C — apply step).
 *
 * Reads `glossary-curation.json` (decisions made via the curator web
 * UI) and inserts `defines: ["<slug>"]` into each chosen block's `.ts`
 * file. Idempotent: if a slug is already present in the target's
 * `defines[]`, it is skipped. If the file already has a `defines: [...]`
 * array, the new slug is appended.
 *
 * Curation file format:
 *
 *   {
 *     "decisions": [
 *       { "slug": "rigid-monoidal-category",
 *         "ownerBlock": "rem:glossary-rigid-monoidal-category",
 *         "tsPath": "/abs/path/to/block.ts" },
 *       ...
 *     ]
 *   }
 *
 * Run modes:
 *
 *   bun run pipeline/apply-glossary-curation.ts <paper-dir>           # dry-run (default)
 *   bun run pipeline/apply-glossary-curation.ts <paper-dir> --write   # apply edits
 *
 * The script does **not** re-format the file beyond inserting the
 * single new field; downstream `bun run validate` checks the result.
 *
 * @module content/pipeline/apply-glossary-curation
 */
import { existsSync, readFileSync, writeFileSync } from "fs";
import { basename, join, resolve } from "path";

export interface CurationDecision {
  slug: string;
  ownerBlock: string;
  tsPath: string;
}

export interface CurationFile {
  decisions: CurationDecision[];
}

export interface ApplyResult {
  applied: { slug: string; tsPath: string }[];
  skipped: { slug: string; tsPath: string; reason: string }[];
}

// ── Insertion logic ─────────────────────────────────────────────

/**
 * Insert (or extend) a `defines: ["<slug>"]` field in a builder call
 * source. Returns `null` if the file already declares the slug or
 * if the builder call cannot be located.
 */
export function insertDefines(source: string, slug: string): string | null {
  // Already has this slug?
  const existsRe = new RegExp(
    `defines\\s*:\\s*\\[[^\\]]*['"\`]${slug.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}['"\`]`,
    "m",
  );
  if (existsRe.test(source)) return null;

  // Case 1: existing `defines: [ ... ]` array — append slug.
  const existingArrayRe = /defines\s*:\s*\[([^\]]*)\]/;
  const arrMatch = source.match(existingArrayRe);
  if (arrMatch) {
    const inside = arrMatch[1].trim();
    const sep = inside.length === 0 ? "" : ", ";
    const replacement = `defines: [${inside}${sep}"${slug}"]`;
    return source.replace(existingArrayRe, replacement);
  }

  // Case 2: insert before the closing `})`. Locate the LAST `})` —
  // matches the builder call closer for `default <builder>({ ... })`.
  // We insert the new line before the `}`, indented to match the
  // surrounding fields.
  const closeRe = /(\n\s*)\}\)\s*;?\s*\n?\s*$/;
  const closeMatch = source.match(closeRe);
  if (!closeMatch) return null;

  // Find a sibling field's indentation by looking at the line above
  // the closing brace. Default to two spaces.
  const before = source.slice(0, source.length - closeMatch[0].length);
  const lastFieldMatch = before.match(/\n([ \t]+)\S[^\n]*,\s*$/);
  const indent = lastFieldMatch ? lastFieldMatch[1] : "  ";

  // Ensure the previous field ends with a comma so our insertion is
  // syntactically valid. The Section captured already ends with `,`,
  // but the builder may end with a field that omits the trailing
  // comma. Handle both by injecting before the closing `})`.
  const insertion = `\n${indent}defines: ["${slug}"],`;
  return before + insertion + closeMatch[0];
}

// ── Apply ───────────────────────────────────────────────────────

export function applyCuration(
  curation: CurationFile,
  options: { write: boolean } = { write: false },
): ApplyResult {
  const result: ApplyResult = { applied: [], skipped: [] };

  // Group decisions by tsPath so we batch edits per file.
  const byPath = new Map<string, CurationDecision[]>();
  for (const d of curation.decisions) {
    const list = byPath.get(d.tsPath) ?? [];
    list.push(d);
    byPath.set(d.tsPath, list);
  }

  for (const [tsPath, decs] of byPath) {
    if (!existsSync(tsPath)) {
      for (const d of decs) {
        result.skipped.push({ slug: d.slug, tsPath, reason: "file not found" });
      }
      continue;
    }

    let source = readFileSync(tsPath, "utf-8");
    let mutated = false;

    for (const d of decs) {
      const next = insertDefines(source, d.slug);
      if (next === null) {
        result.skipped.push({ slug: d.slug, tsPath, reason: "already declared" });
        continue;
      }
      source = next;
      mutated = true;
      result.applied.push({ slug: d.slug, tsPath });
    }

    if (mutated && options.write) {
      writeFileSync(tsPath, source);
    }
  }

  return result;
}

// ── CLI ─────────────────────────────────────────────────────────

if (import.meta.main) {
  const args = process.argv.slice(2);
  const paperArg = args.find(a => !a.startsWith("--"));
  const write = args.includes("--write");
  if (!paperArg) {
    console.error("Usage: bun run pipeline/apply-glossary-curation.ts <paper-dir> [--write]");
    process.exit(2);
  }

  const paperDir = resolve(paperArg);
  const curationPath = join(paperDir, "glossary-curation.json");
  if (!existsSync(curationPath)) {
    console.error(`No curation file at ${curationPath}`);
    process.exit(2);
  }

  const curation = JSON.parse(readFileSync(curationPath, "utf-8")) as CurationFile;
  const result = applyCuration(curation, { write });

  const mode = write ? "applied" : "would apply";
  console.log(`[apply-glossary-curation] ${mode} ${result.applied.length} edit(s)`);
  for (const a of result.applied) {
    console.log(`  + ${a.slug}  →  ${basename(a.tsPath)}`);
  }
  if (result.skipped.length > 0) {
    console.log(`[apply-glossary-curation] skipped ${result.skipped.length}:`);
    for (const s of result.skipped) {
      console.log(`  - ${s.slug}  →  ${basename(s.tsPath)}  (${s.reason})`);
    }
  }
  if (!write && result.applied.length > 0) {
    console.log(`\nDry-run only. Re-run with --write to persist.`);
  }
}
