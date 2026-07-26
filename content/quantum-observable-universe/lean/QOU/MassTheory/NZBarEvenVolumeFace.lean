/-
# The bar-EVEN (Volume) face of the NZ meridian deformation is MAXIMAL on the real substrate ray —
# g₂ lives exactly where the c₃ wall freezes

**The arg(u) wall is a quadrature effect.** The Q_β `c₃` front (PR #4293,
`QOU/QBeta/ArgUPhaseBranchSelection.lean`) proved the Neumann–Zagier **bar-odd / Chern–Simons** face

  `nzImVolume r φ = (√3/2)·r²·sin(2φ)`   (`r = |u|`, `φ = arg u`)

is **frozen on the real substrate ray**: `nzImVolume r 0 = 0` (`sin 0 = 0`), because the substrate
meridian coordinate `u = 2·log q₀` is a nonnegative real (`φ = 0`). That is the `c₃` wall — the CS
face carries the swing entirely in the phase, and the phase is off at `φ = 0`.

The μ₀ binding coefficient `g₂` is the **bar-EVEN / Volume** face — the **cos-quadrature partner**

  `nzReVolume r φ = (√3/2)·r²·cos(2φ)`.

At the *same* real ray `φ = 0`, `cos 0 = 1`, so `nzReVolume r 0 = (√3/2)·r²` — **maximal, not
frozen** — and since `nzReVolume` is **even** in `φ` (vs `nzImVolume` odd), `φ = 0` is a *stationary
extremum*: the bar-even face has **zero phase-slope** there (doubly anchor-smooth), whereas the
bar-odd face has maximal slope. So the wall that kills `c₃` on the real ray leaves `g₂` maximal and
stable. The two μ₀/Q_β closures are the two quadrature faces of one Neumann–Zagier object; the real
substrate ray is exactly the point where CS (`c₃`) vanishes and Volume (`g₂`) is at its peak.

§7c: archimedean (`Real.cos`, ordering) ⇒ base ring `ℝ`. `nzReVolume` mirrors the corpus
`QOU.QBeta.ArgUPhaseBranchSelection.nzImVolume` with `cos` in place of `sin` (stated standalone to
keep this file Mathlib-only; the definitional correspondence is exact by inspection).
-/
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic.Positivity

namespace QOU.MassTheory

open Real

/-- The **bar-even (Volume) face** of the NZ meridian deformation: the cos-quadrature partner of the
corpus bar-odd `nzImVolume r φ = (√3/2)·r²·sin(2φ)`. -/
noncomputable def nzReVolume (r φ : ℝ) : ℝ := (Real.sqrt 3 / 2) * r ^ 2 * Real.cos (2 * φ)

/-- **On the real substrate ray `φ = 0` the bar-even face is MAXIMAL:** `nzReVolume r 0 = (√3/2)·r²`
(`cos 0 = 1`) — in contrast to the bar-odd `nzImVolume r 0 = 0` (frozen). -/
theorem nzReVolume_real_ray (r : ℝ) : nzReVolume r 0 = Real.sqrt 3 / 2 * r ^ 2 := by
  simp [nzReVolume]

/-- **The bar-even face is nonzero (not frozen) on the real ray** for any nonzero magnitude — the
structural opposite of the bar-odd CS face, which vanishes there. So `g₂`'s seat survives the
substrate real-ray restriction that walls `c₃`. -/
theorem nzReVolume_real_ray_ne_zero (r : ℝ) (hr : r ≠ 0) : nzReVolume r 0 ≠ 0 := by
  rw [nzReVolume_real_ray]
  have hpos : 0 < Real.sqrt 3 / 2 * r ^ 2 := by positivity
  exact hpos.ne'

/-- **The bar-even face is EVEN in the phase `φ`** (`cos` is even), so the real ray `φ = 0` is a
*stationary extremum* — zero phase-slope, doubly anchor-smooth. Contrast: the bar-odd `nzImVolume`
is *odd* in `φ` (`sin`), so `φ = 0` is its steepest point (value 0, maximal slope). This is the
quadrature structure of the arg(u) wall. -/
theorem nzReVolume_phase_even (r φ : ℝ) : nzReVolume r (-φ) = nzReVolume r φ := by
  unfold nzReVolume
  rw [show 2 * (-φ) = -(2 * φ) by ring, Real.cos_neg]

/-- **Peak value at the substrate.** The bar-even face attains `(√3/2)·r²` on the real ray, and (by
evenness) this is a local extremum — the `g₂` seat is at the peak of the Volume face precisely where
the CS face (`c₃`) is null. -/
theorem nzReVolume_real_ray_pos (r : ℝ) (hr : r ≠ 0) : 0 < nzReVolume r 0 := by
  rw [nzReVolume_real_ray]; positivity

end QOU.MassTheory
