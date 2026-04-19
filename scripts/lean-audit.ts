#!/usr/bin/env bun
/**
 * Deep Lean content block audit.
 *
 * Produces a chapter-by-chapter summary of Lean formalization status:
 *   - sorry inventory (with citation check)
 *   - trivial truth detection (True := by trivial)
 *   - axiom inventory
 *   - witness staleness (commit SHA comparison)
 *   - missing .lean files for blocks that require them
 *
 * Usage:
 *   bun run scripts/lean-audit.ts                 # full audit, console output
 *   bun run scripts/lean-audit.ts --json          # JSON output
 *   bun run scripts/lean-audit.ts --chapter ch5   # filter to one chapter
 *
 * @module scripts/lean-audit
 */

import { readFileSync, existsSync, readdirSync, statSync } from "fs";
import { resolve, basename, dirname, relative, join } from "path";
import { globSync } from "glob";
import { execSync } from "child_process";
import { isWitnessed, leanFileHash, isStale } from "./lean-witness";

const REPO_ROOT = resolve(import.meta.dir, "..");
const CONTENT_ROOT = resolve(REPO_ROOT, "content");

// ── Types ────────────────────────────────────────────────────────

interface SorryEntry {
  file: string;
  line: number;
  context: string;       // surrounding lines for context
  hasCitation: boolean;
  citation?: string;      // extracted citation text
}

interface TrivialEntry {
  file: string;
  line: number;
  statement: string;
}

interface AxiomEntry {
  file: string;
  line: number;
  name: string;
  hasCitation: boolean;
}

interface LeanFileStatus {
  file: string;           // relative to repo root
  lines: number;
  codeLines: number;      // non-comment, non-blank
  sorries: SorryEntry[];
  trivials: TrivialEntry[];
  axioms: AxiomEntry[];
  hash: string;
  witnessed: boolean;
  commitSha?: string;     // from witness file if it exists
  stale: boolean;         // hash mismatch with witness
}

/**
 * Gap discovered while comparing a content-block manifest (.ts/.md) against
 * the Lean code that should formalize it.
 */
interface BlockGap {
  /** Repo-relative path to the .ts manifest. */
  tsFile: string;
  /** Block label, e.g. "prop:foo". */
  label: string;
  /** Block kind from builder call (definition / theorem / proposition / ...). */
  kind: string;
  /** Gap classification. */
  gap:
    | "missing-lean-file"     // provable block has neither sibling .lean nor lean: field
    | "unresolved-decl"       // lean.decl declared in manifest but not found in any .lean file
    | "decl-in-wrong-file"    // decl exists, but not in the file the manifest references
    | "placeholder-statement" // referenced decl has trivial type (True/Unit) — narrative purports more
    | "sorry-no-citation";    // referenced decl proved with sorry and no -- Ref:
  /** Extra detail (decl name, file path, statement excerpt, etc.). */
  detail?: string;
}

interface ChapterAudit {
  chapter: string;
  siblingFiles: LeanFileStatus[];  // chapter-dir .lean files (legacy; usually empty)
  buildFiles: LeanFileStatus[];    // lean/ build system files
  /** Content-block-level gaps cross-referenced against Lean code. */
  blockGaps: BlockGap[];
  /** # provable content blocks (definition / theorem / lemma / proposition / corollary). */
  provableBlocks: number;
  /** # provable blocks with a working Lean reference (sibling or resolvable lean.decl). */
  leanLinked: number;
  totalSorries: number;
  uncitedSorries: number;
  trivialTruths: number;
  axiomCount: number;
  witnessedCount: number;
  staleCount: number;
  totalFiles: number;
}

interface AuditReport {
  generatedAt: string;
  currentCommitSha: string;
  paper: string;
  chapters: ChapterAudit[];
  summary: {
    totalLeanFiles: number;
    totalSorries: number;
    uncitedSorries: number;
    trivialTruths: number;
    axiomCount: number;
    witnessedCount: number;
    staleCount: number;
    pendingCount: number;
    /** Aggregate block-level gap counts (across all chapters). */
    provableBlocks: number;
    leanLinked: number;
    missingLeanFile: number;
    unresolvedDecl: number;
    declInWrongFile: number;
    placeholderStatement: number;
    sorryNoCitation: number;
  };
}

// ── Helpers ──────────────────────────────────────────────────────

function getCurrentCommitSha(): string {
  try {
    return execSync("git rev-parse HEAD", { cwd: REPO_ROOT })
      .toString()
      .trim();
  } catch {
    return "unknown";
  }
}

