---
# qou-hcas
title: drop y_eq_self_conjugate — the Wenzl-bridge class field, refuted 2026-09-02, dropped on owner ruling A
status: in-progress
type: task
created_at: 2026-09-04T10:44:38Z
updated_at: 2026-09-04T10:44:38Z
---

Owner ruling 2026-09-04 ('merge and next. drop A'), answering item 1 of the 2026-09-03 question. The class field WedderburnWeightCanonical.y_eq_self_conjugate (y_λ = w̃_λ on κ_λ = 0) was measured FALSE at every self-conjugate partition with n ≤ 6 except (1), in both conventions (computations/probes/wenzl_bridge_self_conjugate_premise_is_false.py, 2026-09-02); the three dispositions (restrict to (1) / drop / demote to conjecture) were the author's call. Chosen: DROP. Done on branch claude/drop-y-eq-self-conjugate-2026-09-04: field + projection theorem y_self_conjugate removed from mass-theory/wedderburn-weight-canonical.lean (y kept as data only; beta_mul_h_eq_neg_C unchanged; lean-direct 0 errors); .md statement no longer asserts the bridge and the caveat records the disposition; .ts title clause removed + dated authorNotes; probe check 0 now guards the drop. Consumers of the block (algebraic-gns-embedding, q-plancherel-asymptotic-skeleton, two-row-stratum, two-row-projection) use only the scalings, not the bridge.
