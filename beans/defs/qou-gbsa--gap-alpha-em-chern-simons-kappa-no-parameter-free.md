---
# qou-gbsa
title: 'GAP: alpha_EM Chern-Simons kappa — no parameter-free q-deformed Gram pairing G_q reproduces 1/alpha (ChernSimonsCorrectionConjecture carries G_q as a parameter, no instance)'
status: todo
type: task
priority: normal
tags:
    - lean
    - gap
created_at: 2026-09-03T09:08:30Z
updated_at: 2026-09-03T09:38:55Z
parent: qou-ggdk
---

Class B gap (SM-surface Lean sweep, bean qou-08zf, 2026-09-03). predicted-spectra/em-coupling-chern-simons.lean now states the .md's LIVE formula 1/α = q[9]_q[10]_q (1 + δ_CS/(1 − δ_CS κ)), with csGramClassical the explicit 2×2 Chern–Simons pairing of the .md, κ = det csGramClassical / det G_q, and G_q a PARAMETER of the conjecture class ChernSimonsCorrectionConjecture (fields gram_nondegenerate, tower_convergent, identity). No instance. gramDetRatio_congr proves basis-independence of κ; alphaInv_eq_bare_mul_tower derives the full-tower form conditionally. Previously the Lean formalised the superseded gluon-octet form with κ := 8q and a CODATA literal as the class content (bean qou-aemx).

OPEN: which q-deformation of the classical pairing is G_q. The .md enumerates 16 readings of "replace m,n by [m]_q,[n]_q"; the shipped producer's reading gives κ ≈ 1.7216 and misses CODATA by −468 ppb at the proton pin; exact closure needs κ ≈ 1.9153; none of the 16 lands in the window [1.8739, 1.9567]. A parameter-free G_q would close the identification. Related: qou-aemx, qou-93ap. Tower status ORDER-ZERO-ONLY (single carrier pair {T(2,9), T(3,5)}; the δ_CS tower is resummed to all orders but the H_n(q) tower is not used).

NEXT HONEST STEP: a structural argument selecting the q-deformed pairing (or a different pairing — the .md's surviving explanation is "wrong decomposition"), computed end-to-end in exact arithmetic. Never fit κ.

Note (2026-09-03, session qou-ggdk): computations/alpha_em_lean_vs_compute_divergence_probe.py still re-implements the SUPERSEDED alphaEmInvCorrected / gluonOctetKappa = 8q and describes them as 'exactly as the .lean declares' — false since em-coupling-chern-simons.lean now states the .md's resummed form with the Gram ratio as a class parameter (this branch). Numbers unaffected; the wording is stale. Comment-only producer edits drift scriptHash on any witness it writes, so fix it together with the next substantive change to that probe, not as a drive-by.