function getFileCommitSha(filePath: string): string {
  try {
    return execSync(`git log -1 --format=%H -- "${filePath}"`, {
      cwd: REPO_ROOT,
    })
      .toString()
      .trim();
  } catch {
    return "unknown";
  }
}

function countCodeLines(content: string): number {
  return content
    .split("\n")
    .filter((line) => {
      const trimmed = line.trim();
      return (
        trimmed.length > 0 &&
        !trimmed.startsWith("--") &&
        !trimmed.startsWith("/-") &&
        !trimmed.startsWith("-/")
      );
    }).length;
}

/**
 * Regex matching a Lean 4 declaration head. Captures the declaration's
 * bare name. Recognises the full set of declaration keywords used in
 * the project (theorem/lemma/def/inductive/structure/class/instance/
 * abbrev/axiom) and permits any mix of standard modifiers
 * (noncomputable / partial / private / protected / scoped) as well as
 * attribute prefixes like `@[simp]`.
 */
const DECL_HEAD_RE =
  /^(?:(?:noncomputable|partial|private|protected|scoped)\s+|@\[[^\]]+\]\s+)*(?:theorem|lemma|def|inductive|structure|class|instance|abbrev|axiom)\s+([A-Za-z_][A-Za-z0-9_.']*)/;

/**
 * Strip Lean comments from a single line, carrying the multi-line
 * `/- ... -/` block-comment state across calls via a mutable state
 * object.  Both balanced same-line blocks (`/- foo -/`) and trailing
 * `--` line comments are removed so that a caller testing
 * `/\bsorry\b/` against the result only sees non-comment code.
 */
function stripLeanComments(
  line: string,
  state: { inBlock: boolean },
): string {
  let out = "";
  let i = 0;
  while (i < line.length) {
    if (state.inBlock) {
      const close = line.indexOf("-/", i);
      if (close < 0) { i = line.length; break; }
      state.inBlock = false;
      i = close + 2;
    } else {
      const open = line.indexOf("/-", i);
      const lineComment = line.indexOf("--", i);
      // Whichever marker comes first wins.
      if (lineComment >= 0 && (open < 0 || lineComment < open)) {
        out += line.slice(i, lineComment);
        return out; // rest of line is a trailing `--` comment
      }
      if (open < 0) { out += line.slice(i); break; }
      out += line.slice(i, open);
      state.inBlock = true;
      i = open + 2;
    }
  }
  return out;
}

function extractSorries(filePath: string, content: string): SorryEntry[] {
  const lines = content.split("\n");
  const entries: SorryEntry[] = [];

  const state = { inBlock: false };
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const stripped = stripLeanComments(line, state);

    // Match sorry as a term in *code* (comments have been stripped above).
    if (
      /\bsorry\b/.test(stripped) &&
      !/sorry-free|sorryFree|sorry_free|not sorry|no sorry|without sorry|No sorry|Proved.*not sorry/i.test(
        line
      )
    ) {

      // Look for citation within the enclosing declaration + its docstring:
      // scan backwards until the declaration head (theorem/lemma/def/...),
      // then continue past any leading `-- Ref:` / `--` / `/-- ... -/` lines
      // that form the docstring, bounded by 30 lines for sanity.
      const declRe = DECL_HEAD_RE;
      let start = i;
      for (let k = i - 1; k >= Math.max(0, i - 30); k--) {
        start = k;
        if (declRe.test(lines[k])) break;
      }
      // Extend further up through any preceding `--` comment lines and
      // docstring closers (`-/`), so `-- Ref:` above the declaration counts.
      while (start > 0 && start > i - 30) {
        const prev = lines[start - 1].trim();
        if (prev.startsWith("--") || prev.endsWith("-/") || prev.startsWith("/-")) {
          start -= 1;
        } else break;
      }
      const context = lines.slice(start, i + 1).join("\n");
      // Primary: explicit Ref: [key] citation format
      const explicitCitation = context.match(
        /Ref:\s*\[([^\]]+)\]/i
      );
      // Secondary: other citation signals (weaker confidence)
      const implicitCitation = !explicitCitation
        ? context.match(/requires|blocked|manuscript|conjecture/i)
        : null;

      entries.push({
        file: relative(REPO_ROOT, filePath),
        line: i + 1,
        context: context.trim(),
        hasCitation: !!(explicitCitation || implicitCitation),
        citation: explicitCitation
          ? explicitCitation[0]
          : implicitCitation
            ? implicitCitation[0]
            : undefined,
      });
    }
  }
  return entries;
}

