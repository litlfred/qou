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

/-! ## The N=2..5 coupling `b` is a convention-D object

`N2..N5` are built from the Hoefsmit coupling `b = hoefsmitB` and `hbarQ'`.
The following ties `b` to the convention-D Wedderburn weights of `H₃(q)`, and the
identity is D-specific (it fails in C). Symbolic cross-check (exact over ℚ(q),
solving the three Markov equations at both `z_C` and `z_D`):
`computations/qbeta/hoefsmit_b_vs_d_weights_probe.py` (7/7). -/

/-- D-frame standard-block `(2,1)` Wedderburn weight of `H₃(q)` (S2 PR #5185,
    `gram-radical-exact`): `y_(2,1)^D = q²/(q²+1)²`. At `z_D = q³/(q²+1)` the
    three Markov equations force `y_(1³) = 0` (two-row Temperley–Lieb) and pin
    this value. -/
noncomputable def stdWeightD (q : ℝ) : ℝ := q ^ 2 / (q ^ 2 + 1) ^ 2

/-- **The Hoefsmit coupling squared is the complement of the D standard-block
    weight: `b² = 1 − y_(2,1)^D`.**

    This is the D-frame structural anchor of the whole `N2..N5` tail: the
    coupling `b` that generates the Kashiwara/Hopf rungs is exactly
    `√(1 − y_(2,1)^D)`. The identity is **convention-D specific** — under C the
    `H₃(q)` weights carry `√q` and keep `y_(1³) ≠ 0`, and `b² ≠ 1 − y_(2,1)^C`
    (`hoefsmit_b_vs_d_weights_probe.py`). So `b`, hence `N2..N5`, is naturally a
    D-frame object, a positive structural reason the categorical tails are
    correctly framed in D (bean `qou-cds1`). -/
theorem hoefsmitB_sq_eq_one_sub_stdWeightD (q : ℝ) :
    hoefsmitB q ^ 2 = 1 - stdWeightD q := by
  unfold hoefsmitB stdWeightD
  have hnn : (0 : ℝ) ≤ q ^ 4 + q ^ 2 + 1 := by positivity
  have hd : (q ^ 2 + 1) ≠ 0 := by positivity
  rw [div_pow, Real.sq_sqrt hnn]
  field_simp
  ring

