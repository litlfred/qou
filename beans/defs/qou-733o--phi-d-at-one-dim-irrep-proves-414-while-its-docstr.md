---
# qou-733o
title: phi_d_at_one_dim_irrep proves 4*1=4 while its docstring claims a structural proof
status: completed
type: task
priority: normal
tags:
    - lean
created_at: 2026-11-22T15:20:07Z
updated_at: 2026-11-22T15:29:45Z
parent: qou-uwyf
---

Found by rule 6 of the self-assuming audit, 2026-11-22. mass-endomorphism/phi-d-syt-count-conjecture.lean:152 takes h : lam_syt_count = 1 and proves 4 * lam_syt_count = 4 by rw [h]. The preceding comment says the one-dimensional case can be proved structurally (the σ_i act by q or −q⁻¹, so Φ_4 = q²+1 appears). That structural statement is not in the Lean. Fix: state the cyclotomic-factor claim for a 1-d irrep and prove it, or reword the comment. The block is a conjecture, so this is a docstring overclaim, not a false theorem.


2026-11-22: fixed in PR #9033 (rebase-merged, 1c2d81edee3). lean-direct exit 0.
