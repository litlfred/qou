---
# qou-wbtz
title: 'FINDING: lean-self-assuming-audit is blind to CONJUNCTIVE projections (row 46)'
status: in-progress
type: task
priority: normal
created_at: 2026-09-14T18:08:47Z
updated_at: 2026-09-14T18:16:06Z
---

MEASURED. scripts/lean-self-assuming-audit.py reports 30 candidates over 2880 .lean files. Its rules are ONLY (1) proof IS a bare binder whose type == conclusion, and (2) proof is a single qualified projection X.f whose field type == conclusion. It has ZERO handling for anonymous constructors: grep for the bracket char in the script returns nothing. So a theorem concluding A AND B AND C, proved by a tuple of exactly the three assumed fields, is INVISIBLE BY CONSTRUCTION. Own measurement: 13 such conjunctive all-field projections, DISJOINT from the detector's 30. They concentrate on the flagship claims, which is the point: qou_is_ccc (3 components, 'QOU is a conformal cyclic cosmology'), ns_obstruction_tower + q_bkm_criterion (Navier-Stokes), p_bandwidth_bound + equivalence_of_faithfulness (P vs NP), confinement_frobenius_reciprocity (SIX components), deuteron_binding_energy, four_term_pair_nucleon, parity_regime_selection, lp_dual_stability. FAIRNESS NOTE: AGENTS.md 3b-cond names q_bkm_criterion the VERIFIED EXEMPLAR of a legitimate conditional-class theorem, so a 2-component Iff.intro assembly is a defensible pattern (there is a composition step). The defect class is the PURE RE-BUNDLING case: conclusion A AND B AND C, hypotheses exactly A, B, C, zero derivation — qou_is_ccc is the clean instance. Proposed detector fix: parse the anonymous constructor, require every component to be a field projection off ONE binder, and compare the conjunction of the declared field types against the conclusion. Candidate row 46 for the detector-blindness taxonomy.
