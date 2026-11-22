import Mathlib.Algebra.Polynomial.Laurent
import QOU.ParticleInteractions.AtomicityLieRank


/-!
# QOU.Examples.maximal_torus_su2 — Maximal torus for SU(2)

The maximal torus T ≅ U(1) of SU(2):
- V = ℂ² with weight decomposition V = ℂe₊ ⊕ ℂe₋
- e₃ = ½ diag(1, −1) generates T
- t ∈ T acts on e₊ by e^{iθ} and e₋ by e^{−iθ}
- T = { diag(e^{iθ}, e^{−iθ}) : θ ∈ ℝ } ≅ U(1)
- Rank of T = 1 (= rank of SU(2))

**Rank one is DERIVED, not asserted.** The former version set the torus
`rank := 1` with `rank_one := rfl` — a fiat assertion (the "axiomatization ≠
proof" anti-pattern). Here the SU(2) maximal-torus rank is instead *identified*
with the rank of the complexified Lie algebra `𝔰𝔩₂(ℂ)`, and its value `= 1` is
taken from the genuinely-proved `QOU.Atomicity.sl2_rank_eq_one`
(rank from the `ad h` characteristic polynomial `X³ − 4X`, trailing degree 1),
instantiated at the infinite field ℂ. See `su2ComplexifiedRank_eq_one` /
`su2_torus_rank` below.

LaTeX label: `ex:maximal-torus-su2`

## References

- [lusztig1993] https://doi.org/10.1007/978-0-8176-4717-9
- [leitner2026] §1 Example: Maximal torus for SU(2)

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU.Examples

noncomputable section

open QOU.Atomicity LieAlgebra.SpecialLinear

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-! ## Rank of the SU(2) maximal torus — derived from `rank 𝔰𝔩₂(ℂ)`

The maximal torus `T ≅ U(1) ⊂ SU(2)` has `rank = dim T = 1`. Structurally this
rank is the rank of the Lie algebra `𝔰𝔲₂ = Lie(SU(2))`, and rank is a
**complexification invariant**:
`rank_ℝ 𝔰𝔲₂ = rank_ℂ (𝔰𝔲₂ ⊗_ℝ ℂ) = rank_ℂ 𝔰𝔩₂(ℂ)`, because
`𝔰𝔲₂ ⊗_ℝ ℂ ≅ 𝔰𝔩₂(ℂ)` as complex Lie algebras. The QOU categorical substrate
works over the **complexified** algebra `𝔰𝔩₂(ℂ) = sl (Fin 2) ℂ` directly, so we
take the SU(2) maximal-torus rank to be `LieAlgebra.rank ℂ (sl (Fin 2) ℂ)`.

The real-form/complexification bridge `𝔰𝔲₂ ⊗_ℝ ℂ ≅ 𝔰𝔩₂(ℂ)` is a standard fact
(compact real form of `𝔰𝔩₂`); Mathlib has no `sl`-vs-compact-real-form
isomorphism, so that identification is a *modelling choice* stated in prose here,
NOT a fabricated Lean instance. What IS discharged in Lean — replacing the old
`rfl` fiat — is the value: `rank 𝔰𝔩₂(ℂ) = 1`, via the proved
`QOU.Atomicity.sl2_rank_eq_one`. -/

/-- **The SU(2) maximal-torus rank, as the complexified Lie-algebra rank.**
    `= LieAlgebra.rank ℂ (sl (Fin 2) ℂ)`. The `Module.Finite`/`Module.Free`
    instances (needed to form `LieAlgebra.rank`) come from the 𝔰𝔩₂ triple basis
    `QOU.Atomicity.sl2Basis`; both are Prop-valued, so they agree with the
    instances used inside `sl2_rank_eq_one` by proof irrelevance. -/
def su2ComplexifiedRank : ℕ :=
  haveI : Module.Finite ℂ (sl (Fin 2) ℂ) := Module.Finite.of_basis (sl2Basis ℂ)
  haveI : Module.Free ℂ (sl (Fin 2) ℂ) := Module.Free.of_basis (sl2Basis ℂ)
  LieAlgebra.rank ℂ (sl (Fin 2) ℂ)

/-- **`rank 𝔰𝔩₂(ℂ) = 1` — DERIVED from the proved `sl2_rank_eq_one`.**
    This is the atomicity Lie-rank theorem (built from the `ad h` charpoly
    `X³ − 4X`, trailing degree `1`) instantiated at ℂ (an infinite field with
    `2 ≠ 0`). It replaces the former structure-field fiat `rank_one := rfl`. -/
theorem su2ComplexifiedRank_eq_one : su2ComplexifiedRank = 1 := by
  unfold su2ComplexifiedRank
  exact sl2_rank_eq_one (K := ℂ) (by norm_num)

/-- **SU(2) maximal torus data**: T ≅ U(1) with 2 weight spaces.

    LaTeX: `\label{ex:maximal-torus-su2}` -/
-- Ref: [lusztig1993] Lusztig, "Introduction to Quantum Groups," Birkhäuser 1993 (DOI: 10.1007/978-0-8176-4717-9)
structure SU2MaximalTorusData where
  /-- Number of weight spaces in the fundamental V = ℂ². -/
  numWeightSpaces : ℕ
  /-- V decomposes into 2 weight spaces (±1/2). -/
  weight_decomp : numWeightSpaces = 2
  /-- Rank of the maximal torus. -/
  rank : ℕ
  /-- T has rank 1 (one-dimensional torus ≅ U(1)). -/
  rank_one : rank = 1
  /-- The weights of V are ±1/2 (represented as ±1 in the twice-weight convention). -/
  weights : List ℤ
  /-- The weight list for V_{1/2}. -/
  weights_are : weights = [1, -1]

/-- The maximal torus data for SU(2).

    `rank` is populated by `su2ComplexifiedRank = rank 𝔰𝔩₂(ℂ)` and its `= 1`
    proof by `su2ComplexifiedRank_eq_one` — so the rank-one datum bottoms out at
    the proved `QOU.Atomicity.sl2_rank_eq_one`, not at `rfl`. -/
-- Ref: [leitner2026] §1
def su2MaximalTorus : SU2MaximalTorusData where
  numWeightSpaces := 2
  weight_decomp := rfl
  rank := su2ComplexifiedRank
  rank_one := su2ComplexifiedRank_eq_one
  weights := [1, -1]
  weights_are := rfl

/-- T has rank 1 (≅ U(1)) — derived, via `su2MaximalTorus.rank_one`, from
    `su2ComplexifiedRank_eq_one` and ultimately `QOU.Atomicity.sl2_rank_eq_one`. -/
theorem su2_torus_rank : su2MaximalTorus.rank = 1 := su2MaximalTorus.rank_one

/-- V_{1/2} has 2 weight spaces. -/
theorem su2_weight_count : su2MaximalTorus.numWeightSpaces = 2 := rfl

end

end QOU.Examples
