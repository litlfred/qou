import Mathlib.Tactic

/-!
# `g_A⁽⁰⁾ = 5/3` on the symmetric cube of spin ⊗ flavour, and the moment ratio as a condition

Bean `qou-iw1d` (QFT-4, math-only core; epic `qou-3fjn`). Representation theory of
`(ℚ² ⊗ ℚ²)^{⊗3}` only; no measured number enters.

A one-quark state is a pair `(s, f) ∈ Fin 2 × Fin 2`: spin `s` (`0` = up, `1` = down) and
flavour `f` (`0` = `u`, `1` = `d`). Three-quark states are functions on `Q × Q × Q`; amplitudes are kept in `ℤ` so that every finite
check is a kernel `decide`.

* `pUp` is the (unnormalised) vector with amplitude `2` on the three arrangements of
  `u↑ u↑ d↓` and `−1` on the six arrangements of `u↑ u↓ d↑`. It is
  - **totally symmetric** under the three transpositions of the slots (`pUp_symm12`, `pUp_symm23`),
    so it lies in `Sym³(ℚ⁴)`;
  - annihilated by the total **spin-raising** operator `S₊` (`spinRaise_pUp`) and by the total
    **isospin-raising** operator `I₊` (`isoRaise_pUp`): it has total spin `1/2` and total isospin
    `1/2` (it is not a component of the spin-`3/2`, isospin-`3/2` decuplet);
  - of squared norm `18` (`pUp_normSq`).
* `axial_charge` — **`g_A⁽⁰⁾ = 5/3`**: `⟨p↑| Σᵢ σ_z⁽ⁱ⁾ τ₃⁽ⁱ⁾ |p↑⟩ = (5/3) ⟨p↑|p↑⟩`.
* `moment_p`, `moment_n` — for **arbitrary** flavour weights `e_u, e_d` (no values adopted), the
  operator `Σᵢ e(fᵢ) σ_z⁽ⁱ⁾` has expectation `(4e_u − e_d)/3` on `p↑` and `(4e_d − e_u)/3` on the
  flavour-swapped state `n↑`.
* `moment_ratio_iff` — the ratio is `−3/2` **iff** `e_u = −2 e_d`. The file proves the condition;
  it does not assert that the condition holds, so no quark charge is assumed (quark charges are
  derived elsewhere, owner ruling 2026-11-22).

## Scope

Dropped from the bean at its re-scope (owner card 2026-11-21): `g_A(q₀) = 1.2690` (an empirical
comparison) and the Bjorken sum rule (loop corrections and DIS data).
-/

namespace QOU.QFTMath.SpinFlavour

/-- One-quark spin ⊗ flavour basis: `(spin, flavour)`. -/
abbrev Q := Fin 2 × Fin 2

/-- Three-quark basis. -/
abbrev Q3 := Q × Q × Q

/-- `±1` sign of a `Fin 2` label (`0 ↦ 1`, `1 ↦ −1`). -/
def sgn (a : Fin 2) : ℤ := if a = 0 then 1 else -1

/-- Number of down-spins, of `d`-quarks, and of spin-down `d`-quarks in a configuration. -/
def nDown (x : Q3) : ℕ := (if x.1.1 = 1 then 1 else 0) + (if x.2.1.1 = 1 then 1 else 0) +
  (if x.2.2.1 = 1 then 1 else 0)
def nD (x : Q3) : ℕ := (if x.1.2 = 1 then 1 else 0) + (if x.2.1.2 = 1 then 1 else 0) +
  (if x.2.2.2 = 1 then 1 else 0)
def nDdown (x : Q3) : ℕ := (if x.1 = (1, 1) then 1 else 0) + (if x.2.1 = (1, 1) then 1 else 0) +
  (if x.2.2 = (1, 1) then 1 else 0)

/-- The spin-up proton state (unnormalised): `2` on arrangements of `u↑u↑d↓`, `−1` on
arrangements of `u↑u↓d↑`. -/
def pUp (x : Q3) : ℤ := if nD x = 1 ∧ nDown x = 1 then (if nDdown x = 1 then 2 else -1) else 0

/-- Flavour swap `u ↔ d` on each slot. -/
def flip (x : Q3) : Q3 :=
  ((x.1.1, 1 - x.1.2), (x.2.1.1, 1 - x.2.1.2), (x.2.2.1, 1 - x.2.2.2))

/-- The spin-up neutron state: the flavour swap of `pUp`. -/
def nUp (x : Q3) : ℤ := pUp (flip x)

