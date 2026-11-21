/-
  Is the T5 channel's `u` the substrate-matched Murakami meridian?  (bean qou-5nze)

  CONTEXT (PR #4513).  `PhiBSArgumentIdentification.SDeformedVolumeChannel`
  documents its field `u : ℝ → ℂ` as "the substrate → deformation map `u(q₀)`
  (log meridian holonomy)", and `DeltaLambdaT5Assembly.s_channel_at_substrate`
  reads `ϑ_K = Im(u(q₀))` off it under the hypothesis `Re(u(q₀)) = ln q₀`.
  Separately `Knot.DeformedMeridianWinding` proves, sorry-free, that the
  substrate-matched Murakami meridian for 4₁ is `u = N·t − 2πi·k` (`t = ln q₀`).
  If the two `u` were the same object, `ϑ_K` would be QUANTIZED (`Im u = −2πk`).
  This file settles whether they are.

  THE ANSWER IS NO, on two independent grounds, both proved below.

  1. `channelFree` — the class constrains `u` NOT AT ALL.  For every `u`, every
     `V` and every `A_ω` the class is inhabited, so no theorem stated for a
     general `SDeformedVolumeChannel` can impose the Murakami matching on `u`.
     (The corpus contains ZERO instances; every use is a hypothesis binder.)

  2. `color_eq_one_of_re_eq_log` — IF one nevertheless identifies the two, the
     T5 hypothesis `Re(u(q₀)) = ln q₀` forces `N = 1`, because the meridian's
     real part is `N·t`, not `t`.  `N = 1` is the one-dimensional colouring, at
     which the coloured Jones polynomial is identically `1` and carries no knot
     information — the deformed volume conjecture is an `N → ∞` statement.  So
     the identification is available only at the degenerate colour.

  AND THE IDENTIFICATION IS REFUTED BY THE MEASURED SIGNS.  Under it, the
  boost-dominated branch (`S > 0`, i.e. `ϑ² < ln²q₀`) forces `k = 0`
  (`winding_eq_zero_of_boost_dominated`), hence `ϑ = 0`; and `ϑ = 0` at both
  anchors puts `S` at the SAME sign at both (`no_sign_flip_of_theta_zero`),
  contradicting the measured `S_μ > 0 > S_p`.

  SCOPE — (a), not (b), per AGENTS.md §"Before declaring refuted".  What is
  excluded is the CONJUNCTION "the channel's `u` is the substrate-matched
  Murakami meridian" + the T5 `Re u = ln q₀` hypothesis.  Both source objects
  stand on their own.  No value of `A_ω` is derived, no `ϑ_K` is proposed, and
  nothing here is wired to production.

  A NOTE ON THE T5 DOCSTRING.  `DeltaLambdaT5Assembly` attributes
  `Re(u(q₀)) = ln q₀` to a lemma `meridian_holonomy_boost`, which does not
  exist anywhere in the corpus.  `hRe` is an undischarged hypothesis of
  `s_channel_at_substrate`, not a proved fact; the docstring there has been
  corrected alongside this file.

  TRIVIALITY LADDER (reported honestly, per PR #4513's own bar).
  `color_eq_one_of_re_eq_log` and `re_ne_log_of_color_ne_one` ARE discharged by
  `aesop` — they are one-line cast arguments.  They are not vacuous: dropping
  `ht : t ≠ 0` makes the first FALSE (`N = 5, t = 0`), so the hypothesis is
  load-bearing.  Their value is interpretive, not technical.  The declarations
  carrying the actual content — `winding_eq_zero_of_boost_dominated`,
  `color_one_and_theta_zero`, `no_sign_flip_of_theta_zero` — all survive the
  ladder.

  Archimedean (ℝ, ℂ): genuinely archimedean (`Real.pi`, `Real.log`, ordering)
  — §7c.

  -- Ref: [murakami2004] figure-eight & Dehn surgery spaces (math/0401084)
  -- Ref: [murakami-murakami2001] https://doi.org/10.1007/BF02392716
  -- Ref: [leitner2026] conj:binding-qbeta-complex-volume
-/

import QOU.Knot.FigureEightDeformedMeridianWinding
import QOU.QBeta.PhiBSArgumentIdentification

namespace QOU.QBeta.ChannelMeridianIdentification

open QOU.Knot.DeformedMeridianWinding
open QOU.QBeta.PhiBSArgumentIdentification

/-! ## 1. The channel imposes nothing on `u` -/

/-- **The channel is conservative over `u` (branch (a), proved).**  For an
arbitrary deformation map `u`, an arbitrary deformed volume `V` and an arbitrary
Stokes constant `A`, the S-channel class is inhabited — witnessed by the `S`
that the class identity itself names.  Hence `SDeformedVolumeChannel` places NO
condition whatsoever on `u`, and in particular does not impose the Murakami
substrate matching `u = N·t − 2πi·k`.  Any quantization of `Im u` must therefore
come from OUTSIDE the class.

**This is deliberately a `def`, never an `instance`.**  Registering it for
typeclass resolution would let every `[SDeformedVolumeChannel S]` theorem
discharge itself against a tautologically-defined `S` and silently trivialise
the downstream chain.  It also does NOT fabricate the open conjecture: the
conjecture concerns the MEASURED `S_K`, whereas the `S` built here is defined to
satisfy the identity. -/
def channelFree (u : ℝ → ℂ) (V : ℂ → ℂ) (A : ℝ) :
    SDeformedVolumeChannel (fun q₀ => A * (V (u q₀)).im) where
  u := u
  V := V
  A_ω := A
  S_eq := fun _ _ => rfl

@[simp] lemma channelFree_u (u : ℝ → ℂ) (V : ℂ → ℂ) (A : ℝ) :
    (channelFree u V A).u = u := rfl

/-! ## 2. The identification forces the degenerate colour `N = 1` -/

/-- **`Re u = ln q₀` forces trivial colour.**  The substrate-matched meridian
has real part `N·t`; demanding it equal `t` (the T5 hypothesis `hRe`, with
`t = ln q₀ ≠ 0` for `q₀ ≠ 1`) forces `N = 1`.

This is the quantitative form of the identification's cost: `hRe` is not a free
normalisation, it pins the colour to the one value at which the coloured Jones
polynomial is trivial.

Technically easy (`aesop` discharges it); its weight is in what it says, not in
its proof.  It is nonetheless falsifiable — without `ht` it is false at
`N = 5, t = 0`. -/
theorem color_eq_one_of_re_eq_log {N k : ℕ} {t : ℝ} (ht : t ≠ 0)
    (hRe : (meridian ((N : ℝ) * t) k).re = t) :
    N = 1 := by
  rw [meridian_re] at hRe
  have hN : (N : ℝ) = 1 := by
    have : ((N : ℝ) - 1) * t = 0 := by linarith [hRe]
    rcases mul_eq_zero.mp this with h | h
    · linarith
    · exact absurd h ht
  exact_mod_cast hN

/-- Contrapositive, in the form the deformed volume conjecture cares about: at
any non-degenerate colour `N ≠ 1`, the substrate-matched meridian's real part is
NOT `ln q₀`, so the T5 hypothesis `hRe` fails outright. -/
theorem re_ne_log_of_color_ne_one {N k : ℕ} {t : ℝ} (ht : t ≠ 0) (hN : N ≠ 1) :
    (meridian ((N : ℝ) * t) k).re ≠ t :=
  fun hRe => hN (color_eq_one_of_re_eq_log ht hRe)

/-! ## 3. Under the identification, a boost-dominated anchor has `ϑ = 0` -/

/-- **Boost dominance kills the winding.**  The meridian's imaginary part is
`−2πk`, so `Im²u = 4π²k²`.  If the anchor is boost-dominated — `ϑ² < t²`, the
`S > 0` branch of `s_channel_sign_pos` — and the substrate scale is subarchimedean
in the sense `|t| < 2π` (amply true at `t = ln q₀ ≈ 0.104`), then `k = 0`.

There is no room here: the smallest nonzero winding already contributes
`2π ≈ 6.28`, some sixty times `ln q₀`. -/
theorem winding_eq_zero_of_boost_dominated {N k : ℕ} {t : ℝ}
    (ht : |t| < 2 * Real.pi)
    (hboost : (meridian ((N : ℝ) * t) k).im ^ 2 < t ^ 2) :
    k = 0 := by
  by_contra hk
  have hk1 : 1 ≤ (k : ℝ) := by
    have : 1 ≤ k := Nat.one_le_iff_ne_zero.mpr hk
    exact_mod_cast this
  rw [meridian_im] at hboost
  -- `Im²u = (2πk)² ≥ (2π)² > t²`, contradicting `Im²u < t²`
  have hpi : (0 : ℝ) < 2 * Real.pi := by positivity
  have ht2 : t ^ 2 < (2 * Real.pi) ^ 2 := by
    have := abs_nonneg t
    nlinarith [sq_abs t, abs_nonneg t]
  nlinarith [hpi, hk1, sq_nonneg ((k : ℝ) - 1)]

/-- **The identification collapses a boost-dominated anchor to `ϑ = 0`.**
Combining §2 and §3: the colour is degenerate AND the angular deformation
vanishes identically. -/
theorem color_one_and_theta_zero {N k : ℕ} {t : ℝ}
    (ht0 : t ≠ 0) (htpi : |t| < 2 * Real.pi)
    (hRe : (meridian ((N : ℝ) * t) k).re = t)
    (hboost : (meridian ((N : ℝ) * t) k).im ^ 2 < t ^ 2) :
    N = 1 ∧ (meridian ((N : ℝ) * t) k).im = 0 := by
  refine ⟨color_eq_one_of_re_eq_log ht0 hRe, ?_⟩
  rw [meridian_im, winding_eq_zero_of_boost_dominated htpi hboost]
  norm_num

/-! ## 4. `ϑ = 0` at both anchors admits no sign flip -/

/-- **No sign flip at vanishing angular deformation.**  In the T5 shape
`S = A_ω · κ · (ln²q₀ − ϑ²)`, two anchors that both have `ϑ = 0` carry `S` of
the SAME (positive) sign, whatever their Stokes constants.

This is what refutes the identification against data: the two anchors are
MEASURED with `S_μ > 0 > S_p`, and §3 forces `ϑ = 0` at the boost-dominated one
while §2 forces the same degenerate colour at both. -/
theorem no_sign_flip_of_theta_zero {A₁ A₂ κ t ϑ₁ ϑ₂ S₁ S₂ : ℝ}
    (hA₁ : 0 < A₁) (hA₂ : 0 < A₂) (hκ : 0 < κ) (ht : t ≠ 0)
    (hϑ₁ : ϑ₁ = 0) (hϑ₂ : ϑ₂ = 0)
    (hS₁ : S₁ = A₁ * κ * (t ^ 2 - ϑ₁ ^ 2))
    (hS₂ : S₂ = A₂ * κ * (t ^ 2 - ϑ₂ ^ 2)) :
    0 < S₁ ∧ 0 < S₂ := by
  have ht2 : 0 < t ^ 2 := by positivity
  constructor
  · rw [hS₁, hϑ₁]; have := mul_pos hA₁ hκ; nlinarith
  · rw [hS₂, hϑ₂]; have := mul_pos hA₂ hκ; nlinarith

/-- The falsification, stated as the impossibility it is: with `ϑ = 0` at both
anchors, the second anchor cannot be negative. -/
theorem not_neg_of_theta_zero {A₁ A₂ κ t ϑ₁ ϑ₂ S₁ S₂ : ℝ}
    (hA₁ : 0 < A₁) (hA₂ : 0 < A₂) (hκ : 0 < κ) (ht : t ≠ 0)
    (hϑ₁ : ϑ₁ = 0) (hϑ₂ : ϑ₂ = 0)
    (hS₁ : S₁ = A₁ * κ * (t ^ 2 - ϑ₁ ^ 2))
    (hS₂ : S₂ = A₂ * κ * (t ^ 2 - ϑ₂ ^ 2)) :
    ¬ (S₂ < 0) := by
  have h := no_sign_flip_of_theta_zero hA₁ hA₂ hκ ht hϑ₁ hϑ₂ hS₁ hS₂
  exact not_lt.mpr (le_of_lt h.2)

end QOU.QBeta.ChannelMeridianIdentification
