import Mathlib.Analysis.SpecialFunctions.Complex.Arg
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv
import Mathlib.Analysis.SpecialFunctions.Log.Basic

/-!
# The phase `arg(u)` branch-selection channel is FROZEN on the real substrate ray
— the last seat of the c₃ bar-odd anchor-swing is a WALL, not a handle

**The c₃ bar-odd anchor-carrier question, closed at its final seat.**

A chain of proved exclusions collapsed the seat of `c₃`'s percent-level bar-odd
anchor-swing to a single channel — the **phase** `arg(u)` of the Neumann–Zagier
meridian-deformation coordinate `u`:

* `C1` (`QOU.QBeta.BarOddAntisymOffDiagonal`, #4282, sorry-free): the bar-odd datum
  is the ι-odd antisymmetric off-diagonal `ω(β,p,q)=β·p−β⁻¹·q`, **anchor-smooth**
  (4.56 ppm swing across the muon↔proton `q₀` anchors).
* `#4288` (`QOU.QBeta.MeridianHolonomyAnchorCarrier`, sorry-free): the exact boost-
  hyperbola bound `(barEven/barOdd)² = 1 + 4/barOdd²` forces amplification `ρ ≥ N`
  to require `barOdd² ≤ 4/(N²−1)` — a large **magnitude** amplification needs `q`
  within `~3×10⁻⁷` of the compact locus `q=±1`; the substrate is `0.11` away, so the
  `S ∝ |u|²` **magnitude** channel is anchor-smooth (5.5 orders too far).

The residual was localized to the **phase** `arg(u)` — the branch-selection of the
open `conj:algebraic-geometric-dilog-equivalence`. `CuspShapeBarParity`'s degenerate-
branch analysis showed: the figure-eight gluing `(z(z−1))²=1` factors into the
**cusp** branch (`z²−z+1=0`, `ω=e^{iπ/3}`, `barOdd²=−3`, hyperbolic, `Vol≠0`) and
the **golden** branch (`z²−z−1=0`, `φ=(1+√5)/2`, real, `Vol=0`); seeding Thurston's
Newton with a **real** substrate pole flows to the golden (real) branch — only a
**phase** rotates the seed onto the cusp branch.

## The result — the phase is a live, independent, maximal-leverage DOF that the real
## substrate never MOVES ⇒ zero anchor-swing

Write the leading Neumann–Zagier imaginary complex-volume (the bar-odd / Chern–Simons
`S = Im 𝔙`) in the meridian-deformation polar coordinates `(r, φ) = (|u|, arg u)`.
From the derived `u=0` quadratic branch (`𝔙(u) ≈ 𝔙(0) − (τ/4)u²`, cusp modulus
`τ = 2√−3 = barOdd(ω)`, amphichiral base `Im 𝔙(0)=0`), the corpus-derived leading
form is (`docs/audits/2026-07-11-c3-wall-branch-structure.md §2`):

`nzImVolume r φ = (√3/2)·r²·sin(2φ)`.

Three facts pin the verdict:

* `nzImVolume_real_ray` — on the real ray `φ = 0`, `S = 0` for **every** magnitude
  `r`. This is the #3654 amphichirality `Im 𝔙(real) = 0`, recovered from the phase
  formula: the CS is carried **entirely** by the phase `sin(2φ)`, and it is off at
  `φ=0`.
* `nzImVolume_quarter_turn` / `nzImVolume_phase_hasDerivAt` — the phase is a
  **maximal-leverage, independent DOF**: a quarter turn `φ:0↦π/4` swings `S` across
  its **full** `(√3/2)r²` range, and the phase-sensitivity at `φ=0` is
  `∂S/∂φ = √3·r² ≠ 0`. This sensitivity is **NOT** bounded by #4288's boost-
  hyperbola magnitude ratio `ρ = barEven/barOdd` — phase and magnitude are
  genuinely independent degrees of freedom (the handle the search hoped for).
* `substrate_meridian_arg_zero` / `anchor_phase_difference_zero` — **BUT** the
  substrate meridian coordinate is `u = 2·log q₀`, a **nonnegative real** for the
  physical `q₀ ≥ 1` (the meridian holonomy is multiplication by the real `q₀`), so
  its complex phase is `arg(u) = 0` at **every** anchor. Hence `Δ(arg u) = 0`
  between the proton and muon anchors.

The composition is the **wall** (`phase_channel_anchor_swing_zero`): the phase-
channel anchor-swing is `(∂S/∂φ)·Δφ = (√3 r²)·0 = 0`, **independent of how large
the phase-sensitivity is**. The real substrate freezes `arg(u)` at `0`; the same
reality of `q₀` that puts the pole on the degenerate golden branch (`Vol=0`) also
pins the phase, killing its anchor-swing.

## Verdict — WALL (scope-(a)), confirming and completing the 2026-07-12 capstone

This is **not** a handle. The phase `arg(u)` cannot carry the `c₃` anchor-swing at
the observable (real-`q₀`) level — not because it is bounded (it is not; it is a
maximal-leverage DOF), but because the real substrate never moves it. Combined with
`#4282` (`ω`-home anchor-smooth) and `#4288` (magnitude bounded), **every**
categorical/geometric DOF at real `q₀` supplies zero-or-negligible anchor-swing, so
the `c₃` anchor-dependence is genuinely **non-categorical** — a fibre-level
`ε = Im(q) ≠ 0` (`#3636`, `fig8Trace_im_odd`: `sign S = sign ε`, no real `q₀`
produces the flip) realized through the `1/u³` ladder **representation** (`#3636`,
`#3654`, `#4064`-refutation), exactly the merged 2026-07-12 wall-resolution capstone.
The observable-level phase is frozen; the phase DOF lives at the fibre level where
`Im q` is free, which the observable anchor comparison cannot access.

**No `c_k` value is produced; nothing inverts `Q_β`/CODATA; nothing is wired. The
branch-selection conjecture `conj:algebraic-geometric-dilog-equivalence` remains
open — what is proved is that whatever branch it selects, the phase it would supply
is frozen at the observable level and cannot be the seat of the observable swing.**

Base ring: `nzImVolume` and its phase lemmas are over `ℝ` (genuinely archimedean —
`Real.sin`, `Real.log`, `Complex.arg`, ordering `1 ≤ q₀`), the correct wall
placement (the observable / archimedean side of the `Im q` wall).

-- Ref: [neumann-zagier1985] https://doi.org/10.1016/0040-9383(85)90004-7
-- Ref: [manuscript] conj:algebraic-geometric-dilog-equivalence
-- Ref: [manuscript] docs/audits/2026-07-25-argu-phase-branch-selection.md
-- Ref: [manuscript] docs/audits/2026-07-11-c3-wall-branch-structure.md
-- Ref: [manuscript] docs/audits/2026-07-12-c3-wall-resolution-capstone.md
-/

namespace QOU.QBeta.ArgUPhaseBranchSelection

open Real

/-- **Leading Neumann–Zagier imaginary complex-volume** `S = Im 𝔙` in the meridian-
deformation polar coordinates `(r, φ) = (|u|, arg u)`. From the derived `u=0`
quadratic branch `𝔙(u) ≈ 𝔙(0) − (τ/4)u²` with cusp modulus `τ = 2√−3` and
amphichiral base `Im 𝔙(0)=0` (`docs/audits/2026-07-11-c3-wall-branch-structure.md`):
`S = (√3/2)·|u|²·sin(2·arg u)`. The Chern–Simons / bar-odd part is carried
**entirely** by the phase `sin(2φ)`. -/
noncomputable def nzImVolume (r φ : ℝ) : ℝ := (Real.sqrt 3 / 2) * r ^ 2 * Real.sin (2 * φ)

/-- **Real ray ⇒ CS off (amphichirality).** On the real ray `arg u = 0` the bar-odd
`S = 0` for **every** magnitude `r` — the whole `Im 𝔙` is carried by the phase, and
it vanishes at `φ=0`. This recovers the #3654 amphichirality `Im 𝔙(real) = 0` from
the phase formula. -/
theorem nzImVolume_real_ray (r : ℝ) : nzImVolume r 0 = 0 := by
  simp [nzImVolume]

/-- **The phase is a maximal-leverage DOF.** A quarter phase-turn `φ : 0 ↦ π/4`
swings `S` across its **full** `(√3/2)·r²` range (`sin(π/2)=1`). So the phase alone
moves the bar-odd `S` over its entire amplitude — it is a live, high-leverage
degree of freedom, **independent** of the magnitude `r`. -/
theorem nzImVolume_quarter_turn (r : ℝ) :
    nzImVolume r (Real.pi / 4) = Real.sqrt 3 / 2 * r ^ 2 := by
  unfold nzImVolume
  rw [show 2 * (Real.pi / 4) = Real.pi / 2 by ring, Real.sin_pi_div_two, mul_one]

/-- **Phase-sensitivity at `φ=0` is `√3·r²` (exact, nonzero).** The derivative of `S`
along the phase at the real ray is `∂S/∂φ|₀ = √3·r²`. This is the intrinsic phase
sensitivity — nonzero for `r ≠ 0` and **NOT** bounded by the boost-hyperbola
magnitude ratio `ρ = barEven/barOdd` of #4288 (which bounds only the `|u|`-log-
derivative). Phase and magnitude are independent DOF. -/
theorem nzImVolume_phase_hasDerivAt (r : ℝ) :
    HasDerivAt (fun φ => nzImVolume r φ) (Real.sqrt 3 * r ^ 2) 0 := by
  have hinner : HasDerivAt (fun φ : ℝ => 2 * φ) 2 0 := by
    simpa using (hasDerivAt_id (0 : ℝ)).const_mul (2 : ℝ)
  have hsin : HasDerivAt (fun φ : ℝ => Real.sin (2 * φ))
      (Real.cos (2 * 0) * 2) 0 := (Real.hasDerivAt_sin (2 * 0)).comp 0 hinner
  have hfull := hsin.const_mul (Real.sqrt 3 / 2 * r ^ 2)
  have heq : Real.sqrt 3 / 2 * r ^ 2 * (Real.cos (2 * 0) * 2) = Real.sqrt 3 * r ^ 2 := by
    rw [mul_zero, Real.cos_zero]; ring
  rw [heq] at hfull
  exact hfull

