/**
 * Registry of QA criteria the per-block sweep recognises.
 *
 * Each criterion is one independently-trackable audit dimension.
 * The sweep walker iterates the registry and, per block, decides
 * whether to run the automated checker or queue an agent / human
 * adjudication request.
 *
 * Domain buckets (current):
 *
 * - `voice` — scholarly voice + status-leak greps (extends
 *   `.claude/skills/local/one-voice-audit.md` with four new
 *   axes: scholarly-default, ai-slop, fit-section-chapter,
 *   framework-canonical, wall-side-correct).
 * - `fit` — does the block belong in its declared sub-section /
 *   section / chapter.
 * - `framework` — uses current canonical math (not deprecated
 *   notation, e.g. old 5-tuple, $\omega$ for fibre functor).
 * - `wall` — archimedean vs algebraic placement, per CLAUDE.md
 *   §7c base-ring convention.
 *
 * Future watchers (proof, canonical, compute, detangler) extend
 * the registry with their own criteria.
 *
 * @module content/pipeline/qa-criteria-registry
 */

import type { QaCriterionDefinition } from "../../folio-assistant/schemas/block-qa";

// ── Domain: voice ───────────────────────────────────────────────

const VOICE: QaCriterionDefinition[] = [
  {
    id: "voice-status-leak",
    domain: "voice",
    description:
      "No status markers in body prose (✅ Done, (TODO), (TBD), **Pending.**). " +
      "Work-tracker speech belongs in todos/, not in the paper.",
    default_severity: "critical",
    depends_on: ["md"],
    automated: true,
  },
  {
    id: "voice-emoji-content",
    domain: "voice",
    description:
      "No emoji used as content (✅, ❌, ⚠, 🔧, 🚧) outside tables. In " +
      "tables, only compact comparison markers (✓ matches / ✗ diverges).",
    default_severity: "major",
    depends_on: ["md"],
    automated: true,
  },
  {
    id: "voice-first-person-work",
    domain: "voice",
    description:
      "No first-person work tone: 'we'll add X', 'let me', 'needs more " +
      "work', 'I'll fix this'. These signal draft state, not paper authority.",
    default_severity: "major",
    depends_on: ["md"],
    automated: true,
  },
  {
    id: "voice-time-stamped-notes",
    domain: "voice",
    description:
      "No time-stamped notes ('as of 2026-…', 'after the recent push', " +
      "'in the current draft'). The paper does not narrate its own draft history.",
    default_severity: "major",
    depends_on: ["md"],
    automated: true,
  },
  {
    id: "voice-unicode-crash",
    domain: "voice",
    description:
      "No Unicode characters that crash pdflatex (↦, ⁻, √, ─, ✅, ·, ²) " +
      "outside preamble-mapped sets. Use LaTeX equivalents in math.",
    default_severity: "critical",
    depends_on: ["md"],
    automated: true,
  },
  {
    id: "voice-editorializing",
    domain: "voice",
    description:
      "No editorialising phrases ('surprisingly', 'remarkably', " +
      "'interestingly', 'it is worth noting that', 'a beautiful result'). " +
      "Results speak for themselves.",
    default_severity: "minor",
    depends_on: ["md"],
    automated: true,
  },
  {
    id: "voice-scholarly-default",
    domain: "voice",
    description:
      "Block uses scholarly third-person voice by default. Applies to " +
      "both narrative .md AND proof bodies (Lean docstrings, expository " +
      "comments inside .lean). Exceptions require explicit author markers. " +
      "Heuristic-automated: second-person address, lecturer-cadence openers, " +
      "paper-past-tense narration. Borderline cases are confirmed / overruled " +
      "by an agent reviewer entry on the same sidecar.",
    default_severity: "major",
    // Applies to narrative prose independently of proofs; relaxed
    // to `["md"]` so prose-only blocks (no `.lean` sibling) still
    // run through the scholarly check.  Lean-docstring scanning is
    // dispatched per-block when the `.lean` is present (see the
    // dispatcher in `qa-checkers-voice.ts`).
    depends_on: ["md"],
    automated: true,
  },
  {
    id: "voice-title-scholarly",
    domain: "voice",
    description:
      "Content block `title:` field is a scholarly noun-phrase (e.g. " +
      "\"Borromean baryon\", \"Quantum-deformed Reeb flow\"), NOT a " +
      "question (\"Why is this important?\"), an imperative " +
      "(\"Compute the Markov trace\"), a first-person aside " +
      "(\"We derive…\"), or a casual marker (\"Quick note on …\"). " +
      "Scanned by extracting the `title:` value from the block's `.ts` " +
      "manifest and applying scholarly-form patterns.",
    default_severity: "minor",
    depends_on: ["ts"],
    automated: true,
  },
  {
    id: "voice-statement-no-interpretation",
    domain: "voice",
    description:
      "Provable block (theorem/proposition/lemma/corollary) STATEMENT " +
      "is the bare claim — interpretation / motivation / physical " +
      "meaning belongs in a SEPARATE `remark` block linked via " +
      "`interprets:`. A statement block whose `.md` carries an " +
      "`## Interpretation` / `## Discussion` / `## Motivation` / " +
      "`## Why this matters` / `## Significance` heading after the " +
      "statement is a candidate for splitting. Agent-only (the actual " +
      "judgement — what counts as interpretation vs. legitimate proof " +
      "sketch — is non-mechanical); the script merely flags candidates " +
      "with the heading patterns above and queues them for the agent.",
    default_severity: "minor",
    depends_on: ["md"],
    automated: false,
    applies_to: ["theorem", "lemma", "proposition", "corollary"],
  },
  {
    id: "voice-ai-slop",
    domain: "voice",
    description:
      "No AI / status-update tells: 'Let me think about this', 'Here's " +
      "what I did', 'I'll go ahead and', 'Note that we should', 'Great " +
      "question', repeated First/Second/Third bullet cadence, over-use of " +
      "'essentially' / 'comprehensive' / 'leverage' / 'streamline' / 'robust'. " +
      "Heuristic-automated: direct LLM tells (zero false-positives in practice), " +
      "≥ 3 distinct hedge tokens in one .md (concentration signal), and " +
      "First/Second/Third comma-anchored sentence cadence. Borderline cases " +
      "are confirmed / overruled by an agent reviewer entry.",
    default_severity: "critical",
    depends_on: ["md"],
    automated: true,
  },
];

