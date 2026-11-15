/-
# conj:binding-qbeta-complex-volume — the fibre-descent conjecture, as a §3b class

The complex-volume observable `𝔙 = Vol + i·CS` (`conj:binding-qbeta-complex-volume`) packages the
two real archimedean observables as `Re 𝔙 = 𝔈_bind` (binding, **bar-even** cosh) and
`Im 𝔙 = 𝔔_β` (β-decay Q-value, **bar-odd** sinh). The **open** content of the conjecture is that
the framework's binding and Q_β observables both **descend from one fibre object** `𝔙` — not merely
that they can be packaged as the real/imaginary parts of *some* complex number.

This file states that descent as a §3b conjecture class with genuine content (the bar-parity
structure of the two channels), and exhibits the natural `cosh/sinh` model that makes the class
**non-vacuous** (§3b-tax: a conjecture carrier must assert something and be of an inhabited shape).

* `ComplexVolumeFibre V` — a fibre map `V : ℝ → ℂ` (`η ↦ 𝔙(e^η)`) whose **real part is bar-even**
  (the binding / cosh channel) and **imaginary part is bar-odd** (the Q_β / sinh channel) under the
  bar involution `η ↦ −η`. This is the structural content the descent must have.
* `vCoshSinh` + its instance — the natural model `V₀(η) = cosh η + i·sinh η` satisfies it
  (`Re = cosh` even, `Im = sinh` odd), witnessing the shape is realizable.

What is **NOT** asserted (the open conjecture): that the framework's *actual* binding and Q_β
observables — `Re 𝔙 = 𝔈_bind`, `Im 𝔙 = 𝔔_β` with `𝔙 = E₀·tr_M((Π_free−1)∘ℳ)` — descend from a
single such `V`. There is **no instance for the trace object** here; that descent is the open
keystone, advanced (the ζ₄ generator coupling is proved in
`QOU.Mass.Zeta4ComplexVolumeModerator`: `cosh(z+iπ/2)=i·sinh z`) but not closed, and the
observable-level match is degenerate (`Im(q₀)=0`, see
`computations/substrate/frakV_zeta4_fibre_vs_observable_probe.py`).

Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-06-28-frakV-zeta4-fibre-vs-observable.md
-/
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic

namespace QOU.Mass.ComplexVolumeFibreDescent

/-- **conj:binding-qbeta-complex-volume (fibre descent), §3b class.** A complex-volume fibre object
is a map `V : ℝ → ℂ` whose **real part is bar-even** (binding / cosh channel: even under `η ↦ −η`)
and **imaginary part is bar-odd** (Q_β / sinh channel: odd under `η ↦ −η`). The framework's binding
and Q_β observables descending from one such `V` is the open conjecture. -/
class ComplexVolumeFibre (V : ℝ → ℂ) : Prop where
  /-- `Re V` is bar-even — the binding (cosh) channel. -/
  re_bar_even : ∀ η : ℝ, (V (-η)).re = (V η).re
  /-- `Im V` is bar-odd — the Q_β (sinh) channel. -/
  im_bar_odd : ∀ η : ℝ, (V (-η)).im = -(V η).im

/-- The natural `cosh/sinh` model `V₀(η) = cosh η + i·sinh η`. -/
noncomputable def vCoshSinh (η : ℝ) : ℂ := (Real.cosh η : ℂ) + Complex.I * (Real.sinh η : ℂ)

@[simp] theorem vCoshSinh_re (η : ℝ) : (vCoshSinh η).re = Real.cosh η := by
  simp only [vCoshSinh, Complex.add_re, Complex.ofReal_re, Complex.mul_re, Complex.I_re,
    Complex.I_im, Complex.ofReal_im, zero_mul, mul_zero, sub_zero, add_zero]

@[simp] theorem vCoshSinh_im (η : ℝ) : (vCoshSinh η).im = Real.sinh η := by
  simp only [vCoshSinh, Complex.add_im, Complex.ofReal_im, Complex.mul_im, Complex.I_re,
    Complex.I_im, Complex.ofReal_re, one_mul, mul_zero, zero_add]

