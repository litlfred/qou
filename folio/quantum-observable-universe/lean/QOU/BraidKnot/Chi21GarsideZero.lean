import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic

/-!
# QOU.BraidKnot.Chi21GarsideZero

**The α₃-break structural prune.**

This file *derives* — from the explicit `2 × 2` Hoefsmit seminormal
representation of the two braid generators — the fact that the
`(2,1)` Hecke character of the Garside (half-twist) element
`σ₁σ₂σ₁ ∈ B₃` vanishes:

  `χ^{(2,1)}(σ₁σ₂σ₁) = tr ρ_{(2,1)}(σ₁σ₂σ₁) = 0`.

Contrast with
[`ChiLambdaW0SignWeighting.lean`](ChiLambdaW0SignWeighting.lean),
which records `χ_{(2,1)}(w₀) = 0` as a *constant* imported from `S₃`
character theory.  Here the value is obtained by forming the concrete
seminormal matrices `ρ_{(2,1)}(σ₁)`, `ρ_{(2,1)}(σ₂)`, multiplying to
get `ρ_{(2,1)}(σ₁σ₂σ₁)`, and computing its trace.

## The `(2,1)` seminormal representation of `H₃(q)`

The irrep `(2,1) ⊢ 3` is `2`-dimensional, with basis the two standard
Young tableaux of shape `(2,1)`:

    t₁ = 1 2 / 3 ,   t₂ = 1 3 / 2 .

