import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
-- Imports the parent block's content (CanonicalMarkovWeightsH3 class,
-- delta_tau_M_canonical, chi_block_*, chi_blocks_have_q2_minus_1_factor).
-- Resolves via the Lake-tree mirror at
-- `content/quantum-observable-universe/lean/QOU/BraidKnot/QBetaPerBlockChiClosedForms.lean`
-- (added in this PR alongside the conditional theorem).
import QOU.BraidKnot.QBetaPerBlockChiClosedForms

/-!
# QOU.BraidKnot.DeltaTauMCanonicalConditional

**Conditional theorem (§3b-cond, AGENTS.md):** Under the
`CanonicalMarkovWeightsH3` class hypothesis, the canonical
$\Delta\tau_M^{\text{can}}(q) = \sum_\lambda y_\lambda(q) \cdot \chi_\lambda(q)$
factors $(q^2 - 1)$ for $q > 0$.

The block is a rigorous conditional consequence of the per-block
$\chi_\lambda$ closed-form theorems landed in
`qbeta-per-block-chi-closed-forms.lean` (PR #1764). The only
unproved input is a concrete instance of `CanonicalMarkovWeightsH3`,
which axiomatises the canonical Wenzl–Markov weights (`√q`-bearing,
currently open at the formalisation level).

LaTeX label: `prop:qbeta-delta-tau-canonical-conditional-q2-minus-1-factor`

## Dependency

This file imports `QOU.BraidKnot.QBetaPerBlockChiClosedForms` from
the parent block's Lake-tree mirror, which provides:

- `CanonicalMarkovWeightsH3` class
- `delta_tau_M_canonical` conditional def
- `chi_block_3 / chi_block_21 / chi_block_111` defs
- `chi_blocks_have_q2_minus_1_factor` theorem

## References

- [hoefsmit1974] seminormal representation matrices for H_3
- [wenzl1988] Hecke-algebra subfactors (Markov-trace weights y_λ)
- Witness: `qbeta-per-block-paper-closed-forms.witness.json`
-/

namespace QOU.BraidKnot

/-- **Theorem (conditional on `CanonicalMarkovWeightsH3`,
§3b-cond pattern).** The canonical $\Delta\tau_M$ factors $(q^2 - 1)$
for any $q > 0$.

**Proof.** By `chi_blocks_have_q2_minus_1_factor` each per-block
$\chi_\lambda(q) = (q^2 - 1) \cdot P_\lambda(q)$. Substituting into
`delta_tau_M_canonical` and factoring out $(q^2 - 1)$ from the
weighted sum gives the claim with
$P^{\text{can}}(q) = y_3(q) P_3(q) + y_{21}(q) P_{21}(q) + y_{111}(q) P_{111}(q)$.

This is fully verified by Lean modulo the single class instance —
the §3b-cond conditional rigour pattern. -/
theorem delta_tau_M_canonical_has_q2_minus_1_factor
    [w : CanonicalMarkovWeightsH3] (q : ℝ) (hq : 0 < q) :
    ∃ P : ℝ, delta_tau_M_canonical q = (q^2 - 1) * P := by
  -- Pull per-block factorisations from the parent block's theorem.
  obtain ⟨P3, P21, P111, h3, h21, h111⟩ :=
    chi_blocks_have_q2_minus_1_factor q hq
  refine ⟨w.y3 q * P3 q + w.y21 q * P21 q + w.y111 q * P111 q, ?_⟩
  unfold delta_tau_M_canonical
  rw [h3, h21, h111]
  ring

/-- **Corollary (vanishing at q = 1 from the factorisation).** As an
immediate consequence of the factorisation,
$\Delta\tau_M^{\text{can}}(1) = 0$.

This is the same vanishing already proved as
`delta_tau_M_canonical_vanish_at_one` in the parent block; we restate
it here as a corollary of the factorisation to make the structural
connection explicit. -/
theorem delta_tau_M_canonical_vanish_at_one_via_factor
    [CanonicalMarkovWeightsH3] :
    delta_tau_M_canonical 1 = 0 := by
  obtain ⟨P, hP⟩ := delta_tau_M_canonical_has_q2_minus_1_factor 1 one_pos
  rw [hP]; ring

end QOU.BraidKnot
