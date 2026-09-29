---
# qou-bybn
title: 13 declarations named *_iff* state no biconditional -- the structure-word class, drained of its bijection member
status: todo
type: task
priority: normal
created_at: 2026-09-14T19:56:26Z
updated_at: 2026-09-14T19:57:11Z
---

Measured 2026-09-14 while exploring `qou-mfdq` Finding 3 (PR #7401, issue #7400).
**Nothing renamed here** — per AGENTS.md §"ASK THE OWNER BEFORE CHANGING THINGS",
a rename tranche across 13 declarations in 11 files is not one of the two
exemptions, so it waits.

## The class

Taxonomy row 46: a declaration whose NAME asserts a mathematical **structure**
its own **statement** does not contain. Distinct from
`scripts/lean-borrowed-name-audit.py`, which asks whether a declaration is named
after an external *body* (Seifert, Kashiwara, Donaldson) whose theorem it does
not use — that audit's gate is `hits = borrowed_hits(name, doc); if not hits:
continue`, and a name borrowing *content words* rather than an eponym never
reaches it.

The type case was `pole_cusp_bijection_proved` (renamed to
`denomPolyLocal_roots_explicit` in #7371). Measured with
`scripts/lean-structure-word-audit.py`, it was the **sole** `bijection` member at
`926f2c71ec^` and the token is now empty — so that half of the class is drained.

## The 13 live members, all under one token

`*_iff*` with **no `↔` and no `Iff` anywhere in the statement OR the proof**
(verified against the whole declaration body, so not a parser artifact):

| file:line | declaration | what the type actually says |
|---|---|---|
| `mass-theory/q-pochhammer-partial-product.lean:66` | `denomPoly_root_iff` | one direction: `1 - x q^k = 0 → denomPoly q x n = 0` |
| `mass-theory/figure-eight-branching-rule.lean:96` | `figure_eight_b_zero_iff_row_or_col` | one direction |
| `lean/QOU/ColorTubeFibers.lean:50` | `mem_iff_shift_root` | hypothesis → a polynomial identity; no "mem" either |
| `lean/QOU/PAdicQuantumGroups.lean:87` | `padic_observability_iff_irreducible` | a single `∀`; neither named property appears |
| `lean/QOU/PAdicQuantumGroups.lean:170` | `unit_root_iff_skew_poisson_integrable` | `∀ y ∃ x, frobenius x = y` — Frobenius **surjectivity** |
| `lean/QOU/BringsSurface/BarLiftAmbiguity.lean:156` | `invLift_defect_eq_zero_iff` | conclusion is `≠ 0` — the name says `eq_zero` |
| `lean/QOU/Mass/LowerBoundCannotConstrainADifference.lean:113` | `diff_bounded_collapses_iff_saturated` | one direction |
| `lean/QOU/Mass/QGaugeSpectralRigidity.lean:215` | `gauge_scaling_fixes_colorCubic_iff` | hypothesis → `t = 1` |
| `lean/QOU/BraidKnot/PartitionLex.lean:306` | `partitionDom_not_iff_lexGt` | **defensible** — refuting one direction refutes the iff |
| `lean/QOU/SchurWeyl/OffDiagNonvanishing.lean:45` | `offDiag_eq_zero_iff` | one direction |
| `lean/QOU/Eightfold/NonetMixingUnconstrained.lean:128` | `no_mixing_iff_eigenvalues_are_diagonal` | a `charPoly` identity; no "no mixing" predicate |
| `lean/QOU/QBeta/FiveTwoEnvelopeWiring.lean:272` | `exp_saddle_iff_curve` | hypothesis → `curve x y = 0` |
| `lean/QOU/QBeta/WindingLatticeNormForm.lean:130` | `parity_flip_iff_golden` | a **conjunction** of two facts, not a biconditional |

**12 of 13 are genuine over-namings; `partitionDom_not_iff_lexGt` is defensible.**
The two `PAdicQuantumGroups` ones are the sharpest — same shape as
`pole_cusp_bijection_proved`, a name asserting properties the type does not
mention.

## Why it matters here specifically, and it is not style

Mathlib's convention is that `foo_iff_bar` **is** an `↔`; a one-directional
lemma is `bar_of_foo`. So the name is a claim about what was proved. An agent
running the corpus-grep checklist to ask *"is X ⟺ Y established?"* finds a
sorry-free `X_iff_Y` and stops. That is the trap `qou-mfdq` documents for
`pole_cusp_bijection_proved`, one token over.

`denomPoly_root_iff` is in the same arc: its converse is in fact true over a
domain (a product vanishes iff a factor does) — so the honest options there are
*prove the converse* or *rename to `_of_`*, and they are different amounts of
work.

## Options

1. **Rename all 12** to Mathlib style (`_of_`, `_imp_`, or drop the token).
   Cheap per site, 11 files, zero mathematical risk. Needs `lean`-direct on each
   changed file plus consumer updates; several are library modules with
   importers, so the blast radius is real and must be measured per site first.
2. **Prove the missing directions** where they are true (`denomPoly_root_iff`,
   `offDiag_eq_zero_iff` are the plausible ones) and rename the rest. More work,
   strictly better outcome, and it turns a naming defect into content.
3. **Do nothing.** The 13 stay, the audit keeps reporting them, and the
   corpus-grep trap stays live. Nothing downstream moves — none of these is
   cited as evidence for a physical claim as far as I measured.

**Recommendation (judgement, not a finding): option 2 for the two in the
`q-pochhammer` / `SchurWeyl` arcs where the converse is true and cheap, option 1
for the rest, as one reviewable tranche.** But it is a rename tranche across
library modules and it is the owner's call to start it.

## Reproduce

    python3 scripts/lean-structure-word-audit.py --token iff
    python3 scripts/lean-structure-word-audit.py --selftest

`--selftest` hardcodes nothing: it fails unless `pole_cusp_bijection_proved` is
the sole `bijection` hit at `926f2c71ec^`, unless that token is empty now, and
unless the Mathlib uniqueness idiom is NOT flagged.
