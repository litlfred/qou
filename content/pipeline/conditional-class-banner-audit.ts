#!/usr/bin/env bun
/**
 * §3b-cond conditional-class banner & hypothesis audit
 * (CLAUDE.md §3b-cond, items #2 and #3).
 *
 * For every block that the conjectural-propagation audit classifies
 * as "conditional-on-class" (i.e. a provable-kind block whose
 * uses[] cone touches only class-axiomatised conjectures), this
 * audit verifies:
 *
 *   (#2) **Lean class hypothesis** — the block's `.lean`
 *        declaration includes an `[Inst : C ...]` instance
 *        hypothesis whose class name matches one of the conjectures
 *        in the cone (per the conjecture's `class C` declaration).
 *
 *   (#3) **Narrative conditional banner** — the block's `.md`
 *        opens with a "Theorem (conditional on …)." (or
 *        Proposition/Lemma/Corollary) banner referencing at least
 *        one of the conjectures in the cone.
 *
 * Run from repo root:
 *
 *     bun run content/pipeline/conditional-class-banner-audit.ts
 *
 * Emits a witness JSON suitable for CI; non-zero exit on any
 * conditional-on-class block missing either component (when run
 * with `--strict`).
 */
import { readdir, readFile } from "node:fs/promises";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { leanPackageByName } from "../../folio-assistant/schemas/lean-packages.ts";

const SCRIPT_DIR = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(SCRIPT_DIR, "..", "..");
const ROOT = join(REPO_ROOT, "content/quantum-observable-universe");
const STRICT = process.argv.includes("--strict");
const WITNESS_OUT = process.argv.find((a) => a.endsWith(".json")) ??
  join(REPO_ROOT, "docs/audits/2026-05-09-conditional-class-banner.witness.json");

interface Block {
  label: string;
  kind: string;
  uses: string[];
  file: string;
}

const PROVABLE = new Set(["theorem", "proposition", "lemma", "corollary"]);

async function loadAll(): Promise<Map<string, Block>> {
  const blocks = new Map<string, Block>();
  const dirs = await readdir(ROOT, { withFileTypes: true });
  for (const d of dirs) {
    if (!d.isDirectory()) continue;
    const dirPath = join(ROOT, d.name);
    let files: string[];
    try { files = await readdir(dirPath); } catch { continue; }
    for (const f of files) {
      if (!f.endsWith(".ts")) continue;
      const path = join(dirPath, f);
      const text = await readFile(path, "utf8");
      const builderMatch = text.match(
        /export default (definition|theorem|proposition|lemma|corollary|conjecture|remark|prose|equation|diagram|example|simulator)\(/,
      );
      if (!builderMatch) continue;
      const kind = builderMatch[1];
      const labelMatch = text.match(/label:\s*"([^"]+)"/);
      if (!labelMatch) continue;
      const label = labelMatch[1];
      const usesIdx = text.indexOf("uses:");
      let uses: string[] = [];
      if (usesIdx >= 0) {
        const afterUses = text.slice(usesIdx);
        const arrStart = afterUses.indexOf("[");
        const arrEnd = afterUses.indexOf("]", arrStart);
        if (arrStart >= 0 && arrEnd > arrStart) {
          const arr = afterUses.slice(arrStart + 1, arrEnd);
          uses = [...arr.matchAll(/"([^"]+)"/g)].map((m) => m[1]);
        }
      }
      blocks.set(label, { label, kind, uses, file: path });
    }
  }
  return blocks;
}

/** Find the `.lean` file backing a block via lean.ref. */
async function leanFileFor(block: Block): Promise<string | null> {
  // Sibling first.
  const sibling = block.file.replace(/\.ts$/, ".lean");
  try { await readFile(sibling, "utf8"); return sibling; } catch {}
  // Then lean.ref.
  try {
    const tsText = await readFile(block.file, "utf8");
    const refMatch = tsText.match(/ref:\s*"([^:"]+):([^"]+)"/);
    if (!refMatch) return null;
    const pkg = leanPackageByName(refMatch[1]);
    if (!pkg) return null;
    const leanPath = join(REPO_ROOT, pkg.lakeRoot,
      refMatch[2].replace(/\./g, "/") + ".lean");
    await readFile(leanPath, "utf8");
    return leanPath;
  } catch { return null; }
}

/** Extract the class-name registered by a `class C` declaration. */
async function classNameOf(conjBlock: Block): Promise<string | null> {
  const leanPath = await leanFileFor(conjBlock);
  if (!leanPath) return null;
  const text = await readFile(leanPath, "utf8");
  const m = text.match(/^class\s+(\w+)/m);
  return m ? m[1] : null;
}

/** Transitive-conjecture cone, identical to conjectural-propagation-audit. */
function transitivelyTouchesConjecture(
  start: string,
  blocks: Map<string, Block>,
  cache: Map<string, Set<string>>,
): Set<string> {
  if (cache.has(start)) return cache.get(start)!;
  const visited = new Set<string>();
  const conjAncestors = new Set<string>();
  const stack = [start];
  while (stack.length) {
    const cur = stack.pop()!;
    if (visited.has(cur)) continue;
    visited.add(cur);
    const block = blocks.get(cur);
    if (!block) continue;
    for (const u of block.uses) {
      if (u.includes(":") && !["conj:", "def:", "thm:", "prop:", "lem:",
          "cor:", "rem:", "ex:", "sim:", "eq:"].some((p) => u.startsWith(p))) {
        continue;
      }
      if (u.startsWith("conj:")) conjAncestors.add(u);
      if (!visited.has(u)) stack.push(u);
    }
  }
  cache.set(start, conjAncestors);
  return conjAncestors;
}

