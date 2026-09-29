import Mathlib.Analysis.SpecialFunctions.Complex.Analytic
import Mathlib.Analysis.SpecialFunctions.Pow.Real

/-!
# QOU.AlgebraicSubstrate.macroscopic_stability_equivalence

Macroscopic stability of the spacetime continuum, the Riemann hypothesis,
and critical-line behaviour of the Reeb spectrum, related as a **conjecture**:

(1) optimal error in the prime-counting Chebyshev function,
(2) all non-trivial zeros of ζ(s) on Re(s) = 1/2,
(3) the Reeb spectrum on the critical line under the classical limit functor.

LaTeX label: `conj:macroscopic-stability-equivalence`

## 🛑 Two inconsistent axioms removed (2026-08-22, bean `qou-rhax`)

This file previously carried

```
axiom macroscopic_iff_rh_axiom :
    ∀ (ψ : R_q → R_q) (ζ : ℂ → ℂ), MacroscopicStability ψ ↔ RiemannHypothesis ζ
axiom rh_iff_persistence_axiom :
    ∀ (ζ : ℂ → ℂ) (spectral_limit : ℕ → Fin 8 → R_q),
      RiemannHypothesis ζ ↔ SpectralPersistence spectral_limit
```

**Both prove `False`, and for the same structural reason:** each states an
`Iff` between two propositions whose arguments are quantified
**independently**. An `∀ a b, P a ↔ Q b` forces `P` to be constant in `a`
(fix any `b` and the right side no longer varies). `RiemannHypothesis` is
not constant in `ζ`: it holds vacuously at `ζ = fun _ => 1` (never zero)
and fails at `ζ = fun _ => 0` (every point of the strip is a zero, so
`s = 1/4` would force `1/4 = 1/2`). Feeding both into either axiom, with
one fixed right-hand argument, yields `False`.

Machine-checked at Lean v4.24.0: `lean`-direct on a standalone file
restating `rh_iff_persistence_axiom` derived `False` from it in four lines,
with `#print axioms` showing the derivation depends on nothing but that
axiom, `propext`, `Classical.choice` and `Quot.sound`.

A second, independent route was reported for
`rh_iff_persistence_axiom`: `SpectralPersistence` as it stood
(`(∀ n i, f n i = 1/2) → ∀ i, f 0 i = 1/2`) is a tautology inhabited by
`fun h i => h 0 i` — it says "if every level is ½ then level 0 is ½",
which is instantiation, not persistence. Either route suffices.

**Three further defects found while fixing this, all in the same file:**

* **The file had never compiled.** `lean`-direct reported 22 errors: the
  imports never provided `LaurentPolynomial`, two docstrings sat back to
  back before `macroscopic_iff_rh_axiom`, and the `noncomputable section`
  was never closed so the final `end` failed. It survived because content-
  block `.lean` siblings live outside `content/<paper>/lean/` and are
  therefore outside the `qou` package's `["QOU", "QOU.+"]` globs — nothing
  ever compiled it. That is the real reason the blast radius was contained.
* **`1/2 : R_q` does not elaborate.** `R_q = LaurentPolynomial ℤ` has no
  `Div`, so `SpectralPersistence` and `MacroscopicStability` were ill-typed
  as written. The critical line is an archimedean statement about `Re`; it
  is stated here over `ℝ`/`ℂ`, which is what it needs (§7c: the ordering,
  `|·|` and `rpow` below are genuinely archimedean).
* **The Weil attribution was wrong.** The axiom was headed *"External axiom
  (Weil 1948 explicit formula)"*. Weil's explicit formula is a duality
  between zeros and prime powers; no formulation of it makes RH equivalent
  to a proposition in which ζ does not occur. The citation is what made an
  arbitrary axiom look load-bearing, and it is not reinstated below.

## What replaces them

A single content-bearing **primary conjecture class** over one datum
(§3b, §3b-tax). Binding ζ, ψ and the Reeb spectrum into one structure is
the fix: the removed axioms related quantities that were never tied to a
common system. There is deliberately **no instance** — the honest state of
"RH ↔ our spectral condition" is *open*, not axiomatised
(§"Axiomatization is NOT a Proof").

The von Koch direction (1) ⟹ (2) is genuine classical mathematics, but it
is not in Mathlib and is not proved here, so it is carried as a class field
rather than as an axiom asserting it.
-/

set_option autoImplicit false

open Complex

namespace QOU.AlgebraicSubstrate

/-- Riemann hypothesis for a given candidate zeta function: every zero in
    the critical strip lies on the critical line. -/
def RiemannHypothesis (ζ : ℂ → ℂ) : Prop :=
  ∀ (s : ℂ), 0 < s.re → s.re < 1 → ζ s = 0 → s.re = 1 / 2

