---
# qou-us0a
title: 'SW-9 (Phase 3): U_q(gl_N) + V^⊗n + Jimbo double centralizer End_{U_q}(V^⊗n)=im H_n(q)'
status: todo
type: task
priority: normal
created_at: 2026-08-02T19:33:08Z
updated_at: 2026-08-19T13:42:34Z
parent: qou-59vq
blocked_by:
    - qou-0h5k
---

Full quantum Schur-Weyl: the U_q(gl_N) R-matrix action on V^⊗n, H_n(q)→End(V^⊗n), double centralizer + V^⊗n=⊕_λ L_λ⊗S^λ. Hardest; needs a U_q(gl_N) model (none in Mathlib). Ref: [jimbo1986].

## Refine (recon): NO Jacobson density / double-centralizer / bicommutant in Mathlib (Subalgebra.centralizer exists but no centralizer_centralizer). This is the largest gap and the heart of SW duality. NOTE: SW-8/R2-inst (the HeckeWedderburnData instance) is reachable via SW-7 without SW-9 — SW-9 is the full V^⊗n duality, a separate Phase-3 goal.


## Measured 2026-08-19 — still not started, and still correctly deprioritised

Nothing in the tree touches U_q(gl_N) or a double centralizer. Recon finding
still holds: no Jacobson density / bicommutant in Mathlib v4.24.0
(`Subalgebra.centralizer` exists, `centralizer_centralizer` does not). Confirmed
that SW-8/R2-inst was reachable without this (`qou-tpl5` closed at n=3), so this
remains a separate Phase-3 goal rather than a blocker for the Wedderburn arc.
