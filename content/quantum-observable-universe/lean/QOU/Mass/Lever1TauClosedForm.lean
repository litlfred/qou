import Mathlib.Tactic

/-!
# Lever-1 binding kernel — closed form for the depth-2 trace `τ = tr B`

The lever-1 binding kernel is the depth-2, `det = 1` recurrence `R = x² − τx + 1`, so the entire
kernel reduces to the single trace `τ = tr B`, fixed by the three production-wired prolonged
Seiberg–Witten period anchors (`lever1_lambda_sw_no_shortcut.py`):

* `a_D^(2) = 1` (muon, c = 1),
* `a_D^(3) = (q+1)²/(3q)` (c = 2 selection rule),
* `a_D^(4) = (3q² + 4 + 3q⁻²)/4` (Family-A, the production proton multiplier `linking_weight_family_a`),

via the seed identity `τ = (a_D^(2) + a_D^(4)) / a_D^(3)` (`sl2-prolongation-recurrence.md`). This file
proves the **exact closed form** of that trace:

    τ(q) = 3(3q⁴ + 8q² + 3) / (4q(q+1)²).

At the substrate `q₀ ≈ 1.10998` this evaluates to `τ ≈ 2.64239` (`θ_binding = acosh(τ/2) ≈ 0.78145`),
the hyperbolic `SL₂(ℝ)` rapidity of the abelianised `λ_SW` connection — see the first geometric
probe `computations/substrate/z2bn_tau_derivation_probe.py` (which cross-checks this closed form to
50 dps and confirms the coral curve `E_q` via `j(q₀) = 129.86`).

**Scope.** This formalizes the *algebraic* reduction of the kernel trace to a closed form in `q` from
the three anchors — an exact, substrate-independent rational identity (pure field algebra; `q₀`
never used). It is **not** the geometric derivation of `τ` as the `λ_SW` Gauss–Manin holonomy (the
owner-gated keystone residual): the first probe found that no bare-period quantity of `E_q`
reproduces `τ = 2.6424` (the prolongation operator `λ_SW^(n) → a_D^(n)` is non-trivial — the anchors
are not the curve's bare power sums), so that step stays open. Base ring `ℝ` (the analytic/archimedean
realisation, matching the coral-curve and `BindingRecurrenceSpectral` files).
Ref: [manuscript] content/.../mass-theory/sl2-prolongation-recurrence.md
-/

namespace QOU.Mass.Lever1Tau

/-- **Closed form for the depth-2 binding-kernel trace.** Given the three production-wired anchors
`a_D^(2)=1`, `a_D^(3)=(q+1)²/(3q)`, `a_D^(4)=(3q²+4+3q⁻²)/4`, the seed trace
`τ = (a_D^(2)+a_D^(4))/a_D^(3)` equals the cubic-over-quadratic rational `3(3q⁴+8q²+3)/(4q(q+1)²)`.
Exact field identity for `q ≠ 0`, `q + 1 ≠ 0`. -/
theorem tau_kernel_closed_form (q : ℝ) (hq : q ≠ 0) (hq1 : q + 1 ≠ 0) :
    (1 + (3 * q ^ 2 + 4 + 3 / q ^ 2) / 4) / ((q + 1) ^ 2 / (3 * q))
      = 3 * (3 * q ^ 4 + 8 * q ^ 2 + 3) / (4 * q * (q + 1) ^ 2) := by
  have hq2 : q ^ 2 ≠ 0 := pow_ne_zero 2 hq
  have hq12 : (q + 1) ^ 2 ≠ 0 := pow_ne_zero 2 hq1
  field_simp
  ring

end QOU.Mass.Lever1Tau
