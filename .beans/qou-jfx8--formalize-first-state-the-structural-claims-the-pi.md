---
# qou-jfx8
title: 'Formalize-first: state the structural claims the picture needs (shadow prices as directions of entanglement history; phase-space measure from the dual; relative Reeb angle as a jet-level datum) as Lean scaffolds or conjecture classes before any probe'
status: in-progress
type: task
priority: normal
created_at: 2026-09-16T00:47:53Z
updated_at: 2026-09-16T01:29:13Z
---

## 2026-09-16 — derived half landed; conjecture half held for the owner

LANDED: content/quantum-observable-universe/lean/QOU/MassTheory/BlockMeasureFromFrobeniusPairing.lean — FrobeniusPairingData (trM = Σ y χ, χ(1)=dim, trM 1 = 1); blockMass_sum_eq_one; trM_eq_expectation; trM_le_of_normalised_le / le_trM_of_le_normalised (needs IsProbability, a HYPOTHESIS — positivity of convention-D y_λ is measured n=3..12, not proved at general n); entangledSupp + trM_eq_of_entangledSupp_empty + bindingForm_eq_zero_of_entangledSupp_empty (ℝ section); charSupp/level + level_one_eq_top + level_le_level_one. lean-direct -DautoImplicit=false -s 65536 exit 0, no warnings; #print axioms: propext, Classical.choice, Quot.sound on all seven. Registered in QOU.lean.

HELD (not committed): a primary conjecture class RelativeReebDatum for the owner's relative-angle datum — Lean text in the analysis doc §8 O3. Reason: §3b-tax needs content-bearing fields and the content is exactly what is undefined; owner's rule against speculative code. Also held: any Möbius-energy objective (O4) until qou-99qc pins classicalLimitConst.

Probe: computations/probes/deuteron_block_measure_entangled_support_probe.py (6/6, committed inputs only, weight_family declared). Bean stays in-progress per rule 13a (the picture's structural claims are open).


Correction (same hour): the ℝ theorem bindingForm_eq_zero_of_entangledSupp_empty lives in the §7c companion QOU/MassTheory/BlockMeasureBindingFormArchimedean.lean, not in the generic file — check-sidecars flagged the mixed file and it was split before commit.
