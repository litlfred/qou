import Mathlib.Data.Nat.Basic

/-!
# PSLQ certifies Cl_3(2π/5) - Cl_3(4π/5) is independent

Compiled formalisation of `prop:cl3-zeta5-pslq-independence`.
Sibling docstub at `braids-and-knots/cl3-zeta5-pslq-independence.lean`.

PSLQ is a numerical certification at fixed precision and norm
bound. The substantive content lives in `cl3-zeta5-pslq.witness.json`;
this Lean stub captures the certification parameters (precision,
norm bound) and the certified outcome (no integer relation found
at the given parameters).
-/

namespace QOU.BraidKnot.Cl3Zeta5PslqIndependence

/-- Abstract context for `prop:cl3-zeta5-pslq-independence`. -/
class Cl3Zeta5PslqIndependenceContext where
  /-- Decimal precision used by PSLQ (digits). -/
  pslq_precision_dps : ℕ
  /-- Norm-bound parameter used by PSLQ (≤ which any integer relation
      coefficient must lie). -/
  pslq_norm_bound : ℕ
  /-- Predicate "PSLQ found no integer relation at the given
      precision and norm bound on `(Cl_3(2π/5), Cl_3(4π/5), ζ_5)`". -/
  no_integer_relation_found : Prop
  /-- Manuscript claim — PSLQ certifies independence at substantial
      precision (≥ 1000 dps) and significant norm bound (≥ 10^10). -/
  claim_pslq_independence :
    1000 ≤ pslq_precision_dps ∧
    10 ^ 10 ≤ pslq_norm_bound ∧
    no_integer_relation_found


/-! ### Removed 2026-08-30 — self-assuming projections

- `pslq_independence` — body was `ctx.claim_pslq_independence`: the conclusion was the projected
  field verbatim, so the declaration restated its own hypothesis.

**Why removal.** The content is not lost: it stays in the class field each
declaration projected, which asserts the same proposition under the same
hypotheses. Only the restatement goes. That is the disposition the vacuity
ledger records for this category — *"drop the pseudo-theorem and project the
field at use sites"* — and there were no use sites: each had **zero references
anywhere in the corpus**, including in this file. A caller wanting the fact
writes the projection directly, which is what the removed body did.
Bean `qou-z9ws`.
-/

end QOU.BraidKnot.Cl3Zeta5PslqIndependence
