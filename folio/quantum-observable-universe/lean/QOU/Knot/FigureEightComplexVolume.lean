/-
  Figure-eight (4₁) deformed complex volume 𝔙₄₁(u) = Vol(u) + i·CS(u) — the
  concrete Neumann–Zagier leading form that realizes the abstract `V` field of
  the keystone class `QOU.QBeta.PhiBSArgumentIdentification.SDeformedVolumeChannel`.

  GOAL (bean qou-6s8k, T1 of docs/coordination/keystone-sdeformedvolume-channel-attack.md).
  The keystone §3b class carries `V : ℂ → ℂ` — the figure-eight deformed complex
  volume — as an ABSTRACT field. This file makes it CONCRETE, reducing the class's
  open surface from {u, V, S_eq} to {u, S_eq}. `V₄₁` is assembled from the
  figure-eight geometry ALONE (Thurston gluing / the CCGLS A-polynomial), NOT
  fitted to any S target (anti-fit). No `SDeformedVolumeChannel` instance is
  fabricated — `u(q₀)` and `S_eq` stay OPEN (anti-laundering).

  THE LITERATURE OBJECT (Gukov 2003; H. Murakami; Ohtsuki 2016; Murakami–Yokota).
  The generalized/parametrized volume conjecture for 4₁ is a THEOREM:
        J_N(4₁; e^{(2πi+u)/N}) → 𝔙(u) = Vol(u) + i·CS(u),
  the complex volume of the u-deformed knot (u = log meridian holonomy). Near the
  complete structure it is the Neumann–Zagier series. The leading term is fixed by
  the figure-eight CUSP MODULUS, the leading longitude coefficient
        τ = ± i·√3   (PURELY IMAGINARY, ℚ(√−3); v(u) = τ·u + O(u³)),
  recognised exactly from the A-polynomial by
  `computations/probes/qbeta_nz_even_series_fourone_probe.py` (τ = (0,∓1,1)).
  With the NZ relation 𝔙′(u) ∝ v(u) (real proportionality), the leading
  complex-volume coefficient `a₂ = 𝔙″(0)/2` is PURELY IMAGINARY, `a₂ = i·√3/4`, so

        𝔙₄₁(u) = Vol(4₁) + i·(√3/4)·u² + O(u⁴)          (even; O(u⁴) even),
        Vol(4₁) = 2·Cl₂(π/3)  (QOU.Knot.FigureEightVolume.VOL_4_1),
        Im 𝔙₄₁(u) = (√3/4)·Re(u²) = (√3/4)·(Re²u − Im²u).

  This file DEFINES `V₄₁` as this leading NZ form (the sole geometric datum being
  the cusp modulus √3/4 = sin(π/3) = Im ω, ω = e^{iπ/3}; NOT a fit). The exact
  literature object differs by an EVEN O(u⁴) tail (`QOU.Knot.NeumannZagierParity`:
  the classical potential is even, no odd rung), carried as a cited residual — it
  does not change the sign structure of `Im 𝔙₄₁` established here.

  WHAT IS PROVED SORRY-FREE:
   * `V₄₁_zero_re`     — 𝔙₄₁(0) on the Vol axis = 2·Cl₂(π/3) (EXACT, since a₂ is
                         purely imaginary: no residual needed here);
   * `V₄₁_even`        — 𝔙₄₁(−u) = 𝔙₄₁(u) (Neumann–Zagier evenness), and
                         `nzPoly₄₁_no_u3` — no u³ rung, via the proved
                         `NeumannZagierParity.no_cubic_rung` on the concrete
                         polynomial;
   * `imV₄₁`           — Im 𝔙₄₁(u) = (√3/4)(Re²u − Im²u): the CS part is a
                         HARMONIC quadratic form vanishing on the DIAGONALS
                         |Re u| = |Im u|, NOT on the axes;
   * `imV₄₁_pos_iff`, `signflip_forces_diagonal_cross`, `f3_re_linear_same_sign`
                       — the T2 sign-flip invariant: because Im 𝔙₄₁ = κ(Re²−Im²)
                         with κ>0, the measured flip S(muon)>0>S(proton) FORCES
                         u(q₀) to cross the diagonal |Re u|=|Im u|; the #3773
                         "surviving" family F3 (one component linear-through-zero,
                         the other anchor-constant) keeps both anchors on the SAME
                         side of the diagonal, so it CANNOT sign-flip (companion
                         probe `sdeformed_channel_signflip_probe.py`).

  Archimedean (ℂ/ℝ): genuinely archimedean (Real.sqrt, Complex) — §7c.

  -- Ref: [murakami-murakami2001] https://doi.org/10.1007/BF02392716
  -- Ref: [murakami2004] figure-eight & Dehn surgery spaces (math/0401084)
  -- Ref: [leitner2026] conj:binding-qbeta-complex-volume;
       docs/audits/2026-07-11-complex-volume-conditional-mass-binding.md;
       docs/audits/2026-07-26-sdeformed-channel-signflip.md
  -- Ref: [leitner2026] O(u⁴) even NZ tail: exact literature 𝔙₄₁ beyond the
       leading a₂·u² is even (QOU.Knot.NeumannZagierParity.no_odd_rung); the
       higher even coefficients (v₃ = ∓i√3/3, ℚ(√−3)) are the residual carried
       by this citation and do not alter the Im-sign structure proved below.
