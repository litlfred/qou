# Requirements — block-qa/v1 devil's-advocate (da-axis) extension

**For:** the folio-assistant agent (owner of `litlfred/folio-assistant`
`schemas/block-qa.ts` + the `block-qa-schema` cross-language package).
**From:** qou `local/devils-advocate-watcher` (PR #2688, branch
`claude/lucid-gates-92e98s`).
**Status:** qou has **pre-adopted** this schema — it already emits
`da-*` sidecar entries with the structured fields below (see the four
wave-1 `.qa.json` files in PR #2688). The folio-assistant validator
must be extended to **accept** them. Until it is, the fields are
additive/optional and a passthrough validator ignores them; this doc
asks you to make them first-class.

Canonical fragment to implement against:
[`block-qa-da-extension.schema.json`](block-qa-da-extension.schema.json)
(in this directory).

## Background

`local/devils-advocate-watcher` is a new qou integration-watcher child
(adversarial "why is this block wrong" review). It fans out four
referee lenses + an adjudicator per block and persists findings as
`<block>.qa.json` criteria, exactly like the voice / canonical /
q-usage axes — except these are **agent-only** (no script reviewer)
and carry adversarial metadata the current `QaCriterionEntry` has no
fields for.

## R1 — Extend `QaCriterionEntry` (producing types, `schemas/block-qa.ts`)

Add these **optional** fields (do **not** make them required — most
criteria never set them):

```ts
/** Refutation scope (AGENTS.md "Before declaring refuted"). */
scope?: "limited" | "structural";
/** Adjudicator ruling on a single objection. */
ruling?: "surviving" | "rebutted" | "partial";
/** The objection in the referee's voice (1-3 sentences). On a
 *  da-referee-verdict rollup entry, the strongest objection. */
referee_argument?: string;
/** What rebuts the objection, or "none — survived because …".
 *  For scope:"structural" this must name the proved invariant. */
rebuttal?: string;
/** Block-level rollup verdict. Set ONLY on da-referee-verdict entries. */
verdict?: "clean" | "survivable-objection" | "open-objection";
```

These compose with the existing `field_hash` / `result` / `severity`
/ `evidence` / `reviewer` / `reviewed_at` / `reviewed_sha` / `notes`
fields — no existing field changes shape.

## R2 — Consistency constraints (validator)

Enforce (see the JSON Schema `allOf` in the fragment):

| When | Require |
|------|---------|
| `ruling: "surviving"` | `result == "fail"` |
| `ruling: "partial"` | `result == "warn"` |
| `ruling: "rebutted"` | `result == "pass"` |
| `verdict: "open-objection"` | `result == "fail"` |
| `verdict: "survivable-objection"` | `result == "warn"` |
| `verdict: "clean"` | `result == "pass"` |
| `scope: "structural"` | `rebuttal` **and** `referee_argument` present and non-empty (the invariant must be named) |

The structural-scope guard is the schema-level enforcement of the
AGENTS.md (a)/(b) rule: no structural refutation without a cited
proved invariant.

## R3 — Register the `da-*` criterion ids

Add 13 criterion definitions to the registry (`da-false-claim`,
`da-vacuous`, `da-circular`, `da-overclaim`, `da-hidden-dof`,
`da-non-sequitur`, `da-lean-narrative-divergence`, `da-citation-misuse`,
`da-definitional-ambiguity`, `da-empirical-fragility`,
`da-physical-implausibility`, `da-reproducibility`, and the rollup
`da-referee-verdict`). Ids, `default_severity`, and one-line summaries
are in the fragment's `daCriteria` block. All are **agent-only**:
`getCriterionSourceFile()` / the script-sidecar machinery must treat
them as having no script reviewer (they never appear in
`qa-checkers-*.ts`; staleness is by `field_hash` drift only, not by
`script_hash`).

## R4 — Mirror in the cross-language `block-qa-schema` package

Reflect R1–R3 in all three mirrors so the interchange schema stays
consistent across languages:

- **JSON Schema** — fold the fragment's `$defs` into the canonical
  `block-qa/v1` schema (the four optional fields + the constraints).
- **Zod** (`@litlfred/block-qa-schema`) — add the optional fields +
  a `.refine()` for each R2 constraint.
- **Pydantic** (`block-qa-schema` PyPI) — add the optional fields +
  `@model_validator` for the R2 constraints.

Corpus-validate against the four wave-1 sidecars shipped in qou PR
#2688 (they are the conformance fixtures):
`mass-theory/borromean-baryon-mass-formula.qa.json`,
`observations/three-calibration-discipline.qa.json`,
`appendix-mass-binding-algorithms/mba-sidecar-delta-lambda-closure.qa.json`,
`appendix-qvalues/qbeta-ck-truncation-canonical.qa.json`.

## R5 — Reviewer registry

Register `local/devils-advocate-watcher` as a known `agent_skill`
value for `reviewer.kind: "agent"` entries (alongside
`local/qa-agent-drain`, the voice axis, etc.).

## R6 — Non-goals

- No script checker for any `da-*` criterion (the axis is inherently
  semantic / agent-judged). Do **not** add `qa-checkers-da.ts`.
- No change to the `result` enum (`pass|fail|warn|n/a`), the
  `field_hash` mechanism, or the multi-reviewer array shape.
- Rendering: `da-*` findings are author-facing QA, not publication
  content — they must **not** surface in the LaTeX/HTML render of a
  block (same as every other sidecar criterion).

## Acceptance

1. The four wave-1 `.qa.json` fixtures validate clean under the
   extended Zod + Pydantic + JSON Schema.
2. A sidecar with `scope:"structural"` and no `rebuttal` is **rejected**.
3. A sidecar with `ruling:"surviving"` and `result:"pass"` is **rejected**.
4. Existing (non-da) sidecars still validate unchanged.
