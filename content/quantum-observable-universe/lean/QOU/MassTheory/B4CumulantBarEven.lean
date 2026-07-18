/-
# Bar-evenness of the ⁴He writhe-exchange cumulant determinant

The Δ_λ magnitude front (2026-07-18, Vector 3) asks whether **bar-even
symmetrisation** of the connected `b_A = -ln det(I + m·S)` cumulant
(`b4_slater_antisymmetrizer_exchange_sign.py`, #3924) can isolate a mass
(bar-even) part from a decay (bar-odd) part and thereby tame the ⁴He
magnitude overshoot.

This file records the structural obstruction at `A = 4`.  The ⁴He writhe
exchange matrix `S` (diagonal `1`, off-diagonal `sgn·m` with pp = +1,
nn = -1, pn = +1 on the word `ppnn`) has the **symmetric spectrum**
`{±√5, ±1}`, so its shifted determinant has the closed form

  `det (I + m·S) = (1 - 5 m²)(1 - m²)`   =:  `he4WritheDet m`.

That the `4×4` determinant equals this closed form is verified **exactly**
(45-digit `mp.det` agreement, over the concrete symmetric matrix) in the
companion probe
`computations/deltalambda/deltalambda_bareven_b4_magnitude_probe.py`
(assertion `writhe_det_matches_closed_form`).  This file supplies the
other half: the closed form is a function of `m²` alone, hence **even in
`m`** (`he4WritheDet_bar_even`).

Consequence.  The cumulant `b₄ = -ln (he4WritheDet m)` is invariant under
`m ↦ -m`, which is exactly the bar involution `q ↦ q⁻¹` acting on a
bar-odd magnitude.  So at the dominant `A = 4` wall the bar-even
symmetrisation `½(b₄(q) + b₄(q⁻¹))` returns `b₄` unchanged: there is **no
bar-odd part to remove**, and Vector 3 cannot alter the ⁴He cumulant.

This is a *scope-(b) structural exclusion* of bar-even symmetrisation as a
fix for the `A = 4` overshoot (a proved invariant: evenness of the
determinant in `m`), not a scope-(a) numerical miss.  It complements — does
not re-derive — the 2026-06-25 scope-(b) pruning that ⁴He binding must be
bar-even (`docs/audits/2026-06-25-he4-magic-factor-bar-even-pruning.md`):
there the *observable* is forced bar-even; here the *cumulant carrier* is
shown to be already bar-even, so symmetrisation is a no-op.

Base ring: generic `CommRing R` (§7c) — no ordering, no `Real`; the
statement is a polynomial identity in the formal magnitude `m`.
-/
import Mathlib.Tactic.Ring

namespace QOU.MassTheory

variable {R : Type*} [CommRing R]

/-- Closed form of the ⁴He writhe cumulant determinant `det (I + m·S)`,
`S` the `ppnn` writhe exchange matrix with spectrum `{±√5, ±1}`.  (The
`det = this` equality is verified exactly against `mp.det` in
`deltalambda_bareven_b4_magnitude_probe.py`.) -/
def he4WritheDet (m : R) : R := (1 - 5 * m ^ 2) * (1 - m ^ 2)

/-- The ⁴He writhe cumulant determinant factors as `(1 - √5 m)(1 + √5 m)(1 - m)(1 + m)`,
i.e. it is `(1 - 5 m²)(1 - m²)` — exhibiting the symmetric `{±√5, ±1}`
spectrum as the four roots `m ∈ {±1/√5, ±1}`. -/
theorem he4WritheDet_eq (m : R) :
    he4WritheDet m = 1 - 6 * m ^ 2 + 5 * m ^ 4 := by
  unfold he4WritheDet; ring

/-- **⁴He cumulant is bar-even.**  `he4WritheDet` is a function of `m²`
alone, so it is invariant under `m ↦ -m`.  Hence the connected cumulant
`b₄ = -ln (he4WritheDet m)` is even in the magnitude `m`.  Under the bar
involution `q ↦ q⁻¹` acting on a bar-odd magnitude (`m ↦ -m`) this says
`b₄(q) = b₄(q⁻¹)`: bar-even symmetrisation is a **no-op** at `A = 4`, so it
cannot tame the ⁴He magnitude overshoot (the scope-(b) obstruction to
Vector 3). -/
theorem he4WritheDet_bar_even (m : R) : he4WritheDet (-m) = he4WritheDet m := by
  unfold he4WritheDet; ring

end QOU.MassTheory
