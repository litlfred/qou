import Mathlib.Algebra.BigOperators.Fin
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FinCases

/-!
# QOU.BraidsAndKnots.explicit_alpha_k_h4

The `H₄(R, q)` class-function representatives of
[`conj:explicit-alpha-k-h4`](explicit-alpha-k-h4.md), in exact `ℚ(q)` form.

## 2026-11-20 rewrite (W8b, gap 2 of bean `qou-w8cg`)

This file used to carry one row of the table as **float literals**
(`-0.30555901`, `1.45407306`, …) and an `α₃ = 0.0034625204` pinned to a
witness, with "theorems" that only range-checked those literals by `norm_num`
(e.g. that the coefficients sum to at most 1). Nothing was derived, the
`lean.ref` name `explicit_alpha_k_h4` did not exist, and the header used the
convention-C Markov parameter.

It now carries the **whole table of the block, exactly**, and proves the
property the table claims:

Everything is stated with denominators cleared, so every identity is a
polynomial identity in `q` over a generic commutative ring (§7c) and is
discharged by `ring`:

* `charTableH4 q μ C` — `q³ · χ_μ(T_{w_C})`, the `H₄(q)` characters on the five
  class representatives `1, σ₁, σ₁σ₃, σ₁σ₂, σ₁σ₂σ₃` (normalisation
  `(σ − q)(σ + q⁻¹) = 0`), scaled by `q³` to clear `q⁻¹`. **Input data, not
  derived here:** computed from Young's seminormal form in sympy on
  2026-11-20, with the Hecke and braid relations checked symbolically on every
  representation. The `e` column `q³·(1, 3, 2, 3, 1)` is the dimensions.
* `repNumH4 q λ C` — `D_λ · c_C(λ)`: the block's table row `λ` times its
  common denominator `D_λ`, where
  `D = (q³(q²+1)[3]', q²(q²+1), (q²+1)², q(q²+1), (q²+1)[3]')` and
  `[3]' = q⁴+q²+1`. (Checked against the `.md` table entry by entry.)
* `explicit_alpha_k_h4` — **the table is a dual basis**:
  `Σ_C N_λ(C) χ̃_μ(C) = δ_{λμ} K_λ` for all `λ, μ ⊢ 4`, i.e.
  `χ_μ(r_λ) = δ_{λμ} κ_λ` with `κ_λ = K_λ/(q³ D_λ)`. So `r_λ` is killed by
  every character except `χ_λ`.
* `kappa_factor` — each `K_λ` factors through `q`, `q²+1`, `q⁴+1` and
  `q⁴+q²+1` only, so `κ_λ ≠ 0` away from those roots (generic `q`).
* `markov_pairing_rep` — for **any** trace expanded in the Frobenius basis
  `tr = Σ_μ y_μ χ_μ`, `tr(r_λ) = y_λ κ_λ`. The `α_k` of the block are these
  numbers.

## What this means for the old `α₃ ≈ +0.003463`

The old `r₃` is the row `λ = (1⁴)` (its floats are this row at the proton
`q₀`, to the 8 digits recorded). By `markov_pairing_rep`,
`α₃ = tr_M(r_{(1⁴)}) = y_{(1⁴)} · κ_{(1⁴)}`. Under **convention D** every shape
with a third row has Ocneanu weight `0`
(`QOU.SchurWeyl.ocneanuWeight_conventionD_eq_zero_of_three_rows`), so under the
canonical convention `α₃(H₄) = 0`; `markov_pairing_rep_eq_zero` states this for
any trace with `y_{(1⁴)} = 0`. The recorded `+0.003463` was the
**convention-C** value, where `y_{(1⁴)} ≠ 0`. This file does not import the
convention-D lemma; it proves the reduction to `y_{(1⁴)}`.

Base ring: a generic commutative ring (§7c); nothing archimedean is used.

-- Ref: [leitner2026] mass-theory/explicit-alpha-k-h4.md
-- Ref: [geckpfeiffer2000] Ch. 9–10 (characters of Iwahori–Hecke algebras)
-/

namespace QOU.BraidsAndKnots

/-- `q³ · χ_μ(T_{w_C})`; rows `μ = (4), (3,1), (2,2), (2,1,1), (1⁴)`, columns
`C = e, (12), (12)(34), (123), (1234)`. -/
def charTableH4 {R : Type*} [CommRing R] (q : R) : Fin 5 → Fin 5 → R :=
  ![![q^3, q^4, q^5, q^5, q^6],
    ![3*q^3, 2*q^4 - q^2, q^5 - 2*q^3, q^5 - q^3, -q^4],
    ![2*q^3, q^4 - q^2, q^5 + q, -q^3, 0],
    ![3*q^3, q^4 - 2*q^2, -2*q^3 + q, -q^3 + q, q^2],
    ![q^3, -q^2, q, q, -1]]

