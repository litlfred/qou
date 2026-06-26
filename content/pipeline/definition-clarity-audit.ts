#!/usr/bin/env bun
/**
 * Definition / statement clarity + concision audit.
 *
 * A content block can validate (schema-clean, refs resolve, Lean sibling
 * present) and still read badly: the defined term is never emphasised, the
 * definition is buried under paragraphs of motivation, or a single
 * `definition` block silently bundles three or four distinct definienda.
 * None of the existing QA axes (voice / wall / q-usage / canonical /
 * detangler / bib / proof / compute) measure *clarity of the statement
 * itself*. This scanner adds that axis.
 *
 * It walks every content block (`.md` + sibling `.ts`), reads the block
 * kind + title from the manifest and the prose from the `.md`, strips
 * code/TeX fences, applies cheap structural heuristics, and reports
 * candidates for four criteria:
 *
 *   clarity-defterm-bold   (definition)            — the principal defined
 *       term must be marked at its definition site, either in markdown
 *       bold `**…**` or via the `:defterm[…]{#slug}` glossary directive.
 *       A definition whose own term appears only as plain text / `*italic*`
 *       fails.
 *
 *   clarity-defn-single    (definition)            — a definition block
 *       defines exactly ONE concept. Multiple bold section-headers,
 *       multiple `defines:` entries, or several "we define / is defined as"
 *       lead-ins are a candidate for "split into one block per definiendum".
 *
 *   clarity-defn-tight     (definition)            — the definition is
 *       stated tightly and near the top, without a long motivational
 *       preamble or a stack of downstream-realisation sub-sections
 *       ("Physical meaning.", "Role in …", "Three-context behaviour.").
 *
 *   clarity-stmt-tight     (theorem/proposition/   — the claim is stated
 *                           lemma/corollary)          tightly. Proofs live
 *       in separate `*-proof` blocks in this corpus, so a provable block
 *       is just its statement and should not ramble.
 *
 * Heuristics are deliberately high-recall / agent-confirmed, exactly like
 * `lean-vacuity-axiom-audit.ts`: a `fail` here is a *candidate*, not a
 * verdict. The `definition-clarity-audit` skill opens the block, applies
 * judgement, and (when the criteria are registered in the canonical
 * qa-sweep registry, which lives in the external folio-assistant repo)
 * records the adjudicated `reviewer.kind="agent"` sidecar entry. Until
 * then this scanner is standalone: it emits a JSON + Markdown report and,
 * with `--write-sidecars`, upserts `reviewer.kind="script"` candidate
 * entries into `<block>.qa.json`.
 *
 *   bun run content/pipeline/definition-clarity-audit.ts \
 *     [root ...]                 # default: content/
 *     [--json  docs/audits/2026-06-26-definition-clarity-audit.json]
 *     [--md    docs/audits/2026-06-26-definition-clarity-audit.md]
 *     [--only  <criterion>]      # restrict to one criterion id
 *     [--branch <name>]          # blob-url branch (default: current)
 *     [--write-sidecars]         # upsert <block>.qa.json script entries
 *     [--top N]                  # offenders per criterion in the MD (def 25)
 *     [--quiet]
 *
 * Criterion ids (the "audit parameters"):
 *   clarity-defterm-bold   clarity-defn-single
 *   clarity-defn-tight     clarity-stmt-tight
 *
 * @module content/pipeline/definition-clarity-audit
 */
import { createHash } from "node:crypto";
import {
  existsSync,
  readFileSync,
  readdirSync,
  statSync,
  writeFileSync,
} from "node:fs";
import { execFileSync } from "node:child_process";
import { join, relative, resolve, dirname, basename } from "node:path";

// ---------------------------------------------------------------------------
// `block-qa/v1` sidecar types, inlined. The canonical schema lives at
// `folio-assistant/schemas/block-qa.ts`, but `folio-assistant/` is gitignored
// on this branch (the QA pipeline migration), so this scanner carries its own
// copy to stay self-contained and committable — same pattern as
// `lean-vacuity-axiom-audit.ts`.
// ---------------------------------------------------------------------------
interface QaFieldHash {
  md?: string;
  ts?: string;
  lean?: string;
}
interface QaReviewer {
  kind: "script" | "agent" | "human";
  id: string;
  version?: string;
  script_hash?: string;
  script_commit_sha?: string;
}
interface QaCriterionEntry {
  field_hash: QaFieldHash;
  result: "pass" | "fail" | "warn" | "n/a";
  severity?: "critical" | "major" | "minor";
  evidence?: string;
  reviewer: QaReviewer;
  reviewed_at: string;
  reviewed_sha: string;
  notes?: string;
}

