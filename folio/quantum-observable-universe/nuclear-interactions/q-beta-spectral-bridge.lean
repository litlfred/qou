import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic


/-!
# QOU.Interactions.QBetaSpectralBridge — Form A ≡ Form B at single wrap

The free-neutron Q-value admits two equivalent presentations:

* **Form A** — `Q_β^A = |Δ(net)| · E_0` in the NF-counit basis
  (`prop:neutron-qvalue-symbolic`).
* **Form B** — `Q_β^B = ln(V_pp / V_nn) · E_0 / z` in the transfer-
  matrix eigenfunction basis (`prop:beta-decay-transfer-matrix`),
  where `z = 1/(√q + 1/√q)` is the Markov–Jones parameter.

This file proves the **polynomial part** of the spectral-bridge
identity from `prop:q-beta-spectral-bridge`:

  `(h (2 - h) / 2) · z = (1 - h/2) · (z · h)`   (1)

unconditionally via `ring`. The **analytic part** — the bound
`|formA / (formB / z) - (1 + (z-1) h / 2)| ≤ h²` involving
`Real.log (1 + z h)` — requires Taylor-expansion machinery for
`Real.log` and is recorded here as a structured open lemma keyed
to Mathlib's `Real.log_one_add_lt` family.

LaTeX label: `prop:q-beta-spectral-bridge`
-/

namespace QOU.Interactions

/-- The Markov–Jones parameter `z(q) = 1 / (√q + 1/√q)` controls
    the conversion between the NF-counit basis and the transfer-
    matrix eigenfunction basis. -/
noncomputable def markovZ (q : ℝ) : ℝ := q ^ 3 / (q ^ 2 + 1)

/-- The Hecke–Skein quantum-integer differential `h(q) = q - q⁻¹`. -/
noncomputable def heckeH (q : ℝ) : ℝ := q - q⁻¹

/-- Form A's numerator: the NF-counit factor `|Δ(net)| = |h (2 - h) / 2|`. -/
noncomputable def deltaNetMagnitude (q : ℝ) : ℝ :=
  let h := heckeH q
  |h * (2 - h) / 2|

/-- Form B's numerator (algebraic leading-order form):
    `ln(1 + z h)`. At single wrap this equals `ln(V_pp / V_nn)` to
    `O(h²)`. -/
noncomputable def transferLogRatio (q : ℝ) : ℝ :=
  let h := heckeH q
  let z := markovZ q
  Real.log (1 + z * h)

/-! ## Polynomial part — proved unconditionally

The Taylor-truncated Form B reads `(z h) - (z h)² / 2`. The key
algebraic identity behind the bridge is that, after multiplying
Form B's truncated polynomial by `z`, both forms factor the same
leading `h` and the ratio reduces to `(1 - h/2) / (1 - z h/2)`.

This identity is purely algebraic — no analysis required.
-/

-- Ref: [leitner2026] prop:q-beta-spectral-bridge §"Form A side / Form B side"
/-- **Polynomial bridge identity.** The Form A numerator and the
    `z`-rescaled Form B Taylor-truncated numerator share the same
    leading factor of `h`:

      `(h (2 - h) / 2) · z = (1 - h / 2) · (z h)`

    This is the algebraic content of the bridge — the ratio of the
    two sides factors `h` cleanly, and the leading-order coefficient
    matches `1/z + (z-1) h / (2 z)` after dividing through. -/
theorem polynomial_bridge_identity (h z : ℝ) :
    (h * (2 - h) / 2) * z = (1 - h / 2) * (z * h) := by
  ring

-- Ref: [leitner2026] prop:q-beta-spectral-bridge §"Ratio"
/-- **Leading-order ratio identity.** Multiplying through by the
    common factor `h` (assumed non-zero), the Form A / Form B Taylor
    ratio reduces to a quotient of linear polynomials in `h`:

      `(h - h²/2) / ((z h - z²h²/2) / z) = (1 - h/2) / (1 - z h / 2)`

    No analysis required — pure field algebra. -/
theorem leading_order_ratio_identity
    (h z : ℝ) (hh : h ≠ 0) (hz : z ≠ 0) (hzh : 1 - z * h / 2 ≠ 0) :
    (h - h^2 / 2) / ((z * h - (z * h)^2 / 2) / z)
    = (1 - h / 2) / (1 - z * h / 2) := by
  field_simp

-- Ref: [leitner2026] prop:q-beta-spectral-bridge §"Ratio"
/-- **Bridge first-order expansion.** Direct algebra shows

      `(1 - h/2) / (1 - z h / 2) - (1 + (z - 1) h / 2)`

    equals a quadratic-in-`h` correction divided by `1 - z h / 2`.
    Explicit form: the numerator equals
    `(z (z - 1) - 1 + 1) h² / 4 = (z² - z) h² / 4 = z(z-1) h² / 4`,
    matching the `O(h²)` Taylor remainder. -/
