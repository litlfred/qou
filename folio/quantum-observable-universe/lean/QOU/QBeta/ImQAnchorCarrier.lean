import QOU.QBeta.ArgUPhaseBranchSelection

/-!
# The Im(q) reframe of the c₃ anchor-swing, tested against #4293's proved `∂S/∂φ`
— a single global `Im(q₀)` cannot carry the swing; per-anchor `Im(q)` fits anything

**The owner's reframe (capstone #4297).** `q₀` is not a universal real constant but
our *local, measured* substrate value — a field that VARIES and generically carries
`Im(q) ≠ 0`. #4293 (`ArgUPhaseBranchSelection`, sorry-free) proved the bar-odd phase
channel `S(r,φ) = (√3/2) r² sin(2φ)`, `φ = arg(u)`, `u = 2 log q₀`, is a
**maximal-leverage** DOF (`∂S/∂φ|₀ = √3 r² ≠ 0`, `nzImVolume_phase_hasDerivAt`) that
is **frozen** at strictly real `q₀` (`arg(u)=0`, `substrate_meridian_arg_zero`). Allow
`Im(q₀) ≠ 0` ⇒ `arg(u) ≠ 0` ⇒ the phase **unfreezes**. This file makes the
falsifiable test of that reframe a typed object.

**The `arg(u) ↔ Im(q₀)` relation (probe, exact — `qbeta_imq_anchor_carrier_probe.py`).**
For `q₀ = q_r + i ε`, `u = 2 log q₀`, the phase's leading response is linear in `ε`:

`d arg(u)/dε |₀ = 1/(q_r log q_r)`  (numeric = analytic = `8.63427` at `q_r=1.10998`),

so, composing with `∂S/∂φ|₀ = √3 r²` (`r = 2 log q_r`), the phase-channel linear
response is `S ≈ k·ε` with

`k = √3 r² / (q_r log q_r) = 4√3 log(q_r)/q_r = 0.651275`  (exact = numeric).

**The falsifiable test.** The proton-pin and muon-pin anchors are two pins of the
SAME `q₀`, differing only `~22 ppb` in `q_r`; the slope `k` is therefore
anchor-invariant to `1.9×10⁻⁷`, so the model MEASURES `Im(q₀)` faithfully. **But**
that same near-equality is the problem: a **single global** `Im(q₀)=ε` produces the
SAME `S` at both anchors up to the `22 ppb` `q_r` difference — a swing of
`7.4×10⁻⁹` for the fitted `|ε|≈0.06`, versus the observed `|S_p − S_m| = 0.0492`: an
**order-mismatch of `6.63×10⁶`** (the registry `dc₃/dq ≈ 3.84×10⁶` obstruction
reappearing through `arg(u)`; corrected 2026-08-29 from `4.6×10⁶`, the
superseded-`c₃` secant — bean `qou-kt8o`; and the amplitude ceiling `(√3/2)r² = 0.0377` at fixed
`r` is already below `|S_p|=0.0395`). Reproducing the swing therefore demands a
**different `Im(q)` per anchor**: `ε_p = −0.061` (`−5.5%` of `q_r`),
`ε_m = +0.015` (`+1.3%`), **opposite sign** (forced by the merged
`fig8Trace_im_odd`: `sign S = sign ε`) and `4.07×` in magnitude — a **free** `O(10⁻²)`
knob with no derived scale.

**Verdict — NOT a lead (scope-(a)).** Both guardrail failures fire together:
* *order-mismatch wall* — any anchor-invariant `Im(q₀)`, at any physical magnitude,
  is `~10⁶`–`10⁷` too small (`global_imq_cannot_realize_swing` + the probe's
  quantitative gap);
* *unfalsifiable knob* — per-anchor `Im(q)` fits ANY residual pair
  (`peranchor_imq_fits_anything`), with the required values sign-flipping between a
  mere *pinning choice* (`required_imq_opposite_sign`) and no independent predictor.

This is exactly the honesty guardrail's purpose: it keeps "q₀ varies" from being
laundered into a c₃ closure. `S`'s value stays measurement-limited
(`no_anchor_invariant_realizes_swing`, `MeasurementLimitedFloor`);
`conj:algebraic-geometric-dilog-equivalence` stays OPEN. **No `c_k` value is
produced; NO residual is inverted to define `Im(q)`; nothing is wired.**

