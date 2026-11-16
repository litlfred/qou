import Mathlib.Tactic
import Mathlib.Algebra.BigOperators.Group.Finset.Defs
import Mathlib.Data.Real.Basic
import Mathlib.Data.Fintype.Fin

/-!
# QOU.Shared.OperatorSelectionLP — shared context for LP-dual claims

An *LP-selection claim* is any proposition that bundles:
- A target `n_target ∈ ℝ_{>0}`
- A `d`-dimensional NF basis with Markov-trace coefficients `t_i`
- A `d × d` Frobenius Gram matrix `G_{ij}`
- The LP primal optimum `x* : Fin d → ℝ`
- The LP dual optima `(y_0*, y* : Fin d → ℝ)`

Per `local/lean-substantive-pass`, ~10 blocks share this shape
(operator-selection / confinement / shadow-price / strong-duality
content).  This typeclass extracts the shared structure so per-block
claims only need to specify which LP-property they encode (primal
feasibility / strong duality / active-set characterisation / etc.).

**Usage**:

```lean
class MyLPClaim extends QOU.Shared.OperatorSelectionLPContext where
  -- block-specific assertion
  claim_active_set_size :
    (Finset.filter (fun i => 0 < y_star i) Finset.univ).card = 3
```

-- Ref: [leitner2026] particle-interactions/operator-selection-lp.md (shared)
-/

namespace QOU.Shared

/-- Shared context for any block whose claim involves the
    operator-selection LP and its dual certificate. -/
class OperatorSelectionLPContext where
  /-- Strand number `n ≥ 2`. -/
  n : ℕ
  /-- Basis dimension `d` (usually `n!`). -/
  d : ℕ
  /-- The target net value `n_target ∈ ℝ_{>0}`. -/
  n_target : ℝ
  /-- The Markov-trace coefficient vector `t : Fin d → ℝ`. -/
  t : Fin d → ℝ
  /-- The Frobenius Gram matrix `G : Fin d → Fin d → ℝ`. -/
  G : Fin d → Fin d → ℝ
  /-- The primal optimum `x* : Fin d → ℝ`. -/
  x_star : Fin d → ℝ
  /-- The Markov-trace dual variable `y_0* : ℝ`. -/
  y_0_star : ℝ
  /-- The Frobenius-positivity dual variables `y* : Fin d → ℝ`. -/
  y_star : Fin d → ℝ
  /-- LP-active set: the indices `i` with strictly positive dual
      variable, `A* = {i : y*_i > 0}`. -/
  A_star : Finset (Fin d)
  /-- Strong-duality identity: `Σ t_i · x*_i = n_target · y_0*`.
      (Needs abstract LP duality infrastructure that does not exist in Mathlib; kept as an honest assumption for models without certificates) -/
  strong_duality :
    (Finset.univ.sum fun i : Fin d => t i * x_star i)
      = n_target * y_0_star

/-! ## Dual certificate existence and strong-duality reduction (`qou-k4f8`)

Formalizes the dual certificate predicate `DualCertificateExists t G` for the operator-selection LP
and proves the two structural reductions from `qou-k4f8`:
1. If `s` solves the linear system `G s = t - y₀ 𝟙` with `s ≥ 0` (in particular `s = G⁻¹(t - y₀ 𝟙)`
   when `G` is invertible), it exhibits `DualCertificateExists t G`.
2. Any dual certificate `(y₀, s)` together with primal normalization `∑ j, x*_j = n_target` and
   aggregated complementary slackness `∑ j, (∑ i, s_i G_{ij}) x*_j = 0` discharges the
   `strong_duality` identity `∑ j, t_j x*_j = n_target · y₀`.
-/

/-- Existence of a non-negative dual certificate `(y₀, s)` satisfying `t_j = y₀ + ∑_i s_i G_{ij}`. -/
def DualCertificateExists {d : ℕ} (t : Fin d → ℝ) (G : Fin d → Fin d → ℝ) : Prop :=
  ∃ (y0 : ℝ) (s : Fin d → ℝ),
    (∀ i : Fin d, 0 ≤ s i) ∧
    (∀ j : Fin d, t j = y0 + (Finset.univ.sum fun i : Fin d => s i * G i j))

/-- Candidate dual multiplier vector `s_i = ∑_j G_inv_{ij} (t_j - y₀)` obtained from an inverse
Gram matrix `G_inv`. -/
def dualMultiplierOfInverse {d : ℕ} (G_inv : Fin d → Fin d → ℝ) (t : Fin d → ℝ)
    (y0 : ℝ) (i : Fin d) : ℝ :=
  Finset.univ.sum fun j : Fin d => G_inv i j * (t j - y0)

/-- **Reduction 1 (`qou-k4f8`):** If `G_inv` reconstructs `t - y₀ 𝟙` against `G` and the resulting
one-parameter vector `dualMultiplierOfInverse G_inv t y0` is entrywise non-negative, then
`DualCertificateExists t G` holds. -/
theorem dualCertificateExists_of_inverse_cone {d : ℕ} (t : Fin d → ℝ)
    (G G_inv : Fin d → Fin d → ℝ) (y0 : ℝ)
    (hnonneg : ∀ i : Fin d, 0 ≤ dualMultiplierOfInverse G_inv t y0 i)
    (hrec : ∀ j : Fin d,
      (Finset.univ.sum fun i : Fin d => dualMultiplierOfInverse G_inv t y0 i * G i j) = t j - y0) :
    DualCertificateExists t G := by
  refine ⟨y0, dualMultiplierOfInverse G_inv t y0, hnonneg, fun j => ?_⟩
  linarith [hrec j]

/-- **Reduction 2 (`qou-k4f8`):** A dual certificate `(y₀, s)` for `(t, G)`, paired with primal
normalization `∑_j x*_j = n_target` and aggregated complementary slackness
`∑_j (∑_i s_i G_{ij}) x*_j = 0`, proves the LP strong-duality identity
`∑_j t_j x*_j = n_target · y₀`. -/
theorem strong_duality_of_dualCertificate {d : ℕ} (t x_star : Fin d → ℝ)
    (G : Fin d → Fin d → ℝ) (n_target y0 : ℝ) (s : Fin d → ℝ)
    (hdual : ∀ j : Fin d, t j = y0 + (Finset.univ.sum fun i : Fin d => s i * G i j))
    (hnorm : (Finset.univ.sum fun j : Fin d => x_star j) = n_target)
    (hslack : (Finset.univ.sum fun j : Fin d =>
      (Finset.univ.sum fun i : Fin d => s i * G i j) * x_star j) = 0) :
    (Finset.univ.sum fun j : Fin d => t j * x_star j) = n_target * y0 := by
  have h1 : (Finset.univ.sum fun j : Fin d => t j * x_star j) =
      (Finset.univ.sum fun j : Fin d => y0 * x_star j) +
      (Finset.univ.sum fun j : Fin d =>
        (Finset.univ.sum fun i : Fin d => s i * G i j) * x_star j) := by
    rw [← Finset.sum_add_distrib]
    refine Finset.sum_congr rfl fun j _ => ?_
    rw [hdual j]
    ring
  have h2 : (Finset.univ.sum fun j : Fin d => y0 * x_star j) =
      y0 * (Finset.univ.sum fun j : Fin d => x_star j) := by
    rw [← Finset.mul_sum]
  rw [h1, h2, hnorm, hslack]
  ring

end QOU.Shared

