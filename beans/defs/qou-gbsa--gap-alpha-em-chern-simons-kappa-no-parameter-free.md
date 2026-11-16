---
# qou-gbsa
title: 'GAP: alpha_EM Chern-Simons kappa — no parameter-free q-deformed Gram pairing G_q reproduces 1/alpha (ChernSimonsCorrectionConjecture carries G_q as a parameter, no instance)'
status: in-progress
type: task
priority: normal
tags:
    - gap
    - reorg-2026-10-04
    - lean
created_at: 2026-09-03T09:08:30Z
updated_at: 2026-11-16T19:56:51Z
parent: qou-3l2l
---

Class B gap (SM-surface Lean sweep, bean qou-08zf, 2026-09-03). predicted-spectra/em-coupling-chern-simons.lean now states the .md's LIVE formula 1/α = q[9]_q[10]_q (1 + δ_CS/(1 − δ_CS κ)), with csGramClassical the explicit 2×2 Chern–Simons pairing of the .md, κ = det csGramClassical / det G_q, and G_q a PARAMETER of the conjecture class ChernSimonsCorrectionConjecture (fields gram_nondegenerate, tower_convergent, identity). No instance. gramDetRatio_congr proves basis-independence of κ; alphaInv_eq_bare_mul_tower derives the full-tower form conditionally. Previously the Lean formalised the superseded gluon-octet form with κ := 8q and a CODATA literal as the class content (bean qou-aemx).

OPEN: which q-deformation of the classical pairing is G_q. The .md enumerates 16 readings of "replace m,n by [m]_q,[n]_q"; the shipped producer's reading gives κ ≈ 1.7216 and misses CODATA by −468 ppb at the proton pin; exact closure needs κ ≈ 1.9153; none of the 16 lands in the window [1.8739, 1.9567]. A parameter-free G_q would close the identification. Related: qou-aemx, qou-93ap. Tower status ORDER-ZERO-ONLY (single carrier pair {T(2,9), T(3,5)}; the δ_CS tower is resummed to all orders but the H_n(q) tower is not used).

NEXT HONEST STEP: a structural argument selecting the q-deformed pairing (or a different pairing — the .md's surviving explanation is "wrong decomposition"), computed end-to-end in exact arithmetic. Never fit κ.

Note (2026-09-03, session qou-ggdk): computations/alpha_em_lean_vs_compute_divergence_probe.py still re-implements the SUPERSEDED alphaEmInvCorrected / gluonOctetKappa = 8q and describes them as 'exactly as the .lean declares' — false since em-coupling-chern-simons.lean now states the .md's resummed form with the Gram ratio as a class parameter (this branch). Numbers unaffected; the wording is stale. Comment-only producer edits drift scriptHash on any witness it writes, so fix it together with the next substantive change to that probe, not as a drive-by.

## Round 50 Formalization & 50-dps Witness (PR #8177)
- **Lean 4 Module (`0 sorry`, `0 axiom`, `0 vacuity`):** `folio/quantum-observable-universe/lean/QOU/AlphaEM/ChernSimonsTowerAndT35Linchpin.lean`
  - `qGram16_all_outside_codata_window`: proves across all 16 parameter-free $[m]_q$-substitution readings of the Seifert pairing matrix $G = \begin{pmatrix} 2 & 1 \\ 1 & 5 \end{pmatrix}$ ($G_{11} \in \{2, [2]_q\}$, $G_{12}, G_{21} \in \{1, [1]_q\}$, $G_{22} \in \{5, [5]_q, [2]_q + [3]_q, [4]_q + 1\}$) that every resulting $\kappa = 9 / \det G_q$ lies strictly outside the $100\text{ ppb}$ CODATA window $[1.873903, 1.956720]$ around $\kappa_\star = 1.915314296...$.
- **50-dps Witness:** `computations/probes/round50-zeta4-bridge-and-alpha-em-cs-tower.witness.json` (`scriptHash: e7bf4a93b887`, `scriptCommitSha: cf283b8e199f4643fb9e0259ec0a2702096bdd9b`).
- **PR:** `litlfred/qou#8177` (`https://github.com/litlfred/qou/pull/8177`, head SHA `3fdbeeb87a6b1821ff8d57a95f95d4d20cf72628`).
- **Status:** Kept at `status: in-progress` per reviewer-separated closure discipline.
