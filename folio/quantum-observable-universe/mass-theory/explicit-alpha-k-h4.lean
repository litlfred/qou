import Mathlib.Algebra.BigOperators.Fin
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FinCases
import Mathlib.LinearAlgebra.Matrix.Trace

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
  `(σ − q)(σ + q⁻¹) = 0`), scaled by `q³` to clear `q⁻¹`. First computed from
  Young's seminormal form in sympy (2026-11-20); **derived in Lean since
  2026-11-27** from five explicit representations with entries in `ℤ[q²]`
  (`charTableH4_derived`, section `Derived` below). The `e` column
  `q³·(1, 3, 2, 3, 1)` is the dimensions.
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

/-! ## The character table, derived (2026-11-27)

`charTableH4` above was **input data** (sympy, Young's seminormal form). It is now
**derived** in Lean: five explicit representations of `H₄` with entries polynomial
in `Q = q²`, in the normalisation `T² = (Q−1)T + Q` (`T = q·σ`):

* `(4)`: `T ↦ Q`; `(1⁴)`: `T ↦ −1`;
* `(3,1)`: the reflection representation `refl₃₁` (3×3);
* `(2,1,1)`: its twist `T ↦ (Q−1) − T` (the involution `T ↦ −Q T⁻¹`);
* `(2,2)`: the `H₃` reflection representation pulled back along
  `T₁, T₂, T₃ ↦ T₁, T₂, T₁` (`refl₂₂`).

`refl31_relations`, `refl211_relations`, `refl22_relations` check the Hecke, braid
and far-commutation relations; `charTableH4_derived` checks that
`q^{3−ℓ(w)} · tr ρ_μ(T_w)` is entry `(μ, C)` of `charTableH4` on every class
representative `w = 1, T₁, T₁T₃, T₁T₂, T₁T₂T₃` (lengths `0, 1, 2, 2, 3`). Since
`T_w = q^{ℓ(w)} σ_w`, this is `q³ · χ_μ(σ_w)`, the table's definition. Everything is
a polynomial identity over a generic commutative ring.
-/

section Derived

open Matrix

variable {R : Type*} [CommRing R]

/-- Reflection representation `(3,1)` of `H₄`, generators `T₁, T₂, T₃`. -/
def refl31 (Q : R) : Fin 3 → Matrix (Fin 3) (Fin 3) R :=
  ![!![-1, 0, 0; Q, Q, 0; 0, 0, Q],
    !![Q, 1, 0; 0, -1, 0; 0, Q, Q],
    !![Q, 0, 0; 0, Q, 1; 0, 0, -1]]

/-- The twisted representation `(2,1,1)`: `T ↦ (Q − 1) − T`, written out
(`refl211_eq_twist` checks it is the twist of `refl31`). -/
def refl211 (Q : R) : Fin 3 → Matrix (Fin 3) (Fin 3) R :=
  ![!![Q, 0, 0; -Q, -1, 0; 0, 0, -1],
    !![-1, -1, 0; 0, Q, 0; 0, -Q, -1],
    !![-1, 0, 0; 0, -1, -1; 0, 0, Q]]

theorem refl211_eq_twist (Q : R) (i : Fin 3) :
    refl211 Q i = (Q - 1) • (1 : Matrix (Fin 3) (Fin 3) R) - refl31 Q i := by
  fin_cases i <;> ext a b <;> fin_cases a <;> fin_cases b <;>
    simp [refl211, refl31]

/-- The representation `(2,2)`: the `H₃` reflection representation on `T₁, T₂, T₁`. -/
def refl22 (Q : R) : Fin 3 → Matrix (Fin 2) (Fin 2) R :=
  ![!![Q, 1; 0, -1], !![-1, 0; Q, Q], !![Q, 1; 0, -1]]

/-- Hecke, braid and far-commutation relations, stated for a family of three
generators in any ring. -/
def IsH4Rep {M : Type*} [Ring M] [Algebra R M] (Q : R) (T : Fin 3 → M) : Prop :=
  (∀ i, T i * T i = (Q - 1) • T i + Q • (1 : M)) ∧
  T 0 * T 1 * T 0 = T 1 * T 0 * T 1 ∧
  T 1 * T 2 * T 1 = T 2 * T 1 * T 2 ∧
  T 0 * T 2 = T 2 * T 0

theorem refl31_relations (Q : R) : IsH4Rep Q (refl31 Q) := by
  refine ⟨fun i => ?_, ?_, ?_, ?_⟩
  · fin_cases i <;> ext a b <;> fin_cases a <;> fin_cases b <;>
      simp [refl31, Matrix.mul_apply, Fin.sum_univ_three] <;> ring
  all_goals ext a b; fin_cases a <;> fin_cases b <;>
    simp [refl31, Matrix.mul_apply, Fin.sum_univ_three]

theorem refl211_relations (Q : R) : IsH4Rep Q (refl211 Q) := by
  refine ⟨fun i => ?_, ?_, ?_, ?_⟩
  · fin_cases i <;> ext a b <;> fin_cases a <;> fin_cases b <;>
      simp [refl211, Matrix.mul_apply, Fin.sum_univ_three] <;> ring
  all_goals ext a b; fin_cases a <;> fin_cases b <;>
    simp [refl211, Matrix.mul_apply, Fin.sum_univ_three]

theorem refl22_relations (Q : R) : IsH4Rep Q (refl22 Q) := by
  refine ⟨fun i => ?_, ?_, ?_, ?_⟩
  · fin_cases i <;> ext a b <;> fin_cases a <;> fin_cases b <;>
      simp [refl22, Matrix.mul_apply, Fin.sum_univ_two] <;> ring
  all_goals ext a b; fin_cases a <;> fin_cases b <;>
    simp [refl22, Matrix.mul_apply, Fin.sum_univ_two]

/-- The one-dimensional representations satisfy the relations. -/
theorem triv_sign_relations (Q : R) :
    IsH4Rep Q (fun _ : Fin 3 => Q) ∧ IsH4Rep Q (fun _ : Fin 3 => (-1 : R)) := by
  refine ⟨⟨fun _ => ?_, ?_, ?_, ?_⟩, ⟨fun _ => ?_, ?_, ?_, ?_⟩⟩ <;>
    simp only [smul_eq_mul, mul_one] <;> ring

/-- Values of a representation on the class words `1, T₁, T₁T₃, T₁T₂, T₁T₂T₃`,
rescaled by `q^{3 − ℓ}`: this is `q³ · χ(σ_w)`. -/
def classRow {n : Type*} [Fintype n] [DecidableEq n] (q : R)
    (T : Fin 3 → Matrix n n R) : Fin 5 → R :=
  ![q ^ 3 * trace (1 : Matrix n n R), q ^ 2 * trace (T 0), q * trace (T 0 * T 2),
    q * trace (T 0 * T 1), trace (T 0 * T 1 * T 2)]

/-- The same row for a one-dimensional representation `T ↦ t`. -/
def classRow1 (q t : R) : Fin 5 → R :=
  ![q ^ 3, q ^ 2 * t, q * t ^ 2, q * t ^ 2, t ^ 3]

/-- **The `H₄` character table, derived.** With `Q = q²`, the explicit
representations reproduce every row of `charTableH4`. -/
theorem charTableH4_derived (q : R) (C : Fin 5) :
    classRow1 q (q ^ 2) C = charTableH4 q 0 C ∧
    classRow q (refl31 (q ^ 2)) C = charTableH4 q 1 C ∧
    classRow q (refl22 (q ^ 2)) C = charTableH4 q 2 C ∧
    classRow q (refl211 (q ^ 2)) C = charTableH4 q 3 C ∧
    classRow1 q (-1) C = charTableH4 q 4 C := by
  fin_cases C <;> refine ⟨?_, ?_, ?_, ?_, ?_⟩ <;>
    simp [classRow, classRow1, charTableH4, refl31, refl211, refl22, Matrix.trace,
      Fin.sum_univ_three, Fin.sum_univ_two] <;> ring

end Derived

end QOU.BraidsAndKnots
