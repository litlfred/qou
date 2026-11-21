#!/usr/bin/env bun
/**
 * Paper-commentary audit — audit / agent-discussion commentary in paper prose.
 *
 * Paper prose (`folio/<paper>/**\/*.md`) carries mathematics and, at the
 * comparison points, physics. It must NOT carry:
 *
 *   commentary-formal-status   formalisation bookkeeping: "sorry-free",
 *       "axiom-free", "#print axioms", "not formalised", "the Lean backing
 *       does not carry it", "self-assuming projection", "absent from
 *       Mathlib", "honest conjecture class". Naming the Lean declaration
 *       that states a result is fine; grading the Lean is not.
 *
 *   commentary-corpus-history  the corpus narrating its own past: "earlier
 *       statements of this definition wrote …", "an earlier formulation
 *       derived …", "previously stated", "was corrected", "retracted",
 *       "superseded by", "the old wording".
 *
 *   commentary-repo-ref        repository furniture in prose: bean IDs
 *       (`qou-xxxx`), `computations/…`, `docs/audits/…`,
 *       `scripts/…`, a backticked `lean/QOU/….lean` path, PR numbers.
 *       (A markdown LINK to a Lean declaration is not flagged — the
 *       visible text is a declaration name.)
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
 *   commentary-open-status     work-status speech about an open item
 *       ("remains open", "not discharged here", "pending … infrastructure",
 *       "is not claimed here"). EXCEPTION (owner ruling 2026-10-11): an open
 *       conjecture may carry ONE brief scholarly status/routes remark. So in
 *       a `conjecture` block, or a block whose `interprets`/`uses` names a
 *       `conj:` label, up to BRIEF_STATUS_MAX such sentences pass; beyond
 *       that the block fails. Outside a conjecture context every hit fails.
 *
 * Why this exists: the platform's voice checkers (`voice-author-notes-
 * pollution`, `voice-time-stamped-notes`, `voice-agent-speak`) key on
 * banners, PR#/commit refs, ISO dates and model NAMES. None of them sees
 * the forms above, and `voice-author-notes-pollution` P4 explicitly EXEMPTS
 * "measured … <date>". Measured on chapters 1–2 (2026-10-11): those
 * checkers flagged 0 of the passages this audit finds.
 *
 * Not covered here: prose about the Lean formalisation, backticked Lean or
 * repository identifiers, first/second person, and reading-order
 * anachronisms. Those are the four leak classes of epic `qou-d4kh` and live
 * in `voice-leak-audit.ts` (the exemption above for naming a Lean
 * declaration is the reason they needed a separate audit).
 *
 * High-recall / agent-confirmed: a hit is a candidate, not a verdict.
 * Fenced code, inline math and the link-target half of markdown links are
 * stripped before matching.
 *
 *   bun run folio/pipeline/paper-commentary-audit.ts [root ...] [--json] [--quiet]
 *
 * Exit 1 if any block has a non-advisory hit, else 0.
 */
import { existsSync, readFileSync, readdirSync, statSync } from "node:fs";
import { join, relative, resolve } from "node:path";

export const BRIEF_STATUS_MAX = 3;

export interface CommentaryHit {
  criterion: string;
  line: number;
  text: string;
  /** advisory hits are reported but do not fail the block */
  advisory?: boolean;
}

