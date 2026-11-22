/-
# The bar-EVEN (Volume) face of the NZ meridian deformation — corrected quadrature
(cos → −sin): the Volume-deviation VANISHES on the real substrate ray

**CONVENTION CORRECTION (2026-07-27, bean `qou-u14x`).** This file's original
version assigned `cos(2φ)` to the Volume face and its companion
(`QOU/QBeta/ArgUPhaseBranchSelection.lean`) assigned `sin(2φ)` to the CS face.
The A-polynomial ground truth
([`docs/audits/2026-07-27-nzImVolume-sincos-convention-bug.md`]) shows the two
quadratures were SWAPPED: from `𝔙(u) = Vol + i·κ·u²`,

  `Im 𝔙 = (√3/2)·r²·cos(2φ)`   (CS face — even, maximal-and-stationary at φ=0),
  `Re 𝔙 − Vol = −(√3/2)·r²·sin(2φ)`   (Volume-DEVIATION face — odd, zero at φ=0).

So on the real substrate ray it is the **CS face** that is maximal and doubly
anchor-smooth, and the **Volume-deviation** that vanishes with maximal phase
slope — the opposite of this file's original narrative. The physical reading
this file used to carry ("g₂ lives where c₃ freezes": g₂ maximal / CS frozen at
φ=0) does NOT survive the correction as stated; what replaces it is: at φ = 0
the total Volume face is the undeformed `Vol` exactly (deviation = 0), and the
CS face is the maximal `(√3/2)r²`. The g₂ narrative must be re-derived against
the corrected quadratures — tracked in bean `qou-u14x`; no g₂ claim is asserted
here.

§7c: archimedean (`Real.sin`, ordering) ⇒ base ring `ℝ`.

-- Ref: [neumann-zagier1985] https://doi.org/10.1016/0040-9383(85)90004-7
-- Ref: [leitner2026] docs/audits/2026-07-27-nzImVolume-sincos-convention-bug.md
-/
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic.Positivity

namespace QOU.MassTheory

open Real

/-- The **bar-even Volume-DEVIATION face** of the NZ meridian deformation
(corrected quadrature): `Re 𝔙 − Vol = −(√3/2)·r²·sin(2φ)`. Odd in `φ`;
vanishes identically on the real ray. -/
noncomputable def nzReVolume (r φ : ℝ) : ℝ := -((Real.sqrt 3 / 2) * r ^ 2 * Real.sin (2 * φ))

/-- **Real ray ⇒ Volume-deviation off (corrected).** `sin 0 = 0`: on the real
substrate ray the Volume face is the undeformed `Vol` exactly. The old
`nzReVolume r 0 = (√3/2)r²` (and its `≠ 0` / `> 0` corollaries) belonged to the
CS face. -/
theorem nzReVolume_real_ray (r : ℝ) : nzReVolume r 0 = 0 := by
  simp [nzReVolume]

/-- The Volume-deviation face is **odd** in the phase (the CS face is the even
one) — the quadrature signature that identifies which face is which. -/
theorem nzReVolume_phase_odd (r φ : ℝ) : nzReVolume r (-φ) = -nzReVolume r φ := by
  simp [nzReVolume, mul_comm]

end QOU.MassTheory
