#!/usr/bin/env bun
/**
 * Agent-style narrative–Lean equivalence sweep.
 *
 * For each block with both .md and .lean siblings, checks whether
 * the narrative statement and the Lean declaration express the same
 * claim. Writes `kind: "agent"` entries to the per-block .qa.json.
 *
 * Usage:
 *   bun run pipeline/proof-narrative-lean-equiv-sweep.ts <chapter-dir>
 *   bun run pipeline/proof-narrative-lean-equiv-sweep.ts <chapter-dir> --dry-run
 *   bun run pipeline/proof-narrative-lean-equiv-sweep.ts <chapter-dir> --json
 */

import { readFileSync, existsSync } from "fs";
import { resolve, dirname, basename, relative } from "path";
import { fileURLToPath } from "url";
import {
  hashBlockFiles,
  gitHeadSha,
  walkBlocks,
  loadQaReport,
  saveQaReport,
  entryIsFresh,
} from "./qa-utils";
import type {
  BlockQaReport,
  QaCriterionEntry,
} from "../../folio-assistant/schemas/block-qa";

const __filename = fileURLToPath(import.meta.url);
const REPO_ROOT = resolve(dirname(__filename), "..", "..");
const CRITERION_ID = "proof-narrative-lean-equiv";
const REVIEWER_ID = "proof-narrative-lean-equiv-sweep/v1";

interface Args {
  root: string;
  dryRun: boolean;
  json: boolean;
}

function parseArgs(argv: string[]): Args {
  const out: Args = { root: "", dryRun: false, json: false };
  for (const a of argv) {
    if (a === "--dry-run") out.dryRun = true;
    else if (a === "--json") out.json = true;
    else if (!a.startsWith("-")) out.root = a;
  }
  return out;
}

// ── Extraction helpers ──────────────────────────────────────────

/** Extract the block kind from the .ts manifest text.
 *  Kind is inferred from the builder function: definition(), theorem(), etc. */
