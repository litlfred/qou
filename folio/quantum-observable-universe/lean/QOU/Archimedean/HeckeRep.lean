import QOU.Archimedean.GroundRing
import QOU.Archimedean.TransferMatrix
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.Tactic.Ring

/-!
# Iwahori–Hecke Algebra Representations

General framework for finite-dimensional representations of the
Iwahori–Hecke algebra H_n(q) over `ℤ[t, t⁻¹]`.

## Main definitions

- `HeckeRep n d` — a representation of H_n(q) of dimension d
- `HeckeRep.genInv` — generator inverse from the Hecke relation
- `HeckeRep.eval` — evaluate a signed braid word
- `HeckeRep.halfBorromean` — the half-Borromean element h_{ij}
- `HeckeRep.character` — trace (character) of a Hecke element

## The Hecke relation

The generators σ_i satisfy `σ² = HA · σ + 1` where `HA = t² − t⁻²`.
The eigenvalues of each generator are `t² = q` and `−t⁻² = −q⁻¹`.

## References

- [iwahori1964] N. Iwahori, On the structure of a Hecke ring.
- [jones1987] V. Jones, Hecke algebra representations of braid groups.
- [murphy1992] G. Murphy, On the representation theory of the symmetric
  groups and associated Hecke algebras.
-/

namespace QOU.Archimedean

open Matrix

variable {n d : ℕ}

/-! ## §1  Representation structure -/

/-- A representation of the Iwahori–Hecke algebra H_n(q) of dimension d
    over the ground ring `ℤ[t, t⁻¹]`.

    A representation assigns a `d × d` matrix to each generator
    `σ_i` (for `i ∈ {0, …, n−2}`) satisfying:
    1. The Hecke relation: `σ_i² = HA · σ_i + I`
    2. The braid relation: `σ_i σ_{i+1} σ_i = σ_{i+1} σ_i σ_{i+1}`
    3. Far commutativity: `σ_i σ_j = σ_j σ_i` for `|i − j| ≥ 2` -/
structure HeckeRep (n d : ℕ) where
  /-- Matrix for generator σ_i. -/
  gen : Fin (n - 1) → Matrix (Fin d) (Fin d) R_t
  /-- Hecke relation: `σ_i² = HA · σ_i + I` for each generator. -/
  hecke_rel : ∀ i, gen i * gen i = HA_t • gen i + 1
  /-- Adjacent braid relation: `σ_i σ_{i+1} σ_i = σ_{i+1} σ_i σ_{i+1}`. -/
  braid_adj : ∀ (i : ℕ) (hi₀ : i < n - 1) (hi₁ : i + 1 < n - 1),
    gen ⟨i, hi₀⟩ * gen ⟨i + 1, hi₁⟩ * gen ⟨i, hi₀⟩ =
    gen ⟨i + 1, hi₁⟩ * gen ⟨i, hi₀⟩ * gen ⟨i + 1, hi₁⟩
  /-- Far commutativity: `σ_i σ_j = σ_j σ_i` for `|i − j| ≥ 2`. -/
  braid_far : ∀ (i j : Fin (n - 1)),
    (i : ℕ) + 2 ≤ (j : ℕ) →
    gen i * gen j = gen j * gen i

/-! ## §2  Generator inverse -/

/-- The inverse of generator σ_i, derived from the Hecke relation:

    `σ_i⁻¹ = σ_i − HA · I`

    Verification: `σ_i · (σ_i − HA · I) = σ_i² − HA · σ_i = 1`. -/
noncomputable def HeckeRep.genInv (ρ : HeckeRep n d) (i : Fin (n - 1)) :
    Matrix (Fin d) (Fin d) R_t :=
  ρ.gen i - HA_t • 1

