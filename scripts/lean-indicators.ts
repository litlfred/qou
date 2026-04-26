#!/usr/bin/env bun
/**
 * Lean indicators — content-addressable, hierarchical audit.
 *
 * Walks the content hierarchy `folio → paper → chapter → section → block`
 * and computes per-block indicators (sorry counts, axioms, trivial
 * placeholders, etc.) together with **input SHAs** so staleness is
 * detectable at every level:
 *
 *   - Each block records `inputSha` (git-blob hashes of `.ts`, `.lean`,
 *     `.md`) and a `rollupHash` = SHA-256 over `inputSha` + indicators.
 *   - Each section's `rollupHash` = SHA-256 over its blocks' rollupHashes
 *     (sorted, deterministic).
 *   - Each chapter's = SHA-256 over its sections'.
 *   - Each paper's = SHA-256 over its chapters'.
 *
 * If any input file changes, the rollup hash propagates upward and the
 * subtree is "stale" until the audit is re-run.
 *
 * This **replaces** the embedded "Current Snapshot" sections that used to
 * live in `.claude/skills/local/{proof-status-tracking,proof-triage,
 * lean-proof-review}.md`. Those drift; this is the source of truth.
 *
 * Usage:
 *   bun run scripts/lean-indicators.ts                  # full audit
 *   bun run scripts/lean-indicators.ts --paper qou      # one paper
 *   bun run scripts/lean-indicators.ts --json-only      # skip markdown
 *
 * Outputs:
 *   audit/lean-indicators.json   (machine-readable)
 *   audit/lean-indicators.md     (one table per section, per chapter,
 *                                  per paper; rollup hashes inline)
 *
 * Exit code: 0 always (this is a measurement, not a gate).
 *
 * @module scripts/lean-indicators
 */

import { readFileSync, existsSync, mkdirSync, writeFileSync } from "fs";
import { resolve, join, basename, relative, dirname } from "path";
import { fileURLToPath } from "url";
import { execSync } from "child_process";
import { createHash } from "crypto";

const SCRIPT_DIR = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(SCRIPT_DIR, "..");
const CONTENT_ROOT = resolve(REPO_ROOT, "content");
const FOLIO_PATH = resolve(CONTENT_ROOT, "folio.ts");
const AUDIT_DIR = resolve(REPO_ROOT, "audit");

// ── Types ────────────────────────────────────────────────────────

interface BlockIndicators {
  /** Active `sorry` occurrences (excluding comments / mentions). */
  sorryTotal: number;
  /** Active `sorry` without a `-- Ref:` citation within 3 preceding lines. */
  sorryUncited: number;
  /** `axiom` declarations. */
  axioms: number;
  /** `admit` occurrences. */
  admits: number;
  /** `True := by trivial` placeholders. */
  trivialPlaceholders: number;
  /** Lean code lines (non-comment, non-blank). null if no .lean file. */
  leanCodeLines: number | null;
  /** True iff a `.lean` sibling resolves on disk. */
  leanFileExists: boolean;
  /** Validation declared in the .ts manifest, if any. */
  manifestValidation: string | null;
  /** sorryFree flag declared in the .ts manifest, if any. */
  manifestSorryFree: boolean | null;
}

const ZERO_INDICATORS: BlockIndicators = {
  sorryTotal: 0,
  sorryUncited: 0,
  axioms: 0,
  admits: 0,
  trivialPlaceholders: 0,
  leanCodeLines: null,
  leanFileExists: false,
  manifestValidation: null,
  manifestSorryFree: null,
};

interface BlockRecord {
  paper: string;
  chapterDir: string;
  chapterTitle: string;
  sectionLabel: string | null;
  sectionTitle: string | null;
  blockRoot: string;
  label: string | null;
  kind: string | null;
  leanRef: string | null;
  files: {
    ts: { path: string; sha: string } | null;
    lean: { path: string; sha: string } | null;
    md: { path: string; sha: string } | null;
  };
  indicators: BlockIndicators;
  /** SHA-256 of `inputSha` + canonical-JSON indicators. */
  rollupHash: string;
}

interface SectionRollup {
  paper: string;
  chapterDir: string;
  label: string | null;
  title: string | null;
  blockCount: number;
  leanBlockCount: number;
  indicators: BlockIndicators;
  /** SHA-256 over sorted blockHashes — content-addressable. */
  rollupHash: string;
}

