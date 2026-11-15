---
# qou-ky5e
title: 'q-Collatz ℤ[ω]: tree-structure induction — main chain plus bare k≥1 branches'
status: completed
type: task
priority: normal
created_at: 2026-08-30T03:07:55Z
updated_at: 2026-08-30T03:20:16Z
---

PROVED. `QOU.AppendixSurreals.CollatzEisenstein.branch_subtree_no_oddPreimage`. The induction is cheaper than expected because the Eisenstein norm is the invariant: N(w+1) = 1, so the even branch-inverse preserves the norm; an odd-preimage forces P(w) = -w, of norm 1; and the k>=1 branch sits at norm 1+6k+12k^2 > 1. So the whole even subtree above any k>=1 branch is norm-fixed away from 1, non-unit, and blocked by the already-proved evenSubtree_no_oddPreimage engine. Each branch is a bare even chain; no two odd-preimages chain in the backward tree. Carries the explicit hypothesis that 1,w are Z-independent (holds in Z[w], fails in ZMod 3) - a condition on the ring, not a conjecture. Does NOT extend to D_inf; that step is qcz7 A1.