/-- `σ_i · σ_i⁻¹ = I`: the generator inverse is a right inverse. -/
-- Ref: [iwahori1964]
theorem HeckeRep.gen_mul_genInv (ρ : HeckeRep n d) (i : Fin (n - 1)) :
    ρ.gen i * ρ.genInv i = 1 := by
  unfold HeckeRep.genInv
  rw [mul_sub, mul_smul_comm, mul_one, ρ.hecke_rel i]
  -- goal: HA_t • gen i + 1 - HA_t • gen i = 1
  abel

/-- `σ_i⁻¹ · σ_i = I`: the generator inverse is a left inverse. -/
-- Ref: [iwahori1964]
theorem HeckeRep.genInv_mul_gen (ρ : HeckeRep n d) (i : Fin (n - 1)) :
    ρ.genInv i * ρ.gen i = 1 := by
  unfold HeckeRep.genInv
  rw [sub_mul, smul_mul_assoc, one_mul, ρ.hecke_rel i]
  abel

/- The Hecke relation for the inverse: `σ_i⁻¹² = −HA · σ_i⁻¹ + I`.

    Proof sketch: `σ⁻¹ = σ − HA`, so
      `σ⁻¹² = σ² − 2·HA·σ + HA²` (using that `HA·1` commutes with `σ`)
            = `(HA·σ + 1) − 2·HA·σ + HA²`            [Hecke]
            = `1 − HA·σ + HA²`
            = `1 − HA·(σ − HA)`                       [bilinearity]
            = `1 − HA·σ⁻¹`.

    Equivalently: `(σ⁻¹ − (−q⁻¹))(σ⁻¹ − q) = 0`.

    DIAGNOSTIC: the algebraic massage requires combining smul of the
    identity matrix with matrix multiplication.  `abel` fails on the
    final goal because the term `(HA_t * HA_t) • 1` appears with a
    nested `(-1) • (-1) •` after `neg_smul` rewrites, and `abel` does
    not normalize `(-1) • (-1) • X` to `X` when `X` is itself a smul.
    The cleanest fix would be:
    1. introduce `H := HA_t • (1 : Matrix _ _ R_t)` as a local set
       so `abel` sees `H` and `σ` as the only atoms; then
    2. precompute `H * σ = σ * H = HA_t • σ` and
       `H * H = (HA_t * HA_t) • 1` once, and
    3. close by `linear_combination` against `hecke`.

    Sorry retained pending that refactor. -/
/-- **Hecke relation for σ⁻¹**:
    `σ⁻¹² = −HA · σ⁻¹ + 1`.

    **Theorem** (was previously `HeckeRep.genInv_hecke_axiom`).
    Discharged 2026-06-08 via the docstring's suggested
    `linear_combination` approach against `hecke_rel`.

    Proof sketch: σ⁻¹ = σ - HA·1, so
    σ⁻¹² = σ² - 2(HA·σ) + (HA·HA)·1
          = (HA·σ + 1) - 2(HA·σ) + (HA·HA)·1     [hecke_rel]
          = 1 - HA·σ + (HA·HA)·1
    RHS: -HA·σ⁻¹ + 1 = -HA·(σ - HA·1) + 1
                     = -HA·σ + (HA·HA)·1 + 1
                     = 1 - HA·σ + (HA·HA)·1
    LHS = RHS. -/
-- Ref: [iwahori1964] Iwahori, "On the structure of a Hecke ring of a Chevalley group over a finite field," J. Fac. Sci. Univ. Tokyo 10 (1964)
theorem genInv_hecke (ρ : HeckeRep n d) (i : Fin (n - 1)) :
    ρ.genInv i * ρ.genInv i = (- HA_t) • ρ.genInv i + 1 := by
  have hecke := ρ.hecke_rel i
  unfold HeckeRep.genInv
  -- Expand both sides via distributivity of (•) over matrix multiplication
  rw [sub_mul, mul_sub, mul_sub, hecke]
  -- After expansion, normalize the four cross-terms involving HA_t • 1
  rw [mul_smul_comm, mul_one]      -- gen i * (HA_t • 1) = HA_t • gen i
  rw [smul_mul_assoc, one_mul]     -- HA_t • 1 * gen i = HA_t • gen i
  rw [smul_mul_smul_comm, mul_one] -- HA_t • 1 * (HA_t • 1) = (HA_t * HA_t) • 1
  -- RHS expansion
  rw [smul_sub, smul_smul]         -- -HA_t • (gen i - HA_t • 1) factored
  -- Now both sides are expressions in `HA_t • gen i`, `(HA_t * HA_t) • 1`, `1`
  -- with matching coefficients up to sign normalization
  module