interface ChapterRollup {
  paper: string;
  dir: string;
  title: string;
  sectionCount: number;
  blockCount: number;
  leanBlockCount: number;
  indicators: BlockIndicators;
  rollupHash: string;
}

interface PaperRollup {
  dir: string;
  title: string;
  chapterCount: number;
  blockCount: number;
  leanBlockCount: number;
  indicators: BlockIndicators;
  rollupHash: string;
}

interface FolioReport {
  generatedAt: string;
  measuredCommit: string;
  papers: Array<{
    rollup: PaperRollup;
    chapters: Array<{
      rollup: ChapterRollup;
      sections: Array<{
        rollup: SectionRollup;
        blocks: BlockRecord[];
      }>;
    }>;
  }>;
  folio: {
    paperCount: number;
    blockCount: number;
    leanBlockCount: number;
    indicators: BlockIndicators;
    rollupHash: string;
  };
}

// ── Hashing / git helpers ────────────────────────────────────────

function gitBlobSha(filePath: string): string | null {
  if (!existsSync(filePath)) return null;
  try {
    return execSync(`git hash-object "${filePath}"`, {
      cwd: REPO_ROOT,
    })
      .toString()
      .trim();
  } catch {
    return null;
  }
}

function currentCommitSha(): string {
  try {
    return execSync("git rev-parse HEAD", { cwd: REPO_ROOT })
      .toString()
      .trim();
  } catch {
    return "unknown";
  }
}

/** Canonical-JSON SHA-256 (sorted keys). */
function sha256OfJson(obj: unknown): string {
  return createHash("sha256")
    .update(canonicalJson(obj))
    .digest("hex");
}

function canonicalJson(obj: unknown): string {
  if (obj === null || typeof obj !== "object") return JSON.stringify(obj);
  if (Array.isArray(obj)) return `[${obj.map(canonicalJson).join(",")}]`;
  const keys = Object.keys(obj as Record<string, unknown>).sort();
  const pairs = keys.map(
    (k) =>
      `${JSON.stringify(k)}:${canonicalJson((obj as Record<string, unknown>)[k])}`,
  );
  return `{${pairs.join(",")}}`;
}

/** Combine child rollup hashes into one parent hash. Order-independent
 *  (inputs are sorted before hashing) so the parent hash is a
 *  deterministic function of its children's content. */
function combineHashes(childHashes: string[]): string {
  const sorted = [...childHashes].sort();
  return createHash("sha256")
    .update(sorted.join("\n"))
    .digest("hex");
}

// ── Indicator extraction (pure, file-based) ──────────────────────

function isCommentLine(s: string): boolean {
  const t = s.trim();
  return (
    t.startsWith("--") ||
    t.startsWith("/-") ||
    t.startsWith("-/") ||
    t.startsWith("*") ||
    t.startsWith("/-!")
  );
}

function extractLeanIndicators(content: string): {
  sorryTotal: number;
  sorryUncited: number;
  axioms: number;
  admits: number;
  trivialPlaceholders: number;
  leanCodeLines: number;
} {
  const lines = content.split("\n");
  let sorryTotal = 0;
  let sorryUncited = 0;
  let axioms = 0;
  let admits = 0;
  let trivialPlaceholders = 0;
  let codeLines = 0;

  // Track if we're inside a /- ... -/ block comment
  let inBlock = false;

  for (let i = 0; i < lines.length; i++) {
    const raw = lines[i];
    const t = raw.trim();

    // Cheap block-comment tracking
    if (!inBlock && (t.startsWith("/-") && !t.includes("-/"))) {
      inBlock = true;
      continue;
    }
    if (inBlock) {
      if (t.includes("-/")) inBlock = false;
      continue;
    }

    if (t.length === 0) continue;
    if (!isCommentLine(raw)) codeLines++;

    // ── sorry ──
    if (
      /\bsorry\b/.test(raw) &&
      !isCommentLine(raw) &&
      !/sorry-free|sorryFree|sorry_free|no sorry|not sorry|without sorry|No sorry/i.test(
        raw,
      )
    ) {
      sorryTotal++;
      const ctxStart = Math.max(0, i - 3);
      const ctx = lines.slice(ctxStart, i + 1).join("\n");
      if (!/Ref:\s*\[[^\]]+\]/.test(ctx)) sorryUncited++;
    }

    // ── admit ──
    if (/\badmit\b/.test(raw) && !isCommentLine(raw)) admits++;

    // ── axiom ──
    if (/^\s*axiom\s+\w/.test(raw)) axioms++;

    // ── trivial placeholders ──
    if (/:\s*True\s*:=\s*by\s*trivial/.test(raw)) trivialPlaceholders++;
  }

  return {
    sorryTotal,
    sorryUncited,
    axioms,
    admits,
    trivialPlaceholders,
    leanCodeLines: codeLines,
  };
}

