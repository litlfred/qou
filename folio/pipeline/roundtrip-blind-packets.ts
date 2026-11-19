#!/usr/bin/env bun
/**
 * Deterministic Comment/Spoiler Scrubber & Blind Packet Builder for the
 * Three-Way Multi-Agent Semantic Round-Trip Audits (Epic `qou-ncxf`, Task `qou-7vhp`):
 *
 *   - RT-1: Lean Statement -> English -> Lean Statement (+ vs Paper Statement)
 *   - RT-2: English Narrative Proof -> Lean Stmt/Skeleton & Lean Proof -> Narrative
 *   - RT-3: Theorem Statement <-> English Narrative Proof
 *
 * Enforces strict information isolation:
 *   1. Strips all `-- ...` line comments and nested `/- ... -/` / `/-! ... -/`
 *      docstrings from Lean 4 source files.
 *   2. Replaces theorem/lemma proof bodies with `:= sorry` for RT-1 statement
 *      packets while preserving full comment-stripped proof bodies for RT-2.
 *   3. Splits inline `**Proof.**` sections or pairs explicit `proof(...)` blocks
 *      (`prf:*`), scrubbing self-identifying `#label` anchors from blind proof
 *      inputs and assigning opaque `item_NNN` IDs so blind agents cannot infer
 *      claims from block filenames or labels.
 */

import { existsSync, mkdirSync, readdirSync, readFileSync, statSync, writeFileSync } from "node:fs";
import { basename, dirname, join, relative, resolve } from "node:path";

const REPO_ROOT = resolve(import.meta.dir, "..", "..");
const DEFAULT_FOLIO = join(REPO_ROOT, "folio", "quantum-observable-universe");

/**
 * Strip all `--` line comments and arbitrarily nested `/- ... -/` block
 * comments from Lean 4 code while preserving string literals.
 */
export function stripLeanComments(src: string): string {
  let out = "";
  let i = 0;
  let blockDepth = 0;
  let inString = false;

  while (i < src.length) {
    const ch = src[i];
    const next = i + 1 < src.length ? src[i + 1] : "";

    if (blockDepth > 0) {
      if (ch === "/" && next === "-") {
        blockDepth++;
        i += 2;
        continue;
      }
      if (ch === "-" && next === "/") {
        blockDepth--;
        i += 2;
        continue;
      }
      if (ch === "\n") out += "\n";
      i++;
      continue;
    }

    if (inString) {
      out += ch;
      if (ch === "\\" && i + 1 < src.length) {
        out += src[i + 1];
        i += 2;
        continue;
      }
      if (ch === '"') inString = false;
      i++;
      continue;
    }

    if (ch === '"') {
      inString = true;
      out += ch;
      i++;
      continue;
    }

    if (ch === "/" && next === "-") {
      blockDepth = 1;
      i += 2;
      continue;
    }

    if (ch === "-" && next === "-") {
      // Advance to newline
      while (i < src.length && src[i] !== "\n") i++;
      continue;
    }

    out += ch;
    i++;
  }

  return out
    .split("\n")
    .map((line) => line.replace(/\s+$/, ""))
    .join("\n")
    .replace(/\n{3,}/g, "\n\n")
    .trim();
}

const TOP_LEVEL_DECL_RE =
  /^(?:@(?:[^\n]+)\s+)*(?:private\s+|protected\s+|noncomputable\s+)*(theorem|lemma|example|def|abbrev|structure|class|inductive|instance|axiom|opaque|namespace|section|end|open|variable|import)\b/;

export interface LeanTopChunk {
  kind: string;
  name?: string;
  text: string;
}

/**
 * Split comment-stripped Lean source into top-level chunks (unindented decl headers).
 */
