import Mathlib.Data.Real.Basic

/-!
# Mass formula regime switching

The unified knot mass formula (thm:knot-mass-formula-unified) sums
six structural terms, but naïve summation double-counts because
the paper's BW coefficients and Schur-Weyl descended trace compute
overlapping partition-sum content.  The correct formula is regime-
switched:

  B(Z, N) =
    SW+Frob if A ≤ 2,
    BW+χ    if 3 ≤ A ≤ 4,
    BW+shell if A ≥ 5.

Ref: [manuscript] Chapter 6, §Nuclear Binding and Beta Stability
LaTeX label: `prop:mass-formula-regime-switching`
-/

namespace QOU.BraidKnot

/-- Binding energy from the Schur-Weyl + Frobenius pipeline.
    Dominant for A = 2 where the atomic braid is short. -/
noncomputable opaque bindingSW (Z N : ℕ) : ℝ

/-- Binding energy from paper's BW + chirality formula.
    Dominant for A ∈ {3, 4} where figure-eight topology applies. -/
noncomputable opaque bindingBW (Z N : ℕ) : ℝ

/-- Binding energy from paper's BW + shell correction (no chirality).
    Dominant for A ≥ 5. -/
noncomputable opaque bindingBWShell (Z N : ℕ) : ℝ

/-- **Regime-switching mass formula.**

    The binding energy prescription depends on the atomic number A:

      B(Z, N) = bindingSW        if A ≤ 2
              = bindingBW        if 3 ≤ A ≤ 4
              = bindingBWShell   if A ≥ 5.

    Empirical verification (`mass_formula_6term.py`):
      D:    SW+Frob gives +2.1%; BW+χ gives -353%
      T:    SW+Frob gives -79%;  BW+χ gives +0.51%
      ³He:  SW+Frob gives -73%;  BW+χ gives +0.86%
      ⁴He:  SW+Frob gives -94%;  BW+χ gives -4.07%

    Regime switching is required because SW and BW compute
    overlapping content (same Wedderburn partition sum at the
    Hecke algebra level) — simply adding them double-counts.

    Ref: [manuscript] `rem:deuteron-first-principles`,
    `rem:np-discrepancy-resolution`. -/
def regimeSwitchedBinding (Z N : ℕ) : ℝ :=
  let A := Z + N
  if A ≤ 2 then bindingSW Z N
  else if A ≤ 4 then bindingBW Z N
  else bindingBWShell Z N

/-- The regime-switched formula is well-defined for all (Z, N). -/
theorem regime_switched_binding_defined (Z N : ℕ) :
    ∃ B : ℝ, B = regimeSwitchedBinding Z N :=
  ⟨regimeSwitchedBinding Z N, rfl⟩

/-- Deuteron (A=2) uses SW+Frob. -/
theorem deuteron_regime : regimeSwitchedBinding 1 1 = bindingSW 1 1 := by
  unfold regimeSwitchedBinding
  simp

/-- Tritium (A=3) uses BW+χ. -/
theorem tritium_regime : regimeSwitchedBinding 1 2 = bindingBW 1 2 := by
  unfold regimeSwitchedBinding
  decide

/-- Helium-4 (A=4) uses BW+χ. -/
theorem helium4_regime : regimeSwitchedBinding 2 2 = bindingBW 2 2 := by
  unfold regimeSwitchedBinding
  decide

/-- Lithium-6 (A=6) uses BW+shell. -/
theorem lithium6_regime :
    regimeSwitchedBinding 3 3 = bindingBWShell 3 3 := by
  unfold regimeSwitchedBinding
  decide

end QOU.BraidKnot