-/

import QOU.Knot.FigureEightVolume
import QOU.Knot.NeumannZagierParity
import Mathlib.Analysis.SpecialFunctions.Sqrt

namespace QOU.Knot.FigureEightComplexVolume

open QOU.Knot.FigureEightVolume
open scoped Real

/-- The figure-eight cusp modulus `κ = √3/4 = |a₂|` — the magnitude of the
    (purely imaginary) leading Neumann–Zagier complex-volume coefficient.
    `√3/2 = sin(π/3) = Im(e^{iπ/3})` is the cusp shape's imaginary part; the
    factor `1/2` is the NZ potential normalisation. Geometric datum, not fitted. -/
noncomputable def cuspModulus : ℝ := Real.sqrt 3 / 4

theorem cuspModulus_pos : 0 < cuspModulus := by
  unfold cuspModulus
  positivity

/-- The leading complex-volume coefficient `a₂ = i·(√3/4)` — PURELY IMAGINARY
    (real part 0), the algebraic fingerprint of the ℚ(√−3) cusp modulus
    `τ = −i√3`. This is why `Im 𝔙₄₁` is a harmonic quadratic form in `u`. -/
noncomputable def a₂ : ℂ := ⟨0, cuspModulus⟩

@[simp] theorem a₂_re : a₂.re = 0 := rfl
@[simp] theorem a₂_im : a₂.im = cuspModulus := rfl

/-- **The figure-eight deformed complex volume, leading Neumann–Zagier form.**
    `𝔙₄₁(u) = Vol(4₁) + i·(√3/4)·u²`, `Vol(4₁) = 2·Cl₂(π/3)`. This concrete
    `ℂ → ℂ` realizes the abstract `SDeformedVolumeChannel.V` field. -/
noncomputable def V₄₁ (u : ℂ) : ℂ := (VOL_4_1 : ℂ) + a₂ * u ^ 2

/-- 𝔙₄₁(0) = Vol(4₁). -/
@[simp] theorem V₄₁_zero : V₄₁ 0 = (VOL_4_1 : ℂ) := by
  simp [V₄₁]

/-- **Complete-structure value on the Vol axis (EXACT).** `Re 𝔙₄₁(0) = 2·Cl₂(π/3)`
    — the figure-eight hyperbolic volume, with `Im 𝔙₄₁(0) = 0` (CS = 0,
    amphichiral). No residual: `a₂` purely imaginary makes the u=0 real part
    exactly the complete-structure volume. -/
