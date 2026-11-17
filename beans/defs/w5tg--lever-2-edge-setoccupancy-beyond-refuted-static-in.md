---
# w5tg
title: 'Lever 2: edge-set/occupancy beyond refuted static-integer graph (halo-D + magic-α blockers)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-06-23T14:19:27Z
updated_at: 2026-10-04T15:13:13Z
parent: qou-10v9
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



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-06-23 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

### Progress (Round 74 — PR litlfred/qou#8322)
- Formalized in PR `litlfred/qou#8322` (`feat/round74-kashaev-stokes3-stokesamp-ohtsukinz-pauli-43c1`, Commit 1 `82ec77a3b69cc6d79a85c01e64b63d422fa51c45`, Head `d13ffedea3175ba61da12a5b2abf5cf08d471608`, `scriptHash: 79ed375a0246`).