// ── Block resolution ─────────────────────────────────────────────

interface BlockManifestData {
  kind?: string;
  label?: string;
  lean?: { ref?: string; validation?: string; sorryFree?: boolean };
}

async function loadBlockManifest(
  tsPath: string,
): Promise<BlockManifestData | null> {
  if (!existsSync(tsPath)) return null;
  try {
    const mod = await import(tsPath);
    const obj = mod.default;
    if (!obj || typeof obj !== "object") return null;
    return obj as BlockManifestData;
  } catch {
    return null;
  }
}

/**
 * Resolve the `.lean` file for a block, using the same fallback the
 * pipeline uses: sibling `<root>.lean` first, then leanRef → file path
 * under the package's Lake root.
 *
 * For now we only check the sibling — package-resolution would require
 * loading `lean-packages.ts` and is not needed for correct hashing
 * (we hash whichever file is the sibling on disk).
 */
function resolveLeanSibling(blockTsPath: string): string | null {
  const sibling = blockTsPath.replace(/\.ts$/, ".lean");
  return existsSync(sibling) ? sibling : null;
}

function resolveMdSibling(blockTsPath: string): string | null {
  const sibling = blockTsPath.replace(/\.ts$/, ".md");
  return existsSync(sibling) ? sibling : null;
}

async function auditBlock(
  paper: string,
  chapterDir: string,
  chapterTitle: string,
  sectionLabel: string | null,
  sectionTitle: string | null,
  blockRoot: string,
  blockTsPath: string,
): Promise<BlockRecord> {
  const manifest = await loadBlockManifest(blockTsPath);
  const tsSha = gitBlobSha(blockTsPath);

  const leanPath = resolveLeanSibling(blockTsPath);
  const mdPath = resolveMdSibling(blockTsPath);

  const leanSha = leanPath ? gitBlobSha(leanPath) : null;
  const mdSha = mdPath ? gitBlobSha(mdPath) : null;

  let indicators: BlockIndicators = { ...ZERO_INDICATORS };
  if (leanPath) {
    const content = readFileSync(leanPath, "utf-8");
    const ext = extractLeanIndicators(content);
    indicators = {
      ...ext,
      leanFileExists: true,
      manifestValidation: manifest?.lean?.validation ?? null,
      manifestSorryFree: manifest?.lean?.sorryFree ?? null,
    };
  } else {
    indicators = {
      ...ZERO_INDICATORS,
      leanFileExists: false,
      manifestValidation: manifest?.lean?.validation ?? null,
      manifestSorryFree: manifest?.lean?.sorryFree ?? null,
    };
  }

  const files: BlockRecord["files"] = {
    ts: tsSha ? { path: relative(REPO_ROOT, blockTsPath), sha: tsSha } : null,
    lean:
      leanPath && leanSha
        ? { path: relative(REPO_ROOT, leanPath), sha: leanSha }
        : null,
    md:
      mdPath && mdSha
        ? { path: relative(REPO_ROOT, mdPath), sha: mdSha }
        : null,
  };

  // Content-addressable rollup hash for this block
  const rollupHash = sha256OfJson({ files, indicators });

  return {
    paper,
    chapterDir,
    chapterTitle,
    sectionLabel,
    sectionTitle,
    blockRoot,
    label: manifest?.label ?? null,
    kind: manifest?.kind ?? null,
    leanRef: manifest?.lean?.ref ?? null,
    files,
    indicators,
    rollupHash,
  };
}

// ── Rollup arithmetic ────────────────────────────────────────────

function sumIndicators(records: { indicators: BlockIndicators }[]): BlockIndicators {
  const out: BlockIndicators = { ...ZERO_INDICATORS };
  let codeLinesAccum = 0;
  let codeLinesSeen = false;
  for (const r of records) {
    out.sorryTotal += r.indicators.sorryTotal;
    out.sorryUncited += r.indicators.sorryUncited;
    out.axioms += r.indicators.axioms;
    out.admits += r.indicators.admits;
    out.trivialPlaceholders += r.indicators.trivialPlaceholders;
    if (r.indicators.leanCodeLines !== null) {
      codeLinesAccum += r.indicators.leanCodeLines;
      codeLinesSeen = true;
    }
    if (r.indicators.leanFileExists) out.leanFileExists = true;
  }
  out.leanCodeLines = codeLinesSeen ? codeLinesAccum : null;
  // manifestValidation/sorryFree are not summable; null at rollup level.
  out.manifestValidation = null;
  out.manifestSorryFree = null;
  return out;
}