// ── Domain: fit ─────────────────────────────────────────────────

const FIT: QaCriterionDefinition[] = [
  {
    id: "fit-section-chapter",
    domain: "fit",
    description:
      "Block topic + kind fit the declared sub-section / section / " +
      "chapter context. Stranger-than-fiction blocks (off-topic, wrong " +
      "register, redundant with siblings) should move or be promoted / demoted.",
    default_severity: "major",
    depends_on: ["md", "ts"],
    automated: false,
  },
];

// ── Domain: framework ───────────────────────────────────────────

const FRAMEWORK: QaCriterionDefinition[] = [
  {
    id: "framework-canonical",
    domain: "framework",
    description:
      "Uses current canonical math framework, not deprecated notation. " +
      "Examples of deprecated forms: 5-tuple (M, Θ, G, P, E) instead of " +
      "(C, Θ, G, S); $\\omega$ for fibre functor (canonical: $\\tau$); " +
      "$\\mathcal{C}$ for category (canonical: $\\mathbf{C}$); $E$ alone for " +
      "exceptional divisor or state bundle; bare $H_q$ (now $\\mathcal{H}_q$, " +
      "$\\hat{H}_q$, or $H_n(q)$ depending on meaning).",
    default_severity: "major",
    // The automated checker only scans the .md body for deprecated
    // notation. The .ts manifest carries metadata, not prose; including
    // it here would over-stale on label-only edits.
    depends_on: ["md"],
    automated: true,
  },
];

// ── Domain: wall ────────────────────────────────────────────────

