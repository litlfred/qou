import Mathlib.Data.Complex.Basic
import Mathlib.Tactic

/-!
# Why the `S` parity is convention-immune: it never reads the Markov parameter

`ImQDecayLinearResponse.lean` proves the `ε`-parity for **one** concrete
Laurent expression (`fig8TraceC`), by the route

  real coefficients  ⇒  `T(conj z) = conj (T z)`  ⇒  `Im T` odd in `ε`.

The registry's KC21 row claims that parity statement is *convention-immune* —
unaffected by the 2026-08-09 Markov-trace flip `C → D`
(`z_C = √q/(1+q)` ↦ `z_D = q³/(q²+1)`). That claim was **asserted**, not
derived: `c₃` is *defined by* an extractor whose `N=1` rung consumes `z`
(`α = (z−1)h/2`), and under `D` the extractor is a numerically and
structurally different function (`c₃ ≈ −974` rather than `≈ −2.07`). Parity of
`f_C` does not transfer to `f_D` just because both are written `c₃`.

This file supplies the missing reduction. The observation is that the middle
step above needs nothing about the *formula* for `T`: it needs only that
conjugation commutes with it. Isolate that as `Reflective`, prove the parity
from it alone, and prove the class is **closed** under every operation the
ladder performs. The Markov parameter then enters as one reflective
ingredient among many, and *which* `z` it is never appears in the argument —
which is exactly what "convention-immune" should mean.

The concrete instances confirming `z_D` (rational, proved here) and `z_C`
(needs the principal `√` branch, so measured rather than proved — probe
assertion A8) sit in
`computations/qbeta/qbeta_kc21_parity_convention_immunity_probe.py`.

Two scope pins, both load-bearing:

* **This is complex conjugation, not the bar involution.** `σ : q ↦ q⁻¹` is a
  different involution. Nothing here says `S` is bar-odd, and nothing here
  bears on `bar(z_D) = q⁻⁴·z_D` or on the `z_C` full-bar-condition failure.
* **`Reflective` does not single out the bar-odd channel.** Every reflective
  function has `Im` odd in `ε` — bar-even ones included (`Q_A` is bar-even and
  has it; probe assertion A11). So the parity is a consequence of
  real-analyticity, and is *not* evidence that the channel carrying it is
  bar-odd. KC21 states the derivation as "bar-odd ⇒ odd in ε"; the honest
  statement is "reflective ⇒ `Im` odd in ε".

Base ring is `ℂ` by necessity (§7c archimedean side): conjugation and the `Im`
projection are the content. No `sorry`.

-- Ref: [leitner2026] docs/audits/2026-08-15-kc21-parity-convention-immunity-audit.md
-- Ref: [leitner2026] conj:im-q-physical-role
-/

-- Declarations here are nested one namespace deeper than the module's
-- parent so this module and QOU.QBeta.LadderPhaseMirrorCovariance
-- can be imported together: both declared the same fully-qualified
-- name(s), and Lean rejects the second import with "environment already
-- contains" (bean `qou-kfcl`). Nothing imports this module, so the
-- nesting costs no consumer.
namespace QOU.QBeta.LadderParityReflection

/-- A map is **reflective** when complex conjugation commutes with it:
    `f(conj z) = conj (f z)`. Every function built from real constants by the
    field operations and composition is reflective (see the closure lemmas
    below); `fig8TraceC_conj` is the concrete instance for the figure-eight
    trace. -/
def Reflective (f : ℂ → ℂ) : Prop :=
  ∀ z : ℂ, f (starRingEnd ℂ z) = starRingEnd ℂ (f z)

section Parity

variable {f : ℂ → ℂ}

/-- **Reflective ⇒ `Im` is odd in `ε`.** `Im f(q₀ − iε) = − Im f(q₀ + iε)`.

    This is the generalisation of `fig8Trace_im_odd`: the hypothesis is a
    property of `f`, not of its construction, so no ingredient of `f` — the
    Markov parameter included — appears in the statement or the proof. -/
theorem reflective_im_odd (hf : Reflective f) (q0 eps : ℝ) :
    (f ⟨q0, -eps⟩).im = -(f ⟨q0, eps⟩).im := by
  have hconj : (⟨q0, -eps⟩ : ℂ) = starRingEnd ℂ ⟨q0, eps⟩ := by
    apply Complex.ext <;> simp [Complex.conj_re, Complex.conj_im]
  rw [hconj, hf, Complex.conj_im]

/-- **Reflective ⇒ `Re` is even in `ε`.** The companion of `reflective_im_odd`,
    and the reason the *literal* reading of KC21's `S(−ε) = −S(ε)` is false:
    the real part is even and generically nonzero, so the full value is not an
    odd function of `ε`. Only the imaginary part / decay projection is. -/
theorem reflective_re_even (hf : Reflective f) (q0 eps : ℝ) :
    (f ⟨q0, -eps⟩).re = (f ⟨q0, eps⟩).re := by
  have hconj : (⟨q0, -eps⟩ : ℂ) = starRingEnd ℂ ⟨q0, eps⟩ := by
    apply Complex.ext <;> simp [Complex.conj_re, Complex.conj_im]
  rw [hconj, hf, Complex.conj_re]

/-- **Real substrate carries no decay projection.** At `ε = 0` the imaginary
    part vanishes — the generalisation of `fig8Trace_im_real_zero`. -/