/-- `D_λ · c_C(λ)`, the block's table with each row's denominator cleared. -/
def repNumH4 {R : Type*} [CommRing R] (q : R) : Fin 5 → Fin 5 → R :=
  ![![1, q^5 + 2*q^3 + 3*q, q^6 + q^4 + q^2, q^8 + 2*q^6 + 3*q^4 + 2*q^2,
      q^9 + 2*q^7 + 2*q^5 + q^3],
    ![-q, -q^4 - 2*q^2 + 1, q, -q^5 + q, q^4 + q^2],
    ![-q^2, -q^3 + q, -q^4 - q^2 - 1, q^4 + 2*q^2 + 1, 0],
    ![q^4, q^5 - 2*q^3 - q, -q^4, 1 - q^4, q^3 + q],
    ![-q^9, 3*q^8 + 2*q^6 + q^4, -q^7 - q^5 - q^3, -2*q^7 - 3*q^5 - 2*q^3 - q,
      q^6 + 2*q^4 + 2*q^2 + 1]]

/-- `K_λ = q³ D_λ κ_λ`, the diagonal pairing with denominators cleared. -/
def kappaNumH4 {R : Type*} [CommRing R] (q : R) : Fin 5 → R :=
  ![q^15 + 3*q^13 + 5*q^11 + 6*q^9 + 5*q^7 + 3*q^5 + q^3,
    -q^10 - 2*q^8 - 2*q^6 - 2*q^4 - q^2,
    -q^9 - 3*q^7 - 4*q^5 - 3*q^3 - q,
    q^9 + 2*q^7 + 2*q^5 + 2*q^3 + q,
    -q^12 - 3*q^10 - 5*q^8 - 6*q^6 - 5*q^4 - 3*q^2 - 1]

/-- The pairing `Σ_C N_λ(C) · χ̃_μ(C)`. -/
def pairH4 {R : Type*} [CommRing R] (q : R) (lam mu : Fin 5) : R :=
  ∑ C : Fin 5, repNumH4 q lam C * charTableH4 q mu C

/-- Diagonal pairings: `Σ_C N_λ(C) χ̃_λ(C) = K_λ`. -/
theorem pairH4_diag {R : Type*} [CommRing R] (q : R) (lam : Fin 5) :
    pairH4 q lam lam = kappaNumH4 q lam := by
  fin_cases lam <;>
    simp [pairH4, Fin.sum_univ_five, repNumH4, charTableH4, kappaNumH4] <;> ring

/-- Off-diagonal pairings vanish: `Σ_C N_λ(C) χ̃_μ(C) = 0` for `λ ≠ μ`. -/
theorem pairH4_offdiag {R : Type*} [CommRing R] (q : R) (lam mu : Fin 5)
    (h : lam ≠ mu) : pairH4 q lam mu = 0 := by
  fin_cases lam <;> fin_cases mu <;> simp at h <;>
    simp [pairH4, Fin.sum_univ_five, repNumH4, charTableH4] <;> ring

/-- **The table is a dual basis.** `Σ_C N_λ(C) χ̃_μ(C) = δ_{λμ} K_λ`. -/
-- Ref: [leitner2026] mass-theory/explicit-alpha-k-h4.md
theorem explicit_alpha_k_h4 {R : Type*} [CommRing R] (q : R) (lam mu : Fin 5) :
    pairH4 q lam mu = if lam = mu then kappaNumH4 q lam else 0 := by
  split_ifs with h
  · subst h; exact pairH4_diag q lam
  · exact pairH4_offdiag q lam mu h

/-- Each `K_λ` factors through `q`, `q² + 1`, `q⁴ + 1` and `q⁴ + q² + 1` only. -/
theorem kappa_factor {R : Type*} [CommRing R] (q : R) :
    kappaNumH4 q 0 = q^3 * (q^2+1)^2 * (q^4+1) * (q^4+q^2+1) ∧
    kappaNumH4 q 1 = -(q^2 * (q^2+1)^2 * (q^4+1)) ∧
    kappaNumH4 q 2 = -(q * (q^2+1)^2 * (q^4+q^2+1)) ∧
    kappaNumH4 q 3 = q * (q^2+1)^2 * (q^4+1) ∧
    kappaNumH4 q 4 = -((q^2+1)^2 * (q^4+1) * (q^4+q^2+1)) := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩ <;> simp [kappaNumH4] <;> ring

/-- **Markov pairing.** For any trace in the Frobenius basis,
`tr = Σ_μ y_μ χ_μ`, the cleared value on `r_λ` is `y_λ K_λ`. -/
theorem markov_pairing_rep {R : Type*} [CommRing R] (q : R) (y : Fin 5 → R)
    (lam : Fin 5) :
    ∑ mu : Fin 5, y mu * pairH4 q lam mu = y lam * kappaNumH4 q lam := by
  simp only [explicit_alpha_k_h4, mul_ite, mul_zero]
  rw [Finset.sum_ite_eq]
  simp

/-- `α₃(H₄) = tr(r_{(1⁴)})` vanishes for every trace with `y_{(1⁴)} = 0`, which
convention D satisfies (three-row shapes carry Ocneanu weight `0`). -/
theorem markov_pairing_rep_eq_zero {R : Type*} [CommRing R] (q : R) (y : Fin 5 → R)
    (hy : y 4 = 0) : ∑ mu : Fin 5, y mu * pairH4 q 4 mu = 0 := by
  rw [markov_pairing_rep, hy, zero_mul]

end QOU.BraidsAndKnots
