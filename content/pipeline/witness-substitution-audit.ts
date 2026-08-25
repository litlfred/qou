#!/usr/bin/env bun
/**
 * `witness-substitution` QA axis — is a quoted number traceable to a producer?
 *
 * ## The gap this closes
 *
 * A block declares the computations it rests on:
 *
 * ```ts
 * computation: {
 *   script: "computations/markov/markov_trace_recursive.py",
 *   witness: ["computations/markov/markov-trace-recursive.witness.json"],
 * }
 * ```
 *
 * and then its prose quotes numbers:
 *
 * ```md
 * | proton | $\sigma_1^7 \sigma_2^4$ | $H_3$ | $1.633154\ldots$ |
 * ```
 *
 * **Nothing checks that the second came from the first.** There is no
 * substitution mechanism — no `{{witness:…}}`, no macro — so every quoted
 * value in the corpus is a decimal somebody typed once. The declaration is a
 * *citation*, and citations are not checked.
 *
 * That is how convention C survived in content long after the producers moved.
 * `markov_trace_recursive.py` was migrated and re-run; its witness says the
 * proton trace is `1.884319467254976`; the block still said `1.633154…`, the
 * convention-C value, and every gate stayed green — including
 * `trace-convention-audit`, because `1.633154` is not one of the four
 * fingerprints in the registry and never could be: the registry lists `z` and
 * the `y_λ`, not every downstream number computed from them.
 *
 * The fingerprint axis asks *"is this one of the known-bad numbers?"* — a list
 * that can only ever be as complete as somebody's memory. This axis asks
 * **"where did this number come from?"**, which needs no list. A number the
 * block cannot source is suspect whatever its value, so this catches the stale
 * literals nobody thought to enumerate — the same generalisation
 * `convention-c-witness-audit.py` made over decimal-string grepping when the
 * fingerprint work list turned out to have missed 41 of 53 witnesses.
 *
 * ## The two detectors
 *
 *   `unsourced-literal`   (major)
 *       A high-precision literal in the block's prose matches no value in any
 *       witness the block declares. Either it is stale, or it is derived from
 *       witness values by arithmetic done in somebody's head — both are
 *       untraceable, and the first is indistinguishable from the second by
 *       reading.
 *
 *   `no-witness-declared`   (major)
 *       The block quotes high-precision literals and declares no
 *       `computation.witness` at all. There is nothing it *could* be checked
 *       against; the numbers rest on the commit that introduced them.
 *
 * ## What is deliberately not flagged
 *
 * Each exclusion is a class where a typed literal is legitimate, not a
 * concession to noise:
 *
 * * **Fewer than `MIN_DECIMALS` decimal places.** `0.1 %`, `2.5`, a `(3,1)`
 *   signature, `10^{-15}` tolerances. Convention-sensitive values are quoted
 *   to many digits precisely because they are claims about agreement.
 * * **Integers.** Page ranges, strand counts, `H_6`, years. No decimal point,
 *   no claim of precision.
 * * **Lines carrying a citation** (`\cite{…}`, `[Author 1987]`). A value
 *   attributed to the literature is sourced — to a paper rather than to a
 *   producer, which is the right kind of source for it.
 * * **Fenced code blocks.** Pseudocode and snippets are a different surface
 *   with different rules; flagging them here would bury the prose findings.
 * * **An explicit marker.** `<!-- literal-source: … -->` within
 *   `MARKER_WINDOW` characters before the literal exempts it, and says in the
 *   file why. Used for values that are genuinely definitional or external.
 *
 * ## Matching
 *
 * Witness values are extracted from the raw JSON text rather than the parsed
 * object, because this corpus stores high-precision values as **strings**
 * (`"1.24824815696488285122900522964549301099821592058993116790559"`) as often
 * as numbers, and a NO-FLOAT64 pipeline is meant to. A prose literal matches
 * when it is a **prefix** of a witness value's decimal expansion (the usual
 * case — prose truncates and writes `\ldots`) or when it agrees numerically to
 * within half a unit in its own last place (prose rounded instead).
 *
 * ## Usage
 *
 *     bun run content/pipeline/witness-substitution-audit.ts            # summary
 *     bun run content/pipeline/witness-substitution-audit.ts --list
 *     bun run content/pipeline/witness-substitution-audit.ts --json out.json
 *     bun run content/pipeline/witness-substitution-audit.ts --selftest
 *     bun run content/pipeline/witness-substitution-audit.ts <path>...
 *
 * Exit 1 when any block has a finding.
 *
 * This axis does **not** write `.qa.json` sidecars yet, unlike the older axes.
 * That is a deliberate scope line rather than an oversight: the first sweep
 * touches a large fraction of the corpus, and committing a sidecar per block
 * before the detector has been tuned against real output would bury the tuning
 * diff in thousands of lines of generated JSON. Sidecar upsert lands once the
 * finding count is stable.
 */

import { existsSync, readFileSync, readdirSync, statSync } from "node:fs";
import { basename, dirname, join, relative, resolve } from "node:path";