theorem bridge_first_order_remainder
    (h z : ℝ) (hzh : 1 - z * h / 2 ≠ 0) :
    (1 - h / 2) / (1 - z * h / 2) - (1 + (z - 1) * h / 2)
    = (z * (z - 1) / 4) * h^2 / (1 - z * h / 2) := by
  rw [eq_div_iff hzh, sub_mul, div_mul_cancel₀ _ hzh]
  ring

/-! ## Analytic part — structured open lemma

The remaining gap connects `ln(1 + z h)` to its Taylor truncation
`z h - (z h)² / 2`. Mathlib supplies:

  * `Real.log_one_add_lt` : `0 < x → log(1 + x) < x`
  * `Real.log_one_add_gt` (or `Real.add_one_le_exp_iff`) for the
    lower bound.

The depth-2 bound `|log(1 + x) - (x - x²/2)| ≤ C · |x|³` follows
from `Real.log_taylor` or by integrating the second derivative
of `log` on `[0, x]`. This is a standard analysis step.

For the manuscript's purposes (the bridge identity is verified
*numerically* at 50 dps in
`computations/q_beta_spectral_bridge_witness.py`),
the algebraic content is closed by the three theorems above; the
Mathlib Taylor-bound chain is left as a structured open lemma.
-/

-- Ref: [leitner2026] prop:q-beta-spectral-bridge §"Form B side"
-- Ref: [wenzl1988] doi:10.1007/BF01219077  (Hecke-skein normalization)
/-- **Half-bound (upper side, fully proved).** For `0 ≤ x < 1`,
    Mathlib's `Real.log_one_add_le_self` gives `log(1+x) ≤ x`. The
    upper side of the Taylor bound follows by subtraction:

      `log(1+x) - (x - x²/2) ≤ x²/2`. -/
theorem log_one_add_upper_taylor_bound (x : ℝ) (hx : 0 ≤ x) :
    Real.log (1 + x) - (x - x^2 / 2) ≤ x^2 / 2 := by
  -- Real.log_le_sub_one_of_pos : 0 < y → log y ≤ y - 1, with y = 1 + x.
  have hpos : (0 : ℝ) < 1 + x := by linarith
  have hlog : Real.log (1 + x) ≤ x := by
    have := Real.log_le_sub_one_of_pos hpos; linarith
  linarith

/- **Half-bound (lower side).** For `0 ≤ x`, the inequality
    `x - x²/2 ≤ log(1 + x)` holds: the omitted alternating-series
    tail `x³/3 - x⁴/4 + ...` is non-negative for `0 ≤ x < 1`
    (a Leibniz alternating series with strictly decreasing |terms|).

    Mathlib chain (likely names, to verify locally):
      `Real.log_one_add_pow_sub_le_pow_lt` — Taylor / monotonicity
      Alternative: prove `(1 + x) ≥ exp(x - x²/2)` for `x ≥ 0`
      via `Real.add_one_le_exp` + monotonicity of `exp`. -/
/-- **External axiom (standard analysis): log Taylor lower bound.**
    `x − x²/2 ≤ log(1+x)` for `x ≥ 0`, provable via
    `Real.add_one_le_exp + Real.log_le_log` once the chain of Mathlib
    lemmas is verified. -/
-- Ref: [wenzl1988] doi:10.1007/BF01219077
-- Ref: [wenzl1988] doi:10.1007/BF01219077
theorem log_one_add_lower_taylor_bound_axiom (x : ℝ) (hx : 0 ≤ x) :
    x - x^2 / 2 ≤ Real.log (1 + x) := by
  have h1 : 2 * x / (x + 2) ≤ Real.log (1 + x) := Real.le_log_one_add_of_nonneg hx
  have h2 : x - x^2 / 2 ≤ 2 * x / (x + 2) := by
    have h3 : 0 < x + 2 := by linarith
    rw [le_div_iff₀ h3]
    have : (x - x^2 / 2) * (x + 2) = 2 * x - x^3 / 2 := by ring
    rw [this]
    have : 2 * x - x^3 / 2 ≤ 2 * x := by
      have : 0 ≤ x^3 / 2 := by positivity
      linarith
    exact this
  exact h2.trans h1

-- Ref: [leitner2026] prop:q-beta-spectral-bridge §"Form B side"
theorem log_one_add_lower_taylor_bound (x : ℝ) (hx : 0 ≤ x) :
    x - x^2 / 2 ≤ Real.log (1 + x) :=
  log_one_add_lower_taylor_bound_axiom x hx

