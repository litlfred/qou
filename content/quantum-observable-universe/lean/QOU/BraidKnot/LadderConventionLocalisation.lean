import QOU.BraidKnot.QBetaCategoricalPrecisionLadder

/-!
# The Markov-parameter convention enters the categorical Q_β ladder ONLY at N=1

Bean `qou-cds1` (convention C → D re-derivation of the Q_β precision ladder).

Reading the ladder construction
(`QBetaCategoricalPrecisionLadder.Q_beta_categorical`) factor by factor:

* `N1_factor = cos(alpha − b·ℏ_q²/2)` with `alpha = (markovZ' − 1)·h/2` — the
  **only** factor that reads the Markov parameter `markovZ'`;
* `N2_factor = 1 − b²·ℏ_q⁴`  (`c₂ = −1`),
  `N3_factor = 1 − 2·b³·ℏ_q⁶`  (`c₃ = J_Hopf(1) = −2`),
  `N4_factor`, `N5_factor` — closed forms in `q` through `hoefsmitB q` and
  `hbarQ' q` **alone**, with no `markovZ'` and no `alpha`.

So the whole Markov-parameter-convention dependence of the categorical ladder
is the single N=1 eigenphase. This file states that as an identity: the ladder
is the `φ = alpha q` instance of a phase-parameterised family whose N=2..5 tail
(`ckTail`) is a common factor independent of `φ`.

**Consequence for `qou-cds1`.** A convention change C → D moves the Markov
parameter `z_C ↦ z_D`; on this construction that acts **only** by replacing the
phase `alpha q` with the D-frame mirror-covariant phase `alpha_D − h²/4`
(`QOU.QBeta.phaseTwiceD_sub_hsq_bar_odd`). The categorical `c_k` for `k ≥ 2` are
the z-convention-immune Kashiwara/Hopf tails `b^k·ℏ_q^{2k}` and are **unchanged**.
The S1 sensitivity figure `c₃ ≈ −974` under a naive z-swap is the *extractor*
mis-attributing this single N=1 phase change to the higher rungs — it is not a
change in the categorical `c_k`.

**Scope (honest).** This is a statement about the construction *as coded*: it
localises the z-dependence to N=1 and thereby explains the −974 artifact. It does
**not** claim the physical D re-derivation leaves the Kashiwara tails untouched —
whether `N2..N5` should themselves change under D (if the Kashiwara operators see
the trace normalisation) is the open question recorded in
`docs/audits/2026-08-21-cds1-d-frame-ladder-state-synthesis.md`. All proofs are
`ring`/`unfold`, sorry-free.
-/

namespace QOU.BraidKnot

/-- The N=2..5 tail of the categorical ladder — the product of the rungs whose
    coefficients are the `c_k` (`k ≥ 2`). Each factor is a closed form in `q`
    through `hoefsmitB` and `hbarQ'` alone; none reads the Markov parameter. -/
noncomputable def ckTail (q : ℝ) : ℝ :=
  N2_factor q * N3_factor q * N4_factor q * N5_factor q

/-- The categorical ladder with the single-wrap eigenphase supplied as an
    explicit parameter `φ`. The C-frame instance is `φ = alpha q`; convention D
    supplies the mirror-covariant `alpha_D − h²/4`. Every other input is
    convention-blind. -/
noncomputable def Q_beta_categorical_ofPhase (φ q m_e : ℝ) : ℝ :=
  Q_beta_form_A q m_e * Real.cos (φ - hoefsmitB q * (hbarQ' q) ^ 2 / 2) * ckTail q

/-- **The Markov-parameter convention enters the categorical ladder only through
    the N=1 eigenphase.** `Q_beta_categorical` is exactly the `φ = alpha q`
    instance of `Q_beta_categorical_ofPhase`, whose `ckTail` (rungs N=2..5,
    carrying `c₂ = −1`, `c₃ = −2`, `c₄`, `c₅`) is a factor independent of `φ`. -/
theorem Q_beta_categorical_eq_ofPhase (q m_e : ℝ) :
    Q_beta_categorical q m_e = Q_beta_categorical_ofPhase (alpha q) q m_e := by
  unfold Q_beta_categorical Q_beta_categorical_ofPhase ckTail N1_factor
  ring

/-- **The N=2..5 tail is phase-independent**, hence Markov-convention-blind:
    two phases `φ₁`, `φ₂` yield ladders differing only by their `cos` factors,
    with `ckTail` — and so every categorical `c_k`, `k ≥ 2` — common. Stated in
    the division-free cross-multiplied form. -/
theorem Q_beta_categorical_ofPhase_tail_common (φ₁ φ₂ q m_e : ℝ) :
    Q_beta_categorical_ofPhase φ₁ q m_e
        * Real.cos (φ₂ - hoefsmitB q * (hbarQ' q) ^ 2 / 2)
      = Q_beta_categorical_ofPhase φ₂ q m_e
        * Real.cos (φ₁ - hoefsmitB q * (hbarQ' q) ^ 2 / 2) := by
  unfold Q_beta_categorical_ofPhase
  ring

end QOU.BraidKnot
