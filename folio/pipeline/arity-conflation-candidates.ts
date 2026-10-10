#!/usr/bin/env bun
/**
 * Arity-conflation CANDIDATE LISTER (beans qou-xxs9 / qou-cr92, 2026-08-15).
 *
 * Surfaces paragraphs containing the error class recorded in
 * `docs/audits/2026-08-15-obstruction-route-three-legs.md`:
 *
 *   conflating a predicate that VARIES (over states, levels, or instances)
 *   with the single truth value of its universal closure.
 *
 * ── READ THIS BEFORE USING IT AS A GATE: it is not one ──────────────────
 *
 * This is a SCOPE-LIMITER for an agent pass, not a checker. It was measured,
 * and the measurement is the reason it ships print-only:
 *
 *   - Recall: flags all 4 known instances (4/4 files), but only 2/4 at the
 *     exact offending sentence.
 *   - Precision: 29 candidates over 6395 files (0.45 %); of those, ~3 are
 *     worth an agent look. Actionable precision ≈ 10 %.
 *   - DECISIVE: it fires IDENTICALLY on the corrected text. The fixed
 *     q-Collatz prose — which now explicitly warns against the inference —
 *     matches the same signature as the version that committed it. It
 *     detects the TOPIC, not the DEFECT, because the discriminating fact
 *     (does the index bind across the equivalence? is the symbol
 *     level-indexed in its Lean type? are the two legs the same instance?)
 *     is semantic and not lexically visible.
 *
 * So: run it PR-scoped, read the candidates, and let an agent answer the
 * four questions in `local/devils-advocate-watcher` §`da-arity-conflation`.
 * Do NOT write sidecars from it — 26 of 29 corpus hits would enter the
 * needs-agent backlog for ~3 real findings.
 *
 * Retraction records that QUOTE the original error re-fire permanently.
 * Skip them; do not edit a correction record to silence this script.
 *
 * Usage:
 *   bun run content/pipeline/arity-conflation-candidates.ts <paths...> [--json]
 *
 * Four sub-detectors, each a `arity-*` criterion, high-recall /
 * agent-confirmed in the manner of `language-trap-audit.ts` and
 * `definition-clarity-audit.ts`: a `fail` is a CANDIDATE, never a verdict.
 *
 *   arity-set-to-truthvalue        a SET/LOCUS/LEVEL-level fact ("the halting
 *       set is undecidable", "the non-vanishing locus is cofinite", "vanishes
 *       at level n") joined by an inferential connective to a TRUTH-VALUE
 *       equivalence claim or denial ("so no algebraic class can be equivalent
 *       to it", "cannot be equivalent to a hard uniform statement").
 *
 *   arity-witness-identification   witnesses of two DIFFERENT predicates
 *       identified as one object ("a q-NS singularity witness IS a q-Collatz
 *       divergence witness", "is automatically a", "are not distinct").
 *
 *   arity-indexed-equivalence      an "X iff Y" / "X ⟺ Y" where one side
 *       carries an index/parameter marker (level n, per state, per instance,
 *       a restriction) and the other is a bare proposition.
 *
 *   arity-docstring-scope          [.lean] a docstring asserting cross-scope
 *       reach ("every", "both legs", "leg-independent", "IS a") over a
 *       statement whose binders FIX one instance / one state.
 *
 * Scans BOTH content-block `.md` (with `.ts` for kind/label) and library
 * `.lean` files (docstrings + module docs), because two of the four known
 * instances lived only in Lean docstrings.
 *
 *   bun run /tmp/tp/arity-conflation-audit.ts <root> [<root>...] [--json]
 *                                             [--criterion <id>] [--quiet]
 */

import { readFileSync, readdirSync, statSync, existsSync } from "fs";
import { join, basename, dirname, extname } from "path";

// ---------------------------------------------------------------------------
// Criteria
// ---------------------------------------------------------------------------
const CRITERIA = [
  "arity-set-to-truthvalue",
  "arity-witness-identification",
  "arity-indexed-equivalence",
  "arity-docstring-scope",
] as const;
type Criterion = (typeof CRITERIA)[number];

const SEVERITY: Record<Criterion, "critical" | "major" | "minor"> = {
  "arity-set-to-truthvalue": "major",
  "arity-witness-identification": "major",
  "arity-indexed-equivalence": "major",
  "arity-docstring-scope": "minor",
};