const BUILDER_RE =
  /\b(proposition|theorem|lemma|corollary|definition|remark|example|proof|conjecture|axiom|notation)\s*\(/;

/** Minimum digits after the decimal point for a literal to be in scope. */
const MIN_DECIMALS = 4;

/** How far back from a literal an exempting marker may sit. */
const MARKER_WINDOW = 400;

const LITERAL_MARKER = /<!--\s*literal-source:/i;

/**
 * Is this "decimal" actually part of an identifier rather than a quantity?
 *
 * `10.1017` is not a measurement — it is the Cambridge University Press DOI
 * prefix, from `https://doi.org/10.1017/CBO9780511804441` in a citation link.
 * It reached the orphan list (`prf:confinement-phase-stratification`, "one
 * literal in NO witness") looking exactly like an unsourced physical value,
 * and no witness will ever contain it.
 *
 * Two shapes, both checked against the surrounding text rather than the
 * literal alone, because the literal itself is indistinguishable from a real
 * number:
 *
 *   * a DOI — `10.NNNN/…`, i.e. immediately followed by `/`
 *   * an arXiv id — `NNNN.NNNNN` immediately preceded by `arXiv:`
 *
 * Deliberately narrow. Anything followed by a slash could in principle be a
 * ratio written inline, but this corpus writes those in LaTeX, and a decimal
 * butted directly against `/` with no space is an identifier every time it
 * occurs here.
 */
function isIdentifierNotQuantity(text: string, start: number, end: number): boolean {
  if (text[end] === "/") return true; // DOI prefix: 10.1017/...
  const before = text.slice(Math.max(0, start - 12), start);
  return /arxiv:\s*$/i.test(before) || /doi:\s*$/i.test(before);
}

/** Exempts every literal in the file. For generated atlases and data dumps. */
const BLOCK_MARKER = /<!--\s*literal-source-block:/i;

/** `\cite{…}` or a `[Author 1987]`-style bracket cite anywhere on the line. */
const CITATION_LINE = /\\cite[a-zA-Z]*\s*[{[]|\[[A-Z][A-Za-z\-']+(?:\s+(?:et\s+al\.?|and|&)\s+[A-Z][A-Za-z\-']+)*\s+\d{4}[a-z]?\]/;

/**
 * A named external dataset on the line — a citation that is not in citation
 * form. Hyperbolic volumes come from the knot tables, particle masses from
 * CODATA/PDG, nuclear masses from AME. Those are sourced; they are simply not
 * sourced to a *producer*, and no witness in this repo will ever contain them.
 *
 * Matching these does not clear the literal — it moves it to the
 * `externally-attributed` bucket, which is counted and printed. The
 * distinction the axis can honestly draw is *claims a source* vs *claims
 * none*; whether the source actually says this is a different axis, and one
 * that would need the external tables to check against.
 */
const EXTERNAL_SOURCE_LINE =
  /\bCODATA\b|\bPDG\b|\bAME\s?20\d\d\b|\bRolfsen\b|\bThistlethwaite\b|\bSnapPy\b|\bKnotInfo\b|\bLinkInfo\b|\bRegina\b|\bcensus\b|manual-historical-volume-match/i;

/** A decimal literal, capturing the integer and fractional parts. */
const DECIMAL_RE = /(?<![\w.])(\d+)\.(\d{2,})(?![\w.])/g;

type Severity = "critical" | "major" | "minor";

interface Finding {
  detector: "unsourced-literal" | "no-witness-declared" | "externally-attributed";
  severity: Severity;
  literal: string;
  where: string;
  line: number;
  context: string;
}

interface Block {
  root: string;
  dir: string;
  label: string;
  mdPath: string;
  tsPath: string;
  md: string;
  ts: string;
}

// ---------------------------------------------------------------------------
// Block loading
// ---------------------------------------------------------------------------

function parseStringField(ts: string, field: string): string {
  const dq = ts.match(new RegExp(`${field}\\s*:\\s*"((?:[^"\\\\]|\\\\.)*)"`));
  if (dq) return dq[1].replace(/\\(["'`\\])/g, "$1");
  const sq = ts.match(new RegExp(`${field}\\s*:\\s*'((?:[^'\\\\]|\\\\.)*)'`));
  if (sq) return sq[1].replace(/\\(["'`\\])/g, "$1");
  return "";
}

/**
 * Pull `computation.witness` out of the `.ts` source.
 *
 * Accepts both spellings the corpus uses — a bare string and an array — and
 * tolerates a trailing comma. Parsed textually rather than by importing the
 * module: the builders pull in the whole schema package, and an axis that has
 * to typecheck the corpus to scan it cannot run on a broken tree, which is
 * exactly when you want to run it.
 */
function parseWitnessList(ts: string): string[] {
  const arr = ts.match(/witness\s*:\s*\[([\s\S]*?)\]/);
  if (arr) {
    return [...arr[1].matchAll(/["'`]([^"'`]+)["'`]/g)].map((m) => m[1]);
  }
  const one = parseStringField(ts, "witness");
  return one ? [one] : [];
}

function loadBlock(tsPath: string, repoRoot: string): Block | null {
  if (!existsSync(tsPath)) return null;
  const ts = readFileSync(tsPath, "utf8");
  if (!BUILDER_RE.test(ts)) return null;
  const dir = dirname(tsPath);
  const root = basename(tsPath, ".ts");
  const mdPath = join(dir, `${root}.md`);
  const md = existsSync(mdPath) ? readFileSync(mdPath, "utf8") : "";
  return {
    root,
    dir,
    label: parseStringField(ts, "label"),
    mdPath: relative(repoRoot, mdPath),
    tsPath: relative(repoRoot, tsPath),
    md,
    ts,
  };
}

function* walk(dir: string): Generator<string> {
  let entries: string[];
  try {
    entries = readdirSync(dir);
  } catch {
    return;
  }
  for (const e of entries) {
    if (e === "node_modules" || e === ".git" || e === ".lake") continue;
    if (e === "__pycache__") continue;
    // Tooling, not authored blocks — and this file's own selftest fixtures
    // contain unsourced literals by construction, so walking it would make
    // every sweep fail forever and destroy the exit-1 gate. Same reason
    // `trace-convention-audit.ts` skips it.
    if (e === "pipeline") continue;
    const full = join(dir, e);
    let st;
    try {
      st = statSync(full);
    } catch {
      continue;
    }
    if (st.isDirectory()) yield* walk(full);
    else if (e.endsWith(".ts") && !e.endsWith(".d.ts")) yield full;
  }
}

// ---------------------------------------------------------------------------
// Witness value extraction and matching
// ---------------------------------------------------------------------------

/**
 * Every decimal token in the witness, from the RAW TEXT.
 *
 * Deliberately not `JSON.parse` + walk: high-precision values in this corpus
 * live in strings as often as in numbers (that is what NO-FLOAT64 requires),
 * and parsing a 60-digit string into a double truncates it to 17 before the
 * comparison ever happens. The raw text has both, at full width.
 */
function witnessDecimals(paths: string[], repoRoot: string): string[] {
  const out: string[] = [];
  for (const p of paths) {
    const abs = resolve(repoRoot, p);
    let raw: string;
    try {
      raw = readFileSync(abs, "utf8");
    } catch {
      continue;
    }
    for (const m of raw.matchAll(/(\d+)\.(\d+)/g)) out.push(`${m[1]}.${m[2]}`);
  }
  return out;
}

/**
 * Is `lit` sourced by one of `values`?
 *
 * Prefix first — prose almost always truncates and appends `\ldots`. Then a
 * numeric fallback for prose that rounded instead: agreement to within half a
 * unit in the literal's own last place, with a hair of slack for the
 * boundary case where the next digit is exactly 5.
 */
function isSourced(lit: string, values: string[]): boolean {
  if (values.some((v) => v.startsWith(lit))) return true;
  const decimals = lit.split(".")[1].length;
  const tol = 0.5 * Math.pow(10, -decimals) * 1.000001;
  const x = Number(lit);
  if (!Number.isFinite(x)) return false;
  return values.some((v) => {
    const y = Number(v);
    return Number.isFinite(y) && Math.abs(x - y) <= tol;
  });
}

/** Character ranges covered by fenced code blocks. */
function fenceRanges(text: string): Array<[number, number]> {
  const out: Array<[number, number]> = [];
  const re = /^[ \t]*(?:```|~~~)/gm;
  let open: number | null = null;
  for (const m of text.matchAll(re)) {
    if (open === null) open = m.index!;
    else {
      out.push([open, m.index! + m[0].length]);
      open = null;
    }
  }
  if (open !== null) out.push([open, text.length]);
  return out;
}

/**
 * In-scope literals in `text`, with their offsets.
 *
 * A literal is in scope when it has at least `MIN_DECIMALS` decimal places and
 * sits outside a code fence, off a citation line, and beyond the reach of a
 * `literal-source` marker.
 */
function scopedLiterals(
  text: string,
): Array<{ lit: string; index: number; line: number; context: string; attributed: boolean }> {
  if (BLOCK_MARKER.test(text)) return [];
  const fences = fenceRanges(text);
  const inFence = (i: number) => fences.some(([a, b]) => i >= a && i < b);
  const out: Array<{ lit: string; index: number; line: number; context: string; attributed: boolean }> = [];

  for (const m of text.matchAll(DECIMAL_RE)) {
    const [whole, , frac] = m;
    const i = m.index!;
    if (frac.length < MIN_DECIMALS) continue;
    if (inFence(i)) continue;
    if (isIdentifierNotQuantity(text, i, i + whole.length)) continue;

    const lineStart = text.lastIndexOf("\n", i) + 1;
    let lineEnd = text.indexOf("\n", i);
    if (lineEnd === -1) lineEnd = text.length;
    const lineText = text.slice(lineStart, lineEnd);
    if (LITERAL_MARKER.test(text.slice(Math.max(0, i - MARKER_WINDOW), i))) continue;

    out.push({
      lit: whole,
      index: i,
      line: text.slice(0, i).split("\n").length,
      context: lineText.trim().slice(0, 110),
      attributed: CITATION_LINE.test(lineText) || EXTERNAL_SOURCE_LINE.test(lineText),
    });
  }
  return out;
}

// ---------------------------------------------------------------------------
// Scan
// ---------------------------------------------------------------------------

function scanBlock(b: Block, repoRoot: string): { inScope: boolean; findings: Finding[] } {
  const surfaces: Array<[string, string]> = [
    ["md", b.md],
    ["ts", b.ts],
  ];
  const literals = surfaces.flatMap(([where, text]) =>
    scopedLiterals(text).map((l) => ({ ...l, where })),
  );
  if (literals.length === 0) return { inScope: false, findings: [] };

  const unattributed = literals.filter((l) => !l.attributed);
  const declared = parseWitnessList(b.ts);

  if (declared.length === 0) {
    if (unattributed.length === 0) return { inScope: true, findings: [] };
    const first = unattributed[0];
    return {
      inScope: true,
      findings: [
        {
          detector: "no-witness-declared",
          severity: "major",
          literal: first.lit,
          where: first.where,
          line: first.line,
          context: `${unattributed.length} unattributed high-precision literal(s), no computation.witness declared — e.g. ${first.context}`,
        },
      ],
    };
  }

  const values = witnessDecimals(declared, repoRoot);
  const findings: Finding[] = [];
  const seen = new Set<string>();
  for (const l of literals) {
    if (isSourced(l.lit, values)) continue;
    const key = `${l.where}:${l.lit}`;
    if (seen.has(key)) continue;
    seen.add(key);
    findings.push({
      detector: l.attributed ? "externally-attributed" : "unsourced-literal",
      severity: l.attributed ? "minor" : "major",
      literal: l.lit,
      where: l.where,
      line: l.line,
      context: l.context,
    });
  }
  return { inScope: true, findings };
}

// ---------------------------------------------------------------------------
// Selftest — a detector that cannot fail is worse than none
// ---------------------------------------------------------------------------

const WITNESS_FIXTURE = JSON.stringify({
  test_cases: [
    { name: "proton", tr_M_at_q0: 1.884319467254976 },
    { name: "neutron", tr_M_at_q0: 1.464034136338941 },
    { name: "hi_precision", value: "1.24824815696488285122900522964549301099821592058993116790559" },
  ],
});

/** How much is a `--suggest` proposal actually worth?
 *
 * Coverage alone is nearly worthless: on a single-literal block, ANY witness
 * that happens to contain that decimal "covers" it. `def:jet-stratified-reduction`
 * quotes `1.1097`, which 29 witnesses carry, and the greedy cover prints one of
 * them as though it were the source.
 *
 * Two signals separate provenance from arithmetic, in descending strength:
 *   CONFIDENT — the witness is NAMED AFTER the block. Not a coincidence.
 *   UNIQUE    — every literal has exactly one candidate witness in the corpus.
 *               Strong, but NOT proof: two blocks can independently quote the
 *               same rare constant, and `rem:q-beta-gamma-gamma-canonical-derivation`
 *               is UNIQUE against a helium-4 chi matrix it has nothing to do
 *               with. Subject-matter coherence is the remaining human check.
 *   AMBIGUOUS — everything else. Not actionable: declaring one attaches a
 *               source that merely contains the number, and it passes this
 *               axis forever after, because the axis only checks containment.
 */
/** Digits below which a match is arithmetic, not evidence.
 *
 * `ex:qvalue-benchmark-table` and three sibling Q-value blocks were UNIQUE
 * against `sublemma-2-1-A-operator-extract-h9-pn.witness.json` on the literal
 * `0.5904`. The block says that is "the Rosso-Jones weighted average over the
 * two degree-2 torus knots"; the witness carries `0.5904453769109197` as an
 * A-operator pair FROBENIUS NORM. Unrelated quantities, agreeing to four
 * decimals, with only one candidate in the whole corpus — so uniqueness alone
 * proposed a false source for four blocks at once.
 *
 * Contrast `prf:crystal-isospin-degeneracy`, UNIQUE on
 * `0.0020612874779541296` against `.data.atoms[1].S_crystal_at_q_zero`.
 * Seventeen digits do not coincide.
 */
const STRONG_MATCH_DECIMALS = 10;

export function coverageTag(
  covered: number,
  total: number,
  named: boolean,
  worstCand: number,
  minDecimals = Infinity,
): "CONFIDENT" | "UNIQUE" | "WEAK" | "AMBIGUOUS" | "PARTIAL" | "ORPHAN" {
  if (covered === 0) return "ORPHAN";
  if (covered < total) return "PARTIAL";
  if (named) return "CONFIDENT";
  if (worstCand !== 1) return "AMBIGUOUS";
  // Unique, but on too few digits to be evidence of anything.
  return minDecimals >= STRONG_MATCH_DECIMALS ? "UNIQUE" : "WEAK";
}

function selftest(): number {
  const V = witnessDecimalsFromText(WITNESS_FIXTURE);

  const matchCases: Array<[string, string, boolean]> = [
    ["a literal the witness contains verbatim -> sourced", "1.884319467254976", true],
    ["prose truncates and writes \\ldots -> sourced by prefix", "1.884319", true],
    ["prose rounded the last place -> sourced numerically", "1.46403414", true],
    ["a 60-digit string value in the witness -> sourced", "1.248248156964", true],
    ["the convention-C value the witness does NOT contain -> UNSOURCED", "1.633154", false],
    ["a neighbouring but distinct value -> UNSOURCED", "1.884419", false],
  ];

  const scopeCases: Array<[string, string, number]> = [
    ["6 decimals in prose -> in scope", "The trace is $1.633154\\ldots$ here.", 1],
    ["3 decimals -> below threshold, out of scope", "About $1.633$ or so.", 0],
    ["an integer -> out of scope", "Annals of Math. **126**, 335-388.", 0],
    ["inside a fenced code block -> skipped", "```\nx = 1.633154\n```\n", 0],
    [
      "after an explicit literal-source marker -> skipped",
      "<!-- literal-source: CODATA 2022 -->\nThe ratio is $206.7682830\\ldots$.",
      0,
    ],
    [
      "a literal-source-block marker -> whole file skipped",
      "<!-- literal-source-block: generated knot atlas -->\n$1.633154$ and $1.248248$.",
      0,
    ],
    ["two literals on one line -> both in scope", "$1.633154$ and $1.248248$.", 2],
    // Identifiers, not quantities. 10.1017 is the Cambridge UP DOI prefix and
    // reached the orphan list looking like an unsourced physical value.
    [
      "a DOI prefix in a citation link -> not a quantity",
      "see [Boyd-Vandenberghe](https://doi.org/10.1017/CBO9780511804441) for this.",
      0,
    ],
    ["an arXiv id -> not a quantity", "Ref: arXiv:2601.05136 for the construction.", 0],
    ["a bare `doi:` id -> not a quantity", "doi:10.1103/PhysRevD.98.030001", 0],
    [
      "a real value on a line that ALSO has a DOI -> still in scope",
      "gives $1.633154\\ldots$; see https://doi.org/10.1017/CBO9780511804441",
      1,
    ],
  ];

  /** In scope, but attributed to something other than a witness. */
  const attributionCases: Array<[string, string, boolean]> = [
    ["a citation line -> attributed, not unsourced", "[Jones 1987] gives $1.633154\\ldots$ here.", true],
    ["a CODATA line -> attributed", "$m_e = 0.51099895$ MeV (CODATA exact).", true],
    ["a knot-table line -> attributed", "| $6_2$ | Rolfsen | 6 | 4.4008 | volume |", true],
    ["a bare table row -> NOT attributed", "| proton | $H_3$ | $1.633154\\ldots$ |", false],
  ];

  let bad = 0;
  for (const [name, lit, want] of matchCases) {
    const got = isSourced(lit, V);
    const ok = got === want;
    bad += ok ? 0 : 1;
    console.log(`  ${ok ? "ok  " : "FAIL"}  ${name}`);
  }
  for (const [name, text, want] of scopeCases) {
    const got = scopedLiterals(text).length;
    const ok = got === want;
    bad += ok ? 0 : 1;
    console.log(`  ${ok ? "ok  " : "FAIL"}  ${name}${ok ? "" : `  (got ${got}, want ${want})`}`);
  }

  for (const [name, text, want] of attributionCases) {
    const ls = scopedLiterals(text);
    const got = ls.length > 0 && ls[0].attributed;
    const ok = got === want;
    bad += ok ? 0 : 1;
    console.log(`  ${ok ? "ok  " : "FAIL"}  ${name}`);
  }

  // The end-to-end shape: a block declaring no witness at all.
  const noWitness = parseWitnessList(`export default proposition({ label: "prop:x" });`).length === 0;
  console.log(`  ${noWitness ? "ok  " : "FAIL"}  a block with no computation.witness parses as zero witnesses`);
  bad += noWitness ? 0 : 1;

  const twoWitness =
    parseWitnessList(
      `computation: { witness: ["computations/a.witness.json", "computations/b.witness.json"] }`,
    ).length === 2;
  console.log(`  ${twoWitness ? "ok  " : "FAIL"}  a two-element witness array parses as two witnesses`);
  bad += twoWitness ? 0 : 1;

  // `--suggest` triage. These exist because "151 fully coverable" read as a
  // work queue when 138 of the 151 were arbitrary picks, and acting on it would
  // have attached false provenance that this axis could never afterwards
  // detect. The distinction is the whole value of the mode, so it gets tests.
  const tagCases: Array<[string, ReturnType<typeof coverageTag>, ReturnType<typeof coverageTag>]> = [
    ["a witness named after the block is CONFIDENT even if the literal is common",
     coverageTag(1, 1, true, 57), "CONFIDENT"],
    ["one candidate AND 17 matched decimals -> UNIQUE (crystal-isospin)",
     coverageTag(1, 1, false, 1, 19), "UNIQUE"],
    // The four Q-value blocks. One candidate in the whole corpus, and still a
    // coincidence: `0.5904` is a Rosso-Jones average in the block and an
    // A-operator Frobenius norm in the witness.
    ["one candidate but only 4 decimals -> WEAK, not actionable",
     coverageTag(1, 1, false, 1, 4), "WEAK"],
    ["one candidate at exactly the threshold -> UNIQUE",
     coverageTag(1, 1, false, 1, 10), "UNIQUE"],
    ["one candidate one digit below the threshold -> WEAK",
     coverageTag(1, 1, false, 1, 9), "WEAK"],
    ["a named witness outranks a weak digit count",
     coverageTag(1, 1, true, 1, 4), "CONFIDENT"],
    ["one literal, 29 candidate witnesses -> AMBIGUOUS, not coverable work",
     coverageTag(1, 1, false, 29), "AMBIGUOUS"],
    ["a single ambiguous literal poisons an otherwise unique block",
     coverageTag(3, 3, false, 12), "AMBIGUOUS"],
    ["partial coverage is PARTIAL regardless of candidate count",
     coverageTag(1, 2, false, 1), "PARTIAL"],
    ["nothing covered is ORPHAN",
     coverageTag(0, 2, false, 0), "ORPHAN"],
  ];
  for (const [name, got, want] of tagCases) {
    const ok = got === want;
    bad += ok ? 0 : 1;
    console.log(`  ${ok ? "ok  " : "FAIL"}  ${name}${ok ? "" : ` (got ${got}, want ${want})`}`);
  }

  const total = matchCases.length + scopeCases.length + attributionCases.length
    + tagCases.length + 2;
  console.log(
    `selftest: ${total - bad}/${total}` +
      (bad ? "" : " — sources a literal the witness carries, flags one it does not,"
        + " and separates provenance from a decimal coincidence."),
  );
  return bad;
}

/** Selftest helper: the same extraction as `witnessDecimals`, from a string. */
function witnessDecimalsFromText(raw: string): string[] {
  return [...raw.matchAll(/(\d+)\.(\d+)/g)].map((m) => `${m[1]}.${m[2]}`);
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

function main(): number {
  const argv = process.argv.slice(2);
  if (argv.includes("--selftest")) return selftest() ? 1 : 0;

  const wantList = argv.includes("--list");
  const wantSuggest = argv.includes("--suggest");
  const jsonIdx = argv.indexOf("--json");
  const jsonOut = jsonIdx >= 0 ? argv[jsonIdx + 1] : null;
  const targets = argv.filter(
    (a, i) => !a.startsWith("--") && !(jsonIdx >= 0 && i === jsonIdx + 1),
  );

  const repoRoot = process.cwd();
  const roots = targets.length ? targets : [join(repoRoot, "content")];
  const tsPaths = new Set<string>();
  for (const t of roots) {
    const abs = resolve(t);
    if (existsSync(abs) && statSync(abs).isDirectory()) for (const p of walk(abs)) tsPaths.add(p);
    else if (abs.endsWith(".ts")) tsPaths.add(abs);
    else if (abs.endsWith(".md")) tsPaths.add(abs.slice(0, -3) + ".ts");
    else tsPaths.add(abs + ".ts");
  }

  let scanned = 0;
  let inScope = 0;
  const rows: Array<{ block: Block; findings: Finding[] }> = [];
  for (const p of [...tsPaths].sort()) {
    const b = loadBlock(p, repoRoot);
    if (!b) continue;
    scanned++;
    const { inScope: s, findings } = scanBlock(b, repoRoot);
    if (s) inScope++;
    if (findings.length) rows.push({ block: b, findings });
  }

  const has = (r: { findings: Finding[] }, d: Finding["detector"]) =>
    r.findings.some((f) => f.detector === d);
  const count = (d: Finding["detector"]) =>
    rows.reduce((n, r) => n + r.findings.filter((f) => f.detector === d).length, 0);

  const unsourced = rows.filter((r) => has(r, "unsourced-literal"));
  const undeclared = rows.filter((r) => has(r, "no-witness-declared"));
  const attributed = rows.filter((r) => has(r, "externally-attributed"));
  // Only the two major detectors gate. `externally-attributed` is reported so
  // the surface stays visible, but a CODATA mass in a table is not a defect.
  const failing = rows.filter((r) => has(r, "unsourced-literal") || has(r, "no-witness-declared"));

  console.log(
    `witness-substitution: ${scanned} block(s) scanned, ${inScope} quoting high-precision literals, ` +
      `${failing.length} failing`,
  );
  console.log(
    `  unsourced-literal      ${unsourced.length} block(s), ${count("unsourced-literal")} literal(s) matching no declared witness`,
  );
  console.log(
    `  no-witness-declared    ${undeclared.length} block(s) quoting precise values with no computation.witness`,
  );
  console.log(
    `  externally-attributed  ${attributed.length} block(s), ${count("externally-attributed")} literal(s) sourced to CODATA / a knot table / a citation — reported, not failing`,
  );

  if (wantList) {
    for (const { block, findings } of failing) {
      console.log(`\n  ${block.label || block.root}  (${block.mdPath})`);
      for (const f of findings.filter((x) => x.detector !== "externally-attributed").slice(0, 8)) {
        console.log(`      ${f.detector}  ${f.literal}  @ ${f.where}:${f.line}`);
        console.log(`          ${f.context}`);
      }
      if (findings.length > 8) console.log(`      … ${findings.length - 8} more`);
    }
  }

  if (wantSuggest) {
    // Which witnesses would make an undeclared block's numbers traceable?
    //
    // 190 blocks quote high-precision values and declare no
    // `computation.witness`. Triage showed ~115 of them are UNDER-declared --
    // their numbers do exist in some witness, nobody named it -- and ~61 are
    // orphans, quoting values that appear in no witness anywhere. Those are
    // very different pieces of work, and hand-separating 190 blocks is the
    // kind of survey this axis exists to avoid.
    //
    // So: index every decimal token in every witness (truncated to 8 decimal
    // places, which is well past the 4-place scope threshold and cheap to
    // hold), then greedily cover each block's literals. A block that ends up
    // fully covered is a declaration away from being traceable; one that ends
    // up mostly uncovered is a real finding.
    //
    // The output is a PROPOSAL, not an edit. A witness that happens to contain
    // a matching decimal is not necessarily the witness the block means --
    // 0.612688037146 is z at the proton pin and appears in dozens of unrelated
    // files. Coverage narrows the candidates for a human; it does not decide.
    // coarse key -> [(witness, full decimal token)]. The full token is what
    // makes the prefix confirmation possible; the key only buckets.
    const tokenIndex = new Map<string, Array<[string, string]>>();
    const witnessFiles: string[] = [];
    const collect = (dir: string) => {
      let entries: string[];
      try {
        entries = readdirSync(dir);
      } catch {
        return;
      }
      for (const e of entries) {
        if (e === "node_modules" || e === "__pycache__" || e === "_deprecated") continue;
        const full = join(dir, e);
        let st;
        try {
          st = statSync(full);
        } catch {
          continue;
        }
        if (st.isDirectory()) collect(full);
        else if (e.endsWith(".witness.json")) witnessFiles.push(full);
      }
    };
    collect(join(repoRoot, "computations"));
    for (const wf of witnessFiles) {
      let raw: string;
      try {
        raw = readFileSync(wf, "utf8");
      } catch {
        continue;
      }
      const rel = relative(repoRoot, wf);
      const seen = new Set<string>();
      for (const m of raw.matchAll(/(\d+)\.(\d{4,})/g)) {
        // Bucket on MIN_DECIMALS, not 8. Keying both sides at 8 was a bug: a
        // literal with 4-7 decimals produced a key of ITS OWN length while the
        // index produced one of length 8, so `137.0359351` (7) could never
        // match a witness token indexed as `137.03593513` (8). Every literal
        // shorter than 8 decimals was therefore reported ORPHAN regardless of
        // what the corpus contained -- which is most of them, and is why the
        // first orphan list was full of 4-decimal values. Bucket coarsely,
        // then confirm by full prefix below.
        const k = `${m[1]}.${m[2].slice(0, MIN_DECIMALS)}`;
        if (seen.has(k)) continue;
        seen.add(k);
        const full = `${m[1]}.${m[2]}`;
        const arr = tokenIndex.get(k);
        if (arr) {
          if (arr.length < 200) arr.push([rel, full]);
        } else tokenIndex.set(k, [[rel, full]]);
      }
    }
    console.log(
      `\n  suggest: indexed ${witnessFiles.length} witness(es), ${tokenIndex.size} distinct ${MIN_DECIMALS}-dp buckets\n`,
    );

    let fully = 0;
    let partial = 0;
    let orphan = 0;
    let confident = 0;
    let uniqueSrc = 0;
    let weak = 0;
    let ambiguous = 0;
    for (const { block, findings } of failing) {
      if (!findings.some((f) => f.detector === "no-witness-declared")) continue;
      const lits = [...new Set(scopedLiterals(block.md).map((l) => l.lit))];
      if (!lits.length) continue;
      const keyOf = (l: string) => {
        const [a, b] = l.split(".");
        return `${a}.${b.slice(0, MIN_DECIMALS)}`;
      };
      // A bucket hit is necessary, not sufficient: confirm the witness really
      // carries this literal as a prefix of one of its values.
      const witnessesFor = (l: string) => {
        // Prefix OR numeric, matching `isSourced`. Prefix alone was not
        // enough: `1.1099786` in prop:alpha-em-categorical-trace-ratio is q0
        // ROUNDED to eight significant figures, and no prefix of
        // 1.1099785827... starts with it. The main detector already handled
        // rounding and this triage did not, so it reported a rounded q0 as a
        // value no producer emits.
        const out = new Set<string>();
        const decimals = l.split(".")[1].length;
        const tol = 0.5 * Math.pow(10, -decimals) * 1.000001;
        const x = Number(l);
        for (const [w, full] of tokenIndex.get(keyOf(l)) ?? []) {
          if (full.startsWith(l) || l.startsWith(full)) { out.add(w); continue; }
          const y = Number(full);
          if (Number.isFinite(x) && Number.isFinite(y) && Math.abs(x - y) <= tol) out.add(w);
        }
        return out;
      };
      const cover = new Map(lits.map((l) => [l, witnessesFor(l)]));
      let uncovered = new Set(lits.filter((l) => cover.get(l)!.size > 0));
      const missing = lits.filter((l) => cover.get(l)!.size === 0);
      const chosen: Array<[string, number]> = [];
      while (uncovered.size && chosen.length < 6) {
        const tally = new Map<string, number>();
        for (const l of uncovered)
          for (const w of cover.get(l)!) tally.set(w, (tally.get(w) ?? 0) + 1);
        let best = "";
        let bestN = 0;
        for (const [w, n] of tally) if (n > bestN) [best, bestN] = [w, n];
        if (!best) break;
        chosen.push([best, bestN]);
        uncovered = new Set(
          [...uncovered].filter((l) => !cover.get(l)!.has(best)),
        );
      }
      const covered = lits.length - missing.length - uncovered.size;
      if (covered === lits.length) fully++;
      else if (covered === 0) orphan++;
      else partial++;
      // NAME CORRESPONDENCE is the only signal here that is not a decimal
      // coincidence. Coverage alone proposes nonsense on single-literal
      // blocks: rem:collatz-hausdorff-comparison and conj:diophantine-birthday
      // are both "covered" by meson-mass-from-hecke.witness.json, because one
      // shared decimal is all it takes. But when `prop:meson-em-sinh-closed-form`
      // is covered by `meson-em-sinh-closed-form.witness.json`, the witness is
      // named after the block, and that is provenance rather than arithmetic.
      //
      // So a proposal is CONFIDENT only when a chosen witness's basename
      // matches the block's file root. Everything else stays a suggestion for
      // a human, which is what the whole mode is for.
      const rootOf = (w: string) =>
        w.split("/").pop()!.replace(/\.witness\.json$/, "");
      const named = chosen.find(([w]) => rootOf(w) === block.root);

      // AMBIGUITY is the second non-coincidental signal, and without it the
      // "fully coverable" count reads as a work queue when it is mostly noise.
      // `def:jet-stratified-reduction` quotes one literal, `1.1097`, which
      // occurs in 57 witnesses; the greedy cover above picks one of the 57 and
      // prints it as though it were the source. Declaring that would attach
      // FALSE PROVENANCE — and it would pass this axis forever after, because
      // the axis only asks whether the declared witness CONTAINS the number.
      //
      // So report how many witnesses could have supplied each literal. One
      // candidate is evidence; fifty-seven is a coin flip. `cover` already
      // holds the candidate sets — the count was computed and thrown away.
      const candCounts = lits
        .filter((l) => cover.get(l)!.size > 0)
        .map((l) => cover.get(l)!.size);
      const worstCand = candCounts.length ? Math.max(...candCounts) : 0;
      const coveredLits = lits.filter((l) => cover.get(l)!.size > 0);
      const minDec = coveredLits.length
        ? Math.min(...coveredLits.map((l) => (l.split(".")[1] ?? "").length))
        : 0;
      const verdict = coverageTag(covered, lits.length, !!named, worstCand, minDec);
      const unique = verdict === "UNIQUE";
      const tag = verdict.padEnd(9);
      if (verdict === "CONFIDENT") confident++;
      else if (unique) uniqueSrc++;
      else if (verdict === "WEAK") weak++;
      else if (verdict === "AMBIGUOUS") ambiguous++;
      console.log(
        `  ${tag}  ${block.label || block.root}  (${covered}/${lits.length} literals`
        + `, ${minDec}dp`
        + `${worstCand > 1 ? `, up to ${worstCand} candidates` : ""})`,
      );
      for (const [w, n] of chosen)
        console.log(`             +${n} <- ${w}${rootOf(w) === block.root ? "   [named after the block]" : ""}`);
      if (missing.length)
        console.log(
          `             ${missing.length} literal(s) in NO witness: ${missing.slice(0, 3).join(", ")}`,
        );
    }
    console.log(
      `\n  ${fully} fully coverable by declaration — but coverable is NOT a work queue:`
      + `\n    ${confident} CONFIDENT  witness is named after the block (provenance, not arithmetic)`
      + `\n    ${uniqueSrc} UNIQUE     one candidate witness AND >=${STRONG_MATCH_DECIMALS} matched decimals`
      + `\n    ${weak} WEAK       one candidate, but too few decimals to be evidence`
      + `\n    ${ambiguous} AMBIGUOUS  some literal occurs in several witnesses; the cover picks one arbitrarily`
      + `\n  ${partial} partial, ${orphan} orphan`
      + `\n\n  Only the first two are actionable. Declaring an AMBIGUOUS block attaches a`
      + `\n  source that merely happens to contain the number — and it passes this axis`
      + `\n  permanently afterwards, because the axis only checks containment.`,
    );
  }

  if (jsonOut) {
    const payload = rows.map(({ block, findings }) => ({
      label: block.label,
      md: block.mdPath,
      ts: block.tsPath,
      witnesses: parseWitnessList(block.ts),
      findings,
    }));
    require("node:fs").writeFileSync(jsonOut, JSON.stringify(payload, null, 2));
    console.log(`\n  json -> ${jsonOut}`);
  }

  return failing.length ? 1 : 0;
}

process.exit(main());