theorem pUp_symm12 (a b c : Q) : pUp (a, b, c) = pUp (b, a, c) := by
  revert a b c; decide

theorem pUp_symm23 (a b c : Q) : pUp (a, b, c) = pUp (a, c, b) := by
  revert a b c; decide

/-- `S₊ ψ` at `x`: the total spin-raising operator, `Σᵢ σ₊⁽ⁱ⁾` (`σ₊` maps down to up). -/
def spinRaise (ψ : Q3 → ℤ) (x : Q3) : ℤ :=
  (if x.1.1 = 0 then ψ ((1, x.1.2), x.2) else 0) +
  (if x.2.1.1 = 0 then ψ (x.1, (1, x.2.1.2), x.2.2) else 0) +
  (if x.2.2.1 = 0 then ψ (x.1, x.2.1, (1, x.2.2.2)) else 0)

/-- `I₊ ψ` at `x`: the total isospin-raising operator (`d ↦ u`). -/
def isoRaise (ψ : Q3 → ℤ) (x : Q3) : ℤ :=
  (if x.1.2 = 0 then ψ ((x.1.1, 1), x.2) else 0) +
  (if x.2.1.2 = 0 then ψ (x.1, (x.2.1.1, 1), x.2.2) else 0) +
  (if x.2.2.2 = 0 then ψ (x.1, x.2.1, (x.2.2.1, 1)) else 0)

/-- `pUp` is a highest-weight vector for spin: total spin `1/2`. -/
theorem spinRaise_pUp : ∀ x, spinRaise pUp x = 0 := by decide

/-- `pUp` is a highest-weight vector for isospin: total isospin `1/2`. -/
theorem isoRaise_pUp : ∀ x, isoRaise pUp x = 0 := by decide

theorem pUp_normSq : ∑ x : Q3, pUp x * pUp x = 18 := by decide

/-- Diagonal value of `Σᵢ σ_z⁽ⁱ⁾ τ₃⁽ⁱ⁾`. -/
def axialDiag (x : Q3) : ℤ :=
  sgn x.1.1 * sgn x.1.2 + sgn x.2.1.1 * sgn x.2.1.2 + sgn x.2.2.1 * sgn x.2.2.2

/-- **`g_A⁽⁰⁾ = 5/3`**: `3⟨p↑|Σᵢ σ_z⁽ⁱ⁾ τ₃⁽ⁱ⁾|p↑⟩ = 5⟨p↑|p↑⟩` (integer amplitudes, so cleared of
denominators). -/
theorem axial_charge :
    3 * ∑ x : Q3, pUp x * axialDiag x * pUp x = 5 * ∑ x : Q3, pUp x * pUp x := by decide

/-- Diagonal value of `Σᵢ e(fᵢ) σ_z⁽ⁱ⁾` for flavour weights `e_u, e_d`. -/
def momentDiag (eu ed : ℚ) (x : Q3) : ℚ :=
  (if x.1.2 = 0 then eu else ed) * (sgn x.1.1 : ℚ) + (if x.2.1.2 = 0 then eu else ed) * (sgn x.2.1.1 : ℚ) +
  (if x.2.2.2 = 0 then eu else ed) * (sgn x.2.2.1 : ℚ)

theorem moment_p (eu ed : ℚ) :
    ∑ x : Q3, (pUp x : ℚ) * momentDiag eu ed x * pUp x = 18 * ((4 * eu - ed) / 3) := by
  simp only [Fintype.sum_prod_type, Fin.sum_univ_two, pUp, momentDiag, nD, nDown, nDdown, sgn]
  norm_num; ring

theorem moment_n (eu ed : ℚ) :
    ∑ x : Q3, (nUp x : ℚ) * momentDiag eu ed x * nUp x = 18 * ((4 * ed - eu) / 3) := by
  simp only [Fintype.sum_prod_type, Fin.sum_univ_two, nUp, flip, pUp, momentDiag, nD, nDown,
    nDdown, sgn]
  norm_num; ring

/-- **The moment ratio `μ_p/μ_n = −3/2` holds iff `e_u = −2 e_d`.** Stated as `2μ_p + 3μ_n = 0`
to avoid dividing by `μ_n`. -/
theorem moment_ratio_iff (eu ed : ℚ) :
    2 * ((4 * eu - ed) / 3) + 3 * ((4 * ed - eu) / 3) = 0 ↔ eu = -2 * ed := by
  constructor <;> intro h <;> linarith

end QOU.QFTMath.SpinFlavour