Base ring `ℝ` (archimedean side, matching #4293: `Real.log`, ordering, the observable
phase). The `Im(q)` that would unfreeze the phase lives at the *fibre* level where it
is free — which the observable anchor comparison cannot access (AGENTS.md "Im(q) at
fibre vs observable level").

-- Ref: [leitner2026] docs/audits/2026-07-26-q0-varies-imq-c3.md
-- Ref: [leitner2026] docs/audits/2026-07-25-c3-categorical-exclusion-capstone.md
-- Ref: [leitner2026] conj:algebraic-geometric-dilog-equivalence
-- Ref: [leitner2026] conj:im-q-physical-role
-/

namespace QOU.QBeta.ImQAnchorCarrier

open QOU.QBeta.ArgUPhaseBranchSelection

/-- **Linear phase-channel response** `S = k·ε` in the substrate imaginary part
`ε = Im(q₀)`, with slope `k = (∂S/∂φ|₀)·(d arg u/dε|₀) = √3 r²/(q_r log q_r)` (probe:
`k = 0.651275` at the substrate). This is the leading form of the #4293 `nzImVolume`
under the `arg(u) ↔ Im(q₀)` linearization; nonlinear corrections do not rescue the
verdict (probe carries the exact, non-linearized comparison). -/
noncomputable def phaseResponse (k ε : ℝ) : ℝ := k * ε

/-- **Real substrate ⇒ no signal** (`ε=0`), recovering #4293's real-ray
`nzImVolume_real_ray` in the linearized model. -/
theorem phaseResponse_real_zero (k : ℝ) : phaseResponse k 0 = 0 := by
  simp [phaseResponse]

/-- **Odd in `ε`** — the merged parity `fig8Trace_im_odd` (`sign S = sign Im q`) at
the linear level: `S(−ε) = −S(ε)`. -/
theorem phaseResponse_odd (k ε : ℝ) : phaseResponse k (-ε) = -phaseResponse k ε := by
  simp only [phaseResponse]; ring

/-- **The slope is realized at every `ε` (measurement leg).** `dS/dε = k`, a fixed,
anchor-invariant slope — so the model *measures* `Im(q₀)` with the same
proportionality at both anchors (this is the "good news" of the reframe, and exactly
why a single `Im(q₀)` cannot explain a *swing*: the proportionality does not change
between the anchors). -/
theorem phaseResponse_hasDerivAt (k ε : ℝ) : HasDerivAt (phaseResponse k) k ε := by
  simpa [phaseResponse] using (hasDerivAt_id ε).const_mul k

/-- **FALSIFIABLE TEST — a single global `Im(q₀)` cannot realize the swing.** Both
anchors are two pins of the same `q₀`; in a *global* model they share the same
imaginary part `ε`, hence the same phase input, hence the **same** response
`phaseResponse k ε`. A single value cannot equal two distinct targets `S_p ≠ S_m`.
This is `QOU.QBeta.SRigidity.no_anchor_invariant_realizes_swing` for the `Im(q)`
channel: an anchor-invariant `Im(q₀)` is anchor-invariant DATA, and the quantitative
probe shows the residual `q_r`-difference channel is `6.6×10⁶` too weak. -/
theorem global_imq_cannot_realize_swing (k ε Sp Sm : ℝ) (hswing : Sp ≠ Sm) :
    ¬ (Sp = phaseResponse k ε ∧ Sm = phaseResponse k ε) := by
  rintro ⟨hp, hm⟩
  exact hswing (hp.trans hm.symm)

/-- **THE FIT — per-anchor `Im(q)` fits ANY pair of residuals (unfalsifiable knob).**
For nonzero slope `k` and ANY targets `Sp, Sm`, there exist per-anchor imaginary
parts `εp, εm` with `phaseResponse k εp = Sp`, `phaseResponse k εm = Sm` (namely
`εp = Sp/k`, `εm = Sm/k`). Two free parameters fit two data points — the guardrail's
unfalsifiability made precise: a per-anchor `Im(q)` is a fit, never a measurement of
one substrate `Im(q₀)`. -/
theorem peranchor_imq_fits_anything (k : ℝ) (hk : k ≠ 0) (Sp Sm : ℝ) :
    ∃ εp εm : ℝ, phaseResponse k εp = Sp ∧ phaseResponse k εm = Sm :=
  ⟨Sp / k, Sm / k, by simp only [phaseResponse]; field_simp, by simp only [phaseResponse]; field_simp⟩

/-- **Opposite-sign requirement (parity `fig8Trace_im_odd`).** With positive slope
`k>0`, realizing the observed `S_p < 0 < S_m` forces `ε_p < 0 < ε_m`: the required
`Im(q)` FLIPS SIGN between the anchors. The sign is set by *which lepton/baryon ratio
pins `q₀`* — a pinning choice with no independent predictor — which is precisely why
the per-anchor solve is a fit, not a substrate measurement. -/
theorem required_imq_opposite_sign (k εp εm Sp Sm : ℝ) (hk : 0 < k)
    (hp : phaseResponse k εp = Sp) (hm : phaseResponse k εm = Sm)
    (hSp : Sp < 0) (hSm : 0 < Sm) : εp < 0 ∧ 0 < εm := by
  simp only [phaseResponse] at hp hm
  refine ⟨?_, ?_⟩
  · have : k * εp < 0 := hp ▸ hSp
    nlinarith [this, hk]
  · have : 0 < k * εm := hm ▸ hSm
    nlinarith [this, hk]

/-- **The order-mismatch, stated structurally.** A single global `Im(q₀)=ε` feeds the
same magnitude to both anchors, so its *swing* is only the difference of the two
slopes `(k_p − k_m)·ε`. Since `k` is anchor-invariant to the `22 ppb` `q_r`
difference (`k_p = k_m` in the exact-equality idealization), that swing is exactly
zero — the residual real-part channel supplies it, and the probe measures that
channel at `6.6×10⁶` below the observed swing. -/
theorem global_imq_zero_swing_when_slopes_equal (kp km ε : ℝ) (hk : kp = km) :
    phaseResponse kp ε - phaseResponse km ε = 0 := by
  simp only [phaseResponse, hk, sub_self]

end QOU.QBeta.ImQAnchorCarrier
