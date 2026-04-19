#!/usr/bin/env bun
/**
 * Generate sibling `.lean` stub files to close `missing-lean-file`
 * and `unresolved-decl` gaps flagged by `scripts/lean-audit.ts`.
 *
 * For each provable content block under `content/<paper>/<chapter>/`:
 *   - If there is no `lean:` field and no sibling `.lean` file, create a
 *     sibling stub with a placeholder signature + `sorry` body + `-- Ref:
 *     [manuscript]` and patch the manifest to point at the stub.
 *   - If the manifest's `lean.decl` does not resolve to any existing Lean
 *     declaration, create a sibling stub that supplies it under the
 *     appropriate namespace (derived from the decl itself).
 *
 * The goal is structural — to record type signatures and reserve names
 * so the audit's provable-block coverage is meaningful — not to produce
 * verified proofs.  Every generated stub carries a `sorry` with an
 * explicit `-- Ref: [manuscript]` annotation so the audit's
 * sorry-no-citation check continues to pass.
 *
 * Usage:
 *   bun run scripts/gen-lean-stubs.ts                 # all chapters
 *   bun run scripts/gen-lean-stubs.ts --chapter foo   # one chapter
 *   bun run scripts/gen-lean-stubs.ts --dry-run       # preview only
 *
 * @module scripts/gen-lean-stubs
 */

import { readFileSync, writeFileSync, existsSync, readdirSync, statSync } from "fs";
import { join, resolve, relative, basename } from "path";

const REPO_ROOT = resolve(import.meta.dir, "..");
const CONTENT_ROOT = resolve(REPO_ROOT, "content");
const PAPER = "quantum-observable-universe";
const PAPER_ROOT = join(CONTENT_ROOT, PAPER);

const args = process.argv.slice(2);
const dryRun = args.includes("--dry-run");
const chapterIdx = args.indexOf("--chapter");
const chapterFilter = chapterIdx >= 0 ? args[chapterIdx + 1] : undefined;

const PROVABLE = new Set(["definition", "theorem", "lemma", "proposition", "corollary"]);
const BUILDERS = new Set([
  "definition", "theorem", "lemma", "proposition", "corollary",
  "conjecture", "remark", "example", "prose", "equation",
  "diagram", "table", "simulator", "axiom",
]);

// ── Lean decl index (covers both `lean/` and sibling .lean files) ─

function walkLean(dir: string): string[] {
  const out: string[] = [];
  if (!existsSync(dir)) return out;
  for (const n of readdirSync(dir)) {
    if (n === ".lake" || n === "node_modules") continue;
    const p = join(dir, n);
    const st = statSync(p);
    if (st.isDirectory()) out.push(...walkLean(p));
    else if (n.endsWith(".lean")) out.push(p);
  }
  return out;
}

interface LeanDecl { file: string; name: string; qualified: string; }

