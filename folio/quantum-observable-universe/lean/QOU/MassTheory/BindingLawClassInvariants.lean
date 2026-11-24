import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Topology.Instances.RealVectorSpace
import Mathlib.Tactic

/-!
# What the two-nucleon binding LAW can and cannot change

Owner ask (2026-10-11, "explore all", item 3, "the binding law"). The working law
`B = E₀ · ln(tr_free/tr_atom) = −α · ln μ` is tagged **POSITED** by
`computations/mass_binding_dashboard.py` ("no block in the corpus licenses α·ln(ratio) as an
energy"). This file proves three things about the space of candidate laws. None of them
selects a law, and nothing here asserts a value of any trace.

## 1. Additivity forces the logarithm — conditionally, and only up to a free constant

`binding_canonical.py` asserts that `log` "is forced rather than chosen (`log` is the unique
multiplicative-to-additive map)", and `binding_functional_extensivity_probe.py` records that
the uniqueness half of that argument is classical and **not in Lean**
(`QOU.Mass.MarkovBondRuleForcesPairwise` deliberately avoids needing it). It is proved here:

* `eq_mul_log_of_logAdditive_of_continuousOn` — if `f : ℝ → ℝ` satisfies
  `f (x*y) = f x + f y` for `x, y > 0` and is continuous on `(0, ∞)`, then
  `f x = c · log x` on `(0, ∞)` with `c = f e`.

The three premises are all explicit and none is established here: (i) the binding is a
function of the trace ratio **alone** (`L_diff = E₀(tr_free − tr_atom)` and the
`Δ_λ`-weighted functional below are not); (ii) binding is additive over blocks whose traces
multiply (the Markov bond product, `tr_stabWord_eq_prod_tr`, supplies the multiplying half);
(iii) regularity. Without (iii) Hamel-basis solutions exist (not proved here).

What the theorem does **not** do: `cauchy_admits_every_constant` shows every `c ∈ ℝ`,
including `c = 0` and both signs, satisfies all the hypotheses. So additivity fixes the
*shape* and fixes neither the scale nor the trace→energy direction — which is exactly the
open direction recorded in `QOU.Hecke.TwistSplitSignDictionary`.

## 2. Within the class `B = F(μ)`, signs and ordering do not depend on the law

For every `F` strictly antitone on `(0, ∞)` with `F 1 = 0` — the log law, the Mayer
two-body term `α(1 − μ)`, and every other decreasing function of the ratio vanishing at the
free point —

* `pos_iff_lt_one` / `neg_iff_one_lt`: the sign of `B` is the sign of `1 − μ`;
* `lt_iff_gt_ratio`: the channel ORDER is the reverse order of `μ`;
* `projector_channels_both_bind`: under the isospin projector decomposition
  `μ₊ + μ₋ = 1` (`QOU.QBeta.InterfaceScalar.mu_sum_eq_one`) with both channels positive,
  **both** channels bind.

And reversing the direction does not help: `projector_channels_same_sign` shows that for any
`F` strictly monotone *either way* with `F 1 = 0`, the two projector channels have the
**same** sign. So no law of the form `F(μ)` produces one bound and one unbound projector
channel. Changing the law inside this class can only rescale magnitudes; the two-nucleon
sign pattern and ordering are properties of the channel **ratios**, i.e. of the composition
and the letters, never of `F`.

## 3. The `Δ_λ`-weighted functional leaves the class, and splits the channels

The corpus also states `B(K) = m_e · Σ_λ y_λ χ^λ(K) Δ_λ` with
`Δ_λ = (−1)^{n(λ)} dim V_λ` (value proved: `dtEuler_eq_deltaLambda_unconditional`; the LAW is
posited — `computations/delta-lambda-witness.json` caveat: "NOT a binding energy"). At
`n = 2`, `Δ_(2) = +1` and `Δ_(1,1) = −1`, and this functional is linear, not a function of the
ratio. On the projectors:

* `phi_Pplus` : `Φ(P₊) = y_(2)` and `phi_Pminus` : `Φ(P₋) = −y_(1,1)` — opposite signs,
  because the antisymmetric block carries `Δ = −1`;
