import Mathlib.Tactic

/-
  Why the Δ_λ residual's linear isospin coefficient `b` is A-independent.

  Follow-up to `DeltaLambdaExponentKeystone.lean` (#3089) and `DeltaLambdaIMME.lean`
  (#3104). The IMME residual `log_{q₀} Δ_λ = a(A) + b·T₃ + c·T₃²` was measured to
  have a **constant** `b ≈ −1.75` across A=6–12 (ladder A=3,6,7,8,10,12, probe
  `delta_lambda_imme_triplet.py`). This file gives the structural reason.

  The bar-odd writhe `σ−σ⁻¹ = 4Z` (the source of the `b·T₃` term) splits as

      4Z = 2(Z+N) + 2(Z−N) = 2A + 4T₃ ,     T₃ = (Z−N)/2,

  i.e. an isoscalar part `2A` plus an **isovector part `4T₃` whose slope (4 per
  unit T₃) is UNIVERSAL — independent of A**. So if the residual's odd part is
  proportional to the writhe's odd part with an A-independent coefficient `κ`,
  then `b = 4κ` is automatically constant in A. The measured constancy
  (`b ≈ −1.747 ± 0.03`, `κ = b/4 ≈ −0.437`) is exactly this proportionality.

  NOTE (numerology guard): `b ≈ −1.747` sits within 0.9 % of `−√3 = −1.732`, but
  inside the ±0.03 scatter, with no structural derivation of `√3` — it is a
  NEAR-MATCH only, deliberately NOT asserted here (Δ_λ gate). What IS proved is
  the *constancy mechanism* below, not the value.

  All `ring` over a generic `[CommRing R]` (§7c: pure algebra; the residual
  values live in `ℝ` only at the evaluation site).

  -- Ref: [leitner2026] docs/audits/2026-06-29-delta-lambda-residual-synthesis.md
-/

namespace QOU.BraidKnot

/-- **Derived.** The writhe `4Z` splits into an isoscalar part `2(Z+N) = 2A` and
an isovector part `2(Z−N) = 4T₃`. The isovector coefficient is the constant `2`
(per unit `Z−N`) — UNIVERSAL, independent of `A`. -/
theorem writhe_isospin_split (Z N : Int) :
    4 * Z = 2 * (Z + N) + 2 * (Z - N) := by ring

/-- The isovector (odd, `Z↔N`-antisymmetric) part of the writhe is `2(Z−N)`, and
its mirror difference `4(Z−N)` carries NO `A`-dependence — the slope in the
isospin variable is the same at every mass number. -/
theorem writhe_isovector_mirror (Z N : Int) :
    (4 * Z - (4 * N)) = 4 * (Z - N) := by ring

/-- **The constancy mechanism (proved; the proportionality is the hypothesis).**
Model the residual as `r Z N = base(Z+N) + κ·(Z−N)` — an isoscalar baseline plus
an isovector term *linear in `Z−N` with an `A`-independent coefficient `κ`* (the
structural ansatz suggested by the writhe's universal isospin slope). Then the
mirror difference is `2κ·(Z−N)`, with `κ` the **A-independent** slope: this is
exactly why the measured `b` (= the per-`T₃` slope = `4κ`) is constant in `A`.

The file asserts nothing about the value of `κ` (the open per-writhe coefficient,
`κ = b/4 ≈ −0.437`); only that *if* the odd part is writhe-proportional with
A-independent `κ`, the mirror slope cannot depend on `A`. -/
theorem constant_b_from_writhe_proportional {R : Type*} [CommRing R]
    (base : Int → R) (κ : R) (Z N : Int) :
    (base (Z + N) + κ * (Z - N)) - (base (N + Z) + κ * (N - Z))
      = 2 * κ * (Z - N) := by
  rw [add_comm N Z]; ring

/-- Subtracting twice the linear difference from the mirror residual cancels to zero (`qou-k3er`). -/
theorem constant_b_from_writhe_proportional_sub_eq_zero {R : Type*} [CommRing R]
    (base : Int → R) (κ : R) (Z N : Int) :
    ((base (Z + N) + κ * (Z - N)) - (base (N + Z) + κ * (N - Z))) - 2 * κ * (Z - N) = 0 := by
  rw [constant_b_from_writhe_proportional base κ Z N, sub_self]

end QOU.BraidKnot