/-- D-frame trivial-block `(3)` Wedderburn weight (S2): `y_(3)^D = (q⁴+1)/(q²+1)²`. -/
noncomputable def trivWeightD (q : ℝ) : ℝ := (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2

/-- **D-weight normalisation** `y_(3)^D + 2·y_(2,1)^D = 1` (with `y_(1³)^D = 0`):
    the S2 weight vector is a normalised trace on `H₃(q)`. -/
theorem dWeights_normalised (q : ℝ) : trivWeightD q + 2 * stdWeightD q = 1 := by
  unfold trivWeightD stdWeightD
  have hd : (q ^ 2 + 1) ≠ 0 := by positivity
  field_simp
  ring

/-- `y_(3)^D = 1 − 2·y_(2,1)^D` (two-row relation). -/
theorem trivWeightD_eq (q : ℝ) : trivWeightD q = 1 - 2 * stdWeightD q := by
  have := dWeights_normalised q; linarith

/-- **`b² = y_(3)^D + y_(2,1)^D`** — complementary form of
    `hoefsmitB_sq_eq_one_sub_stdWeightD`. -/
theorem hoefsmitB_sq_eq_trivWeightD_add_stdWeightD (q : ℝ) :
    hoefsmitB q ^ 2 = trivWeightD q + stdWeightD q := by
  rw [hoefsmitB_sq_eq_one_sub_stdWeightD, trivWeightD_eq]; ring

/-- **`y_(2,1)^D = 1/[2]_q²`** — the standard-block weight is the Jones-closure
    value, matching the `(q+q⁻¹)²·y₂₁ = 1` conclusion of
    `QOU.BraidsAndKnots.markovWeights_eq_jones_of_threeRow_eq_zero`. -/
theorem stdWeightD_eq_jones (q : ℝ) (hq : q ≠ 0) :
    stdWeightD q = 1 / (q + q⁻¹) ^ 2 := by
  unfold stdWeightD
  have hd : (q ^ 2 + 1) ≠ 0 := by positivity
  field_simp

/-- **The S2 D-weights solve the σ Markov equation at `z_D = q³/(q²+1)`:**
    `q·y_(3)^D + (q−q⁻¹)·y_(2,1)^D = z_D` (with `y_(1³)^D = 0`). Formalises the
    S2 symbolic solution (`gram-radical-exact`) in Lean. -/
theorem dWeights_markov_sigma (q : ℝ) (hq : q ≠ 0) :
    q * trivWeightD q + (q - q⁻¹) * stdWeightD q = q ^ 3 / (q ^ 2 + 1) := by
  unfold trivWeightD stdWeightD
  have hd : (q ^ 2 + 1) ≠ 0 := by positivity
  field_simp
  ring

/-- **The S2 D-weights solve the σσ Markov equation at `z_D`:**
    `q²·y_(3)^D − y_(2,1)^D = z_D²`. -/
theorem dWeights_markov_sigmasigma (q : ℝ) :
    q ^ 2 * trivWeightD q + (-1) * stdWeightD q = (q ^ 3 / (q ^ 2 + 1)) ^ 2 := by
  unfold trivWeightD stdWeightD
  have hd : (q ^ 2 + 1) ≠ 0 := by positivity
  field_simp
  ring

/-- The D-weights and coupling at the classical point `q = 1`:
    `y_(2,1)^D = ¼`, `y_(3)^D = ½`, `b² = ¾`. (`c₃`'s value at `q=1`,
    `J_Hopf(1) = −2`, is a **topological input** — the Jones polynomial of the
    Hopf link — NOT derivable from these weights; there is no forced-`c₃` lemma.
    The provable D-structure is the weight/coupling algebra above.) -/
theorem dWeights_at_one :
    stdWeightD 1 = 1 / 4 ∧ trivWeightD 1 = 1 / 2 ∧ hoefsmitB 1 ^ 2 = 3 / 4 := by
  refine ⟨by norm_num [stdWeightD], by norm_num [trivWeightD], ?_⟩
  rw [hoefsmitB_sq_eq_one_sub_stdWeightD]; norm_num [stdWeightD]

/-! ## The D-frame N=2 rung is forced — `b² = [3]_q / [2]_q²`

Bean `qou-cds1` asks, as its own named next step, to *"state the invariant a
forced D `c₂` must satisfy (D analogue of `c₂ = −1 = 1 − b²ℏ⁴`) and check if
exact weights + `α_D − h²/4` determine it"*.

The answer is that the **phase leg does not enter at all**, and the weight leg
determines the rung completely. `Q_beta_categorical_ofPhase_tail_common` (above)
already localises every `z`-dependence to the `N=1` phase, so `α_D − h²/4` is
irrelevant to `N2_factor`. And `stdWeightD_eq_jones` pins `y_(2,1)^D = 1/[2]_q²`,
so with `hoefsmitB_sq_eq_one_sub_stdWeightD` the coupling collapses to a bare
quantum-integer ratio, via the identity `[2]_q² − [3]_q = 1`.

So under D there is **no free parameter in the `N=2` rung**: `b` is not an
independent Hoefsmit input but a function of the D weights, which are themselves
forced. This is the contrast with C, where `b² ≠ 1 − y_(2,1)^C` and the coupling
is genuinely separate data.

**Scope.** This states and settles the invariant for `c₂` ONLY. It says nothing
about `c₃`/`c₄`/`c₅`, whose values remain fitted near-matches (see
`dWeights_at_one`), and it closes no part of the numerical gap — the `41.94×C`
residual recorded in `qou-cds1` is untouched. What it removes is the possibility
that a D-frame `c₂` could be *chosen*.
-/

/-- **`[2]_q² − [3]_q = 1`** — the quantum-integer identity behind the collapse
    below. With `[2]_q = q + q⁻¹` and `[3]_q = q² + 1 + q⁻²`:
    `(q + q⁻¹)² = q² + 2 + q⁻²`, so subtracting `[3]_q` leaves exactly `1`. -/
theorem bracketTwo_sq_sub_bracketThree_eq_one (q : ℝ) (hq : q ≠ 0) :
    (q + q⁻¹) ^ 2 - (q ^ 2 + 1 + (q ^ 2)⁻¹) = 1 := by
  field_simp
  ring

/-- **`b² = [3]_q / [2]_q²`** — the Hoefsmit coupling squared IS a quantum-integer
    ratio in the D frame.

    Immediate from `hoefsmitB_sq_eq_one_sub_stdWeightD` (`b² = 1 − y_(2,1)^D`)
    and `stdWeightD_eq_jones` (`y_(2,1)^D = 1/[2]_q²`), using
    `bracketTwo_sq_sub_bracketThree_eq_one`. -/
theorem hoefsmitB_sq_eq_bracketThree_div_bracketTwo_sq (q : ℝ) (hq : q ≠ 0) :
    hoefsmitB q ^ 2 = (q ^ 2 + 1 + (q ^ 2)⁻¹) / (q + q⁻¹) ^ 2 := by
  rw [hoefsmitB_sq_eq_one_sub_stdWeightD]
  unfold stdWeightD
  have hd : (q ^ 2 + 1) ≠ 0 := by positivity
  field_simp
  ring

/-- **The `N=2` rung is a function of `q` alone in the D frame** — no free
    parameter. `N2_factor = 1 − ([3]_q/[2]_q²)·ℏ_q⁴`, with the coupling supplied
    by the forced D weights rather than assumed. -/
theorem N2_factor_eq_bracketRatio (q : ℝ) (hq : q ≠ 0) :
    N2_factor q = 1 - ((q ^ 2 + 1 + (q ^ 2)⁻¹) / (q + q⁻¹) ^ 2) * (hbarQ' q) ^ 4 := by
  unfold N2_factor
  rw [hoefsmitB_sq_eq_bracketThree_div_bracketTwo_sq q hq]

end QOU.BraidKnot
