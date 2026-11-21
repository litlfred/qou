#!/usr/bin/env bun
/**
 * Voice-leak audit — the four leak classes of epic `qou-d4kh` (bean V1
 * `qou-9aar`) that `paper-commentary-audit.ts` and the platform voice
 * checkers do not see.
 *
 *   leak-lean-prose (L1)     prose that talks about the formalisation:
 *       "Lean", "Lean sibling/carrier/structure", "Mathlib", "proved
 *       formally", "formalised in", "discharges the axiom", a `## Lean …`
 *       heading. Backticked spans are removed first (those are L2).
 *
 *   leak-lean-ident (L2)     a backticked code span in prose that is a Lean
 *       or repository identifier. Sub-kinds: `fqn` (`QOU.…`, `Mathlib.…`),
 *       `lean-file` (`Foo.lean`), `repo-file` (`.py/.ts/.json`),
 *       `block-id` (`def:foo`), `decl-name` (snake_case or camelCase
 *       declaration-shaped names), `typeclass` (`CommRing`, `IsQGeneric`,
 *       `HochschildZero R A`, `[Add H]`). The platform checker strips every
 *       backtick span before scanning (`qa-checkers-voice.ts`
 *       `stripInlineCode`), so none of these were ever examined.
 *
 *   leak-person (L3)         first/second person: we, our, us, let's,
 *       let us, you, your. "I" is NOT matched (Part I, Type I, …).
 *
 *   leak-reading-order (L4)  (L4a) a `q`-dependent token (`$q$`, `[n]_q`,
 *       `\Phi_d`, `SU_q`, Hecke, "archimedean wall") in a block read before
 *       the first block of `sec:substrate-parameter`, where `q` is
 *       introduced (fails in Chapter 1, advisory in Chapter 2 §1-6, where
 *       `q` appears as the parameter of the q-operators; an `outro-*`
 *       block and the introduction may preview);
 *       (L4b) a `](#label)` link to a block later in reading
 *       order. L4b is failing only in the Part I chapters listed in
 *       PART_I_STRICT and ADVISORY elsewhere: a forward reference is
 *       ordinary in a monograph; the owner's audit asked for none in the
 *       foundations.
 *
 * High-recall / agent-confirmed: a hit is a candidate. Fenced code is
 * skipped everywhere; inline math is removed for L1-L3 (L4a reads math).
 *
 *   bun run folio/pipeline/voice-leak-audit.ts [--json] [--quiet] [--class L1,L2,L3,L4]
 *
 * Exit 1 if any non-advisory hit, else 0.
 */
import { existsSync, readFileSync } from "node:fs";
import { join, relative } from "node:path";

export type LeakClass = "L1" | "L2" | "L3" | "L4";
export interface LeakHit {
  cls: LeakClass;
  criterion: string;
  sub: string;
  line: number;
  text: string;
  advisory?: boolean;
}

export const PART_I_STRICT = new Set(["quantum-universes", "quantum-observable-universes"]);
/** Chapter where a premature `q` token fails; elsewhere before the intro it is advisory. */
export const Q_STRICT_CHAPTER = "quantum-universes";
export const Q_INTRO_SECTION = "sec:substrate-parameter";
/** Back matter a forward link may always point to. */
export const BACK_MATTER = new Set(["glossary", "notation", "index-of-definitions"]);
/**
 * Owner rulings 2026-11-20 (second [W14 ask] on #8526, answers 1b / 2a / 3a):
 * - CODE_BY_DESIGN: chapters whose subject IS the formalisation or the code.
 *   `appendix-mass-binding-algorithms` is the propositions <-> Python-API
 *   contract (AGENTS.md); `appendix-formalisation-notes` holds the Lean and
 *   Mathlib infrastructure blocks moved out of the chapters. L1 and L2 are not
 *   checked there; L3 and L4 still are.
 * - REFERENCE_TABLES: in the reference chapters, a Mathlib name or a
 *   declaration in a TABLE ROW is the reference content and is exempt from
 *   L2; their prose is still checked.
 */
export const CODE_BY_DESIGN = new Set(["appendix-mass-binding-algorithms", "appendix-formalisation-notes"]);
export const REFERENCE_TABLES = new Set(["glossary", "notation", "index-of-definitions"]);

