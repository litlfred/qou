---
# qou-gd90
title: 'qou-q425 torus links gcd(r,s)>1: exact periodic-state correction to MiddleWeightTraces, then prove'
status: completed
type: task
priority: normal
created_at: 2026-10-12T18:13:10Z
updated_at: 2026-10-12T19:14:55Z
parent: qou-xhci
---

Owner order: (1) gcd>1 torus links, (2) Schur–Weyl trace split under q not a root of unity, (3) W_{r,j}.


## 2026-10-12 — coordinator: subject proved, re-verified (PR #7737, head e6b74dffb5)
markov_rossoJones_torusLink (every torus link, any gcd), trace_split (Schur–Weyl split under [k]_q ≠ 0), gamW_fullTwist (γ^r = q^{r(r−1)−2j(r−j+1)} on W_{r,j}), finrank_Wmod, markov_fullTwist. lean -DautoImplicit=false -s 65536 exit 0 (13.8 s / 21 s); #print axioms = [propext, Classical.choice, Quot.sound]; probes 1350/1350 and 22624/22624. Remaining refinement (per-module trace for general p) continues under qou-q425.
