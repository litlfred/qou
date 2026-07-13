import Mathlib.Topology.Order.IntermediateValue
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import QOU.MathlibExt.FaddeevPhiBRealIntegral

/-!
# The S argument-identification keystone (bar-odd face of `conj:algebraic-geometric-dilog-equivalence`)

The c₃ bar-odd derivation converged (every route, 2026-07-11) on a single open
link: identify the Faddeev `Φ_b` **argument** `z(q₀)` whose fibre-branch
evaluation at each substrate anchor reproduces the anchor-dependent S-leak
`S = c₃ + Vol(4₁)` (`S(muon) ≈ +0.00968`, `S(proton) ≈ −0.03946`).  This is
the **keystone conjecture** — the bar-odd companion of the pole↔cusp matching
of `conj:algebraic-geometric-dilog-equivalence` (whose bar-even face is the
`−Vol(4₁)` datum).

**Where physics lives.**  The physical regime is the **fibre branch**: real
`b`, hence `|q_b| = |e^{iπb²}| = 1` (`norm_fibreQParam`).  There the
modular-double product diverges and the construction is the real single
integral `QOU.MathlibExt.FaddeevPhiBRealIntegral.phiB` — a genuine
`noncomputable def`, unimodular (`norm_phiB`) and σ-unitary
(`phiB_mul_conj`), hence an intrinsically **bar-odd** carrier
(`prop:phi-b-unitary-bar-odd`).  The fibre b-map is
`b(q₀) = √(ln q₀ / 2π)`, so `q_b = e^{i·ln q₀ / 2}` (`fibreQParam_fibreB`).

**Honesty discipline.**  The conjecture is stated **relative to a given
argument map** `zArg` — NOT as a bare existence claim.  A pointwise
existence claim (`∀ q₀ ∃ z, phase (fibreB q₀) z = S q₀`) would be near-vacuous
(choice-function selection against an unbounded continuous phase); the open
mathematical content is that the **structural** map — the substrate →
meridian-holonomy map supplied by the pole↔cusp matching of
`conj:algebraic-geometric-dilog-equivalence` /
`conj:shared-denominator-cusp-holonomy` — is such a `zArg`.  No instance is
fabricated (the class is the open state); no `c_k` is produced or wired.

**Physical channel caveat (decay = binding).**  The identification of the
bar-odd face with the *decay observable* `𝔔_β = Im 𝔙` — and hence the
"decay = binding" reading of the Gram-ghost mode — is **conditional on
`conj:binding-qbeta-complex-volume`** (`ComplexVolumeMatch`).  `Φ_b` touches
binding ONLY through that unproven channel identity; nothing in this file
assumes it.  The class below is about the numerical S-map (a function of the
substrate modulus), not about the decay observable.

-- Ref: [manuscript] conj:algebraic-geometric-dilog-equivalence; docs/audits/2026-07-11-qbeta-c3-barodd-sleak-phib-target.md
-- Ref: [manuscript] docs/audits/2026-07-11-algebraic-geometric-dilog-provability.md
-- Ref: [faddeev1995] Faddeev, Lett. Math. Phys. 34 (1995) 249. https://doi.org/10.1007/BF01872779
-/

namespace QOU.QBeta.PhiBSArgumentIdentification

open QOU.MathlibExt.FaddeevPhiBRealIntegral

/-- The **fibre b-map** `b(q₀) = √(ln q₀ / 2π)`: the real-`b` (fibre-branch)
    counterpart of the product-branch substrate map
    `√(ln q₀/2π)·e^{iπ/4}` (`QOU.MathlibExt.PhiBProd.substrateB`) — the
    `e^{iπ/4}` phase removed, so the modular parameter lands ON the unit
    circle instead of inside it. -/
-- Ref: [manuscript] docs/audits/2026-07-11-phib-lean-route-memo.md
noncomputable def fibreB (q₀ : ℝ) : ℝ :=
  Real.sqrt (Real.log q₀ / (2 * Real.pi))

/-- The fibre b-map is positive on the physical domain `q₀ > 1`. -/
theorem fibreB_pos {q₀ : ℝ} (h : 1 < q₀) : 0 < fibreB q₀ :=
  Real.sqrt_pos.mpr (div_pos (Real.log_pos h) (by positivity))

/-- `b(q₀)² = ln q₀ / 2π` on `q₀ ≥ 1`. -/
theorem fibreB_sq {q₀ : ℝ} (h : 1 ≤ q₀) :
    fibreB q₀ ^ 2 = Real.log q₀ / (2 * Real.pi) :=
  Real.sq_sqrt (div_nonneg (Real.log_nonneg h) (by positivity))

/-- **The fibre modular parameter at the substrate is the pure phase
    `e^{i·ln q₀ / 2}`** — `|q_b| = 1` with the substrate modulus as the
    angle.  (Contrast the product branch, where `q_b = e^{-t} = 1/q₀` is
    real inside the disc.) -/
