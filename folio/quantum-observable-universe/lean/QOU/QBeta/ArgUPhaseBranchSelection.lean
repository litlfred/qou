import Mathlib.Analysis.SpecialFunctions.Complex.Arg
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv
import Mathlib.Analysis.SpecialFunctions.Log.Basic

/-!
# The phase `arg(u)` channel at the real substrate ray — corrected quadrature
(sin → cos), and what survives of the "wall"

**CONVENTION CORRECTION (2026-07-27, bean `qou-u14x`).** The original version of
this file defined the bar-odd / Chern–Simons face as
`nzImVolume r φ = (√3/2)·r²·sin(2φ)`. The A-polynomial ground-truth computation
([`docs/audits/2026-07-27-nzImVolume-sincos-convention-bug.md`]) shows the
correct quadrature is **cos**: from `𝔙(u) = Vol + i·κ·u²` (the proved
`QOU.Knot.FigureEightComplexVolume.imV₄₁`, half-potential `κ = √3/4`; this file
keeps the full-potential normalisation `√3/2`),

`Im 𝔙 − 0 = (√3/2)·r²·cos(2φ)`,   `Re 𝔙 − Vol = −(√3/2)·r²·sin(2φ)`.

The original file's sin-form was the **Re**-face (up to sign), not the Im-face.
Consequences, stated plainly rather than patched around:

* **`nzImVolume_real_ray` inverts.** On the real ray `φ = 0` the bar-odd face is
  `(√3/2)·r²` — **positive and maximal**, not `0`. The old "S = 0 on the real
  ray" wall theorem was false; the amphichirality statement `Im 𝔙(0) = 0` holds
  at the complete point `u = 0`, not along the whole real ray.
* **The phase is stationary, not maximal-leverage.** `∂S/∂φ|₀ = 0` (cos is even);
  the old `√3·r²` slope belonged to the Re-face. Phase perturbations move the
  bar-odd face only at second order — the phase channel is *doubly* frozen:
  never displaced (`arg u = 0` at every real anchor, unchanged below) and
  stationary even if displaced infinitesimally.
* **What survives of the wall:** the anchor-swing of the bar-odd face is carried
  **entirely by the magnitude channel** (`anchor_swing_is_magnitude_only`),
  which #4288 proved anchor-smooth. The sign flip `S(muon) > 0 > S(proton)`
  therefore cannot come from smooth phase or magnitude perturbations at the
  real ray at all: reaching `S < 0` requires `cos(2φ) < 0`, i.e. crossing the
  diagonal `φ = π/4` by a *finite* rotation — a discrete branch/winding datum
  (the cusp-lattice slope of `QOU.QBeta.WindingLatticeNormForm`), not an
  infinitesimal q₀-sensitivity. `nzImVolume_quarter_turn` marks the diagonal:
  the quarter turn lands exactly on the zero.

The substrate-reality facts (`substrate_meridian_arg_zero`,
`anchor_phase_difference_zero`) are independent of the quadrature and unchanged.
No `c_k` value is produced; nothing inverts `Q_β`/CODATA; nothing is wired.

Base ring: archimedean (`Real.cos`, `Complex.arg`, ordering) ⇒ `ℝ` (§7c).

-- Ref: [neumann-zagier1985] https://doi.org/10.1016/0040-9383(85)90004-7
-- Ref: [leitner2026] docs/audits/2026-07-27-nzImVolume-sincos-convention-bug.md
-- Ref: [leitner2026] docs/audits/2026-07-25-argu-phase-branch-selection.md
-/

namespace QOU.QBeta.ArgUPhaseBranchSelection

open Real

/-- **Leading Neumann–Zagier bar-odd (Chern–Simons) face** in meridian polar
coordinates `(r, φ) = (|u|, arg u)`, corrected quadrature (bean `qou-u14x`):
`S = (√3/2)·r²·cos(2φ)`, from `𝔙 = Vol + iκu²` (full-potential normalisation). -/
noncomputable def nzImVolume (r φ : ℝ) : ℝ := (Real.sqrt 3 / 2) * r ^ 2 * Real.cos (2 * φ)

/-- **Real ray ⇒ bar-odd face maximal (corrected).** `cos 0 = 1`, so
`S(r, 0) = (√3/2)·r²` — positive for `r ≠ 0`, not zero. The old `S = 0` claim
was the sin-quadrature bug. -/
theorem nzImVolume_real_ray (r : ℝ) : nzImVolume r 0 = Real.sqrt 3 / 2 * r ^ 2 := by
  simp [nzImVolume]

/-- The bar-odd face is even in the phase: `φ = 0` is a stationary point. -/
theorem nzImVolume_phase_even (r φ : ℝ) : nzImVolume r (-φ) = nzImVolume r φ := by
  simp [nzImVolume, mul_comm]

