import QOU.Core.QDifferentialGeometry
import Mathlib.LinearAlgebra.Matrix.Trace

/-!
# Trial: the normalised categorical Lagrangian (owner, 2026-11-21, "Try 1 for now")

`NormalisedCategoricalLagrangian` adds one field to `CategoricalLagrangian`: the state is
normalised, `ψ ≫ ψ* = 𝟙`. This is a **trial**, logged in `docs/coordination/owner-rulings.md`;
`def:categorical-lagrangian` itself is unchanged.

What it buys downstream:

* `matter_projector_idempotent`: `ψ* ≫ ψ` is an idempotent, so the matter term `ψ* ≫ ψ ≫ 𝒟`
  is `𝒟` compressed onto the line of the state.
* `matter_trace_eq_eigenvalue` (matrix model, `D` acting on columns, matter term `D ψ φ`): if
  `φ ψ = 1` and `D ψ = μ • ψ`, then `tr(D ψ φ) = μ`.
* `weighted_matter_trace_eq_eigenvalue`: with a Cartan weight `K ψ = w • ψ`,
  `tr(K ψ φ D) = w μ`.

So under normalisation the own-sector constant `c` of `TwoTermMatterOwnSector.lean` is
the `∇`-eigenvalue of the nucleon state (an expectation value in general), with no scale
attached. The neutron/proton horizontal split is `q⁻¹·(q⁻¹ − q)·μ`.

What it does not buy: it does not supply `∇`. The corpus `nablaEndo` is still uninstantiated,
so `μ` is not computed here, and nothing here produces the 12.
-/

namespace QOU.MassTheory.NormalisedLagrangian

open CategoryTheory MonoidalCategory

universe u v

/-- A categorical Lagrangian whose state is normalised, `ψ ≫ ψ* = 𝟙`. -/
structure NormalisedCategoricalLagrangian (R : Type*) [CommRing R]
    (C : Type u) [Category.{v} C] [MonoidalCategory C] [BraidedCategory C]
    [Preadditive C] [Linear R C] (fh : QOU.FrobeniusHopfData C)
    extends QOU.CategoricalLagrangian R C fh where
  /-- The state is normalised against its own costate. -/
  normalised : state ≫ costate = 𝟙 (𝟙_ C)

variable {R : Type*} [CommRing R] {C : Type u} [Category.{v} C] [MonoidalCategory C]
  [BraidedCategory C] [Preadditive C] [Linear R C] {fh : QOU.FrobeniusHopfData C}

/-- `ψ* ≫ ψ` is idempotent for a normalised state. -/
theorem matter_projector_idempotent (L : NormalisedCategoricalLagrangian R C fh) :
    (L.costate ≫ L.state) ≫ (L.costate ≫ L.state) = L.costate ≫ L.state := by
  rw [Category.assoc, ← Category.assoc L.state, L.normalised, Category.id_comp]

/-- The matter term is `𝒟` precomposed with the idempotent `ψ* ≫ ψ`. -/
theorem matter_term_eq_projector_comp (L : NormalisedCategoricalLagrangian R C fh) :
    L.costate ≫ L.state ≫ L.dirac.dirac = (L.costate ≫ L.state) ≫ L.dirac.dirac := by
  rw [Category.assoc]

open Matrix

variable {K : Type*} [CommRing K] {n : Type*} [Fintype n]

/-- Matrix model: for a normalised eigenstate, the trace of the matter term is the eigenvalue. -/
theorem matter_trace_eq_eigenvalue (D : Matrix n n K) (ψ : Matrix n (Fin 1) K)
    (φ : Matrix (Fin 1) n K) (μ : K) (hn : φ * ψ = 1) (hD : D * ψ = μ • ψ) :
    trace (D * (ψ * φ)) = μ := by
  rw [← Matrix.mul_assoc, Matrix.trace_mul_comm, hD, Matrix.mul_smul, hn, Matrix.trace_smul, Matrix.trace_one, Fintype.card_fin,
    Nat.cast_one, smul_eq_mul, mul_one]

/-- With a Cartan weight `K ψ = w • ψ`, the weighted matter trace is `w μ`. -/
theorem weighted_matter_trace_eq_eigenvalue (Kc D : Matrix n n K) (ψ : Matrix n (Fin 1) K)
    (φ : Matrix (Fin 1) n K) (w μ : K) (hn : φ * ψ = 1) (hK : Kc * ψ = w • ψ)
    (hD : D * ψ = μ • ψ) :
    trace (Kc * (ψ * φ) * D) = w * μ := by
  have h1 : Kc * (ψ * φ) * D = (Kc * ψ) * (φ * D) := by simp only [Matrix.mul_assoc]
  rw [h1, Matrix.trace_mul_comm, hK, Matrix.mul_smul, Matrix.trace_smul, Matrix.mul_assoc,
    hD, Matrix.mul_smul, hn, Matrix.trace_smul, Matrix.trace_one, Fintype.card_fin,
    Nat.cast_one, smul_eq_mul, smul_eq_mul, mul_one]

/-- Neutron minus proton horizontal matter trace for normalised eigenstates sharing `μ`, with
horizontal weight `q⁻¹` and sector weights `q` (proton) and `q⁻¹` (neutron). -/
theorem nucleon_horizontal_split (q qi μ : K) :
    qi * (qi * μ) - qi * (q * μ) = qi * (qi - q) * μ := by ring

end QOU.MassTheory.NormalisedLagrangian
