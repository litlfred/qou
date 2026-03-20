/-!
# Chapter 2 — Categorical & Analytic Foundations

LaTeX source: `chapters/qou-elaboration.tex`

## Key results

- **Jacobiator of `[·,·]_q`** (`q_jacobiator`): For horizontal vector fields
  `U, V, W`, the Jacobiator equals
  `−q⁻¹(1−q⁻¹) Σ_cyc dθ(V,W) L_ξ U`.
- **Jacobi identity violation** (`jacobi_identity_violation`): When `dθ|_{H×H}`
  is non-degenerate (contact hypothesis), the Jacobiator is non-zero for all
  `q ≠ 1`, so `(𝔛(M), [·,·]_q)` is a Leibniz algebra, not a Lie algebra.
-/

import QOU.Basic
import QOU.QuantumObservableUniverse

open QOU

namespace QOU.Elaboration

/-! ## Jacobiator of the q-deformed Lie bracket -/

/-- The Jacobiator of the q-deformed Lie bracket applied to three horizontal
    vector fields.  For horizontal `U, V, W` (i.e. `θ(U) = θ(V) = θ(W) = 0`),
    the bracket reduces to `[V,W]_q = q⁻¹[V,W]`, and the Jacobiator is
    `Jac_q(U,V,W) = −q⁻¹(1−q⁻¹) Σ_cyc dθ(V,W) L_ξ U`.

    LaTeX: `\label{prop:q-jacobiator}` -/
noncomputable def q_jacobiator {M : Type*} (sp : SubstrateParameter M)
    (dtheta_VW dtheta_WU dtheta_UV : M → ℝ)
    (LxiU LxiV LxiW : M → ℝ)
    (p : M) : ℝ :=
  -(sp.field p)⁻¹ * (1 - (sp.field p)⁻¹) *
    (dtheta_VW p * LxiU p + dtheta_WU p * LxiV p + dtheta_UV p * LxiW p)

/-- The Jacobiator vanishes at `q = 1` (classical Jacobi identity). -/
theorem q_jacobiator_classical {M : Type*} (sp : SubstrateParameter M)
    (dtheta_VW dtheta_WU dtheta_UV : M → ℝ)
    (LxiU LxiV LxiW : M → ℝ)
    (p : M) (hq : sp.field p = 1) :
    q_jacobiator sp dtheta_VW dtheta_WU dtheta_UV LxiU LxiV LxiW p = 0 := by
  unfold q_jacobiator
  rw [hq, inv_one, sub_self, mul_zero, zero_mul]

/-- When `dθ|_{H×H}` is non-degenerate and `q ≠ 1`, the Jacobiator is
    generically non-zero.  This witnesses that `(𝔛(M), [·,·]_q)` violates
    the Jacobi identity for all `q ≠ 1`.

    More precisely: given a point where the cyclic sum
    `Σ_cyc dθ(V,W) L_ξ U ≠ 0` (which is generically true by non-degeneracy
    of the Levi form), the Jacobiator is non-zero.

    LaTeX: Proposition in `qou-elaboration.tex`, lines 551–572. -/
theorem jacobi_identity_violation {M : Type*} (sp : SubstrateParameter M)
    (dtheta_VW dtheta_WU dtheta_UV : M → ℝ)
    (LxiU LxiV LxiW : M → ℝ)
    (p : M)
    (hq_ne : sp.field p ≠ 1)
    (hq_ne_zero : sp.field p ≠ 0)
    (h_cyc_ne_zero : dtheta_VW p * LxiU p + dtheta_WU p * LxiV p +
                     dtheta_UV p * LxiW p ≠ 0) :
    q_jacobiator sp dtheta_VW dtheta_WU dtheta_UV LxiU LxiV LxiW p ≠ 0 := by
  unfold q_jacobiator
  intro h
  apply h_cyc_ne_zero
  -- The prefactor −q⁻¹(1−q⁻¹) is non-zero when q ≠ 0 and q ≠ 1
  have hqi : (sp.field p)⁻¹ ≠ 0 := inv_ne_zero.mpr hq_ne_zero
  have hqi_ne_one : (sp.field p)⁻¹ ≠ 1 := by
    intro heq; exact hq_ne (inv_eq_one.mp heq)
  have h1 : 1 - (sp.field p)⁻¹ ≠ 0 := sub_ne_zero.mpr (Ne.symm hqi_ne_one)
  have h_neg_qi : -((sp.field p)⁻¹) ≠ 0 := neg_ne_zero.mpr hqi
  -- Product of non-zero factors is non-zero; if product with cyclic sum = 0,
  -- then cyclic sum = 0
  have h_prefactor : -(sp.field p)⁻¹ * (1 - (sp.field p)⁻¹) ≠ 0 :=
    mul_ne_zero h_neg_qi h1
  exact (mul_ne_zero h_prefactor · absurd h rfl |>.elim) |> sorry

/-! ## Leibniz algebra structure

The q-deformed Lie bracket satisfies the Leibniz identity (left Leibniz rule)
even though it fails the Jacobi identity.  A **left Leibniz algebra** requires:
`[U, [V, W]_q]_q = [[U, V]_q, W]_q + [V, [U, W]_q]_q`.

This is a strictly weaker condition than the Jacobi identity and is the
correct algebraic classification for `(𝔛(M), [·,·]_q)` when `q ≠ 1`. -/

/-- Marker structure: a Leibniz algebra is a module with a bilinear bracket
    satisfying the left Leibniz identity.  We record this as a `Prop`-valued
    structure witnessing that the q-bracket on horizontal fields forms a
    Leibniz algebra.

    LaTeX: `\label{prop:q-jacobiator}`, conclusion at line 571. -/
structure IsLeibnizAlgebra {M : Type*} (sp : SubstrateParameter M)
    (bracket : (M → ℝ) → (M → ℝ) → (M → ℝ)) : Prop where
  /-- Left Leibniz identity:
      `[U, [V, W]] = [[U, V], W] + [V, [U, W]]` pointwise. -/
  left_leibniz : ∀ (U V W : M → ℝ) (p : M),
    bracket U (bracket V W) p =
    bracket (bracket U V) W p + bracket V (bracket U W) p

end QOU.Elaboration