// ── Walking the hierarchy ────────────────────────────────────────

interface Section {
  title?: string;
  label?: string;
  blocks?: string[];
  subsections?: Section[];
}

interface Chapter {
  title: string;
  label?: string;
  sections: Section[];
}

interface PaperManifest {
  title: string;
  chapters: Array<{ dir: string }>;
}

interface Folio {
  papers: Array<{ dir: string; title: string }>;
}

/** Flatten subsections into a single list of leaf sections. Each leaf
 *  section retains the `(label, title, blocks)` triple needed for the
 *  rollup. */
function flattenSections(sections: Section[]): Section[] {
  const out: Section[] = [];
  for (const s of sections) {
    if (s.blocks && s.blocks.length > 0) {
      out.push(s);
    }
    if (s.subsections && s.subsections.length > 0) {
      out.push(...flattenSections(s.subsections as Section[]));
    }
  }
  return out;
}

async function auditChapter(
  paper: string,
  chapterDirAbs: string,
  chapterDirName: string,
): Promise<{
  rollup: ChapterRollup;
  sections: Array<{ rollup: SectionRollup; blocks: BlockRecord[] }>;
} | null> {
  const chPath = join(chapterDirAbs, `${chapterDirName}.ts`);
  if (!existsSync(chPath)) {
    return null;
  }

  let chapter: Chapter;
  try {
    const mod = await import(chPath);
    chapter = mod.default as Chapter;
    if (!chapter || !Array.isArray(chapter.sections)) return null;
  } catch (e) {
    console.warn(`Could not import chapter ${chapterDirName}: ${e}`);
    return null;
  }

  const leafSections = flattenSections(chapter.sections);
  const sectionResults: Array<{ rollup: SectionRollup; blocks: BlockRecord[] }> =
    [];

  for (const sec of leafSections) {
    const blocks: BlockRecord[] = [];
    for (const blockRoot of sec.blocks ?? []) {
      const blockTsPath = join(chapterDirAbs, `${blockRoot}.ts`);
      const rec = await auditBlock(
        paper,
        chapterDirName,
        chapter.title,
        sec.label ?? null,
        sec.title ?? null,
        blockRoot,
        blockTsPath,
      );
      blocks.push(rec);
    }

    const blockHashes = blocks.map((b) => b.rollupHash);
    const indicators = sumIndicators(blocks);
    const sectionRollup: SectionRollup = {
      paper,
      chapterDir: chapterDirName,
      label: sec.label ?? null,
      title: sec.title ?? null,
      blockCount: blocks.length,
      leanBlockCount: blocks.filter((b) => b.indicators.leanFileExists).length,
      indicators,
      rollupHash: combineHashes(blockHashes),
    };
    sectionResults.push({ rollup: sectionRollup, blocks });
  }

  // Chapter rollup
  const allBlocks = sectionResults.flatMap((s) => s.blocks);
  const indicators = sumIndicators(allBlocks);
  const chapterRollup: ChapterRollup = {
    paper,
    dir: chapterDirName,
    title: chapter.title,
    sectionCount: sectionResults.length,
    blockCount: allBlocks.length,
    leanBlockCount: allBlocks.filter((b) => b.indicators.leanFileExists).length,
    indicators,
    rollupHash: combineHashes(sectionResults.map((s) => s.rollup.rollupHash)),
  };

  return { rollup: chapterRollup, sections: sectionResults };
}

async function auditPaper(paperDir: string): Promise<FolioReport["papers"][0] | null> {
  const paperPath = join(CONTENT_ROOT, paperDir, `${paperDir}.ts`);
  if (!existsSync(paperPath)) return null;

  let paper: PaperManifest;
  try {
    const mod = await import(paperPath);
    paper = mod.default as PaperManifest;
    if (!paper || !Array.isArray(paper.chapters)) return null;
  } catch (e) {
    console.warn(`Could not import paper ${paperDir}: ${e}`);
    return null;
  }

  const chapters: Array<NonNullable<Awaited<ReturnType<typeof auditChapter>>>> =
    [];
  for (const chRef of paper.chapters) {
    const chDirAbs = join(CONTENT_ROOT, paperDir, chRef.dir);
    const result = await auditChapter(paperDir, chDirAbs, chRef.dir);
    if (result) chapters.push(result);
  }

  const allBlocks = chapters.flatMap((c) => c.sections.flatMap((s) => s.blocks));
  const indicators = sumIndicators(allBlocks);
  const paperRollup: PaperRollup = {
    dir: paperDir,
    title: paper.title,
    chapterCount: chapters.length,
    blockCount: allBlocks.length,
    leanBlockCount: allBlocks.filter((b) => b.indicators.leanFileExists).length,
    indicators,
    rollupHash: combineHashes(chapters.map((c) => c.rollup.rollupHash)),
  };

  return { rollup: paperRollup, chapters };
}

