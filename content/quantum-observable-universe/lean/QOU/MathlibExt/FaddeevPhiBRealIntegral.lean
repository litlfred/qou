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

**Hypothesis discipline (the `PhiBProd` precedent).**  The two *majorant*
integrability facts — `e^{−bt}` and `t^{−2}` are integrable on `[1, ∞)` —
are standard Mathlib theorems (`exp_neg_integrableOn_Ioi`,
`integrableOn_Ioi_rpow_of_lt`) whose modules
(`Mathlib.MeasureTheory.Integral.ExpDecay`,
`Mathlib.Analysis.SpecialFunctions.Integrals`) are outside the current
sandbox olean cone.  They are therefore carried as **explicit named
hypotheses** (`hexp`, `hinv`) on `integrableOn_kernel_Ioi_one` — not
axiomatized, not `sorry`'d; on a full Mathlib each discharges in one line.
What remains genuinely open for integrability on all of `(0, ∞)` is only the
bounded near-`0` piece (`Ioc 0 1`, where the `−2z/t²` subtraction cancels the
pole); `integrableOn_kernel_Ioi_zero` reduces the full statement to exactly
that hypothesis.  The def↔contour identification of `phiB` with the Faddeev
contour integral remains the `8e-29` numerical pin (module docstring) — it is
NOT assumed anywhere in this file. -/

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

/-- **Tail integrability.**  The Faddeev kernel is integrable on `[1, ∞)` for
every `b > 0`: the oscillatory piece is dominated by `C·e^{−bt}`, the
subtraction by `2|z|·t^{−2}`.  All kernel-specific analysis is proved here;
the two hypotheses are the standard majorant facts (see the section
docstring), each a one-line Mathlib theorem outside the sandbox olean cone. -/
theorem integrableOn_kernel_Ioi_one (b z : ℝ) (hb : 0 < b)
    (hexp : IntegrableOn (fun t => Real.exp (-b * t)) (Set.Ioi 1))
    (hinv : IntegrableOn (fun t : ℝ => (t ^ 2)⁻¹) (Set.Ioi 1)) :
    IntegrableOn (kernel b z) (Set.Ioi 1) := by
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

/-- **Reduction of full integrability to the bounded near-`0` piece.**  Given
integrability on `(0, 1]` (where the `−2z/t²` subtraction cancels the pole —
the remaining open analytic input), the kernel is integrable on all of
`(0, ∞)`; the tail is the theorem above. -/
theorem integrableOn_kernel_Ioi_zero (b z : ℝ) (hb : 0 < b)
    (hexp : IntegrableOn (fun t => Real.exp (-b * t)) (Set.Ioi 1))
    (hinv : IntegrableOn (fun t : ℝ => (t ^ 2)⁻¹) (Set.Ioi 1))
    (h0 : IntegrableOn (kernel b z) (Set.Ioc 0 1)) :
    IntegrableOn (kernel b z) (Set.Ioi 0) := by
  have hset : Set.Ioc (0 : ℝ) 1 ∪ Set.Ioi 1 = Set.Ioi 0 :=
    Set.Ioc_union_Ioi_eq_Ioi (by norm_num)
  rw [← hset]
  exact h0.union (integrableOn_kernel_Ioi_one b z hb hexp hinv)

end QOU.MathlibExt.FaddeevPhiBRealIntegral
