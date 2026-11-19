#!/usr/bin/env bun
/**
 * Paper-commentary audit — fourth-wall Lean leaks, audit / agent commentary,
 * and Part-I reading-order anachronisms in paper prose.
 *
 * Paper prose (`folio/<paper>/**\/*.md`) carries mathematics and, at the
 * comparison points, physics. Formalisation links belong solely to the `.ts`
 * `lean:` metadata and rendered `∀` badge — never to reader-facing `.md` prose.
 * Prose must NOT carry:
 *
 *   commentary-lean-prose      (Class L1) fourth-wall prose mentions of Lean,
 *       `Lean 4`, `Lean carrier`, `Lean sibling`, `Lean backing`, `Lean file`,
 *       `Lean structure`, `Mathlib`, `proved formally`, `formally proved`,
 *       `formalised in`, `discharges the axiom`, `## Lean …` headings, or
 *       `**Lean.**` lead-ins.
 *
 *   commentary-lean-ident      (Class L2) backticked Lean identifiers or raw
 *       block IDs in narrative prose: Lean FQNs (`QOU.Foo.bar`, `Mathlib.…`,
 *       `CategoryTheory.…`), `.lean` filenames, Lean typeclasses/types
 *       (`CommRing`, `IsQGeneric`, `[Add H]`, `HochschildZero R A`), raw
 *       `def:foo` / `thm:bar` labels in backticks, or Lean snake_case /
 *       camelCase theorem and definition names (`dimQK0_eq_…`, `su2Character_one`).
 *
 *   commentary-formal-status   formalisation bookkeeping: "sorry-free",
 *       "axiom-free", "#print axioms", "not formalised", "self-assuming
 *       projection", "honest conjecture class", "previously proved".
 *
 *   commentary-corpus-history  the corpus narrating its own past: "earlier
 *       statements of this definition wrote …", "an earlier formulation
 *       derived …", "previously stated", "was corrected", "retracted",
 *       "superseded by", "the old wording".
 *
 *   commentary-repo-ref        repository furniture in prose: bean IDs
 *       (`qou-xxxx`), `computations/…`, `docs/audits/…`, `scripts/…`,
 *       a backticked `lean/QOU/….lean` path, PR numbers.
 *
 *   commentary-witness-ref     (ADVISORY) a `*.witness.json` pointer —
 *       provenance or bookkeeping, agent decides.
 *
 *   commentary-provenance      figure-provenance stories: "measured on
 *       2026-…", "re-measured", "at the proton pin", "precision gate",
 *       "stale witness".
 *
 *   commentary-agent           agent / session speech: "this session",
 *       "an agent", "the agent", "subagent", "we tried".
 *
 *   commentary-reading-order   (Class L4) Part-I reading-order anachronisms:
 *       premature `q` / `[n]_q` / `\Phi_d` / Hecke / `\mathrm{SU}_q(2)` /
 *       "substrate parameter" / "archimedean wall" mentions in Chapter 1
 *       (`quantum-universes`), or forward `](#label)` cross-references in
 *       Chapters 1–2 whose target block sits later in monograph reading order.
 *
 *   commentary-title-placeholder  block `.ts` manifest `title` or `caption`
 *       carrying raw label prefixes (`rem:…`, `def:…`, `prop:…`, `thm:…`,
 *       `lem:…`, `cor:…`, `conj:…`, `alg:…`, `ex:…`, `sec:…`, `ch:…`,
 *       `app:…`, `tbl:…`, `fig:…`), mechanical table-extraction placeholders
 *       (`Data table …`, `Table N from …`), or truncated titles ending in
 *       dangling articles/prepositions (`… is a`, `… from`, `… the`, etc.).
 *
 *   commentary-open-status     work-status speech about an open item
 *       ("remains open", "not discharged here", "pending … infrastructure",
 *       "is not claimed here"). EXCEPTION (owner ruling 2026-10-11): an open
 *       conjecture may carry ONE brief scholarly status/routes remark (up to
 *       BRIEF_STATUS_MAX sentences).
 *
 *   bun run folio/pipeline/paper-commentary-audit.ts [root ...] [--json] [--quiet] [--no-lean-ident] [--no-reading-order] [--no-title-placeholder]
 *
 * Exit 1 if any block has a non-advisory hit, else 0.
 */
