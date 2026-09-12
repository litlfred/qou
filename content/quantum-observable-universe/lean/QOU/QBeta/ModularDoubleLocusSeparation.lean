/-
  The Faddeev modular involution `b² ↦ 1/b²` cannot bridge the `|q| = 1` fibre
  regime and the real-`q` substrate regime, because it fixes each of them.

  WHY THIS FILE EXISTS.  `qou-pdix` needs a transcendental carrier for the
  `Q_β` ladder's `α` eigenphase; route 5 of its route table names Faddeev's
  `Φ_b`, whose distinguishing feature over the compact `Φ_q` is the modular
  duality `b ↦ 1/b`, with

      q = exp(iπb²)      q̃ = exp(iπ/b²).

  "Attack B" proposed reading that involution as a BRIDGE: the eigenphase is
  natural on the elliptic `|q| = 1` fibre, the ladder is evaluated at real
  `q₀ > 1`, and the modular double would carry one to the other.

  WHAT IS PROVED HERE, and it is elementary on purpose.  The two regimes are
  cut out by

      |q| = 1                 ↔  `b²` real         (`InFibreLocus`)
      q real and positive     ↔  `b²` imaginary     (`InSubstrateLocus`,
                                                     principal branch)

  and complex inversion fixes the real axis and the imaginary axis SETWISE.  So
  each locus maps into itself and neither can be reached from the other:
  `modular_cannot_bridge`.  On the substrate locus inversion additionally flips
  the sign of `Im b²` (`substrate_inv_im_neg`), so it sends the `Im b² > 0`
  branch to its own reflection — the only motion it has there.

  The two loci meet only at `b² = 0`, which `FaddeevPhi.hb`'s `0 < Re b`
  excludes, so there is no shared point to pass through either
  (`loci_inter_eq_zero`).

  THIS IS THE CORPUS'S OWN SEPARATION.  `FaddeevPhi`'s class docstring already
  draws this line and records that only one side is discharged: "on the
  `Im b² > 0` substrate branch this is discharged by the modular-double product
  — see `QOU.MathlibExt.PhiBProd`; the `|q| = 1` fibre regime, real `b`, remains
  open."  The lemmas below say why no amount of modular duality closes that gap.

  SCOPE — this is a scope-(b) exclusion of ONE MECHANISM, not of `Φ_b`.  What is
  excluded is inversion-as-a-bridge.  `Φ_b`'s `b`-shift relation carries no
  non-perturbative `exp(-1/t)` scale and remains a live transcendental
  ingredient for branch 3 (the holonomy of an independently-defined connection).
  Companion measurement, including the quantitative prune of `q̃` as a carrier
  (375× too steep on the ladder's own log-slope constraint):
  `computations/qbeta/qbeta_pdix_modular_double_locus_probe.py`.

  -- Ref: [faddeev1995] Faddeev, Lett. Math. Phys. 34 (1995) 249.
-/
import Mathlib.Analysis.SpecialFunctions.Complex.Log

namespace QOU.QBeta.ModularDoubleLocusSeparation

open Complex

/-! ### The two loci -/

/-- The fibre / elliptic regime: `|q| = 1`, equivalently `b²` real.  Since
`q = exp(iπb²)` has `|q| = exp(-π Im b²)`, this is exactly `Im b² = 0`. -/
def InFibreLocus (w : ℂ) : Prop := w.im = 0

/-- The substrate regime on its principal branch: `q` real positive with
`Re b² = 0`, i.e. `b²` purely imaginary.  (`q = exp(iπb²)` is real positive iff
`Re b² ∈ 2ℤ`; the principal branch is the `0` cell, which is the one the
`arg b = π/4` substrate branch lands in.) -/
def InSubstrateLocus (w : ℂ) : Prop := w.re = 0

/-! ### Each locus is inversion-invariant -/

/-- Inversion fixes the real axis: the fibre locus maps into itself. -/
theorem fibre_inv_mem {w : ℂ} (h : InFibreLocus w) : InFibreLocus w⁻¹ := by
  simp only [InFibreLocus] at h ⊢
  rw [Complex.inv_im, h]
  simp

/-- Inversion fixes the imaginary axis: the substrate locus maps into itself. -/
theorem substrate_inv_mem {w : ℂ} (h : InSubstrateLocus w) : InSubstrateLocus w⁻¹ := by
  simp only [InSubstrateLocus] at h ⊢
  rw [Complex.inv_re, h]
  simp

/-- On the substrate locus inversion FLIPS the sign of `Im b²`.  So it carries
the `Im b² > 0` branch — the one `PhiBProd` supports — to its own reflection,
and that is the only motion it has there. -/
theorem substrate_inv_im_neg {w : ℂ} (h : InSubstrateLocus w) (hpos : 0 < w.im) :
    (w⁻¹).im < 0 := by
  simp only [InSubstrateLocus] at h
  rw [Complex.inv_im, Complex.normSq_apply, h]
  have hsq : (0 : ℝ) < 0 * 0 + w.im * w.im := by
    simpa using mul_pos hpos hpos
  exact div_neg_of_neg_of_pos (neg_neg_of_pos hpos) hsq

/-! ### Therefore the involution is not a bridge -/

/-- The two loci meet only at `0`.  `FaddeevPhi.hb` asserts `0 < Re b`, hence
`b ≠ 0` and `b² ≠ 0`, so no admissible `b` sits on both. -/
theorem loci_inter_eq_zero {w : ℂ} (hf : InFibreLocus w) (hs : InSubstrateLocus w) :
    w = 0 := by
  simp only [InFibreLocus] at hf
  simp only [InSubstrateLocus] at hs
  exact Complex.ext (by simpa using hs) (by simpa using hf)

/-- **Attack B's mechanism is excluded.**  For a nonzero `b²` in the fibre
locus, the modular partner `1/b²` is *still* in the fibre locus and is NOT in
the substrate locus.  Modular inversion therefore cannot carry the `|q| = 1`
elliptic regime to the real-`q` substrate. -/
theorem modular_cannot_bridge {w : ℂ} (hf : InFibreLocus w) (hw : w ≠ 0) :
    InFibreLocus w⁻¹ ∧ ¬ InSubstrateLocus w⁻¹ := by
  refine ⟨fibre_inv_mem hf, fun hs => ?_⟩
  have := loci_inter_eq_zero (fibre_inv_mem hf) hs
  exact hw (inv_eq_zero.mp this)

/-- The same statement from the substrate side: a nonzero purely-imaginary `b²`
has a purely-imaginary modular partner, never a real one.  So the substrate
cannot reach the fibre regime either — the exclusion is symmetric. -/
theorem modular_cannot_bridge' {w : ℂ} (hs : InSubstrateLocus w) (hw : w ≠ 0) :
    InSubstrateLocus w⁻¹ ∧ ¬ InFibreLocus w⁻¹ := by
  refine ⟨substrate_inv_mem hs, fun hf => ?_⟩
  have := loci_inter_eq_zero hf (substrate_inv_mem hs)
  exact hw (inv_eq_zero.mp this)

end QOU.QBeta.ModularDoubleLocusSeparation