theorem V₄₁_zero_re : (V₄₁ 0).re = 2 * QOU.Archimedean.Cl_2 (Real.pi / 3) := by
  rw [V₄₁_zero]
  simp only [Complex.ofReal_re]
  rfl

theorem V₄₁_zero_im : (V₄₁ 0).im = 0 := by
  rw [V₄₁_zero]; simp

/-- **Neumann–Zagier evenness.** `𝔙₄₁(−u) = 𝔙₄₁(u)` — the deformed complex
    volume is even in the meridian deformation (NZ: the longitude `v(u)` is odd,
    so the potential is even; `QOU.Knot.NeumannZagierParity`). -/
theorem V₄₁_even (u : ℂ) : V₄₁ (-u) = V₄₁ u := by
  simp [V₄₁, pow_two]

/-- **Im 𝔙₄₁ is a harmonic quadratic form.** `Im 𝔙₄₁(u) = (√3/4)·(Re²u − Im²u)`
    — the Chern–Simons part is `κ·Re(u²)`; it vanishes on the DIAGONALS
    `|Re u| = |Im u|`, NOT on the coordinate axes. (Contrast the heuristic
    `√3·Re u·Im u` of the earlier gluing probe, which corresponds to a REAL `a₂`
    and is REFUTED by `τ = −i√3`.) -/
theorem imV₄₁ (u : ℂ) : (V₄₁ u).im = cuspModulus * (u.re ^ 2 - u.im ^ 2) := by
  simp only [V₄₁, Complex.add_im, Complex.ofReal_im, Complex.mul_im, a₂_re, a₂_im,
    zero_add]
  have hre : (u ^ 2).re = u.re ^ 2 - u.im ^ 2 := by
    rw [pow_two, Complex.mul_re]; ring
  have him : (u ^ 2).im = 2 * u.re * u.im := by
    rw [pow_two, Complex.mul_im]; ring
  rw [hre, him]; ring

/-- The classical (Vol-axis) potential of the leading form as a polynomial,
    `Φ₄₁ = Vol(4₁)·1 + κ·X²` — even, and hence with NO cubic (u³) rung by the
    proved `NeumannZagierParity.no_cubic_rung`. This ties the concrete `V₄₁` to
    the corpus parity prune. -/
noncomputable def nzPoly₄₁ : Polynomial ℝ :=
  Polynomial.C VOL_4_1 + Polynomial.C cuspModulus * Polynomial.X ^ 2

theorem nzPoly₄₁_even : nzPoly₄₁.comp (-Polynomial.X) = nzPoly₄₁ := by
  simp [nzPoly₄₁, Polynomial.comp, pow_two]

/-- The concrete leading potential instantiates the NZ even-potential class —
    the parity hypothesis is genuinely satisfied (not fabricated: `Φ₄₁` IS even).
    This is the §3b-cond parity class of `NeumannZagierParity`, NOT the keystone
    conjecture; no `SDeformedVolumeChannel` instance is produced. -/
noncomputable instance : QOU.Knot.NeumannZagierParity.NeumannZagierEvenPotential ℝ where
  potential := nzPoly₄₁
  even_potential := nzPoly₄₁_even

/-- **No u³ rung for the concrete leading form** (via the proved
    `NeumannZagierParity.no_cubic_rung`): the classical potential's cubic
    coefficient vanishes. -/
theorem nzPoly₄₁_no_u3 : nzPoly₄₁.coeff 3 = 0 := by
  have h := QOU.Knot.NeumannZagierParity.no_cubic_rung ℝ
  simpa using h

/-! ## T2 sign-flip invariant — the concrete `V₄₁` sharpens the open `u(q₀)`

