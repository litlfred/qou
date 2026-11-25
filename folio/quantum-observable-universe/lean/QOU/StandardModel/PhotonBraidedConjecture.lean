/-
  Conjecture carrier: γγ is the product of a braided tensor algebra on the photon space.

  Owner ruling 2026-11-25 ("3y"): test, Lean first, whether γγ pair production is natural
  as the degree-2 product of a braided (not symmetric) tensor algebra on the photon space
  `W = span{σ₀, σ₁, σ₀σ₁⁻¹}`.

  What is measured (exact over `ℚ(q)`, `computations/probes/photon_jet_spectral/
  tangent_followups_probe.py`): the associated graded of the photon filtration of `H₃(q)` is
  the quadratic algebra `T(W)/(R)` with `R = ker(W ⊗ W → gr₂)`, `dim R = 7`, Hilbert series
  `1 + 3t + 2t²`, degree 3 zero. That fact is NOT stated here; it is the input.

  The conjecture is the structure `BraidedPhotonPresentation`: a braiding `c` on `W ⊗ W`
  (a solution of the braid relation on `W ⊗ W ⊗ W`) and a scalar `μ` with
  `ker(c − μ) = Rel`, i.e. the two-photon relations are one eigenspace of a braiding (as the
  q-exterior relations of a q-symmetric algebra are). There is no instance: the conjecture is
  open. Two limits on the carrier, stated honestly:
  * it is not discharged by scalar braidings: `c = μ` braids, but `ker(c − μ)` is everything,
    which is not a proper `Rel` (`scalar_not_presentation`; measured `dim Rel = 7 < 9`);
  * it is not shown to be non-vacuous in general. Whether every subspace is an eigenspace of
    some braiding is not settled here, so an instance would need to come with `c` tied to the
    Hecke structure (e.g. built from the action of `H₃(q)` on `W`) to mean anything.
  Measured obstruction (audit §8): for the two standard braidings on a 3-dimensional space,
  the `U_q(gl₃)` vector braiding (eigenspaces 6, 3) and the `U_q(sl₂)` spin-1 braiding
  (eigenspaces 5, 3, 1), no eigenspace and no sum of eigenspaces has dimension 7, so `Rel` is
  not one of their eigenspaces.

  Generic commutative ring `R₀` and module `W` (§7c).

  -- Ref: [leitner2026] predicted-spectra, def:photon
  -- Ref: [kassel2008] https://doi.org/10.1007/978-0-387-68548-9
-/
import Mathlib.LinearAlgebra.TensorProduct.Basic
import Mathlib.LinearAlgebra.TensorProduct.Associator

namespace QOU.PhotonBraided

open TensorProduct

variable {R₀ W : Type*} [CommRing R₀] [AddCommGroup W] [Module R₀ W]

/-- `c ⊗ 1` on `W ⊗ (W ⊗ W)`, through the associator. -/
noncomputable def c12 (c : W ⊗[R₀] W →ₗ[R₀] W ⊗[R₀] W) :
    W ⊗[R₀] (W ⊗[R₀] W) →ₗ[R₀] W ⊗[R₀] (W ⊗[R₀] W) :=
  (TensorProduct.assoc R₀ W W W).toLinearMap ∘ₗ TensorProduct.map c LinearMap.id ∘ₗ
    (TensorProduct.assoc R₀ W W W).symm.toLinearMap

/-- `1 ⊗ c` on `W ⊗ (W ⊗ W)`. -/
noncomputable def c23 (c : W ⊗[R₀] W →ₗ[R₀] W ⊗[R₀] W) :
    W ⊗[R₀] (W ⊗[R₀] W) →ₗ[R₀] W ⊗[R₀] (W ⊗[R₀] W) :=
  TensorProduct.map LinearMap.id c

/-- The braid (Yang–Baxter) relation for `c`. -/
def IsBraiding (c : W ⊗[R₀] W →ₗ[R₀] W ⊗[R₀] W) : Prop :=
  c12 c ∘ₗ c23 c ∘ₗ c12 c = c23 c ∘ₗ c12 c ∘ₗ c23 c

/-- **Conjecture carrier.** The two-photon relations `Rel` form one eigenspace of a
braiding. -/
structure BraidedPhotonPresentation (Rel : Submodule R₀ (W ⊗[R₀] W)) : Prop where
  exists_braiding :
    ∃ (c : W ⊗[R₀] W →ₗ[R₀] W ⊗[R₀] W) (μ : R₀),
      IsBraiding c ∧ LinearMap.ker (c - μ • LinearMap.id) = Rel

/-- A scalar `c = μ` is a braiding. -/
theorem isBraiding_scalar (μ : R₀) :
    IsBraiding (μ • LinearMap.id : W ⊗[R₀] W →ₗ[R₀] W ⊗[R₀] W) := by
  have hm1 : TensorProduct.map (μ • LinearMap.id : W ⊗[R₀] W →ₗ[R₀] W ⊗[R₀] W)
      (LinearMap.id : W →ₗ[R₀] W) = μ • LinearMap.id :=
    TensorProduct.ext' fun x y => by simp [TensorProduct.smul_tmul']
  have hm2 : TensorProduct.map (LinearMap.id : W →ₗ[R₀] W)
      (μ • LinearMap.id : W ⊗[R₀] W →ₗ[R₀] W ⊗[R₀] W) = μ • LinearMap.id :=
    TensorProduct.ext' fun x y => by simp [TensorProduct.tmul_smul]
  have h12 : c12 (μ • LinearMap.id : W ⊗[R₀] W →ₗ[R₀] W ⊗[R₀] W) = μ • LinearMap.id := by
    apply LinearMap.ext; intro z; simp [c12, hm1]
  have h23 : c23 (μ • LinearMap.id : W ⊗[R₀] W →ₗ[R₀] W ⊗[R₀] W) = μ • LinearMap.id := by
    simp [c23, hm2]
  simp only [IsBraiding, h12, h23]

/-- **Scalar braidings do not discharge the carrier** for a proper relation space. -/
theorem scalar_not_presentation (μ : R₀) (Rel : Submodule R₀ (W ⊗[R₀] W)) (hRel : Rel ≠ ⊤) :
    LinearMap.ker ((μ • LinearMap.id : W ⊗[R₀] W →ₗ[R₀] W ⊗[R₀] W) - μ • LinearMap.id)
      ≠ Rel := by
  simpa using hRel.symm

end QOU.PhotonBraided