/-! ## §3  Braid word evaluation -/

/-- A signed braid word: a list of (generator_index, is_positive) pairs.
    Positive = σ_i, negative = σ_i⁻¹. -/
abbrev BraidWord (n : ℕ) := List (Fin (n - 1) × Bool)

/-- Evaluate a signed braid word in a representation.
    Products are computed left to right: `[σ₀, σ₁⁻¹]` → `σ₀ · σ₁⁻¹`. -/
noncomputable def HeckeRep.eval (ρ : HeckeRep n d) : BraidWord n →
    Matrix (Fin d) (Fin d) R_t
  | [] => 1
  | (i, true) :: rest => ρ.gen i * ρ.eval rest
  | (i, false) :: rest => ρ.genInv i * ρ.eval rest

/-- The empty braid word evaluates to the identity matrix. -/
theorem eval_nil (ρ : HeckeRep n d) : ρ.eval [] = 1 := rfl

/-- Character (trace) of a braid word in a representation. -/
noncomputable def HeckeRep.character (ρ : HeckeRep n d) (w : BraidWord n) : R_t :=
  (ρ.eval w).trace

/-! ## §4  Half-Borromean element -/

/-- The half-Borromean braid word `h_{ij} = σ_i⁻¹ σ_j σ_i σ_j⁻¹`.

    This is the fundamental building block of the Borromean linking
    in H_n(q).  It measures the mutual linking of strands i and j
    with all other strands as spectators. -/
def halfBorromeanWord (i j : Fin (n - 1)) : BraidWord n :=
  [(i, false), (j, true), (i, true), (j, false)]

/-- The half-Borromean element h_{ij} as a matrix in a representation. -/
noncomputable def HeckeRep.halfBorromeanMat (ρ : HeckeRep n d)
    (i j : Fin (n - 1)) : Matrix (Fin d) (Fin d) R_t :=
  ρ.genInv i * ρ.gen j * ρ.gen i * ρ.genInv j

/-- The half-Borromean matrix equals evaluation of the half-Borromean word. -/
theorem halfBorromeanMat_eq_eval (ρ : HeckeRep n d)
    (i j : Fin (n - 1)) :
    ρ.halfBorromeanMat i j = ρ.eval (halfBorromeanWord i j) := by
  simp [HeckeRep.halfBorromeanMat, halfBorromeanWord, HeckeRep.eval, Matrix.mul_assoc]

/-- The conjugated half-Borromean `h'_{ij} = σ_i⁻¹ σ_j⁻¹ σ_i σ_j`.

    This is a variant of the half-Borromean where the second and
    fourth factors have flipped signs.  It represents the linking
    of non-adjacent strands in H₃(q). -/
def halfBorromeanConjWord (i j : Fin (n - 1)) : BraidWord n :=
  [(i, false), (j, false), (i, true), (j, true)]

/-- The conjugated half-Borromean as a matrix. -/
noncomputable def HeckeRep.halfBorromeanConjMat (ρ : HeckeRep n d)
    (i j : Fin (n - 1)) : Matrix (Fin d) (Fin d) R_t :=
  ρ.genInv i * ρ.genInv j * ρ.gen i * ρ.gen j

/-! ## §4b  Algebraic identities in R_t = ℤ[t, t⁻¹] -/

