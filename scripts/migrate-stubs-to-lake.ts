#!/usr/bin/env bun
/**
 * Migrate sibling `.lean` stubs (created by scripts/gen-lean-stubs.ts)
 * from chapter directories into the Lake project tree.
 *
 * For every chapter with generated stubs, this script:
 *   1. Consolidates the stubs into a single Lake-buildable file under
 *      content/<paper>/lean/QOU/...  (one file per chapter, named
 *      after the stub namespace).
 *   2. Updates each content manifest's `lean: { decl, file }` to point
 *      at the consolidated file.
 *   3. Deletes the redundant sibling `.lean` stubs.
 *   4. Adds the new module to the root `QOU.lean` import list.
 *
 * The consolidated file preserves the namespace each stub uses
 * (`QOU.<Chapter>` for most chapters). If a namespace collides with
 * an existing Lake module (e.g. `QOU.BraidKnot` already exists), the
 * stubs are grouped under `QOU.<Chapter>.Stubs` instead, and the file
 * is written to `lean/QOU/<Chapter>/Stubs.lean`.
 *
 * Usage:
 *   bun run scripts/migrate-stubs-to-lake.ts                  # migrate everything
 *   bun run scripts/migrate-stubs-to-lake.ts --chapter foo    # one chapter
 *   bun run scripts/migrate-stubs-to-lake.ts --dry-run        # preview
 *
 * @module scripts/migrate-stubs-to-lake
 */

import {
  readFileSync, writeFileSync, existsSync, unlinkSync,
  readdirSync, statSync, mkdirSync,
} from "fs";
import { join, dirname, basename, relative, resolve } from "path";

const REPO_ROOT = resolve(import.meta.dir, "..");
const PAPER = "quantum-observable-universe";
const PAPER_ROOT = join(REPO_ROOT, "content", PAPER);
const LEAN_ROOT = join(PAPER_ROOT, "lean");
const ROOT_MODULE = join(LEAN_ROOT, "QOU.lean");
const STUB_MARKER = "Generated sibling stub";

const args = process.argv.slice(2);
const dryRun = args.includes("--dry-run");
const chapterIdx = args.indexOf("--chapter");
const chapterFilter = chapterIdx >= 0 ? args[chapterIdx + 1] : undefined;

// ── Map chapter dir to target Lake path + namespace ──────────────

interface Target {
  /** Full namespace (e.g. "QOU.ParticleInteractions"). */
  ns: string;
  /** Lake-relative file path (e.g. "QOU/ParticleInteractions.lean"). */
  file: string;
  /** Absolute path to the Lake file. */
  abs: string;
  /** Root module import statement to add. */
  rootImport: string;
}

function targetFor(chapter: string): Target {
  // Map dash-case chapter to CamelCase module.
  const camel = chapter.split(/[-_]/)
    .map(w => w.charAt(0).toUpperCase() + w.slice(1))
    .join("");
  // Collision check against existing Lake modules.
  const direct = `QOU/${camel}.lean`;
  const directExists =
    existsSync(join(LEAN_ROOT, direct)) ||
    existsSync(join(LEAN_ROOT, "QOU", camel));
  if (directExists) {
    // Put into an existing or new subdirectory to avoid clobbering.
    const subDir = join(LEAN_ROOT, "QOU", camel);
    return {
      ns: `QOU.${camel}.Stubs`,
      file: `QOU/${camel}/Stubs.lean`,
      abs: join(subDir, "Stubs.lean"),
      rootImport: `import QOU.${camel}.Stubs`,
    };
  }
  return {
    ns: `QOU.${camel}`,
    file: direct,
    abs: join(LEAN_ROOT, direct),
    rootImport: `import QOU.${camel}`,
  };
}

// ── Harvest stubs from a chapter ─────────────────────────────────

interface Stub {
  siblingPath: string;   // absolute path to the sibling .lean file
  tsPath: string;        // absolute path to the .ts manifest
  slug: string;          // basename without extension
  originalDecl: string;  // fully-qualified decl name as the stub declared it
  bareName: string;      // bare decl name inside its namespace
  body: string;          // the declaration block (between `namespace` and `end`)
  leadingDoc: string;    // the doc comment preceding the decl
}

