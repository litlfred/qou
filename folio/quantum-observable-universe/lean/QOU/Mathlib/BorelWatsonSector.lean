/-
  Watson-uniqueness brick 4b-i — the fractional-power sector map (bean el8w
  tranche 5).

  The final Watson transport needs a sector of opening `> π` to be carried into
  a half-plane, because the Phragmén–Lindelöf engine (brick 3) needs the
  STRETCHED-exponential decay that only a `>π` opening produces. The carrier is
  the fractional power `z ↦ z^t` with `t = 1/β < 1` (β = opening/π > 1): it
  contracts the angular opening `βπ` down to `π` (a half-plane) while amplifying
  an `exp(−c/|z|)` bound to the stretched `exp(−c|w|^β)`.

  This file proves the SECTOR-GEOMETRY core of that carrier, sorry-free — the
  fact that `z^t` sends the sector `{|arg z| < π/(2t)}` into the open right
  half-plane `{re > 0}`. The clean route avoids any branch-cut `arg`-of-`cpow`
  identity: `z^t = exp(log z · t)` and `Complex.exp_re` give directly

      Re(z^t) = ‖z‖^t · cos(t · arg z),

  which is positive exactly when `|t · arg z| < π/2` — i.e. on the sector
  `|arg z| < π/(2t)`. The half-plane is opening `π`; the source sector has
  opening `π/t = βπ > π`, so this is the opening-`>π` → half-plane contraction.

  Remaining for full Watson (honestly, not faked): the holomorphy of `z^t` on
  the sector (free from `AnalyticAt.cpow`, a follow-up once its olean cone is
  built) and the boundary/`DiffContOnCl` limiting argument at `0`/`∞`. Scoped in
  the el8w tranche 5 bean.

  Archimedean (ℂ): genuinely archimedean — `Complex.cpow`, `Complex.exp`,
  `Real.cos`, ordering.

  -- Ref: [leitner2026] bean el8w tranche 5 — Watson uniqueness brick 4b-i
-/

import Mathlib.Analysis.SpecialFunctions.Pow.Complex
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.SpecialFunctions.Complex.Analytic

namespace QOU.Mathlib.Borel

open Complex Set
open scoped Real

/-- `Re(z^t) = ‖z‖^t · cos(t · arg z)` for `z ≠ 0` and real `t`: the real part
    of a fractional power, computed via `z^t = exp(log z · t)` and
    `Complex.exp_re`. No branch-cut `arg`-of-`cpow` identity needed. -/
theorem re_cpow_ofReal {z : ℂ} {t : ℝ} (hz : z ≠ 0) :
    (z ^ (t : ℂ)).re
      = Real.exp (Real.log ‖z‖ * t) * Real.cos (z.arg * t) := by
  rw [Complex.cpow_def_of_ne_zero hz, Complex.exp_re]
  have hre : (Complex.log z * (t : ℂ)).re = Real.log ‖z‖ * t := by
    rw [Complex.mul_re, Complex.log_re, Complex.ofReal_re, Complex.ofReal_im,
      mul_zero, sub_zero]
  have him : (Complex.log z * (t : ℂ)).im = z.arg * t := by
    rw [Complex.mul_im, Complex.log_im, Complex.ofReal_im, Complex.ofReal_re,
      mul_zero, zero_add]
  rw [hre, him]

/-- **The fractional-power sector map (brick 4b-i).** For `0 < t` and `z ≠ 0` in
    the sector `|arg z| < π/(2t)`, the fractional power `z^t` lands in the open
    right half-plane. Since the source sector has opening `π/t` (which is `> π`
    precisely when `t < 1`), this is the opening-`>π` → half-plane contraction
    the Watson transport needs. -/
theorem re_cpow_pos_of_abs_arg_lt {z : ℂ} {t : ℝ} (hz : z ≠ 0) (ht : 0 < t)
    (harg : |z.arg| < Real.pi / (2 * t)) :
    0 < (z ^ (t : ℂ)).re := by
  rw [re_cpow_ofReal hz]
  apply mul_pos (Real.exp_pos _)
  apply Real.cos_pos_of_mem_Ioo
  have hbound : |z.arg * t| < Real.pi / 2 := by
    rw [abs_mul, abs_of_pos ht]
    have h := mul_lt_mul_of_pos_right harg ht
    have hsimp : Real.pi / (2 * t) * t = Real.pi / 2 := by
      field_simp [ht.ne']
    rwa [hsimp] at h
  exact abs_lt.mp hbound

/-- The sector `{z ≠ 0 : |arg z| < π/(2t)}` is mapped by `z ↦ z^t` into the open
    right half-plane `{re > 0}` — the `MapsTo` form the Watson transport
    consumes. -/
theorem sector_cpow_mapsTo {t : ℝ} (ht : 0 < t) :
    MapsTo (fun z : ℂ => z ^ (t : ℂ))
      {z : ℂ | z ≠ 0 ∧ |z.arg| < Real.pi / (2 * t)} {z : ℂ | 0 < z.re} :=
  fun _ hz => re_cpow_pos_of_abs_arg_lt hz.1 ht hz.2

/-- **Holomorphy of the fractional power** `z ↦ z^t` on the slit plane
    (`ℂ ∖ ℝ_{≤0}`), which contains every sector of opening `< 2π` about the
    positive axis. A direct instance of `AnalyticAt.cpow` (`z^t = exp(t log z)`,
    `log` analytic off the slit). The second geometric ingredient of the Watson
    carrier, alongside `sector_cpow_mapsTo`. -/
theorem analyticAt_cpow_const {t : ℝ} {z : ℂ} (hz : z ∈ slitPlane) :
    AnalyticAt ℂ (fun w : ℂ => w ^ (t : ℂ)) z :=
  analyticAt_id.cpow analyticAt_const hz

end QOU.Mathlib.Borel
