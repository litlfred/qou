---
# cldt
title: 'Clarity EPIC: clarity-defn-tight bucket — 61 genuine editorial cases (drain deliberately, per-block rewriting)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-12T00:55:00Z
updated_at: 2026-10-04T15:17:56Z
parent: qou-mub3
---

## Assessment (2026-07-12)

`definition-clarity-audit.ts clarity-defn-tight` reports **61 fails** (pass 208).
Unlike `clarity-defn-misplaced` (11/11 false positives, bean `clab`) and
`clarity-defterm-bold` (~50% checker artifacts, fixed in PR #3632), this bucket is
**genuine editorial debt** — the flags are objective structural measurements, not
term-normalization artifacts:

| reason | count (approx) | meaning |
|---|---|---|
| `rambling: N sub-sections (>=3)` | ~23 | definition block has ≥3 bold sub-headers; should be one tight statement |
| `rambling: N-word preamble (>60)` | ~20 | too much context before the actual definition |
| `rambling: N prose words (>250)` | ~18 | the definition block is over-long overall |

These are **real** "the definition rambles" cases. Draining them is **per-block
rewriting** (move the definitional statement up-front, trim preamble to the
essential setup, split multi-concept sub-sections into follow-on `remark`s,
condense prose) — with `scientific-accuracy` + `readability-editing` judgment so
no necessary mathematical setup is lost. NOT mechanical; NOT a checker fix.

## Why not drained here

Deliberately deferred: rushing 61 definition rewrites at the tail of a long session
risks dropping necessary setup from a `definition` block (worse than the rambling).
This bucket wants fresh-context, careful per-block editorial attention.

## Worst offenders (start here — longest/rambliest first)

- `def:sign-sequence-of-braid` (331-word preamble + 331 prose words)
- `def:birthday-grading` (335 words, 105-word preamble)
- `def:surreal-blowup-calculus` (122-word preamble)
- `def:categorical-mordell-weil` (252 words)
- `def:hopf-diquark`, `def:substrate-line-bundle` (≥3 sub-sections)
- (full list: run `bun run content/pipeline/definition-clarity-audit.ts --json /tmp/c.json`
  then filter `criterion==clarity-defn-tight && result==fail`)

## Definition of done

Each flagged `definition` block reads as one tight statement (defterm-bold term,
minimal setup, interpretation moved to a follow-on `remark`), re-verified
`clarity-defn-tight pass`. Route through `scientific-accuracy` (claim integrity) +
`readability-editing` (prose) per block; do NOT delete mathematical content to
satisfy the word count.

## Full 46-block triage (2026-07-12, 3 parallel agents) + checker FP fixes (PR #3679)

Reviewed EACH remaining fail. FP classes fixed in the checker (PR #3679, 46→34):
first-bold anchor (math-term-leading defs), table-text-not-prose, §7c/`:`-component
sub-section exclusion, algorithm-spec exemption.

**Agent-confirmed FALSE POSITIVES (do NOT hand-edit):**
- cleared by #3679: frobenius-hopf-substrate, yekutieli-triple, division-algorithm,
  gs-quotient-ideals, phi-q-piece(core), q-angular-momentum, z-habiro-ring,
  universal-ilp-algorithm, jet-stratified-reduction.
- RESIDUAL FP (checker can't distinguish w/o over-correcting genuine; leave as-is):
  substrate-line-bundle, q-navier-stokes, q-momentum, molecular-hopf-chain,
  confinement-category, typed-garside-element (tuple/construction defs);
  categorical-mordell-weil, co-molecular-braid (dense/multi-stage intrinsic length).

**Agent-confirmed GENUINE (hand-fix, per-block extraction to follow-on remark/example):**
| block | fix |
|---|---|
| hopf-diquark | 4 property/interpretation sections → remarks |
| planck-time | Interpretation/Regime/Field-realisations → remarks; split **Planck length** to own def |
| observable-subcategory | Observability/Complement/Connected-components → remarks; aeons its own def |
| big-bang-state (mild) | Relation-to-jet-horizon + Existence-not-assumed → remarks |
| threading-link (mild) | Component-structure + Alexander-polynomial → remark/example |
| arc-space | Identification-with-brane-tower + Role-of-arc-spaces → remarks |
| algebraic-quantum-volume (mild) | Structure-of-sum + Substrate-isolation → remarks |
| per-nucleon-channel-decomposition | proton/neutron tables → example; S3^A + four-channels → remarks |
| stable-atom (mild) | Independence + Connection-to-LP(proton ex) → remarks |
| isotope-knot (mild) | two consequence sections → remarks |
| nucleon-hecke-element | Proton/Neutron evals → example; Normal-form → remark/prop |
| dressed-particle | Examples → example; Composition/Stability/Markov-functoriality → remarks |
| quantum-bloch-group | connection-list/why/Kashaev/pre-archimedean → remarks |
| qou-motivic-galois-instance | verification/downstream/coherence → remarks; keep frobenius map + Lean instance |
| stable-nucleus | Restricting-hadron + not-an-axiom → remark |
| categorical-meson | worked Hecke reduction → example; particle-content → remark |
| confinement-level | split k_max to own def; magic/categorical/q-dep → remarks |
| birthday-grading | cut preamble; q=1+ε example → example; Rep_ℝ/relaxed-axiom → remark; split b(x) + graded-hom |
| confined-particle | 8 examples → example block |
| sign-sequence-of-braid | bold+front the surr(β,t) construction; motivation+Jones-refinement → remarks |
| adelic-substrate | Motivation + Tate-integral development → remarks |
| archimedean-realization-functor | naming caveat → authorNotes; Realization/Synthesis → remarks |
| motivic-mass-measure | Motivic-rationale + R_top pointer → remark |
| motivic-substrate (mild) | Canonicity + Relation-to-existing → remarks |
| unstable-atom | (multi-flag; parallel to stable-atom) extract examples/consequences |

These need per-block extraction to NEW follow-on `remark`/`example` blocks (.ts+.md +
manifest) — real structural content work, best done carefully in batches with fresh
context, NOT a rushed sweep. sign-sequence-of-braid + the "front/bold the buried
construction" ones are the cleanest in-block starters.