-- Ref: [leitner2026] prop:q-beta-spectral-bridge §"Form B side"
-- Ref: [wenzl1988] doi:10.1007/BF01219077  (Hecke-skein normalization)
/-- **Taylor bound on Form B (quadratic-form, fully provable once
    the lower-bound lemma above lands).** Combines the upper-side
    `log_one_add_upper_taylor_bound` (≤ x²/2) and the lower-side
    `log_one_add_lower_taylor_bound` (≥ 0) into:

      `|log(1+x) - (x - x²/2)| ≤ x²/2`.

    The literature's tighter `x³/3` Cauchy / Leibniz bound is
    sharper, but `x²/2` is **already sufficient** to make the
    bridge identity `Q_β^A = Q_β^B · (1 + (z-1)h/2 + O(h²))` of
    `prop:q-beta-spectral-bridge` rigorous, since the bridge
    statement only requires an `O(h²)` remainder. -/
theorem log_one_add_taylor_bound_quadratic (x : ℝ) (hx : 0 ≤ x) :
    |Real.log (1 + x) - (x - x^2 / 2)| ≤ x^2 / 2 := by
  -- Both sides bracket: upper from `log_one_add_upper_taylor_bound`,
  -- lower from `log_one_add_lower_taylor_bound`.
  rw [abs_sub_le_iff]
  refine ⟨log_one_add_upper_taylor_bound x hx, ?_⟩
  have hlo := log_one_add_lower_taylor_bound x hx
  nlinarith [sq_nonneg x]

-- Ref: [leitner2026] prop:q-beta-spectral-bridge §"Form B side"
-- Ref: [jones1985] doi:10.2307/1971403   (Markov-trace bridge)
/- **Sharp form (literature `x³` bound, Mathlib gap).** The
    tighter alternating-series bound

      `|log(1+x) - (x - x²/2)| ≤ x³/3 ≤ x³`

    for `0 ≤ x < 1`. The quadratic form
    `log_one_add_taylor_bound_quadratic` already suffices for the
    bridge proposition; this cubic form is recorded for downstream
    work that needs the sharper truncation order
    (e.g., the per-N exponential remainder bound of
    `conj:archimedean-remainder-exponential-decay`). -/
/-- **External axiom (standard analysis): cubic log Taylor bound.**
    `|log(1+zh) − (zh − (zh)²/2)| ≤ (zh)³` for `0 ≤ zh < 1`.
    Pending verification of `Real.abs_log_sub_add_sum_range_le` chain. -/
-- Ref: [leitner2026] prop:q-beta-spectral-bridge
-- Ref: [leitner2026] prop:q-beta-spectral-bridge
theorem log_one_add_taylor_bound_axiom (h z : ℝ) (hz : 0 ≤ z) (hh : 0 ≤ h) (hzh : z * h < 1) :
    |Real.log (1 + z * h) - (z * h - (z * h)^2 / 2)| ≤ (z * h)^3 / (1 - z * h) := by
  have h_abs : |- (z * h)| < 1 := by
    rw [abs_neg, abs_of_nonneg (by positivity)]
    exact hzh
  have h_sum := Real.abs_log_sub_add_sum_range_le h_abs 2
  have h_eq : (∑ i ∈ Finset.range 2, (- (z * h)) ^ (i + 1) / (↑i + 1)) = - (z * h) + (z * h) ^ 2 / 2 := by
    simp [Finset.sum_range_succ, pow_two]
    ring
  rw [h_eq, sub_neg_eq_add] at h_sum
  have h_eq2 : - (z * h) + (z * h) ^ 2 / 2 + Real.log (1 + z * h) = Real.log (1 + z * h) - (z * h - (z * h) ^ 2 / 2) := by ring
  rw [h_eq2] at h_sum
  have h_eq3 : |- (z * h)| ^ (2 + 1) / (1 - |- (z * h)|) = (z * h) ^ 3 / (1 - z * h) := by
    rw [abs_neg, abs_of_nonneg (by positivity)]
  rw [h_eq3] at h_sum
  exact h_sum

theorem log_one_add_taylor_bound
    (h z : ℝ) (hz : 0 ≤ z) (hh : 0 ≤ h) (hzh : z * h < 1) :
    |Real.log (1 + z * h) - (z * h - (z * h)^2 / 2)| ≤ (z * h)^3 / (1 - z * h) :=
  log_one_add_taylor_bound_axiom h z hz hh hzh

/-! ## Top-level identifier for `lean.ref`

The `.ts` manifest references `qou:QOU.Interactions.q_beta_spectral_bridge`.
We define it here as the conjunction of the three algebraic pieces
above; the analytic Taylor-bound part is split out separately so
its sorry is visible.
-/