theorem reflective_im_real_zero (hf : Reflective f) (q0 : ℝ) :
    (f ⟨q0, 0⟩).im = 0 := by
  have h := reflective_im_odd hf q0 0
  simp only [neg_zero] at h
  linarith

end Parity

section Closure

variable {f g : ℂ → ℂ}

/-- A real constant is reflective. -/
theorem reflective_const_real (r : ℝ) : Reflective (fun _ => (r : ℂ)) := by
  intro z; simp

/-- The identity is reflective. -/
theorem reflective_id : Reflective id := by
  intro z; rfl

theorem Reflective.add (hf : Reflective f) (hg : Reflective g) :
    Reflective (fun z => f z + g z) := by
  intro z; simp [hf z, hg z]

theorem Reflective.sub (hf : Reflective f) (hg : Reflective g) :
    Reflective (fun z => f z - g z) := by
  intro z; simp [hf z, hg z]

theorem Reflective.mul (hf : Reflective f) (hg : Reflective g) :
    Reflective (fun z => f z * g z) := by
  intro z; simp [hf z, hg z]

theorem Reflective.neg (hf : Reflective f) : Reflective (fun z => -f z) := by
  intro z; simp [hf z]

/-- Reflectivity survives inversion — `ℂ` is a field and `starRingEnd` is a
    ring hom, so `conj (x⁻¹) = (conj x)⁻¹` including at `x = 0`. -/
theorem Reflective.inv (hf : Reflective f) : Reflective (fun z => (f z)⁻¹) := by
  intro z; simp [hf z, map_inv₀]

theorem Reflective.div (hf : Reflective f) (hg : Reflective g) :
    Reflective (fun z => f z / g z) := by
  intro z; simp [hf z, hg z, map_div₀]

theorem Reflective.pow (hf : Reflective f) (n : ℕ) :
    Reflective (fun z => f z ^ n) := by
  intro z; simp [hf z]

/-- Reflectivity is closed under composition — so a ladder built by
    substituting one reflective expression into another stays reflective. -/
theorem Reflective.comp (hf : Reflective f) (hg : Reflective g) :
    Reflective (f ∘ g) := by
  intro z; simp only [Function.comp_apply, hg z, hf (g z)]

end Closure

section MarkovParameter

/-- The `N=1` rung phase `α = (z−1)·h/2` with `h = q − q⁻¹`, as a function of
    the substrate parameter, **parameterised by the Markov parameter `z`**.
    This is the site where the trace convention enters the `Q_β` ladder
    (`qbeta_utils.py:124-125`; the same `z` in the exact-series core at
    `qbeta_ck_sseries_exact_rational.py:20,248`). -/
noncomputable def alphaPhase (zf : ℂ → ℂ) (q : ℂ) : ℂ :=
  (zf q - 1) * (q - q⁻¹) / 2

/-- **The convention-immunity statement.** For *every* reflective Markov
    parameter, the rung phase is reflective.

    This quantifies over conventions: it is not a fact about `z_C`, nor about
    `z_D`, but about the whole class. A future convention change cannot break
    it unless the new `z` is non-reflective — i.e. unless it fails to be
    real-valued on the real `q`-axis. -/
theorem alphaPhase_reflective {zf : ℂ → ℂ} (hz : Reflective zf) :
    Reflective (alphaPhase zf) := by
  intro q
  simp only [alphaPhase, map_div₀, map_mul, map_sub, map_one, map_inv₀,
    map_ofNat, hz q]

/-- **The parity, for any convention.** `Im α(q₀ − iε) = − Im α(q₀ + iε)`
    whenever the Markov parameter is reflective — the `C`/`D`/anything
    statement the KC21 immunity claim needed. -/
theorem alphaPhase_im_odd_of_reflective_markov {zf : ℂ → ℂ} (hz : Reflective zf)
    (q0 eps : ℝ) :
    (alphaPhase zf ⟨q0, -eps⟩).im = -(alphaPhase zf ⟨q0, eps⟩).im :=
  reflective_im_odd (alphaPhase_reflective hz) q0 eps

/-- Convention **D** (SU(2)/Temperley–Lieb Jones; owner ruling 2026-08-09):
    `z_D = q³/(q²+1)`. -/
noncomputable def zD (q : ℂ) : ℂ := q ^ 3 / (q ^ 2 + 1)

/-- `z_D` is reflective — it is a rational function with rational
    coefficients. Together with `alphaPhase_im_odd_of_reflective_markov` this
    discharges the `D`-frame half of the immunity claim in Lean; the `C`-frame
    half needs the principal branch of `√q` (outside this file's algebraic
    scope) and is measured instead, at 60 dps, by probe assertion A8. -/
theorem zD_reflective : Reflective zD := by
  intro q
  simp only [zD, map_div₀, map_pow, map_add, map_one]

/-- The `D`-frame rung phase has `Im` odd in `ε`. Concrete corollary; the
    general statement above is the one that carries the immunity. -/
theorem alphaPhase_zD_im_odd (q0 eps : ℝ) :
    (alphaPhase zD ⟨q0, -eps⟩).im = -(alphaPhase zD ⟨q0, eps⟩).im :=
  alphaPhase_im_odd_of_reflective_markov zD_reflective q0 eps

end MarkovParameter

end QOU.QBeta.LadderParityReflection
