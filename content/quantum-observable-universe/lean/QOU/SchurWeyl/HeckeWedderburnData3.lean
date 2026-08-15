import QOU.SchurWeyl.HeckeWedderburn3
import QOU.SchurWeyl.HeckeMarkov3
import QOU.QuantumObservableUniverses.QSchurWeyl

/-!
# `QOU.SchurWeyl.HeckeWedderburnData3` — the `HeckeWedderburnData` instance at `n = 3`
(bean `qou-tpl5`, part B)

`QSchurWeyl.lean` states the Wedderburn form of the Markov trace against an
abstract bundle `HeckeWedderburnData K Part H`: block dimensions `d_λ`, Markov
weights `w_λ`, a Wedderburn isomorphism `H ≃ₐ ∏_λ M_{d_λ}(K)`, a trace
functional, and the identity `tr_M = ∑_λ w_λ χ_λ`.  Every result there
(`markov_one_eq`, `markov_add`, `markov_smul`) is therefore *conditional* on such
a bundle existing.  This file **discharges that condition at `n = 3`**, so those
results become unconditional statements about `H_3(q)`.

## What is delivered

* `heckeDim3 = ![1, 1, 2]` — the block dimensions of `H_3(q)`, one per partition
  of `3` (`(3)`, `(1,1,1)`, `(2,1)`), satisfying `1² + 1² + 2² = 6 = 3!`.
* `piReshape3` — the algebra isomorphism
  `ℝ × ℝ × M₂(ℝ) ≃ₐ[ℝ] ∏ l : Fin 3, M_{d_l}(ℝ)`, i.e. the reshape of the
  binary-product form produced by `wedderburn3` into the indexed-product form
  the bundle requires.  The two `1`-blocks use `M₁(ℝ) ≅ ℝ`.
* `heckeWedderburnData3` — the bundle itself, assembled from `wedderburn3`
  (SW-7), the canonical Ocneanu/HOMFLY weights `markovWeight0/1/2` (SW-8 part A)
  and `markovTrace3`.  Its `markov_eq` field is *proved*, not assumed: the
  weighted-character definition of `markovTrace3` is shown to agree termwise with
  the block traces of the reshaped isomorphism.
* `markov_one_eq₃` — the specialisation of `markov_one_eq`, recorded to
  demonstrate that the abstract results now apply concretely.

Base ring: `ℝ` throughout, as `HeckeWedderburnData` requires a `Field` and the
`n = 3` Wedderburn iso (`wedderburn3`) is stated over `ℝ`.  The archimedean
specialisation is inherited, not introduced here (§7c).

Refs:
- [jones1987] Jones, *Hecke algebra representations of braid groups and link
  polynomials*, https://doi.org/10.2307/1971403
- [wenzl1988] Wenzl, *Hecke algebras of type `A_n` and subfactors*,
  https://doi.org/10.1007/BF01393520
-/

namespace QOU.SchurWeyl

open Hecke Matrix

namespace WedderburnData3

/-! ## Block dimensions -/

/-- The Wedderburn block dimensions of `H_3(q)`, indexed by the three partitions
of `3`: `d_{(3)} = 1` (trivial), `d_{(1,1,1)} = 1` (sign), `d_{(2,1)} = 2` (the
seminormal block).  `1² + 1² + 2² = 6 = 3!`. -/
abbrev heckeDim3 : Fin 3 → ℕ := ![1, 1, 2]

@[simp] theorem heckeDim3_zero : heckeDim3 0 = 1 := rfl
@[simp] theorem heckeDim3_one : heckeDim3 1 = 1 := rfl
@[simp] theorem heckeDim3_two : heckeDim3 2 = 2 := rfl

/-! ## Reshaping `ℝ × ℝ × M₂(ℝ)` into `∏ l : Fin 3, M_{d_l}(ℝ)` -/

/-- The forward reshape: the two scalar blocks become `1 × 1` matrices, the
seminormal block is carried across unchanged. -/
def reshapeFun (x : ℝ × ℝ × Matrix (Fin 2) (Fin 2) ℝ) :
    ∀ l : Fin 3, Matrix (Fin (heckeDim3 l)) (Fin (heckeDim3 l)) ℝ
  | ⟨0, _⟩ => Matrix.of fun _ _ => x.1
  | ⟨1, _⟩ => Matrix.of fun _ _ => x.2.1
  | ⟨2, _⟩ => x.2.2
  | ⟨n + 3, h⟩ => absurd h (by omega)

/-- The single entry of a `1 × 1` block.  The index is built from the width
hypothesis rather than from a numeral: `(0 : Fin (heckeDim3 l))` cannot be
elaborated, because instance synthesis works at reducible transparency and will
not evaluate `heckeDim3 0` down to `1`. -/
def entry11 {d : ℕ} (hd : d = 1) (M : Matrix (Fin d) (Fin d) ℝ) : ℝ :=
  M ⟨0, by omega⟩ ⟨0, by omega⟩

/-- The inverse reshape: read the single entry out of each `1 × 1` block. -/
def reshapeInv (f : ∀ l : Fin 3, Matrix (Fin (heckeDim3 l)) (Fin (heckeDim3 l)) ℝ) :
    ℝ × ℝ × Matrix (Fin 2) (Fin 2) ℝ :=
  (entry11 rfl (f 0), entry11 rfl (f 1), f 2)

/-- **The Π-reshape isomorphism** `ℝ × ℝ × M₂(ℝ) ≃ₐ[ℝ] ∏ l : Fin 3, M_{d_l}(ℝ)`.