The measured bar-odd leak flips sign, `S(muon) ≈ +0.00968 > 0 > S(proton) ≈
−0.03946`. Under the channel identity `S(q₀) = Im 𝔙₄₁(u(q₀))` and the concrete
`Im 𝔙₄₁ = κ(Re²u − Im²u)` (κ > 0), the two anchor signs force `Re²u − Im²u` to
change sign between the anchors — i.e. `u(q₀)` must CROSS the diagonal
`|Re u| = |Im u|`. The #3773-surviving family F3 (one component linear-through-
zero at q*, the other anchor-constant) keeps both anchors on the SAME side of
the diagonal near q*, so it cannot produce the flip. -/

/-- `Im 𝔙₄₁(u) > 0 ↔ |Im u| < |Re u|` (strictly, `u.im² < u.re²`). Sign of the CS
    part = sign of `Re²u − Im²u`, since `κ > 0`. -/
theorem imV₄₁_pos_iff (u : ℂ) : 0 < (V₄₁ u).im ↔ u.im ^ 2 < u.re ^ 2 := by
  rw [imV₄₁]
  constructor
  · intro h
    have := (mul_pos_iff_of_pos_left cuspModulus_pos).mp h
    linarith
  · intro h
    have : 0 < u.re ^ 2 - u.im ^ 2 := by linarith
    exact mul_pos cuspModulus_pos this

/-- `Im 𝔙₄₁(u) < 0 ↔ |Re u| < |Im u|`. -/
theorem imV₄₁_neg_iff (u : ℂ) : (V₄₁ u).im < 0 ↔ u.re ^ 2 < u.im ^ 2 := by
  rw [imV₄₁]
  constructor
  · intro h
    nlinarith [cuspModulus_pos, mul_neg_iff.mp h]
  · intro h
    have : u.re ^ 2 - u.im ^ 2 < 0 := by linarith
    exact mul_neg_of_pos_of_neg cuspModulus_pos this

/-- **Im 𝔙₄₁ vanishes on the diagonal** `|Re u| = |Im u|` (i.e. `Re²u = Im²u`),
    not on the axes. -/
theorem imV₄₁_zero_on_diagonal {u : ℂ} (h : u.re ^ 2 = u.im ^ 2) :
    (V₄₁ u).im = 0 := by
  rw [imV₄₁, h]; ring

/-- **The sign flip forces a diagonal crossing (T2 invariant).** If the CS part
    is positive at one substrate point and negative at another, then `u` lies in
    OPPOSITE regions relative to the diagonal `|Re u| = |Im u|`: `|Im u₁| < |Re u₁|`
    but `|Re u₂| < |Im u₂|`. So any `u(q₀)` realizing the measured flip
    `S(muon) > 0 > S(proton)` must cross that diagonal between the anchors. -/
theorem signflip_forces_diagonal_cross {u₁ u₂ : ℂ}
    (h₁ : 0 < (V₄₁ u₁).im) (h₂ : (V₄₁ u₂).im < 0) :
    u₁.im ^ 2 < u₁.re ^ 2 ∧ u₂.re ^ 2 < u₂.im ^ 2 :=
  ⟨(imV₄₁_pos_iff u₁).mp h₁, (imV₄₁_neg_iff u₂).mp h₂⟩

/-- **F3 cannot sign-flip (the #3773 survivor, refuted against the corrected
    form).** For the F3 family `u = ⟨k·d, c₀⟩` — real part linear-through-zero at
    q* (value `k·d`, `d = q−q*`), imaginary part the anchor-constant `c₀` — as
    long as the linear excursion stays below the constant, `(k·d)² < c₀²`, the CS
    part is NEGATIVE. Hence at two anchors both with `(k·dᵢ)² < c₀²` the sign is
    the SAME (both negative): F3 keeps both on the same side of the diagonal and
    cannot reproduce the sign flip. (The mirror sub-case, `Re = a₀`
    const and `Im = k·d`, is `imV₄₁_pos_iff` with the roles swapped — both
    positive.) This lemma is the small-excursion building block; the fully
    robust F3 refutation (not assuming `(k·dᵢ)²<c₀²`, but respecting the pinned
    product-slope) is the `c₀`-incompatibility argument (`c₀ < c_mu* ≈ 0.0748`
    AND `c₀ > c_pr* ≈ 0.1509` simultaneously — impossible) in
    `sdeformed_channel_signflip_probe.py` + the 2026-07-26 audit; the conclusion
    (F3 cannot reproduce the measured μ>0>p flip) is the same. -/
