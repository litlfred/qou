/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic

/-!
# The Reeb weight on the proton weight space, from the KZ identification

Audit: `docs/audits/2026-11-21-proton-two-twelve-count-survey.md` §4. Issue #8967.

The two-term route writes `−12 = −k²·3`, where `3 = dim W_p`
(`ProtonWeightSpaceDim.dim_proton_weight_space`) and `k` is the weight of the Reeb part
`R` of the Dirac operator on `W_p`, provided `R∘R` is scalar there. This file asks what the
corpus's one concrete realisation of `R` gives.

That realisation is `LagrangianKZIdentification.arnold_euler`: on the KZ sector, under the
postulates P1–P3 of that file, the Reeb part is the Euler contraction
`R = ½ Σ_{i≠j} M_{ij} = Σ_{i<j} M_{ij}`, with pair residue `M_{ij} = 2κ (P_{ij} − c)` in the
Lean KZ normalisation (`docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md` §5.2,
`q = e^{2πiκ}`). The constant `c` is not fixed by the Hecke factorisation: `kzBraidRep`
satisfies the Hecke quadratic for every `c`.

`W_p` is spanned by the three states with one `e₂`, indexed by the position of the `e₂`.
A transposition `P_{ij}` moves that position by `Equiv.swap i j`.

## Results

* `transpositionSum_eq_ones`: `Σ_{i<j} P_{ij}` on `W_p` is the all-ones matrix `J`.
* `shifted_sq`: `(J − s·1)² = (3 − 2s)·J + s²·1`.
* `shifted_sq_scalar_iff`: `(J − s·1)²` is scalar iff `2s = 3`. With `s = 3c` this is
  `c = 1/2`, the traceless (𝔰𝔩₂) Casimir `P − ½`. So `R∘R` is scalar on `W_p` exactly in the
  𝔰𝔩₂ normalisation, and at no other `c`.
* `reeb_sq_sl2`: at `c = 1/2`, `R∘R = 9κ²·1` on `W_p`, and its trace is `27κ²`.
* `trace_eq_neg_twelve_iff`: `27κ² = −12 ↔ 9κ² = −4`, i.e. `k² = −9κ² = 4`.

So `k = 2` holds iff `κ² = −4/9`. Nothing in this file fixes `κ`. The corpus ties `κ` to the
pinned `q₀` by `q = e^{2πiκ}`; that evaluation is a comparison, done in the audit, not here.

Base ring: any field (§7c). `CharZero` only where `2 ≠ 0` is used. No empirical number.
-/

namespace QOU.MassTheory.ProtonReebKZWeight

open Matrix

/-- The transpositions `(i, j)`, `i < j`, of three strands. -/
def pairs : List (Fin 3 × Fin 3) := [(0, 1), (0, 2), (1, 2)]

/-- How many transpositions `P_{ij}` send the state with `e₂` at position `b` to the
state with `e₂` at position `a`. -/
def pairCount (a b : Fin 3) : ℕ :=
  (pairs.filter fun p => Equiv.swap p.1 p.2 b = a).length

theorem pairCount_eq_one : ∀ a b : Fin 3, pairCount a b = 1 := by decide

variable {K : Type*} [Field K]

/-- `Σ_{i<j} P_{ij}` on `W_p`, in the position basis. -/
def transpositionSum : Matrix (Fin 3) (Fin 3) K := fun a b => (pairCount a b : K)

/-- The all-ones `3 × 3` matrix. -/
def J : Matrix (Fin 3) (Fin 3) K := fun _ _ => 1

theorem transpositionSum_eq_ones : (transpositionSum : Matrix (Fin 3) (Fin 3) K) = J := by
  ext a b
  simp [transpositionSum, J, pairCount_eq_one]

theorem J_sq : (J : Matrix (Fin 3) (Fin 3) K) * J = (3 : K) • J := by
  ext a b
  simp [J, Matrix.mul_apply]

theorem shifted_sq (s : K) :
    (J - s • (1 : Matrix (Fin 3) (Fin 3) K)) * (J - s • 1) =
      (3 - 2 * s) • J + (s ^ 2) • (1 : Matrix (Fin 3) (Fin 3) K) := by
  have h := (J_sq (K := K))
  ext a b
  have hab := congrFun (congrFun h a) b
  simp only [Matrix.sub_mul, Matrix.mul_sub, Matrix.smul_mul, Matrix.mul_smul, Matrix.one_mul,
    Matrix.mul_one, h] at *
  simp only [Matrix.add_apply, Matrix.sub_apply, Matrix.smul_apply, smul_eq_mul]
  fin_cases a <;> fin_cases b <;> simp [J] <;> ring