const blocks = await loadAll();

// Determine the class-axiomatised set + their class names.
const classNames = new Map<string, string>();
await Promise.all(
  [...blocks].filter(([_, b]) => b.kind === "conjecture")
    .map(async ([label, b]) => {
      const name = await classNameOf(b);
      if (name) classNames.set(label, name);
    }),
);

// Walk every provable block and collect conditional-on-class entries.
const cache = new Map<string, Set<string>>();
type Finding = {
  label: string;
  kind: string;
  conj_cone: string[];
  has_lean_class_hypothesis: boolean;
  has_md_conditional_banner: boolean;
  lean_file: string | null;
  md_file: string;
};
const findings: Finding[] = [];

const BANNER_RE = /\b(Theorem|Proposition|Lemma|Corollary)\s*\(\s*conditional\s+on\b/i;

for (const [label, block] of blocks) {
  if (!PROVABLE.has(block.kind)) continue;
  const cone = transitivelyTouchesConjecture(label, blocks, cache);
  if (cone.size === 0) continue;
  const allAxiomatised = [...cone].every((c) => classNames.has(c));
  if (!allAxiomatised) continue; // not §3b-cond eligible — separate concern

  // Look up the Lean file and check for an `[Inst : C ...]` hypothesis
  // matching one of the conjectures' class names.
  const leanPath = await leanFileFor(block);
  let hasClass = false;
  if (leanPath) {
    const text = await readFile(leanPath, "utf8");
    for (const c of cone) {
      const cls = classNames.get(c);
      if (!cls) continue;
      // [Inst : ClassName ...] OR [ClassName ...] OR `(_ : ClassName ...)`
      const re = new RegExp(`\\[(?:[\\w_]+\\s*:\\s*)?${cls}\\b`);
      if (re.test(text)) { hasClass = true; break; }
    }
  }

  // Look up the md file and check for the conditional-banner.
  const mdPath = block.file.replace(/\.ts$/, ".md");
  let hasBanner = false;
  try {
    const md = await readFile(mdPath, "utf8");
    hasBanner = BANNER_RE.test(md);
  } catch {}

  findings.push({
    label,
    kind: block.kind,
    conj_cone: [...cone],
    has_lean_class_hypothesis: hasClass,
    has_md_conditional_banner: hasBanner,
    lean_file: leanPath ? leanPath.replace(REPO_ROOT + "/", "") : null,
    md_file: mdPath.replace(REPO_ROOT + "/", ""),
  });
}

findings.sort((a, b) => a.label.localeCompare(b.label));

const missingLean = findings.filter((f) => !f.has_lean_class_hypothesis);
const missingBanner = findings.filter((f) => !f.has_md_conditional_banner);
const fullyCompliant = findings.filter((f) =>
  f.has_lean_class_hypothesis && f.has_md_conditional_banner);

console.log(`§3b-cond conditional-class banner audit`);
console.log(`Total blocks scanned:                       ${blocks.size}`);
console.log(`Conditional-on-class candidates:            ${findings.length}`);
console.log(`  ✓ fully compliant (banner + class-hyp):   ${fullyCompliant.length}`);
console.log(`  ✗ missing Lean [Class] hypothesis:        ${missingLean.length}`);
console.log(`  ✗ missing .md conditional banner:         ${missingBanner.length}`);

if (missingLean.length > 0) {
  console.log(`\nMissing Lean [Class] hypothesis:`);
  for (const f of missingLean.slice(0, 10)) {
    console.log(`  ${f.kind.padEnd(11)} ${f.label}`);
    console.log(`    cone: {${f.conj_cone.join(", ")}}`);
    console.log(`    lean: ${f.lean_file ?? "(not found)"}`);
  }
  if (missingLean.length > 10) console.log(`  … (${missingLean.length - 10} more)`);
}

if (missingBanner.length > 0) {
  console.log(`\nMissing .md conditional banner:`);
  for (const f of missingBanner.slice(0, 10)) {
    console.log(`  ${f.kind.padEnd(11)} ${f.label}`);
    console.log(`    md: ${f.md_file}`);
  }
  if (missingBanner.length > 10) console.log(`  … (${missingBanner.length - 10} more)`);
}

await Bun.write(
  WITNESS_OUT,
  JSON.stringify({
    audit: "§3b-cond conditional-class banner (CLAUDE.md §3b-cond #2 + #3)",
    generated: new Date().toISOString(),
    total_blocks: blocks.size,
    conditional_on_class: findings.length,
    fully_compliant: fullyCompliant.length,
    missing_lean_class_hypothesis: missingLean.length,
    missing_md_conditional_banner: missingBanner.length,
    findings,
  }, null, 2),
);
console.log(`\nWitness: ${WITNESS_OUT.replace(REPO_ROOT + "/", "")}`);

if (STRICT && (missingLean.length + missingBanner.length) > 0) {
  console.error(`\nSTRICT mode: ${missingLean.length + missingBanner.length} compliance gaps`);
  process.exit(1);
}