/-- **The phase-derivative value.** `∂S/∂φ|₀ = √3·r²`. -/
theorem nzImVolume_phase_deriv (r : ℝ) :
    deriv (fun φ => nzImVolume r φ) 0 = Real.sqrt 3 * r ^ 2 :=
  (nzImVolume_phase_hasDerivAt r).deriv

/-- **The substrate freezes the phase.** The substrate meridian coordinate is
`u = 2·log q₀`, a **nonnegative real** for the physical `q₀ ≥ 1` (the meridian
holonomy is multiplication by the real `q₀`), so its complex phase is `arg(u) = 0`.
This is what pins `φ = 0`. -/
theorem substrate_meridian_arg_zero {q₀ : ℝ} (hq : 1 ≤ q₀) :
    Complex.arg ((2 * Real.log q₀ : ℝ) : ℂ) = 0 := by
  apply Complex.arg_ofReal_of_nonneg
  have : (0 : ℝ) ≤ Real.log q₀ := Real.log_nonneg hq
  positivity

/-- **Zero phase displacement between anchors.** Both anchors are real `q₀ ≥ 1`, so
`arg(u)=0` at each ⇒ `Δ(arg u) = 0`. The real substrate does not move the phase. -/
theorem anchor_phase_difference_zero {qp qm : ℝ} (hp : 1 ≤ qp) (hm : 1 ≤ qm) :
    Complex.arg ((2 * Real.log qp : ℝ) : ℂ)
      - Complex.arg ((2 * Real.log qm : ℝ) : ℂ) = 0 := by
  rw [substrate_meridian_arg_zero hp, substrate_meridian_arg_zero hm, sub_self]