function extractStub(siblingPath: string): Stub | null {
  const text = readFileSync(siblingPath, "utf8");
  if (!text.includes(STUB_MARKER)) return null;
  const nsMatch = text.match(/namespace\s+([A-Za-z_][A-Za-z0-9_.']*)/);
  if (!nsMatch) return null;
  const ns = nsMatch[1];
  // Slice from after namespace to before `end <ns>`.
  const openIdx = text.indexOf(nsMatch[0]);
  const endIdx = text.lastIndexOf(`end ${ns}`);
  if (openIdx < 0 || endIdx < 0) return null;
  const inner = text.slice(openIdx + nsMatch[0].length, endIdx).trim();
  // Find the first decl keyword to split doc from body.
  const declRe = /(?:^|\n)(?:noncomputable\s+|@\[[^\]]+\]\s+)?(theorem|lemma|def|structure|class|instance|abbrev|axiom)\s+([A-Za-z_][A-Za-z0-9_.']*)/;
  const dm = declRe.exec(inner);
  if (!dm) return null;
  const bareName = dm[2];
  const startOfDecl = dm.index;
  const leadingDoc = inner.slice(0, startOfDecl).trim();
  const decl = inner.slice(startOfDecl).trim();

  const slug = basename(siblingPath, ".lean");
  return {
    siblingPath,
    tsPath: siblingPath.replace(/\.lean$/, ".ts"),
    slug,
    originalDecl: `${ns}.${bareName}`,
    bareName,
    body: decl,
    leadingDoc,
  };
}

function harvestChapter(chapter: string): Stub[] {
  const dir = join(PAPER_ROOT, chapter);
  if (!existsSync(dir)) return [];
  const stubs: Stub[] = [];
  for (const name of readdirSync(dir)) {
    if (!name.endsWith(".lean")) continue;
    const s = extractStub(join(dir, name));
    if (s) stubs.push(s);
  }
  return stubs;
}

// ── Build consolidated file ──────────────────────────────────────

function buildConsolidatedFile(
  chapter: string, target: Target, stubs: Stub[],
): string {
  const header = [
    `/-!`,
    `# ${target.ns} — Ch ${chapter} stubs (Lake-buildable)`,
    ``,
    `Consolidated Lake-tree home for the ${chapter} content-block`,
    `declarations stubbed by \`scripts/gen-lean-stubs.ts\`. Every`,
    `declaration below has a matching \`.ts\`/\`.md\` sibling under`,
    `\`content/${PAPER}/${chapter}/\` and records the type signature the`,
    `block claims; the proof body is a bridged placeholder until the`,
    `real formalisation lands.`,
    `-/`,
    ``,
    `import Mathlib.Tactic`,
    ``,
    `namespace ${target.ns}`,
    ``,
  ].join("\n");

  const bodies = stubs.map(s => {
    // Preserve the leading doc comment if any; strip any namespace fragment.
    const doc = s.leadingDoc ? s.leadingDoc + "\n" : "";
    return `${doc}${s.body}`;
  }).join("\n\n");

  return `${header}${bodies}\n\nend ${target.ns}\n`;
}

// ── Update a .ts manifest to point at the Lake file ──────────────

function patchManifest(tsPath: string, fullDecl: string, leanFile: string): boolean {
  if (!existsSync(tsPath)) return false;
  const txt = readFileSync(tsPath, "utf8");
  const leanBlock =
    `  lean: {\n    decl: "${fullDecl}",\n    file: "${leanFile}",\n    validation: "not_checked",\n  },`;
  let out = txt;
  if (/\n\s*lean\s*:\s*\{[\s\S]*?\},/.test(out)) {
    out = out.replace(/\n\s*lean\s*:\s*\{[\s\S]*?\},/, "\n" + leanBlock);
  } else {
    out = out.replace(/(\n\s*label:[^,\n]+,\n)/, `$1${leanBlock}\n`);
  }
  if (out === txt) return false;
  if (!dryRun) writeFileSync(tsPath, out);
  return true;
}

// ── Add a root-module import if absent ───────────────────────────

function ensureRootImport(importLine: string): boolean {
  const txt = readFileSync(ROOT_MODULE, "utf8");
  if (txt.includes(importLine)) return false;
  // Append near the other imports (end of the import block).
  const out = txt.replace(
    /(import [^\n]+\n)(?![\s\S]*^import )/m,
    `$1${importLine}\n`,
  );
  if (!dryRun) writeFileSync(ROOT_MODULE, out);
  return true;
}

// ── Main ─────────────────────────────────────────────────────────

const chapters = readdirSync(PAPER_ROOT).filter(name => {
  const p = join(PAPER_ROOT, name);
  return name !== "lean" && name !== "node_modules" && statSync(p).isDirectory();
});

let totalMigrated = 0;
let totalManifestsPatched = 0;
let totalDeleted = 0;

for (const chapter of chapters) {
  if (chapterFilter && chapter !== chapterFilter) continue;
  const stubs = harvestChapter(chapter);
  if (stubs.length === 0) continue;

  const target = targetFor(chapter);
  // Refine each stub's final decl name: the namespace might change
  // under a Stubs-suffix if there was a collision.
  const stubNamespace = stubs[0].originalDecl.split(".").slice(0, -1).join(".");
  const finalNs = stubNamespace === target.ns ? target.ns : target.ns;

  console.log(`\n═══ ${chapter} → ${target.file}  [${target.ns}] ═══`);
  console.log(`  ${stubs.length} stubs to migrate`);

  if (!dryRun) {
    const content = buildConsolidatedFile(chapter, target, stubs);
    mkdirSync(dirname(target.abs), { recursive: true });
    writeFileSync(target.abs, content);
  }
  totalMigrated += stubs.length;

  for (const s of stubs) {
    const newDecl = `${target.ns}.${s.bareName}`;
    if (patchManifest(s.tsPath, newDecl, target.file)) {
      totalManifestsPatched += 1;
    }
    if (!dryRun) { unlinkSync(s.siblingPath); totalDeleted += 1; }
  }

  if (ensureRootImport(target.rootImport)) {
    console.log(`  ✓ added ${target.rootImport} to root QOU.lean`);
  }
}

console.log(`\nMigrated ${totalMigrated} stubs across ${chapters.length} chapters (scanned).`);
console.log(`Patched ${totalManifestsPatched} manifests; deleted ${totalDeleted} sibling files.`);
if (dryRun) console.log("(dry run — no files written)");