function extractTrivials(filePath: string, content: string): TrivialEntry[] {
  const lines = content.split("\n");
  const entries: TrivialEntry[] = [];

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    if (/True\s*:=\s*by\s*trivial/.test(line)) {
      entries.push({
        file: relative(REPO_ROOT, filePath),
        line: i + 1,
        statement: line.trim(),
      });
    }
  }
  return entries;
}

function extractAxioms(filePath: string, content: string): AxiomEntry[] {
  const lines = content.split("\n");
  const entries: AxiomEntry[] = [];

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    if (/^axiom\s+\w|^\s+axiom\s+\w/.test(line)) {
      const nameMatch = line.match(/axiom\s+(\w+)/);
      const name = nameMatch ? nameMatch[1] : "unknown";

      // Check for citation in nearby lines
      const contextLines = [
        i >= 2 ? lines[i - 2] : "",
        i >= 1 ? lines[i - 1] : "",
        line,
        i + 1 < lines.length ? lines[i + 1] : "",
      ];
      const context = contextLines.join("\n");
      const hasCitation =
        /Ref:|citation|doi|https?:|manuscript/i.test(context);

      entries.push({
        file: relative(REPO_ROOT, filePath),
        line: i + 1,
        name,
        hasCitation,
      });
    }
  }
  return entries;
}

function auditLeanFile(filePath: string): LeanFileStatus {
  const content = readFileSync(filePath, "utf-8");
  const witnessResult = isWitnessed(filePath);

  // Use shared isStale() for consistent staleness detection
  const staleResult = isStale(filePath);
  const stale = staleResult.stale;
  const witnessCommitSha = staleResult.witnessCommitSha;

  return {
    file: relative(REPO_ROOT, filePath),
    lines: content.split("\n").length,
    codeLines: countCodeLines(content),
    sorries: extractSorries(filePath, content),
    trivials: extractTrivials(filePath, content),
    axioms: extractAxioms(filePath, content),
    hash: witnessResult.hash,
    witnessed: witnessResult.witnessed,
    commitSha: witnessCommitSha,
    stale,
  };
}

// ── Lean declaration index ───────────────────────────────────────

/** A declaration discovered in a .lean file. */
interface LeanDecl {
  /** Repo-relative path to the .lean file. */
  file: string;
  /** Bare declaration name (without enclosing namespace). */
  name: string;
  /** Fully-qualified name when the file uses `namespace ... end`. */
  qualifiedName: string;
  /** 1-based line number of the declaration head inside `file`. */
  line: number;
  /** Type signature text up to `:=` or end of declaration head. */
  signature: string;
  /** Whether the body uses `sorry`. */
  hasSorry: boolean;
  /** Whether the body is `:= by trivial` (placeholder). */
  isTrivial: boolean;
  /** Whether the *type* is a trivial proposition (True / Unit / PUnit). */
  trivialType: boolean;
}

/** Walk a directory recursively, returning all .lean files (skipping .lake). */
function walkLeanFiles(dir: string): string[] {
  const out: string[] = [];
  if (!existsSync(dir)) return out;
  for (const name of readdirSync(dir)) {
    if (name === ".lake" || name === "node_modules") continue;
    const p = join(dir, name);
    const st = statSync(p);
    if (st.isDirectory()) out.push(...walkLeanFiles(p));
    else if (name.endsWith(".lean")) out.push(p);
  }
  return out;
}

/**
 * Parse a Lean source file and extract all top-level declarations along
 * with their enclosing namespace stack. Heuristic — does not run Lean.
 */
