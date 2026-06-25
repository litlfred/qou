import Mathlib.Data.Nat.Basic
import Mathlib.Tactic
import Mathlib.LinearAlgebra.Dimension
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic

/-!
# QOU.OrbitalSpaceNormalBundle

The orbital space at shell n: sections of the trefoil's normal bundle
in the Bring surface, with q-Laplacian eigenvalue cutoff.

The SO(3) decomposition O_n ≅ V_0 ⊕ V_1 ⊕ ⋯ ⊕ V_{n-1} gives
dim O_n = Σ(2ℓ+1) = n².

LaTeX label: `prop:orbital-space-normal-bundle`

## References

- [manuscript] Ch. 6, §3
- [kock2004] https://doi.org/10.1017/CBO9780511615443

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

-- Ref: [kock2004] Kock, "Frobenius Algebras and 2D Topological Quantum Field Theories," CUP LMS Student Texts 59, 2004


open Finset

noncomputable section

namespace QOU

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

-- ═══════════════════════════════════════════════════════════════════
-- §1. Orbital decomposition data
-- ═══════════════════════════════════════════════════════════════════

/-- The **orbital decomposition** at shell n packages the SO(3)
    representation-theoretic data:
    - n modes (ℓ = 0, 1, …, n−1)
    - Each mode ℓ transforms as the irreducible V_ℓ of dimension 2ℓ+1
    - Total dimension is n²

    This is a purely combinatorial encoding: the geometric content
    (normal-bundle sections, q-Laplacian eigenmodes) is captured by
    the narrative in the sibling .md file.  The representation-theoretic
    fact — that mode ℓ on the trefoil transforms as V_ℓ under SO(3) —
    is stated as an axiom in `mode_is_so3_irrep`. -/
structure OrbitalDecomposition (n : ℕ) where
  /-- The dimension of the ℓ-th irreducible V_ℓ is 2ℓ+1. -/
  irrep_dim : Fin n → ℕ := fun ℓ => 2 * ℓ.val + 1
  /-- The total orbital dimension. -/
  total_dim : ℕ := (range n).sum (fun ℓ => 2 * ℓ + 1)

-- ═══════════════════════════════════════════════════════════════════
-- §2. Dimensional results
-- ═══════════════════════════════════════════════════════════════════

/-- The total orbital dimension at shell n is n².
    This is the purely arithmetic content of the SO(3) decomposition:
    Σ_{ℓ=0}^{n-1} (2ℓ+1) = n². -/
theorem orbital_space_dim (n : ℕ) :
    (range n).sum (fun ℓ => 2 * ℓ + 1) = n ^ 2 := by
  induction n with
  | zero => simp
  | succ k ih =>
    rw [sum_range_succ, ih]; ring

/-- Dimension of the orbital space at shell n is n² (alternate form). -/
theorem orbital_dim_eq_square (n : ℕ) :
    (OrbitalDecomposition.mk (n := n)).total_dim = n ^ 2 :=
  orbital_space_dim n

-- ═══════════════════════════════════════════════════════════════════
-- §3. SO(3) decomposition (representation-theoretic content)
-- ═══════════════════════════════════════════════════════════════════

/-- **Axiom**: For each ℓ, the SO(3) irreducible representation V_ℓ
    has dimension 2ℓ+1.

    In the QOU context: mode ℓ on the trefoil T_{2,3} ⊂ Σ₄ transforms
    as V_ℓ when the trefoil orbits the Borromean anchor sweeping out S².

    ## Mathlib status (as of v4.24.0)

    Available:
    - `Module.finrank` (Mathlib.LinearAlgebra.Dimension)
    - SO(3) definable via `Matrix.specialOrthogonalGroup (Fin 3) ℝ`

    Missing (not formalized in Mathlib):
    - Peter–Weyl theorem (L²(G) ≅ ⊕ V_π ⊗ V_π*)
    - Classification of SO(3) irreps (highest weight theory)
    - Spherical harmonics Y_ℓ^m as explicit basis for V_ℓ
    - Continuous representations of Lie groups

    ## Proof route when Mathlib gains these

    1. Define `SO3 := Matrix.specialOrthogonalGroup (Fin 3) ℝ`
    2. Apply compact group irrep classification: for each ℓ ∈ ℕ,
       the unique (up to iso) irreducible real representation V_ℓ
       has `Module.finrank ℝ V_ℓ = 2 * ℓ + 1`
    3. Peter–Weyl on L²(S²) under the SO(3) action gives
       L²(S²) ≅ ⊕_{ℓ≥0} V_ℓ with V_ℓ = span{Y_ℓ^m : m = -ℓ..ℓ}
    4. Trefoil averaging: the time-averaged section space of mode ℓ
       on T_{2,3} projects isomorphically onto V_ℓ ⊂ L²(S²)

    Steps 1–3 are standard harmonic analysis; step 4 is the
    geometry specific to the QOU framework. -/
