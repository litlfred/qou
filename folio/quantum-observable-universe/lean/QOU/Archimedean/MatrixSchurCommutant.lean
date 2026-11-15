/-
# Matrix Schur: the commutant of an irreducible representation is scalar

Discharges the *named hypothesis* of the α_EM B2 Schur core
(`SchurInvariantFormProportional.lean`, PR #4160): the theorem
`invariantForm_proportional_of_commutantScalar` takes as input a hypothesis

    schur : ∀ A, (∀ s, A * ρ s = ρ s * A) → ∃ c, A = c • 1

("the commutant of `ρ` is scalar" — absolute irreducibility, Schur's lemma).
This file **proves** that hypothesis from a cleaner premise — that `ρ` is an
irreducible matrix representation over an algebraically closed field — so the
`schur` hypothesis is no longer assumed but *derived* from irreducibility.

**The argument (classical, sorry-free).** Let `A` commute with every `ρ s`.
Over an algebraically closed field, `A` (as the endomorphism `toLin' A` of the
nonzero finite-dimensional space `n → k`) has an eigenvalue `μ`
(`Module.End.exists_eigenvalue`). Its eigenspace `E = eigenspace (toLin' A) μ`
is `ρ`-invariant (each `ρ s` commutes with `A`, so preserves eigenspaces) and
nonzero (`μ` is an eigenvalue). Irreducibility forces `E = ⊤`, i.e. every vector
is a `μ`-eigenvector, i.e. `A = μ • 1`.

**Instantiation for the B2 wall.** With `ρ = ` the S₅-action on `std = (4,1)` and
`k = ℂ` (algebraically closed), `IsIrreducibleRep ρ` is exactly the absolute
irreducibility of the standard representation. That irreducibility is the
character fact `⟨χ_(4,1), χ_(4,1)⟩ = 1`, proved sorry-free in
`QOU.ArchimedeanUniverse.S5BringHodgeDepth.W41_irreducible`. The one remaining
(standard, unformalized) bridge is the equivalence "character-norm-one ⟺
`IsIrreducibleRep`" — the Maschke/orthogonality translation between the
class-function inner product and the submodule-lattice definition used here;
it is NOT fabricated in this file. What this file removes is the *abstract*
Schur step: once irreducibility is in hand, scalar-commutant is a theorem.

STRICT (§"Axiomatization is NOT a Proof"): this derives scalar-commutant from
irreducibility; it does not assume the τ-identification, construct `τ`, or
register any `TauRhoHodgeLift` instance. `1/(8π)` stays a phase-4 identification.

-- Ref: [serre1977] Linear Representations of Finite Groups (Schur's lemma)
-- Ref: [leitner2026] prop:em-coupling-bring-zero-mode
-/
import Mathlib.LinearAlgebra.Matrix.ToLin
import Mathlib.LinearAlgebra.Eigenspace.Triangularizable
import Mathlib.FieldTheory.IsAlgClosed.Basic

namespace QOU.Archimedean.MatrixSchurCommutant

open Matrix

variable {n : Type*} [Fintype n] [DecidableEq n] {k : Type*} [Field k]
variable {G : Type*}

/-- **Irreducibility of a matrix representation.** The only subspaces of `n → k`
invariant under every `ρ s` are `⊥` and `⊤`. -/
def IsIrreducibleRep (ρ : G → Matrix n n k) : Prop :=
  ∀ p : Submodule k (n → k),
    (∀ s, ∀ v ∈ p, (ρ s) *ᵥ v ∈ p) → p ≠ ⊥ → p = ⊤

/-- **Matrix Schur's lemma.** Over an algebraically closed field, any matrix `A`
commuting with every generator `ρ s` of an *irreducible* representation is a
scalar multiple of the identity. This is exactly the `schur` hypothesis of
`invariantForm_proportional_of_commutantScalar` (#4160) — now a theorem, given
irreducibility. -/
theorem commutant_scalar_of_irreducible [IsAlgClosed k] [Nonempty n]
    {ρ : G → Matrix n n k} (hirr : IsIrreducibleRep ρ)
    {A : Matrix n n k} (hA : ∀ s, A * ρ s = ρ s * A) :
    ∃ c : k, A = c • (1 : Matrix n n k) := by
  -- `A` acts as the endomorphism `toLin' A`; get an eigenvalue over `IsAlgClosed`.
  obtain ⟨μ, hμ⟩ := Module.End.exists_eigenvalue (Matrix.toLin' A)
  refine ⟨μ, ?_⟩
  -- Pointwise commutation `A *ᵥ (ρ s *ᵥ v) = ρ s *ᵥ (A *ᵥ v)`.
  have hcomm : ∀ (s : G) (v : n → k), A *ᵥ (ρ s *ᵥ v) = ρ s *ᵥ (A *ᵥ v) := by
    intro s v; rw [Matrix.mulVec_mulVec, Matrix.mulVec_mulVec, hA s]
  -- The `μ`-eigenspace is `ρ`-invariant, and nonzero, so irreducibility ⇒ `⊤`.
  have hEtop : Module.End.eigenspace (Matrix.toLin' A) μ = ⊤ := by
    apply hirr
    · intro s v hv
      rw [Module.End.mem_eigenspace_iff, Matrix.toLin'_apply] at hv ⊢
      rw [hcomm s, hv, Matrix.mulVec_smul]
    · exact hμ
  -- `E = ⊤` ⇒ every vector is a `μ`-eigenvector ⇒ `A = μ • 1`.
  refine Matrix.toLin'.injective (LinearMap.ext fun v => ?_)
  have hv : v ∈ Module.End.eigenspace (Matrix.toLin' A) μ := hEtop ▸ Submodule.mem_top
  rw [Module.End.mem_eigenspace_iff, Matrix.toLin'_apply] at hv
  rw [Matrix.toLin'_apply, Matrix.toLin'_apply, hv, Matrix.smul_mulVec, Matrix.one_mulVec]

end QOU.Archimedean.MatrixSchurCommutant