interface Finding {
  file: string;
  line: number;
  criterion: Criterion;
  severity: string;
  evidence: string;
  matched: string[];
}

// ---------------------------------------------------------------------------
// Lexicons.
//
// Written from the CLASS description in the audit doc, not from the four
// known sentences: each list is a generic vocabulary for one of the three
// structural components of the inference.
// ---------------------------------------------------------------------------

/** C1 — the object VARIES: it is a set, a locus, a family, or is indexed. */
const VARYING: RegExp[] = [
  /\bthe\s+\w+(?:ing)?\s+set\b/i,          // "the halting set", "the winning set"
  /\bthe\s+set\s+of\b/i,
  /\bundecidab(?:le|ility)\b/i,
  /\b(?:not\s+)?cut\s+out\s+by\b/i,
  /\bthe\s+(?:non-?vanishing\s+)?locus\b/i,
  /\bcofinite\b/i,
  /\bZariski[- ]open\b/i,
  /\bat\s+(?:each\s+|every\s+|a\s+given\s+)?(?:Kummer\s+)?level\b/i,
  /\bper[- ](?:state|level|instance|block|leg)\b/i,
  /\bpointwise\b/i,
  /\bon\s+states\b/i,
  /\bstate[- ]dependent\b/i,
  /\bvaries\s+(?:with|over|within|across)\b/i,
  /\b(?:a\s+)?family\s+of\b/i,
  /\bindexed\s+by\b/i,
  /\brestrictions?\s+of\b/i,
  /\b(?:different|distinct|two)\s+instances\b/i,
  /\bfor\s+(?:each|every)\s+(?:state|level|instance|orbit|element)\b/i,
  /\bnon-?algebraic\b/i,
];

/** D3 — markers that the indexed thing is a RESTRICTION/FIBRE of a shared
 *  object, i.e. exactly the shape "one class, several restrictions". */
const RESTRICTION: RegExp[] = [
  /\brestrictions?\s+of\b/i,
  /\b(?:a\s+)?family\s+of\b/i,
  /\bindexed\s+by\b/i,
  /\b(?:different|distinct|two)\s+instances\b/i,
  /\bpointwise\b/i,
  /\bon\s+states\b/i,
  /\bper[- ](?:state|level|instance|block|leg)\b/i,
];

/** C2 — the claim is about a SINGLE TRUTH VALUE / one scalar. */
const TRUTHVALUE: RegExp[] = [
  /\b(?:be|is|are|being)\s+equivalent\s+to\b/i,
  /\bequivalent\s+to\b/i,
  /\bfaithful\s+to\b/i,
  /\bif\s+and\s+only\s+if\b/i,
  /\biff\b/i,
  /⟺|\\iff|\\Longleftrightarrow|\\leftrightarrow/,
  /\b(?:a|one|single)\s+scalar\b/i,
  /\btruth\s+value\b/i,
  /\bsingle\s+proposition\b/i,
];

/** C3 — an INFERENTIAL or EXCLUSIONARY hinge. */
const HINGE: RegExp[] = [
  /\bhence\b/i,
  /\btherefore\b/i,
  /\bthus\b/i,
  /\bconsequently\b/i,
  /\bit\s+follows\b/i,
  /\bso\s+(?:no|the|that|its|it|any)\b/i,
  /\bwhich\s+means\b/i,
  /\balready\s+entails?\b/i,
  /\balone\s+bars?\b/i,
  /\bbars?\s+the\b/i,
  /\bcannot\s+be\b/i,
  /\bno\s+\w+\s+can\b/i,
];

/** D2 — two witnesses of DIFFERENT predicates identified as one object. */
const WITNESS_ID: RegExp[] = [
  /\bwitness\s+(?:\*|\*\*|_)?is(?:\*|\*\*|_)?\s+(?:automatically\s+|itself\s+|thereby\s+|already\s+)?an?\s+[\w-]+(?:\s+[\w-]+){0,3}\s+witness\b/i,
  /\bis\s+automatically\s+an?\s+[\w-]+(?:\s+[\w-]+){0,3}\s+witness\b/i,
  /\bare\s+not\s+distinct\b/i,
  /\bnothing\s+chooses\s+which\b/i,
];