async function buildFolioReport(paperFilter: string | null): Promise<FolioReport> {
  let folio: Folio;
  try {
    const mod = await import(FOLIO_PATH);
    folio = mod.default as Folio;
  } catch (e) {
    throw new Error(`Could not load folio.ts: ${e}`);
  }

  const papers: FolioReport["papers"] = [];
  for (const p of folio.papers) {
    if (paperFilter && p.dir !== paperFilter) continue;
    const result = await auditPaper(p.dir);
    if (result) papers.push(result);
  }

  const allBlocks = papers.flatMap((p) =>
    p.chapters.flatMap((c) => c.sections.flatMap((s) => s.blocks)),
  );
  const indicators = sumIndicators(allBlocks);

  return {
    generatedAt: new Date().toISOString(),
    measuredCommit: currentCommitSha(),
    papers,
    folio: {
      paperCount: papers.length,
      blockCount: allBlocks.length,
      leanBlockCount: allBlocks.filter((b) => b.indicators.leanFileExists)
        .length,
      indicators,
      rollupHash: combineHashes(papers.map((p) => p.rollup.rollupHash)),
    },
  };
}

// ── Markdown rendering ───────────────────────────────────────────

function shortHash(h: string): string {
  return h.slice(0, 12);
}

function renderIndicatorRow(
  name: string,
  ind: BlockIndicators,
  blockCount: number,
  leanBlockCount: number,
  rollupHash: string,
): string {
  const codeLines = ind.leanCodeLines ?? 0;
  return `| ${name} | ${blockCount} | ${leanBlockCount} | ${ind.sorryTotal} | ${ind.sorryUncited} | ${ind.axioms} | ${ind.admits} | ${ind.trivialPlaceholders} | ${codeLines} | \`${shortHash(rollupHash)}\` |`;
}

const TABLE_HEADER = [
  "| Name | Blocks | Lean | Sorry | Uncited | Axiom | Admit | Trivial | LoC | Rollup |",
  "|---|---:|---:|---:|---:|---:|---:|---:|---:|---|",
].join("\n");