import { existsSync, readFileSync, readdirSync, statSync } from "node:fs";
import { basename, dirname, join, relative, resolve } from "node:path";

export const BRIEF_STATUS_MAX = 3;

export interface CommentaryHit {
  criterion: string;
  line: number;
  text: string;
  /** advisory hits are reported but do not fail the block */
  advisory?: boolean;
}

/**
 * Class L1: fourth-wall Lean / Mathlib / formalisation mechanics in prose.
 * Case-sensitive `\bLean\b` avoids matching lowercase English verb "lean",
 * while structured phrases (`Lean carrier`, `Mathlib`, `proved formally`, etc.)
 * match case-insensitively.
 */
const L1_CASE_SENSITIVE_LEAN_RE = /\bLean(?:'s)?\b/;
const L1_STRUCTURED_LEAN_PROSE_RE =
  /^#{1,6}\s*Lean\b|\*\*Lean\.?\*\*|\bLean\s+(?:4\b|carrier|sibling|backing|file|module|proof|theorem|lemma|definition|declaration|structure|formalisation|formalization|implementation|companion|namespace|typeclass|code|source|verify|verification)\b|\bin\s+Lean(?:\s+4)?\b|\bMathlib\b|\bproved\s+formally\b|\bformally\s+proved\b|\bproved\s+in\s+(?:the\s+)?Lean\b|\bformali[sz]ed\s+in\b|\bdischarges?\s+the\s+axiom\b/i;

/** Class L2: backticked Lean identifiers or raw block IDs in narrative prose. */
const BACKTICK_SPAN_RE = /`([^`\n]+)`/g;
const L2_FQN_RE =
  /^(?:qou:)?(?:QOU|Mathlib|Real|Nat|Int|Rat|Finset|Matrix|Polynomial|Complex|CategoryTheory|Algebra|Ring|LinearAlgebra)\.[A-Za-z0-9_.']+$/;
const L2_LEAN_FILE_RE = /^[A-Za-z0-9_./-]+\.lean$/;
const L2_RAW_BLOCK_ID_RE =
  /^(?:def|thm|prop|lem|cor|conj|rem|ex|sec|chap|app|tab):[a-z0-9-]+$/;
const L2_LEAN_TYPE_OR_DECL_RE =
  /^(?:CommRing|Field|LinearOrderedField|IsQGeneric|Fintype|DecidableEq|Nonempty|Unique|\[[A-Z][A-Za-z0-9_ ]+\]|[A-Z][a-zA-Z0-9]+(?:\s+[A-Za-z0-9_]+)+|Is[A-Z][a-zA-Z0-9]+|[a-z][a-zA-Z0-9]*(?:_[a-zA-Z0-9]+)+|[a-z][a-z0-9]+(?:[A-Z][a-z0-9]+)+)$/;
const L2_NON_LEAN_PATH_RE = /\.(?:py|json|ts|js|md|tex|sh|yml|yaml|toml|csv|svg|png)$/i;

const L2_EXEMPT_TOKENS = new Set([
  "plain",
  "KnKp",
  "Kp3",
  "nuc11_interleaved",
  "nuc11_gen_grouped",
  "true",
  "false",
]);

export function classifyLeanIdentBacktick(rawToken: string): string | null {
  const tok = rawToken.trim();
  if (!tok || L2_EXEMPT_TOKENS.has(tok)) return null;
  if (L2_FQN_RE.test(tok)) return "lean-fqn";
  if (L2_LEAN_FILE_RE.test(tok)) return "lean-file-ref";
  if (L2_NON_LEAN_PATH_RE.test(tok)) return null;
  if (L2_RAW_BLOCK_ID_RE.test(tok)) return "raw-block-id";
  if (L2_LEAN_TYPE_OR_DECL_RE.test(tok)) return "lean-decl-or-type";
  return null;
}

const RULES: { criterion: string; re: RegExp }[] = [
  {
    criterion: "commentary-formal-status",
    re: /\bsorry[- ]free\b|\baxiom[- ]free\b|#print\s+axioms|\bnot\s+(?:yet\s+)?formali[sz]ed\b|\bself-assuming\s+projection\b|\babsent\s+from\s+Mathlib\b|\bhonest\s+conjecture\b|\bpreviously\s+proved\b/i,
  },
  {
    criterion: "commentary-corpus-history",
    re: /\bearlier\s+(?:statements?|formulations?|versions?|drafts?|wording)\b|\bpreviously\s+(?:stated|written|read|said|claimed|recorded)\b|\b(?:was|were|is)\s+(?:since\s+)?(?:corrected|retracted)\b|\bretraction\b|\bsuperseded\s+(?:by|wording|value)\b|\bold\s+wording\b|\bthis\s+(?:block|paragraph|definition)\s+(?:used\s+to|previously|once)\b/i,
  },
  {
    criterion: "commentary-repo-ref",
    re: /\bqou-[a-z0-9]{4}\b|`?\bcomputations\/|\bdocs\/(?:audits|coordination)\/|`scripts\/|`(?:\.\.\/)*lean\/QOU\/[^`]*\.lean`|\bPR\s*#\s*\d{3,}|\bbeans?\s+`|\bbean\s+[a-z0-9]{4}\b/i,
  },
  {
    criterion: "commentary-provenance",
    re: /\b(?:re-)?measured\s+(?:on|at|in)\s+20\d{2}\b|\bre-measured\b|\bprecision[- ]gate|\bstale\s+(?:witness|figure|value)\b|\bat\s+the\s+(?:proton|muon)\s+pin\b/i,
  },
  {
    criterion: "commentary-agent",
    re: /\bthis\s+session\b|\b(?:an|the)\s+agent\b|\bsub-?agents?\b|\bwe\s+tried\b|\bagent[- ]authored\b/i,
  },
];

