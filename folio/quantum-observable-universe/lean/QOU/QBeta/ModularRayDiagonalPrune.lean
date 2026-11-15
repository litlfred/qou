import QOU.QBeta.ObservableComplexVolumeVsFullPotential

set_option autoImplicit false

/-!
# QOU.QBeta.ModularRayDiagonalPrune — the substrate ray is the diagonal (A2)

The A2 modular-involution prune (bean `qou-x341`, 2026-08-15 attack-options
ledger): a proved constraint on the `u(q₀)` argument BEFORE any scan.

The corpus's fibre→observable bridge sets the substrate fluctuation variable
imaginary, `2πb² = i·ln q₀`, i.e. `b = √(ln q₀/2π)·e^{iπ/4}`
(`OhtsukiTowerBarParity`, header) — so `b²` is purely imaginary and the
substrate `b` sits ON the ray `arg = π/4`. This file proves what that
implies for the corrected NZ leading form `Im 𝔙(u) = κ_pot·(Re²u − Im²u)`:

* `Re²u − Im²u = Re(u²)` (`imComplexVolume_eq_sq_re`), so the diagonal
  vanishing locus `|Re u| = |Im u|` is exactly `Re(u²) = 0`;
* the substrate-ray condition `Re(b²) = 0` therefore puts every REAL
  multiple of `b` on that locus: `Im 𝔙(b·t) = 0` for all real `t`
  (`imCV_zero_on_substrate_ray`);
* the modular involution `b ↦ b⁻¹` preserves the condition
  (`inv_preserves_ray`): it swaps the two diagonals `arg = ±π/4`, so the
  excluded locus is self-duality-symmetric.

**Prune (scope-(a), stated as the theorems above).** Any candidate
deformation family of the form `u(q) = b(q)·t(q)` with `t(q)` REAL and
`b(q)` on the substrate ray has leading `Im 𝔙 ≡ 0` identically — it cannot
produce ANY nonzero leading-order `S`, independent of the (conditional)
sign-flip premise. A viable `u(q₀)` must leave the substrate ray by a
non-real scaling, not merely rescale along it. This complements the
real-seed scope-(b) exclusion (`NewtonRealityInvariance`): the real axis
and the substrate diagonal ray are BOTH now proof-excluded as leading-order
`S` carriers.

## Honesty

The substrate-ray condition `(b²).re = 0` is an explicit hypothesis (the
`2πb² = i·ln q₀` bridge relation is corpus-established prose + Lean
elsewhere; this file does not re-derive it). Nothing here constructs
`u(q₀)`, decides the A-binary (`TauNormalizationChoice`), or touches the
open link (`qou-82w7`).

## References

- [neumann-zagier1985] Neumann & Zagier, "Volumes of hyperbolic
  three-manifolds," Topology 24 (1985). https://doi.org/10.1016/0040-9383(85)90004-7
- [leitner2026] QOU/QBeta/OhtsukiTowerBarParity.lean (the imaginary-substrate bridge);
  docs/audits/2026-07-26-sdeformed-channel-signflip.md (the corrected leading form).
-/

namespace QOU.QBeta.ModularRayDiagonalPrune

open QOU.QBeta.ObservableComplexVolumeVsFullPotential

/-- The corrected leading form reads off the real part of `u²`:
`Re²u − Im²u = Re(u²)`. The diagonal locus `|Re u| = |Im u|` is exactly
`Re(u²) = 0`. -/
theorem imComplexVolume_eq_sq_re (u : ℂ) :
    imComplexVolume u = kappaCV * (u ^ 2).re := by
  unfold imComplexVolume
  congr 1
  simp [sq, Complex.mul_re]

/-- **The substrate ray is the diagonal.** If `b² ` is purely imaginary (the
`2πb² = i·ln q₀` substrate condition), every real multiple of `b` lies on the
diagonal vanishing locus of the leading form: `Im 𝔙(b·t) = 0` for all real
`t`. A real-scaling family along the substrate ray carries NO leading-order
`S`. -/
theorem imCV_zero_on_substrate_ray {b : ℂ} (hb : (b ^ 2).re = 0) (t : ℝ) :
    imComplexVolume (b * (t : ℂ)) = 0 := by
  rw [imComplexVolume_eq_sq_re]
  have : (b * (t : ℂ)) ^ 2 = (t : ℂ) ^ 2 * b ^ 2 := by ring
  rw [this]
  have hre : ((t : ℂ) ^ 2 * b ^ 2).re = (t : ℝ) ^ 2 * (b ^ 2).re := by
    have h2 : ((t : ℂ) ^ 2) = ((t ^ 2 : ℝ) : ℂ) := by push_cast; ring
    rw [h2, Complex.re_ofReal_mul]
  rw [hre, hb, mul_zero, mul_zero]

/-- **The modular involution preserves the ray condition.** `b ↦ b⁻¹` maps
`arg = π/4` to `arg = −π/4` — the other diagonal — and purely-imaginary
squares stay purely imaginary: the excluded locus is `b ↔ 1/b` symmetric,
as the `Φ_b = Φ_{1/b}` self-duality requires. -/
theorem inv_preserves_ray {b : ℂ} (hb : (b ^ 2).re = 0) :
    ((b⁻¹) ^ 2).re = 0 := by
  rw [inv_pow, Complex.inv_re, hb, zero_div]

end QOU.QBeta.ModularRayDiagonalPrune
