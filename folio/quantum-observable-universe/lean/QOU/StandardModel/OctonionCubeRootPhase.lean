import QOU.StandardModel.OctonionColourTripletComplexType
import Mathlib.Algebra.Polynomial.AlgebraMap
import Mathlib.Tactic.LinearCombination

/-!
# QOU.StandardModel.OctonionCubeRootPhase — an order-3 central phase from a complex structure

Bean `qou-x08k`, octonion route (follows `QOU.Core.FlavourCentralPhase`).

`FlavourCentralPhase` reduces the non-self-duality of `W` to a central phase `ω` with
`ω³ = 1` and `1 - ω²` regular.  The octonions supply a complex structure: left multiplication
by a unit imaginary `e` gives `J6` on the colour triple, `J6² = -1`, commuting with the
`𝔰𝔲(3)` stabiliser (`su3ToEndTriplet_comm_J6`).  This file asks whether `J` yields the
phase.

## Results

* `cubeRootPhase` / `cubeRootPhase_sq_add_add_one` / `cubeRootPhase_cube` — **existence,
  generic ring**.  Over any commutative ring `R` with `s² = 3` and `2` invertible, for any
  `R`-linear `J` with `J² = -1`, `Ω := ½(s·J - 1)` satisfies `Ω² + Ω + 1 = 0`, hence `Ω³ = 1`.
  (`Ω` is `e^{2πJ/3}` written algebraically: `-½ + (√3/2) J`.)
* `cubeRootPhase_commute` — `Ω` commutes with every operator commuting with `J`; in particular
  with the whole `𝔰𝔲(3)` action, so it is central for that action.
* `no_rational_cubeRoot_phase` — **obstruction over `ℚ`**: no element `a + bJ` with
  `a, b ∈ ℚ` (and `1, J` independent) is a nontrivial cube root of unity.  Applied to the
  octonionic `J6`: `colourTriple_no_rational_cubeRoot_phase`.  The phase needs `√3` (equivalently
  `√-3`) adjoined to the base ring; `ℚ(J) ≅ ℚ(i)` does not contain `ω`.

## Honest label

This produces the phase on the **colour** triple.  It does not identify colour with flavour,
and it does not build `W` as an object of an abstract quantum observable universe.  What it
settles: the octonionic complex structure is enough to manufacture an order-3 central phase,
but only after adjoining `√3`; over `ℚ` it is impossible.  Pure algebra, no analytic or
empirical input.
-/

namespace QOU.StandardModel.OctonionCubeRootPhase

open Polynomial

section Generic

variable {R : Type*} [CommRing R] {M : Type*} [AddCommGroup M] [Module R M]

/-- The cube-root phase `Ω = h • (s • J - 1)`, where `h = ½` and `s = √3`. -/
def cubeRootPhase (h s : R) (J : Module.End R M) : Module.End R M := h • (s • J - 1)

/-- `Ω` is the value at `J` of the polynomial `h(sX - 1)`. -/
theorem cubeRootPhase_eq_aeval (h s : R) (J : Module.End R M) :
    cubeRootPhase h s J = aeval J (C h * (C s * X - 1)) := by
  simp [cubeRootPhase, Algebra.smul_def, mul_sub]

/-- The polynomial identity behind `Ω² + Ω + 1 = 0`. -/
theorem poly_identity (h s : R) (hs : s * s = 3) (hh : h * 2 = 1) :
    C h * (C s * X - 1) * (C h * (C s * X - 1)) + C h * (C s * X - 1) + 1
      = 3 * C h * C h * (X ^ 2 + 1) := by
  have hs' : C s * C s = (3 : R[X]) := by rw [← C_mul, hs]; exact map_ofNat C 3
  have hh' : C h * 2 = (1 : R[X]) := by rw [← C_1, ← hh, C_mul, map_ofNat]
  linear_combination (C h ^ 2 * X ^ 2) * hs' - (C h * C s * X + C h + 1) * hh'

/-- **`Ω² + Ω + 1 = 0`** for any complex structure `J`. -/
theorem cubeRootPhase_sq_add_add_one (h s : R) (hs : s * s = 3) (hh : h * 2 = 1)
    (J : Module.End R M) (hJ : J * J = -1) :
    cubeRootPhase h s J * cubeRootPhase h s J + cubeRootPhase h s J + 1 = 0 := by
  rw [cubeRootPhase_eq_aeval, ← map_one (aeval (R := R) J), ← map_mul, ← map_add, ← map_add,
    poly_identity h s hs hh, map_mul]
  simp [sq, hJ]

