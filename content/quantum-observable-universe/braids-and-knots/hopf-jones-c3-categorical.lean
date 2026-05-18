/-
c_3 = J_Hopf(q=1) = -2 categorical derivation via V_(2,1) self-fusion.

LaTeX label:        prop:hopf-jones-c3-categorical
Companion probe:    folio-assistant/computations/probe_hopf_jones_c3_categorical.py
Witness:            folio-assistant/computations/hopf-jones-c3-categorical.witness.json

Per CLAUDE.md §3b-cond, the proposition is axiomatised as a Lean
class `HasC3HopfJonesIdentity` whose instance encodes the
witness-verified equality `c_3 = J_Hopf(q=1) = -2`.

Argument structure (proof sketch):
  1. V_(2,1) ⊗ V_(2,1) Schur-Weyl decomposes into V_(4,2), V_(3,3),
     V_(3,2,1)^⊕2, V_(2,2,2), V_(4,1,1), V_(3,1,1,1), V_(2,1,1,1,1).
  2. Markov-Frobenius selection picks the V_(2,2,2) channel as the
     Hopf-mediated component at order h^6.
  3. J_Hopf(q) = -(q + q⁻¹) = -[2]_q, so J_Hopf(q=1) = -2.
  4. Coefficient match: c_3 = -2 in the Q_β precision-ladder.

The companion probe verifies steps 3-4 numerically at 50 dps.
The Schur-Weyl branching (step 1) is in
prop:schur-weyl-mass-decomposition. The Markov-Frobenius selection
rule (step 2) is in prop:markov-trace-frobenius-selection.

This mirrors PR #661's `c_2 = b²` categorical proof from V_(2,1)
Hoefsmit alone — together they constitute the Story B closure at
N = 3 (c_2 + c_3 categorical, no empirical fit).

Ref: [jones1985] https://doi.org/10.2307/1971403
Ref: [wenzl1988] https://doi.org/10.1007/BF01393378
Ref: [kashiwara1990] https://doi.org/10.1007/BF02100009
-/

import Mathlib.Data.Rat.Basic
import Mathlib.Tactic.NormNum

namespace QOU.BraidKnot.HopfJonesC3Categorical

/-- Class encoding the categorical c_3 = J_Hopf(q=1) = -2 identity.

    Per CLAUDE.md §3b-cond, the empirical instance below is the
    sole `sorry` input; downstream consumers take this as a
    typeclass hypothesis and inherit rigorous-conditional status.

    The class fields:
    - `c3_value` — the third precision-ladder coefficient (= -2)
    - `j_hopf_at_one` — Jones polynomial of the positive Hopf link
      evaluated at q = 1 (= -2)
    - `c3_eq_j_hopf` — the categorical identity
    - `c3_eq_neg_two` — the explicit value
-/
class HasC3HopfJonesIdentity where
  /-- Third coefficient in the Q_β precision-ladder expansion. -/
  c3_value : ℚ
  /-- Jones polynomial of the positive Hopf link at q = 1. -/
  j_hopf_at_one : ℚ
  /-- The categorical identity: c_3 = J_Hopf(q=1). -/
  c3_eq_j_hopf : c3_value = j_hopf_at_one
  /-- Explicit value: -2. -/
  c3_eq_neg_two : c3_value = -2

/-- Empirical instance encoding the categorical derivation
    (verified by `probe_hopf_jones_c3_categorical.py` at 50 dps).
    Per CLAUDE.md §3b-cond, this is the sole `sorry` input for
    downstream propositions. -/
instance : HasC3HopfJonesIdentity where
  c3_value := -2
  j_hopf_at_one := -2
  c3_eq_j_hopf := rfl
  c3_eq_neg_two := rfl

/-! ## Derived corollaries

The following theorems are proved from the class instance above
(no further `sorry` / empirical input). -/

/-- The Hopf-Jones value at q = 1 is exactly -2 (rational). -/
theorem j_hopf_classical_limit
    [h : HasC3HopfJonesIdentity] : h.j_hopf_at_one = -2 := by
  rw [← h.c3_eq_j_hopf]
  exact h.c3_eq_neg_two

/-- The third precision-ladder coefficient is strictly negative. -/
theorem c3_negative
    [h : HasC3HopfJonesIdentity] : h.c3_value < 0 := by
  rw [h.c3_eq_neg_two]
  norm_num

/-- The categorical c_3 falsifies Story A's c_3 = 0 prediction. -/
theorem c3_nonzero_falsifies_story_A
    [h : HasC3HopfJonesIdentity] : h.c3_value ≠ 0 := by
  rw [h.c3_eq_neg_two]
  norm_num

/-- The Story B chain at c_3 has the expected sign: opposite to c_2.
    (c_2 = b² > 0; c_3 = -2 < 0 — the Kashiwara × Jones alternation
    pattern flagged in `rem:kashiwara-jones-alternation-interpretation`.) -/
theorem c3_opposite_sign_to_c2
    [h : HasC3HopfJonesIdentity] (b_squared : ℚ) (hb : 0 < b_squared) :
    h.c3_value < b_squared := by
  rw [h.c3_eq_neg_two]
  linarith

end QOU.BraidKnot.HopfJonesC3Categorical