const WALL: QaCriterionDefinition[] = [
  {
    id: "wall-side-correct",
    domain: "wall",
    description:
      "Block (`.lean` body) is on the correct side of the substrate-to-" +
      "archimedean wall (CLAUDE.md §7c). Algebraic Lean code must NOT " +
      "mention `ℝ`, `Real.sqrt`, `Real.rpow`, `Real.log`, `Real.exp`, " +
      "`linarith`, `0 < q`, or other archimedean-specific constructs. " +
      "Archimedean Lean code must declare `ℝ` (or LinearOrderedField) " +
      "explicitly. Each block belongs in either the algebraic substrate " +
      "or the archimedean specialisation, never both.",
    default_severity: "critical",
    // The automated checker scans .lean imports and the .md narrative
    // for an archimedean acknowledgement banner. The .ts manifest is
    // not read — kept out of depends_on to avoid spurious staleness.
    depends_on: ["md", "lean"],
    automated: true,
  },
  {
    id: "wall-side-statement",
    domain: "wall",
    description:
      "The narrative **Statement** of the block (in the `.md`) is on the " +
      "correct side of the substrate-to-archimedean wall. A theorem stated " +
      "as `∀ q : ℝ, …` is archimedean; one stated as `∀ R, [CommRing R], " +
      "∀ q : R, …` is algebraic. Mismatched statements are usually a sign " +
      "that the block needs a `wall:` placement field and a §7c-style " +
      "banner in the narrative.",
    default_severity: "major",
    depends_on: ["md"],
    automated: false,
    applies_to: [
      "theorem",
      "lemma",
      "proposition",
      "corollary",
      "definition",
    ],
  },
  {
    id: "wall-side-proof",
    domain: "wall",
    description:
      "The narrative `**Proof.**` body (in the `.md`) is on the correct " +
      "side of the substrate-to-archimedean wall. An algebraic statement " +
      "cannot be proved by `linarith` / IVT / continuity arguments; an " +
      "archimedean statement should explicitly cite the specialisation " +
      "or use Real.* lemmas. Mostly an agent-reviewer criterion — the " +
      "script flags candidate phrasings (`linarith`, `IVT`, `continuity`, " +
      "`Real.`) and queues agent adjudication.",
    default_severity: "major",
    depends_on: ["md"],
    automated: false,
    applies_to: ["theorem", "lemma", "proposition", "corollary"],
  },
];

// ── Domain: proof ───────────────────────────────────────────────
//
// Owned by `proof-integration-watcher`. Each criterion maps to one
// existing Lean / proof skill — the orchestration table lives in
// `.claude/skills/local/proof-integration-watcher.md §Dispatch`.

const PROOF: QaCriterionDefinition[] = [
  {
    id: "proof-no-bare-sorries",
    domain: "proof",
    description:
      "Every `sorry` in the block's `.lean` carries a `-- Ref: [key] <url>` " +
      "citation per CLAUDE.md §1 (proof-status-tracking). Bare `sorry` " +
      "without a reference is always a review failure.",
    default_severity: "critical",
    depends_on: ["lean"],
    automated: true,
    applies_to: [
      "theorem",
      "lemma",
      "proposition",
      "corollary",
      "definition",
      "conjecture",
    ],
  },
  {
    id: "proof-no-axiom-growth",
    domain: "proof",
    description:
      "Block's `#print axioms` set is a subset of the same block's axiom " +
      "set on `origin/main`. Verified against the doc-gen4 axiom-report. " +
      "Routes to `lean-witness-audit` on failure.",
    default_severity: "critical",
    depends_on: ["lean"],
    automated: true,
    applies_to: ["theorem", "lemma", "proposition", "corollary"],
  },
  {
    id: "proof-build-green",
    domain: "proof",
    description:
      "Block's Lake package builds clean. On failure routes to " +
      "`lean-build-fix`. Result is read from the `proof-objects.json` " +
      "manifest emitted by `lean_ci.yml`.",
    default_severity: "critical",
    depends_on: ["lean"],
    automated: true,
    applies_to: [
      "theorem",
      "lemma",
      "proposition",
      "corollary",
      "definition",
    ],
  },
  {
    id: "proof-narrative-lean-equiv",
    domain: "proof",
    description:
      "The .md statement and the .lean signature express the same claim. " +
      "Routes to `proof-narrative-lean-equivalence` (agent) — non- " +
      "deterministic; the checker only flags blocks that have BOTH a " +
      "Lean sibling AND a narrative `**Proposition.**` / `**Theorem.**` " +
      "envelope, and queues them for the agent.",
    default_severity: "major",
    depends_on: ["md", "lean"],
    automated: false,
    applies_to: ["theorem", "lemma", "proposition", "corollary"],
  },
  {
    id: "proof-substantive",
    domain: "proof",
    description:
      "Block's Lean does NOT use the abstract `holds : Prop` placeholder " +
      "without a matching `[Instance]` hypothesis on the downstream " +
      "consumer (CLAUDE.md §3b-cond). Routes to `lean-substantive-pass`.",
    default_severity: "major",
    depends_on: ["lean"],
    automated: true,
    applies_to: ["theorem", "lemma", "proposition", "corollary"],
  },
  {
    id: "proof-no-conj-propagation-violation",
    domain: "proof",
    description:
      "Provable block (theorem/proposition/lemma/corollary) whose " +
      "transitive `uses[]` cone touches a `conj:` label is either " +
      "demoted to `conjecture` OR satisfies the §3b-cond exception " +
      "(class-axiomatised conjecture + [Instance] hypothesis + " +
      "narrative banner). Reads cached witness " +
      "`docs/audits/2026-05-01-p3-1-conjectural-propagation.witness.json`.",
    default_severity: "critical",
    depends_on: ["ts"],
    automated: true,
    applies_to: ["theorem", "lemma", "proposition", "corollary"],
  },
  {
    id: "proof-no-trivial-skeleton",
    domain: "proof",
    description:
      "Block's `.lean` does not contain a trivial-skeleton pattern " +
      "(`def f := 0`, `:= PUnit`, `:= True`, `:= id`, `:= trivial`, " +
      "`:= rfl`, etc.) that encodes none of the conjectural content. " +
      "Reads cached witness " +
      "`docs/audits/2026-05-08-trivial-skeleton-audit.json` (keyed " +
      "by `.lean` path).",
    default_severity: "major",
    depends_on: ["lean"],
    automated: true,
  },
  {
    id: "proof-conditional-class-banner",
    domain: "proof",
    description:
      "Block classified as conditional-on-class by the conjectural- " +
      "propagation audit has both (a) a Lean class-hypothesis `[Inst : " +
      "C ...]` in its `.lean`, AND (b) a narrative banner `**Theorem " +
      "(conditional on …).**` in its `.md` (CLAUDE.md §3b-cond rules " +
      "2-4). Reads cached witness " +
      "`docs/audits/2026-05-09-conditional-class-banner.witness.json`.",
    default_severity: "major",
    depends_on: ["md", "lean"],
    automated: true,
    applies_to: ["theorem", "lemma", "proposition", "corollary"],
  },
];