export function splitLeanTopChunks(stripped: string): LeanTopChunk[] {
  const lines = stripped.split("\n");
  const chunks: LeanTopChunk[] = [];
  let curKind = "header";
  let curName: string | undefined;
  let curLines: string[] = [];

  const flush = () => {
    const text = curLines.join("\n").trim();
    if (text) chunks.push({ kind: curKind, name: curName, text });
    curLines = [];
  };

  for (const line of lines) {
    if (line.length > 0 && !/^\s/.test(line)) {
      const m = line.match(TOP_LEVEL_DECL_RE);
      if (m) {
        flush();
        curKind = m[1];
        const afterKw = line.slice(m[0].length).trim();
        const nm = afterKw.match(/^([A-Za-z0-9_'.]+)/);
        curName = nm ? nm[1] : undefined;
      }
    }
    curLines.push(line);
  }
  flush();
  return chunks;
}

/**
 * Replace the proof body of a `theorem` / `lemma` / `example` chunk with `:= sorry`
 * while keeping its full binder + type signature intact.
 */
export function stripProofFromTheoremChunk(chunkText: string): string {
  // Match the top-level `:= by` or `:=` that starts the proof term after the return type.
  // Track (), [], {}, ⦃⦄ nesting so `:=` inside default binder args `(x : Nat := 0)` is ignored!
  let depth = 0;
  for (let i = 0; i < chunkText.length - 1; i++) {
    const ch = chunkText[i];
    if (ch === "(" || ch === "[" || ch === "{" || ch === "⦃") depth++;
    else if (ch === ")" || ch === "]" || ch === "}" || ch === "⦄") depth = Math.max(0, depth - 1);
    else if (depth === 0 && ch === ":" && chunkText[i + 1] === "=") {
      return chunkText.slice(0, i).trimEnd() + " := sorry";
    }
  }
  // `where` or pattern-matched theorem fallback
  const byIdx = chunkText.search(/\bby\b/);
  if (byIdx > 0) return chunkText.slice(0, byIdx).trimEnd() + "sorry";
  return chunkText;
}

/**
 * Build focused RT-1 (signature-only) and RT-2 (signature + proof) windows around `targetDecl`
 * (or the whole file if small / sibling `.lean`), keeping helper `def`/`structure`/`abbrev`
 * chunks above `targetDecl` and eliding unrelated other theorems' proof bodies.
 */
export function extractFocusedLeanViews(
  rawLean: string,
  targetFqn?: string,
): { signatureOnly: string; fullTargetProof: string } {
  const stripped = stripLeanComments(rawLean);
  const chunks = splitLeanTopChunks(stripped);
  const shortTarget = targetFqn ? targetFqn.split(".").pop() : undefined;

  let targetIdx = -1;
  if (shortTarget) {
    // Prefer matching a theorem/lemma declaration; if `targetFqn` names the module
    // or a carrier `class`/`structure` at the top of the file (e.g. `SurrealRateCalculus`),
    // do not truncate before the theorems that follow that carrier!
    targetIdx = chunks.findIndex(
      (c) =>
        (c.kind === "theorem" || c.kind === "lemma" || c.kind === "example") &&
        (c.name === shortTarget || (c.name && shortTarget.endsWith(c.name))),
    );
  }

  const sigParts: string[] = [];
  const fullParts: string[] = [];

  for (let idx = 0; idx < chunks.length; idx++) {
    const c = chunks[idx];
    const isThmLike = c.kind === "theorem" || c.kind === "lemma" || c.kind === "example";
    if (targetIdx >= 0 && idx > targetIdx && c.kind !== "end") {
      // Stop after the target declaration (except closing namespace/section `end`s)
      continue;
    }
    if (isThmLike) {
      if (targetIdx < 0) {
        // Sibling file with no explicit target hit: strip proofs for RT-1, keep all for RT-2
        sigParts.push(stripProofFromTheoremChunk(c.text));
        fullParts.push(c.text);
      } else if (idx === targetIdx) {
        sigParts.push(stripProofFromTheoremChunk(c.text));
        fullParts.push(c.text);
      } else {
        // Earlier helper lemma: keep only its signature as context
        const helperSig = stripProofFromTheoremChunk(c.text);
        sigParts.push(helperSig);
        fullParts.push(helperSig);
      }
    } else {
      sigParts.push(c.text);
      fullParts.push(c.text);
    }
  }

  return {
    signatureOnly: sigParts.join("\n\n").slice(0, 14000),
    fullTargetProof: fullParts.join("\n\n").slice(0, 18000),
  };
}

/**
 * Scrub anchor spoilers (`[text](#label)` -> `text`, `\ref{...}` -> `[ref]`) and
 * leading `**Proof.**` headers from markdown so blind agents cannot read target labels.
 */
export function scrubBlindProofMarkdown(md: string): string {
  return md
    .replace(/\[([^\]]+)\]\(#([^)]+)\)/g, "$1")
    .replace(/^(\*\*Proof[^*]*\*\*\.?|\*Proof[^*]*\*\.?|##+\s*Proof[^\n]*)\s*/i, "")
    .trim();
}

export function scrubBlindStatementMarkdown(md: string): string {
  return md
    .replace(/\[([^\]]+)\]\(#([^)]+)\)/g, "$1")
    .replace(/\{#[A-Za-z0-9_:-]+\}/g, "")
    .trim();
}

/**
 * Split a statement `.md` file if it embeds an inline `**Proof.**` section.
 */
export function splitInlineProof(md: string): { stmtMd: string; inlineProofMd?: string } {
  const m = md.match(/\n(\*\*Proof(?:\s*\([^)]*\))?\.\*\*|\*Proof\.\*|##+\s*Proof\b)/i);
  if (!m || m.index === undefined) {
    return { stmtMd: md.trim() };
  }
  return {
    stmtMd: md.slice(0, m.index).trim(),
    inlineProofMd: md.slice(m.index + 1).trim(),
  };
}

interface ParsedBlockMeta {
  kind: string;
  label: string;
  title: string;
  tsPath: string;
  mdPath: string;
  leanRef?: string;
  uses: string[];
}

function parseTsBlock(tsPath: string): ParsedBlockMeta | undefined {
  const mdPath = tsPath.replace(/\.ts$/, ".md");
  if (!existsSync(mdPath)) return undefined;
  const txt = readFileSync(tsPath, "utf8");
  const km = txt.match(/export\s+default\s+(\w+)\s*\(\s*\{/);
  const lm = txt.match(/label:\s*"([^"]+)"/);
  if (!km || !lm) return undefined;
  const tm = txt.match(/title:\s*(?:\n\s*)?"([^"]+)"/);
  const rm = txt.match(/ref:\s*"([^"]+)"/);
  const usesBlock = txt.match(/uses:\s*\[([\s\S]*?)\]/);
  const uses: string[] = [];
  if (usesBlock) {
    for (const um of usesBlock[1].matchAll(/"([^"]+)"/g)) uses.push(um[1]);
  }
  return {
    kind: km[1],
    label: lm[1],
    title: tm ? tm[1] : "",
    tsPath,
    mdPath,
    leanRef: rm ? rm[1] : undefined,
    uses,
  };
}

function collectLeanFiles(dir: string): string[] {
  const res: string[] = [];
  if (!existsSync(dir)) return res;
  for (const entry of readdirSync(dir)) {
    if (entry === ".lake" || entry === "node_modules") continue;
    const full = join(dir, entry);
    const st = statSync(full);
    if (st.isDirectory()) res.push(...collectLeanFiles(full));
    else if (entry.endsWith(".lean")) res.push(full);
  }
  return res;
}

async function createLeanResolver(): Promise<(leanRef: string | undefined, tsPath: string) => string | undefined> {
  // Build a single O(1) declaration-name -> file index over folio/quantum-observable-universe/lean/QOU
  const declIndex = new Map<string, string[]>();
  const leanFiles = collectLeanFiles(join(DEFAULT_FOLIO, "lean", "QOU"));
  const declRe = /^(?:@(?:[^\n]+)\s+)*(?:private\s+|protected\s+|noncomputable\s+)*(?:theorem|lemma|def|abbrev|structure|class|inductive|axiom|opaque)\s+([A-Za-z0-9_']+)/gm;
  // Also cache file contents so import-only aggregator files (e.g. `QOU/AlgebraicSubstrate.lean`)
  // never swallow a declaration that actually lives in a submodule!
  const fileDeclSet = new Map<string, Set<string>>();
  for (const lf of leanFiles) {
    const txt = readFileSync(lf, "utf8");
    const s = new Set<string>();
    for (const m of txt.matchAll(declRe)) {
      const shortName = m[1];
      s.add(shortName);
      const arr = declIndex.get(shortName);
      if (arr) arr.push(lf);
      else declIndex.set(shortName, [lf]);
    }
    fileDeclSet.set(lf, s);
  }

  return (leanRef: string | undefined, tsPath: string) => {
    const sibling = tsPath.replace(/\.ts$/, ".lean");
    if (existsSync(sibling)) return sibling;
    if (!leanRef || !leanRef.startsWith("qou:")) return undefined;
    const fqn = leanRef.slice("qou:".length);
    const parts = fqn.split(".");
    const shortName = parts[parts.length - 1];
    for (let cut = parts.length - 1; cut >= 2; cut--) {
      const cand = join(DEFAULT_FOLIO, "lean", ...parts.slice(0, cut)) + ".lean";
      if (existsSync(cand) && fileDeclSet.get(cand)?.has(shortName)) return cand;
    }
    const hits = declIndex.get(shortName);
    if (hits && hits.length === 1) return hits[0];
    if (hits && hits.length > 1) {
      const modHint = parts.slice(1, -1).join("/");
      const best = hits.find((h) => h.includes(modHint));
      return best ?? hits[0];
    }
    return undefined;
  };
}

function collectTsFiles(dir: string): string[] {
  const res: string[] = [];
  for (const entry of readdirSync(dir)) {
    if (entry === "lean" || entry === ".lake" || entry === "node_modules" || entry === "audit") continue;
    const full = join(dir, entry);
    const st = statSync(full);
    if (st.isDirectory()) res.push(...collectTsFiles(full));
    else if (entry.endsWith(".ts") && !entry.endsWith(".test.ts")) res.push(full);
  }
  return res.sort();
}

export interface ManifestRecord {
  id: string;
  label: string;
  kind: string;
  title: string;
  chapter: string;
  mdRelPath: string;
  proofMdRelPath?: string;
  leanRelPath?: string;
  leanRef?: string;
  hasRT1: boolean;
  hasRT2: boolean;
  hasRT3: boolean;
  paperStmtMd: string;
  narrativeProofMd?: string;
  originalLeanSignature?: string;
  strippedLeanFull?: string;
}

export async function buildRoundtripPackets(opts: {
  folioDir?: string;
  chapter?: string;
  filter?: string;
  requireProof?: boolean;
  requireLean?: boolean;
  offset?: number;
  limit?: number;
}) {
  const folioDir = opts.folioDir ?? DEFAULT_FOLIO;
  const resolveLean = await createLeanResolver();
  const tsFiles = collectTsFiles(opts.chapter ? join(folioDir, opts.chapter) : folioDir);

  const allBlocks: ParsedBlockMeta[] = [];
  const proofByTarget = new Map<string, ParsedBlockMeta>();
  const proofByStem = new Map<string, ParsedBlockMeta>();

  for (const f of tsFiles) {
    const meta = parseTsBlock(f);
    if (!meta) continue;
    allBlocks.push(meta);
    if (meta.kind === "proof") {
      const dir = dirname(f);
      const stem = basename(f, ".ts").replace(/-proof$/, "");
      proofByStem.set(join(dir, stem), meta);
      if (meta.uses.length > 0) {
        proofByTarget.set(meta.uses[0], meta);
      }
    }
  }

  const provableKinds = new Set(["theorem", "proposition", "lemma", "corollary"]);
  const records: ManifestRecord[] = [];

  for (const b of allBlocks) {
    if (!provableKinds.has(b.kind)) continue;
    if (opts.filter && !b.label.includes(opts.filter) && !b.mdPath.includes(opts.filter)) continue;

    const rawMd = readFileSync(b.mdPath, "utf8");
    const { stmtMd, inlineProofMd } = splitInlineProof(rawMd);
    const stemKey = join(dirname(b.tsPath), basename(b.tsPath, ".ts"));
    const companionPrf = proofByStem.get(stemKey) ?? proofByTarget.get(b.label);
    const rawProofMd = companionPrf ? readFileSync(companionPrf.mdPath, "utf8") : inlineProofMd;

    const leanPath = resolveLean(b.leanRef, b.tsPath);
    if (opts.requireProof && !rawProofMd) continue;
    if (opts.requireLean && !leanPath) continue;

    let originalLeanSignature: string | undefined;
    let strippedLeanFull: string | undefined;
    if (leanPath && existsSync(leanPath)) {
      const rawLean = readFileSync(leanPath, "utf8");
      const isSiblingLean = dirname(leanPath) === dirname(b.mdPath);
      const includeWholeFile = isSiblingLean || rawLean.length <= 16000;
      const targetFqn =
        !includeWholeFile && b.leanRef?.startsWith("qou:") ? b.leanRef.slice(4) : undefined;
      const views = extractFocusedLeanViews(rawLean, targetFqn);
      originalLeanSignature = views.signatureOnly;
      strippedLeanFull = views.fullTargetProof;
    }

    const cleanStmt = scrubBlindStatementMarkdown(stmtMd);
    const cleanProof = rawProofMd ? scrubBlindProofMarkdown(rawProofMd) : undefined;

    records.push({
      id: "", // assigned after slicing
      label: b.label,
      kind: b.kind,
      title: b.title,
      chapter: basename(dirname(b.mdPath)),
      mdRelPath: relative(REPO_ROOT, b.mdPath),
      proofMdRelPath: companionPrf ? relative(REPO_ROOT, companionPrf.mdPath) : undefined,
      leanRelPath: leanPath ? relative(REPO_ROOT, leanPath) : undefined,
      leanRef: b.leanRef,
      hasRT1: Boolean(originalLeanSignature),
      hasRT2: Boolean(originalLeanSignature && cleanProof),
      hasRT3: Boolean(cleanProof),
      paperStmtMd: cleanStmt,
      narrativeProofMd: cleanProof,
      originalLeanSignature,
      strippedLeanFull,
    });
  }

  const offset = opts.offset ?? 0;
  const sliced = opts.limit ? records.slice(offset, offset + opts.limit) : records.slice(offset);
  sliced.forEach((r, idx) => {
    r.id = `item_${String(offset + idx + 1).padStart(4, "0")}`;
  });

  return {
    totalMatched: records.length,
    sliced,
    rt1Leg1A: sliced
      .filter((r) => r.hasRT1)
      .map((r) => ({ id: r.id, leanSignature: r.originalLeanSignature! })),
    rt2Leg2A: sliced
      .filter((r) => r.hasRT2)
      .map((r) => ({ id: r.id, narrativeProofMd: r.narrativeProofMd! })),
    rt2Leg2B: sliced
      .filter((r) => r.hasRT2)
      .map((r) => ({ id: r.id, strippedLeanFull: r.strippedLeanFull! })),
    rt3Leg3A: sliced
      .filter((r) => r.hasRT3)
      .map((r) => ({ id: r.id, narrativeProofMd: r.narrativeProofMd! })),
    rt3Leg3B: sliced
      .filter((r) => r.hasRT3)
      .map((r) => ({ id: r.id, theoremStmtMd: r.paperStmtMd })),
  };
}

if (import.meta.main) {
  const arg = (name: string) => {
    const i = process.argv.indexOf(`--${name}`);
    return i >= 0 ? process.argv[i + 1] : undefined;
  };
  const hasFlag = (name: string) => process.argv.includes(`--${name}`);

  const outDir = arg("out");
  const chapter = arg("chapter");
  const filter = arg("filter");
  const offset = arg("offset") ? Number(arg("offset")) : 0;
  const limit = arg("limit") ? Number(arg("limit")) : undefined;
  const requireProof = hasFlag("require-proof");
  const requireLean = hasFlag("require-lean");

  const res = await buildRoundtripPackets({
    chapter,
    filter,
    offset,
    limit,
    requireProof,
    requireLean,
  });

  console.log(
    JSON.stringify({
      totalMatched: res.totalMatched,
      emittedCount: res.sliced.length,
      rt1Count: res.rt1Leg1A.length,
      rt2Count: res.rt2Leg2A.length,
      rt3Count: res.rt3Leg3A.length,
    }),
  );

  if (outDir) {
    mkdirSync(outDir, { recursive: true });
    writeFileSync(join(outDir, "manifest.json"), JSON.stringify(res.sliced, null, 2));
    writeFileSync(join(outDir, "rt1_leg1a_lean_only.json"), JSON.stringify(res.rt1Leg1A, null, 2));
    writeFileSync(join(outDir, "rt2_leg2a_narr_only.json"), JSON.stringify(res.rt2Leg2A, null, 2));
    writeFileSync(join(outDir, "rt2_leg2b_lean_full_only.json"), JSON.stringify(res.rt2Leg2B, null, 2));
    writeFileSync(join(outDir, "rt3_leg3a_prf_only.json"), JSON.stringify(res.rt3Leg3A, null, 2));
    writeFileSync(join(outDir, "rt3_leg3b_stmt_only.json"), JSON.stringify(res.rt3Leg3B, null, 2));
  }
}
