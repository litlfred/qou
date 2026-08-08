---
# dsm1
title: 'GAP: 13 declarations whose docstring claims a `sorry` the body does not have'
status: todo
type: task
priority: high
tags:
    - lean
    - vacuity
    - proof-integrity
created_at: 2026-08-08T21:00:00Z
updated_at: 2026-08-08T21:00:00Z
---

Queue produced by the new `proof-docstring-sorry-mismatch` detector
(`content/pipeline/lean-vacuity-axiom-audit.ts`), added the same day. Each entry
is a **candidate**; the legit-vs-genuine call is an agent's, per the ledger.

## Why the detector exists

`detectSelfAssuming` gates on the projected **field name** (`CONCLUSION_FIELD`:
`claim_`, `_holds`, `_eq`, …). A class field named outside that convention is
invisible to it however plainly it posits the conclusion. Two live cases found by
hand on 2026-08-08 were missed for exactly that reason, both named `*_ident`:
`confinement_categorical` (`exact ctx.confinement_ident`) and
`nucleon_ordering_factorization` (`exact ctx.factorization_ident`). Both are now
fixed; the detector fires on both pre-fix versions, which is how it was validated.

The new criterion reads only the doc block and the body, so no naming choice can
dodge it.

## The 13

| file | declaration |
|---|---|
| `AlgebraicSubstrate/JointGaloisBraidFigure8.lean:134` | `kappa_commutes_bar` |
| `AlgebraicSubstrate/qou_obstruction_reduction.lean:90` | `kappa_vanishes_iff_chi` |
| `BraidKnot/OVTopAssembly.lean:203` | `identityB_general` |
| `BraidKnot/volume_perturbation.lean:80` | `volume_perturbation` |
| `BraidsKnots/mobius_frobenius_kernel.lean:78` | `mobius_frobenius_kernel` |
| `BraidsKnots/nsi_q_deformed_kernel.lean:159` | `nsi_q_kernel_identification` |
| `BraidsKnots/skein_mass_from_linking.lean:93` | `skein_mass_from_linking` |
| `FeynmanPathIntegrals/markov_identification.lean:88` | `markovTrace_branching` |
| `Interactions/ConfinementSDP.lean:141` | `ConfinementSDP` |
| `Molecular/shell_filling_rule.lean:145` | `shell_filling_rule` |
| `ParticleInteractions/four_term_pair_nucleon.lean:114` | `four_term_pair_nucleon` |
| `ParticleInteractions/mass_categorical_descent.lean:75` | `mass_categorical_descent` |
| `Torsion/neutron_proton_splitting.lean:91` | `neutron_proton_splitting` |

## Three were spot-checked; all three were true positives

Two of them assert the **precise opposite** of their own code:

- **`volume_perturbation`** — *"Stated with `sorry` + citation per AGENTS.md §1a
  disposition 2 — **no conclusion field on the class hands this back**."* The body
  is `exact ctx.volume_perturbation_claim`, and the class field is commented
  `(conclusion)`.
- **`shell_filling_rule`** — *"the unproved ones carry honest `sorry`s in their
  named sub-theorems …, **not projected conclusion fields**."* Both named
  sub-theorems are `exact ctx.inner_shells_fill` and `exact ctx.hund_rule`, and
  neither carries a `sorry`.
- **`kappa_vanishes_iff_chi`** — *"inherits that lemma's single honest `sorry`."*
  `qou_obstruction_reduction.lean` contains **no `sorry` in code at all**; the
  cited `obstruction_trace_gap` is `exact ⟨ctx.kappa0_eq_chi_A,
  ctx.phi_1_image_eq_chi_A⟩`.

The remaining 10 are **unread**. Do not assume they follow the same pattern.

## This one touches live work

`collatz_contact_boundary` derives `obstruction_removable_of_even_chi` through
`kappa_vanishes_iff_chi`, so its own docstring's *"derived from the universal
obstruction-reduction … no independent assumption"* bottoms out in an assumed
class field rather than a proof. The §7c base-ring port of that file (same PR) is
unaffected — it was about the coefficient ring — but the **derivation** claim
should be re-scoped when this bean is worked.

## Do NOT soften the regex

The obvious refinement — skip when the doc delegates the `sorry` to a sub-theorem
or an inherited lemma ("in their named sub-theorems", "inherits … `sorry`") —
would have suppressed **two of the three confirmed true positives**. Delegation is
precisely where the claim goes unchecked. Keep it high-recall; keep the call with
the agent.

## Honest disposition per item (AGENTS.md §1a)

1. **Prove it** — discharge the goal.
2. **Queue it** — delete the conclusion-bearing class field and restore a real
   `sorry` + `-- Ref:`, so the docstring becomes true. This is what was done for
   `confinement_categorical` and `nucleon_ordering_factorization`.
3. **Fix the prose** — if the projection is a legitimate §3b-cond composition,
   the docstring is simply wrong and should stop claiming a `sorry`.

Whichever is chosen, the outcome is that the prose and `#print axioms` agree.