// ── Domain: canonical ───────────────────────────────────────────
//
// Owned by `canonical-watcher`. Enforces the three-calibration
// discipline (`prop:three-calibration-discipline`) and bans
// numerology / fits.

const CANONICAL: QaCriterionDefinition[] = [
  {
    id: "canonical-calibration-count",
    domain: "canonical",
    description:
      "Block declares at most 3 calibration anchors (CODATA m_e + α + " +
      "G_Planck normalisation, per the three-calibration discipline). " +
      "Counted by scanning the .md / .ts for `calibration:` / " +
      "`anchor:` markers. Routes to a manual `canonical-watcher` review " +
      "on fail (cannot auto-resolve a 4th calibration).",
    default_severity: "critical",
    depends_on: ["md", "ts"],
    automated: true,
  },
  {
    id: "canonical-no-numerology",
    domain: "canonical",
    description:
      "Block does not claim numerical coincidence without a categorical " +
      "derivation chain (`derivation:` / `derived_from:` / `uses:`). " +
      "Numerology = a number is asserted to match an observable without " +
      "naming the structural reason. Agent reviewer — script only " +
      "flags candidate phrasings (`miraculous`, `surprising agreement`, " +
      "`numerical coincidence`).",
    default_severity: "critical",
    depends_on: ["md"],
    automated: false,
  },
  {
    id: "canonical-witness-pinned",
    domain: "canonical",
    description:
      "Every `:val[…]` directive in the .md references an existing " +
      "witness JSON under `folio-assistant/computations/*.witness.json`, " +
      "and the block's `computation:` field matches (or is absent and " +
      "the implicit dep is declared). Routes to `witnessed-values` skill.",
    default_severity: "major",
    depends_on: ["md", "ts"],
    automated: true,
  },
];

// ── Domain: compute ─────────────────────────────────────────────
//
// Owned by `compute-integration-watcher`. Implements the 13-pattern
// I1-I13 audit + LP-dual-witness validator (CLAUDE.md "LP / SDP
// duals — first-class infra").

