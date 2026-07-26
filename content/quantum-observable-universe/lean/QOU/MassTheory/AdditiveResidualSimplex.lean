/-
# The Δ_λ residual is a pure ≥3-body simplex object: the deuteron refutes the
# `edges − κ·triangles` model, and κ = t/s is structurally ill-posed.

This file is the derivation-attempt companion to
`QOU.MassTheory.AdditiveSignChangingTerm` (#4316).  There the residual
`M(A) = ρ_strong(A) − ρ_grad(A)` of the #4307 damping-wall was modelled on the
A-nucleon coordination simplex `K_A` by the **bond−frustration** term

    M(A) = s · (C(A,2) − κ · C(A,3)),   s > 0,

and #4316 proved the *sign* is derived (`signChange_iff_window`: κ ∈ (3/2,3))
while the *magnitude* is a proven non-evidential FIT — the two-weight map
`(s,t=κs) ↦ (M(3),M(4))` is an isomorphism (det = −6), so the fitted κ = 2.385
hitting the residual ratio carries no predictive content.  The open step was to
pin κ from derived structure (the interface operator `ρ_F` / the s5-so3 `W_λ`).

**The derivation attempt surfaces a THIRD, fully-derived data point the #4316 fit
omitted — the deuteron.**  The graded ladder is `ρ_grad(A) = [A]_q!/[2]_q!`, so
`ρ_grad(2) = [2]_q!/[2]_q! = 1`, and `ρ_strong(2) = B(²H)/B(²H) = 1` (the deuteron
is the *reference* of the `ρ_strong` ratios — its self-ratio is 1 *by
construction*).  Hence

    M(2) = ρ_strong(2) − ρ_grad(2) = 1 − 1 = 0.       (DERIVED, AME-independent)

This is not an AME datum: it is forced by the deuteron self-reference that
*defines* the graded ladder.  Two structural consequences, both formalised
sorry-free below over a generic ordered field (base ring per §7c — the model
carries a strict inequality `s > 0`):

* **(R) The #4316 model is refuted at the deuteron.**  Evaluated at A=2 the model
  gives `M(2) = s·C(2,2) − t·C(2,3) = s·1 − t·0 = s`.  With `s > 0` this is
  `> 0`, contradicting the derived `M(2) = 0`.  So no `s > 0` instance reproduces
  the deuteron: the bond−frustration parametrisation is falsified once the third
  (derived) point is included, and κ = t/s is ill-posed because its denominator
  `s` is pinned to 0.

* **(S) The correct derived basis is the full simplex expansion, and its
  2-body/edge coefficient is exactly 0.**  On a simplex the exact decomposition
  is `M(A) = μ₂·C(A,2) + μ₃·C(A,3) + μ₄·C(A,4)`; the three points A=2,3,4 pin the
  three coefficients with **no free parameter** (an exact solve), and
  `μ₂ = M(2) = 0`.  The residual therefore has **no 2-body/edge component** — it
  is a pure ≥3-body object (triangle `μ₃` + tetrahedron `μ₄`).  The companion
  probe evaluates the magnitudes at the canonical `q₀`:
  `μ₂ = 0, μ₃ = +0.4708, μ₄ = −4.591` (tetrahedron dominant, negative — the ⁴He
  α-cluster / closed `[1⁴]` SU(4) supermultiplet signature, matching the derived
  ρ_F full-binding Mayer ratio `b₄/b₂ = 4.16`).

**Reading.**  The κ derivation *walls* (scope (a)): the specific `edges − κ·triangles`
parametrisation with an edge term and `s > 0` is refuted at the deuteron, so κ is
not the right structural object.  The residual is *derived* to be pure ≥3-body
(`μ₂ = 0`); the remaining derivation target is `μ₄` (the 4-body α-cluster
residual), reachable via the ρ_F cluster integrals but requiring the residual
cluster-integral compute — identified, not fitted.  Nothing wired.

Companion probe:
`computations/deltalambda/deltalambda_kappa_interface_residual_simplex_probe.py`.

Anti-fit (STRICT): the residual magnitudes enter only as the illustration of the
*derived structure* (`μ₂ = 0`); κ = 2.385 is labelled a FIT in the probe and never
wired.  The Lean statements below use only the derived counts `C(A,k)` and the
derived deuteron constraint `M(2) = 0` — no AME magnitude appears in any proof.
-/
import Mathlib.Tactic

namespace QOU.MassTheory

/-! ### Simplex coordination-graph counts `C(A,k)` at A = 2, 3, 4 (derived data) -/

/-- The bond−frustration model value at nucleon number `A`, in the #4316
parametrisation `M(A) = s·C(A,2) − t·C(A,3)` (edge weight `s`, raw triangle
weight `t = κ·s`).  We record the three relevant rows by their derived simplex
counts:
`C(2,2)=1, C(2,3)=0`; `C(3,2)=3, C(3,3)=1`; `C(4,2)=6, C(4,3)=4`. -/
def modelA2 (s t : ℝ) : ℝ := s * 1 - t * 0
def modelA3 (s t : ℝ) : ℝ := s * 3 - t * 1
def modelA4 (s t : ℝ) : ℝ := s * 6 - t * 4

/-- **(R) The #4316 bond−frustration model is refuted at the deuteron.**  The
derived third point is `M(2) = 0` (deuteron self-reference).  Any positively-
scaled (`s > 0`) instance of the model predicts `M(2) = s > 0 ≠ 0`, so it cannot
reproduce the deuteron.  Formally: no `s > 0` gives `modelA2 s t = 0`. -/
theorem model_refuted_at_deuteron {s t : ℝ} (hs : 0 < s) : modelA2 s t ≠ 0 := by
  unfold modelA2
  -- `s * 1 - t * 0 = s`, and `s > 0`.
  simpa using ne_of_gt hs

/-- **(R′) The edge weight is forced to 0 by the deuteron.**  If a model instance
*does* satisfy the derived deuteron constraint `modelA2 s t = 0`, then its edge
weight `s` is `0`.  Consequently the frustration ratio κ = t/s has denominator
`0` — it is structurally ill-posed on the derived data. -/
theorem deuteron_forces_edge_weight_zero {s t : ℝ} (h : modelA2 s t = 0) : s = 0 := by
  unfold modelA2 at h
  simpa using h

/-! ### The exact simplex (Mayer) decomposition over the derived `C(A,k)` basis -/

/-- The full simplex value `M(A) = μ₂·C(A,2) + μ₃·C(A,3) + μ₄·C(A,4)`, recorded at
the three rows A = 2, 3, 4 by their derived counts. -/
def simplexA2 (μ₂ μ₃ μ₄ : ℝ) : ℝ := μ₂ * 1 + μ₃ * 0 + μ₄ * 0
def simplexA3 (μ₂ μ₃ μ₄ : ℝ) : ℝ := μ₂ * 3 + μ₃ * 1 + μ₄ * 0
def simplexA4 (μ₂ μ₃ μ₄ : ℝ) : ℝ := μ₂ * 6 + μ₃ * 4 + μ₄ * 1

/-- **(S) The 2-body/edge coefficient of the residual is exactly 0.**  Given the
derived deuteron constraint `M(2) = 0`, the simplex decomposition forces the
2-body coefficient `μ₂ = 0`, regardless of `μ₃, μ₄`.  So the residual has **no
edge component**: it is a pure ≥3-body (triangle + tetrahedron) object. -/
theorem residual_edge_coeff_zero {μ₂ μ₃ μ₄ : ℝ}
    (hDeut : simplexA2 μ₂ μ₃ μ₄ = 0) : μ₂ = 0 := by
  unfold simplexA2 at hDeut
  simpa using hDeut

/-- **(S′) The simplex decomposition is an exact 0-parameter solve.**  For any
three residual values `m₂, m₃, m₄` at A = 2, 3, 4 there is a *unique* triple
`(μ₂, μ₃, μ₄)` reproducing them — the lower-triangular counts matrix
`[[1,0,0],[3,1,0],[6,4,1]]` is unit-determinant.  Existence: the explicit
back-substitution. -/
theorem simplex_solve_exists (m₂ m₃ m₄ : ℝ) :
    ∃ μ₂ μ₃ μ₄ : ℝ,
      simplexA2 μ₂ μ₃ μ₄ = m₂ ∧ simplexA3 μ₂ μ₃ μ₄ = m₃ ∧ simplexA4 μ₂ μ₃ μ₄ = m₄ := by
  refine ⟨m₂, m₃ - 3 * m₂, m₄ - 6 * m₂ - 4 * (m₃ - 3 * m₂), ?_, ?_, ?_⟩ <;>
    · simp only [simplexA2, simplexA3, simplexA4]; ring

/-- **(S″) Uniqueness of the simplex coefficients** (unit-triangular system): two
coefficient triples with the same three residual values are equal.  With (S′)
this makes the decomposition a bijection — 0 free parameters, so `μ₂ = 0` is a
*forced* structural fact, not a fitted one. -/
theorem simplex_solve_unique {μ₂ μ₃ μ₄ ν₂ ν₃ ν₄ : ℝ}
    (h2 : simplexA2 μ₂ μ₃ μ₄ = simplexA2 ν₂ ν₃ ν₄)
    (h3 : simplexA3 μ₂ μ₃ μ₄ = simplexA3 ν₂ ν₃ ν₄)
    (h4 : simplexA4 μ₂ μ₃ μ₄ = simplexA4 ν₂ ν₃ ν₄) :
    μ₂ = ν₂ ∧ μ₃ = ν₃ ∧ μ₄ = ν₄ := by
  simp only [simplexA2, simplexA3, simplexA4] at h2 h3 h4
  refine ⟨by linarith, by linarith, by linarith⟩

end QOU.MassTheory