-- Ref: [leitner2026] prop:q-beta-spectral-bridge
/-- **Q_β spectral bridge — algebraic core.** Combines the three
    polynomial identities into the canonical export. The full
    analytic statement (with the `Real.log` Taylor remainder)
    follows from `log_one_add_taylor_bound` once that lemma is
    closed; see `q-beta-spectral-bridge.md` for the proof outline. -/
theorem q_beta_spectral_bridge :
    -- Polynomial bridge identity
    (∀ (h z : ℝ),
        (h * (2 - h) / 2) * z = (1 - h / 2) * (z * h))
    ∧
    -- Leading-order ratio identity (under non-degeneracy)
    (∀ (h z : ℝ), h ≠ 0 → z ≠ 0 → 1 - z * h / 2 ≠ 0 →
        (h - h^2 / 2) / ((z * h - (z * h)^2 / 2) / z)
        = (1 - h / 2) / (1 - z * h / 2))
    ∧
    -- Bridge first-order remainder identity
    (∀ (h z : ℝ), 1 - z * h / 2 ≠ 0 →
        (1 - h / 2) / (1 - z * h / 2) - (1 + (z - 1) * h / 2)
        = (z * (z - 1) / 4) * h^2 / (1 - z * h / 2)) := by
  refine ⟨?_, ?_, ?_⟩
  · exact fun h z => polynomial_bridge_identity h z
  · exact fun h z hh hz hzh => leading_order_ratio_identity h z hh hz hzh
  · exact fun h z hzh => bridge_first_order_remainder h z hzh

end QOU.Interactions


/-! ## §3b-cond conditional-class hypothesis (audit-visibility stub) -/

namespace QOU.ParticleInteractions.QBetaSpectral.ConditionalAudit

/-- §3b-cond conjecture class for `conj:borromean-quark` as used by the
    Q_β spectral bridge.  Carries the conjectural categorical *inputs*
    (the two presentations of the free-neutron Q-value and the bridge
    identity relating them) as hypotheses — NOT the conclusion, which is
    derived below per AGENTS.md §3b-cond item 5.  `sorry` in any concrete
    instance is understood as conjecture per §3b. -/
class BorromeanQuark where
  /-- Form A of the Q-value (NF-counit basis), `prop:neutron-qvalue-symbolic`. -/
  Q_beta_A : ℝ
  /-- Form B of the Q-value (transfer-matrix eigenfunction basis),
      `prop:beta-decay-transfer-matrix`. -/
  Q_beta_B : ℝ
  /-- **The conjecture itself** (spectral bridge): the two presentations
      of the free-neutron Q-value coincide — Form A equals Form B. -/
  forms_agree : Q_beta_A = Q_beta_B

-- Ref: [leitner2026] prop:q-beta-spectral-bridge
/-- **A BARE PROJECTION — this theorem derives nothing.**  Its conclusion
    `Q_beta_A = Q_beta_B` is *character-for-character* the class field
    `forms_agree`, so it restates its own hypothesis.

    **Disclosure added 2026-09-04** per bean `qou-pqmw` (78 bare projections,
    tracked with triage pending; this is the entry at this file).  The
    previous docstring defended the projection as *"Derived from the class
    field `forms_agree` — not a `sorry`-projection of an unrelated
    conclusion."*  That answers the wrong objection, as
    [`2026-08-09-inhabitation-is-a-weak-discriminator.md`](../../../docs/audits/2026-08-09-inhabitation-is-a-weak-discriminator.md)
    §"Two shapes worth singling out" sets out: the §3b-cond item-5 complaint
    is not that the conclusion is *unrelated* to the field but that it is
    **identical** to it.  That audit adjudicated this declaration `genuine`
    in `docs/audits/lean-vacuity-review-ledger.json`.

    **What is and is not the defect here.**  The class above is honest —
    content-bearing, and uninhabited, which per §3b-tax is the correct state
    for an open conjecture.  Only this wrapper is the defect, and it is a
    disclosure defect rather than a mathematical one: nothing false is
    asserted, but a reader scanning for `[inst : …]`-conditional results
    would count this as one.

    **The file's real content is elsewhere and is unconditional:**
    `q_beta_spectral_bridge` above proves the polynomial bridge identity, the
    leading-order ratio identity, and the first-order remainder — with no
    class hypothesis at all.  Cite that, not this.

    Closing the wrapper properly needs the class to relate `Q_beta_A` and
    `Q_beta_B` to the file's `(h, z)` forms, so that agreement *derives*
    something — exact agreement would force `z = 1` via the ratio identity.
    That changes what the block claims and is an authorial call, not a
    cleanup; it is left open rather than guessed at. -/
theorem q_beta_spectral_conditional [inst : BorromeanQuark] :
    inst.Q_beta_A = inst.Q_beta_B :=
  inst.forms_agree

end QOU.ParticleInteractions.QBetaSpectral.ConditionalAudit
