---
# qou-10v9
title: 'PROGRAM: L2 at 1 ppQ (mass and binding accuracy)'
status: in-progress
type: milestone
priority: critical
tags:
    - reorg-2026-10-04
created_at: 2026-10-04T15:09:54Z
updated_at: 2026-11-22T21:54:03Z
---

Programme root for the L2 / 1 ppQ target. Anchor document: `docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md`.

- L1 (compute precision, cross-method agreement <= 1 ppQ) is met.
- L2 (per-observable accuracy sigma_th <= sigma_exp/100) is 1 of 6 scoreable, 0 of 6 unconditional (2026-09-07 dashboard).
- Four un-derived objects: the Q_beta functional under convention D, the extensive binding term, the m_mu / proton-pin tension, the alpha_em conditional classes.

Predecessor articulations (cite, do not restate): 1qug, vibo, m2ay, ggdk/65jh, qou-37j2, qou-tonv.
Physical-identification conjectures (owner ruling 2026-10-04, decision 1) live here or under P4, never under the formal-conjecture umbrella.

2026-10-10: ofri named this OWNER GOAL #2 (goal #1 is qou-ywyq, trace = multiplicative integral).



## Progress Update (2026-11-19)
Updated 2026-11-19 L1/L2 status: L1 core gate GREEN (`1.82e-49` Markov cross-check, `1.32e-50` clarabel-mpfr duality gap); `m_mu` improved 26x to `8.058 ppb` (`+0.37 sigma_exp`), `v_EW` at `29.37 ppb` (`0.11 sigma_exp`), `m_K/m_pi` at `51.43 ppb` (`5.1x` inside L2), `Delta_pn` within `111 eV` (`86.2 ppm`). Added child tasks for anchor round-trip polish, `q_2t - q_mu` 2-loop dressing, 2-loop `v_EW`, and Dirac-Coulomb-Breit atomic electron binding.

## 2026-11-20 — W2 cross-workstream briefing (owner: "make sure they know")
Full briefing: PR #8526 comment 7047864732 and docs/coordination/2026-11-20-w2-qbeta-ud-briefing.md. Record: docs/audits/2026-11-20-qbeta-epsilon-is-ruled-not-derived.md sections 1-11.
Key points: Q_beta = (h[2]/2)*y3*E0 and sees only the isospin-3/2 block. The ruled epsilon (z_D, -43%) = label-A round trip = whole-space quantum trace. Label B (J4, strand-4 gamma-gamma) gives +0.33% and is NOT adopted (it labels isospin multiplicity, not n<->p). Label C gives 1/3, 0 and 0.202, none close. The owner made no label ruling ("3 2"). u/d are separate lines of the (3,1) rep of H4, not orientation-only (def:up/down-quark are stale). Convention-D volumes lie past the Phi_q pole. The six-term -2.43e15 was a truncated divergent series (fixed). The +0.17% / ~1 ppm Q_beta values and the April BW run are superseded or circular.


## 2026-11-22 — coordination pass (thread "Coordinate the L2 1-ppQ derivation plan")

Plan, gap list and applicability review: /mnt/project-files/l2-1ppq-coordination/2026-11-22-l2-1ppq-coordination-plan.md (to be committed to docs/coordination/ if the owner approves a PR).

Where we are (main 46c74c318):
- p–n: m_p = m_n at q = 1 proved for every braid-built functional (FlipSymmetryAtOne); pp = nn at generic q for within-nucleon braids (Q(q) at n = 6; Lean for the full-twist core in progress, #9123); no Coulomb pair term from Hecke insertions between blocks (α + β = 1 identity, #9103/#9125); charge lives on hadron lines, strand U(1) phase obstructed; colour moves no number (#9107). Numbers (cmp): strong O(h) arm +0.171 MeV, EM α·S −2.30 MeV on the facade, vs 1.293. Structure proved, magnitude not.
- Q_β: ruled γγ cell 0.3254 MeV (−58 %); Lean bound R ≤ 3/4 ⇒ cell ≤ 0.383 MeV; missing factor must survive at q = 1. Half-life: two-term 𝒲 in Lean, no number (c_em, μ₀ underived).
- Binding A ≤ 4: every γγ chain unbinds (Lean); A = 3 exact locality and product rule to (1 − z²)h⁶ (#9144 merged). keV-scale, wrong sign.
- Canonical chain: steps 3 axioms removed (proved false); step 2 Bridge A is circular (hL assumes the conclusion), HeckeMonodromy has only a toy instance, colour cubic needs Bridge A restated; step 5 T_β needs a TwistedPSDTrace instance; step 6 /q³ asserted, k = 2 not found, muon carrier asserted, 𝔈 → MeV open; a false axiom proton_mass_from_substrate_axiom sits in knots-particles-confinement/categorical-proton.lean (outside the build).
Ranked obligations: (1) Bridge A without hL; (2) 𝔈 → MeV and the muon carrier (qou-91w7, qou-6gf9); (3) proton normaliser; (4) two-term trace from the Lagrangian (c_em); (5) Hecke positivity/unification and axiom deletion.
Applicability review: ~36 stale in-progress children reset to todo (claims were untouched batch PRs); superseded/done/needs-owner lists are in the plan doc, Part 4; no bean closed or scrapped without the owner.