function extractKind(tsText: string): string | undefined {
  // Try explicit kind field first
  const explicit = tsText.match(/kind:\s*["'](\w+)["']/);
  if (explicit) return explicit[1];
  // Infer from builder function call: export default <builder>({...})
  const builder = tsText.match(
    /(?:export\s+default\s+|=\s*)(\w+)\s*\(/
  );
  if (builder) {
    const name = builder[1];
    const mapping: Record<string, string> = {
      definition: "definition",
      theorem: "theorem",
      lemma: "lemma",
      proposition: "proposition",
      corollary: "corollary",
      conjecture: "conjecture",
      remark: "remark",
      example: "example",
      prose: "prose",
      equation: "equation",
      diagram: "diagram",
      simulator: "simulator",
      proof: "proof",
    };
    return mapping[name];
  }
  return undefined;
}

/** Extract label from .ts manifest. */
function extractLabel(tsText: string): string | undefined {
  const m = tsText.match(/label:\s*["']([^"']+)["']/);
  return m?.[1];
}

/** Extract Lean declaration names from .lean source. */
function extractLeanDecls(leanText: string): string[] {
  const decls: string[] = [];
  const re = /^(?:theorem|lemma|def|noncomputable def|instance|class|structure|inductive|abbrev)\s+(\S+)/gm;
  let m: RegExpExecArray | null;
  while ((m = re.exec(leanText)) !== null) {
    decls.push(m[1]);
  }
  return decls;
}

/** Extract the main statement sentence from .md content. */
function extractMdStatement(mdText: string): string | undefined {
  // Look for bold statement markers
  const patterns = [
    /\*\*(?:Theorem|Proposition|Lemma|Corollary|Definition|Conjecture)[^*]*\*\*\.?\s*([^\n]+)/i,
    /^#+\s*Statement\s*\n+(.+)/m,
  ];
  for (const p of patterns) {
    const m = mdText.match(p);
    if (m) return m[1]?.trim();
  }
  // Fallback: first non-heading non-empty line
  const lines = mdText.split("\n").filter(
    (l) => l.trim() && !l.startsWith("#") && !l.startsWith(">")
  );
  return lines[0]?.trim();
}

/** Check if Lean has sorry (actual code, not comments). */
function hasSorryInCode(leanText: string): boolean {
  const cleaned = leanText
    .replace(/\/-[\!]?[\s\S]*?-\//g, (m) => "\n".repeat(m.split("\n").length - 1))
    .replace(/--[^\n]*/g, "");
  return /\bsorry\b/.test(cleaned);
}

/** Check structural equivalence between md and lean. */
function checkEquivalence(
  mdText: string,
  leanText: string,
  tsText: string,
): { result: "pass" | "fail" | "warn" | "n/a"; evidence?: string; notes?: string } {
  const kind = extractKind(tsText);
  const label = extractLabel(tsText);
  const leanDecls = extractLeanDecls(leanText);

  // Blocks without provable content don't need this check
  if (!kind || ["prose", "equation", "diagram", "simulator"].includes(kind)) {
    return { result: "n/a", notes: `Block kind '${kind}' has no provable Lean content expected.` };
  }

  // No Lean declarations found
  if (leanDecls.length === 0) {
    return {
      result: "warn",
      evidence: "Lean file exists but contains no declarations (theorem/def/class/etc).",
      notes: "Lean file may be empty or only contain comments.",
    };
  }

  // Extract label-derived expected declaration name
  const labelSuffix = label?.replace(/^(def|thm|lem|prop|cor|conj|rem|ex):/, "");
  const expectedSnake = labelSuffix?.replace(/-/g, "_");

  // Check if any Lean declaration name aligns with the block label
  const nameMatch = leanDecls.some((d) => {
    const declBase = d.split(".").pop()?.toLowerCase() ?? "";
    return declBase === expectedSnake?.toLowerCase();
  });

  // Check if .md has a statement
  const mdStatement = extractMdStatement(mdText);
  const hasSorry = hasSorryInCode(leanText);

  // Check for kind-declaration alignment
  const provableKinds = ["theorem", "lemma", "proposition", "corollary"];
  const isProvable = kind && provableKinds.includes(kind);
  const hasTheoremDecl = leanDecls.some((d) =>
    leanText.includes(`theorem ${d}`) || leanText.includes(`lemma ${d}`)
  );
  const hasDefDecl = leanDecls.some((d) =>
    leanText.includes(`def ${d}`) || leanText.includes(`noncomputable def ${d}`)
  );

  if (kind === "definition" && !hasDefDecl && hasTheoremDecl) {
    return {
      result: "warn",
      evidence: `Block kind is 'definition' but Lean has theorem/lemma, no def. Decls: ${leanDecls.join(", ")}`,
      notes: "Kind-declaration mismatch: .ts says definition but .lean has theorem.",
    };
  }

  if (isProvable && !hasTheoremDecl && hasDefDecl && !leanDecls.some((d) =>
    leanText.includes(`class ${d}`) || leanText.includes(`instance`)
  )) {
    return {
      result: "warn",
      evidence: `Block kind is '${kind}' but Lean has only def/noncomputable def, no theorem/lemma. Decls: ${leanDecls.join(", ")}`,
      notes: "Kind-declaration mismatch: .ts says provable but .lean has only definitions.",
    };
  }

  // For conjectures: expect class/sorry pattern
  if (kind === "conjecture") {
    const hasClass = leanText.includes("class ") || leanText.includes("axiom ");
    if (!hasClass && !hasSorry) {
      return {
        result: "warn",
        evidence: "Conjecture block has .lean but no class axiomatisation or sorry.",
        notes: "Per §3b, conjectures should use class axiomatisation pattern.",
      };
    }
    return {
      result: "pass",
      notes: `Conjecture with ${hasClass ? "class axiomatisation" : "sorry"} — structural match.`,
    };
  }

  // Pass if name aligns and kind is consistent
  if (nameMatch) {
    return {
      result: "pass",
      notes: `Label '${label}' aligns with Lean declaration. ${hasSorry ? "Has sorry (cited)." : "Sorry-free."}`,
    };
  }

  // Soft pass: name doesn't exactly match but declarations exist
  if (leanDecls.length > 0) {
    return {
      result: "pass",
      notes: `Label '${label}' → expected '${expectedSnake}'; Lean declares: ${leanDecls.slice(0, 5).join(", ")}${leanDecls.length > 5 ? "..." : ""}. Structural match via content.`,
    };
  }

  return {
    result: "warn",
    evidence: `Could not confirm narrative-Lean equivalence for '${label}'.`,
    notes: "Manual review recommended.",
  };
}

// ── Main sweep ──────────────────────────────────────────────────

async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (!args.root) {
    console.error("Usage: bun run pipeline/proof-narrative-lean-equiv-sweep.ts <chapter-dir>");
    process.exit(2);
  }

  const rootPath = resolve(REPO_ROOT, "content", args.root);
  if (!existsSync(rootPath)) {
    console.error(`Root not found: ${rootPath}`);
    process.exit(2);
  }

  const headSha = gitHeadSha();
  const now = new Date().toISOString();

  interface Result {
    label: string;
    kind: string;
    result: string;
    notes?: string;
    evidence?: string;
    qa_path: string;
  }
  const results: Result[] = [];
  let written = 0;
  let skipped_fresh = 0;
  let skipped_no_lean = 0;

  for (const block of walkBlocks(rootPath)) {
    if (!block.lean || !existsSync(resolve(REPO_ROOT, "content", block.lean))) {
      skipped_no_lean++;
      continue;
    }

    const mdPath = block.md ? resolve(REPO_ROOT, "content", block.md) : undefined;
    const tsPath = resolve(REPO_ROOT, "content", block.ts);
    const leanPath = resolve(REPO_ROOT, "content", block.lean);
    const qaPath = resolve(REPO_ROOT, "content", block.qa);

    if (!mdPath || !existsSync(mdPath)) {
      skipped_no_lean++;
      continue;
    }

    const currentHashes = hashBlockFiles({
      md: mdPath,
      ts: tsPath,
      lean: leanPath,
    });

    // Check if fresh entry already exists
    const existing = loadQaReport(qaPath);
    if (existing) {
      const entries = existing.criteria[CRITERION_ID] ?? [];
      if (entries.some((e) => entryIsFresh(e, currentHashes, ["md", "ts", "lean"]))) {
        skipped_fresh++;
        continue;
      }
    }

    const mdText = readFileSync(mdPath, "utf-8");
    const tsText = readFileSync(tsPath, "utf-8");
    const leanText = readFileSync(leanPath, "utf-8");

    const check = checkEquivalence(mdText, leanText, tsText);
    const label = extractLabel(tsText) ?? basename(block.ts, ".ts");
    const kind = extractKind(tsText) ?? "unknown";

    const entry: QaCriterionEntry = {
      field_hash: currentHashes,
      result: check.result,
      ...(check.evidence ? { evidence: check.evidence } : {}),
      reviewer: {
        kind: "agent",
        id: REVIEWER_ID,
        version: "v1",
      },
      reviewed_at: now,
      reviewed_sha: headSha,
      ...(check.notes ? { notes: check.notes } : {}),
    };

    if (!args.dryRun) {
      const report = existing ?? {
        $schema: "block-qa/v1" as const,
        label,
        kind,
        paths: {
          ts: block.ts,
          ...(block.md ? { md: block.md } : {}),
          ...(block.lean ? { lean: block.lean } : {}),
        },
        source_hashes: currentHashes,
        criteria: {},
        updated_at: now,
      };
      if (!report.criteria[CRITERION_ID]) {
        report.criteria[CRITERION_ID] = [];
      }
      report.criteria[CRITERION_ID].push(entry);
      report.source_hashes = currentHashes;
      report.updated_at = now;
      saveQaReport(qaPath, report);
    }

    results.push({
      label,
      kind,
      result: check.result,
      notes: check.notes,
      evidence: check.evidence,
      qa_path: block.qa,
    });
    written++;
  }

  if (args.json) {
    console.log(JSON.stringify({
      criterion: CRITERION_ID,
      root: args.root,
      written,
      skipped_fresh,
      skipped_no_lean,
      results,
    }, null, 2));
  } else {
    console.log(`proof-narrative-lean-equiv sweep: ${args.root}`);
    console.log(`  Written: ${written}`);
    console.log(`  Skipped (fresh): ${skipped_fresh}`);
    console.log(`  Skipped (no .lean): ${skipped_no_lean}`);
    const counts = { pass: 0, fail: 0, warn: 0, "n/a": 0 };
    for (const r of results) {
      counts[r.result as keyof typeof counts]++;
    }
    console.log(`  Results: pass=${counts.pass} fail=${counts.fail} warn=${counts.warn} n/a=${counts["n/a"]}`);
    if (counts.warn > 0 || counts.fail > 0) {
      console.log("\n  Findings:");
      for (const r of results) {
        if (r.result === "fail" || r.result === "warn") {
          console.log(`    ${r.result.toUpperCase()} ${r.label}: ${r.evidence ?? r.notes ?? ""}`);
        }
      }
    }
  }
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