/-- **The quarter turn lands on the diagonal zero.** `cos(π/2) = 0`: the
spin-dominated regime `S < 0` begins only past the finite rotation `φ = π/4`. -/
theorem nzImVolume_quarter_turn (r : ℝ) : nzImVolume r (Real.pi / 4) = 0 := by
  unfold nzImVolume
  rw [show 2 * (Real.pi / 4) = Real.pi / 2 by ring, Real.cos_pi_div_two, mul_zero]

/-- **Phase-sensitivity at `φ = 0` is ZERO (corrected).** The bar-odd face is
stationary in the phase at the real ray — the old `√3·r²` slope was the
Re-face's. Infinitesimal phase perturbations cannot move `S` at first order. -/
theorem nzImVolume_phase_hasDerivAt (r : ℝ) :
    HasDerivAt (fun φ => nzImVolume r φ) 0 0 := by
  have hinner : HasDerivAt (fun φ : ℝ => 2 * φ) 2 0 := by
    simpa using (hasDerivAt_id (0 : ℝ)).const_mul (2 : ℝ)
  have hcos : HasDerivAt (fun φ : ℝ => Real.cos (2 * φ))
      (-Real.sin (2 * 0) * 2) 0 := (Real.hasDerivAt_cos (2 * 0)).comp 0 hinner
  have hfull := hcos.const_mul (Real.sqrt 3 / 2 * r ^ 2)
  have heq : Real.sqrt 3 / 2 * r ^ 2 * (-Real.sin (2 * 0) * 2) = 0 := by
    rw [mul_zero, Real.sin_zero]; ring
  rw [heq] at hfull
  exact hfull

/-- `∂S/∂φ|₀ = 0`. -/
theorem nzImVolume_phase_deriv (r : ℝ) :
    deriv (fun φ => nzImVolume r φ) 0 = 0 :=
  (nzImVolume_phase_hasDerivAt r).deriv

/-- **The substrate freezes the phase** (unchanged by the correction). The
substrate meridian coordinate is `u = 2·log q₀`, a nonnegative real for
`q₀ ≥ 1`, so `arg(u) = 0`. -/
theorem substrate_meridian_arg_zero {q₀ : ℝ} (hq : 1 ≤ q₀) :
    Complex.arg ((2 * Real.log q₀ : ℝ) : ℂ) = 0 := by
  apply Complex.arg_ofReal_of_nonneg
  have : (0 : ℝ) ≤ Real.log q₀ := Real.log_nonneg hq
  positivity

/-- **Zero phase displacement between anchors** (unchanged). -/
theorem anchor_phase_difference_zero {qp qm : ℝ} (hp : 1 ≤ qp) (hm : 1 ≤ qm) :
    Complex.arg ((2 * Real.log qp : ℝ) : ℂ)
      - Complex.arg ((2 * Real.log qm : ℝ) : ℂ) = 0 := by
  rw [substrate_meridian_arg_zero hp, substrate_meridian_arg_zero hm, sub_self]

/-- **The corrected wall: the anchor-swing is pure magnitude.** At two real
anchors the phase is `0` at both, and the bar-odd swing collapses to the
magnitude difference `(√3/2)·(rp² − rm²)` — the channel #4288 proved
anchor-smooth. The phase contributes exactly nothing; and by
`nzImVolume_phase_deriv` it could not contribute at first order even if
perturbed. The sign flip is therefore out of reach of both smooth channels. -/
theorem anchor_swing_is_magnitude_only {qp qm : ℝ} (hp : 1 ≤ qp) (hm : 1 ≤ qm)
    (rp rm : ℝ) :
    nzImVolume rp (Complex.arg ((2 * Real.log qp : ℝ) : ℂ))
      - nzImVolume rm (Complex.arg ((2 * Real.log qm : ℝ) : ℂ))
      = Real.sqrt 3 / 2 * (rp ^ 2 - rm ^ 2) := by
  rw [substrate_meridian_arg_zero hp, substrate_meridian_arg_zero hm,
    nzImVolume_real_ray, nzImVolume_real_ray]
  ring

/-- **The chain-rule crux (doubly zero after the correction).** The phase-channel
contribution `(∂S/∂φ)·Δφ` vanishes for two independent reasons: the displacement
`Δφ = 0` (real anchors), and the sensitivity `∂S/∂φ|₀ = 0` (stationarity). -/
theorem phase_sensitivity_times_frozen_displacement (r Δφ : ℝ) (hfrozen : Δφ = 0) :
    (deriv (fun φ => nzImVolume r φ) 0) * Δφ = 0 := by
  rw [hfrozen, mul_zero]

end QOU.QBeta.ArgUPhaseBranchSelection
