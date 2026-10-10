---
# qou-lgex
title: 'A=3 magnitude ROUTE 3: multi-sub-link channel sum — WALL(scope-b) Brunnian triviality'
status: completed
type: task
tags:
    - a3-cross-channel
created_at: 2026-08-01T23:55:30Z
updated_at: 2026-08-01T23:55:30Z
---

ROUTE 3 of the A=3 magnitude cross-channel program. Test whether summing the distinct sub-link trace objects of the triton (3 pairwise 2-sub-links + the 3-body Borromean) supplies the missing magnitude factor r*=μ₃/c₃≈1.585.

VERDICT: WALL(scope-b) — Brunnian sub-link triviality kills ROUTE 3. Every proper 2-sub-link of the Borromean rings is the unlink ⇒ pairwise deficits fᵢ=0 exactly (strand-forgetting collapses each sub-word to the empty word; verified through the corpus χ_λ/y_λ pipeline). Both channel closures (additive Σ, multiplicative 1−∏(1−fᵢ)) collapse to the single 3-body Borromean deficit ⇒ magnitude factor exactly 1; r*≈1.585 NOT supplied. AGENTS.md 'compositional/trace object' caveat turned decisive: cross terms are protected only when pairwise deficits are nonzero; here they are provably zero.

Lean QOU.MassTheory.BorromeanSubLinkChannelSum sorry-free (lean-direct exit 0): brunnian_channelClosureMul_eq_triple, brunnian_channel_no_magnitude [IsDomain], borromean_channelClosure_eq_c3 / borromean_channel_ne_r_star (ℝ). Generic [CommRing R] per §7c.
Probe computations/deltalambda/borromean_sublink_channel_sum_probe.py + witness borromean-sublink-channel-sum.witness.json (closes=false, free_parameters=0).
Audit docs/audits/2026-08-01-a3-magnitude-sublink-channel-sum-brunnian-wall.md. Ledger row in option-e.md.
Branch claude/a3-magnitude-multi-sublink-channel-sum-2026-08-01. Nothing wired; μ₃/c₃ never inverted.