// ── line preparation ────────────────────────────────────────────────
/** Fenced code blanked; returns raw (math kept) lines. */
function unfence(src: string): string[] {
  let inFence = false;
  return src.split("\n").map((raw) => {
    if (/^\s*(```|~~~)/.test(raw)) {
      inFence = !inFence;
      return "";
    }
    return inFence ? "" : raw;
  });
}
/** Remove display/inline math and the target half of links. */
function stripMath(l: string): string {
  return l.replace(/\$\$[^$]*\$\$/g, " ").replace(/\$[^$]*\$/g, " ").replace(/\]\([^)]*\)/g, "]");
}
const BACKTICK_RE = /`([^`\n]+)`/g;
function stripCode(l: string): string {
  return l.replace(BACKTICK_RE, " ");
}
/** Remove remark-directive wrappers' slug part: :refterm[Text]{#slug}. */
function stripDirectives(l: string): string {
  return l.replace(/\{#[^}]*\}/g, " ");
}

// ── L1 ──────────────────────────────────────────────────────────────
const L1_RES: { sub: string; re: RegExp }[] = [
  { sub: "lean-heading", re: /^#{1,6}\s*Lean\b/ },
  { sub: "lean-word", re: /\bLean(?:'s)?\b/ },
  { sub: "mathlib", re: /\bMathlib\b/ },
  { sub: "formally", re: /\b(?:proved|proven|verified|checked|stated)\s+formally\b|\bformally\s+(?:proved|proven|verified|checked)\b/i },
  { sub: "formalised-in", re: /\bformali[sz](?:ed|ation)\s+(?:in|of|as)\b/i },
  { sub: "discharges-axiom", re: /\bdischarges?\s+the\s+(?:axiom|hypothes[ie]s|field)/i },
  { sub: "formalise", re: /\bformali[sz](?:e|es|ed|ing|ation|ations)\b/i },
  { sub: "proof-assistant", re: /\bproof\s+assistant\b|\bkernel[- ]checked\b|\bmachine[- ]checked\b/i },
];

// ── L2 ──────────────────────────────────────────────────────────────
const LEAN_TYPES = new Set(
  ("CommRing Ring Field Semiring CommSemiring Fintype Finset DecidableEq Module Algebra Monoid " +
    "CommMonoid Group CommGroup AddCommGroup AddGroup Add Mul Category MonoidalCategory " +
    "BraidedCategory SymmetricCategory RigidCategory Prop Type Sort Nat Int Rat Real Complex " +
    "Matrix Polynomial LaurentPolynomial LinearMap IsUnit IsDomain Subsingleton Nontrivial " +
    "Functor Equiv Fin Set List Multiset Bool Inhabited Unique Units NoZeroDivisors CharZero " +
    "LinearOrder StarRing TopologicalSpace MetricSpace NormedField IsAlgClosed").split(/\s+/),
);
export function classifyCode(span: string): string | null {
  const s = span.trim();
  if (!s || /[$\\]/.test(s)) return null; // TeX in code: not an identifier
  if (/^(?:def|thm|lem|prop|cor|conj|rem|ex|sim|sec|chap|app|eq|fig|tab|alg|defn|obs):[\w.:-]+$/.test(s)) return "block-id";
  if (/\.lean\b/.test(s)) return "lean-file";
  if (/^(?:QOU|Mathlib|UGB|Fred2005|CategoryTheory)\.[\w.'₀-₉]+/.test(s)) return "fqn";
  if (/\.(?:py|ts|json|md|sh|toml)\b/.test(s) || /^(?:computations|scripts|tools|folio|docs)\//.test(s)) return "repo-file";
  if (/^\[[A-Z][\w']*(?:\s+[\w'.]+)*\]$/.test(s)) return "typeclass";
  const head = s.split(/\s+/)[0]!;
  if (LEAN_TYPES.has(head) && /^[A-Z][\w']*(?:\s+[\w'.()]+)*$/.test(s)) return "typeclass";
  if (/^[A-Z][a-z0-9]+(?:[A-Z][A-Za-z0-9]*)+(?:\s+[\w'.]+)*$/.test(s)) return "typeclass"; // IsQGeneric, HochschildZero R A
  if (/^[A-Za-z][A-Za-z0-9']*(?:\.[A-Za-z][\w']*)+$/.test(s) && /[a-z]/.test(s)) return "fqn"; // Foo.bar_baz
  if (/^[A-Za-z][A-Za-z0-9']*(?:_[A-Za-z0-9']+)+$/.test(s)) return "decl-name";
  if (/^[a-z][a-z0-9]*[A-Z][A-Za-z0-9']*$/.test(s)) return "decl-name";
  return null;
}

// ── L3 ──────────────────────────────────────────────────────────────
// A quotation is the quoted author's voice, not the paper's: "we" inside
// "..." or “...” is not a person leak (measured 2026-11-21: all 7 L3 hits
// left on main were Einstein, Heisenberg and Wigner quotations).
const QUOTE_RE = /"[^"\n]*"|“[^”\n]*”/g;
export function stripQuotes(l: string): string {
  return l.replace(QUOTE_RE, " ");
}

const L3_RE = /\b(?:[Ww]e|[Oo]ur|[Oo]urs|[Oo]urselves|us|[Ll]et's|[Ll]et\s+us|[Yy]ou|[Yy]our|[Yy]ours|[Yy]ourself|the\s+reader)\b/g;

// ── L4a ─────────────────────────────────────────────────────────────
const Q_TOKEN_RES: { sub: string; re: RegExp }[] = [
  { sub: "q-integer", re: /\[[^\]$]{1,12}\]_\{?q\b/ },
  { sub: "cyclotomic", re: /\\Phi_\{?d\b|\\Phi_\{?[0-9]/ },
  { sub: "su_q", re: /SU\}?_\{?q\b|\\mathrm\{SU\}_q|U_q\(/ },
  { sub: "hecke", re: /\bHecke\b/ },
  { sub: "archimedean-wall", re: /archimedean wall/i },
  { sub: "q-symbol", re: /\$[^$]*(?<![\\A-Za-z])q(?![A-Za-z])[^$]*\$|\bq-(?:deform|integer|analog|number)/ },
];

export function scanText(src: string, opts: { premature?: boolean; prematureAdvisory?: boolean } = {}): LeakHit[] {
  const hits: LeakHit[] = [];
  unfence(src).forEach((raw, i) => {
    const line = i + 1;
    const noMath = stripDirectives(stripMath(raw));
    const prose = stripCode(noMath);
    for (const { sub, re } of L1_RES) {
      const m = prose.match(re);
      // "formalise" is also ordinary mathematical English ("this formalises
      // faster-than-viscous growth"): measured 16/20 on a sample, so it is
      // advisory; every other L1 form measured 30/30 and fails.
      if (m) { hits.push({ cls: "L1", criterion: "leak-lean-prose", sub, line, text: m[0], advisory: sub === "formalise" }); break; }
    }
    for (const m of noMath.matchAll(BACKTICK_RE)) {
      const sub = classifyCode(m[1]!);
      if (sub) hits.push({ cls: "L2", criterion: "leak-lean-ident", sub, line, text: m[0] });
    }
    for (const m of stripQuotes(prose).matchAll(L3_RE))
      hits.push({ cls: "L3", criterion: "leak-person", sub: m[0].toLowerCase().replace(/\s+/g, " "), line, text: m[0] });
    if (opts.premature)
      for (const { sub, re } of Q_TOKEN_RES) {
        const m = raw.match(re);
        if (m) { hits.push({ cls: "L4", criterion: "leak-reading-order", sub: `premature-${sub}`, line, text: m[0].slice(0, 60), advisory: opts.prematureAdvisory }); break; }
      }
  });
  return hits;
}

// ── reading order ───────────────────────────────────────────────────
export interface BlockRec {
  idx: number;
  chapter: string;
  section: string;
  name: string;
  md: string;
  label?: string;
}
function collect(node: any, chapter: string, section: string, base: string, out: BlockRec[]) {
  if (!node || typeof node !== "object") return;
  const sec = typeof node.label === "string" && node.label.startsWith("sec:") ? node.label : section;
  if (Array.isArray(node.blocks))
    for (const b of node.blocks) {
      const name = typeof b === "string" ? b : b?.ref ?? b?.name ?? b?.id;
      if (typeof name !== "string") continue;
      out.push({ idx: out.length, chapter, section: sec, name, md: join(base, `${name}.md`) });
    }
  for (const k of ["sections", "subsections", "children"]) if (Array.isArray(node[k])) for (const c of node[k]) collect(c, chapter, sec, base, out);
}
export async function readingOrder(paperDir: string): Promise<BlockRec[]> {
  const paperName = paperDir.split("/").filter(Boolean).pop()!;
  const paper: any = (await import(join(process.cwd(), paperDir, `${paperName}.ts`))).default;
  const out: BlockRec[] = [];
  for (const c of paper.chapters) {
    const dir = c.dir ?? c.uri;
    const base = join(paperDir, dir);
    const chPath = join(process.cwd(), base, `${dir}.ts`);
    if (!existsSync(chPath)) continue;
    collect((await import(chPath)).default, dir, "", base, out);
  }
  for (const b of out) {
    const ts = b.md.replace(/\.md$/, ".ts");
    if (existsSync(ts)) b.label = readFileSync(ts, "utf8").match(/\blabel:\s*"([^"]+)"/)?.[1];
  }
  return out;
}

const LINK_RE = /\]\(#([^)\s]+)\)/g;
export interface FileReport { file: string; chapter: string; hits: LeakHit[] }

export async function audit(paperDir: string, classes: Set<LeakClass>): Promise<{ scanned: number; reports: FileReport[] }> {
  const order = await readingOrder(paperDir);
  const labelIdx = new Map<string, number>();
  for (const b of order) if (b.label && !labelIdx.has(b.label)) labelIdx.set(b.label, b.idx);
  // An index row reproduces another block's title. A title from a
  // CODE_BY_DESIGN chapter is checked (and exempt) at its source, so the
  // copy in a reference table inherits that exemption; the paper's own
  // reference-table prose is still checked.
  const codeLabels = new Set(order.filter((b) => b.label && CODE_BY_DESIGN.has(b.chapter)).map((b) => b.label!));
  const rowFromCodeChapter = (l: string) => {
    const m = /^\s*\|\s*\[[^\]]*\]\(#([^)\s]+)\)/.exec(l);
    return !!m && codeLabels.has(m[1]!);
  };
  const qIntro = order.find((b) => b.section === Q_INTRO_SECTION)?.idx ?? Infinity;
  const reports: FileReport[] = [];
  let scanned = 0;
  for (const b of order) {
    if (!existsSync(b.md)) continue;
    scanned++;
    const src = readFileSync(b.md, "utf8");
    // An outro may name what the next chapter introduces.
    const premature = b.idx < qIntro && PART_I_STRICT.has(b.chapter) && !b.name.startsWith("outro-");
    const srcLines = src.split("\n");
    let hits = scanText(src, { premature, prematureAdvisory: b.chapter !== Q_STRICT_CHAPTER })
      .filter((h) => classes.has(h.cls))
      .filter((h) => !(CODE_BY_DESIGN.has(b.chapter) && (h.cls === "L1" || h.cls === "L2")))
      .filter((h) => !(REFERENCE_TABLES.has(b.chapter) && h.cls === "L2" && /^\s*\|/.test(srcLines[h.line - 1] ?? "")))
      .filter((h) => !(REFERENCE_TABLES.has(b.chapter) && (h.cls === "L1" || h.cls === "L2") && rowFromCodeChapter(srcLines[h.line - 1] ?? "")));
    if (classes.has("L4"))
      unfence(src).forEach((raw, i) => {
        for (const m of raw.matchAll(LINK_RE)) {
          const t = labelIdx.get(m[1]!);
          if (t === undefined || t <= b.idx) continue;
          const tb = order[t]!;
          // back matter, and a block's own table/data sibling, are not anachronisms
          if (BACK_MATTER.has(tb.chapter) || tb.name.startsWith(b.name)) continue;
          hits.push({
            cls: "L4", criterion: "leak-reading-order",
            sub: tb.chapter !== b.chapter ? "forward-link-cross-chapter"
              : tb.section !== b.section ? "forward-link-later-section" : "forward-link-same-section",
            line: i + 1, text: m[1]!,
            advisory: !PART_I_STRICT.has(b.chapter),
          });
        }
      });
    if (hits.length) reports.push({ file: relative(process.cwd(), b.md), chapter: b.chapter, hits });
  }
  return { scanned, reports };
}

if (import.meta.main) {
  const args = process.argv.slice(2);
  const json = args.includes("--json");
  const quiet = args.includes("--quiet");
  const ci = args.indexOf("--class");
  const classes = new Set<LeakClass>(
    (ci >= 0 ? args[ci + 1]! : "L1,L2,L3,L4").split(",") as LeakClass[],
  );
  const paperDir = args.find((a, i) => !a.startsWith("--") && args[i - 1] !== "--class") ?? "folio/quantum-observable-universe";
  const { scanned, reports } = await audit(paperDir, classes);
  const failing = reports.filter((r) => r.hits.some((h) => !h.advisory)).length;
  if (json) console.log(JSON.stringify({ scanned, failing, reports }, null, 2));
  else {
    if (!quiet) for (const r of reports) for (const h of r.hits)
      console.log(`${r.file}:${h.line}  [${h.cls} ${h.sub}${h.advisory ? " (advisory)" : ""}]  ${h.text}`);
    const by: Record<string, number> = {};
    for (const r of reports) for (const h of r.hits) if (!h.advisory) by[h.cls] = (by[h.cls] ?? 0) + 1;
    console.log(`voice-leak-audit: ${failing} of ${scanned} block(s) fail; hits ${JSON.stringify(by)}`);
  }
  process.exit(failing ? 1 : 0);
}