function renderMarkdown(report: FolioReport): string {
  const out: string[] = [];
  out.push("# Lean indicators (per block, with rollups)");
  out.push("");
  out.push(`_Generated: ${report.generatedAt} · commit \`${shortHash(report.measuredCommit)}\`_`);
  out.push("");
  out.push(
    "Each row's **Rollup** is a content-addressable SHA-256 over the row's inputs (block) or its children's rollups (section / chapter / paper / folio). Comparing rollups across runs tells you exactly which subtree changed.",
  );
  out.push("");
  out.push("Columns: **Sorry** = total active sorry; **Uncited** = sorry without a `-- Ref:` citation in the 3 preceding lines; **Axiom** = `axiom` declarations; **Admit** = `admit` occurrences; **Trivial** = `: True := by trivial` placeholders; **LoC** = Lean code lines (non-comment, non-blank).");
  out.push("");

  // ── Folio summary ─────────────────────────────────────────────
  out.push("## Folio rollup");
  out.push("");
  out.push(TABLE_HEADER);
  out.push(
    renderIndicatorRow(
      "**folio**",
      report.folio.indicators,
      report.folio.blockCount,
      report.folio.leanBlockCount,
      report.folio.rollupHash,
    ),
  );
  out.push("");

  // ── Per-paper rollup ──────────────────────────────────────────
  out.push("## Papers");
  out.push("");
  out.push(TABLE_HEADER);
  for (const p of report.papers) {
    out.push(
      renderIndicatorRow(
        `${p.rollup.title} (\`${p.rollup.dir}\`)`,
        p.rollup.indicators,
        p.rollup.blockCount,
        p.rollup.leanBlockCount,
        p.rollup.rollupHash,
      ),
    );
  }
  out.push("");

  // ── Per-paper, per-chapter, per-section ───────────────────────
  for (const p of report.papers) {
    out.push(`## Paper: ${p.rollup.title}`);
    out.push("");

    out.push("### Chapters");
    out.push("");
    out.push(TABLE_HEADER);
    for (const c of p.chapters) {
      out.push(
        renderIndicatorRow(
          `${c.rollup.title} (\`${c.rollup.dir}\`)`,
          c.rollup.indicators,
          c.rollup.blockCount,
          c.rollup.leanBlockCount,
          c.rollup.rollupHash,
        ),
      );
    }
    out.push("");

    out.push("### Sections");
    out.push("");
    for (const c of p.chapters) {
      if (c.sections.length === 0) continue;
      out.push(`#### ${c.rollup.title}`);
      out.push("");
      out.push(TABLE_HEADER);
      for (const s of c.sections) {
        const name = s.rollup.title
          ? s.rollup.title
          : s.rollup.label ?? "(unnamed)";
        out.push(
          renderIndicatorRow(
            name,
            s.rollup.indicators,
            s.rollup.blockCount,
            s.rollup.leanBlockCount,
            s.rollup.rollupHash,
          ),
        );
      }
      out.push("");
    }
  }

  // ── Top sorry sites for quick triage ──────────────────────────
  out.push("## Top blocks by uncited sorry");
  out.push("");
  out.push("| Block | Chapter | Sorry | Uncited | File |");
  out.push("|---|---|---:|---:|---|");
  const allBlocks = report.papers.flatMap((p) =>
    p.chapters.flatMap((c) => c.sections.flatMap((s) => s.blocks)),
  );
  const top = allBlocks
    .filter((b) => b.indicators.sorryUncited > 0)
    .sort((a, b) => b.indicators.sorryUncited - a.indicators.sorryUncited)
    .slice(0, 25);
  for (const b of top) {
    const file = b.files.lean?.path ?? b.files.ts?.path ?? "—";
    const name = b.label ?? b.blockRoot;
    out.push(
      `| ${name} | ${b.chapterTitle} | ${b.indicators.sorryTotal} | ${b.indicators.sorryUncited} | \`${file}\` |`,
    );
  }
  out.push("");

  out.push("---");
  out.push("");
  out.push(
    "**Staleness**: every row's `Rollup` is the SHA-256 over its inputs and (for non-leaves) its children's rollups. If you commit this report and the rollup at any level changes on the next run, that subtree is stale. Per-block input SHAs are recorded in `audit/lean-indicators.json` (`files.{ts,lean,md}.sha`).",
  );
  out.push("");
  return out.join("\n");
}

// ── Main ─────────────────────────────────────────────────────────

async function main() {
  const args = process.argv.slice(2);
  let paperFilter: string | null = null;
  let jsonOnly = false;
  for (let i = 0; i < args.length; i++) {
    if (args[i] === "--paper" && args[i + 1]) {
      paperFilter = args[i + 1];
      i++;
    } else if (args[i] === "--json-only") {
      jsonOnly = true;
    }
  }

  const report = await buildFolioReport(paperFilter);

  if (!existsSync(AUDIT_DIR)) mkdirSync(AUDIT_DIR, { recursive: true });

  const jsonPath = join(AUDIT_DIR, "lean-indicators.json");
  writeFileSync(jsonPath, JSON.stringify(report, null, 2) + "\n", "utf-8");

  if (!jsonOnly) {
    const mdPath = join(AUDIT_DIR, "lean-indicators.md");
    writeFileSync(mdPath, renderMarkdown(report), "utf-8");
  }

  // Console summary
  const ind = report.folio.indicators;
  console.log(
    `[lean-indicators] ${report.folio.blockCount} blocks (${report.folio.leanBlockCount} with .lean) · ` +
      `sorry ${ind.sorryTotal} (uncited ${ind.sorryUncited}) · axioms ${ind.axioms} · ` +
      `admits ${ind.admits} · trivials ${ind.trivialPlaceholders} · ` +
      `folio rollup ${shortHash(report.folio.rollupHash)}`,
  );
  console.log(`[lean-indicators] wrote ${relative(REPO_ROOT, jsonPath)}`);
  if (!jsonOnly) {
    console.log(
      `[lean-indicators] wrote ${relative(REPO_ROOT, join(AUDIT_DIR, "lean-indicators.md"))}`,
    );
  }
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
