import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination

/-!
# QOU.Hecke.SpectralProjector — the rank (generator-level) Hecke spectral projectors

The Iwahori–Hecke generator `σ` satisfies `(σ − q)(σ + q⁻¹) = 0`; clearing `q`
gives the polynomial form `q·σ² = (q² − 1)·σ + q`, so `σ` carries exactly the two
eigenvalues `{q, −q⁻¹}`. Written over the common denominator `q² + 1`, the two
**spectral projectors** are

* `e₊ = (q·σ + 1)/(q² + 1)` — the **symmetric** (eigenvalue `q`) block,
* `e₋ = (q² − q·σ)/(q² + 1)` — the **antisymmetric** (eigenvalue `−q⁻¹`) block.

They are **idempotent**, **orthogonal**, and **complete** (`e₊ + e₋ = 1`). These
are the `q`-Young (anti)symmetrizers at the GENERATOR level — the `n = 2` case of
`e_λ = P(q)⁻¹ Σ_w q^{ℓ(w)} T_w` (see `rem:h3-hecke-idempotents`), and the
algebraic origin of the **sign-alternating Bethe–Weizsäcker pairing term** (the
two Hecke eigenvalues, `bw-mass-decomposition-dictionary.md`).

**Why this is only the rank case (the owner's "have full matrices").** A block-swap
braid `β = σ_{i₁}⋯σ_{i₉}` is a *word*, not a generator, so it does **not** satisfy
the Hecke quadratic: on a reducible module its R-matrix carries far more than two
eigenvalues (22 distinct at `H₆`, `block_swap_spectrum.py`). The exact `q`-correct
projector for `β` is the full **Lagrange** spectral projector `Π_{μ≠λ}(β−μ)/(λ−μ)`
(verified idempotent numerically), of which the `e₊/e₋` proved here are the
rank-1 building blocks — so reducing the symmetrizer to a scalar combination of
`{id, β}` (degree ≤ 1) is provably insufficient.

All four facts close by `field_simp` + `linear_combination` against the Hecke
quadratic (sympy-cross-checked). Self-contained over any `Field` with `q² + 1 ≠ 0`.
-/

namespace QOU.Hecke.SpectralProjector

variable {R : Type*} [Field R]

/-- The Hecke quadratic in cleared polynomial form: `q·σ² = (q² − 1)·σ + q`
(equivalent to `(σ − q)(σ + q⁻¹) = 0` for `q ≠ 0`). -/
def HeckeQuadratic (q σ : R) : Prop := q * σ ^ 2 = (q ^ 2 - 1) * σ + q

/-- **Symmetric projector is idempotent.** `e₊ = (qσ+1)/(q²+1)`, `e₊² = e₊`. -/
theorem eplus_idem (q σ : R) (hq : q ^ 2 + 1 ≠ 0) (h : HeckeQuadratic q σ) :
    ((q * σ + 1) / (q ^ 2 + 1)) ^ 2 = (q * σ + 1) / (q ^ 2 + 1) := by
  rw [HeckeQuadratic] at h
  field_simp
  linear_combination q * h

/-- **Antisymmetric projector is idempotent.** `e₋ = (q²−qσ)/(q²+1)`, `e₋² = e₋`. -/
theorem eminus_idem (q σ : R) (hq : q ^ 2 + 1 ≠ 0) (h : HeckeQuadratic q σ) :
    ((q ^ 2 - q * σ) / (q ^ 2 + 1)) ^ 2 = (q ^ 2 - q * σ) / (q ^ 2 + 1) := by
  rw [HeckeQuadratic] at h
  field_simp
  linear_combination q * h

/-- **Orthogonality.** `e₊ · e₋ = 0` — the symmetric and antisymmetric blocks meet
only at `0`. -/
theorem eplus_eminus_orthogonal (q σ : R) (hq : q ^ 2 + 1 ≠ 0) (h : HeckeQuadratic q σ) :
    ((q * σ + 1) / (q ^ 2 + 1)) * ((q ^ 2 - q * σ) / (q ^ 2 + 1)) = 0 := by
  rw [HeckeQuadratic] at h
  field_simp
  linear_combination -q * h

/-- **Completeness.** `e₊ + e₋ = 1` — the two spectral blocks resolve the identity. -/
theorem eplus_add_eminus (q σ : R) (hq : q ^ 2 + 1 ≠ 0) :
    (q * σ + 1) / (q ^ 2 + 1) + (q ^ 2 - q * σ) / (q ^ 2 + 1) = 1 := by
  field_simp
  ring

end QOU.Hecke.SpectralProjector