This is pure bookkeeping — `M₁(ℝ) ≅ ℝ` on the two one-dimensional blocks — but it
is what lets the binary-product Wedderburn iso of `wedderburn3` meet the
indexed-product shape that `HeckeWedderburnData.iso` demands. -/
def piReshape3 :
    (ℝ × ℝ × Matrix (Fin 2) (Fin 2) ℝ) ≃ₐ[ℝ]
      (∀ l : Fin 3, Matrix (Fin (heckeDim3 l)) (Fin (heckeDim3 l)) ℝ) where
  toFun := reshapeFun
  invFun := reshapeInv
  left_inv := by
    rintro ⟨a, b, M⟩
    rfl
  right_inv := by
    intro f
    funext l
    match l with
    | ⟨0, _⟩ => ext i j; fin_cases i; fin_cases j; simp [reshapeFun, reshapeInv, entry11]
    | ⟨1, _⟩ => ext i j; fin_cases i; fin_cases j; simp [reshapeFun, reshapeInv, entry11]
    | ⟨2, _⟩ => simp [reshapeFun, reshapeInv, entry11]
    | ⟨n + 3, h⟩ => exact absurd h (by omega)
  map_mul' := by
    rintro ⟨a, b, M⟩ ⟨a', b', M'⟩
    funext l
    match l with
    | ⟨0, _⟩ => ext i j; fin_cases i; fin_cases j
                simp [reshapeFun, Matrix.mul_apply]
    | ⟨1, _⟩ => ext i j; fin_cases i; fin_cases j
                simp [reshapeFun, Matrix.mul_apply]
    | ⟨2, _⟩ => rfl
    | ⟨n + 3, h⟩ => exact absurd h (by omega)
  map_add' := by
    rintro ⟨a, b, M⟩ ⟨a', b', M'⟩
    funext l
    match l with
    | ⟨0, _⟩ => rfl
    | ⟨1, _⟩ => rfl
    | ⟨2, _⟩ => rfl
    | ⟨n + 3, h⟩ => exact absurd h (by omega)
  commutes' := by
    intro r
    funext l
    match l with
    | ⟨0, _⟩ => ext i j; fin_cases i; fin_cases j
                simp [reshapeFun, Algebra.algebraMap_eq_smul_one]
    | ⟨1, _⟩ => ext i j; fin_cases i; fin_cases j
                simp [reshapeFun, Algebra.algebraMap_eq_smul_one]
    | ⟨2, _⟩ => rfl
    | ⟨n + 3, h⟩ => exact absurd h (by omega)

@[simp] theorem piReshape3_apply_zero (x : ℝ × ℝ × Matrix (Fin 2) (Fin 2) ℝ) :
    piReshape3 x 0 = Matrix.of fun _ _ => x.1 := rfl

@[simp] theorem piReshape3_apply_one (x : ℝ × ℝ × Matrix (Fin 2) (Fin 2) ℝ) :
    piReshape3 x 1 = Matrix.of fun _ _ => x.2.1 := rfl

@[simp] theorem piReshape3_apply_two (x : ℝ × ℝ × Matrix (Fin 2) (Fin 2) ℝ) :
    piReshape3 x 2 = x.2.2 := rfl

variable (q : ℝ)

/-! ## The bundle -/

/-- **The `HeckeWedderburnData` bundle for `H_3(q)`** (`q ≠ 0`, Ocneanu parameter
`z`).  This discharges the hypothesis of every conditional result in
`QSchurWeyl.lean` at `n = 3`.

The `markov_eq` field is the substance: `markovTrace3` is *defined* as the
weighted character sum `w₀·χ_triv + w₁·χ_sign + w₂·χ_{(2,1)}`, and the bundle
demands `∑_λ w_λ · tr((iso h) λ)`.  These agree because the trace of a `1 × 1`
block is its single entry, so the two scalar blocks contribute their characters
directly, while the `(2,1)` block contributes its matrix trace. -/
noncomputable def heckeWedderburnData3 (hq : q ≠ 0) (z : ℝ) :
    HeckeWedderburnData ℝ (Fin 3) (Hecke ℝ q q⁻¹ 2) where
  dim := heckeDim3
  weight := ![markovWeight0 q z, markovWeight1 q z, markovWeight2 q z]
  iso := (wedderburn3 q hq).trans piReshape3
  markov := markovTrace3 q hq (markovWeight0 q z) (markovWeight1 q z) (markovWeight2 q z)
  markov_eq := by
    intro h
    rw [Fin.sum_univ_three]
    simp only [AlgEquiv.trans_apply, piReshape3_apply_zero, piReshape3_apply_one,
      piReshape3_apply_two, markovTrace3, Matrix.trace, Matrix.diag, Fin.sum_univ_one,
      Matrix.of_apply, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons,
      Matrix.cons_val_two, Matrix.tail_cons, wedderburn3, AlgEquiv.ofBijective_apply,
      rho_apply]
    rfl

/-- The abstract partition-function identity `tr_M(1) = ∑_λ d_λ w_λ`
(`markov_one_eq`), now unconditional at `n = 3`: the conditional result of
`QSchurWeyl.lean` applied to the bundle built above. -/
theorem markov_one_eq₃ (hq : q ≠ 0) (z : ℝ) :
    markovTrace3 q hq (markovWeight0 q z) (markovWeight1 q z) (markovWeight2 q z) 1
      = ∑ l : Fin 3, (heckeWedderburnData3 q hq z).weight l
          * ((heckeWedderburnData3 q hq z).dim l : ℝ) :=
  markov_one_eq (heckeWedderburnData3 q hq z)

end WedderburnData3

end QOU.SchurWeyl