// ---------------------------------------------------------------------------
// Tunable thresholds. Conservative defaults; a `fail` is a candidate the
// agent confirms. Adjust here, not in the per-criterion functions.
// ---------------------------------------------------------------------------
const T = {
  /** clarity-defterm-bold: min token overlap between a bold/defterm span and
   *  the title term for the term to count as "marked at its definition". */
  termOverlap: 0.5,
  /** clarity-defn-single: bold section-headers at/above this count flag a
   *  block as bundling multiple definienda. */
  singleHeaders: 3,
  /** clarity-defn-single: defining-verb lead-ins ("we define", …). */
  singleVerbs: 3,
  /** clarity-defn-tight: prose word count (TeX/code stripped). */
  defnWords: 250,
  /** clarity-defn-tight: bold section-headers. */
  defnHeaders: 3,
  /** clarity-defn-tight: words of preamble before the first display-math /
   *  marked term. */
  defnPreamble: 60,
  /** clarity-stmt-tight: prose word count for a statement block. */
  stmtWords: 300,
  /** clarity-stmt-tight: bold section-headers. */
  stmtHeaders: 3,
  /** clarity-stmt-tight: preamble words before the first display-math. */
  stmtPreamble: 80,
};

type Result = "pass" | "fail" | "n/a";
type Severity = "critical" | "major" | "minor";
type DefnKind =
  | "definition"
  | "theorem"
  | "lemma"
  | "proposition"
  | "corollary"
  | "conjecture"
  | "example"
  | "remark"
  | "prose"
  | "equation"
  | "diagram"
  | "simulator";

const PROVABLE: DefnKind[] = ["theorem", "lemma", "proposition", "corollary"];

const CRITERIA = [
  "clarity-defterm-bold",
  "clarity-defn-single",
  "clarity-defn-tight",
  "clarity-stmt-tight",
] as const;
type Criterion = (typeof CRITERIA)[number];

interface Finding {
  label: string;
  kind: DefnKind;
  criterion: Criterion;
  result: Result;
  severity?: Severity;
  evidence: string;
  /** raw metrics, surfaced in the report for triage */
  metrics: Record<string, number | string>;
  mdPath: string; // repo-relative
  qaPath: string; // repo-relative sidecar path (may not exist)
}

interface Block {
  root: string;
  dir: string;
  kind: DefnKind;
  title: string;
  label: string;
  definesCount: number;
  mdPath: string;
  tsPath: string;
  md: string;
  ts: string;
}

// ---------------------------------------------------------------------------
// Manifest / prose parsing — regex only, no schema import (self-contained).
// ---------------------------------------------------------------------------