/-- Macroscopic stability: the Chebyshev-type function `ψ` satisfies
    `ψ(X) = X + O(X^{1/2+ε})` for every `ε > 0`.

    Stated over `ℝ`: the ordering, `|·|` and `rpow` are archimedean, so
    this sits on the archimedean side of the wall by necessity (§7c). -/
noncomputable def MacroscopicStability (ψ : ℝ → ℝ) : Prop :=
  ∀ (ε : ℝ), 0 < ε →
    ∃ (C : ℝ), 0 < C ∧ ∀ (X : ℝ), 2 ≤ X → |ψ X - X| ≤ C * X ^ (1 / 2 + ε)

/-- Critical-line behaviour of the Reeb spectrum: every eigenvalue, at
    every deformation level, has real part `1/2`.

    This is the statement the removed `SpectralPersistence` was meant to
    make. That version quantified over all levels in its hypothesis and
    concluded about level `0` only, which is instantiation and is provable
    outright; this one has content because it constrains the family. -/
def CriticalLineSpectrum (ρ : ℕ → Fin 8 → ℂ) : Prop :=
  ∀ (n : ℕ) (i : Fin 8), (ρ n i).re = 1 / 2

/-- One system: a candidate zeta function, its Chebyshev-type counting
    function, and the Reeb spectrum of the same substrate.

    The three fields exist to be related to **each other**. Quantifying
    over them independently is precisely the defect that made the removed
    axioms inconsistent. -/
structure SubstrateSpectralDatum where
  /-- The candidate zeta function. -/
  zeta : ℂ → ℂ
  /-- The associated Chebyshev-type prime-counting function. -/
  psi : ℝ → ℝ
  /-- Reeb eigenvalues, indexed by deformation level and by the eight
      generators. -/
  rho : ℕ → Fin 8 → ℂ

/-- **Primary conjecture (open — no instance is provided, and none should
    be added without a proof).**

    For one substrate datum, macroscopic stability, the Riemann hypothesis
    for that datum's zeta function, and critical-line behaviour of that
    datum's Reeb spectrum are pairwise equivalent.

    Field 1 is classical in one direction (von Koch 1901: RH implies the
    optimal Chebyshev error; the converse follows from the explicit
    formula) but is not available in Mathlib. Field 2 is the framework's
    own claim and is entirely open.

    Both fields quantify over the *same* `D`, so neither forces either side
    to be constant in its argument — the equivalence is between two
    properties of one system, which is what the informal statement always
    meant. -/
class MacroscopicStabilityEquivalence (D : SubstrateSpectralDatum) : Prop where
  /-- (1) ↔ (2): optimal Chebyshev error ↔ RH, for this datum. -/
  stability_iff_rh : MacroscopicStability D.psi ↔ RiemannHypothesis D.zeta
  /-- (2) ↔ (3): RH ↔ the Reeb spectrum of this datum on the critical line. -/
  rh_iff_critical_line : RiemannHypothesis D.zeta ↔ CriticalLineSpectrum D.rho

/-- **Macroscopic stability equivalence, conditional on the conjecture.**

    Derives the third equivalence (1) ↔ (3) — the one the class does *not*
    carry — by transitivity. This is a derivation from the hypotheses, not
    a projection of a field (§3b-cond item 5). -/
theorem macroscopic_stability_equivalence
    (D : SubstrateSpectralDatum) [h : MacroscopicStabilityEquivalence D] :
    MacroscopicStability D.psi ↔ CriticalLineSpectrum D.rho :=
  h.stability_iff_rh.trans h.rh_iff_critical_line

/-- The removed axiom's first refuting witness: RH holds vacuously for a
    nowhere-zero candidate. Kept so the inconsistency argument above is
    checkable in this file rather than only in the commentary. -/
theorem riemannHypothesis_const_one : RiemannHypothesis (fun _ => 1) := by
  intro _ _ _ h
  exact absurd h one_ne_zero

/-- The second refuting witness: RH fails for the identically-zero
    candidate, since `s = 1/4` lies in the strip and is a zero.

    Together with `riemannHypothesis_const_one` this shows
    `RiemannHypothesis` is not constant in `ζ`, which is exactly why an
    `Iff` against an independently-quantified proposition proved `False`. -/
theorem not_riemannHypothesis_const_zero : ¬ RiemannHypothesis (fun _ => 0) := by
  intro h
  have h4 : ((1 : ℂ) / 4).re = 1 / 2 := by
    refine h (1 / 4) ?_ ?_ rfl <;> norm_num
  rw [show ((1 : ℂ) / 4).re = 1 / 4 by norm_num] at h4
  norm_num at h4

end QOU.AlgebraicSubstrate
