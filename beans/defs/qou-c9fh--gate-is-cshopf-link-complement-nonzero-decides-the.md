---
# qou-c9fh
title: 'GATE: is CS(Hopf link complement) nonzero? Decides the deuteron complex-volume resolution'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T09:39:35Z
updated_at: 2026-11-22T21:52:51Z
parent: qou-n4nr
---

## Round 73 Progress (`litlfred/qou#8257`)
- **Lean module**: `folio/quantum-observable-universe/lean/QOU/QBeta/HabiroCyclotomicRecurrenceAndHopfCSBrick.lean` (`hopf_link_chern_simons_pairing_nonzero_criterion`)
- **Summary**: Proved polarization identity `2 * u1 * u2 = ((u1 + u2)^2 - (u1 - u2)^2) / 2`, symmetry, and strict non-vanishing `2 * u1 * u2 != 0` whenever `u1 != 0` and `u2 != 0` for the Hopf link Chern-Simons torsion pairing.
- **80-dps Probe & Witness**: `computations/probes/habiro_cyclotomic_recurrence_and_hopf_cs_brick_probe.py` -> `computations/probes/habiro-cyclotomic-recurrence-and-hopf-cs-brick.witness.json` (`scriptCommitSha: aee44290d86add18624df3d3bce0a730246dc422`, PR head `eb8e68feba9367aa951532accb9ea1ab3a723c3a`)
- **PR**: https://github.com/litlfred/qou/pulls (`status: in-progress` pending merge)

## 2026-11-22 — wave-2 drain (thread "Work the volume conjecture beans")

**Answered: the complex volume of the Hopf-link complement is 0, so the gate closes negative.** `S³ ∖ Hopf ≅ T² × (0,1)`, `π₁ = ℤ²`. (A) A boundary-parabolic representation sends a generator to a nontrivial unipotent `U_b`; its centraliser in `SL₂` is `±P` (proved: `commute_unipotent_iff`, `eq_pm_unipotent_of_commute`), so `ρ` factors through `±P`, and the fundamental class in `H₃(SL₂ℂ, P)` comes from `H₃(P, P) = 0`: `Vol + i·CS = 0`. (B) For any representation, a flat connection on `T² × I` is gauge-equivalent to a pullback from `T²`, and the Chern–Simons 3-form of a pullback from a 2-dimensional base vanishes pointwise (proved: `alternating_three_eq_zero_of_finrank_two`, `pullback_alternating_three_eq_zero`), so `CS = 0` with the product boundary trivialisation. `Vol = 0` for every representation by Gromov–Thurston (simplicial volume of a Seifert-fibred manifold is 0). Scope (b), structural, with those invariants; the topological steps are cited (Garoufalidis–Thurston–Zickert 2011 §4.1, §6.1, §7; Gromov 1982), the algebraic ones are proved in `QOU/Archimedean/HopfLinkComplexVolume.lean` (commit `0e203a4cb` on branch `claude/volume-conjecture-bean-drain-2026-11-22`; sorry-free, axioms [propext, Classical.choice, Quot.sound], lean-direct exit 0; PR pending owner approval; audit `docs/audits/2026-11-22-hopf-link-complement-complex-volume.md`). Consequence, per the gate's own wording in `docs/audits/2026-08-07-two-row-projection-is-the-pairwise-cap.md` §4: the "deuteron carried on the CS axis" resolution dies; a nonzero value could only come from a hand-picked boundary trivialisation, i.e. a convention chosen to fit. No physical quantity is used in the argument. Bean stays in-progress until the PR merges.

## 2026-11-22 — applicability review (owner instruction, thread "Work the volume conjecture beans")

**Verdict: ALREADY-DONE.** ALREADY-DONE in substance: answered 0 (structural, scope b) in docs/audits/2026-11-22-hopf-link-complement-complex-volume.md and QOU/Archimedean/HopfLinkComplexVolume.lean on branch claude/volume-conjecture-bean-drain-2026-11-22, PR awaiting owner card. On review it is consistent with Ruling A (2026-08-29: deuteron binding is not a hyperbolic-volume term); the result adds that the CS axis is empty too. Complete once the PR merges.

## 2026-11-22 — merged
PR #9141 merged to main (3a1a9e87e). Gate answered: CS(Hopf complement) = 0, structural (scope b); HopfLinkComplexVolume.lean + audit on main.