/** Class L4a: premature post-Ch1 concepts appearing inside Chapter 1 (`quantum-universes`). */
const L4A_CH1_PREMATURE_CONCEPT_RES: { subkind: string; re: RegExp }[] = [
  { subkind: "substrate-parameter", re: /\bsubstrate\s+(?:parameter|anchor)\b/i },
  { subkind: "archimedean-wall", re: /\barchimedean\s+wall\b/i },
  { subkind: "hecke-concept", re: /\bHecke\s+(?:basis|decompositions?|algebras?|-type)\b/i },
  { subkind: "cyclotomic-Phi_d", re: /\\Phi_[0-9d]\b|\b[Cc]yclotomics?\b/ },
  { subkind: "quantum-group-SU_q", re: /\bq-deformed\b|\\mathrm\{SU\}_q\(2\)|quantum\s+groups?\s*\(\s*\$?q\s*\\neq\s*1/i },
  { subkind: "quantum-integer-bracket", re: /\[[0-9nm+ -]+\]_q\b/ },
  { subkind: "dim_q-before-q", re: /\\dim_q\b/ },
  { subkind: "laurent-ring-Z-q", re: /\\mathbb\{Z\}\[q,\s*q\^\{-1\}\]/ },
];

const MD_INTERNAL_LINK_RE = /\[([^\]]+)\]\(#([a-zA-Z0-9_:-]+)\)/g;

const WITNESS_REF_RE = /\b[\w-]+\.witness\.json\b|\bwitness-json\b/i;

const OPEN_STATUS_RE =
  /\bremains?\s+(?:genuinely\s+)?open\b|\bnot\s+discharged\s+here\b|\bpending\s+[\w-]+(?:\s+[\w-]+)?\s+infrastructure\b|\bis\s+not\s+claimed\s+here\b|\bremains?\s+to\s+be\s+(?:proved|shown|discharged)\b|\bopen\s+problem\b/i;

/** Block `.ts` `title:` / `caption:` mechanical placeholder & truncation checks. */
const TS_TITLE_OR_CAPTION_FIELD_RE =
  /\b(title|caption):\s*(?:"((?:[^"\\]|\\.)*)"|'((?:[^'\\]|\\.)*)')/g;
