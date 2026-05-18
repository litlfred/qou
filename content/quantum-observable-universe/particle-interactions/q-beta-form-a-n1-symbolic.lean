/-!
# QOU.Interactions.QBetaFormA_N1 — depth-1 geometric-series lift

Encodes the symbolic closed form for $Q_\beta^{A, N=1}$ under
the **geometric-series lift** of `E_0`:

  E_0_N=1 = E_0_N=0 · (1 + ℏ_q²) = m_e · (2q² - 2q + 1) / (q³(q - 1))

  Q_β^{A, N=1} = m_e · (q + 1) · |q² - 2q - 1| · (2q² - 2q + 1) / (2 q⁵)

The form is the natural N=1 lift of `prop:neutron-qvalue-symbolic`.
**It is empirically refuted as a closure path** (overshoots the
per-braid-mass-tower ceiling 97 ppm by ~120×); the correct N≥1
lift is per-partition $k_\lambda$ (open per
`conj:brane-tower-z-habiro`).

What this file proves:
- The symbolic identity for the multiplicative factor
  `(1 + ℏ_q²) = (2q² - 2q + 1) / q²`.
- The closed-form expression for `Q_β^{A, N=1}(q)`.

What this file does NOT prove:
- That the geometric-series lift is the correct one (it ISN'T —
  see the negative finding documented in the sibling .md).

LaTeX label: `prop:q-beta-form-a-n1-symbolic`
-/

import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic

namespace QOU.Interactions

/-- Hecke–Skein differential `h(q) = q - q⁻¹`. -/
noncomputable def heckeH' (q : ℝ) : ℝ := q - q⁻¹

/-- ℏ_q substrate constant `(q - 1) / q`. -/
noncomputable def hbarQ (q : ℝ) : ℝ := (q - 1) / q

/-- Single-tick energy scale `E_0_N=0 = m_e / (q (q - 1))`. -/
noncomputable def E0N0 (m_e q : ℝ) : ℝ := m_e / (q * (q - 1))

/-- N=1 lift factor `1 + ℏ_q²` under the geometric series. -/
noncomputable def liftFactorN1 (q : ℝ) : ℝ := 1 + (hbarQ q) ^ 2

/-- N=1 energy scale `E_0_N=1 = E_0_N=0 · (1 + ℏ_q²)`. -/
noncomputable def E0N1 (m_e q : ℝ) : ℝ := E0N0 m_e q * liftFactorN1 q

/-- Form A's NF-counit magnitude `|Δ(net)| = |h(q)(2 - h(q))/2|`. -/
noncomputable def deltaNetMag (q : ℝ) : ℝ :=
  |heckeH' q * (2 - heckeH' q) / 2|

/-- $Q_\beta^A$ at depth N=0 (single-wrap symbolic;
    `prop:neutron-qvalue-symbolic`). -/
noncomputable def QBetaAN0 (m_e q : ℝ) : ℝ :=
  m_e * deltaNetMag q * (1 / (q * (q - 1)))

/-- $Q_\beta^A$ at depth N=1 (geometric-series lift; THIS prop). -/
noncomputable def QBetaAN1 (m_e q : ℝ) : ℝ :=
  m_e * deltaNetMag q * (1 / (q * (q - 1))) * liftFactorN1 q

/-! ## Algebraic identities (proved unconditionally) -/

-- Ref: [manuscript] prop:q-beta-form-a-n1-symbolic
/-- **Lift-factor identity**: `(1 + ℏ_q²) = (2q² - 2q + 1) / q²`. -/
theorem liftFactor_N1_closed_form (q : ℝ) (hq : q ≠ 0) :
    liftFactorN1 q = (2 * q ^ 2 - 2 * q + 1) / q ^ 2 := by
  unfold liftFactorN1 hbarQ
  field_simp
  ring

-- Ref: [manuscript] prop:q-beta-form-a-n1-symbolic
/-- **N=1 to N=0 ratio**: `Q_β^{A,N=1} = Q_β^{A,N=0} · (1 + ℏ_q²)`. -/
theorem QBetaAN1_eq_QBetaAN0_times_liftFactor
    (m_e q : ℝ) (hq : q ≠ 0) (hq1 : q - 1 ≠ 0) :
    QBetaAN1 m_e q = QBetaAN0 m_e q * liftFactorN1 q := by
  unfold QBetaAN1 QBetaAN0
  ring