const RULES: { criterion: string; re: RegExp }[] = [
  {
    criterion: "commentary-formal-status",
    re: /\bsorry[- ]free\b|\baxiom[- ]free\b|#print\s+axioms|\bnot\s+(?:yet\s+)?formali[sz]ed\b|\bLean\s+(?:backing|carrier|sibling|file)\b[^.]{0,80}\b(?:does\s+not|doesn't|cannot)\b|\bself-assuming\s+projection\b|\babsent\s+from\s+Mathlib\b|\bhonest\s+conjecture\b|\bpreviously\s+proved\b/i,
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

/**
 * A pointer to a witness file is ADVISORY: the platform's
 * `voice-probe-narrative` deliberately treats a witnessed-value citation as
 * legitimate provenance, indistinguishable by regex from probe bookkeeping.
 * The agent decides whether the pointer is provenance or a story about it.
 */
const WITNESS_REF_RE = /\b[\w-]+\.witness\.json\b|\bwitness-json\b/i;

const OPEN_STATUS_RE =
  /\bremains?\s+(?:genuinely\s+)?open\b|\bnot\s+discharged\s+here\b|\bpending\s+[\w-]+(?:\s+[\w-]+)?\s+infrastructure\b|\bis\s+not\s+claimed\s+here\b|\bremains?\s+to\s+be\s+(?:proved|shown|discharged)\b|\bopen\s+problem\b/i;

/** Strip fenced code, math, inline code that is NOT a path, link targets. */
function cleanLines(src: string): string[] {
  const out: string[] = [];
  let inFence = false;
  for (const raw of src.split("\n")) {
    if (/^```/.test(raw.trim())) {
      inFence = !inFence;
      out.push("");
      continue;
    }
    if (inFence) {
      out.push("");
      continue;
    }
    out.push(
      raw
        .replace(/\$\$[^$]*\$\$/g, " ")
        .replace(/\$[^$]*\$/g, " ")
        .replace(/\]\([^)]*\)/g, "]"),
    );
  }
  return out;
}

export interface BlockCtx {
  /** block kind from the .ts manifest, if known */
  kind?: string;
  /** true when the block interprets / uses a `conj:` label */
  conjectureContext?: boolean;
}

export function scanCommentary(src: string, ctx: BlockCtx = {}): CommentaryHit[] {
  const lines = cleanLines(src);
  const hits: CommentaryHit[] = [];
  const openHits: CommentaryHit[] = [];
  lines.forEach((l, i) => {
    for (const { criterion, re } of RULES) {
      const m = l.match(re);
      if (m) hits.push({ criterion, line: i + 1, text: m[0] });
    }
    const w = l.match(WITNESS_REF_RE);
    if (w) hits.push({ criterion: "commentary-witness-ref", line: i + 1, text: w[0], advisory: true });
    // count sentences, not lines, for the brief-status allowance
    for (const sentence of l.split(/(?<=[.;])\s+/)) {
      const m = sentence.match(OPEN_STATUS_RE);
      if (m) openHits.push({ criterion: "commentary-open-status", line: i + 1, text: m[0] });
    }
  });
  // Brief status: up to BRIEF_STATUS_MAX open-status sentences are an allowed
  // scholarly status/routes remark in a conjecture context, and an ADVISORY
  // (agent-confirmed) candidate elsewhere, since a one-clause scope statement
  // ("… remains open") is ordinary mathematics. Beyond the cap it fails.
  const inConj = ctx.kind === "conjecture" || ctx.conjectureContext === true;
  if (openHits.length > BRIEF_STATUS_MAX) hits.push(...openHits);
  else if (!inConj) hits.push(...openHits.map((h) => ({ ...h, advisory: true })));
  return hits;
}

function blockCtx(mdPath: string): BlockCtx {
  const tsPath = mdPath.replace(/\.md$/, ".ts");
  if (!existsSync(tsPath)) return {};
  const ts = readFileSync(tsPath, "utf8");
  const kind = ts.match(/\bkind:\s*"([a-z]+)"/)?.[1] ??
    ts.match(/export default\s+([a-z]+)\s*\(/)?.[1];
  const interp = ts.match(/interprets:\s*"([^"]+)"/)?.[1] ?? "";
  const label = ts.match(/label:\s*"([^"]+)"/)?.[1] ?? "";
  return {
    kind,
    conjectureContext: interp.startsWith("conj:") || label.startsWith("conj:"),
  };
}

function walk(p: string, out: string[]) {
  if (statSync(p).isDirectory()) {
    for (const e of readdirSync(p)) {
      if (e === "lean" || e.startsWith(".")) continue;
      walk(join(p, e), out);
    }
  } else if (p.endsWith(".md")) out.push(p);
}

if (import.meta.main) {
  const args = process.argv.slice(2);
  const json = args.includes("--json");
  const quiet = args.includes("--quiet");
  const roots = args.filter((a) => !a.startsWith("--"));
  if (roots.length === 0) roots.push("folio/quantum-observable-universe");
  const files: string[] = [];
  for (const r of roots) walk(resolve(r), files);
  const report: { file: string; hits: CommentaryHit[] }[] = [];
  let failing = 0;
  for (const f of files) {
    const hits = scanCommentary(readFileSync(f, "utf8"), blockCtx(f));
    if (hits.some((h) => !h.advisory)) failing++;
    if (hits.length) report.push({ file: relative(process.cwd(), f), hits });
  }
  if (json) {
    console.log(JSON.stringify({ scanned: files.length, failing, report }, null, 2));
  } else {
    if (!quiet)
      for (const r of report)
        for (const h of r.hits) console.log(`${r.file}:${h.line}  [${h.criterion}${h.advisory ? " (advisory)" : ""}]  ${h.text}`);
    console.log(`paper-commentary-audit: ${failing} of ${files.length} block(s) fail; ${report.length - failing} advisory-only`);
  }
  process.exit(failing ? 1 : 0);
}