Contents `c = col − row`:  cell `(1,1)↦0`, `(1,2)↦1`, `(2,1)↦−1`.
The Hoefsmit seminormal form
([`mass-theory/hoefsmit-seminormal-form.md`](../../../mass-theory/hoefsmit-seminormal-form.md),
\[hoefsmit1974\], \[wenzl1988\]) sets, for a generator `σ_i` and tableau
`s` with axial distance `ρ = c(s,i+1) − c(s,i)`,

    ρ_λ(σ_i)_{s,s}  = a_ρ := (q − q⁻¹) / (1 − q^{−2ρ}),
    ρ_λ(σ_i)_{s,sᵢ} = b   := √(a_ρ · a_{−ρ} + 1)   (when sᵢ is standard),
    ρ_λ(σ_i)_{s,s'} = 0    otherwise.

* `σ₁` (swap entries `1,2`) is **diagonal** on `{t₁,t₂}`:
  on `t₁` the distance is `c(2)−c(1)=1−0=1`, on `t₂` it is
  `c(2)−c(1)=−1−0=−1`, and neither swap is standard.  Hence
  `ρ(σ₁) = diag(a₁, a₋₁)`.
* `σ₂` (swap entries `2,3`) mixes `t₁ ↔ t₂`:
  on `t₁` the distance is `c(3)−c(2)=−1−1=−2`, on `t₂` it is
  `c(3)−c(2)=1−(−1)=2`; the swap `t₁ ↔ t₂` **is** standard.  Hence
  `ρ(σ₂) = !![a₋₂, b; b, a₂]`.

The off-diagonal entry `b` is carried as a **free parameter** — it
never enters the trace of `ρ(σ₁)·ρ(σ₂)·ρ(σ₁)`, so the vanishing is
independent of the seminormal square root:

    tr(D · M · D) = a₁²·a₋₂ + a₋₁²·a₂ ,   D = diag(a₁,a₋₁), M = !![a₋₂,b;b,a₂].

With `s := q²`, `a₁²·a₋₂ = −s²/((s−1)³(s+1)) = −a₋₁²·a₂`, so the two
summands cancel exactly.

## α₃-break meaning

The `z^k` Markov marker (the `z`-graded piece detecting a full
`k`-fold Garside twist) breaks at `k = 3` structurally: the half-twist
`σ₁σ₂σ₁` is the `(2,1)`-blind element, so the `(2,1)` Wedderburn block
contributes **nothing** to any observable built from the `α₃` (three-
strand Garside) marker.  This is a *structural* prune of the α₃
channel, not a numerical near-cancellation.  See
[`computations/probes/probe_9b_alphak_structure.py`](../../../../../computations/probes/probe_9b_alphak_structure.py).

-- Ref: [hoefsmit1974] P.N. Hoefsmit, "Representations of Hecke algebras
     of finite groups with BN-pairs of classical type", PhD thesis, 1974.
-- Ref: [wenzl1988] https://doi.org/10.1007/BF01404457
-- Ref: [leitner2026] mass-theory/hoefsmit-seminormal-form.md (prop:hoefsmit-seminormal-form);
     probe computations/probes/probe_9b_alphak_structure.py
-/

namespace QOU.BraidKnot

open Matrix

variable {R : Type*} [Field R]

/-- The Hoefsmit seminormal diagonal entry `a_ρ = (q − q⁻¹)/(1 − q^{−2ρ})`
    for the small axial distances used by the `(2,1)` irrep of `H₃(q)`.
    Stated over a generic field per the base-ring convention (§7c); no
    archimedean structure is required — `q` is a formal parameter with
    the seminormal denominators kept nonzero by hypothesis. -/
noncomputable def a1 (q : R) : R := (q - q⁻¹) / (1 - q⁻¹ ^ 2)   -- ρ = 1
noncomputable def aNeg1 (q : R) : R := (q - q⁻¹) / (1 - q ^ 2)  -- ρ = −1
noncomputable def a2 (q : R) : R := (q - q⁻¹) / (1 - q⁻¹ ^ 4)   -- ρ = 2
noncomputable def aNeg2 (q : R) : R := (q - q⁻¹) / (1 - q ^ 4)  -- ρ = −2

/-- `ρ_{(2,1)}(σ₁)` — diagonal on the standard-tableau basis `{t₁,t₂}`. -/
noncomputable def rhoSigma1 (q : R) : Matrix (Fin 2) (Fin 2) R :=
  !![a1 q, 0; 0, aNeg1 q]

/-- `ρ_{(2,1)}(σ₂)` — the `t₁ ↔ t₂` mixing block; `b` is the
    (undetermined) seminormal off-diagonal entry. -/
noncomputable def rhoSigma2 (q b : R) : Matrix (Fin 2) (Fin 2) R :=
  !![aNeg2 q, b; b, a2 q]

/-- `ρ_{(2,1)}(σ₁σ₂σ₁)`, the seminormal representation of the Garside
    (half-twist) element `Δ = σ₁σ₂σ₁ ∈ B₃`, evaluated in the `(2,1)`
    block. -/
noncomputable def rhoGarside (q b : R) : Matrix (Fin 2) (Fin 2) R :=
  rhoSigma1 q * rhoSigma2 q b * rhoSigma1 q

/-- **α₃-break structural prune.**  The `(2,1)` Hecke character of the
    Garside half-twist `σ₁σ₂σ₁` vanishes, derived from the explicit
    `2 × 2` Hoefsmit seminormal matrices:

      `χ^{(2,1)}(σ₁σ₂σ₁) = tr ρ_{(2,1)}(σ₁σ₂σ₁) = a₁²·a₋₂ + a₋₁²·a₂ = 0`.

    Over any field, with `q ≠ 0`, `q² ≠ 1`, and `q⁴ ≠ 1` (the
    seminormal axial-distance denominators nonzero).  The off-diagonal
    seminormal entry `b` is arbitrary — it does not enter the trace. -/
-- Ref: [leitner2026] mass-theory/hoefsmit-seminormal-form.md; probe probe_9b_alphak_structure.py
theorem chi21_garside_zero (q b : R)
    (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (hq4 : q ^ 4 ≠ 1) :
    Matrix.trace (rhoGarside q b) = 0 := by
  -- Step 1: extract the trace of the concrete `D · M · D` product.  Only the
  -- diagonal entries `a₁², a₋₁²` and `a₋₂, a₂` survive; the off-diagonal `b`
  -- cancels out of the trace entirely.
  have htr : Matrix.trace (rhoGarside q b)
      = a1 q ^ 2 * aNeg2 q + aNeg1 q ^ 2 * a2 q := by
    simp [rhoGarside, rhoSigma1, rhoSigma2, Matrix.trace_fin_two]
    ring
  rw [htr, a1, aNeg1, a2, aNeg2]
  -- Step 2: the seminormal denominators are nonzero (field-generic; no order).
  have hq2' : q⁻¹ ^ 2 ≠ 1 := by rw [inv_pow]; exact fun h => hq2 (inv_eq_one.mp h)
  have hq4' : q⁻¹ ^ 4 ≠ 1 := by rw [inv_pow]; exact fun h => hq4 (inv_eq_one.mp h)
  have d1 : (1 : R) - q⁻¹ ^ 2 ≠ 0 := sub_ne_zero.mpr (Ne.symm hq2')
  have d2 : (1 : R) - q ^ 2 ≠ 0 := sub_ne_zero.mpr (Ne.symm hq2)
  have d3 : (1 : R) - q⁻¹ ^ 4 ≠ 0 := sub_ne_zero.mpr (Ne.symm hq4')
  have d4 : (1 : R) - q ^ 4 ≠ 0 := sub_ne_zero.mpr (Ne.symm hq4)
  -- variant denominator forms field_simp forms after clearing the `q⁻¹` powers
  have e2 : q ^ 2 - 1 ≠ 0 := sub_ne_zero.mpr hq2
  have e2' : (-1 : R) + q ^ 2 ≠ 0 := by
    rw [show (-1 : R) + q ^ 2 = q ^ 2 - 1 by ring]; exact e2
  have e4 : q ^ 4 - 1 ≠ 0 := sub_ne_zero.mpr hq4
  have e4' : (-1 : R) + q ^ 4 ≠ 0 := by
    rw [show (-1 : R) + q ^ 4 = q ^ 4 - 1 by ring]; exact e4
  -- Step 3: `a₁²·a₋₂ = −s²/((s−1)³(s+1)) = −a₋₁²·a₂` (`s = q²`) — exact cancel.
  field_simp
  ring

end QOU.BraidKnot
