/-
# Why the nucleon difference is elliptic: nearly-parallel hyperbolic directions

Bean `qou-cds1`, Step 23. Sequel to `TraceRealSpectrumComplex`, which found that
`Δ_L = NF(n) − NF(p)` is **elliptic** in the `(2,1)` block while `Δ_S` and the
individual nucleon normal forms are hyperbolic. The question left open was
whether that is **structural** or an artefact of the 11-crossing word choice.

It is structural, and this file carries the mechanism.

## The identity

For traceless `2 × 2` matrices `A₀ = (a, b; c, −a)` and `B₀ = (d, e; f, −d)`,

    det (A₀ − B₀) = det A₀ + det B₀ + tr (A₀ B₀).

`det_sub_traceless` below, by `ring`. A traceless real `2 × 2` matrix has
`det < 0` exactly when its spectrum is real (**hyperbolic**) and `det > 0` when it
is a complex-conjugate pair (**elliptic**), so this says:

> the difference of two hyperbolic directions is elliptic precisely when their
> Killing pairing `tr(A₀B₀)` exceeds `−(det A₀ + det B₀)` — that is, when the two
> directions are sufficiently **aligned**.

## What that gives, measured

At the proton pin, in the `(2,1)` block
(`qbeta_nucleon_difference_ellipticity_structural_probe.py`):

    det A₀ (proton)   = −1.041656      hyperbolic
    det B₀ (neutron)  = −1.056560      hyperbolic
    tr (A₀ B₀)        =  2.107175
    sum               =  0.0089591  > 0   ⇒ ELLIPTIC

and the direct `det` of the traceless part of `Δ_L` reproduces `0.0089591` to
working precision, so the identity is not merely stated but checked.

The threshold for exact parallelism is `2√(det A₀ · det B₀) = 2.098163`, against
a measured `2.107175` — the neutron and proton traceless parts are aligned to
within **0.43 %** of parallel. **That is the near-degeneracy of the nucleons**
(`m_n − m_p = 1.29 MeV` out of `939`), not a property of any particular word.

## Why it is not an artefact

* **8 of 9** quark-word orderings of `uud`/`udd` give an elliptic difference.
  (Honest caveat: they collapse to only **3 distinct** values, of which 2 are
  elliptic, so the counting evidence alone is weak — the mechanism and the
  controls below are what carry it.)
* **Random control**: NF vectors resampled at matched scale give an elliptic
  difference **8.9 %** of the time (4000 draws). The nucleon family is an order
  of magnitude enriched over its own null.
* **Robust in `q`**: the discriminant `tr² − 4 det` stays negative with no sign
  change across `q ∈ [1.01, 1.61]`, varying smoothly from `−0.0338` to `−0.0448`.
  So this is not fine-tuning at `q₀`.

## Scope

Scope-(a). The Lean content is the algebraic identity and the sign dictionary;
everything numerical is in the probe. Nothing derived, proposed, wired or
readmitted, and no `c_k` value is asserted — in particular the eigenphase
`θ = 2.020445` remains a factor 35.7 from the ladder phase (Step 22), so this
explains why an elliptic generator *exists*, not why it would be the right one.
-/
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

namespace QOU.QBeta

/-- **The mechanism.** For traceless `2 × 2` matrices written out by entries,
`det (A₀ − B₀) = det A₀ + det B₀ + tr (A₀ B₀)`, where a traceless
`(x, y; z, −x)` has `det = −x² − yz` and
`tr (A₀ B₀) = 2ad + bf + ce`. -/
theorem det_sub_traceless (a b c d e f : ℝ) :
    (-(a - d) ^ 2 - (b - e) * (c - f))
      = (-a ^ 2 - b * c) + (-d ^ 2 - e * f) + (2 * a * d + b * f + c * e) := by
  ring

/-- The ellipticity criterion in Killing-pairing form: the difference of two
traceless directions is elliptic (`det > 0`) exactly when their pairing exceeds
minus the sum of their determinants. For two **hyperbolic** directions
(`det A₀, det B₀ < 0`) that threshold is positive, so alignment is required. -/
theorem sub_elliptic_iff_pairing_large (a b c d e f : ℝ) :
    0 < -(a - d) ^ 2 - (b - e) * (c - f)
      ↔ -((-a ^ 2 - b * c) + (-d ^ 2 - e * f)) < 2 * a * d + b * f + c * e := by
  rw [det_sub_traceless]
  constructor <;> intro h <;> linarith

/-- Two hyperbolic directions force a strictly positive alignment threshold, so
the difference cannot be elliptic "for free" — the pairing has to be large. This
is what makes the measured `2.107175 > 2.098162` a statement about the nucleons
rather than a generic fact. -/
theorem threshold_pos_of_both_hyperbolic
    {dA dB : ℝ} (hA : dA < 0) (hB : dB < 0) : 0 < -(dA + dB) := by
  linarith

end QOU.QBeta
