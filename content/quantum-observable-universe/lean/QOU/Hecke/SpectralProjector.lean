import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination

/-!
# QOU.Hecke.SpectralProjector — the rank (generator-level) Hecke spectral projectors

The Iwahori–Hecke generator `σ` satisfies `(σ − q)(σ + q⁻¹) = 0`, equivalently the
quadratic `σ² = (q − q⁻¹)σ + 1`, so `σ` carries exactly the two eigenvalues
`{q, −q⁻¹}`. The two **spectral projectors**

* `e₊ = (σ + q⁻¹)/(q + q⁻¹)` — the **symmetric** (eigenvalue `q`) block,
* `e₋ = (q − σ)/(q + q⁻¹)` — the **antisymmetric** (eigenvalue `−q⁻¹`) block,

are **idempotent**, **orthogonal**, and **complete** (`e₊ + e₋ = 1`). They are the
`q`-Young symmetrizer / antisymmetrizer at the GENERATOR level — the `n = 2` case
of `e_λ = P(q)⁻¹ Σ_w q^{ℓ(w)} T_w` (see `rem:h3-hecke-idempotents`).

**Why this is only the rank case (the owner's "have full matrices").** A block-swap
braid `β = σ_{i₁}⋯σ_{i₉}` is a *word*, NOT a generator, so it does **not** satisfy
the Hecke quadratic: on a reducible module its R-matrix carries far more than two
eigenvalues (22 distinct at `H₆`, `block_swap_spectrum.py`). The exact `q`-correct
projector for `β` is the full **Lagrange** spectral projector
`Π_{μ≠λ}(β − μ)/(λ − μ)` — verified idempotent numerically in that module — of which
the `e₊ / e₋` proved here are the rank-1 building blocks. Reducing the symmetrizer
to a scalar combination of `{id, β}` (degree ≤ 1) is therefore insufficient.

All four facts close by `field_simp` + `linear_combination` against the Hecke
quadratic (sympy-cross-checked). Self-contained `Field` identities.
-/

namespace QOU.Hecke.SpectralProjector

variable {R : Type*} [Field R]

/-- The Hecke quadratic in solved form: `σ² = (q − q⁻¹)·σ + 1`
(equivalent to `(σ − q)(σ + q⁻¹) = 0`). -/
def HeckeQuadratic (q σ : R) : Prop := σ ^ 2 = (q - q⁻¹) * σ + 1

/-- **Symmetric projector is idempotent.** `e₊ = (σ+q⁻¹)/(q+q⁻¹)`, `e₊² = e₊`. -/
theorem eplus_idem (q σ : R) (hq : q + q⁻¹ ≠ 0) (h : HeckeQuadratic q σ) :
    ((σ + q⁻¹) / (q + q⁻¹)) ^ 2 = (σ + q⁻¹) / (q + q⁻¹) := by
  rw [HeckeQuadratic] at h
  field_simp
  linear_combination h

/-- **Antisymmetric projector is idempotent.** `e₋ = (q−σ)/(q+q⁻¹)`, `e₋² = e₋`. -/
theorem eminus_idem (q σ : R) (hq : q + q⁻¹ ≠ 0) (h : HeckeQuadratic q σ) :
    ((q - σ) / (q + q⁻¹)) ^ 2 = (q - σ) / (q + q⁻¹) := by
  rw [HeckeQuadratic] at h
  field_simp
  linear_combination h

/-- **Orthogonality.** `e₊ · e₋ = 0` — the symmetric and antisymmetric blocks meet
only at `0`. -/
theorem eplus_eminus_orthogonal (q σ : R) (hq : q + q⁻¹ ≠ 0) (h : HeckeQuadratic q σ) :
    ((σ + q⁻¹) / (q + q⁻¹)) * ((q - σ) / (q + q⁻¹)) = 0 := by
  rw [HeckeQuadratic] at h
  field_simp
  linear_combination -h

/-- **Completeness.** `e₊ + e₋ = 1` — the two spectral blocks resolve the identity. -/
theorem eplus_add_eminus (q σ : R) (hq : q + q⁻¹ ≠ 0) :
    (σ + q⁻¹) / (q + q⁻¹) + (q - σ) / (q + q⁻¹) = 1 := by
  field_simp

end QOU.Hecke.SpectralProjector
