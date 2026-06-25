import Mathlib.Tactic
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic

/-!
# Lever-1 kernel trace τ — quantum-integer (bar-even) form + SL₂ transfer structure

The lever-1 binding kernel trace has the proved closed form (`Lever1Tau.tau_kernel_closed_form`,
PRs #2767/#2755)

    τ(q) = 3(3q⁴ + 8q² + 3) / (4q(q+1)²).

This file records three structural facts that sharpen what kind of operator the prolongation
`M` (`a_D^(n+2) = τ a_D^(n+1) − a_D^(n)`) is — the z2bn third probe (PF-monodromy synthesis):

1. `tau_quantum_integer_form` — **τ is a rational function of the quantum integer `[2]_q = q+q⁻¹`
   alone:** `τ = 3(3[2]² + 2) / (4([2]+2))`. This is the Hecke/q-difference fingerprint: a classical
   `d/dz` jet trace would be a function of `q` with no reason to collapse onto `[2]_q`.
2. `tau_bar_even` — consequently **τ(q⁻¹) = τ(q)** (bar-even, invariant under `q ↔ q⁻¹`), as a
   Markov-trace / quantum-dimension object must be.
3. `transfer_det_one` — the depth-2 transfer matrix `!![τ,-1;1,0]` has **det = 1**, so `M ∈ SL₂`:
   its eigenvalues multiply to 1 and sum to τ. With `τ > 2` (`Lever1Tau.tauAnchor_gt_two`) the
   element is **hyperbolic** (`λ₊ > 1`, the seed kernel's extensivity — the physical `lw` grows
   super-geometrically *past* `λ₊`, #2752) — distinguishing it from the topological
   Picard–Fuchs monodromy, which is `SL₂(ℤ)` (integer trace, parabolic `trace = 2` at the `I₁` nodal
   fibres of the squarefree-Δ color curve). Since `τ ∉ ℤ` (even `τ(1)=21/8`), `M` is **not** the
   arithmetic monodromy — it is a real / q-difference `SL₂(ℝ)` operator.

See `computations/substrate/z2bn_pf_monodromy_synthesis.py` and the audit
`docs/audits/2026-06-25-z2bn-pf-monodromy-synthesis.md`. Statements are over `ℝ` (the trace is an
archimedean object evaluated at the substrate `q₀`); `det` lemma is trace-agnostic.
-/

namespace QOU.Mass.TauQuantumInteger

/-- **τ is a rational function of the quantum integer `[2]_q = q + q⁻¹` alone:**
`τ(q) = 3(3[2]² + 2)/(4([2]+2))`. The proved closed form `3(3q⁴+8q²+3)/(4q(q+1)²)` collapses onto
`[2]_q` — the Hecke / q-difference fingerprint. -/
theorem tau_quantum_integer_form (q : ℝ) (hq : 0 < q) :
    3 * (3 * q ^ 4 + 8 * q ^ 2 + 3) / (4 * q * (q + 1) ^ 2)
      = 3 * (3 * (q + q⁻¹) ^ 2 + 2) / (4 * ((q + q⁻¹) + 2)) := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hq1 : q + 1 ≠ 0 := by positivity
  have hb : (q + q⁻¹) + 2 ≠ 0 := by positivity
  field_simp
  ring

/-- **τ is bar-even: `τ(q⁻¹) = τ(q)`** (invariant under `q ↔ q⁻¹`), as a Markov-trace /
quantum-dimension object must be. Immediate from the `[2]_q` form (`[2]_{q⁻¹} = [2]_q`). -/
theorem tau_bar_even (q : ℝ) (hq : 0 < q) :
    3 * (3 * (q⁻¹) ^ 4 + 8 * (q⁻¹) ^ 2 + 3) / (4 * (q⁻¹) * ((q⁻¹) + 1) ^ 2)
      = 3 * (3 * q ^ 4 + 8 * q ^ 2 + 3) / (4 * q * (q + 1) ^ 2) := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hqi : q⁻¹ ≠ 0 := inv_ne_zero hq0
  have hq1 : q + 1 ≠ 0 := by positivity
  have hqi1 : q⁻¹ + 1 ≠ 0 := by positivity
  field_simp
  ring

/-- **The depth-2 transfer matrix `!![τ,-1;1,0]` has `det = 1`** — so the prolongation operator
`M` lies in `SL₂`: its eigenvalues multiply to 1 and sum to its trace `τ`. Trace-agnostic (holds
for any `t`), establishing the `SL₂` structure independent of the trace value. -/
theorem transfer_det_one (t : ℝ) : Matrix.det !![t, -1; 1, 0] = 1 := by
  rw [Matrix.det_fin_two_of]; ring

end QOU.Mass.TauQuantumInteger
