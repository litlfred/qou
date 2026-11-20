---
# qou-nzp3
title: 'GAP: convention-D closed form for the constit per-Z step tr_M(proton)'
status: todo
type: task
created_at: 2026-10-10T14:13:02Z
updated_at: 2026-11-20T09:30:00Z
parent: qou-d8c7
---

Split from qou-7xpx (2026-10-10). Under convention D the interface-knot factorisation full/constit = prod(z_D + d_i) holds for D, T, 3He, 4He at H6/H9/H12 (to 5e-50; probe computations/probes/interface_knot_markov_z_convention_d_probe.py). But the constit per-Z step, which equals tr_M(proton), is 0.62932840 on the live alternating word and 1.14575969 on the old grouped word, against 2q-1 = 1.21995717 (misses 48.4% and 6.1%). The full per-Z step on the canonical word is 0.38558198, not z_D(2q-1) = 0.7475. So conj:constit-factor-2q-minus-1 fails at D for both orderings (scope-(a) negative: this closed form, not every closed form). Open: is there a derived D-frame closed form for tr_M(proton)? Do not fit one against the measured value. Note conj:constit-factor-2q-minus-1 has no content block, only code-quoted references.

## 2026-11-20 — W1 survey (session_01VQDpPcT9hCf4RF1bQwk66r, epic PR #8534)

Claim released. No progress; open research gap (no derived D-frame closed form for tr_M(proton)). Do not fit one.