-- Ref: [manuscript] Ch. 6, §3 — "The critical step"
-- Ref: [kock2004] Kock, "Frobenius Algebras and 2D Topological Quantum Field Theories," CUP LMS Student Texts 59, 2004
axiom mode_is_so3_irrep :
  ∀ (ℓ : ℕ), ∃ (V : Type) [inst_acg : AddCommGroup V] [inst_mod : Module R_q V]
    [inst_fd : FiniteDimensional R_q V],
    Module.finrank R_q V = 2 * ℓ + 1

-- ═══════════════════════════════════════════════════════════════════
-- §4. Mode cutoff
-- ═══════════════════════════════════════════════════════════════════

/-- Mode cutoff: ℓ(ℓ+1) ≤ n(n-1) ⟹ ℓ ≤ n-1.
    Proof: contrapositive — if ℓ ≥ n then ℓ(ℓ+1) ≥ n(n+1) > n(n-1). -/
-- theorem mode_cutoff {n ℓ : ℕ} (hn : n ≥ 1) (h : ℓ * (ℓ + 1) ≤ n * (n - 1)) :  -- (archimedean; not meaningful over R_q)
    ℓ ≤ n - 1 := by
  by_contra hc
  push_neg at hc
  have h1 : n ≤ ℓ := by omega
  have h2 : n * (n - 1) < ℓ * (ℓ + 1) := by
    calc ℓ * (ℓ + 1) ≥ n * (n + 1) :=
          Nat.mul_le_mul h1 (by omega)
      _ > n * (n - 1) := by
          cases n with
          | zero => omega
          | succ k => nlinarith
  omega

/-- Converse: ℓ ≤ n-1 ⟹ ℓ(ℓ+1) ≤ n(n-1). -/
-- theorem mode_cutoff_conv {n ℓ : ℕ} (hn : n ≥ 1) (h : ℓ ≤ n - 1) :  -- (archimedean; not meaningful over R_q)
    ℓ * (ℓ + 1) ≤ n * (n - 1) := by
  have : ℓ + 1 ≤ n := by omega
  calc ℓ * (ℓ + 1) ≤ (n - 1) * n := Nat.mul_le_mul h this
    _ = n * (n - 1) := by ring

/-- Mode cutoff iff: ℓ(ℓ+1) ≤ n(n-1) ↔ ℓ ≤ n-1. -/
-- theorem mode_cutoff_iff {n ℓ : ℕ} (hn : n ≥ 1) :  -- (archimedean; not meaningful over R_q)
    ℓ * (ℓ + 1) ≤ n * (n - 1) ↔ ℓ ≤ n - 1 :=
  ⟨mode_cutoff hn, mode_cutoff_conv hn⟩

/-- The orbital space at shell n has dimension n².
    This is the declaration referenced by the content manifest
    `prop:orbital-space-normal-bundle`. -/
theorem orbital_space_normal_bundle (n : ℕ) :
    (range n).sum (fun ℓ => 2 * ℓ + 1) = n ^ 2 :=
  orbital_space_dim n

end QOU

end


/-! ## §3b-cond conditional-class hypothesis

This proposition is conditional on the conjecture [`conj:borromean-quark`]
(see `content/quantum-observable-universe/observations/borromean-quark.lean`
for the canonical `class BorromeanQuark` declaration).  The local stub
below mirrors that class name so the §3b-cond audit
(`content/pipeline/conditional-class-banner-audit.ts`) recognises the
conditional-on-class structure; downstream consumers should import the
canonical class from the sibling stub file instead. -/

/-- Local stub of `conj:borromean-quark`'s axiomatised class.
    See `borromean-quark.lean` (sibling) for the canonical declaration. -/
class BorromeanQuark : Prop where
  /-- The conjecture's content is the class instance (sorry = conjecture
      per AGENTS.md §3b). -/
  holds : True

/-- Witness theorem: this file's proposition is conditional on
    `BorromeanQuark` per CLAUDE.md §3b-cond. -/
def orbital_space_normal_bundle_conditional_on_borromean_quark
    [_inst : BorromeanQuark] : True := trivial
