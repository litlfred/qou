---
# qou-3jgd
title: '2A: Borel singularity = period of A-polynomial for 4_1'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-30T01:05:37Z
updated_at: 2026-11-22T21:33:04Z
parent: c7vs
---

## Round 72 Progress (`litlfred/qou#8252`)
- **Lean module**: `folio/quantum-observable-universe/lean/QOU/QBeta/FigureEightAPolyPeriodAndTakataHolonomicBrick.lean` (`figure_eight_a_poly_discriminant_and_amphicheiral_recip`)
- **Summary**: Proved parabolic cusp factorization `figureEightAPoly 1 L = (L + 1)^2`, double root `figureEightAPoly 1 (-1) = 0`, and amphicheiral Borel period cancellation `omega_plus + (-omega_plus) = 0`.
- **80-dps Probe & Witness**: `computations/probes/figure_eight_a_poly_period_and_takata_holonomic_brick_probe.py` -> `computations/probes/figure-eight-a-poly-period-and-takata-holonomic-brick.witness.json` (`scriptCommitSha: 5c4e30462ed53f77f251c4ddf47409b4459308ef`, PR head `f6277d470f462db4f8fd3f013f12ae4b9781d94b`)
- **PR**: https://github.com/litlfred/qou/pull/8252 (`status: in-progress` pending merge)

## 2026-11-22 — wave-2 drain (thread "Work the volume conjecture beans")

No change; open. The latest note above points at batch PR #8252, which is still open and unmerged; its theorems are short algebraic identities with the bean's quantities as free variables, and they do not bear on this bean's question. Treat this bean's state as what the earlier text says.

## 2026-11-22 — applicability review (owner instruction, thread "Work the volume conjecture beans")

**Verdict: APPLIES.** Formal mathematics (volume conjecture, Lean hyperbolic/AJ infrastructure, Mathlib gaps). Checked its premises against owner-rulings.md on main: it uses none of the retired ones (σ₀σ₁ photon, trefoil electron, convention C, z = 1 Q_β base, census selection, absolute mass, muon pin A, substrate-q₀ derivation, virtual photons, SM quark charges). Today's rulings (strand colour states, b = −qX on colour singlets with flavour trace values unchanged, convention D on the baryon sector, photon kept with fixed constant 1) do not reach knot-complement geometry. Its batch-PR notes (Nov 16–18 Round PRs) are all still open and unmerged as of 2026-11-22.
