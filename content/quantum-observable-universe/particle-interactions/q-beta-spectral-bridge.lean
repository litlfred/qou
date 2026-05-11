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

import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic

namespace QOU.Interactions

/-- The Markov–Jones parameter `z(q) = 1 / (√q + 1/√q)` controls
    the conversion between the NF-counit basis and the transfer-
    matrix eigenfunction basis. -/
noncomputable def markovZ (q : ℝ) : ℝ := 1 / (Real.sqrt q + (Real.sqrt q)⁻¹)

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

-- Ref: [manuscript] prop:q-beta-spectral-bridge §"Form A side / Form B side"
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

-- Ref: [manuscript] prop:q-beta-spectral-bridge §"Ratio"
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
  ring

-- Ref: [manuscript] prop:q-beta-spectral-bridge §"Ratio"
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
  field_simp
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
`folio-assistant/computations/q_beta_spectral_bridge_witness.py`),
the algebraic content is closed by the three theorems above; the
Mathlib Taylor-bound chain is left as a structured open lemma.
-/

-- Ref: [manuscript] prop:q-beta-spectral-bridge §"Form B side"
-- Ref: [wenzl1988] doi:10.1007/BF01219077  (Hecke-skein normalization)
-- Ref: [jones1985] doi:10.2307/1971403   (Markov-trace bridge)
/-- **Taylor bound on Form B (Mathlib gap).** The transfer-matrix
    log-ratio `Real.log (1 + z h)` agrees with its degree-2 Taylor
    expansion `z h - (z h)² / 2` up to a cubic-in-`(z h)` correction.

    Provable via Mathlib's `Real.log_one_add` Taylor expansion + a
    standard cubic-remainder estimate on `[0, z h]` for `0 ≤ z h < 1`. -/
theorem log_one_add_taylor_bound
    (h z : ℝ) (hz : 0 ≤ z) (hh : 0 ≤ h) (hzh : z * h < 1) :
    |Real.log (1 + z * h) - (z * h - (z * h)^2 / 2)| ≤ (z * h)^3 := by
  -- Standard Taylor remainder for log(1 + x) at x ∈ [0, 1):
  --   log(1 + x) = x - x²/2 + x³/3 - x⁴/4 + ...
  -- Remainder bound: |log(1 + x) - (x - x²/2)| ≤ |x|³ / 3 ≤ |x|³.
  -- Mathlib reference: `Real.log_le_sub_one_of_le` / `Real.log_lt_sub_one`
  -- + alternating-series tail bound on the natural log expansion.
  sorry

/-! ## Top-level identifier for `lean.ref`

The `.ts` manifest references `qou:QOU.Interactions.q_beta_spectral_bridge`.
We define it here as the conjunction of the three algebraic pieces
above; the analytic Taylor-bound part is split out separately so
its sorry is visible.
-/

-- Ref: [manuscript] prop:q-beta-spectral-bridge
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