/-- `(J − s·1)²` is a scalar matrix iff `2s = 3`. -/
theorem shifted_sq_scalar_iff [CharZero K] (s : K) :
    (∃ μ : K, (J - s • (1 : Matrix (Fin 3) (Fin 3) K)) * (J - s • 1) =
        μ • (1 : Matrix (Fin 3) (Fin 3) K)) ↔ 2 * s = 3 := by
  rw [shifted_sq]
  constructor
  · rintro ⟨μ, hμ⟩
    have h01 := congrFun (congrFun hμ 0) 1
    simp [J] at h01
    linear_combination -h01
  · intro h
    refine ⟨s ^ 2, ?_⟩
    have : (3 : K) - 2 * s = 0 := by linear_combination -h
    rw [this, zero_smul, zero_add]

/-- The Reeb part on `W_p`: `R = Σ_{i<j} 2κ(P_{ij} − c) = 2κ (J − 3c·1)`. -/
def reeb (κ c : K) : Matrix (Fin 3) (Fin 3) K :=
  (2 * κ) • (transpositionSum - (3 * c) • 1)

theorem reeb_eq (κ c : K) :
    reeb κ c = (2 * κ) • (J - (3 * c) • (1 : Matrix (Fin 3) (Fin 3) K)) := by
  simp [reeb, transpositionSum_eq_ones]

/-- `R∘R` is scalar on `W_p` iff `κ = 0` or `c = 1/2` (the 𝔰𝔩₂ normalisation). -/
theorem reeb_sq_scalar_iff [CharZero K] (κ c : K) (hκ : κ ≠ 0) :
    (∃ μ : K, reeb κ c * reeb κ c = μ • (1 : Matrix (Fin 3) (Fin 3) K)) ↔ 2 * c = 1 := by
  rw [reeb_eq, Matrix.smul_mul, Matrix.mul_smul, smul_smul]
  have h2κ : (2 * κ) * (2 * κ) ≠ 0 := by
    have : (2 : K) ≠ 0 := two_ne_zero
    exact mul_ne_zero (mul_ne_zero this hκ) (mul_ne_zero this hκ)
  constructor
  · rintro ⟨μ, hμ⟩
    have key : ∃ ν : K, (J - (3 * c) • (1 : Matrix (Fin 3) (Fin 3) K)) *
        (J - (3 * c) • 1) = ν • (1 : Matrix (Fin 3) (Fin 3) K) := by
      refine ⟨((2 * κ) * (2 * κ))⁻¹ * μ, ?_⟩
      calc (J - (3 * c) • (1 : Matrix (Fin 3) (Fin 3) K)) * (J - (3 * c) • 1)
          = ((2 * κ) * (2 * κ))⁻¹ • (((2 * κ) * (2 * κ)) •
              ((J - (3 * c) • (1 : Matrix (Fin 3) (Fin 3) K)) * (J - (3 * c) • 1))) := by
            rw [smul_smul, inv_mul_cancel₀ h2κ, one_smul]
        _ = ((2 * κ) * (2 * κ))⁻¹ • (μ • (1 : Matrix (Fin 3) (Fin 3) K)) := by rw [hμ]
        _ = _ := by rw [smul_smul]
    have := (shifted_sq_scalar_iff (3 * c)).1 key
    linear_combination this / 3
  · intro h
    obtain ⟨ν, hν⟩ := (shifted_sq_scalar_iff (K := K) (3 * c)).2 (by linear_combination 3 * h)
    exact ⟨(2 * κ) * (2 * κ) * ν, by rw [hν, smul_smul]⟩

/-- At `c = 1/2`, `R∘R = 9κ²·1` on `W_p`. -/
theorem reeb_sq_sl2 [CharZero K] (κ c : K) (hc : 2 * c = 1) :
    reeb κ c * reeb κ c = (9 * κ ^ 2) • (1 : Matrix (Fin 3) (Fin 3) K) := by
  rw [reeb_eq, Matrix.smul_mul, Matrix.mul_smul, smul_smul, shifted_sq]
  have h3 : (3 : K) - 2 * (3 * c) = 0 := by linear_combination -3 * hc
  have hc' : c = 1 / 2 := by
    field_simp
    linear_combination hc
  rw [h3, zero_smul, zero_add, smul_smul, hc']
  congr 1
  ring

/-- Its trace on `W_p` is `27κ²`. -/
theorem trace_reeb_sq_sl2 [CharZero K] (κ c : K) (hc : 2 * c = 1) :
    (reeb κ c * reeb κ c).trace = 27 * κ ^ 2 := by
  rw [reeb_sq_sl2 κ c hc, Matrix.trace_smul, Matrix.trace_one, Fintype.card_fin]
  simp only [smul_eq_mul]
  push_cast
  ring

/-- The `−12` of the production identity, read as `τ(R∘R)` on `W_p`, holds iff `9κ² = −4`.
In the `−k²·3` reading, `k² = −9κ²`, so this is `k² = 4`. -/
theorem trace_eq_neg_twelve_iff [CharZero K] (κ c : K) (hc : 2 * c = 1) :
    (reeb κ c * reeb κ c).trace = -12 ↔ 9 * κ ^ 2 = -4 := by
  rw [trace_reeb_sq_sl2 κ c hc]
  constructor
  · intro h; linear_combination h / 3
  · intro h; linear_combination 3 * h

end QOU.MassTheory.ProtonReebKZWeight