const TITLE_RAW_LABEL_RE =
  /\b(?:rem|def|prop|thm|lem|cor|conj|alg|ex|sec|ch|app|tbl|fig):[a-zA-Z0-9_-]*/;
const TITLE_MECH_PLACEHOLDER_RE = /\bData\s+table\b|\bTable\s+\d+\s+from\b/i;
const TITLE_DANGLING_TAIL_RE =
  /\s+(?:a|[Aa]n|[Tt]he|[Ff]rom|[Oo]f|[Ii]n|[Tt]o|[Ff]or|[Ww]ith|[Ii]s\s+a)\s*$/;

export function scanTitleOrCaptionValue(
  field: "title" | "caption",
  val: string,
  lineNo = 1,
): CommentaryHit[] {
  if (!val) return [];
  const hits: CommentaryHit[] = [];
  const rawLabel = val.match(TITLE_RAW_LABEL_RE);
  if (rawLabel) {
    hits.push({
      criterion: "commentary-title-placeholder",
      line: lineNo,
      text: `${field}-raw-label (${rawLabel[0]}): "${val.slice(0, 140)}"`,
    });
  }
  const mech = val.match(TITLE_MECH_PLACEHOLDER_RE);
  if (mech) {
    hits.push({
      criterion: "commentary-title-placeholder",
      line: lineNo,
      text: `${field}-mechanical-placeholder (${mech[0]}): "${val.slice(0, 140)}"`,
    });
  }
  const tail = val.match(TITLE_DANGLING_TAIL_RE);
  if (tail) {
    hits.push({
      criterion: "commentary-title-placeholder",
      line: lineNo,
      text: `${field}-dangling-tail ("${tail[0].trim()}"): "${val.slice(0, 140)}"`,
    });
  }
  return hits;
}

interface CleanedLine {
  /** Raw line with fences/display-math blanked, link URLs & inline math stripped, backticks preserved. */
  withBackticks: string;
  /** Prose-only line with backtick spans also stripped. */
  proseOnly: string;
  /** Raw line outside fenced code blocks (math preserved for L4a LaTeX checks). */
  rawUnfenced: string;
  inDisplayMath: boolean;
}