/-- `t · t⁻¹ = 1` in `R_t = ℤ[t, t⁻¹]`. -/
lemma t_mul_t_inv : t * t_inv = (1 : R_t) := by
  unfold t t_inv
  rw [← LaurentPolynomial.T_add]
  simp [LaurentPolynomial.T_zero]

/-- `t⁻¹ · t = 1` in `R_t`. -/
lemma t_inv_mul_t : t_inv * t = (1 : R_t) := by
  unfold t t_inv
  rw [← LaurentPolynomial.T_add]
  simp [LaurentPolynomial.T_zero]

/-- `q · q⁻¹ = 1` in `R_t` (using `q_from_t`/`q_inv_from_t`).
    Distinct from `QOU.Archimedean.q_mul_q_inv` (which uses the
    `q`/`q_inv` aliases in `GroundRing.lean`). -/
lemma q_from_t_mul_q_inv_from_t : q_from_t * q_inv_from_t = (1 : R_t) := by
  unfold q_from_t q_inv_from_t
  -- (t·t)·(t⁻¹·t⁻¹) = t·(t·t⁻¹)·t⁻¹ = t·1·t⁻¹ = t·t⁻¹ = 1
  calc t * t * (t_inv * t_inv)
      = t * (t * t_inv) * t_inv := by ring
    _ = t * 1 * t_inv := by rw [t_mul_t_inv]
    _ = t * t_inv := by rw [mul_one]
    _ = 1 := t_mul_t_inv

/-- The Hecke quadratic identity in R_t: `q² = HA · q + 1`. -/
lemma q_squared_eq : q_from_t * q_from_t = HA_t * q_from_t + 1 := by
  unfold HA_t
  -- Goal: q*q = (q − q⁻¹)*q + 1
  -- Residual: q*q − (q − q⁻¹)*q − 1 = q⁻¹*q − 1, which matches h' below.
  have h' : q_inv_from_t * q_from_t = (1 : R_t) := by
    rw [mul_comm]; exact q_from_t_mul_q_inv_from_t
  linear_combination h'

/-- The signed Hecke quadratic identity: `q⁻² = −HA · q⁻¹ + 1`. -/
lemma q_inv_squared_eq :
    q_inv_from_t * q_inv_from_t = (- HA_t) * q_inv_from_t + 1 := by
  unfold HA_t
  -- Goal: q⁻¹*q⁻¹ = -(q − q⁻¹)*q⁻¹ + 1 = -q*q⁻¹ + q⁻¹*q⁻¹ + 1
  -- Residual: q⁻¹*q⁻¹ + q*q⁻¹ − q⁻¹*q⁻¹ − 1 = q*q⁻¹ − 1, matches h.
  have h := q_from_t_mul_q_inv_from_t
  linear_combination h

/-! ## §5  Trivial (symmetric) representation -/

/-- The trivial (symmetric) representation of H_n(q):
    every generator σ_i maps to `q · I` (scalar matrix).

    This is the 1-dimensional representation corresponding to the
    partition (n) of n. -/
noncomputable def trivRep (n : ℕ) : HeckeRep n 1 where
  gen _ := q_from_t • 1
  -- Hecke relation: q² = HA·q + 1 (q_squared_eq).
  hecke_rel _ := by
    show (q_from_t • (1 : Matrix (Fin 1) (Fin 1) R_t))
        * (q_from_t • (1 : Matrix (Fin 1) (Fin 1) R_t))
      = HA_t • (q_from_t • (1 : Matrix (Fin 1) (Fin 1) R_t)) + 1
    rw [smul_mul_smul_comm, Matrix.one_mul, ← smul_assoc,
        smul_eq_mul, q_squared_eq, add_smul, one_smul]
  -- braid_adj and braid_far close by reflexivity since `gen` is constant.
  braid_adj _ _ _ := rfl
  braid_far _ _ _ := rfl