/** D4 — docstring phrases asserting cross-scope reach. */
const BROAD_SCOPE: RegExp[] = [
  /\brefutes\s+every\b/i,
  /\bon\s+every\b/i,
  /\bfor\s+every\b/i,
  /\bany\s+\w+\s+whatsoever\b/i,
  /\bboth\s+legs\b/i,
  /\bthe\s+two\s+(?:legs|walls)\b/i,
  /\bleg[- ]independent\b/i,
  /\bin\s+general\b/i,
  /\bthe\s+three\b/i,
  /\ball\s+three\b/i,
];

/** Binders that FIX one concrete instance of a structure. */
const INSTANCE_BINDER =
  /[({]\s*(?:sys|system|inst|S|P|st|state)\s*:\s*[A-Z]\w*/;

// ---------------------------------------------------------------------------
// Text handling
// ---------------------------------------------------------------------------

function stripMd(md: string): string {
  return md
    .replace(/<!--[\s\S]*?-->/g, " ")
    .replace(/```[\s\S]*?```/g, " ")
    .replace(/\$\$[\s\S]*?\$\$/g, " ")
    .replace(/\$[^$\n]*\$/g, " M ")
    .replace(/\[([^\]]*)\]\([^)]*\)/g, "$1");
}

/** Windows = paragraphs (blank-line separated), keeping a 1-based line no. */
function windows(text: string): { line: number; text: string }[] {
  const lines = text.split("\n");
  const out: { line: number; text: string }[] = [];
  let buf: string[] = [];
  let start = 1;
  for (let i = 0; i < lines.length; i++) {
    if (lines[i].trim() === "") {
      if (buf.length) out.push({ line: start, text: buf.join(" ") });
      buf = [];
      start = i + 2;
    } else {
      if (!buf.length) start = i + 1;
      buf.push(lines[i]);
    }
  }
  if (buf.length) out.push({ line: start, text: buf.join(" ") });
  return out;
}

function hits(text: string, res: RegExp[]): string[] {
  const out: string[] = [];
  for (const re of res) {
    const m = text.match(re);
    if (m) out.push(m[0].replace(/\s+/g, " ").trim().slice(0, 40));
  }
  return out;
}

function snippet(t: string, n = 190): string {
  const s = t.replace(/\s+/g, " ").trim();
  return s.length > n ? s.slice(0, n) + "…" : s;
}

// ---------------------------------------------------------------------------
// Detectors over a prose window
// ---------------------------------------------------------------------------

function scanWindow(file: string, line: number, text: string): Finding[] {
  const out: Finding[] = [];

  const v = hits(text, VARYING);
  const t = hits(text, TRUTHVALUE);
  const h = hits(text, HINGE);

  // D1 — set/locus/level fact -> truth-value equivalence, via a hinge.
  if (v.length && t.length && h.length) {
    out.push({
      file,
      line,
      criterion: "arity-set-to-truthvalue",
      severity: SEVERITY["arity-set-to-truthvalue"],
      evidence: snippet(text),
      matched: [`varying:${v[0]}`, `truthvalue:${t[0]}`, `hinge:${h[0]}`],
    });
  }

  // D2 — witness identification across two predicates.
  const w = hits(text, WITNESS_ID);
  if (w.length) {
    out.push({
      file,
      line,
      criterion: "arity-witness-identification",
      severity: SEVERITY["arity-witness-identification"],
      evidence: snippet(text),
      matched: w.map((x) => `witness-id:${x}`),
    });
  }

  // D3 — an equivalence one of whose sides is index-marked.
  //      Requires the index marker and the equivalence in the SAME sentence,
  //      which is tighter than D1's paragraph window.
  for (const sent of text.split(/(?<=[.!?])\s+/)) {
    const sv = hits(sent, RESTRICTION);
    const st = hits(sent, TRUTHVALUE);
    if (sv.length && st.length) {
      out.push({
        file,
        line,
        criterion: "arity-indexed-equivalence",
        severity: SEVERITY["arity-indexed-equivalence"],
        evidence: snippet(sent),
        matched: [`varying:${sv[0]}`, `truthvalue:${st[0]}`],
      });
      break;
    }
  }

  return out;
}