* read as a **difference** against the free element `1`
  (`phi_one_sub_Pplus`, `phi_one_sub_Pminus`): `Φ(1) − Φ(P₊) = −y_(1,1)`,
  `Φ(1) − Φ(P₋) = y_(2)` — opposite signs again, **swapped**.

So this is the one corpus formula under which the projector decomposition yields a bound and
an unbound channel, and which channel is bound flips with the reading (direct vs.
difference). The corpus fixes neither reading; choosing one because its signs match the
two-nucleon spectrum would be selection against the target.

Probe: `computations/probes/two_nucleon_binding_law_comparison_probe.py` (all laws on the
same exact channel data). Base ring (§7c): §3 is over a generic field / ordered field; `ℝ`
enters only where `Real.log` and `Real.exp` do (§1, §2).
-/

namespace QOU.Mass.BindingLawClassInvariants

open Real Set

/-! ## §1 Cauchy: additivity on products + continuity ⇒ `c · log` -/

/-- The multiplicative-to-additive property on the positive reals. -/
def IsLogAdditiveOnPos (f : ℝ → ℝ) : Prop :=
  ∀ x y : ℝ, 0 < x → 0 < y → f (x * y) = f x + f y

theorem map_one_eq_zero {f : ℝ → ℝ} (hf : IsLogAdditiveOnPos f) : f 1 = 0 := by
  have h := hf 1 1 one_pos one_pos
  rw [mul_one] at h
  linarith

/-- **Additivity + continuity force the logarithm.** Any continuous solution of
`f (x*y) = f x + f y` on `(0, ∞)` is `c · log` with `c = f e`. -/
theorem eq_mul_log_of_logAdditive_of_continuousOn {f : ℝ → ℝ}
    (hf : IsLogAdditiveOnPos f) (hc : ContinuousOn f (Ioi 0)) :
    ∀ x : ℝ, 0 < x → f x = f (exp 1) * log x := by
  let g : ℝ →+ ℝ :=
    { toFun := fun t => f (exp t)
      map_zero' := by simp [map_one_eq_zero hf]
      map_add' := by
        intro s t
        simp only [exp_add]
        exact hf _ _ (exp_pos s) (exp_pos t) }
  have hg : Continuous g :=
    hc.comp_continuous continuous_exp (fun t => exp_pos t)
  have hlin : ∀ t : ℝ, f (exp t) = t * f (exp 1) := by
    intro t
    have h := map_real_smul g hg t 1
    simpa [g, smul_eq_mul] using h
  intro x hx
  rw [← exp_log hx, hlin, exp_log hx, mul_comm]

/-- **Additivity does not fix the constant.** Every `c · log`, for every real `c`, satisfies
both hypotheses — so the sign (trace→energy direction) and the scale stay free. -/
theorem cauchy_admits_every_constant (c : ℝ) :
    IsLogAdditiveOnPos (fun x => c * log x) ∧ ContinuousOn (fun x => c * log x) (Ioi 0) := by
  refine ⟨?_, ?_⟩
  · intro x y hx hy
    simp only
    rw [log_mul hx.ne' hy.ne']
    ring
  · exact continuousOn_const.mul (continuousOn_log.mono (fun x hx => (ne_of_gt hx)))

/-! ## §2 Law-class invariants for `B = F(μ)` -/

section Class

variable {F : ℝ → ℝ}

/-- The sign of the binding is the sign of `1 − μ`, for every strictly decreasing law
vanishing at the free point. -/
theorem pos_iff_lt_one (hF : StrictAntiOn F (Ioi 0)) (h1 : F 1 = 0) {μ : ℝ} (hμ : 0 < μ) :
    0 < F μ ↔ μ < 1 := by
  have h1m : (1 : ℝ) ∈ Ioi (0 : ℝ) := by simp
  constructor
  · intro h
    by_contra hge
    push_neg at hge
    rcases hge.lt_or_eq with hlt | heq
    · have := hF h1m hμ hlt
      linarith
    · rw [← heq] at h; linarith
  · intro hlt
    have := hF hμ h1m hlt
    linarith

theorem neg_iff_one_lt (hF : StrictAntiOn F (Ioi 0)) (h1 : F 1 = 0) {μ : ℝ} (hμ : 0 < μ) :
    F μ < 0 ↔ 1 < μ := by
  have h1m : (1 : ℝ) ∈ Ioi (0 : ℝ) := by simp
  constructor
  · intro h
    by_contra hle
    push_neg at hle
    rcases hle.lt_or_eq with hlt | heq
    · have := hF hμ h1m hlt
      linarith
    · rw [heq] at h; linarith
  · intro hlt
    have := hF h1m hμ hlt
    linarith

