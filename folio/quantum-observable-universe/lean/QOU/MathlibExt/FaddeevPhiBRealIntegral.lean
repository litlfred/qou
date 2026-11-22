import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.SpecialFunctions.Complex.Circle
import Mathlib.MeasureTheory.Integral.Bochner.Basic
import Mathlib.MeasureTheory.Measure.Lebesgue.Basic
import Mathlib.MeasureTheory.Integral.ExpDecay
import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals
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
is *not* proved here — and is the remaining analytic content — is the
identification of `phiB` with the contour-integral Φ_b (the `8e-29` numerical
pin, P1–P4); kernel integrability IS proved (near-`0` outright, the tail
modulo two standard majorant facts — see the integrability sections). No `c_k`
value is produced or wired; the argument-identification is a separate item.

-- Ref: [faddeev1995] Faddeev, Lett. Math. Phys. 34 (1995) 249.
--        https://doi.org/10.1007/BF01872779
-- Ref: [leitner2026] PR #3544 real-form pin; docs/audits/2026-07-11-qbeta-c3-barodd-sleak-phib-target.md
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

/-! ## The fibre branch is the `|q| = 1` regime, and `Φ_b` is σ-unitary there

At real `b` the modular parameter `q_b = e^{iπb²}` sits ON the unit circle —
the fibre / root-of-unity regime where the modular-double product diverges
(`QOU.MathlibExt.PhiBProd` covers only `Im b² > 0`, where `|q_b| < 1`) and the
real integral above is the construction.  The defined `phiB` is a genuine
phase there: `Φ_b · conj(Φ_b) = 1`.  This is the archimedean instance of the
σ-unitarity hypothesis of `prop:phi-b-unitary-bar-odd` (σ = complex
conjugation): by that proposition's rigidity clause, any such phase with
`Φ² ≠ 1` carries a nontrivial bar-odd part — the fibre-branch `Φ_b` is an
intrinsically **bar-odd** carrier. -/

/-- The fibre modular parameter `q_b = e^{iπb²}` at real `b`. -/
noncomputable def fibreQParam (b : ℝ) : ℂ :=
  Complex.exp (Complex.ofReal (π * b ^ 2) * Complex.I)

/-- **`|q_b| = 1` at every real `b`** — the fibre branch is exactly the
`|q| = 1` regime (contrast `Im b² > 0`, where `|q_b| < 1` and the
modular-double product converges). -/
theorem norm_fibreQParam (b : ℝ) : ‖fibreQParam b‖ = 1 := by
  unfold fibreQParam
  rw [Complex.norm_exp, Complex.mul_I_re, Complex.ofReal_im]
  simp

/-- **σ-unitarity** `Φ_b(z) · conj(Φ_b(z)) = 1` — the ring-involution form of
`|Φ_b| = 1`, instantiating the σ-unitarity hypothesis of
`prop:phi-b-unitary-bar-odd` at σ = complex conjugation. -/
theorem phiB_mul_conj (b z : ℝ) :
    phiB b z * (starRingEnd ℂ) (phiB b z) = 1 := by
  unfold phiB
  rw [← Complex.exp_conj, ← Complex.exp_add]
  have h : (phase b z : ℂ) * Complex.I
      + (starRingEnd ℂ) ((phase b z : ℂ) * Complex.I) = 0 := by
    rw [map_mul, Complex.conj_ofReal, Complex.conj_I]
    ring
  rw [h, Complex.exp_zero]

/-! ## Integrability: the exponential-tail domination is a THEOREM

`sin` is bounded, the double-`sinh` denominator grows like `e^{(b+1/b)t}`, and
the subtracted `2z/t²` is a `t^{-2}` tail — so the kernel is dominated on
`[1, ∞)` by `C·e^{−bt} + 2|z|·t^{−2}`, and integrable there.  All the
kernel-specific analysis (the `sinh` lower bound, the domination chain,
continuity/measurability) is proved sorry-free below.

**Fully unconditional (2026-07-14).**  The two *majorant* integrability facts
— `e^{−bt}` and `t^{−2}` are integrable on `[1, ∞)` — are the standard Mathlib
theorems `exp_neg_integrableOn_Ioi` and `integrableOn_Ioi_rpow_of_lt`, proved
here as the private lemmas `majorant_exp` / `majorant_inv`.  (Their modules
`Mathlib.MeasureTheory.Integral.ExpDecay` +
`Mathlib.Analysis.SpecialFunctions.ImproperIntegrals` were built into the
sandbox olean cone; an earlier revision carried them as explicit `hexp`/`hinv`
hypotheses per the `PhiBProd` precedent — now discharged.)  So the tail
(`integrableOn_kernel_Ioi_one`), the near-`0` piece
(`integrableOn_kernel_Ioc_zero_one` — the `−2z/t²` subtraction cancels the
pole), and hence the full `(0, ∞)` integrability (`integrableOn_kernel_Ioi_zero`)
are all **hypothesis-free theorems**.  The def↔contour identification of `phiB`
with the Faddeev contour integral remains the `8e-29` numerical pin (module
docstring) — it is NOT assumed anywhere in this file. -/

/-- `sinh` is positive on positives (local; the Mathlib lemma lives in the
`Trigonometric.Deriv` cone, outside the sandbox oleans). -/
private lemma sinh_pos_of_pos {x : ℝ} (hx : 0 < x) : 0 < Real.sinh x := by
  rw [Real.sinh_eq]
  have h : Real.exp (-x) < Real.exp x := Real.exp_lt_exp.mpr (by linarith)
  linarith

