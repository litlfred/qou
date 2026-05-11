/-!
# QOU.Interactions.QBetaSpectralBridge — Form A ≡ Form B at single wrap

The free-neutron Q-value admits two equivalent presentations:

* **Form A** — `Q_β^A = |Δ(net)| · E_0` in the NF-counit basis
  (`prop:neutron-qvalue-symbolic`).
* **Form B** — `Q_β^B = ln(V_pp / V_nn) · E_0 / z` in the transfer-
  matrix eigenfunction basis (`prop:beta-decay-transfer-matrix`),
  where `z = 1/(√q + 1/√q)` is the Markov–Jones parameter.

This file states the spectral bridge identity proved (modulo a
Taylor-expansion sorry) in
`content/quantum-observable-universe/particle-interactions/q-beta-spectral-bridge.md`:

  Q_β^A / Q_β^B  =  1 + (z - 1) h / 2 + O(h²)

with `h := q - q⁻¹`.

Provable in standard Mathlib — the proof reduces to:

1. Algebraic Taylor expansion of `h(2-h)/2` and `ln(1 + z h)`.
2. The ratio identity `(1 - h/2)/(1 - z h/2) = 1 + (z-1)h/2 + O(h²)`.

LaTeX label: `prop:q-beta-spectral-bridge`
-/

namespace QOU.Interactions

/-- The Markov–Jones parameter `z(q) = 1 / (√q + 1/√q)` controls
    the conversion between the NF-counit basis and the transfer-
    matrix eigenfunction basis. -/
noncomputable def markovZ (q : ℝ) : ℝ := 1 / (Real.sqrt q + (Real.sqrt q)⁻¹)

/-- The Hecke–Skein quantum-integer differential `h(q) = q - q⁻¹`. -/
noncomputable def heckeH (q : ℝ) : ℝ := q - q⁻¹

/-- Form A: the NF-counit factor `|Δ(net)| = h(2 - h)/2`. -/
noncomputable def deltaNetMagnitude (q : ℝ) : ℝ :=
  let h := heckeH q
  |h * (2 - h) / 2|

/-- Form B: the transfer-matrix log-ratio `ln(1 + z h)`. -/
noncomputable def transferLogRatio (q : ℝ) : ℝ :=
  let h := heckeH q
  let z := markovZ q
  Real.log (1 + z * h)

/--
**Theorem (Q_β spectral bridge, leading order).**
At single wrap and 1 < q, the dimensionless ratio of Form A to
(z-rescaled) Form B equals `1 + (z - 1) h / 2 + O(h²)`. Equivalently:

  |Δ(net)| / (ln(1 + z h) · z⁻¹)  =  1 + (z - 1) h / 2 + R(q),

with `|R(q)| ≤ h²` for `q` close to 1.

This is the algebraic content of `prop:q-beta-spectral-bridge`. The
proof reduces to a Taylor-expansion of `|h(2-h)/2|` and `ln(1 + z h)`
and ratio simplification. Mechanical in Mathlib (`Real.log_one_add_lt`,
`Real.log_one_add_gt`).
-/
theorem q_beta_spectral_bridge (q : ℝ) (hq : 1 < q) :
    let h := heckeH q
    let z := markovZ q
    |deltaNetMagnitude q / (transferLogRatio q / z) - (1 + (z - 1) * h / 2)| ≤ h^2 := by
  -- Ref: [manuscript] prop:q-beta-spectral-bridge
  -- Ref: [manuscript] prop:neutron-qvalue-symbolic
  -- Ref: [manuscript] prop:beta-decay-transfer-matrix
  -- Ref: [wenzl1988] doi:10.1007/BF01219077  (Hecke-skein normalization)
  -- Ref: [jones1985] doi:10.2307/1971403   (Markov-trace bridge)
  -- Proof: Taylor-expand |h(2-h)/2| = h - h²/2 + O(h³) and
  -- ln(1 + z h) = z h - (z h)²/2 + O(h³); form the ratio after
  -- multiplying B by z to cancel the leading factor of h.
  -- The error term is bounded by h² for q sufficiently close to 1.
  sorry

/--
**Corollary.** At leading order, Form A and Form B are equal up to
the Markov-parameter normalization:

  Q_β^A  =  Q_β^B · (1 + (z - 1) h / 2 + O(h²))

Substituting `Q_β^B = (ln(V_pp/V_nn) · E_0) / z` gives the explicit
basis-change identity used in `prop:q-beta-spectral-bridge`. -/
theorem q_beta_form_A_eq_form_B_leading_order (q : ℝ) (hq : 1 < q) :
    let h := heckeH q
    let z := markovZ q
    |deltaNetMagnitude q - transferLogRatio q / z * (1 + (z - 1) * h / 2)| ≤ h^2 := by
  -- Ref: [manuscript] prop:q-beta-spectral-bridge
  -- Follows directly from `q_beta_spectral_bridge` by clearing
  -- denominators; bound on |R| transfers via boundedness of
  -- transferLogRatio / z near q = 1.
  sorry

end QOU.Interactions