const BUILDER_RE =
  /\b(definition|theorem|lemma|proposition|corollary|conjecture|example|remark|prose|equation|diagram|simulator)\s*\(\s*\{/;

function parseKind(ts: string): DefnKind | null {
  const m = ts.match(BUILDER_RE);
  return m ? (m[1] as DefnKind) : null;
}

function parseStringField(ts: string, field: string): string {
  // double-quote (with escapes), then single, then backtick
  const dq = ts.match(
    new RegExp(`${field}\\s*:\\s*"((?:[^"\\\\]|\\\\.)*)"`),
  );
  if (dq) return dq[1].replace(/\\(["'`\\])/g, "$1");
  const sq = ts.match(
    new RegExp(`${field}\\s*:\\s*'((?:[^'\\\\]|\\\\.)*)'`),
  );
  if (sq) return sq[1].replace(/\\(["'`\\])/g, "$1");
  const bt = ts.match(new RegExp(`${field}\\s*:\\s*\`([^\`]*)\``));
  if (bt) return bt[1];
  return "";
}

function parseDefinesCount(ts: string): number {
  const m = ts.match(/defines\s*:\s*\[([\s\S]*?)\]/);
  if (!m) return 0;
  const inner = m[1].trim();
  if (!inner) return 0;
  // count quoted entries
  const entries = inner.match(/["'`][^"'`]+["'`]/g);
  return entries ? entries.length : 0;
}

const STOP = new Set([
  "the", "a", "an", "of", "for", "and", "or", "to", "in", "on", "is", "as",
  "by", "with", "its", "via", "at", "be", "we", "this", "that", "it",
]);

/** lower-case alphanumeric tokens; strips inline math and latex commands. */
function tokens(s: string): string[] {
  return s
    .replace(/\$[^$]*\$/g, " ") // inline math
    .replace(/\\[a-zA-Z]+/g, " ") // latex commands
    .replace(/[^a-zA-Z0-9]+/g, " ")
    .toLowerCase()
    .split(/\s+/)
    .filter((t) => t.length > 1 && !STOP.has(t));
}

/** principal term tokens from a title (text before the first parenthetical). */
function principalTokens(title: string): string[] {
  const head = title.split(/\s*[(（]/)[0];
  return tokens(head);
}

/** strip fenced code / tex blocks and display math; keep prose for wordcount. */
function prose(md: string): string {
  return md
    .replace(/```[\s\S]*?```/g, " ") // fenced code/tex
    .replace(/\$\$[\s\S]*?\$\$/g, " ") // display math
    .replace(/\\begin\{[\s\S]*?\\end\{[a-zA-Z*]+\}/g, " ") // latex envs
    .replace(/\$[^$]*\$/g, " M ") // inline math -> placeholder
    .replace(/:def?term\[[^\]]*\]\{[^}]*\}/g, (x) => x) // keep directives
    .replace(/[*_>#`]/g, " ");
}

function wordCount(s: string): number {
  return s.split(/\s+/).filter((w) => /[a-zA-Z0-9]/.test(w)).length;
}

/** bold spans that begin a paragraph/line and read like section headers:
 *  `**Pentagon identity.**`, `**Iterated-primitive definition.**` … */
function boldHeaders(md: string): string[] {
  const out: string[] = [];
  const re = /(^|\n)\s*\*\*([^*\n]{2,80}?)\*\*/g;
  let m: RegExpExecArray | null;
  while ((m = re.exec(md))) out.push(m[2].trim());
  return out;
}

/** every bold/defterm span inner text (for term-marking detection). */
function markedSpans(md: string): string[] {
  const out: string[] = [];
  let m: RegExpExecArray | null;
  const bold = /\*\*([^*\n]{1,120}?)\*\*/g;
  while ((m = bold.exec(md))) out.push(m[1]);
  const defterm = /:defterm\[([^\]]+)\]/g;
  while ((m = defterm.exec(md))) out.push(m[1]);
  return out;
}

const DEFINING_VERB =
  /\b(we define|is defined as|are defined as|defined to be|define the|denote[ds]? by|we call|is called|are called|call the|we set|we write)\b/gi;

function definingVerbs(s: string): number {
  const m = s.match(DEFINING_VERB);
  return m ? m.length : 0;
}

/** index of the first display-math / equation environment, or -1. */
function firstDisplayIdx(md: string): number {
  const idxs = [
    md.indexOf("$$"),
    md.search(/\\begin\{(equation|align|gather|multline)/),
    md.search(/```tex/),
  ].filter((i) => i >= 0);
  return idxs.length ? Math.min(...idxs) : -1;
}

/** index of the first marked principal-term occurrence, or -1. */
function firstMarkedTermIdx(md: string, pt: string[]): number {
  if (!pt.length) return -1;
  let best = -1;
  const scan = (re: RegExp) => {
    let m: RegExpExecArray | null;
    while ((m = re.exec(md))) {
      const tk = tokens(m[1]);
      const overlap = pt.filter((t) => tk.includes(t)).length / pt.length;
      if (overlap >= T.termOverlap) {
        if (best < 0 || m.index < best) best = m.index;
      }
    }
  };
  scan(/\*\*([^*\n]{1,120}?)\*\*/g);
  scan(/:defterm\[([^\]]+)\]/g);
  return best;
}

// ---------------------------------------------------------------------------
// Per-criterion checks
// ---------------------------------------------------------------------------

function checkDeftermBold(b: Block): Finding {
  const pt = principalTokens(b.title);
  const base = mkFinding(b, "clarity-defterm-bold");
  if (!pt.length) {
    base.result = "n/a";
    base.evidence = "title has no plain-text term (fully mathematical)";
    return base;
  }
  const spans = markedSpans(b.md);
  let best = 0;
  let bestSpan = "";
  for (const sp of spans) {
    const tk = tokens(sp);
    const overlap = pt.filter((t) => tk.includes(t)).length / pt.length;
    if (overlap > best) {
      best = overlap;
      bestSpan = sp;
    }
  }
  base.metrics = {
    term: pt.join(" "),
    bestOverlap: Number(best.toFixed(2)),
    boldSpans: spans.length,
  };
  if (best >= T.termOverlap) {
    base.result = "pass";
    base.evidence = `term marked via "${bestSpan.slice(0, 60)}"`;
  } else {
    base.result = "fail";
    base.severity = "minor";
    base.evidence = spans.length
      ? `term "${pt.join(" ")}" never bolded/defterm'd (${spans.length} bold spans, none match)`
      : `term "${pt.join(" ")}" never bolded/defterm'd (no bold spans at all)`;
  }
  return base;
}

function checkDefnSingle(b: Block): Finding {
  const headers = boldHeaders(b.md);
  const verbs = definingVerbs(prose(b.md));
  const base = mkFinding(b, "clarity-defn-single");
  base.metrics = {
    boldHeaders: headers.length,
    definesCount: b.definesCount,
    definingVerbs: verbs,
  };
  const tooMany =
    headers.length >= T.singleHeaders ||
    b.definesCount >= 2 ||
    verbs >= T.singleVerbs;
  if (tooMany) {
    base.result = "fail";
    base.severity =
      headers.length >= T.singleHeaders + 1 || b.definesCount >= 3
        ? "major"
        : "minor";
    const bits: string[] = [];
    if (headers.length >= T.singleHeaders)
      bits.push(`${headers.length} bold section-headers (${headers.slice(0, 4).map((h) => `"${h}"`).join(", ")}…)`);
    if (b.definesCount >= 2) bits.push(`${b.definesCount} defines[] entries`);
    if (verbs >= T.singleVerbs) bits.push(`${verbs} defining-verb lead-ins`);
    base.evidence = `bundles multiple definienda: ${bits.join("; ")}`;
  } else {
    base.result = "pass";
    base.evidence = "single definiendum";
  }
  return base;
}

function checkDefnTight(b: Block): Finding {
  const p = prose(b.md);
  const words = wordCount(p);
  const headers = boldHeaders(b.md).length;
  const pt = principalTokens(b.title);
  const dispIdx = firstDisplayIdx(b.md);
  const termIdx = firstMarkedTermIdx(b.md, pt);
  const anchor =
    [dispIdx, termIdx].filter((i) => i >= 0).length === 0
      ? -1
      : Math.min(...[dispIdx, termIdx].filter((i) => i >= 0));
  const preamble = anchor < 0 ? words : wordCount(prose(b.md.slice(0, anchor)));
  const base = mkFinding(b, "clarity-defn-tight");
  base.metrics = { words, boldHeaders: headers, preambleWords: preamble };
  const rambling =
    words > T.defnWords ||
    headers >= T.defnHeaders ||
    preamble > T.defnPreamble;
  if (rambling) {
    base.result = "fail";
    base.severity = words > 2 * T.defnWords || headers >= T.defnHeaders + 2 ? "major" : "minor";
    const bits: string[] = [];
    if (words > T.defnWords) bits.push(`${words} prose words (>${T.defnWords})`);
    if (headers >= T.defnHeaders) bits.push(`${headers} sub-sections (>=${T.defnHeaders})`);
    if (preamble > T.defnPreamble) bits.push(`${preamble}-word preamble before the definition (>${T.defnPreamble})`);
    base.evidence = `rambling: ${bits.join("; ")}`;
  } else {
    base.result = "pass";
    base.evidence = `tight (${words} words, ${headers} sub-sections)`;
  }
  return base;
}

function checkStmtTight(b: Block): Finding {
  const p = prose(b.md);
  const words = wordCount(p);
  const headers = boldHeaders(b.md).length;
  const dispIdx = firstDisplayIdx(b.md);
  const preamble = dispIdx < 0 ? words : wordCount(prose(b.md.slice(0, dispIdx)));
  const base = mkFinding(b, "clarity-stmt-tight");
  base.metrics = { words, boldHeaders: headers, preambleWords: preamble };
  const rambling =
    words > T.stmtWords ||
    headers >= T.stmtHeaders ||
    preamble > T.stmtPreamble;
  if (rambling) {
    base.result = "fail";
    base.severity = words > 2 * T.stmtWords || headers >= T.stmtHeaders + 2 ? "major" : "minor";
    const bits: string[] = [];
    if (words > T.stmtWords) bits.push(`${words} prose words (>${T.stmtWords})`);
    if (headers >= T.stmtHeaders) bits.push(`${headers} sub-sections (>=${T.stmtHeaders})`);
    if (preamble > T.stmtPreamble) bits.push(`${preamble}-word preamble before the statement (>${T.stmtPreamble})`);
    base.evidence = `rambling statement: ${bits.join("; ")}`;
  } else {
    base.result = "pass";
    base.evidence = `tight (${words} words, ${headers} sub-sections)`;
  }
  return base;
}

function mkFinding(b: Block, criterion: Criterion): Finding {
  return {
    label: b.label || `(${b.root})`,
    kind: b.kind,
    criterion,
    result: "n/a",
    evidence: "",
    metrics: {},
    mdPath: b.mdPath,
    qaPath: join(b.dir, `${b.root}.qa.json`),
  };
}

// ---------------------------------------------------------------------------
// Walk + drive
// ---------------------------------------------------------------------------

function* walk(dir: string): Generator<string> {
  let entries: string[];
  try {
    entries = readdirSync(dir);
  } catch {
    return;
  }
  for (const e of entries) {
    if (e === "node_modules" || e === ".git" || e === ".lake") continue;
    const full = join(dir, e);
    let st;
    try {
      st = statSync(full);
    } catch {
      continue;
    }
    if (st.isDirectory()) yield* walk(full);
    else if (e.endsWith(".md")) yield full;
  }
}

function loadBlock(mdPath: string, repoRoot: string): Block | null {
  const dir = dirname(mdPath);
  const root = basename(mdPath, ".md");
  const tsPath = join(dir, `${root}.ts`);
  if (!existsSync(tsPath)) return null;
  const ts = readFileSync(tsPath, "utf8");
  const kind = parseKind(ts);
  if (!kind) return null;
  const md = readFileSync(mdPath, "utf8");
  return {
    root,
    dir,
    kind,
    title: parseStringField(ts, "title"),
    label: parseStringField(ts, "label"),
    definesCount: parseDefinesCount(ts),
    mdPath: relative(repoRoot, mdPath),
    tsPath: relative(repoRoot, tsPath),
    md,
    ts,
  };
}

function findingsFor(b: Block, only?: Criterion): Finding[] {
  const out: Finding[] = [];
  const want = (c: Criterion) => !only || only === c;
  if (b.kind === "definition") {
    if (want("clarity-defterm-bold")) out.push(checkDeftermBold(b));
    if (want("clarity-defn-single")) out.push(checkDefnSingle(b));
    if (want("clarity-defn-tight")) out.push(checkDefnTight(b));
  }
  if (PROVABLE.includes(b.kind) && want("clarity-stmt-tight")) {
    out.push(checkStmtTight(b));
  }
  return out;
}

// ---------------------------------------------------------------------------
// Sidecar upsert (opt-in) — mirrors lean-vacuity-axiom-audit.ts
// ---------------------------------------------------------------------------

function sha12(s: string): string {
  return createHash("sha256").update(s).digest("hex").slice(0, 12);
}

function headSha(repoRoot: string): string {
  try {
    return execFileSync("git", ["rev-parse", "HEAD"], { cwd: repoRoot })
      .toString()
      .trim();
  } catch {
    return "unknown";
  }
}

function writeSidecar(
  b: Block,
  findings: Finding[],
  scriptHash: string,
  scriptSha: string,
  reviewedSha: string,
) {
  const qaPath = join(b.dir, `${b.root}.qa.json`);
  let doc: any = {};
  if (existsSync(qaPath)) {
    try {
      doc = JSON.parse(readFileSync(qaPath, "utf8"));
    } catch {
      doc = {};
    }
  }
  doc.$schema ??= "block-qa/v1";
  doc.label ??= b.label;
  doc.kind ??= b.kind;
  doc.criteria ??= {};
  const fh: QaFieldHash = {
    md: sha12(b.md),
    ts: sha12(b.ts),
  };
  const now = new Date().toISOString();
  for (const f of findings) {
    const entry: QaCriterionEntry = {
      field_hash: fh,
      result: f.result === "n/a" ? "n/a" : f.result,
      reviewer: {
        kind: "script",
        id: "content/pipeline/definition-clarity-audit.ts",
        version: "v1",
        script_hash: scriptHash,
        script_commit_sha: scriptSha,
      },
      reviewed_at: now,
      reviewed_sha: reviewedSha,
    };
    if (f.severity) entry.severity = f.severity;
    if (f.evidence) entry.evidence = f.evidence;
    doc.criteria[f.criterion] = [entry];
  }
  doc.updated_at = now;
  writeFileSync(qaPath, JSON.stringify(doc, null, 2) + "\n");
}

// ---------------------------------------------------------------------------
// Report
// ---------------------------------------------------------------------------

function blob(branch: string, path: string): string {
  return `https://github.com/litlfred/qou/blob/${branch}/${path}`;
}

function buildMd(
  findings: Finding[],
  scanned: number,
  branch: string,
  top: number,
): string {
  const fails = findings.filter((f) => f.result === "fail");
  const lines: string[] = [];
  lines.push(`# Definition / statement clarity audit — ${new Date().toISOString().slice(0, 10)}`);
  lines.push("");
  lines.push(
    `Scanner: [\`content/pipeline/definition-clarity-audit.ts\`](${blob(branch, "content/pipeline/definition-clarity-audit.ts")}). ` +
      `Skill: [\`local/definition-clarity-audit\`](${blob(branch, ".claude/skills/local/definition-clarity-audit.md")}).`,
  );
  lines.push("");
  lines.push(
    `High-recall heuristic candidates — a \`fail\` is a candidate the ` +
      `\`definition-clarity-audit\` skill confirms, not a verdict.`,
  );
  lines.push("");
  lines.push("## Summary");
  lines.push("");
  lines.push("| Criterion | pass | fail | n/a |");
  lines.push("|---|--:|--:|--:|");
  for (const c of CRITERIA) {
    const fc = findings.filter((f) => f.criterion === c);
    const p = fc.filter((f) => f.result === "pass").length;
    const fl = fc.filter((f) => f.result === "fail").length;
    const na = fc.filter((f) => f.result === "n/a").length;
    lines.push(`| \`${c}\` | ${p} | ${fl} | ${na} |`);
  }
  lines.push("");
  lines.push(`Blocks scanned: **${scanned}**. Total candidate fails: **${fails.length}**.`);
  lines.push("");
  for (const c of CRITERIA) {
    const fc = fails
      .filter((f) => f.criterion === c)
      .sort((a, b) => sevRank(b.severity) - sevRank(a.severity));
    lines.push(`## \`${c}\` — ${fc.length} candidate(s)`);
    lines.push("");
    if (!fc.length) {
      lines.push("_No candidates._");
      lines.push("");
      continue;
    }
    lines.push("| block | sev | evidence | metrics |");
    lines.push("|---|---|---|---|");
    for (const f of fc.slice(0, top)) {
      const met = Object.entries(f.metrics)
        .map(([k, v]) => `${k}=${v}`)
        .join(", ");
      lines.push(
        `| [\`${f.label}\`](${blob(branch, f.mdPath)}) | ${f.severity ?? ""} | ${f.evidence.replace(/\|/g, "\\|")} | ${met} |`,
      );
    }
    if (fc.length > top) lines.push(`| … and ${fc.length - top} more | | | |`);
    lines.push("");
  }
  return lines.join("\n") + "\n";
}

function sevRank(s?: Severity): number {
  return s === "critical" ? 3 : s === "major" ? 2 : s === "minor" ? 1 : 0;
}

// ---------------------------------------------------------------------------
// CLI
// ---------------------------------------------------------------------------

function main() {
  const argv = process.argv.slice(2);
  const roots: string[] = [];
  let jsonOut = "";
  let mdOut = "";
  let only: Criterion | undefined;
  let branch = "";
  let writeSidecars = false;
  let quiet = false;
  let top = 25;
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--json") jsonOut = argv[++i];
    else if (a === "--md") mdOut = argv[++i];
    else if (a === "--only") only = argv[++i] as Criterion;
    else if (a === "--branch") branch = argv[++i];
    else if (a === "--write-sidecars") writeSidecars = true;
    else if (a === "--quiet") quiet = true;
    else if (a === "--top") top = parseInt(argv[++i], 10);
    else if (!a.startsWith("--")) roots.push(a);
  }
  const repoRoot = execFileSync("git", ["rev-parse", "--show-toplevel"])
    .toString()
    .trim();
  if (!roots.length) roots.push(join(repoRoot, "content"));
  if (!branch) {
    try {
      branch = execFileSync("git", ["rev-parse", "--abbrev-ref", "HEAD"], {
        cwd: repoRoot,
      })
        .toString()
        .trim();
    } catch {
      branch = "main";
    }
  }
  if (only && !CRITERIA.includes(only)) {
    console.error(`unknown criterion: ${only}; choose from ${CRITERIA.join(", ")}`);
    process.exit(2);
  }

  const allFindings: Finding[] = [];
  const blocks: Block[] = [];
  for (const r of roots) {
    for (const md of walk(resolve(r))) {
      const b = loadBlock(md, repoRoot);
      if (!b) continue;
      const fs = findingsFor(b, only);
      if (fs.length) {
        blocks.push(b);
        allFindings.push(...fs);
      }
    }
  }

  if (writeSidecars) {
    const scriptHash = sha12(readFileSync(resolve(__dirname, basename(__filename)), "utf8"));
    let scriptSha = "uncommitted";
    try {
      scriptSha = execFileSync(
        "git",
        ["log", "-1", "--format=%H", "--", relative(repoRoot, __filename)],
        { cwd: repoRoot },
      )
        .toString()
        .trim() || "uncommitted";
    } catch {
      /* ignore */
    }
    const reviewedSha = headSha(repoRoot);
    const byBlock = new Map<string, Finding[]>();
    for (const f of allFindings) {
      const k = f.mdPath;
      (byBlock.get(k) ?? byBlock.set(k, []).get(k)!).push(f);
    }
    for (const b of blocks) {
      const fs = allFindings.filter((f) => f.mdPath === b.mdPath);
      writeSidecar(b, fs, scriptHash, scriptSha, reviewedSha);
    }
  }

  const fails = allFindings.filter((f) => f.result === "fail");
  if (jsonOut) {
    writeFileSync(
      resolve(jsonOut),
      JSON.stringify(
        {
          generated_at: new Date().toISOString(),
          scanned: blocks.length,
          criteria: CRITERIA,
          thresholds: T,
          findings: allFindings,
        },
        null,
        2,
      ) + "\n",
    );
  }
  if (mdOut) {
    writeFileSync(resolve(mdOut), buildMd(allFindings, blocks.length, branch, top));
  }

  if (!quiet) {
    console.log(`definition-clarity-audit: scanned ${blocks.length} block(s)`);
    for (const c of CRITERIA) {
      const fc = allFindings.filter((f) => f.criterion === c);
      const fl = fc.filter((f) => f.result === "fail").length;
      const p = fc.filter((f) => f.result === "pass").length;
      const na = fc.filter((f) => f.result === "n/a").length;
      console.log(`  ${c.padEnd(22)} pass=${p}  fail=${fl}  n/a=${na}`);
    }
    console.log(`  total candidate fails: ${fails.length}`);
    if (jsonOut) console.log(`  json -> ${jsonOut}`);
    if (mdOut) console.log(`  md   -> ${mdOut}`);
  }
  // Non-zero exit when candidates exist, so CI / pre-commit can gate on it.
  process.exit(fails.length ? 1 : 0);
}

main();