/-- **Closed-form expression** for $Q_\beta^{A,N=1}$ as a single
    rational function of $q$ times $m_e$ and the Form A counit. -/
-- Ref: [manuscript] prop:q-beta-form-a-n1-symbolic
theorem QBetaAN1_closed_form
    (m_e q : ℝ) (hq : q ≠ 0) (hq1 : q - 1 ≠ 0) :
    QBetaAN1 m_e q
    = m_e * deltaNetMag q * (2 * q ^ 2 - 2 * q + 1) / (q ^ 3 * (q - 1)) := by
  unfold QBetaAN1 liftFactorN1 hbarQ E0N0
  field_simp
  ring

/-! ## Negative finding (not proved here; documented in sibling .md)

The geometric-series lift `(1 + ℏ_q²)` overshoots the per-braid-
mass-tower ceiling at q_0:

  N=0 residual: +0.168% (inside 0.991% ceiling)
  N=1 residual: +1.151% (outside 97 ppm ceiling by ~120×)

The closed-form expression above is ALGEBRAICALLY CORRECT but
EMPIRICALLY REFUTED as a closure path. The correct N≥1 lift is
per-partition `k_λ` (non-uniform Wedderburn truncation; open per
`conj:brane-tower-z-habiro` and `rem:per-partition-k-lambda-rule`).

The numerical evaluation at `q_0 = 1.109978595554181` is in
`q-beta-form-a-n1-extension.witness.json` (PR #639).
-/

-- Ref: [manuscript] prop:q-beta-form-a-n1-symbolic
-- Ref: [manuscript] conj:brane-tower-z-habiro §"Status of n_⋆"
/-- The geometric-series N=1 lift is EMPIRICALLY refuted as a
    closure path. The closed form is correct algebra; what's wrong
    is the uniform-k assumption underlying the geometric expansion.
    The correct N≥1 lift requires non-uniform per-partition k_λ
    truncation (open). -/
def QBetaAN1_geometric_lift_refuted_empirically : Prop :=
  -- Documented in q-beta-form-a-n1-extension.witness.json:
  -- |Q_β^{A,N=1}(q_0) - Q_β^CODATA| / Q_β^CODATA > ℏ_q⁴ / (1 - ℏ_q²)
  True  -- structural marker; actual numerical bound lives in the witness

-- Ref: [pr-639] q_beta_form_a_n1_extension.py + witness
/-- Marker theorem for the negative finding (always True; the
    actual content is the witness-recorded numerical inequality). -/
theorem geometric_N1_lift_refuted :
    QBetaAN1_geometric_lift_refuted_empirically := trivial

/-! ## Top-level export `q_beta_form_a_n1_symbolic`

The .ts manifest references `qou:QOU.Interactions.q_beta_form_a_n1_symbolic`.
Define it as the conjunction of the closed-form identities above. -/

-- Ref: [manuscript] prop:q-beta-form-a-n1-symbolic
/-- **Q_β Form A at N=1 (geometric-series lift).** Bundles the
    closed-form identities into the canonical export. -/
theorem q_beta_form_a_n1_symbolic :
    -- Lift factor closed form
    (∀ (q : ℝ), q ≠ 0 →
        liftFactorN1 q = (2 * q ^ 2 - 2 * q + 1) / q ^ 2)
    ∧
    -- Q_β^{A,N=1} via factor product
    (∀ (m_e q : ℝ), q ≠ 0 → q - 1 ≠ 0 →
        QBetaAN1 m_e q = QBetaAN0 m_e q * liftFactorN1 q)
    ∧
    -- Q_β^{A,N=1} closed-form rational expression
    (∀ (m_e q : ℝ), q ≠ 0 → q - 1 ≠ 0 →
        QBetaAN1 m_e q
        = m_e * deltaNetMag q * (2 * q ^ 2 - 2 * q + 1)
          / (q ^ 3 * (q - 1))) := by
  refine ⟨?_, ?_, ?_⟩
  · exact fun q hq => liftFactor_N1_closed_form q hq
  · exact fun m_e q hq hq1 => QBetaAN1_eq_QBetaAN0_times_liftFactor m_e q hq hq1
  · exact fun m_e q hq hq1 => QBetaAN1_closed_form m_e q hq hq1

end QOU.Interactions