/-- **The ordering is the law's business only through `μ`.** Channel `1` binds less than
channel `2` iff its ratio is larger — for every strictly decreasing law. -/
theorem lt_iff_gt_ratio (hF : StrictAntiOn F (Ioi 0)) {μ₁ μ₂ : ℝ} (h₁ : 0 < μ₁) (h₂ : 0 < μ₂) :
    F μ₁ < F μ₂ ↔ μ₂ < μ₁ :=
  hF.lt_iff_gt h₁ h₂

/-- **Under the projector decomposition every decreasing law binds both channels.** -/
theorem projector_channels_both_bind (hF : StrictAntiOn F (Ioi 0)) (h1 : F 1 = 0)
    {μp μm : ℝ} (hsum : μp + μm = 1) (hp : 0 < μp) (hm : 0 < μm) :
    0 < F μp ∧ 0 < F μm :=
  ⟨(pos_iff_lt_one hF h1 hp).2 (by linarith), (pos_iff_lt_one hF h1 hm).2 (by linarith)⟩

/-- Reversing the trace→energy direction (an increasing law) unbinds both channels. -/
theorem projector_channels_both_unbound (hF : StrictMonoOn F (Ioi 0)) (h1 : F 1 = 0)
    {μp μm : ℝ} (hsum : μp + μm = 1) (hp : 0 < μp) (hm : 0 < μm) :
    F μp < 0 ∧ F μm < 0 := by
  have h1m : (1 : ℝ) ∈ Ioi (0 : ℝ) := by simp
  refine ⟨?_, ?_⟩
  · have := hF hp h1m (by linarith : μp < 1); linarith
  · have := hF hm h1m (by linarith : μm < 1); linarith

/-- **No law of the ratio alone splits the projector channels.** For `F` strictly monotone
in either direction with `F 1 = 0`, the two channels have the same sign. -/
theorem projector_channels_same_sign (hF : StrictAntiOn F (Ioi 0) ∨ StrictMonoOn F (Ioi 0))
    (h1 : F 1 = 0) {μp μm : ℝ} (hsum : μp + μm = 1) (hp : 0 < μp) (hm : 0 < μm) :
    (0 < F μp ↔ 0 < F μm) := by
  rcases hF with hA | hM
  · obtain ⟨a, b⟩ := projector_channels_both_bind hA h1 hsum hp hm
    exact ⟨fun _ => b, fun _ => a⟩
  · obtain ⟨a, b⟩ := projector_channels_both_unbound hM h1 hsum hp hm
    exact ⟨fun h => absurd h (not_lt.mpr a.le), fun h => absurd h (not_lt.mpr b.le)⟩

end Class

/-- The log law `B = −c · ln μ`, `c > 0`, is in the class. -/
theorem negLog_strictAntiOn {c : ℝ} (hc : 0 < c) :
    StrictAntiOn (fun μ => -c * log μ) (Ioi 0) := by
  intro a ha b hb hab
  have := strictMonoOn_log ha hb hab
  simp only
  nlinarith

/-- The Mayer two-body law `B = c(1 − μ)`, `c > 0`, is in the class. -/
theorem mayer_strictAntiOn {c : ℝ} (hc : 0 < c) :
    StrictAntiOn (fun μ => c * (1 - μ)) (Ioi 0) := by
  intro a _ b _ hab
  simp only
  nlinarith

/-- **Concrete instance.** Under the projector decomposition the log law binds both channels,
for every positive scale. -/
theorem negLog_projector_both_bind {c μp μm : ℝ} (hc : 0 < c) (hsum : μp + μm = 1)
    (hp : 0 < μp) (hm : 0 < μm) : 0 < -c * log μp ∧ 0 < -c * log μm :=
  projector_channels_both_bind (F := fun μ => -c * log μ) (negLog_strictAntiOn hc)
    (by simp) hsum hp hm