const COMPUTE: QaCriterionDefinition[] = [
  {
    id: "compute-prop-has-probe",
    domain: "compute",
    description:
      "Every `prop:`/`theorem:` block has a corresponding probe witness " +
      "under `folio-assistant/computations/`. The probe is the I1 of the " +
      "13-pattern audit: a numerical check that the proposition's claim " +
      "holds at a representative parameter point.",
    default_severity: "major",
    depends_on: ["ts"],
    automated: true,
    applies_to: ["theorem", "lemma", "proposition", "corollary"],
  },
  {
    id: "compute-prop-has-consumer",
    domain: "compute",
    description:
      "Every `prop:` is consumed by at least one production script (I2- " +
      "I13 of the 13-pattern audit). A prop with a probe but no consumer " +
      "is a NOT-WIRED prop. Routes to `compute-integration-watcher §B`.",
    default_severity: "major",
    depends_on: ["ts"],
    automated: true,
    applies_to: ["theorem", "lemma", "proposition", "corollary"],
  },
  {
    id: "compute-witness-exists",
    domain: "compute",
    description:
      "If the block's `.ts` declares `computation: { witness: '…' }`, " +
      "the referenced witness JSON exists on disk and is non-empty. " +
      "Routes to the `compute-audit` skill on fail.",
    default_severity: "critical",
    depends_on: ["ts"],
    automated: true,
  },
  {
    id: "compute-lp-dual-present",
    domain: "compute",
    description:
      "For LP/SDP/operator-selection witnesses (matched per CLAUDE.md " +
      "`lp_dual_witness_validator.py` hint list), the witness JSON " +
      "includes `y0_star`, `y_star`, `active_set` (or alias), " +
      "`primal_obj`, `dual_obj`, `duality_gap`. Mirrors the standalone " +
      "validator.",
    default_severity: "critical",
    depends_on: ["ts"],
    automated: true,
  },
];

// ── Domain: detangler ───────────────────────────────────────────
//
// Owned by `detangler-integration-watcher`. Enforces the structural
// rules H1-H7 (no forward refs), R1-R3 (section band 3-18 blocks),
// and the cross-chapter forward-edge ban.

const DETANGLER: QaCriterionDefinition[] = [
  {
    id: "detangler-no-forward-ref",
    domain: "detangler",
    description:
      "Block's `uses:` / `interprets:` targets do not appear later in " +
      "the chapter's `<chapter>.ts` ordering (H1-H7). Forward refs " +
      "force the reader to skip ahead. Routes to " +
      "`detangler-integration-watcher §H`.",
    default_severity: "major",
    depends_on: ["ts"],
  },
  {
    id: "detangler-section-band",
    domain: "detangler",
    description:
      "Each `## Section` in the chapter contains between 3 and 18 " +
      "content blocks (R1-R3). Out-of-band sections invite either " +
      "skim-and-skip (>18) or trivial-aside dilution (<3).",
    default_severity: "minor",
    depends_on: ["ts"],
    automated: true,
  },
  {
    id: "detangler-no-xchapter-fwd",
    domain: "detangler",
    description:
      "Block's cross-chapter `uses:` references do not point at a chapter " +
      "later in `paper.ts` ordering. Cross-chapter forward edges break the " +
      "linear reading promise of a folio.",
    default_severity: "major",
    depends_on: ["ts"],
    automated: true,
  },
  {
    id: "detangler-archimedean-wall",
    domain: "detangler",
    description:
      "Chapter-level archimedean wall placement: blocks whose .lean is " +
      "purely archimedean live in `descartes-universe/` / `observations/` / " +
      "`fluid-dynamics/`. Generic-R blocks live in `braids-and-knots/` / " +
      "`quantum-observable-universes/` / `quantum-universes/`. " +
      "Companion to `wall-side-correct` (per-block) — this one is " +
      "per-chapter placement.",
    default_severity: "major",
    depends_on: ["ts", "lean"],
    automated: true,
  },
];

// ── Domain: bibliography ────────────────────────────────────────
//
// Block-level bibliography QA. Per-reference QA lives in the
// separate `content/pipeline/bib-qa.ts` (writes `bib-qa.json`); this
// domain projects the relevant per-reference findings DOWN to each
// content block that cites the reference, so a block's `.qa.json`
// surfaces its bibliography-readiness alongside its voice / proof /
// canonical / compute / detangler axes.