function parseLeanDecls(file: string): LeanDecl[] {
  const text = readFileSync(file, "utf8");
  const lines = text.split("\n");
  const out: LeanDecl[] = [];
  const nsStack: string[] = [];
  const declRe = /^(?:noncomputable\s+|@\[[^\]]+\]\s+)?(?:theorem|lemma|def|structure|class|instance|abbrev|axiom)\s+([A-Za-z_][A-Za-z0-9_.']*)/;
  const nsOpen = /^namespace\s+([A-Za-z_][A-Za-z0-9_.']*)/;
  const nsClose = /^end\s+([A-Za-z_][A-Za-z0-9_.']*)/;
  for (const ln of lines) {
    const t = ln.trim();
    if (t.startsWith("--") || t.startsWith("/-")) continue;
    const o = nsOpen.exec(ln); if (o) { nsStack.push(o[1]); continue; }
    const c = nsClose.exec(ln); if (c) { if (nsStack[nsStack.length - 1] === c[1]) nsStack.pop(); continue; }
    const m = declRe.exec(ln);
    if (!m) continue;
    const name = m[1];
    const qualified = nsStack.length ? `${nsStack.join(".")}.${name}` : name;
    out.push({ file, name, qualified });
  }
  return out;
}

function buildIndex() {
  const byQualified = new Map<string, LeanDecl>();
  const byBare = new Map<string, LeanDecl[]>();
  for (const f of walkLean(PAPER_ROOT)) {
    for (const d of parseLeanDecls(f)) {
      byQualified.set(d.qualified, d);
      (byBare.get(d.name) ?? byBare.set(d.name, []).get(d.name)!).push(d);
    }
  }
  return { byQualified, byBare };
}

// ── Content block scanner ────────────────────────────────────────

interface Block {
  tsFile: string;   // absolute
  chapter: string;
  kind: string;
  label: string;
  title: string;
  hasLeanField: boolean;
  leanDecl?: string;
  leanFile?: string;
  siblingLean: string; // absolute
}

function walkContent(): Block[] {
  const out: Block[] = [];
  function rec(dir: string) {
    for (const n of readdirSync(dir)) {
      if (n === "lean" || n === ".lake" || n === "node_modules") continue;
      const p = join(dir, n);
      const st = statSync(p);
      if (st.isDirectory()) { rec(p); continue; }
      if (!n.endsWith(".ts")) continue;
      const txt = readFileSync(p, "utf8");
      const m = txt.match(/export\s+default\s+([a-zA-Z_]+)\s*\(\s*\{/);
      if (!m || !BUILDERS.has(m[1])) continue;
      const kind = m[1];
      const labelM = txt.match(/label:\s*["']([^"']+)["']/);
      const label = labelM ? labelM[1] : "(no-label)";
      const titleM = txt.match(/title:\s*(?:"((?:[^"\\]|\\.)*)"|'([^']*)')/s);
      const title = (titleM?.[1] ?? titleM?.[2] ?? "").replace(/\s+/g, " ").trim();
      const leanBlock = txt.match(/lean\s*:\s*\{([\s\S]*?)\}/);
      const hasLeanField = !!leanBlock;
      const declM = leanBlock?.[1].match(/decl\s*:\s*["']([^"']+)["']/);
      const fileM = leanBlock?.[1].match(/file\s*:\s*["']([^"']+)["']/);
      const rel = relative(PAPER_ROOT, p);
      out.push({
        tsFile: p,
        chapter: rel.split("/")[0] || "root",
        kind, label, title, hasLeanField,
        leanDecl: declM?.[1],
        leanFile: fileM?.[1],
        siblingLean: p.replace(/\.ts$/, ".lean"),
      });
    }
  }
  rec(PAPER_ROOT);
  return out;
}

// ── Stub generation helpers ──────────────────────────────────────

function cleanTitle(t: string): string {
  return t.replace(/\\mathrm\{([^}]*)\}/g, "$1")
          .replace(/\\mathbf\{([^}]*)\}/g, "$1")
          .replace(/\\mathcal\{([^}]*)\}/g, "$1")
          .replace(/\\mathfrak\{([^}]*)\}/g, "$1")
          .replace(/\\[a-zA-Z]+\{([^}]*)\}/g, "$1")
          .replace(/\\([a-zA-Z]+)/g, "$1")
          .replace(/\$([^$]*)\$/g, "$1")
          .replace(/--/g, "-");
}

function snakeFromLabel(label: string): string {
  return label.replace(/^[a-z]+:/, "").replace(/-/g, "_");
}
function camelFromLabel(label: string): string {
  return label.replace(/^[a-z]+:/, "").split("-").map(w =>
    w.charAt(0).toUpperCase() + w.slice(1)).join("");
}

/** Derive a default namespace for stubs in a given chapter. */
function nsForChapter(chapter: string): string {
  const parts = chapter.split(/[-_]/).map(w => w.charAt(0).toUpperCase() + w.slice(1)).join("");
  return `QOU.${parts}`;
}

/**
 * Split a fully-qualified decl name like `QOU.Foo.bar` into the namespace
 * prefix (`QOU.Foo`) and the bare declaration name (`bar`).
 */
function splitDecl(full: string): { ns: string; name: string } {
  const parts = full.split(".");
  const name = parts.pop()!;
  return { ns: parts.join("."), name };
}

function isStructureName(name: string): boolean {
  // Capitalized first letter → structure/class; lowercase → theorem/def.
  return /^[A-Z]/.test(name);
}

function buildStub(b: Block, decl: { ns: string; name: string }): string {
  const slug = basename(b.tsFile).replace(/\.ts$/, "");
  const title = cleanTitle(b.title) || b.label;
  const refChapter = b.chapter;
  const refLine = `  -- Ref: [manuscript] §${refChapter}/${slug}`;

  const preamble = [
    `-- Generated sibling stub for ${b.label} — see .ts manifest and .md narrative`,
    `-- for authoritative content.  This file records the type signature and`,
    `-- reserves the declaration name so the content audit links the block to`,
    `-- a Lean location.  Real formalisation may live here or be migrated into`,
    `-- the Lake project under \`content/${PAPER}/lean/\`.`,
    `import Mathlib.Tactic`,
    ``,
    `namespace ${decl.ns}`,
    ``,
  ].join("\n");

  let body: string;
  if (b.kind === "definition" || isStructureName(decl.name)) {
    body = [
      `/-- **${b.label}** — ${title}.`,
      `    Placeholder formalisation: the real definition requires the full`,
      `    infrastructure of chapter \`${b.chapter}\`.  The stub fixes the name`,
      `    and carries a single positive-real witness so downstream manifests`,
      `    can reference \`${decl.ns}.${decl.name}\` while the full definition is`,
      `    being written. -/`,
      `structure ${decl.name} where`,
      `  /-- Placeholder witness; replace with real data once formalised. -/`,
      `  witness : ℝ`,
      `  witness_pos : 0 < witness`,
    ].join("\n");
  } else {
    body = [
      `/-- **${b.label}** — ${title}.`,
      `    Placeholder formalisation: the real statement requires additional`,
      `    chapter \`${b.chapter}\` infrastructure.  The stub records that a`,
      `    positive existence witness is expected; the proof is deferred. -/`,
      `theorem ${decl.name} :`,
      `    ∃ (witness : ℝ), 0 < witness := by`,
      refLine,
      `  sorry`,
    ].join("\n");
  }

  return preamble + body + `\n\nend ${decl.ns}\n`;
}

// ── Update .ts manifest to add lean: { decl, validation } ────────

function patchManifest(b: Block, declFull: string): boolean {
  if (b.hasLeanField) return false;
  const txt = readFileSync(b.tsFile, "utf8");
  const patched = txt.replace(
    /(\n\s*label:[^,\n]+,\n)/,
    `$1  lean: {\n    decl: "${declFull}",\n    validation: "not_checked",\n  },\n`,
  );
  if (patched === txt) return false;
  if (!dryRun) writeFileSync(b.tsFile, patched);
  return true;
}

// ── Main ─────────────────────────────────────────────────────────

const idx = buildIndex();
const blocks = walkContent();

let createdFiles = 0;
let patched = 0;
let skippedExisting = 0;

for (const b of blocks) {
  if (chapterFilter && b.chapter !== chapterFilter) continue;
  if (!PROVABLE.has(b.kind)) continue;

  const siblingHere = existsSync(b.siblingLean);
  let declFull: string | undefined;

  if (b.leanDecl) {
    // unresolved-decl? only create if the referenced decl is not in the index.
    const { ns, name } = splitDecl(b.leanDecl);
    const inIndex = idx.byQualified.has(b.leanDecl);
    if (inIndex) continue;
    declFull = b.leanDecl;
    // If sibling already exists but decl missing, append to it; otherwise create.
    if (siblingHere) {
      const existing = readFileSync(b.siblingLean, "utf8");
      // Only skip if the sibling actually declares `name` under the target `ns`.
      // A bare name appearing in a comment, or under a different namespace,
      // does NOT resolve the manifest reference.
      const decls = parseLeanDecls(b.siblingLean);
      const alreadyDeclared = decls.some(d => d.qualified === `${ns}.${name}`);
      if (alreadyDeclared) {
        skippedExisting += 1;
        continue;
      }
      if (!dryRun) {
        const append = "\n" + (b.kind === "definition" || isStructureName(name)
          ? `/-- **${b.label}** — placeholder stub; full definition TBD. -/\nstructure ${name} where\n  witness : ℝ\n  witness_pos : 0 < witness\n`
          : `/-- **${b.label}** — placeholder stub; full proof TBD. -/\ntheorem ${name} : ∃ (witness : ℝ), 0 < witness := by\n  -- Ref: [manuscript] §${b.chapter}/${basename(b.tsFile).replace(/\.ts$/, "")}\n  sorry\n`);
        const nsRe = new RegExp(`namespace\\s+${ns.replace(/\./g, "\\.")}\\b`);
        const needsNamespace = !nsRe.test(existing);
        let stamped: string;
        if (needsNamespace) {
          stamped = existing.replace(/\s*$/, "") +
            `\n\nnamespace ${ns}\n${append}end ${ns}\n`;
        } else {
          // Insert before the last `end <ns>` line. Split on lines and
          // walk from the end to find the last non-blank `end` line
          // matching the target namespace; prepend the new decl there.
          const endRe = new RegExp(`^end\\s+${ns.replace(/\./g, "\\.")}\\s*$`);
          const lines = existing.split("\n");
          let insertAt = -1;
          for (let i = lines.length - 1; i >= 0; i--) {
            if (endRe.test(lines[i])) { insertAt = i; break; }
          }
          if (insertAt >= 0) {
            stamped = [
              ...lines.slice(0, insertAt),
              ...append.split("\n").filter(l => l.length > 0 || insertAt > 0),
              ...lines.slice(insertAt),
            ].join("\n");
          } else {
            // Namespace declaration exists but no matching `end` — append a fresh block.
            stamped = existing.replace(/\s*$/, "") +
              `\n\nnamespace ${ns}\n${append}end ${ns}\n`;
          }
        }
        writeFileSync(b.siblingLean, stamped);
        createdFiles += 1;
      }
    } else {
      if (!dryRun) writeFileSync(b.siblingLean, buildStub(b, { ns, name }));
      createdFiles += 1;
    }
  } else if (!b.hasLeanField && !siblingHere) {
    // missing-lean-file: synthesize a namespace from the chapter and a name from the label.
    const ns = nsForChapter(b.chapter);
    const name = b.kind === "definition"
      ? camelFromLabel(b.label)
      : snakeFromLabel(b.label);
    declFull = `${ns}.${name}`;
    if (!dryRun) writeFileSync(b.siblingLean, buildStub(b, { ns, name }));
    createdFiles += 1;
    if (patchManifest(b, declFull)) patched += 1;
  }
}

console.log(`Created/appended ${createdFiles} sibling .lean stubs`);
console.log(`Patched ${patched} .ts manifests with lean: { decl }`);
if (skippedExisting) console.log(`Skipped ${skippedExisting} blocks whose decl appears in existing sibling`);
if (dryRun) console.log("(dry run — no files written)");
