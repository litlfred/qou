import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.SpecialFunctions.Complex.Circle
import Mathlib.MeasureTheory.Integral.Bochner.Basic
import Mathlib.MeasureTheory.Measure.Lebesgue.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# Faddeev `Φ_b` on the fibre saddle — genuine real-integral construction

The **construction** item of the Φ_b program (PR #3544 work item 2): on the fibre
saddle (real `b`, real `z`) the Faddeev contour integral collapses to a real
single integral, numerically pinned to `8e-29` against the validated contour
evaluator (`computations/qbeta/qbeta_phi_b_real_form_pin.py`, P1–P4 gates):

  `log Φ_b(z) = i·(−J/2 + πz²/2 + π(b² + b⁻²)/24)`,
  `J(b, z) = ∫₀^∞ [ sin(2zt) / (t·sinh(bt)·sinh(t/b)) − 2z/t² ] dt`.

Unlike `QOU.MathlibExt.FaddeevQuantumDilogarithm` (which *axiomatizes* `Φ_b` as a
conjecture-class because the contour integral is out of Mathlib's reach), this
file gives a **genuine `noncomputable def`** — `phiB` is Mathlib's Bochner
integral, no axiom, no class — and proves its structural laws **sorry-free**:

* `phiB_self_dual` — `Φ_{b⁻¹} = Φ_b` (the modular-double self-duality), from the
  manifest `b ↔ b⁻¹` symmetry of the kernel.
* `norm_phiB` — unitarity `‖Φ_b(z)‖ = 1` (the phase is real).
* `phiB_inversion` — `Φ_b(z)·Φ_b(−z) = exp(i·(πz² + π(b²+b⁻²)/12))` (the
  inversion relation: `J` is odd in `z`, so it cancels).
* `phiB_zero` — `Φ_b(0) = exp(i·π(b²+b⁻²)/24)` (`J(b,0) = 0`).

**Honest scope.** These laws hold for the *defined* object unconditionally
(Mathlib's integral is total; the symmetry/oddness proofs are pointwise kernel
identities plus `integral` congruence, needing no integrability hypotheses). What
is *not* proved here — and is the remaining analytic content — is integrability
of the kernel and the identification of `phiB` with the contour-integral Φ_b
(that identification is the `8e-29` numerical pin, P1–P4). No `c_k` value is
produced or wired; the argument-identification probe is a separate item.

-- Ref: [faddeev1995] Faddeev, Lett. Math. Phys. 34 (1995) 249.
--        https://doi.org/10.1007/BF01872779
-- Ref: [manuscript] PR #3544 real-form pin; docs/audits/2026-07-11-qbeta-c3-barodd-sleak-phib-target.md
-/

namespace QOU.MathlibExt.FaddeevPhiBRealIntegral

open Real MeasureTheory

/-- The real Faddeev kernel `sin(2zt)/(t·sinh(bt)·sinh(t/b)) − 2z/t²` (the
    `−2z/t²` subtraction cancels the `t→0` pole; totality of division makes the
    definition unconditional). -/
noncomputable def kernel (b z t : ℝ) : ℝ :=
  Real.sin (2 * z * t) / (t * Real.sinh (b * t) * Real.sinh (t / b)) - 2 * z / t ^ 2

/-- `J(b,z) = ∫₀^∞ kernel` — the real Faddeev phase integral. -/
noncomputable def J (b z : ℝ) : ℝ := ∫ t in Set.Ioi (0 : ℝ), kernel b z t

/-- The real Faddeev phase `−J/2 + πz²/2 + π(b²+b⁻²)/24`. -/
noncomputable def phase (b z : ℝ) : ℝ :=
  -(J b z) / 2 + π * z ^ 2 / 2 + π * (b ^ 2 + b⁻¹ ^ 2) / 24

/-- The Faddeev `Φ_b` on the fibre saddle: a **defined** object (no axiom). -/
noncomputable def phiB (b z : ℝ) : ℂ :=
  Complex.exp ((phase b z : ℂ) * Complex.I)

/-- The kernel is manifestly self-dual under `b ↔ b⁻¹` (the two `sinh` factors
    swap; the identities used are total, so `b = 0` needs no case split). -/
theorem kernel_self_dual (b z t : ℝ) : kernel b⁻¹ z t = kernel b z t := by
  unfold kernel
  rw [inv_mul_eq_div, show t / b⁻¹ = t * b by rw [div_eq_mul_inv, inv_inv],
    mul_comm t b]
  ring_nf

/-- `J` is self-dual: `J(b⁻¹, z) = J(b, z)`. -/
theorem J_self_dual (b z : ℝ) : J b⁻¹ z = J b z := by
  unfold J
  congr 1
  funext t
  exact kernel_self_dual b z t

/-- The phase is self-dual: kernel symmetry plus `(b⁻¹)⁻¹ = b`. -/
theorem phase_self_dual (b z : ℝ) : phase b⁻¹ z = phase b z := by
  unfold phase
  rw [J_self_dual, inv_inv]
  ring

/-- **Modular-double self-duality** `Φ_{b⁻¹} = Φ_b` — sorry-free. -/
theorem phiB_self_dual (b z : ℝ) : phiB b⁻¹ z = phiB b z := by
  unfold phiB
  rw [phase_self_dual]

/-- The kernel is odd in `z`. -/
theorem kernel_odd (b z t : ℝ) : kernel b (-z) t = -kernel b z t := by
  unfold kernel
  rw [show 2 * -z * t = -(2 * z * t) by ring, Real.sin_neg]
  ring

/-- `J` is odd in `z` (no integrability needed: `∫ −f = −∫ f` is unconditional). -/
theorem J_odd (b z : ℝ) : J b (-z) = -J b z := by
  unfold J
  rw [show (fun t => kernel b (-z) t) = fun t => -kernel b z t from
    funext fun t => kernel_odd b z t]
  exact integral_neg _

/-- `J(b, 0) = 0` (the integrand vanishes identically at `z = 0`). -/
theorem J_zero (b : ℝ) : J b 0 = 0 := by
  unfold J
  have h : (fun t => kernel b 0 t) = fun _ => (0 : ℝ) := by
    funext t; unfold kernel; simp
  rw [h]
  exact integral_zero _ _

/-- **Unitarity** `‖Φ_b(z)‖ = 1` — the phase is real. -/
theorem norm_phiB (b z : ℝ) : ‖phiB b z‖ = 1 := by
  unfold phiB
  simp [Complex.norm_exp]

/-- **Inversion relation** `Φ_b(z)·Φ_b(−z) = exp(i(πz² + π(b²+b⁻²)/12))` —
    the odd `J` cancels between the two factors. -/
theorem phiB_inversion (b z : ℝ) :
    phiB b z * phiB b (-z)
      = Complex.exp (Complex.ofReal (π * z ^ 2 + π * (b ^ 2 + b⁻¹ ^ 2) / 12)
          * Complex.I) := by
  unfold phiB phase
  rw [← Complex.exp_add, J_odd]
  congr 1
  push_cast
  ring

/-- **Zero-argument value** `Φ_b(0) = exp(i·π(b²+b⁻²)/24)`. -/
theorem phiB_zero (b : ℝ) :
    phiB b 0 = Complex.exp (Complex.ofReal (π * (b ^ 2 + b⁻¹ ^ 2) / 24)
      * Complex.I) := by
  unfold phiB phase
  rw [J_zero]
  congr 1
  push_cast
  ring

end QOU.MathlibExt.FaddeevPhiBRealIntegral