function parseLeanDecls(filePath: string): LeanDecl[] {
  const text = readFileSync(filePath, "utf-8");
  const lines = text.split("\n");
  const out: LeanDecl[] = [];
  const nsStack: string[] = [];
  const nsOpen = /^namespace\s+([A-Za-z_][A-Za-z0-9_.']*)/;
  const nsClose = /^end\s+([A-Za-z_][A-Za-z0-9_.']*)/;
  const commentState = { inBlock: false };

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    // Strip comments to track block state and avoid matching decls that
    // live inside a /- ... -/ docstring.
    const stripped = stripLeanComments(line, commentState);
    if (!stripped.trim()) continue;
    const open = nsOpen.exec(stripped);
    if (open) { nsStack.push(open[1]); continue; }
    const close = nsClose.exec(stripped);
    if (close) {
      const top = nsStack[nsStack.length - 1];
      if (top === close[1]) nsStack.pop();
      continue;
    }
    const m = DECL_HEAD_RE.exec(stripped);
    if (!m) continue;
    const name = m[1];
    const qualifiedName = nsStack.length > 0 ? `${nsStack.join(".")}.${name}` : name;

    // Collect signature: everything from after the name up to `:=` or end of head.
    let head = line.slice(line.indexOf(name) + name.length);
    let j = i;
    while (!/(:=|\bwhere\b)/.test(head) && j + 1 < lines.length) {
      j += 1;
      head += "\n" + lines[j];
      if (j - i > 40) break; // sanity
    }
    const splitIdx = head.search(/:=|\bwhere\b/);
    const signature = (splitIdx >= 0 ? head.slice(0, splitIdx) : head).trim();
    const body = (splitIdx >= 0 ? head.slice(splitIdx) : "");
    const hasSorry = /\bsorry\b/.test(body);
    const isTrivial = /:=\s*by\s*trivial\b/.test(body);
    const trivialType = /:\s*(?:True|Unit|PUnit)\b/.test(signature);

    out.push({
      file: relative(REPO_ROOT, filePath),
      name,
      qualifiedName,
      line: i + 1,
      signature,
      hasSorry,
      isTrivial,
      trivialType,
    });
  }
  return out;
}

interface LeanIndex {
  byQualified: Map<string, LeanDecl>;
  byBare: Map<string, LeanDecl[]>;
}

function buildLeanIndex(paperPath: string): LeanIndex {
  // Index BOTH the Lake project (`lean/`) and sibling `.lean` files that
  // live next to content-block `.ts` manifests. Sibling files are the
  // convention used in chapters like information-theory and fluid-dynamics.
  const files = walkLeanFiles(paperPath);
  const byQualified = new Map<string, LeanDecl>();
  const byBare = new Map<string, LeanDecl[]>();
  for (const f of files) {
    for (const d of parseLeanDecls(f)) {
      byQualified.set(d.qualifiedName, d);
      const arr = byBare.get(d.name) ?? [];
      arr.push(d);
      byBare.set(d.name, arr);
    }
  }
  return { byQualified, byBare };
}

// ── Content block scanner ────────────────────────────────────────

const PROVABLE_KINDS = new Set([
  "definition", "theorem", "lemma", "proposition", "corollary",
]);
const BUILDER_NAMES = new Set([
  "definition", "theorem", "lemma", "proposition", "corollary",
  "conjecture", "remark", "example", "prose", "equation",
  "diagram", "table", "simulator", "axiom",
]);

interface BlockManifest {
  tsFile: string;        // repo-relative
  chapter: string;       // top-level chapter dir name
  kind: string;
  label: string;
  /** Whether the .ts contains a `lean: { ... }` field. */
  hasLeanField: boolean;
  /** Parsed lean.decl value if present. */
  leanDecl?: string;
  /** Parsed lean.file value if present. */
  leanFile?: string;
  /** Whether a sibling .lean file (same root name) exists. */
  siblingLeanExists: boolean;
}

function walkContentBlocks(paperPath: string): BlockManifest[] {
  const out: BlockManifest[] = [];
  function rec(dir: string) {
    if (!existsSync(dir)) return;
    for (const name of readdirSync(dir)) {
      if (name === "lean" || name === ".lake" || name === "node_modules") continue;
      const p = join(dir, name);
      const st = statSync(p);
      if (st.isDirectory()) { rec(p); continue; }
      if (!name.endsWith(".ts")) continue;
      const txt = readFileSync(p, "utf-8");
      const m = txt.match(/export\s+default\s+([a-zA-Z_]+)\s*\(\s*\{/);
      if (!m || !BUILDER_NAMES.has(m[1])) continue;
      const kind = m[1];
      const labelM = txt.match(/label:\s*["']([^"']+)["']/);
      const label = labelM ? labelM[1] : "(no-label)";
      const leanBlock = txt.match(/lean\s*:\s*\{([\s\S]*?)\}/);
      const hasLeanField = !!leanBlock;
      let leanDecl: string | undefined;
      let leanFile: string | undefined;
      if (leanBlock) {
        const declM = leanBlock[1].match(/decl\s*:\s*["']([^"']+)["']/);
        const fileM = leanBlock[1].match(/file\s*:\s*["']([^"']+)["']/);
        leanDecl = declM?.[1];
        leanFile = fileM?.[1];
      }
      const siblingLeanExists = existsSync(p.replace(/\.ts$/, ".lean"));
      const rel = relative(paperPath, p);
      const chapter = rel.split("/")[0] || "root";
      out.push({
        tsFile: relative(REPO_ROOT, p),
        chapter,
        kind,
        label,
        hasLeanField,
        leanDecl,
        leanFile,
        siblingLeanExists,
      });
    }
  }
  rec(paperPath);
  return out;
}

/**
 * Cross-reference a content block against the Lean index to detect gaps:
 * missing files, unresolved decls, decls in the wrong file, placeholder
 * statements (True/Unit), and uncited sorries on referenced decls.
 */
function classifyBlockGaps(blocks: BlockManifest[], idx: LeanIndex): BlockGap[] {
  const gaps: BlockGap[] = [];
  for (const b of blocks) {
    const isProvable = PROVABLE_KINDS.has(b.kind);
    const hasAnyLink = b.hasLeanField || b.siblingLeanExists;
    if (isProvable && !hasAnyLink) {
      gaps.push({ tsFile: b.tsFile, label: b.label, kind: b.kind, gap: "missing-lean-file" });
      continue;
    }
    if (!b.leanDecl) continue;

    const qualified = idx.byQualified.get(b.leanDecl);
    const bare = b.leanDecl.split(".").pop()!;
    const candidates = qualified ? [qualified] : (idx.byBare.get(bare) ?? []);
    if (candidates.length === 0) {
      gaps.push({
        tsFile: b.tsFile, label: b.label, kind: b.kind,
        gap: "unresolved-decl",
        detail: `decl "${b.leanDecl}" not found in any .lean file under lean/`,
      });
      continue;
    }

    const decl = qualified ?? candidates[0];
    if (b.leanFile) {
      const expected = b.leanFile.replace(/^content\//, "");
      const actual = decl.file.replace(/^content\//, "");
      if (!actual.endsWith(expected) && !actual.includes(expected)) {
        gaps.push({
          tsFile: b.tsFile, label: b.label, kind: b.kind,
          gap: "decl-in-wrong-file",
          detail: `manifest says ${b.leanFile}, found at ${decl.file}`,
        });
      }
    }
    if (decl.trivialType || decl.isTrivial) {
      gaps.push({
        tsFile: b.tsFile, label: b.label, kind: b.kind,
        gap: "placeholder-statement",
        detail: `decl ${decl.qualifiedName} @ ${decl.file}: ${decl.signature.slice(0, 80)}`,
      });
    }
    if (decl.hasSorry) {
      // Use the decl's recorded line number to look at a symmetric window:
      // 20 lines back covers the leading docstring / `-- Ref:` annotation,
      // 50 lines forward covers multi-line proof bodies.  This avoids the
      // fragile `indexOf(signature)` lookup which can fail for empty
      // signatures or collide when two files share a decl name.
      try {
        const txt = readFileSync(join(REPO_ROOT, decl.file), "utf-8");
        const fileLines = txt.split("\n");
        const startLine = Math.max(0, decl.line - 20 - 1);
        const endLine = Math.min(fileLines.length, decl.line + 50);
        const window = fileLines.slice(startLine, endLine).join("\n");
        if (!/Ref:\s*\[[^\]]+\]/i.test(window)) {
          gaps.push({
            tsFile: b.tsFile, label: b.label, kind: b.kind,
            gap: "sorry-no-citation",
            detail:
              `decl ${decl.qualifiedName} (@ ${decl.file}:${decl.line}) ` +
              `uses sorry with no -- Ref: in the surrounding window`,
          });
        }
      } catch { /* file read failure — ignore */ }
    }
  }
  return gaps;
}

// ── Chapter mapping ──────────────────────────────────────────────

function getChapterName(dir: string): string {
  // Extract chapter name from directory path
  const parts = dir.split("/");
  return parts[parts.length - 1] || dir;
}

// Map build-system lean files to chapters based on module path
function mapBuildFileToChapter(filePath: string): string {
  const rel = relative(CONTENT_ROOT, filePath);
  if (rel.includes("QOU/QuantumObservableUniverse")) return "ch1-quantum-observable-universe";
  if (rel.includes("QOU/Torsion")) return "ch3-lifting-of-quantum-torsion";
  if (rel.includes("QOU/Descartes/")) return "ch6-descartes-universe";
  if (rel.includes("QOU/PathIntegrals") || rel.includes("QOU/KnotTheory") || rel.includes("QOU/KnotRegistry"))
    return "ch4-path-integrals-and-braiding";
  if (rel.includes("QOU/BringsSurface")) return "ch5-brings-surface";
  if (rel.includes("QOU/DescartesUniverse")) return "ch6-descartes-universe";
  if (rel.includes("QOU/GaugeFieldFluidDynamics")) return "ch10-fluid-dynamics";
  if (rel.includes("QOU/InformationTheory")) return "ch9-information-theory";
  if (rel.includes("QOU/QGeometricLanglands")) return "ch11-q-geometric-langlands";
  if (rel.includes("QOU/Glossary")) return "ch8-glossary";
  if (rel.includes("QOU/HadronicMass") || rel.includes("QOU/AtomicMass") || rel.includes("QOU/MassDerivation"))
    return "ch7-observations";
  if (rel.includes("QOU/CODATAChain")) return "ch7-observations";
  if (rel.includes("QOU/RepresentationTheory")) return "ch2-quantum-geometry";
  if (rel.includes("QOU/Calculations") || rel.includes("QOU/MathConstants")) return "shared";
  return "core";
}

// ── Main audit ───────────────────────────────────────────────────

function runAudit(paperDir: string, chapterFilter?: string): AuditReport {
  const paperPath = resolve(CONTENT_ROOT, paperDir);
  const currentCommit = getCurrentCommitSha();

  // Build Lean-decl index + scan content blocks for cross-reference gaps.
  const leanIndex = buildLeanIndex(paperPath);
  const blocks = walkContentBlocks(paperPath);
  const allGaps = classifyBlockGaps(blocks, leanIndex);

  // Find all chapter directories
  const chapterDirs = globSync("ch*", {
    cwd: paperPath,
    absolute: true,
  }).filter((d) => {
    try {
      return existsSync(d);
    } catch {
      return false;
    }
  });

  // Find all lean build files
  const buildLeanFiles = globSync("lean/**/*.lean", {
    cwd: paperPath,
    absolute: true,
  }).filter((f) => !f.includes(".lake/"));

  // Group by chapter
  const chapterMap = new Map<string, ChapterAudit>();

  // Initialize chapters from directories
  for (const dir of chapterDirs) {
    const name = getChapterName(dir);
    if (chapterFilter && !name.includes(chapterFilter)) continue;

    const siblingLeanFiles = globSync("*.lean", {
      cwd: dir,
      absolute: true,
    });

    const siblingStatuses = siblingLeanFiles.map(auditLeanFile);

    chapterMap.set(name, {
      chapter: name,
      siblingFiles: siblingStatuses,
      buildFiles: [],
      blockGaps: [],
      provableBlocks: 0,
      leanLinked: 0,
      totalSorries: siblingStatuses.reduce(
        (sum, f) => sum + f.sorries.length,
        0
      ),
      uncitedSorries: siblingStatuses.reduce(
        (sum, f) => sum + f.sorries.filter((s) => !s.hasCitation).length,
        0
      ),
      trivialTruths: siblingStatuses.reduce(
        (sum, f) => sum + f.trivials.length,
        0
      ),
      axiomCount: siblingStatuses.reduce(
        (sum, f) => sum + f.axioms.length,
        0
      ),
      witnessedCount: siblingStatuses.filter((f) => f.witnessed).length,
      staleCount: siblingStatuses.filter((f) => f.stale).length,
      totalFiles: siblingStatuses.length,
    });
  }

  // Add build files to chapters
  for (const bf of buildLeanFiles) {
    const chapter = mapBuildFileToChapter(bf);
    if (chapterFilter && !chapter.includes(chapterFilter)) continue;

    const status = auditLeanFile(bf);

    if (!chapterMap.has(chapter)) {
      chapterMap.set(chapter, {
        chapter,
        siblingFiles: [],
        buildFiles: [],
        blockGaps: [],
        provableBlocks: 0,
        leanLinked: 0,
        totalSorries: 0,
        uncitedSorries: 0,
        trivialTruths: 0,
        axiomCount: 0,
        witnessedCount: 0,
        staleCount: 0,
        totalFiles: 0,
      });
    }

    const ch = chapterMap.get(chapter)!;
    ch.buildFiles.push(status);
    ch.totalSorries += status.sorries.length;
    ch.uncitedSorries += status.sorries.filter((s) => !s.hasCitation).length;
    ch.trivialTruths += status.trivials.length;
    ch.axiomCount += status.axioms.length;
    if (status.witnessed) ch.witnessedCount++;
    if (status.stale) ch.staleCount++;
    ch.totalFiles++;
  }

  // Bucket blocks + gaps into chapters; create chapter entries on demand.
  for (const b of blocks) {
    if (chapterFilter && !b.chapter.includes(chapterFilter)) continue;
    if (!chapterMap.has(b.chapter)) {
      chapterMap.set(b.chapter, {
        chapter: b.chapter,
        siblingFiles: [], buildFiles: [], blockGaps: [],
        provableBlocks: 0, leanLinked: 0,
        totalSorries: 0, uncitedSorries: 0, trivialTruths: 0,
        axiomCount: 0, witnessedCount: 0, staleCount: 0, totalFiles: 0,
      });
    }
    const ch = chapterMap.get(b.chapter)!;
    if (PROVABLE_KINDS.has(b.kind)) {
      ch.provableBlocks++;
      if (b.hasLeanField || b.siblingLeanExists) ch.leanLinked++;
    }
  }
  for (const g of allGaps) {
    // Re-derive chapter from tsFile path to avoid pulling BlockManifest into BlockGap.
    const m = g.tsFile.match(/quantum-observable-universe\/([^/]+)\//);
    const chapter = m ? m[1] : "root";
    if (chapterFilter && !chapter.includes(chapterFilter)) continue;
    chapterMap.get(chapter)?.blockGaps.push(g);
  }

  const chapters = Array.from(chapterMap.values()).sort((a, b) =>
    a.chapter.localeCompare(b.chapter)
  );

  const gapCount = (kind: BlockGap["gap"]) =>
    chapters.reduce((s, c) => s + c.blockGaps.filter((g) => g.gap === kind).length, 0);

  const summary = {
    totalLeanFiles: chapters.reduce((s, c) => s + c.totalFiles, 0),
    totalSorries: chapters.reduce((s, c) => s + c.totalSorries, 0),
    uncitedSorries: chapters.reduce((s, c) => s + c.uncitedSorries, 0),
    trivialTruths: chapters.reduce((s, c) => s + c.trivialTruths, 0),
    axiomCount: chapters.reduce((s, c) => s + c.axiomCount, 0),
    witnessedCount: chapters.reduce((s, c) => s + c.witnessedCount, 0),
    staleCount: chapters.reduce((s, c) => s + c.staleCount, 0),
    pendingCount: 0,
    provableBlocks: chapters.reduce((s, c) => s + c.provableBlocks, 0),
    leanLinked: chapters.reduce((s, c) => s + c.leanLinked, 0),
    missingLeanFile: gapCount("missing-lean-file"),
    unresolvedDecl: gapCount("unresolved-decl"),
    declInWrongFile: gapCount("decl-in-wrong-file"),
    placeholderStatement: gapCount("placeholder-statement"),
    sorryNoCitation: gapCount("sorry-no-citation"),
  };
  summary.pendingCount =
    summary.totalLeanFiles - summary.witnessedCount - summary.staleCount;

  return {
    generatedAt: new Date().toISOString(),
    currentCommitSha: currentCommit,
    paper: paperDir,
    chapters,
    summary,
  };
}

// ── Console output ───────────────────────────────────────────────

function printReport(report: AuditReport) {
  console.log(`\n${"═".repeat(72)}`);
  console.log(`  LEAN CONTENT BLOCK AUDIT — ${report.paper}`);
  console.log(`  Generated: ${report.generatedAt}`);
  console.log(`  Commit: ${report.currentCommitSha}`);
  console.log(`${"═".repeat(72)}\n`);

  // Summary table
  console.log("## Summary\n");
  console.log(`  Total .lean files:         ${report.summary.totalLeanFiles}`);
  console.log(`  Total sorries:             ${report.summary.totalSorries}`);
  console.log(`  Uncited sorries:           ${report.summary.uncitedSorries}  (file-level)`);
  console.log(`  Trivial truths:            ${report.summary.trivialTruths}  (True := by trivial)`);
  console.log(`  Axiom declarations:        ${report.summary.axiomCount}`);
  console.log(`  Witnessed (built):         ${report.summary.witnessedCount}`);
  console.log(`  Stale witnesses:           ${report.summary.staleCount}`);
  console.log(`  Pending (not built):       ${report.summary.pendingCount}`);
  console.log();
  console.log("## Block-level gaps (content blocks vs Lean code)\n");
  console.log(`  Provable blocks:           ${report.summary.provableBlocks}`);
  console.log(`  Lean-linked:               ${report.summary.leanLinked}`);
  console.log(`  Missing .lean file:        ${report.summary.missingLeanFile}`);
  console.log(`  Unresolved decl ref:       ${report.summary.unresolvedDecl}`);
  console.log(`  Decl in wrong file:        ${report.summary.declInWrongFile}`);
  console.log(`  Placeholder statement:     ${report.summary.placeholderStatement}  (decl proves True/Unit)`);
  console.log(`  Sorry on referenced decl:  ${report.summary.sorryNoCitation}`);
  console.log();

  // Chapter-by-chapter
  for (const ch of report.chapters) {
    const statusIcon =
      ch.totalSorries === 0 && ch.trivialTruths === 0
        ? "✅"
        : ch.uncitedSorries > 0 || ch.trivialTruths > 0
          ? "🔴"
          : "🟡";

    console.log(
      `\n### ${statusIcon} ${ch.chapter}  (${ch.totalFiles} files, ${ch.totalSorries} sorries)`
    );

    if (ch.siblingFiles.length > 0) {
      console.log(`  Sibling .lean files: ${ch.siblingFiles.length}`);
    }
    if (ch.buildFiles.length > 0) {
      console.log(`  Build system files:  ${ch.buildFiles.length}`);
    }

    // List sorries
    if (ch.totalSorries > 0) {
      console.log(`\n  Sorries:`);
      const allFiles = [...ch.siblingFiles, ...ch.buildFiles];
      for (const f of allFiles) {
        for (const s of f.sorries) {
          const icon = s.hasCitation ? "📎" : "❌";
          const cite = s.citation ? ` (${s.citation})` : " — NO CITATION";
          console.log(`    ${icon} ${basename(s.file)}:${s.line}${cite}`);
        }
      }
    }

    // List trivial truths
    if (ch.trivialTruths > 0) {
      console.log(`\n  Trivial truths (placeholders):`);
      const allFiles = [...ch.siblingFiles, ...ch.buildFiles];
      for (const f of allFiles) {
        for (const t of f.trivials) {
          console.log(`    🚫 ${basename(t.file)}:${t.line} — ${t.statement}`);
        }
      }
    }

    // List axioms
    if (ch.axiomCount > 0) {
      console.log(`\n  Axioms (${ch.axiomCount}):`);
      const allFiles = [...ch.siblingFiles, ...ch.buildFiles];
      for (const f of allFiles) {
        for (const a of f.axioms) {
          const icon = a.hasCitation ? "📎" : "⚠️";
          console.log(`    ${icon} ${basename(a.file)}:${a.line} — axiom ${a.name}`);
        }
      }
    }

    // Block-level gaps for this chapter
    if (ch.blockGaps.length > 0) {
      const buckets: Record<string, BlockGap[]> = {};
      for (const g of ch.blockGaps) (buckets[g.gap] ??= []).push(g);
      console.log(`\n  Block gaps: ${ch.blockGaps.length} (provable=${ch.provableBlocks}, linked=${ch.leanLinked})`);
      for (const kind of Object.keys(buckets).sort()) {
        const items = buckets[kind];
        console.log(`    [${kind}] ×${items.length}`);
        for (const g of items.slice(0, 8)) {
          const tail = g.detail ? ` — ${g.detail}` : "";
          console.log(`      • ${g.kind}:${g.label}${tail}`);
        }
        if (items.length > 8) console.log(`      … +${items.length - 8} more`);
      }
    }

    // Witness status
    const allFiles = [...ch.siblingFiles, ...ch.buildFiles];
    const witnessedFiles = allFiles.filter((f) => f.witnessed && !f.stale);
    const staleFiles = allFiles.filter((f) => f.stale);
    const pendingFiles = allFiles.filter((f) => !f.witnessed && !f.stale);

    if (staleFiles.length > 0) {
      console.log(`\n  Stale witnesses (need rebuild):`);
      for (const f of staleFiles) {
        console.log(`    🔄 ${basename(f.file)} (hash: ${f.hash})`);
      }
    }
  }

  console.log(`\n${"═".repeat(72)}`);
  console.log(`  END OF AUDIT`);
  console.log(`${"═".repeat(72)}\n`);
}

// ── CLI ──────────────────────────────────────────────────────────

if (import.meta.main) {
  const args = process.argv.slice(2);
  const jsonMode = args.includes("--json");
  const chapterIdx = args.indexOf("--chapter");
  const chapterFilter =
    chapterIdx >= 0 ? args[chapterIdx + 1] : undefined;

  const report = runAudit("quantum-observable-universe", chapterFilter);

  if (jsonMode) {
    console.log(JSON.stringify(report, null, 2));
  } else {
    printReport(report);
  }
}

export { runAudit, type AuditReport, type ChapterAudit, type LeanFileStatus };
