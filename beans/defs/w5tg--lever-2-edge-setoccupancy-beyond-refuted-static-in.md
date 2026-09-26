---
# w5tg
title: 'Lever 2: edge-set/occupancy beyond refuted static-integer graph (halo-D + magic-α blockers)'
status: in-progress
type: task
priority: normal
created_at: 2026-06-23T14:19:27Z
updated_at: 2026-06-23T16:59:40Z
---

## Coordination breadcrumb (2026-06-24, not a w5tg claim)

The deuteron LP-dual **active set** (the 7 Wedderburn blocks the qbk2 Reeb
correction sits on, PR #2661) is **NOT** this bean's binding edge-set — checked
and refuted in PR #2682
(`docs/audits/2026-06-24-lpdual-active-set-not-lever2-edge-set.md`):

- different objects — blocks (partitions λ⊢6) vs nucleon bonds (p–n edges + Z·N
  occupancy);
- no simple block statistic (rows/cols/n(λ)/chirality) separates active/inactive;
- only the Pauli endpoints agree ([6] active, [1⁶] inactive) — already covered by
  `PauliChannelBinding.lean`; the interior breaks any symmetry rule
  ([2,1,1,1,1] near-antisym is the most-active block);
- the raw deuteron LP-dual is degenerate (duality_gap ≈ 4.4e4) anyway.

So the LP-dual active set is **not** a candidate occupancy answer here. The
genuine Z·N p–n occupancy gate (owner-gated to the s5-so3 keystone) is untouched.