const BIBLIOGRAPHY: QaCriterionDefinition[] = [
  {
    id: "bib-cite-resolves",
    domain: "bibliography",
    description:
      "Every `\\cite{key}` and `-- Ref: [key]` in the block resolves to a " +
      "registered entry in `content/schema/references.ts`. Mirrors the " +
      "`validate-bib` skill's resolution check at block granularity.",
    default_severity: "critical",
    depends_on: ["md", "lean"],
    automated: true,
  },
  {
    id: "bib-cited-ref-has-url",
    domain: "bibliography",
    description:
      "Every reference the block cites has a URL or DOI (resolves to one) " +
      "per `bib-qa.ts` tag `has_url`. A block citing an URL-less reference " +
      "fails — the reader has no way to consult the source.",
    default_severity: "major",
    depends_on: ["md", "lean"],
    automated: true,
  },
  {
    id: "bib-cited-ref-metadata-ok",
    domain: "bibliography",
    description:
      "Every reference the block cites has complete metadata (title, " +
      "author/editor, year) per `bib-qa.ts` tag `metadata_ok`.",
    default_severity: "major",
    depends_on: ["md", "lean"],
    automated: true,
  },
  {
    id: "bib-cited-ref-has-screenshot",
    domain: "bibliography",
    description:
      "Every reference the block cites has a screenshot under " +
      "`content/bib-qa-images/<id>.*` per `bib-qa.ts` tag " +
      "`has_screenshot`. Provides provenance for the citation.",
    default_severity: "minor",
    depends_on: ["md", "lean"],
    automated: true,
  },
];

// ── Exported registry ───────────────────────────────────────────

export const QA_CRITERIA_REGISTRY: QaCriterionDefinition[] = [
  ...VOICE,
  ...FIT,
  ...FRAMEWORK,
  ...WALL,
  ...PROOF,
  ...CANONICAL,
  ...COMPUTE,
  ...DETANGLER,
  ...BIBLIOGRAPHY,
];

export const QA_CRITERIA_BY_ID: Record<string, QaCriterionDefinition> =
  Object.fromEntries(QA_CRITERIA_REGISTRY.map((c) => [c.id, c]));

export const QA_CRITERIA_BY_DOMAIN: Record<string, QaCriterionDefinition[]> =
  QA_CRITERIA_REGISTRY.reduce(
    (acc, c) => {
      (acc[c.domain] ??= []).push(c);
      return acc;
    },
    {} as Record<string, QaCriterionDefinition[]>,
  );

// Per-watcher criterion subsets. Each integration watcher reads
// its own subset to compute backlog + dispatch agent reviews.

/**
 * The set of criteria the `one-voice-integration-watcher` is
 * responsible for. Mirrors the historical voice + fit + framework +
 * wall buckets.
 */
export const ONE_VOICE_WATCHER_CRITERIA: string[] = [
  ...VOICE.map((c) => c.id),
  ...FIT.map((c) => c.id),
  ...FRAMEWORK.map((c) => c.id),
  ...WALL.map((c) => c.id),
];

export const PROOF_WATCHER_CRITERIA: string[] = PROOF.map((c) => c.id);
export const CANONICAL_WATCHER_CRITERIA: string[] = CANONICAL.map((c) => c.id);
export const COMPUTE_WATCHER_CRITERIA: string[] = COMPUTE.map((c) => c.id);
export const DETANGLER_WATCHER_CRITERIA: string[] = DETANGLER.map(
  (c) => c.id,
);
export const BIBLIOGRAPHY_WATCHER_CRITERIA: string[] = BIBLIOGRAPHY.map(
  (c) => c.id,
);

/**
 * All 6 watcher buckets, keyed by watcher short name (matches the
 * `/integration-watch` / `/integration-backlog` axis arguments).
 */
export const WATCHER_CRITERIA_BY_AXIS: Record<string, string[]> = {
  "one-voice": ONE_VOICE_WATCHER_CRITERIA,
  proof: PROOF_WATCHER_CRITERIA,
  canonical: CANONICAL_WATCHER_CRITERIA,
  compute: COMPUTE_WATCHER_CRITERIA,
  detangler: DETANGLER_WATCHER_CRITERIA,
  bibliography: BIBLIOGRAPHY_WATCHER_CRITERIA,
};
