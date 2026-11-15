---
# qou-jfx8
title: 'Formalize-first: state the structural claims the picture needs (shadow prices as directions of entanglement history; phase-space measure from the dual; relative Reeb angle as a jet-level datum) as Lean scaffolds or conjecture classes before any probe'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-16T00:47:53Z
updated_at: 2026-10-04T15:12:39Z
parent: qou-v2om
---

## 2026-09-16 — derived half landed; conjecture half held for the owner

LANDED: folio/quantum-observable-universe/lean/QOU/MassTheory/BlockMeasureFromFrobeniusPairing.lean — FrobeniusPairingData (trM = Σ y χ, χ(1)=dim, trM 1 = 1); blockMass_sum_eq_one; trM_eq_expectation; trM_le_of_normalised_le / le_trM_of_le_normalised (needs IsProbability, a HYPOTHESIS — positivity of convention-D y_λ is measured n=3..12, not proved at general n); entangledSupp + trM_eq_of_entangledSupp_empty + bindingForm_eq_zero_of_entangledSupp_empty (ℝ section); charSupp/level + level_one_eq_top + level_le_level_one. lean-direct -DautoImplicit=false -s 65536 exit 0, no warnings; #print axioms: propext, Classical.choice, Quot.sound on all seven. Registered in QOU.lean.

HELD (not committed): a primary conjecture class RelativeReebDatum for the owner's relative-angle datum — Lean text in the analysis doc §8 O3. Reason: §3b-tax needs content-bearing fields and the content is exactly what is undefined; owner's rule against speculative code. Also held: any Möbius-energy objective (O4) until qou-99qc pins classicalLimitConst.

Probe: computations/probes/deuteron_block_measure_entangled_support_probe.py (6/6, committed inputs only, weight_family declared). Bean stays in-progress per rule 13a (the picture's structural claims are open).


Correction (same hour): the ℝ theorem bindingForm_eq_zero_of_entangledSupp_empty lives in the §7c companion QOU/MassTheory/BlockMeasureBindingFormArchimedean.lean, not in the generic file — check-sidecars flagged the mixed file and it was split before commit.



## 2026-09-16 — owner: 'formalize and work on RelativeReebDatum conjecture class'

Owner clarification (verbatim gist): the relative Reeb angle between two knots 'is supposed to be the evaluation/trace of the substrate phase space at the point'. That is explicit consent for the held class. Branch claude/lr-a3-reeb-datum-composition-program-2026-09-16 from main 1a5059cffb; committing RelativeReebDatum as a content-bearing primary conjecture class (no instance), with derived consequences as theorems taking the class as hypothesis.



## 2026-09-16 — RelativeReebDatum committed (class, no instance)

QOU/MassTheory/RelativeReebDatum.lean: class over BranchingData ℝ A₁ A₁ A Λ₁ Λ₁ Λ with lightCone, compose, Entangled; clauses compose_eq (a ⋈ b = (a⊗b)·lightCone), lightCone_of_not_entangled (= 1), trM_lightCone_mem (∈ [−1,1]); phaseSpace (block vector of the light cone), relAngle := arccos ∘ trM ∘ lightCone; proved sum_phaseSpace and the four no-shared-history consequences (composite = free product, trace factorises, bindingForm 0, relAngle 0). Probe relative_reeb_datum_trace_angle_probe.py (7/7): trace-level candidate θ = arccos(∏(z_D+d)) defined and monotone (D 59.45°, 3He 71.86°, T 78.16°, 4He 82.78°); block-level ratio NOT definable (|χ_atom/χ_free| > 1 on T (5,4), 3He (9),(5,4)). Roast: on the only defined candidate the angle is the binding form under cos θ = exp(−B/α) — redundant. Stays in-progress (rule 13a: lightCone is data, the conjecture is open); options doc §8 O2/O5.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-16 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