/-- Same for the Mayer two-body law. -/
theorem mayer_projector_both_bind {c μp μm : ℝ} (hc : 0 < c) (hsum : μp + μm = 1)
    (hp : 0 < μp) (hm : 0 < μm) : 0 < c * (1 - μp) ∧ 0 < c * (1 - μm) :=
  projector_channels_both_bind (F := fun μ => c * (1 - μ)) (mayer_strictAntiOn hc)
    (by simp) hsum hp hm

/-! ## §3 The `Δ_λ`-weighted functional at `n = 2` -/

section Frobenius

variable {K : Type*} [Field K]

/-- `χ^(2)` on `a·1 + b·σ` (σ acts by `q` on the symmetric block). -/
def chiSym (q a b : K) : K := a + b * q

/-- `χ^(1,1)` on `a·1 + b·σ` (σ acts by `−q⁻¹` on the antisymmetric block). -/
def chiAlt (qi a b : K) : K := a - b * qi

/-- `Φ = Σ_λ y_λ χ^λ Δ_λ` at `n = 2`, with `Δ_(2) = +1`, `Δ_(1,1) = −1`. -/
def phi (q qi y2 y11 a b : K) : K := y2 * chiSym q a b - y11 * chiAlt qi a b

/-- `Φ(P₊) = y_(2)`, `P₊ = s(σ + q⁻¹)`. -/
theorem phi_Pplus (q qi s y2 y11 : K) (hs : s * (q + qi) = 1) :
    phi q qi y2 y11 (s * qi) s = y2 := by
  unfold phi chiSym chiAlt
  rw [show y2 * (s * qi + s * q) - y11 * (s * qi - s * qi) = y2 * (s * (q + qi)) by ring, hs,
    mul_one]

/-- `Φ(P₋) = −y_(1,1)`, `P₋ = s(q − σ)`. -/
theorem phi_Pminus (q qi s y2 y11 : K) (hs : s * (q + qi) = 1) :
    phi q qi y2 y11 (s * q) (-s) = -y11 := by
  unfold phi chiSym chiAlt
  rw [show y2 * (s * q + -s * q) - y11 * (s * q - -s * qi) = -(y11 * (s * (q + qi))) by ring,
    hs, mul_one]

/-- Difference reading, `T = 1`: `Φ(1) − Φ(P₊) = −y_(1,1)`. -/
theorem phi_one_sub_Pplus (q qi s y2 y11 : K) (hs : s * (q + qi) = 1) :
    phi q qi y2 y11 1 0 - phi q qi y2 y11 (s * qi) s = -y11 := by
  rw [phi_Pplus q qi s y2 y11 hs]
  unfold phi chiSym chiAlt
  ring

/-- Difference reading, `T = 0`: `Φ(1) − Φ(P₋) = y_(2)`. -/
theorem phi_one_sub_Pminus (q qi s y2 y11 : K) (hs : s * (q + qi) = 1) :
    phi q qi y2 y11 1 0 - phi q qi y2 y11 (s * q) (-s) = y2 := by
  rw [phi_Pminus q qi s y2 y11 hs]
  unfold phi chiSym chiAlt
  ring

variable [LinearOrder K] [IsStrictOrderedRing K]

/-- **The `Δ`-weighted functional splits the projector channels, in both readings, with the
bound channel swapped between them.** With positive Markov weights:
direct reading — `T = 1` positive, `T = 0` negative; difference reading — `T = 1` negative,
`T = 0` positive. -/
theorem phi_splits_channels (q qi s y2 y11 : K) (hs : s * (q + qi) = 1)
    (h2 : 0 < y2) (h11 : 0 < y11) :
    (0 < phi q qi y2 y11 (s * qi) s ∧ phi q qi y2 y11 (s * q) (-s) < 0) ∧
    (phi q qi y2 y11 1 0 - phi q qi y2 y11 (s * qi) s < 0 ∧
      0 < phi q qi y2 y11 1 0 - phi q qi y2 y11 (s * q) (-s)) := by
  rw [phi_one_sub_Pplus q qi s y2 y11 hs, phi_one_sub_Pminus q qi s y2 y11 hs,
    phi_Pplus q qi s y2 y11 hs, phi_Pminus q qi s y2 y11 hs]
  exact ⟨⟨h2, by linarith⟩, ⟨by linarith, h2⟩⟩

end Frobenius

end QOU.Mass.BindingLawClassInvariants