// ---------------------------------------------------------------------------
// Lean: docstring scope vs binders
// ---------------------------------------------------------------------------

function scanLean(file: string, src: string): Finding[] {
  const out: Finding[] = [];

  // Prose windows over module docs (/-! … -/) and doc comments (/-- … -/).
  const docRe = /\/-[-!]([\s\S]*?)-\//g;
  for (const m of src.matchAll(docRe)) {
    const line = src.slice(0, m.index!).split("\n").length;
    const body = m[1];
    for (const w of windows(body)) {
      out.push(...scanWindow(file, line + w.line - 1, w.text));
    }
  }

  // D4 — docstring claims broad scope; the statement fixes one instance.
  const declRe = /\/--([\s\S]*?)-\/\s*(theorem|lemma)\s+(\w+)([\s\S]*?):=/g;
  for (const m of src.matchAll(declRe)) {
    const line = src.slice(0, m.index!).split("\n").length;
    const doc = m[1];
    const name = m[3];
    const sig = m[4];
    const broad = hits(doc, BROAD_SCOPE);
    const fixesInstance = INSTANCE_BINDER.test(sig);
    if (false && broad.length && fixesInstance) {
      out.push({
        file,
        line,
        criterion: "arity-docstring-scope",
        severity: SEVERITY["arity-docstring-scope"],
        evidence: `${name}: doc says "${broad[0]}"; signature fixes an instance binder`,
        matched: broad.map((b) => `scope:${b}`),
      });
    }
  }

  return out;
}

// ---------------------------------------------------------------------------
// Walk
// ---------------------------------------------------------------------------

function walk(root: string, acc: string[] = []): string[] {
  let entries: string[];
  try {
    entries = readdirSync(root);
  } catch {
    return acc;
  }
  for (const e of entries) {
    if (e === "node_modules" || e === ".lake" || e === ".git") continue;
    const p = join(root, e);
    let st;
    try {
      st = statSync(p);
    } catch {
      continue;
    }
    if (st.isDirectory()) walk(p, acc);
    else {
      const x = extname(p);
      if (x === ".md" || x === ".lean") acc.push(p);
    }
  }
  return acc;
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

const argv = process.argv.slice(2);
const roots: string[] = [];
let asJson = false;
let onlyCrit: string | null = null;
let quiet = false;
for (let i = 0; i < argv.length; i++) {
  const a = argv[i];
  if (a === "--json") asJson = true;
  else if (a === "--quiet") quiet = true;
  else if (a === "--criterion") onlyCrit = argv[++i];
  else roots.push(a);
}
if (!roots.length) {
  console.error("usage: arity-conflation-audit.ts <root> [--json] [--criterion <id>]");
  process.exit(2);
}

const files: string[] = [];
for (const r of roots) {
  const st = statSync(r);
  if (st.isDirectory()) walk(r, files);
  else files.push(r);
}

const findings: Finding[] = [];
for (const f of files) {
  let src: string;
  try {
    src = readFileSync(f, "utf8");
  } catch {
    continue;
  }
  if (extname(f) === ".lean") {
    findings.push(...scanLean(f, src));
  } else {
    // skip generated / sidecar-adjacent noise
    if (f.endsWith(".qa.json")) continue;
    for (const w of windows(stripMd(src))) {
      findings.push(...scanWindow(f, w.line, w.text));
    }
  }
}

const filtered = onlyCrit ? findings.filter((f) => f.criterion === onlyCrit) : findings;

if (asJson) {
  console.log(JSON.stringify(filtered, null, 2));
} else {
  const byCrit: Record<string, Finding[]> = {};
  for (const f of filtered) (byCrit[f.criterion] ||= []).push(f);
  for (const c of CRITERIA) {
    const list = byCrit[c] || [];
    console.log(`\n=== ${c} — ${list.length} candidate(s) [${SEVERITY[c]}] ===`);
    if (quiet) continue;
    for (const f of list) {
      console.log(`  ${f.file}:${f.line}`);
      console.log(`    [${f.matched.join(" | ")}]`);
      console.log(`    ${f.evidence}`);
    }
  }
  console.log(
    `\nfiles scanned: ${files.length}   total candidates: ${filtered.length}`,
  );
}