/-- **The WALL — the phase channel supplies EXACTLY zero anchor-swing.** Evaluating
the bar-odd `S` at two real anchors (arbitrary magnitudes `rp, rm` — the #4288-
bounded `|u|`), through the phase-frozen coordinate `φ = arg(u) = 0`, the anchor-
swing of `S` is exactly `0`. The phase-sensitivity `∂S/∂φ = √3·r²` is nonzero and
unbounded by #4288, yet contributes nothing because `Δ(arg u) = 0`: the real
substrate never moves the phase. -/
theorem phase_channel_anchor_swing_zero {qp qm : ℝ} (hp : 1 ≤ qp) (hm : 1 ≤ qm)
    (rp rm : ℝ) :
    nzImVolume rp (Complex.arg ((2 * Real.log qp : ℝ) : ℂ))
      - nzImVolume rm (Complex.arg ((2 * Real.log qm : ℝ) : ℂ)) = 0 := by
  rw [substrate_meridian_arg_zero hp, substrate_meridian_arg_zero hm,
    nzImVolume_real_ray, nzImVolume_real_ray, sub_self]

/-- **The chain-rule crux, isolated.** The phase-channel contribution to the anchor-
swing is `(∂S/∂φ)·Δφ`. Even with the maximal-leverage sensitivity `∂S/∂φ = √3·r²`,
a **frozen** phase (`Δφ = 0`) contributes zero. This is the precise sense in which
the phase, though a live independent DOF, is a **wall** and not a handle: it is not
bounded — it is simply not displaced by the real anchors. -/
theorem phase_sensitivity_times_frozen_displacement (r Δφ : ℝ) (hfrozen : Δφ = 0) :
    (deriv (fun φ => nzImVolume r φ) 0) * Δφ = 0 := by
  rw [hfrozen, mul_zero]

end QOU.QBeta.ArgUPhaseBranchSelection