theorem fibreQParam_fibreB {q₀ : ℝ} (h : 1 ≤ q₀) :
    fibreQParam (fibreB q₀)
      = Complex.exp (Complex.ofReal (Real.log q₀ / 2) * Complex.I) := by
  unfold fibreQParam
  rw [fibreB_sq h]
  have hπ : Real.pi * (Real.log q₀ / (2 * Real.pi)) = Real.log q₀ / 2 := by
    field_simp
  rw [hπ]

/-- **The keystone conjecture (§3b primary class).**  The given argument map
    `zArg` realizes the S-leak through the fibre-branch `Φ_b` phase:

    * `S_continuousOn` — the S-map varies continuously on the physical
      domain `q₀ > 1` (the hypothesis under which the measured sign flip
      `S(muon) > 0 > S(proton)` forces a zero crossing);
    * `readout` — at every substrate modulus the Faddeev phase at the
      identified argument IS the S-leak: `phase (b(q₀)) (zArg q₀) = S q₀`.

    The intended `zArg` is the substrate → meridian-holonomy map of the
    pole↔cusp matching (`conj:algebraic-geometric-dilog-equivalence`); the
    class is parametrized by the map precisely so that it carries that
    structural content rather than a vacuous pointwise choice (module
    docstring).  An instance for the structural map is the OPEN state —
    none is fabricated here. -/
-- Ref: [manuscript] conj:algebraic-geometric-dilog-equivalence
-- Ref: [manuscript] docs/audits/2026-07-11-qbeta-c3-barodd-sleak-phib-target.md
class SArgumentIdentification (zArg S : ℝ → ℝ) : Prop where
  /-- Continuity of the S-map on the physical domain. -/
  S_continuousOn : ContinuousOn S (Set.Ioi 1)
  /-- The Φ_b phase at the identified argument reproduces the S-leak. -/
  readout : ∀ q₀ : ℝ, 1 < q₀ → phase (fibreB q₀) (zArg q₀) = S q₀

/-- **Unimodular readout form (derived).**  Under the identification, the
    Φ_b value at the identified argument is the pure phase `e^{iS(q₀)}` —
    the S-leak is literally the argument of a σ-unitary, matching the
    bar-odd phase reframe `𝔔_β/Q_A = cos Φ(u)`. -/
theorem readout_phiB {zArg S : ℝ → ℝ} [h : SArgumentIdentification zArg S]
    {q₀ : ℝ} (hq : 1 < q₀) :
    phiB (fibreB q₀) (zArg q₀)
      = Complex.exp (Complex.ofReal (S q₀) * Complex.I) := by
  unfold phiB
  rw [h.readout q₀ hq]

/-- **Intermediate-value zero crossing (unconditional).**  If `S` is
    continuous on `q₀ > 1` and takes a positive value at one anchor and a
    negative value at a later one, it vanishes somewhere between.  This is
    the audited sign-flip observation: `S(muon) > 0 > S(proton)` forces a
    substrate `q*` between the anchors with `S(q*) = 0` — i.e.
    `c₃ = −Vol(4₁)` exactly, purely bar-even.  (The two measured signs
    enter as hypotheses: measured values are not Lean-provable.) -/
-- Ref: [manuscript] docs/audits/2026-07-11-qbeta-c3-barodd-sleak-phib-target.md §New observation
theorem exists_zero_crossing {S : ℝ → ℝ} (hS : ContinuousOn S (Set.Ioi 1))
    {a c : ℝ} (ha : 1 < a) (hac : a ≤ c) (hSa : 0 < S a) (hSc : S c < 0) :
    ∃ q ∈ Set.Icc a c, S q = 0 := by
  have hsub : Set.Icc a c ⊆ Set.Ioi 1 := fun x hx => lt_of_lt_of_le ha hx.1
  have hmem : (0 : ℝ) ∈ Set.Icc (S c) (S a) := ⟨hSc.le, hSa.le⟩
  obtain ⟨q, hq, hq0⟩ := intermediate_value_Icc' hac (hS.mono hsub) hmem
  exact ⟨q, hq, hq0⟩

/-- **Pure bar-even point (derived from the class).**  Under the keystone
    identification, the zero crossing is a substrate point where the Φ_b
    phase at the identified argument vanishes exactly and the Φ_b value is
    `1` — the bar-odd leak switches off and `c₃ = −Vol(4₁)` is purely
    bar-even there. -/
theorem exists_pure_bar_even (zArg S : ℝ → ℝ)
    [h : SArgumentIdentification zArg S]
    {a c : ℝ} (ha : 1 < a) (hac : a ≤ c) (hSa : 0 < S a) (hSc : S c < 0) :
    ∃ q ∈ Set.Icc a c,
      phase (fibreB q) (zArg q) = 0 ∧ phiB (fibreB q) (zArg q) = 1 := by
  obtain ⟨q, hq, hq0⟩ := exists_zero_crossing h.S_continuousOn ha hac hSa hSc
  have hq1 : 1 < q := lt_of_lt_of_le ha hq.1
  have hphase : phase (fibreB q) (zArg q) = 0 := by
    rw [h.readout q hq1, hq0]
  refine ⟨q, hq, hphase, ?_⟩
  unfold phiB
  rw [hphase]
  simp

end QOU.QBeta.PhiBSArgumentIdentification