/-- **`Ω³ = 1`.** -/
theorem cubeRootPhase_cube (h s : R) (hs : s * s = 3) (hh : h * 2 = 1)
    (J : Module.End R M) (hJ : J * J = -1) : cubeRootPhase h s J ^ 3 = 1 := by
  have e := cubeRootPhase_sq_add_add_one h s hs hh J hJ
  set Ω := cubeRootPhase h s J
  have : Ω ^ 3 - 1 = (Ω - 1) * (Ω * Ω + Ω + 1) := by noncomm_ring
  rw [e, mul_zero] at this
  exact sub_eq_zero.1 this

/-- `Ω` commutes with every operator that commutes with `J`. -/
theorem cubeRootPhase_commute (h s : R) (J T : Module.End R M) (hTJ : Commute T J) :
    Commute T (cubeRootPhase h s J) :=
  ((hTJ.smul_right s).sub_right (Commute.one_right T)).smul_right h

end Generic

section Rational

variable {M : Type*} [AddCommGroup M] [Module ℚ M]

/-- **No rational cube-root phase.**  If `J² = -1` and `1, J` are `ℚ`-independent, no
`a + bJ` with `a, b ∈ ℚ` satisfies `x² + x + 1 = 0`. -/
theorem no_rational_cubeRoot_phase (J : Module.End ℚ M) (hJ : J * J = -1)
    (hind : ∀ c d : ℚ, c • (1 : Module.End ℚ M) + d • J = 0 → c = 0 ∧ d = 0)
    (a b : ℚ) :
    (a • 1 + b • J) * (a • 1 + b • J) + (a • 1 + b • J) + 1 ≠ 0 := by
  intro H
  have expand : (a • (1 : Module.End ℚ M) + b • J) * (a • 1 + b • J) + (a • 1 + b • J) + 1
      = (a * a - b * b + a + 1) • (1 : Module.End ℚ M) + (2 * a * b + b) • J := by
    simp only [add_mul, mul_add, smul_mul_smul_comm, one_mul, mul_one, hJ, smul_neg,
      add_smul, sub_smul, mul_smul, one_smul, two_smul]
    module
  rw [expand] at H
  obtain ⟨h1, h2⟩ := hind _ _ H
  have hb : b * (2 * a + 1) = 0 := by linarith
  rcases mul_eq_zero.1 hb with hb0 | ha
  · subst hb0
    nlinarith [sq_nonneg (2 * a + 1)]
  · have ha' : a = -1 / 2 := by linarith
    subst ha'
    -- `b² = 3/4` has no rational solution: `3` is not a square in `ℚ`
    have hb2 : (2 * b) * (2 * b) = 3 := by nlinarith
    have hsq : IsSquare (3 : ℚ) := ⟨2 * b, hb2.symm⟩
    rw [Rat.isSquare_iff] at hsq
    have h3 : IsSquare (3 : ℤ) := by simpa using hsq.1
    obtain ⟨r, hr⟩ := h3
    have h1 : r ≤ 2 := by nlinarith
    have h2 : -2 ≤ r := by nlinarith
    interval_cases r <;> omega

end Rational

open QOU.MathlibExt.OctonionDerivations QOU.StandardModel in
/-- **The octonionic colour triple has no cube-root phase over `ℚ` in `ℚ[J6]`.** -/
theorem colourTriple_no_rational_cubeRoot_phase (a b : ℚ) :
    (a • 1 + b • J6) * (a • 1 + b • J6) + (a • 1 + b • J6) + 1 ≠ 0 := by
  apply no_rational_cubeRoot_phase J6 J6_sq_eq_neg_id
  intro c d hcd
  have h0 := congrArg (fun T : Module.End ℚ (Fin 6 → ℚ) => T (Pi.single 0 1) 0) hcd
  have h2 := congrArg (fun T : Module.End ℚ (Fin 6 → ℚ) => T (Pi.single 0 1) 2) hcd
  simp [ColourTripletComplexType.J6_apply] at h0 h2
  exact ⟨h0, h2⟩

end QOU.StandardModel.OctonionCubeRootPhase
