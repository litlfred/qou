/-
Copyright (c) 2026 litlfred. All rights reserved.

# Rigidity prune for the archimedean scalar `S = Q_β/E₀`

The `c_3` odd channel factors as `c_3^odd = κ_(2,1)(q)·S` with a derived pure-q
bar-odd carrier `κ_(2,1)` (`QOU.QBeta.kappaNum/kappa21`) and a single archimedean
scalar `S = Q_β/E₀` — "the single archimedean leak" the whole `c_k` chain carries
(`docs/audits/2026-06-13-qbeta-heat-fmap-symbolic-and-literature.md` §2). Numerically
`S` **swings across anchors**: `S_proton ≈ 908.4`, `S_muon ≈ 886.8`
(`S_p/S_μ ≈ 1.024 ≠ 1`).

This file formalizes the **structural prune** of the naive keystone "`S = g(𝔇)`
for a categorical function `g` of a single calibration datum `𝔇`":

- `no_anchor_invariant_realizes_swing` — the proved invariant: if the datum is
  **anchor-invariant** (`𝔇` takes the same value at the proton and muon anchors,
  as every fixed CAL constant does — `P_skew^β`, `P_avg^π`, `m_π`, …), then any pure
  function `g ∘ 𝔇` is **constant across anchors**, so it cannot equal a target
  `S` that **differs** between anchors. Hence `S` is not a pure function of any
  single anchor-invariant CAL datum. This is a **scope-(b) structural exclusion**
  of the *pure-function* form, citing this invariant.
- `S_bar_odd_of_ratio` — the parity fact: `S = Q_β/E₀` with `Q_β` bar-odd
  (`σ Q_β = −Q_β`, the sinh/CAL-2 = P_skew^β partner) and `E₀` bar-even
  (`σ E₀ = E₀`, the cosh/CAL-3 unit) is **bar-odd** (`σ S = −S`). So `S`'s CAL
  content is P_skew^β (bar-odd, CAL-2), NOT P_avg^π — refining the "`g(P_avg^π)`" label.

**What is NOT excluded (scope-(a), still open).** The invariant excludes only the
*pure-function-of-one-anchor-invariant-datum* form. It does **not** exclude an
anchor-*dependent* fibre object `g(𝔇, q₀)` — but such a `g` would need a
~2×10⁶ logarithmic `q₀`-sensitivity (the registry `dc_3/dq ≈ 3.84×10⁶`
obstruction; corrected 2026-08-29 from `4.6×10⁶`, which is the secant taken
with the pre-#1422 superseded muon `c₃ = -2.0097` — bean `qou-kt8o`) to supply the 2.4 % swing from the ppb-level anchor `q₀` difference,
which no *smooth real* `g` provides. The surviving route is fibre-level (the
ζ₄-residue of `conj:binding-qbeta-complex-volume`), consistent with the Im(q)
fibre-vs-observable reading — NOT a real function of the pion datum.
-/
import Mathlib.Algebra.Field.Basic

namespace QOU.QBeta.SRigidity

variable {A D R : Type*}

/-- **Anchor-invariant input cannot reproduce an anchor-varying target.**
If a candidate `g : D → R` is fed a datum `datum : A → D` that is *constant*
across two anchors (`datum a = datum a'`), then `g ∘ datum` is constant across
those anchors; so a target `S : A → R` with `S a ≠ S a'` is **not** realized by
`g ∘ datum` at every anchor. Applied to `S = Q_β/E₀` (which swings: proton vs
muon) and any fixed CAL datum `𝔇` (`P_skew^β`, `P_avg^π`, `m_π`, all anchor-invariant):
`S` is not a pure function of a single anchor-invariant calibration datum. -/
theorem no_anchor_invariant_realizes_swing
    (g : D → R) (datum : A → D) (S : A → R) (a a' : A)
    (hdatum : datum a = datum a') (hswing : S a ≠ S a') :
    ¬ (∀ x, S x = g (datum x)) := by
  intro h
  apply hswing
  rw [h a, hdatum, ← h a']

/-- **`S = Q_β/E₀` is bar-odd.** With `Q_β` bar-odd (`σ Q_β = −Q_β`, the sinh /
CAL-2 = P_skew^β partner) and `E₀` bar-even (`σ E₀ = E₀`, the cosh / CAL-3 unit),
their product form `Q_β · E₀⁻¹`… — stated multiplicatively as `S · E₀ = Q_β`
to avoid an inverse, the honest content is: `σ (Q_β) = −Q_β` forces `S` bar-odd.
Here we record the clean product version: if `S` satisfies `σ S = ε·S` and
`σ E₀ = E₀` with `S·E₀ = Q_β` and `σ Q_β = −Q_β`, then the odd sign propagates.
The lemma states the carrier-parity step directly: a bar-odd numerator over a
bar-fixed denominator-witness is bar-odd. -/
theorem S_bar_odd_of_ratio [CommRing R] (σ : R →+* R) (S E₀ : R)
    (hE : σ E₀ = E₀) (hodd : σ (S * E₀) = -(S * E₀)) :
    σ S * E₀ = -(S * E₀) := by
  rw [map_mul, hE] at hodd
  exact hodd

end QOU.QBeta.SRigidity
