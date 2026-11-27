/-
Copyright (c) 2026 litlfred. All rights reserved.

# The bar-odd part of the mass endomorphism is carried entirely by the cross-term

Berezinian super-DM brick (bean `qou-jqof`, PR #4140 off-main). The mass endomorphism is the
Schur complement `𝓜 = A − t`, `t = B·D⁻¹·C` the off-diagonal cross-term and `A` the bar-even
diagonal (mass) block. The prior parity results (`BerezinianCrossTermParity`,
`BerezinianSelfAdjointCrossTerm`) established *which* block structure makes `t` bar-odd (the
`c₃` carrier). This file isolates the **source** of the bar-odd part: when `A` is bar-even
(`σA = A`, as a diagonal mass block must be), the diagonal contributes **nothing** to the
bar-odd part of `𝓜` — it is `−(t − σt)`, minus the cross-term's bar-odd part alone.

Consequence for the `q_cubic = C1` wall: the bar-odd `c₃` is sourced **entirely** by the
cross-term `t`, with no contamination from the bar-even mass `A`. So the (anti-fit-gated)
`q_cubic = C1` derivation is a statement about the cross-term `t = B·D⁻¹·C` only — the
diagonal mass drops out of the bar-odd (decay) face exactly.

**Scope.** The bar-odd isolation identity only. It does **not** derive `c₃`'s value
(`q_cubic = C1` stays the anti-fit-gated open wall, PR #4140). §7c: generic `CommRing`,
abstract `σ : R →+* R`, no `ℝ`. Sorry-free. No fit; nothing wired.

-- Ref: [leitner2026] docs/audits/2026-07-31-berezinian-selfadjoint-crossterm-bar-even.md
-/
import Mathlib.Algebra.Ring.Hom.Defs
import Mathlib.Tactic.Ring

namespace QOU.QBeta.BerezinianBarOddIsolation

variable {R : Type*} [CommRing R] (σ : R →+* R)

/-- **Bar-odd isolation.** For the mass endomorphism `𝓜 = A − t` with bar-even diagonal
`A` (`σA = A`), the bar-odd part `𝓜 − σ𝓜` equals `−(t − σt)` — minus the cross-term's
bar-odd part, with **no** contribution from the diagonal mass `A`. So `c₃` (the bar-odd
face) is carried entirely by the cross-term `t = B·D⁻¹·C`. -/
theorem barOdd_M_eq_neg_barOdd_crossTerm (A t : R) (hA : σ A = A) :
    (A - t) - σ (A - t) = -(t - σ t) := by
  rw [map_sub, hA]; ring

/-- **Even diagonal drops out of the bar-odd face (sum form).** For any bar-even `A`, adding
`A` to a cross-term `t` leaves the bar-odd part exactly unchanged: `(A + t) − σ(A + t) =
t − σt` (an exact equality, no sign convention). The bar-even mass is invisible to the decay
(bar-odd) channel. -/
theorem barEven_diagonal_invisible_to_barOdd (A t : R) (hA : σ A = A) :
    (A + t) - σ (A + t) = t - σ t := by
  rw [map_add, hA]; ring

end QOU.QBeta.BerezinianBarOddIsolation