/-- `sinh` is monotone (local; see `sinh_pos_of_pos`). -/
private lemma sinh_le_sinh_of_le {x y : ℝ} (h : x ≤ y) :
    Real.sinh x ≤ Real.sinh y := by
  rw [Real.sinh_eq, Real.sinh_eq]
  have h1 : Real.exp x ≤ Real.exp y := Real.exp_le_exp.mpr h
  have h2 : Real.exp (-y) ≤ Real.exp (-x) := Real.exp_le_exp.mpr (by linarith)
  linarith

/-- Tail lower bound for `sinh`: for `t ≥ 1`,
`sinh(bt) ≥ (1 − e^{−2b})/2 · e^{bt}`. -/
private lemma sinh_tail_lower {b t : ℝ} (hb : 0 < b) (ht : 1 ≤ t) :
    (1 - Real.exp (-(2 * b))) / 2 * Real.exp (b * t) ≤ Real.sinh (b * t) := by
  have key : Real.exp (-(b * t)) ≤ Real.exp (-(2 * b)) * Real.exp (b * t) := by
    rw [← Real.exp_add]
    exact Real.exp_le_exp.mpr (by nlinarith)
  rw [Real.sinh_eq]
  nlinarith

/-- Majorant 1: `e^{−bt}` is integrable on `[1, ∞)` (`exp_neg_integrableOn_Ioi`). -/
private lemma majorant_exp {b : ℝ} (hb : 0 < b) :
    IntegrableOn (fun t => Real.exp (-b * t)) (Set.Ioi 1) :=
  exp_neg_integrableOn_Ioi 1 hb

/-- Majorant 2: `t^{−2}` is integrable on `[1, ∞)` (`integrableOn_Ioi_rpow_of_lt`,
bridged from the `rpow` form to `(t^2)⁻¹` via `t > 0`). -/
private lemma majorant_inv : IntegrableOn (fun t : ℝ => (t ^ 2)⁻¹) (Set.Ioi 1) := by
  have h := integrableOn_Ioi_rpow_of_lt (show (-2 : ℝ) < -1 by norm_num)
    (show (0 : ℝ) < 1 by norm_num)
  refine h.congr_fun (fun t ht => ?_) measurableSet_Ioi
  have ht0 : (0 : ℝ) < t := lt_trans one_pos ht
  rw [Real.rpow_neg ht0.le, ← Real.rpow_natCast t 2]
  norm_num