function prepareLines(src: string): CleanedLine[] {
  const out: CleanedLine[] = [];
  let inFence = false;
  let inDisplayMath = false;

  for (const raw of src.split("\n")) {
    const trimmed = raw.trim();
    if (/^```/.test(trimmed)) {
      inFence = !inFence;
      out.push({ withBackticks: "", proseOnly: "", rawUnfenced: "", inDisplayMath: false });
      continue;
    }
    if (inFence) {
      out.push({ withBackticks: "", proseOnly: "", rawUnfenced: "", inDisplayMath: false });
      continue;
    }
    if (trimmed === "$$") {
      inDisplayMath = !inDisplayMath;
      out.push({ withBackticks: "", proseOnly: "", rawUnfenced: "", inDisplayMath: true });
      continue;
    }
    if (inDisplayMath) {
      out.push({ withBackticks: "", proseOnly: "", rawUnfenced: raw, inDisplayMath: true });
      continue;
    }

    const withBackticks = raw
      .replace(/\{\{[^}]*\}\}/g, " ")
      .replace(/\$\$[^$]*\$\$/g, " ")
      .replace(/\$[^$]*\$/g, " ")
      .replace(/\]\([^)]*\)/g, "]");

    const proseOnly = withBackticks
      .replace(/`[^`\n]+`/g, " ")
      .replace(/:(?:refterm|defterm)\[([^\]]*)\]\{#[^}]*\}/g, "$1");

    out.push({
      withBackticks,
      proseOnly,
      rawUnfenced: raw,
      inDisplayMath: false,
    });
  }
  return out;
}

export interface ReadingOrderIndex {
  /** Global 1-based block index of the block being scanned. */
  sourceIndex: number;
  /** Map from label / raw label / block stem -> global 1-based block index. */
  labelToIndex: ReadonlyMap<string, number>;
}

export interface BlockCtx {
  /** block kind from the .ts manifest, if known */
  kind?: string;
  /** block title from the .ts manifest, if present */
  title?: string;
  /** 1-based line number of `title:` in the .ts manifest */
  titleLine?: number;
  /** block caption from the .ts manifest, if present */
  caption?: string;
  /** 1-based line number of `caption:` in the .ts manifest */
  captionLine?: number;
  /** true when the block interprets / uses a `conj:` label */
  conjectureContext?: boolean;
  /** chapter directory name (e.g. `quantum-universes`) */
  chapter?: string;
  /** block stem (e.g. `authors-note`) */
  blockName?: string;
  /** monograph reading-order index for forward-ref checking in Part I */
  readingOrder?: ReadingOrderIndex;
  /** disable Class L2 backtick identifier checks */
  skipLeanIdent?: boolean;
  /** disable Class L4 reading-order checks */
  skipReadingOrder?: boolean;
  /** disable block title/caption placeholder checks */
  skipTitlePlaceholder?: boolean;
}

export function scanCommentary(src: string, ctx: BlockCtx = {}): CommentaryHit[] {
  const prepared = prepareLines(src);
  const hits: CommentaryHit[] = [];
  const openHits: CommentaryHit[] = [];
  const isAuthorsNote =
    ctx.chapter === "introduction" && ctx.blockName === "authors-note";

  if (!ctx.skipTitlePlaceholder) {
    if (ctx.title) {
      hits.push(...scanTitleOrCaptionValue("title", ctx.title, ctx.titleLine ?? 1));
    }
    if (ctx.caption) {
      hits.push(...scanTitleOrCaptionValue("caption", ctx.caption, ctx.captionLine ?? 1));
    }
  }

  prepared.forEach((entry, i) => {
    const lineNo = i + 1;
    const { withBackticks, proseOnly, rawUnfenced, inDisplayMath } = entry;

    if (!inDisplayMath && withBackticks) {
      // Class L1: fourth-wall Lean / Mathlib prose mentions
      // Exempt `introduction/authors-note.md`, the intentional book-level formalisation
      // overview governed by `scripts/refresh-authors-note.ts`.
      if (!isAuthorsNote) {
        const mStruct = proseOnly.match(L1_STRUCTURED_LEAN_PROSE_RE);
        const mBare = proseOnly.match(L1_CASE_SENSITIVE_LEAN_RE);
        const l1Match = mStruct?.[0] ?? mBare?.[0];
        if (l1Match) {
          hits.push({ criterion: "commentary-lean-prose", line: lineNo, text: l1Match });
        }
      }

      // Class L2: backticked Lean FQNs, `.lean` files, raw block IDs, or Lean decls
      if (!ctx.skipLeanIdent) {
        for (const m of withBackticks.matchAll(BACKTICK_SPAN_RE)) {
          const kind = classifyLeanIdentBacktick(m[1] ?? "");
          if (kind !== null) {
            hits.push({
              criterion: "commentary-lean-ident",
              line: lineNo,
              text: `\`${(m[1] ?? "").trim()}\``,
            });
          }
        }
      }

      // Existing commentary rules (scanned on `withBackticks` so backticked repo paths still match)
      for (const { criterion, re } of RULES) {
        const m = withBackticks.match(re);
        if (m) hits.push({ criterion, line: lineNo, text: m[0] });
      }

      const w = withBackticks.match(WITNESS_REF_RE);
      if (w) {
        hits.push({
          criterion: "commentary-witness-ref",
          line: lineNo,
          text: w[0],
          advisory: true,
        });
      }

      for (const sentence of proseOnly.split(/(?<=[.;])\s+/)) {
        const m = sentence.match(OPEN_STATUS_RE);
        if (m) openHits.push({ criterion: "commentary-open-status", line: lineNo, text: m[0] });
      }
    }

    // Class L4: Part-I reading-order anachronisms (Ch 1 premature concepts + Ch 1-2 forward refs)
    if (!ctx.skipReadingOrder && rawUnfenced) {
      if (ctx.chapter === "quantum-universes") {
        for (const { subkind, re } of L4A_CH1_PREMATURE_CONCEPT_RES) {
          const m4a = rawUnfenced.match(re);
          if (m4a) {
            hits.push({
              criterion: "commentary-reading-order",
              line: lineNo,
              text: `${subkind}: ${m4a[0]}`,
            });
          }
        }
      }

      if (
        ctx.readingOrder &&
        (ctx.chapter === "quantum-universes" || ctx.chapter === "quantum-observable-universes")
      ) {
        const { sourceIndex, labelToIndex } = ctx.readingOrder;
        for (const m4b of rawUnfenced.matchAll(MD_INTERNAL_LINK_RE)) {
          const linkText = m4b[1] ?? "";
          const targetLabel = m4b[2] ?? "";
          const targetIdx = labelToIndex.get(targetLabel);
          if (targetIdx !== undefined && targetIdx > sourceIndex) {
            hits.push({
              criterion: "commentary-reading-order",
              line: lineNo,
              text: `forward-ref [${linkText}](#${targetLabel})`,
            });
          }
        }
      }
    }
  });

  const inConj = ctx.kind === "conjecture" || ctx.conjectureContext === true;
  if (openHits.length > BRIEF_STATUS_MAX) hits.push(...openHits);
  else if (!inConj) hits.push(...openHits.map((h) => ({ ...h, advisory: true })));
  return hits;
}

// ── Monograph Reading-Order Indexer (for Part-I forward-ref detection) ──────

const KIND_PREFIX: Record<string, string> = {
  definition: "def",
  theorem: "thm",
  proposition: "prop",
  lemma: "lem",
  corollary: "cor",
  conjecture: "conj",
  remark: "rem",
  example: "ex",
  table: "tab",
};

interface MonographOrderCache {
  labelToIndex: Map<string, number>;
  mdPathToIndex: Map<string, number>;
}

const monographCache = new Map<string, MonographOrderCache | null>();

function findPaperDirForMd(mdAbsPath: string): string | null {
  let d = dirname(mdAbsPath);
  for (let depth = 0; depth < 4; depth++) {
    const base = basename(d);
    const candidateManifest = join(d, `${base}.ts`);
    if (existsSync(candidateManifest)) {
      const txt = readFileSync(candidateManifest, "utf8");
      if (/\bexport\s+default\s+paper\s*\(/.test(txt)) return d;
    }
    const parent = dirname(d);
    if (parent === d) break;
    d = parent;
  }
  return null;
}

function getMonographOrder(paperDir: string): MonographOrderCache | null {
  if (monographCache.has(paperDir)) return monographCache.get(paperDir)!;
  const manifestPath = join(paperDir, `${basename(paperDir)}.ts`);
  if (!existsSync(manifestPath)) {
    monographCache.set(paperDir, null);
    return null;
  }
  const paperSrc = readFileSync(manifestPath, "utf8");
  const chapterDirs = [...paperSrc.matchAll(/chapterRef\(\{\s*dir:\s*"([^"]+)"/g)].map(
    (m) => m[1]!,
  );
  if (chapterDirs.length === 0) {
    monographCache.set(paperDir, null);
    return null;
  }

  const labelToIndex = new Map<string, number>();
  const mdPathToIndex = new Map<string, number>();
  let globalIdx = 0;

  for (const chDir of chapterDirs) {
    const chTsPath = join(paperDir, chDir, `${chDir}.ts`);
    if (!existsSync(chTsPath)) continue;
    const chSrc = readFileSync(chTsPath, "utf8").replace(/\/\/[^\n]*/g, "");
    const blocks: string[] = [];
    for (const arrMatch of chSrc.matchAll(/blocks:\s*\[([^\]]*)\]/gs)) {
      for (const sMatch of (arrMatch[1] ?? "").matchAll(/"([a-zA-Z0-9_-]+)"/g)) {
        const bName = sMatch[1]!;
        if (!blocks.includes(bName)) blocks.push(bName);
      }
    }
    for (const bName of blocks) {
      globalIdx++;
      const mdAbs = resolve(paperDir, chDir, `${bName}.md`);
      mdPathToIndex.set(mdAbs, globalIdx);
      const bTsPath = join(paperDir, chDir, `${bName}.ts`);
      if (existsSync(bTsPath)) {
        const bSrc = readFileSync(bTsPath, "utf8");
        const m = bSrc.match(
          /export\s+default\s+(definition|theorem|proposition|lemma|corollary|conjecture|remark|example|proof|prose|table)\s*\(\s*\{[\s\S]*?\blabel:\s*"([^"]+)"/,
        );
        if (m) {
          const kind = m[1]!;
          const rawLabel = m[2]!;
          const fullLabel = rawLabel.includes(":")
            ? rawLabel
            : KIND_PREFIX[kind]
              ? `${KIND_PREFIX[kind]}:${rawLabel}`
              : rawLabel;
          labelToIndex.set(fullLabel, globalIdx);
          labelToIndex.set(rawLabel, globalIdx);
        }
      }
      if (!labelToIndex.has(bName)) labelToIndex.set(bName, globalIdx);
    }
  }

  const built = { labelToIndex, mdPathToIndex };
  monographCache.set(paperDir, built);
  return built;
}

function blockCtx(
  mdPath: string,
  opts: {
    skipLeanIdent?: boolean;
    skipReadingOrder?: boolean;
    skipTitlePlaceholder?: boolean;
  } = {},
): BlockCtx {
  const absMd = resolve(mdPath);
  const chapter = basename(dirname(absMd));
  const paperDir = findPaperDirForMd(absMd);
  const order = paperDir ? getMonographOrder(paperDir) : null;
  const sourceIdx = order?.mdPathToIndex.get(absMd);

  const tsPath = absMd.replace(/\.md$/, ".ts");
  let kind: string | undefined;
  let title: string | undefined;
  let titleLine: number | undefined;
  let caption: string | undefined;
  let captionLine: number | undefined;
  let conjectureContext = false;
  if (existsSync(tsPath)) {
    const ts = readFileSync(tsPath, "utf8");
    kind =
      ts.match(/\bkind:\s*"([a-z]+)"/)?.[1] ??
      ts.match(/export default\s+([a-z]+)\s*\(/)?.[1];
    const interp = ts.match(/interprets:\s*"([^"]+)"/)?.[1] ?? "";
    const label = ts.match(/label:\s*"([^"]+)"/)?.[1] ?? "";
    conjectureContext = interp.startsWith("conj:") || label.startsWith("conj:");
    for (const m of ts.matchAll(TS_TITLE_OR_CAPTION_FIELD_RE)) {
      const fld = m[1];
      const val = m[2] ?? m[3] ?? "";
      const ln = ts.slice(0, m.index ?? 0).split("\n").length;
      if (fld === "title" && title === undefined) {
        title = val;
        titleLine = ln;
      } else if (fld === "caption" && caption === undefined) {
        caption = val;
        captionLine = ln;
      }
    }
  }

  return {
    kind,
    title,
    titleLine,
    caption,
    captionLine,
    conjectureContext,
    chapter,
    blockName: basename(absMd, ".md"),
    readingOrder:
      order && sourceIdx !== undefined
        ? { sourceIndex: sourceIdx, labelToIndex: order.labelToIndex }
        : undefined,
    skipLeanIdent: opts.skipLeanIdent,
    skipReadingOrder: opts.skipReadingOrder,
    skipTitlePlaceholder: opts.skipTitlePlaceholder,
  };
}

/**
 * Directories skipped during recursive paper-root walks:
 * - `lean`, `rendered`, `latex`, `computations`, `audit`: non-prose / build / probe trees
 * - `index-of-definitions`, `glossary`: back-matter reference indices whose explicit
 *   purpose is mapping monograph labels/terms to Lean/Mathlib identifiers.
 */
const SKIP_WALK_DIRS = new Set([
  "lean",
  "rendered",
  "latex",
  "computations",
  "audit",
  "index-of-definitions",
  "glossary",
]);

function walk(p: string, out: string[], isExplicitRoot = false) {
  if (statSync(p).isDirectory()) {
    const dirName = basename(p);
    if (!isExplicitRoot && (SKIP_WALK_DIRS.has(dirName) || dirName.startsWith("."))) return;
    for (const e of readdirSync(p).sort()) {
      if (e.startsWith(".")) continue;
      walk(join(p, e), out, false);
    }
  } else if (p.endsWith(".md")) {
    out.push(p);
  }
}

if (import.meta.main) {
  const args = process.argv.slice(2);
  const json = args.includes("--json");
  const quiet = args.includes("--quiet");
  const skipLeanIdent = args.includes("--no-lean-ident");
  const skipReadingOrder = args.includes("--no-reading-order");
  const skipTitlePlaceholder = args.includes("--no-title-placeholder");
  const roots = args.filter((a) => !a.startsWith("--"));
  if (roots.length === 0) roots.push("folio/quantum-observable-universe");

  const files: string[] = [];
  for (const r of roots) walk(resolve(r), files, true);

  const report: { file: string; hits: CommentaryHit[] }[] = [];
  const countsByCriterion: Record<string, number> = {};
  let failing = 0;

  for (const f of files) {
    const hits = scanCommentary(
      readFileSync(f, "utf8"),
      blockCtx(f, { skipLeanIdent, skipReadingOrder, skipTitlePlaceholder }),
    );
    const nonAdvisory = hits.filter((h) => !h.advisory);
    if (nonAdvisory.length > 0) failing++;
    for (const h of nonAdvisory) {
      countsByCriterion[h.criterion] = (countsByCriterion[h.criterion] ?? 0) + 1;
    }
    if (hits.length) report.push({ file: relative(process.cwd(), f), hits });
  }

  if (json) {
    console.log(
      JSON.stringify(
        { scanned: files.length, failing, countsByCriterion, report },
        null,
        2,
      ),
    );
  } else {
    if (!quiet) {
      for (const r of report) {
        for (const h of r.hits) {
          console.log(
            `${r.file}:${h.line}  [${h.criterion}${h.advisory ? " (advisory)" : ""}]  ${h.text}`,
          );
        }
      }
    }
    const breakdown = Object.entries(countsByCriterion)
      .sort(([a], [b]) => a.localeCompare(b))
      .map(([k, v]) => `${k}=${v}`)
      .join(", ");
    console.log(
      `paper-commentary-audit: ${failing} of ${files.length} block(s) fail; ${report.length - failing} advisory-only${breakdown ? ` (${breakdown})` : ""}`,
    );
  }
  process.exit(failing ? 1 : 0);
}