/-- **The conjecture class is non-vacuous.** `V₀(η) = cosh η + i·sinh η` is a complex-volume fibre
object: `Re V₀ = cosh η` is bar-even (binding channel) and `Im V₀ = sinh η` is bar-odd (Q_β
channel). This witnesses the structural shape is realizable — it does **not** claim the framework's
observables descend from `V₀`. -/
noncomputable instance : ComplexVolumeFibre vCoshSinh where
  re_bar_even := by intro η; simp [Real.cosh_neg]
  im_bar_odd := by intro η; simp [Real.sinh_neg]

/-! ## The self-dual locus constraint (from `prop:self-dual-higgs-real-volume`)

The keystone `QOU.Knot.SelfDuality.higgs_complex_volume_real` proves, over a generic
`(CommRing R, σ)`, that a bar-fixed element has zero bar-odd part. Here is its **fibre-map
instance**, wired into the descent class: an **amphichiral** source (`J_N(q) = J_N(q⁻¹)`, the Higgs
`4₁`) gives a bar-fixed fibre object, and for a bar-fixed `ComplexVolumeFibre` the **Q_β channel
vanishes identically** — `𝔙` is purely real (binding only, `CS = 0`).

This is a **falsifiability constraint on the open descent**: any candidate assembly of the actual
trace object `𝔙 = E₀·tr_M((Π_free−1)∘ℳ)` into a `ComplexVolumeFibre` must send amphichiral
composites to real `𝔙` (zero Q_β). A proposed assembly producing a nonzero Q_β for a self-dual
composite is refuted by `barFixed_qbeta_zero` below — structure narrowing the search, per
formalize-first. -/

/-- A fibre object is **bar-fixed** (self-dual / amphichiral source): `V(−η) = V(η)`. This is the
fibre-map form of `J_N(q) = J_N(q⁻¹)` (the Higgs `4₁` self-duality). -/
def BarFixed (V : ℝ → ℂ) : Prop := ∀ η : ℝ, V (-η) = V η

/-- **Self-dual locus vanishing (the CS = 0 mechanism, fibre-map instance).** A bar-fixed
complex-volume fibre object has identically vanishing Q_β (bar-odd / imaginary) channel. -/
theorem barFixed_qbeta_zero (V : ℝ → ℂ) [ComplexVolumeFibre V] (h : BarFixed V) (η : ℝ) :
    (V η).im = 0 := by
  have hodd := ComplexVolumeFibre.im_bar_odd (V := V) η
  rw [h η] at hodd
  linarith

/-- On the self-dual locus `𝔙` is **purely real**: the fibre object equals its binding (Re)
channel — the bare Higgs contributes only the volume/mass face. -/
theorem barFixed_real (V : ℝ → ℂ) [ComplexVolumeFibre V] (h : BarFixed V) (η : ℝ) :
    V η = ((V η).re : ℂ) := by
  apply Complex.ext
  · simp
  · simpa using barFixed_qbeta_zero V h η

/-- At the bar fixed **point** `η = 0` (the classical point `q = 1`) the Q_β channel of *every*
fibre object vanishes — no self-duality hypothesis needed. β-decay is a strictly `q ≠ 1`
(deformation) phenomenon. -/
theorem im_at_classical_point_zero (V : ℝ → ℂ) [ComplexVolumeFibre V] : (V 0).im = 0 := by
  have hodd := ComplexVolumeFibre.im_bar_odd (V := V) 0
  rw [neg_zero] at hodd
  linarith

/-- **The constraint is non-trivial.** The cosh/sinh model is *not* bar-fixed — its Q_β channel is
genuinely nonzero away from `η = 0` — so self-duality is a real restriction on fibre objects, not
an artifact of the class shape (§3b-tax non-degeneracy). -/
theorem vCoshSinh_not_barFixed : ¬ BarFixed vCoshSinh := by
  intro h
  have h1 := congrArg Complex.im (h 1)
  rw [vCoshSinh_im, vCoshSinh_im, Real.sinh_neg] at h1
  have hz : Real.sinh 1 = 0 := by linarith
  rw [Real.sinh_eq] at hz
  have hexp : Real.exp (-1) < Real.exp 1 := Real.exp_lt_exp.mpr (by norm_num)
  linarith

end QOU.Mass.ComplexVolumeFibreDescent
