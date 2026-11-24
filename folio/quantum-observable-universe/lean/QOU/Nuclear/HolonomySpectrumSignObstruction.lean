/-
# A real-spectrum holonomy cannot produce the Q_β ladder's correction

Bean `qou-pdix` (child of `qou-cds1`), route 5 / branch 3.

## The gap this closes, and how it differs from the one already closed

`QOU.QBeta.PhaseFailsLogFunctionalEquation` excludes **constant-residue**
Kohno–Drinfeld holonomies: the scale is fixed (`braiding = P exp(ħt/2)`, `t`
eigenvalues `±1`, matched to the Hecke eigenvalues `{q, −q⁻¹}` by `ħ = 2 ln q`),
so a constant-residue holonomy angle is `c · ln q`, and `α` fails the doubling
identity `f(q²) = 2 f(q)` that every such `c · ln` satisfies. That bean records
what survives: *"a connection whose residues depend on `q`, a non-flat
construction, or a genuinely `q`-dependent-parameter transcendental object is
untouched"*.

**This file closes all three of those at once**, by a sign argument that never
looks at the residues.

## The argument

The ladder's correction is read as the normalised character of a holonomy — that
is the `EigenphaseCarrier` shape, `tr M = 2 cos α`. Measured at the proton pin,
that character must be **strictly below 1**:

    Q_β/Q_A            = 0.998325…      (the full correction)
    cos(θ_C)           = 0.998399…      (the ladder's cosine factor alone)

But if the holonomy generator has **real** spectrum `±a` — which is what
`ħ = 2 ln q` gives at the substrate's real `q₀ = 1.10998 > 1`, since then
`ħ/2 = ln q₀` is real — the character is

    (eᵃ + e⁻ᵃ)/2 = cosh a  ≥  1        for every real a,

with equality only at `a = 0`. `real_spectrum_character_ge_one` below. The bound
holds for **every** real `a`, so it is insensitive to what the residues are or
how they depend on `q`: a `q`-dependent residue merely changes which `a` appears,
and `a` is still real.

At the Kohno–Drinfeld value the miss is explicit and elementary —
`kd_character_sub_one`:

    (q + q⁻¹)/2 − 1 = (q−1)²/(2q)

a square over a positive, hence never negative; numerically `1.005448` against a
required `0.998399`. Wrong **side** of 1, by 0.706 %.

## What this leaves route 5

Not "find a connection" but: **find one whose generator is elliptic at real `q`**
— `det A > 0` for the traceless generator, i.e. spectrum `±iθ` rather than `±a`.
The Kohno–Drinfeld scale-fixing the corpus itself cites does the opposite: it
makes `ħ` real, hence the generator hyperbolic. So the surviving construction must
put the imaginarity somewhere, and the corpus already has a name for that place —
`conj:im-q-physical-role`, whose "phase coordinate" candidate role is exactly
this. That is a materially narrower and more checkable ask than the open
construction problem `qou-pdix` currently records.

It is also a **new tier-0 discriminator** for that bean's D1–D6 acceptance test,
and one no script there can run for the same reason D5/D6 cannot: it is a
condition on the *generator*, read from the construction, not on `α`'s output.
(The "cosh-shaped" row in that test's validation table is a different check — the
shape of `α` as a function of `q`, not the spectrum of the generator.)

## Scope

Scope-(b): a structural exclusion citing a proved inequality. It does **not**
show no connection exists, does not derive `α`, and wires nothing. It shows that
any holonomy reading with a real-spectrum generator lands on the wrong side of 1,
whatever its residues — so the elliptic requirement is not optional.
-/
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity

namespace QOU.QBeta

/-- `x + x⁻¹ ≥ 2` for positive `x` — the whole obstruction in one line, and the
reason it cannot be evaded by choosing residues: it holds for *every* positive
`x`, so every real generator eigenvalue is caught. -/
theorem two_le_add_inv {x : ℝ} (hx : 0 < x) : 2 ≤ x + x⁻¹ := by
  have h : x + x⁻¹ - 2 = (x - 1) ^ 2 / x := by field_simp; ring
  have h3 : 0 ≤ x + x⁻¹ - 2 := by
    rw [h]; exact div_nonneg (sq_nonneg _) hx.le
  linarith

/-- **A holonomy with real spectrum has character at least 1.** If the generator's
eigenvalues are `±a` with `a` real, the normalised character `tr M / 2` is
`cosh a ≥ 1`.

This is the residue-independent step: it is quantified over **all** real `a`, so a
`q`-dependent residue only changes which `a` occurs and the bound is unmoved. -/
theorem real_spectrum_character_ge_one (a : ℝ) :
    1 ≤ (Real.exp a + Real.exp (-a)) / 2 := by
  have hx : 0 < Real.exp a := Real.exp_pos a
  have hinv : Real.exp (-a) = (Real.exp a)⁻¹ := by
    rw [Real.exp_neg]
  rw [hinv, le_div_iff₀ (by norm_num : (0 : ℝ) < 2)]
  linarith [two_le_add_inv hx]

/-- **Hence a sub-unit correction excludes every real-spectrum holonomy.** The
measured correction is `0.998…< 1`, so no real `a` reproduces it. -/
theorem correction_below_one_excludes_real_spectrum {κ a : ℝ} (hκ : κ < 1) :
    κ ≠ (Real.exp a + Real.exp (-a)) / 2 := by
  intro hEq
  exact absurd (hEq ▸ real_spectrum_character_ge_one a) (not_le.mpr hκ)

/-- The Kohno–Drinfeld character at the substrate's real `q`, elementarily:
`(q + q⁻¹)/2 − 1 = (q−1)²/(2q)`. A square over a positive, so the character never
drops below 1 — no analysis, no transcendence, no appeal to `cosh`. -/
theorem kd_character_sub_one {q : ℝ} (hq : 0 < q) :
    (q + q⁻¹) / 2 - 1 = (q - 1) ^ 2 / (2 * q) := by
  field_simp
  ring

/-- **The punchline.** With `ħ = 2 ln q` at real `q > 0`, the holonomy character
is `(q + q⁻¹)/2 ≥ 1`, so it cannot equal a correction strictly below 1. -/
theorem kd_holonomy_cannot_realise_subunit_correction {q κ : ℝ}
    (hq : 0 < q) (hκ : κ < 1) : κ ≠ (q + q⁻¹) / 2 := by
  intro hEq
  have h1 : 1 ≤ (q + q⁻¹) / 2 := by
    rw [le_div_iff₀ (by norm_num : (0 : ℝ) < 2)]
    linarith [two_le_add_inv hq]
  exact absurd (hEq ▸ h1) (not_le.mpr hκ)

/-- Equality holds only at the classical point `q = 1`, so the obstruction is
strict everywhere the substrate actually sits (`q₀ ≈ 1.10998`). -/
theorem kd_character_eq_one_iff {q : ℝ} (hq : 0 < q) :
    (q + q⁻¹) / 2 = 1 ↔ q = 1 := by
  constructor
  · intro hEq
    have h : (q - 1) ^ 2 / (2 * q) = 0 := by
      rw [← kd_character_sub_one hq, hEq]; ring
    have h2 : (q - 1) ^ 2 = 0 := by
      field_simp at h
      linarith [h]
    have h4 : q - 1 = 0 := by
      exact sq_eq_zero_iff.mp h2
    linarith
  · rintro rfl; norm_num

end QOU.QBeta
