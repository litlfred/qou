---
# qou-7mvf
title: prop:plancherel-term-7-formulation defines w_lambda(q)=dim_q^2/[n]_q! in prose; fr_pullback_k3_test now uses d_q^2/D^2 (RT/Verlinde) — block and code diverge
status: completed
type: task
priority: normal
created_at: 2026-09-05T05:55:41Z
updated_at: 2026-09-05T06:05:13Z
---

DONE 2026-09-05. Note added to prop:plancherel-term-7-formulation.md.

The block is NOT wrong and the fix records why rather than 'correcting' it:
Phi_k is LINEAR in w_lambda and enters observables only via differences
Phi^free - Phi^atom, so a lambda-independent rescale cancels from any
comparison at FIXED n. The normalization is genuinely immaterial there --
consistent with the registry ruling that Sigma != 1 is by design for
w_lambda(q).

It is material ACROSS n, since c_n depends on n (= 3A). So the note states
the rule -- cross-atom consumers must use d_q^2/D^2 -- names the two
producers that now do, and cites the Lean showing the two forms differ by
exactly one lambda-independent factor. The divergence is therefore
deliberate and recorded, not silent, which was the whole complaint.

Left open and pointed at qou-oots: whether dim_q^2 is the right NUMERATOR.