/-- The sign (alternating) representation of H_n(q):
    every generator σ_i maps to `−q⁻¹ · I` (scalar matrix).

    This is the 1-dimensional representation corresponding to the
    partition (1, 1, …, 1) of n. -/
noncomputable def signRep (n : ℕ) : HeckeRep n 1 where
  gen _ := (-q_inv_from_t) • 1
  -- Hecke relation: (−q⁻¹)² = q⁻² = −HA·q⁻¹ + 1 = HA·(−q⁻¹) + 1.
  hecke_rel _ := by
    show ((-q_inv_from_t) • (1 : Matrix (Fin 1) (Fin 1) R_t))
        * ((-q_inv_from_t) • (1 : Matrix (Fin 1) (Fin 1) R_t))
      = HA_t • ((-q_inv_from_t) • (1 : Matrix (Fin 1) (Fin 1) R_t)) + 1
    rw [smul_mul_smul_comm, Matrix.one_mul, ← smul_assoc, smul_eq_mul]
    -- Goal: ((-q⁻¹) * (-q⁻¹)) • 1 = (HA · (-q⁻¹)) • 1 + 1
    -- LHS scalar: (-q⁻¹)·(-q⁻¹) = q⁻² = q⁻¹ · q⁻¹
    -- RHS scalar: HA · (-q⁻¹) = -HA·q⁻¹
    -- So need: q⁻¹ · q⁻¹ = -HA · q⁻¹ + 1, which is q_inv_squared_eq.
    have h : (-q_inv_from_t) * (-q_inv_from_t) = HA_t * (-q_inv_from_t) + 1 := by
      have hi := q_inv_squared_eq
      linear_combination hi
    rw [h, add_smul, one_smul]
  braid_adj _ _ _ := rfl
  braid_far _ _ _ := rfl

/-! ## §6  Transfer matrix commutativity -/

/- Transfer matrices commute: `T(a,b) · T(c,d) = T(c,d) · T(a,b)`.

    This follows from the fact that every transfer matrix is of the
    form `c · A + d · I` where `A = T(1,0)` is the proton–proton
    crossing matrix.  Since `A` and `I` generate a commutative
    subalgebra (polynomials in a single matrix), any two transfer
    matrices commute.

    **Theorem** (was previously `transferMatrix_comm_axiom`).
    Discharged 2026-06-07 via entry-by-entry expansion: `ext i j`
    + `fin_cases` covers the 4 entries of the 2x2 matrix product,
    each of which is a polynomial identity in `R_t = ℤ[t, t⁻¹]`
    closable by `ring` after `Matrix.mul_apply` + `Fin.sum_univ_two`
    + `Matrix.cons_val_*` unfold the `Matrix.cons` normal form. -/
-- Ref: [leitner2026] §transfer-matrix-commutativity
set_option maxHeartbeats 800000 in
theorem transferMatrix_comm (a b c d : R_t) :
    transferMatrix a b * transferMatrix c d =
    transferMatrix c d * transferMatrix a b := by
  unfold transferMatrix
  apply Matrix.ext
  intro i j
  fin_cases i <;> fin_cases j <;>
    simp only [Matrix.mul_apply, Fin.sum_univ_two, Matrix.of_apply,
               Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons,
               Fin.mk_zero, Fin.mk_one] <;>
    ring

/-- Corollary: the product of any finite list of transfer matrices
    is independent of the order (for the same multiset of factors). -/
-- Ref: [leitner2026] https://doi.org/10.xxxx/qou
theorem transferMatrix_swap (a₁ b₁ a₂ b₂ : R_t) (M : TMatrix) :
    M * transferMatrix a₁ b₁ * transferMatrix a₂ b₂ =
    M * transferMatrix a₂ b₂ * transferMatrix a₁ b₁ := by
  rw [Matrix.mul_assoc, Matrix.mul_assoc, transferMatrix_comm]

end QOU.Archimedean
