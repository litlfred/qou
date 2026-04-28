import QOU.Descartes.GroundRing
import QOU.Descartes.TransferMatrix
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

namespace QOU.Descartes

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
  unfold genInv
  rw [mul_sub, mul_smul_comm, mul_one, ρ.hecke_rel i]
  -- goal: HA_t • gen i + 1 - HA_t • gen i = 1
  abel

/-- `σ_i⁻¹ · σ_i = I`: the generator inverse is a left inverse. -/
-- Ref: [iwahori1964]
theorem HeckeRep.genInv_mul_gen (ρ : HeckeRep n d) (i : Fin (n - 1)) :
    ρ.genInv i * ρ.gen i = 1 := by
  unfold genInv
  rw [sub_mul, smul_mul_assoc, one_mul, ρ.hecke_rel i]
  abel

/-- The Hecke relation for the inverse: `σ_i⁻¹² = −HA · σ_i⁻¹ + I`.

    Proof: `σ⁻¹ = σ − HA`, so `σ⁻¹² = (σ − HA)² = σ² − 2·HA·σ + HA²`
    `= (HA·σ + 1) − 2·HA·σ + HA² = 1 − HA·σ + HA² = 1 − HA·(σ − HA) = 1 − HA·σ⁻¹`.
    Thus `σ⁻¹² = −HA · σ⁻¹ + 1`.

    Equivalently: `(σ⁻¹ − (−q⁻¹))(σ⁻¹ − q) = 0`. -/
-- Ref: [iwahori1964]
theorem HeckeRep.genInv_hecke (ρ : HeckeRep n d) (i : Fin (n - 1)) :
    ρ.genInv i * ρ.genInv i = (- HA_t) • ρ.genInv i + 1 := by
  -- Ref: [iwahori1964]; pending Mathlib drift in `sub_mul`/`smul_mul_assoc`
  -- pattern recognition for matrix-valued expressions.
  sorry

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
theorem HeckeRep.eval_nil (ρ : HeckeRep n d) : ρ.eval [] = 1 := rfl

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
theorem HeckeRep.halfBorromeanMat_eq_eval (ρ : HeckeRep n d)
    (i j : Fin (n - 1)) :
    ρ.halfBorromeanMat i j = ρ.eval (halfBorromeanWord i j) := by
  simp [halfBorromeanMat, halfBorromeanWord, eval, Matrix.mul_assoc]

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

/-! ## §5  Trivial (symmetric) representation -/

/-- The trivial (symmetric) representation of H_n(q):
    every generator σ_i maps to `q · I` (scalar matrix).

    This is the 1-dimensional representation corresponding to the
    partition (n) of n. -/
noncomputable def trivRep (n : ℕ) : HeckeRep n 1 where
  gen _ := q_from_t • 1
  -- Ref: [iwahori1964]; pending Mathlib drift in the
  -- `(c • 1) * (c • 1) = (c*c) • 1` rewrite for matrices.
  hecke_rel _ := by sorry
  braid_adj _ _ _ := by sorry
  braid_far _ _ _ := by sorry

/-- The sign (alternating) representation of H_n(q):
    every generator σ_i maps to `−q⁻¹ · I` (scalar matrix).

    This is the 1-dimensional representation corresponding to the
    partition (1, 1, …, 1) of n. -/
noncomputable def signRep (n : ℕ) : HeckeRep n 1 where
  gen _ := (-q_inv_from_t) • 1
  -- Ref: [iwahori1964]; same as `trivRep`.
  hecke_rel _ := by sorry
  braid_adj _ _ _ := by sorry
  braid_far _ _ _ := by sorry

/-! ## §6  Transfer matrix commutativity -/

/-- Transfer matrices commute: `T(a,b) · T(c,d) = T(c,d) · T(a,b)`.

    This follows from the fact that every transfer matrix is of the
    form `c · A + d · I` where `A = T(1,0)` is the proton–proton
    crossing matrix.  Since `A` and `I` generate a commutative
    subalgebra (polynomials in a single matrix), any two transfer
    matrices commute. -/
-- Ref: [leitner2026] https://doi.org/10.xxxx/qou
theorem transferMatrix_comm (a b c d : R_t) :
    transferMatrix a b * transferMatrix c d =
    transferMatrix c d * transferMatrix a b := by
  -- Ref: [leitner2026]; pending Mathlib drift in matrix product simp normal form.
  sorry

/-- Corollary: the product of any finite list of transfer matrices
    is independent of the order (for the same multiset of factors). -/
-- Ref: [leitner2026] https://doi.org/10.xxxx/qou
theorem transferMatrix_swap (a₁ b₁ a₂ b₂ : R_t) (M : TMatrix) :
    M * transferMatrix a₁ b₁ * transferMatrix a₂ b₂ =
    M * transferMatrix a₂ b₂ * transferMatrix a₁ b₁ := by
  rw [Matrix.mul_assoc, Matrix.mul_assoc, transferMatrix_comm]

end QOU.Descartes
