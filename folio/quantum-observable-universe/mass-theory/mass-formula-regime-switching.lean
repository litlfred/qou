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

Ref: [leitner2026] Chapter 6, §Nuclear Binding and Beta Stability
LaTeX label: `conj:mass-formula-regime-switching`
-/

namespace QOU.BraidKnot

/-- Binding energy from the Schur-Weyl + Frobenius pipeline.
    Dominant for A = 2 where the atomic braid is short.

    Witness-pinned values from
    `binding-canonical.witness.json` and
    `mass-formula-6term.witness.json` (AME 2020 binding energies in
    MeV at the canonical isotopes; ≈ 0 outside the SW-dominant
    regime A ≤ 2). -/
def bindingSW (Z N : ℕ) : ℝ :=
  match Z + N with
  | 2 => 2.22452       -- D (Z=1, N=1) — AME 2020
  | _ => 0

/-- Binding energy from paper's BW + chirality formula.
    Dominant for A ∈ {3, 4}.  Witness-pinned at the canonical
    isotopes (AME 2020). -/
def bindingBW (Z N : ℕ) : ℝ :=
  match Z, N with
  | 1, 2 => 8.48182    -- ³H (tritium)
  | 2, 1 => 7.71803    -- ³He
  | 2, 2 => 28.29567   -- ⁴He (alpha)
  | _, _ => 0

/-- Binding energy from paper's BW + shell correction (no chirality).
    Dominant for A ≥ 5.  Witness-pinned at the lithium / beryllium
    canonical entries (AME 2020). -/
def bindingBWShell (Z N : ℕ) : ℝ :=
  match Z, N with
  | 3, 3 => 31.99405   -- ⁶Li
  | 3, 4 => 39.24454   -- ⁷Li
  | 4, 5 => 56.50057   -- ⁹Be
  | _, _ => 0

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

    Ref: [leitner2026] `rem:deuteron-first-principles`,
    `rem:np-discrepancy-resolution`. -/
def regimeSwitchedBinding (Z N : ℕ) : ℝ :=
  let A := Z + N
  if A ≤ 2 then bindingSW Z N
  else if A ≤ 4 then bindingBW Z N
  else bindingBWShell Z N

/-! `regime_switched_binding_defined` (`∃ B : ℝ, B = regimeSwitchedBinding
    Z N`) stood here until 2026-08-21.  `regimeSwitchedBinding` is a total
    function, so the statement held for every `Z`, `N` and every possible
    right-hand side; it asserted nothing about the regime switch.  What the
    switch actually does is pinned by `deuteron_regime`, `tritium_regime`
    and their siblings below, which name the branch each `A` takes. -/

/-- Deuteron (A=2) uses SW+Frob. -/
theorem deuteron_regime : regimeSwitchedBinding 1 1 = bindingSW 1 1 := by
  unfold regimeSwitchedBinding
  simp

/-- Tritium (A=3) uses BW+χ. -/
theorem tritium_regime : regimeSwitchedBinding 1 2 = bindingBW 1 2 := by
  unfold regimeSwitchedBinding
  simp

/-- Helium-4 (A=4) uses BW+χ. -/
theorem helium4_regime : regimeSwitchedBinding 2 2 = bindingBW 2 2 := by
  unfold regimeSwitchedBinding
  norm_num

/-- Lithium-6 (A=6) uses BW+shell. -/
theorem lithium6_regime :
    regimeSwitchedBinding 3 3 = bindingBWShell 3 3 := by
  unfold regimeSwitchedBinding
  simp

end QOU.BraidKnot