/-- **Tail integrability (unconditional theorem).**  The Faddeev kernel is
integrable on `[1, ∞)` for every `b > 0`: the oscillatory piece is dominated by
`C·e^{−bt}` (`majorant_exp`), the subtraction by `2|z|·t^{−2}` (`majorant_inv`).
All kernel-specific analysis is proved here. -/
theorem integrableOn_kernel_Ioi_one (b z : ℝ) (hb : 0 < b) :
    IntegrableOn (kernel b z) (Set.Ioi 1) := by
  have hexp : IntegrableOn (fun t => Real.exp (-b * t)) (Set.Ioi 1) := majorant_exp hb
  have hinv : IntegrableOn (fun t : ℝ => (t ^ 2)⁻¹) (Set.Ioi 1) := majorant_inv
  -- the two pieces of the kernel
  set f : ℝ → ℝ := fun t => Real.sin (2 * z * t)
      / (t * Real.sinh (b * t) * Real.sinh (t / b)) with hf_def
  set g : ℝ → ℝ := fun t => 2 * z / t ^ 2 with hg_def
  -- positivity bookkeeping
  have hE : Real.exp (-(2 * b)) < 1 := by
    calc Real.exp (-(2 * b)) < Real.exp 0 := Real.exp_lt_exp.mpr (by linarith)
      _ = 1 := Real.exp_zero
  have hs0 : 0 < Real.sinh (1 / b) := sinh_pos_of_pos (by positivity)
  -- the subtraction piece: `2z/t²` is integrable on `[1, ∞)`
  have hg : IntegrableOn g (Set.Ioi 1) := by
    have h : IntegrableOn (fun t : ℝ => 2 * z * (t ^ 2)⁻¹) (Set.Ioi 1) :=
      hinv.const_mul (2 * z)
    refine h.congr_fun (fun t ht => ?_) measurableSet_Ioi
    simp [hg_def, div_eq_mul_inv]
  -- the oscillatory piece: dominated by `C·e^{−bt}`
  have hfcont : ContinuousOn f (Set.Ioi 1) := by
    apply ContinuousOn.div (by fun_prop) (by fun_prop)
    intro t ht
    have ht0 : (0 : ℝ) < t := lt_trans one_pos ht
    have h1 : 0 < Real.sinh (b * t) := sinh_pos_of_pos (by positivity)
    have h2 : 0 < Real.sinh (t / b) := sinh_pos_of_pos (by positivity)
    exact ne_of_gt (mul_pos (mul_pos ht0 h1) h2)
  have hbound : ∀ t ∈ Set.Ioi (1 : ℝ),
      ‖f t‖ ≤ (2 / ((1 - Real.exp (-(2 * b))) * Real.sinh (1 / b)))
        * Real.exp (-b * t) := by
    intro t ht
    have ht1 : (1 : ℝ) ≤ t := le_of_lt ht
    have ht0 : (0 : ℝ) < t := lt_trans one_pos ht
    have hS1 : 0 < Real.sinh (b * t) := sinh_pos_of_pos (by positivity)
    have hS2 : 0 < Real.sinh (t / b) := sinh_pos_of_pos (by positivity)
    have hD : 0 < t * Real.sinh (b * t) * Real.sinh (t / b) :=
      mul_pos (mul_pos ht0 hS1) hS2
    have hP : 0 < (1 - Real.exp (-(2 * b))) / 2 * Real.exp (b * t) :=
      mul_pos (by linarith) (Real.exp_pos _)
    -- chain: `P·s₀ ≤ S₁·s₀ ≤ S₁·S₂ ≤ t·S₁·S₂`
    have hchain : (1 - Real.exp (-(2 * b))) / 2 * Real.exp (b * t)
        * Real.sinh (1 / b) ≤ t * Real.sinh (b * t) * Real.sinh (t / b) := by
      have step1 : (1 - Real.exp (-(2 * b))) / 2 * Real.exp (b * t)
          * Real.sinh (1 / b) ≤ Real.sinh (b * t) * Real.sinh (1 / b) :=
        mul_le_mul_of_nonneg_right (sinh_tail_lower hb ht1) hs0.le
      have step2 : Real.sinh (b * t) * Real.sinh (1 / b)
          ≤ Real.sinh (b * t) * Real.sinh (t / b) :=
        mul_le_mul_of_nonneg_left
          (sinh_le_sinh_of_le (by gcongr)) hS1.le
      have step3 : Real.sinh (b * t) * Real.sinh (t / b)
          ≤ t * (Real.sinh (b * t) * Real.sinh (t / b)) :=
        le_mul_of_one_le_left (mul_pos hS1 hS2).le ht1
      calc (1 - Real.exp (-(2 * b))) / 2 * Real.exp (b * t) * Real.sinh (1 / b)
          ≤ Real.sinh (b * t) * Real.sinh (1 / b) := step1
        _ ≤ Real.sinh (b * t) * Real.sinh (t / b) := step2
        _ ≤ t * (Real.sinh (b * t) * Real.sinh (t / b)) := step3
        _ = t * Real.sinh (b * t) * Real.sinh (t / b) := by ring
    have habs : ‖f t‖ ≤ 1 / ((1 - Real.exp (-(2 * b))) / 2 * Real.exp (b * t)
        * Real.sinh (1 / b)) := by
      rw [hf_def]
      simp only [Real.norm_eq_abs, abs_div, abs_of_pos hD]
      have hnum : |Real.sin (2 * z * t)| ≤ 1 := Real.abs_sin_le_one _
      have hP0 : 0 < (1 - Real.exp (-(2 * b))) / 2 * Real.exp (b * t)
          * Real.sinh (1 / b) := mul_pos hP hs0
      calc |Real.sin (2 * z * t)| / (t * Real.sinh (b * t) * Real.sinh (t / b))
          ≤ 1 / (t * Real.sinh (b * t) * Real.sinh (t / b)) := by gcongr
        _ ≤ 1 / ((1 - Real.exp (-(2 * b))) / 2 * Real.exp (b * t)
            * Real.sinh (1 / b)) := by
            apply one_div_le_one_div_of_le hP0 hchain
    refine habs.trans (le_of_eq ?_)
    have hE0 : (1 - Real.exp (-(2 * b))) ≠ 0 := by linarith
    have hexp0 : Real.exp (b * t) ≠ 0 := (Real.exp_pos _).ne'
    have hneg : Real.exp (-b * t) = (Real.exp (b * t))⁻¹ := by
      rw [neg_mul]; exact Real.exp_neg _
    rw [hneg]
    field_simp
  have hf : IntegrableOn f (Set.Ioi 1) := by
    have hmaj : IntegrableOn
        (fun t => (2 / ((1 - Real.exp (-(2 * b))) * Real.sinh (1 / b)))
          * Real.exp (-b * t)) (Set.Ioi 1) :=
      hexp.const_mul _
    refine hmaj.mono' (hfcont.aestronglyMeasurable measurableSet_Ioi) ?_
    refine (ae_restrict_iff' measurableSet_Ioi).mpr (Filter.Eventually.of_forall ?_)
    exact hbound
  have : IntegrableOn (fun t => f t - g t) (Set.Ioi 1) := hf.sub hg
  refine this.congr_fun (fun t _ => ?_) measurableSet_Ioi
  rw [hf_def, hg_def]
  rfl

/-! ### The near-`0` piece: the subtraction cancels the pole (THEOREM)

On `(0, 1]` the kernel is **bounded**, hence integrable: writing `y = 2zt`,
`p = bt`, `r = t/b` (so `p·r = t²` exactly), the kernel splits as

  `kernel = (sin y − y)/D  +  2z·(t² − sinh p · sinh r)/(t² · sinh p · sinh r)`,

and each piece is `O(1)`: `|sin y − y| ≤ 2|y|³` (globally) against
`D ≥ t³·e^{−(b+1/b)}` (from `sinh x ≥ x·e^{−x}`), and
`|sinh p · sinh r − pr| ≤ pr·(p² + r²)` on the box `p, r ≤ 1` (from the
two-sided cubic `sinh` estimates supplied by `Real.exp_bound` at order 3)
against `sinh p · sinh r ≥ (49/81)·pr`.  Away from `0` (on `[δ, 1]`,
`δ = min(1, 1/b, b)`) both raw terms are trivially bounded.  All proved
sorry-free below; `integrableOn_kernel_Ioc_zero_one` needs no hypotheses. -/

/-- `sinh x ≥ x·e^{−x}` (from `e^{2x} − 1 ≥ 2x`; holds for all `x`, used on
`x ≥ 0`). -/
private lemma sinh_ge_mul_exp_neg (x : ℝ) :
    x * Real.exp (-x) ≤ Real.sinh x := by
  have h2x : 2 * x + 1 ≤ Real.exp (2 * x) := Real.add_one_le_exp (2 * x)
  have hsplit : Real.exp x - Real.exp (-x)
      = Real.exp (-x) * (Real.exp (2 * x) - 1) := by
    rw [mul_sub, mul_one, ← Real.exp_add]
    ring_nf
  have hstep : Real.exp (-x) * (2 * x) ≤ Real.exp (-x) * (Real.exp (2 * x) - 1) :=
    mul_le_mul_of_nonneg_left (by linarith) (Real.exp_pos (-x)).le
  have h3 : Real.exp (-x) * (2 * x) ≤ Real.exp x - Real.exp (-x) := by
    rw [hsplit]
    exact hstep
  rw [Real.sinh_eq]
  nlinarith [h3]

/-- Global cubic bound `|sin y − y| ≤ 2·|y|³`: `Real.sin_bound` inside the
unit interval, `|sin| ≤ 1` plus `|y| ≤ |y|³` outside. -/
private lemma abs_sin_sub_le_cube (y : ℝ) : |Real.sin y - y| ≤ 2 * |y| ^ 3 := by
  rcases le_or_gt |y| 1 with hy | hy
  · have h := Real.sin_bound hy
    have htri : |Real.sin y - y| ≤ |Real.sin y - (y - y ^ 3 / 6)| + |y| ^ 3 / 6 := by
      have h1 : Real.sin y - y = (Real.sin y - (y - y ^ 3 / 6)) + (-(y ^ 3 / 6)) := by
        ring
      rw [h1]
      refine (abs_add_le _ _).trans ?_
      have h2 : |(-(y ^ 3 / 6))| = |y| ^ 3 / 6 := by
        rw [abs_neg, abs_div, abs_pow]
        norm_num
      rw [h2]
    have h4 : |y| ^ 4 ≤ |y| ^ 3 :=
      pow_le_pow_of_le_one (abs_nonneg y) hy (by norm_num)
    nlinarith [pow_nonneg (abs_nonneg y) 3]
  · have habs : |Real.sin y| ≤ 1 := Real.abs_sin_le_one y
    have htri : |Real.sin y - y| ≤ 1 + |y| := by
      have h1 : Real.sin y - y = Real.sin y + (-y) := by ring
      rw [h1]
      refine (abs_add_le _ _).trans ?_
      rw [abs_neg]
      linarith
    have hy1 : (1 : ℝ) ≤ |y| := hy.le
    have ha2 : (1 : ℝ) ≤ |y| ^ 2 := by nlinarith
    have ha3 : |y| ≤ |y| ^ 3 := by nlinarith
    have hb3 : (1 : ℝ) ≤ |y| ^ 3 := by nlinarith
    linarith

/-- Two-sided cubic `sinh` estimate on `[0, 1]` from `Real.exp_bound` at
order 3: `x − (2/9)x³ ≤ sinh x ≤ x + (2/9)x³`. -/
private lemma sinh_cubic_bounds {x : ℝ} (h0 : 0 ≤ x) (h1 : x ≤ 1) :
    x - 2 / 9 * x ^ 3 ≤ Real.sinh x ∧ Real.sinh x ≤ x + 2 / 9 * x ^ 3 := by
  have hx : |x| ≤ 1 := by rwa [abs_of_nonneg h0]
  have hnx : |(-x)| ≤ 1 := by rwa [abs_neg, abs_of_nonneg h0]
  have hp := Real.exp_bound hx (by norm_num : 0 < 3)
  have hm := Real.exp_bound hnx (by norm_num : 0 < 3)
  have hsum : ∑ m ∈ Finset.range 3, x ^ m / (m.factorial : ℝ)
      = 1 + x + x ^ 2 / 2 := by
    rw [Finset.sum_range_succ, Finset.sum_range_succ, Finset.sum_range_one]
    norm_num [Nat.factorial]
  have hsumm : ∑ m ∈ Finset.range 3, (-x) ^ m / (m.factorial : ℝ)
      = 1 - x + x ^ 2 / 2 := by
    rw [Finset.sum_range_succ, Finset.sum_range_succ, Finset.sum_range_one]
    norm_num [Nat.factorial]
    ring
  rw [hsum] at hp
  rw [hsumm] at hm
  have hxc : |x| ^ 3 = x ^ 3 := by rw [abs_of_nonneg h0]
  have hnxc : |(-x)| ^ 3 = x ^ 3 := by rw [abs_neg, abs_of_nonneg h0]
  rw [hxc] at hp
  rw [hnxc] at hm
  norm_num [Nat.factorial] at hp hm
  have hp' := abs_le.mp hp
  have hm' := abs_le.mp hm
  rw [Real.sinh_eq]
  constructor
  · nlinarith [hp'.1, hm'.2]
  · nlinarith [hp'.2, hm'.1]

/-- Deviation of a product from `p·r` under two-sided cubic bounds on the
factors (pure arithmetic; `sp, sr` stand for `sinh p, sinh r`). -/
private lemma prod_cubic_dev {p r sp sr : ℝ} (hp0 : 0 ≤ p) (hr0 : 0 ≤ r)
    (hp1 : p ≤ 1) (hr1 : r ≤ 1)
    (hlo1 : p - 2 / 9 * p ^ 3 ≤ sp) (hup1 : sp ≤ p + 2 / 9 * p ^ 3)
    (hlo2 : r - 2 / 9 * r ^ 3 ≤ sr) (hup2 : sr ≤ r + 2 / 9 * r ^ 3)
    (hsp0 : 0 ≤ sp) (hsr0 : 0 ≤ sr) :
    |p * r - sp * sr| ≤ p * r * (p ^ 2 + r ^ 2) := by
  have hb0 : (0 : ℝ) ≤ p + 2 / 9 * p ^ 3 := by nlinarith
  have hlo_f2 : (0 : ℝ) ≤ r - 2 / 9 * r ^ 3 := by
    nlinarith [mul_nonneg (mul_nonneg hr0 (by linarith : (0:ℝ) ≤ 1 - r)) (by linarith : (0:ℝ) ≤ 1 + r), pow_nonneg hr0 3]
  have hprod_up : sp * sr ≤ (p + 2 / 9 * p ^ 3) * (r + 2 / 9 * r ^ 3) :=
    mul_le_mul hup1 hup2 hsr0 hb0
  have hprod_lo : (p - 2 / 9 * p ^ 3) * (r - 2 / 9 * r ^ 3) ≤ sp * sr :=
    mul_le_mul hlo1 hlo2 hlo_f2 hsp0
  -- monomial comparisons on the box [0,1]²
  have hpr3 : (0 : ℝ) ≤ p * r ^ 3 := by positivity
  have hp3r : (0 : ℝ) ≤ p ^ 3 * r := by positivity
  have hr3r : r ^ 3 ≤ r := by
    nlinarith [mul_nonneg (mul_nonneg hr0 (by linarith : (0:ℝ) ≤ 1 - r)) (by linarith : (0:ℝ) ≤ 1 + r)]
  have hp3p : p ^ 3 ≤ p := by
    nlinarith [mul_nonneg (mul_nonneg hp0 (by linarith : (0:ℝ) ≤ 1 - p)) (by linarith : (0:ℝ) ≤ 1 + p)]
  have hm3 : p ^ 3 * r ^ 3 ≤ p ^ 3 * r := by nlinarith [pow_nonneg hp0 3]
  rw [abs_le]
  constructor
  · -- −pr(p²+r²) ≤ pr − sp·sr  ⟸  sp·sr ≤ pr + pr(p²+r²)
    nlinarith [hprod_up, hpr3, hp3r, hm3]
  · -- pr − sp·sr ≤ pr(p²+r²)  ⟸  pr − pr(p²+r²) ≤ sp·sr
    nlinarith [hprod_lo, hpr3, hp3r, mul_nonneg (mul_nonneg (pow_nonneg hp0 3) hr0) (sq_nonneg r)]

/-- Lower bound `sp·sr ≥ (49/81)·pr` under the cubic lower bounds on `[0,1]`. -/
private lemma prod_cubic_lower {p r sp sr : ℝ} (hp0 : 0 ≤ p) (hr0 : 0 ≤ r)
    (hp1 : p ≤ 1) (hr1 : r ≤ 1)
    (hlo1 : p - 2 / 9 * p ^ 3 ≤ sp) (hlo2 : r - 2 / 9 * r ^ 3 ≤ sr)
    (hsp0 : 0 ≤ sp) :
    49 / 81 * (p * r) ≤ sp * sr := by
  have hp3p : p ^ 3 ≤ p := by
    nlinarith [mul_nonneg (mul_nonneg hp0 (by linarith : (0:ℝ) ≤ 1 - p)) (by linarith : (0:ℝ) ≤ 1 + p)]
  have hr3r : r ^ 3 ≤ r := by
    nlinarith [mul_nonneg (mul_nonneg hr0 (by linarith : (0:ℝ) ≤ 1 - r)) (by linarith : (0:ℝ) ≤ 1 + r)]
  have h1 : 7 / 9 * p ≤ sp := by nlinarith
  have h2 : 7 / 9 * r ≤ sr := by nlinarith
  have hkey : (7 / 9 * p) * (7 / 9 * r) ≤ sp * sr :=
    mul_le_mul h1 h2 (by positivity) hsp0
  nlinarith [hkey]

/-- **Near-`0` boundedness (the pole cancellation, THEOREM).**  On
`0 < t ≤ 1` with `bt ≤ 1` and `t/b ≤ 1`, the kernel is bounded by the
explicit constant `16|z|³·e^{b+1/b} + (162/49)·|z|·(b² + (1/b)²)`. -/
private lemma kernel_abs_le_near_zero {b z t : ℝ} (hb : 0 < b) (ht0 : 0 < t)
    (ht1 : t ≤ 1) (htb : b * t ≤ 1) (htr : t / b ≤ 1) :
    |kernel b z t| ≤ 16 * |z| ^ 3 * Real.exp (b + 1 / b)
      + 162 / 49 * |z| * (b ^ 2 + (1 / b) ^ 2) := by
  have hp0 : 0 < b * t := by positivity
  have hr0 : 0 < t / b := by positivity
  have hS1 : 0 < Real.sinh (b * t) := sinh_pos_of_pos hp0
  have hS2 : 0 < Real.sinh (t / b) := sinh_pos_of_pos hr0
  have hD : 0 < t * Real.sinh (b * t) * Real.sinh (t / b) :=
    mul_pos (mul_pos ht0 hS1) hS2
  have hSS : 0 < Real.sinh (b * t) * Real.sinh (t / b) := mul_pos hS1 hS2
  -- split: kernel = A + B
  have hsplit : kernel b z t
      = (Real.sin (2 * z * t) - 2 * z * t)
          / (t * Real.sinh (b * t) * Real.sinh (t / b))
        + 2 * z * (t ^ 2 - Real.sinh (b * t) * Real.sinh (t / b))
          / (t ^ 2 * (Real.sinh (b * t) * Real.sinh (t / b))) := by
    have hne1 : Real.sinh (b * t) ≠ 0 := hS1.ne'
    have hne2 : Real.sinh (t / b) ≠ 0 := hS2.ne'
    have hne1' : Real.sinh (t * b) ≠ 0 := by
      rw [mul_comm]
      exact hS1.ne'
    have hne2' : Real.sinh (t * b⁻¹) ≠ 0 := by
      rw [← div_eq_mul_inv]
      exact hS2.ne'
    have hne3 : t ≠ 0 := ht0.ne'
    unfold kernel
    field_simp
    ring
  -- ── Term A ──
  have hyabs : |2 * z * t| = 2 * |z| * t := by
    rw [abs_mul, abs_mul, abs_two, abs_of_pos ht0]
  have hAnum : |Real.sin (2 * z * t) - 2 * z * t| ≤ 2 * (2 * |z| * t) ^ 3 := by
    have h := abs_sin_sub_le_cube (2 * z * t)
    rwa [hyabs] at h
  have hDlow : t ^ 3 * Real.exp (-(b + 1 / b))
      ≤ t * Real.sinh (b * t) * Real.sinh (t / b) := by
    have h1 : b * t * Real.exp (-(b * t)) ≤ Real.sinh (b * t) :=
      sinh_ge_mul_exp_neg (b * t)
    have h2 : t / b * Real.exp (-(t / b)) ≤ Real.sinh (t / b) :=
      sinh_ge_mul_exp_neg (t / b)
    have hprod : t * (b * t * Real.exp (-(b * t)))
        * (t / b * Real.exp (-(t / b)))
        ≤ t * Real.sinh (b * t) * Real.sinh (t / b) := by
      have hstep1 : t * (b * t * Real.exp (-(b * t))) ≤ t * Real.sinh (b * t) :=
        mul_le_mul_of_nonneg_left h1 ht0.le
      exact mul_le_mul hstep1 h2 (by positivity) (by positivity)
    have hval : t * (b * t * Real.exp (-(b * t))) * (t / b * Real.exp (-(t / b)))
        = t ^ 3 * Real.exp (-(b * t + t / b)) := by
      have hexp : Real.exp (-(b * t)) * Real.exp (-(t / b))
          = Real.exp (-(b * t + t / b)) := by
        rw [← Real.exp_add]
        congr 1
        ring
      rw [← hexp]
      field_simp
      try ring
    have hmono : Real.exp (-(b + 1 / b)) ≤ Real.exp (-(b * t + t / b)) := by
      apply Real.exp_le_exp.mpr
      have hbt : b * t ≤ b := by nlinarith
      have htb2 : t / b ≤ 1 / b := by gcongr
      linarith
    calc t ^ 3 * Real.exp (-(b + 1 / b))
        ≤ t ^ 3 * Real.exp (-(b * t + t / b)) := by
          exact mul_le_mul_of_nonneg_left hmono (by positivity)
      _ = t * (b * t * Real.exp (-(b * t))) * (t / b * Real.exp (-(t / b))) :=
          hval.symm
      _ ≤ t * Real.sinh (b * t) * Real.sinh (t / b) := hprod
  have hA : |(Real.sin (2 * z * t) - 2 * z * t)
      / (t * Real.sinh (b * t) * Real.sinh (t / b))|
      ≤ 16 * |z| ^ 3 * Real.exp (b + 1 / b) := by
    rw [abs_div, abs_of_pos hD]
    have hstep : |Real.sin (2 * z * t) - 2 * z * t|
        / (t * Real.sinh (b * t) * Real.sinh (t / b))
        ≤ (2 * (2 * |z| * t) ^ 3) / (t ^ 3 * Real.exp (-(b + 1 / b))) :=
      div_le_div₀ (by positivity) hAnum (by positivity) hDlow
    refine hstep.trans (le_of_eq ?_)
    rw [Real.exp_neg]
    have ht3 : t ^ 3 ≠ 0 := by positivity
    have hE : Real.exp (b + 1 / b) ≠ 0 := (Real.exp_pos _).ne'
    field_simp
    try ring
  -- ── Term B ──
  have hcube := sinh_cubic_bounds hp0.le htb
  have hcube2 := sinh_cubic_bounds hr0.le htr
  have hpr : b * t * (t / b) = t ^ 2 := by
    field_simp
    try ring
  have hBnum : |t ^ 2 - Real.sinh (b * t) * Real.sinh (t / b)|
      ≤ t ^ 2 * ((b * t) ^ 2 + (t / b) ^ 2) := by
    have h := prod_cubic_dev hp0.le hr0.le htb htr
      hcube.1 hcube.2 hcube2.1 hcube2.2 hS1.le hS2.le
    rwa [hpr] at h
  have hBden : 49 / 81 * t ^ 2 ≤ Real.sinh (b * t) * Real.sinh (t / b) := by
    have h := prod_cubic_lower hp0.le hr0.le htb htr hcube.1 hcube2.1 hS1.le
    rwa [hpr] at h
  have hB : |2 * z * (t ^ 2 - Real.sinh (b * t) * Real.sinh (t / b))
      / (t ^ 2 * (Real.sinh (b * t) * Real.sinh (t / b)))|
      ≤ 162 / 49 * |z| * (b ^ 2 + (1 / b) ^ 2) := by
    have hden : 0 < t ^ 2 * (Real.sinh (b * t) * Real.sinh (t / b)) := by positivity
    rw [abs_div, abs_of_pos hden, abs_mul, abs_mul, abs_two]
    have hdenlow : t ^ 2 * (49 / 81 * t ^ 2)
        ≤ t ^ 2 * (Real.sinh (b * t) * Real.sinh (t / b)) :=
      mul_le_mul_of_nonneg_left hBden (by positivity)
    have hnum_le : 2 * |z| * |t ^ 2 - Real.sinh (b * t) * Real.sinh (t / b)|
        ≤ 2 * |z| * (t ^ 2 * ((b * t) ^ 2 + (t / b) ^ 2)) :=
      mul_le_mul_of_nonneg_left hBnum (by positivity)
    have hstep : 2 * |z| * |t ^ 2 - Real.sinh (b * t) * Real.sinh (t / b)|
        / (t ^ 2 * (Real.sinh (b * t) * Real.sinh (t / b)))
        ≤ (2 * |z| * (t ^ 2 * ((b * t) ^ 2 + (t / b) ^ 2)))
          / (t ^ 2 * (49 / 81 * t ^ 2)) :=
      div_le_div₀ (by positivity) hnum_le (by positivity) hdenlow
    refine hstep.trans (le_of_eq ?_)
    have ht2 : t ≠ 0 := ht0.ne'
    have hb0 : b ≠ 0 := hb.ne'
    field_simp
    try ring
  -- assemble
  rw [hsplit]
  calc |(Real.sin (2 * z * t) - 2 * z * t)
        / (t * Real.sinh (b * t) * Real.sinh (t / b))
      + 2 * z * (t ^ 2 - Real.sinh (b * t) * Real.sinh (t / b))
        / (t ^ 2 * (Real.sinh (b * t) * Real.sinh (t / b)))|
      ≤ |(Real.sin (2 * z * t) - 2 * z * t)
        / (t * Real.sinh (b * t) * Real.sinh (t / b))|
      + |2 * z * (t ^ 2 - Real.sinh (b * t) * Real.sinh (t / b))
        / (t ^ 2 * (Real.sinh (b * t) * Real.sinh (t / b)))| := abs_add_le _ _
    _ ≤ 16 * |z| ^ 3 * Real.exp (b + 1 / b)
      + 162 / 49 * |z| * (b ^ 2 + (1 / b) ^ 2) := add_le_add hA hB

/-- Away from `0` (on `[δ, 1]`) both raw kernel terms are trivially bounded. -/
private lemma kernel_abs_le_away {b z t δ : ℝ} (hb : 0 < b) (hδ0 : 0 < δ)
    (hδt : δ ≤ t) :
    |kernel b z t| ≤ 1 / (δ * Real.sinh (b * δ) * Real.sinh (δ / b))
      + 2 * |z| / δ ^ 2 := by
  have ht0 : 0 < t := lt_of_lt_of_le hδ0 hδt
  have hS1 : 0 < Real.sinh (b * t) := sinh_pos_of_pos (by positivity)
  have hS2 : 0 < Real.sinh (t / b) := sinh_pos_of_pos (by positivity)
  have hs1δ : 0 < Real.sinh (b * δ) := sinh_pos_of_pos (by positivity)
  have hs2δ : 0 < Real.sinh (δ / b) := sinh_pos_of_pos (by positivity)
  have hD : 0 < t * Real.sinh (b * t) * Real.sinh (t / b) :=
    mul_pos (mul_pos ht0 hS1) hS2
  have hDδ : 0 < δ * Real.sinh (b * δ) * Real.sinh (δ / b) :=
    mul_pos (mul_pos hδ0 hs1δ) hs2δ
  have hDge : δ * Real.sinh (b * δ) * Real.sinh (δ / b)
      ≤ t * Real.sinh (b * t) * Real.sinh (t / b) := by
    have h1 : Real.sinh (b * δ) ≤ Real.sinh (b * t) :=
      sinh_le_sinh_of_le (by nlinarith)
    have h2 : Real.sinh (δ / b) ≤ Real.sinh (t / b) :=
      sinh_le_sinh_of_le (by gcongr)
    have hstep1 : δ * Real.sinh (b * δ) ≤ t * Real.sinh (b * t) :=
      mul_le_mul hδt h1 hs1δ.le ht0.le
    exact mul_le_mul hstep1 h2 hs2δ.le (by positivity)
  have hterm1 : |Real.sin (2 * z * t)
      / (t * Real.sinh (b * t) * Real.sinh (t / b))|
      ≤ 1 / (δ * Real.sinh (b * δ) * Real.sinh (δ / b)) := by
    rw [abs_div, abs_of_pos hD]
    exact div_le_div₀ (by positivity) (Real.abs_sin_le_one _) hDδ hDge
  have hterm2 : |2 * z / t ^ 2| ≤ 2 * |z| / δ ^ 2 := by
    rw [abs_div, abs_mul, abs_two]
    have ht2 : |t ^ 2| = t ^ 2 := abs_of_pos (by positivity)
    rw [ht2]
    exact div_le_div₀ (by positivity) le_rfl (by positivity) (by nlinarith)
  have hsub : kernel b z t
      = Real.sin (2 * z * t) / (t * Real.sinh (b * t) * Real.sinh (t / b))
        + (-(2 * z / t ^ 2)) := by
    unfold kernel
    ring
  rw [hsub]
  calc |Real.sin (2 * z * t) / (t * Real.sinh (b * t) * Real.sinh (t / b))
      + (-(2 * z / t ^ 2))|
      ≤ |Real.sin (2 * z * t) / (t * Real.sinh (b * t) * Real.sinh (t / b))|
        + |(-(2 * z / t ^ 2))| := abs_add_le _ _
    _ = |Real.sin (2 * z * t) / (t * Real.sinh (b * t) * Real.sinh (t / b))|
        + |2 * z / t ^ 2| := by rw [abs_neg]
    _ ≤ 1 / (δ * Real.sinh (b * δ) * Real.sinh (δ / b)) + 2 * |z| / δ ^ 2 :=
        add_le_add hterm1 hterm2

/-- **Near-`0` integrability (THEOREM, no hypotheses).**  The kernel is
bounded on `(0, 1]` — the `−2z/t²` subtraction cancels the pole — hence
integrable there (`Ioc 0 1` has finite measure). -/
theorem integrableOn_kernel_Ioc_zero_one (b z : ℝ) (hb : 0 < b) :
    IntegrableOn (kernel b z) (Set.Ioc 0 1) := by
  have hδ0 : 0 < min 1 (min (1 / b) b) :=
    lt_min one_pos (lt_min (by positivity) hb)
  set δ : ℝ := min 1 (min (1 / b) b) with hδdef
  have hδ1 : δ ≤ 1 := min_le_left _ _
  have hδinv : δ ≤ 1 / b := le_trans (min_le_right _ _) (min_le_left _ _)
  have hδb : δ ≤ b := le_trans (min_le_right _ _) (min_le_right _ _)
  have hmeas : AEStronglyMeasurable (kernel b z) volume := by
    apply Measurable.aestronglyMeasurable
    unfold kernel
    fun_prop
  have hIoc : volume (Set.Ioc (0 : ℝ) 1) ≠ ⊤ := measure_Ioc_lt_top.ne
  refine Measure.integrableOn_of_bounded hIoc hmeas
    (M := max (16 * |z| ^ 3 * Real.exp (b + 1 / b)
        + 162 / 49 * |z| * (b ^ 2 + (1 / b) ^ 2))
      (1 / (δ * Real.sinh (b * δ) * Real.sinh (δ / b)) + 2 * |z| / δ ^ 2)) ?_
  · refine (ae_restrict_iff' measurableSet_Ioc).mpr (Filter.Eventually.of_forall ?_)
    intro t ht
    obtain ⟨ht0, ht1⟩ := ht
    rw [Real.norm_eq_abs]
    rcases le_or_gt t δ with hcase | hcase
    · refine le_trans (kernel_abs_le_near_zero hb ht0 ht1 ?_ ?_) (le_max_left _ _)
      · have htinv : t ≤ 1 / b := le_trans hcase hδinv
        calc b * t ≤ b * (1 / b) := by gcongr
          _ = 1 := by field_simp
      · rw [div_le_one hb]
        exact le_trans hcase hδb
    · exact le_trans (kernel_abs_le_away hb hδ0 hcase.le) (le_max_right _ _)


/-- **Full integrability on `(0, ∞)` (unconditional theorem).**  Near-`0` is
`integrableOn_kernel_Ioc_zero_one`; the tail is `integrableOn_kernel_Ioi_one`.
Both are hypothesis-free, so the Faddeev kernel is integrable on all of
`(0, ∞)` for every `b > 0` with no remaining analytic input — the def↔contour
identification (the `8e-29` pin) is the only open piece, and is assumed
nowhere. -/
theorem integrableOn_kernel_Ioi_zero (b z : ℝ) (hb : 0 < b) :
    IntegrableOn (kernel b z) (Set.Ioi 0) := by
  have hset : Set.Ioc (0 : ℝ) 1 ∪ Set.Ioi 1 = Set.Ioi 0 :=
    Set.Ioc_union_Ioi_eq_Ioi (by norm_num)
  rw [← hset]
  exact (integrableOn_kernel_Ioc_zero_one b z hb).union
    (integrableOn_kernel_Ioi_one b z hb)

end QOU.MathlibExt.FaddeevPhiBRealIntegral