theorem f3_re_linear_same_sign {k d c₀ : ℝ} (h : (k * d) ^ 2 < c₀ ^ 2) :
    (V₄₁ ⟨k * d, c₀⟩).im < 0 := by
  rw [imV₄₁_neg_iff]
  simpa using h

/-! ## Leading-order magnitude bound — the muon channel is capped by the boost

The T2 invariants above concern the *sign* of `Im 𝔙₄₁`. This block adds the
*magnitude* bound. Because `Im 𝔙₄₁(u) = κ(Re²u − Im²u)` with `κ > 0` and
`Im²u ≥ 0`, the leading form is bounded above by its value on the real axis,
`κ·(Re u)²` — independently of the imaginary (spin) part. So the spin part can
only *decrease* `Im 𝔙₄₁` below the pure-boost value: it can flip the sign
(diagonal crossing) but can NEVER lift the magnitude above `κ·(Re u)²`.

Consequence (companion probe `qbeta_sdeformed_leading_bound_probe.py`): at the
geometrically-derived real boost `Re u = ln q₀` (`meridian-holonomy-boost.md`,
bean `qou-zuk4`), the leading cap is `κ·(ln q₀)² ≈ 0.004714`, while the measured
muon leak is `S_μ ≈ 0.009683 = 2.054 ×` the cap. Hence NO real spin part
realizes `S_μ` at leading order — the muon magnitude must come from the even
`O(u⁴)` Neumann–Zagier tail (dropped in this leading form) or an enlarged real
`Re u`, NOT from the spin part. This is a scope-(a) magnitude insufficiency of
the leading form (invariant cited: `Im²u ≥ 0`, `κ > 0`); it does NOT exclude the
channel identity `S = Im 𝔙_q` (the full quantum complex volume carries the
`O(u⁴)` tail). See
`docs/audits/2026-08-01-derive-S-Qbeta-E0-leading-bound-decoupling.md`. -/

/-- **Leading-form upper bound.** `Im 𝔙₄₁(u) ≤ κ·(Re u)²` for every `u`, since the
    imaginary (spin) part only subtracts (`κ·Im²u ≥ 0`). The spin part can flip
    the sign but never lift the magnitude above the pure-boost value `κ·Re²u`. -/
theorem imV₄₁_le_cuspModulus_reSq (u : ℂ) :
    (V₄₁ u).im ≤ cuspModulus * u.re ^ 2 := by
  rw [imV₄₁]
  have h : (0 : ℝ) ≤ cuspModulus * u.im ^ 2 :=
    mul_nonneg cuspModulus_pos.le (sq_nonneg _)
  nlinarith [h]

/-- **Leading-order unreachability.** If a target `S` exceeds the `Re`-capped
    leading bound `κ·r²`, then NO `u` with real part `r` realizes it at leading
    order: `(V₄₁ u).im = S` is impossible. Instantiated at `r = ln q₀`,
    `S = S_μ`: the muon leak (`= 2.054 × κ(ln q₀)²`) is unreachable for any real
    spin — the magnitude sub-obstruction, orthogonal to the (spin-driven) sign
    flip. -/
theorem imV₄₁_leading_unreachable_of_lt {r S : ℝ} (hlt : cuspModulus * r ^ 2 < S)
    (u : ℂ) (hu : u.re = r) : (V₄₁ u).im ≠ S := by
  intro heq
  have hbound := imV₄₁_le_cuspModulus_reSq u
  rw [heq, hu] at hbound
  exact absurd hbound (not_le.mpr hlt)

end QOU.Knot.FigureEightComplexVolume
