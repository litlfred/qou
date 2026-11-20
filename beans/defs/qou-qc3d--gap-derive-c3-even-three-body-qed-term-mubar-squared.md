---
# qou-qc3d
title: 'GAP: derive c3, the coefficient of the even three-body QED term c3·Q1Q2Q3·mubar^2 on V^3'
status: todo
type: task
priority: normal
created_at: 2026-11-20T09:05:12Z
updated_at: 2026-11-20T19:30:00Z
parent: qou-7xl8
---

**Open (scope a).** From PR #8557 (QOU.BraidsAndKnots.CrossingCovariantQED, sorry-free): the only
surviving Milnor channel for a covariant QED term on the Borromean nucleon is the EVEN three-body term
c3·Q1Q2Q3·mubar(123)^2 (Q1Q2Q3 = −4/27 proton, +2/27 neutron; n−p split (2/9)c3,
evenThreeBody_np_split). A linear mubar coupling is excluded (alternating charge coefficient vanishes
on uu/dd). First-order crossing-local covariant insertions give 0 on V³ (coloured writhe).

Needs a second-order or non-local operator; nothing in the corpus (incl. Evans–Berger, Moffatt–Ricca,
MilnorTripleLinkingMagnus) supplies c3. Single-functional scale c_em = alpha_em·E0_tower = 30.849 keV
(alpha_em conditional on the Witten-κ sorry). Diagnostic ONLY — a derivation must not be tuned to it:
reaching the mu–p gap through the proton would need kappa = c3/c_em = 0.05006.
Also open: the wide-class classification is measured at q = 2 only.


---

**2026-11-20 — PR #8565 (`claude/two-term-qed-derivation-2026-11-20`), `QEDHigherOrderCovariance.lean` (17 thms, sorry-free, lean-direct exit 0) + `computations/probes/two_term_qed_derivation_joint_pin_probe.py` + `docs/audits/2026-11-20-two-term-qed-derivation.md`.**
- All-orders local class: covariance forces y_ab = t·x_ab with one t in {0, −h} (`exact_local_covariant`); the exact per-pair rescaling factor on V³ is 1 (`facU_borromean`), so the second-order (two-insertion) term of the local class is 0 for p and n.
- Naive photon-exchange double sum D is not braid-covariant (shifts by −(Q0Q1)² under σ1σ1⁻¹); its completion S²/2 = 0 on V³.
- No degree≤2 (order-α) charge weight couples to μ̄₁₂₃ (`quad_alternating_eq_zero`). The even degree-4 c₃ μ̄² term remains the only braid-dependent survivor; c₃ still underived.
- Joint pin (scope (a), conditional on α_em form B): α_em pins q0 +0.053 ppb from the proton identity, the muon identity +11.614 ppb. A proton-only term reaching m_μ sends α⁻¹ to +79.00 ppb. So no proton-side term (derived or not) satisfies m_μ and α_em together; the evidence points at the muon carrier (qou-6gf9).

---

**2026-11-20 (PR #8565, commits c965b8d070..405cec8b92). DERIVED within the central-U(1) colouring class, so c3 = 0.** QEDHigherOrderCovariance §U: the U(1)-coloured trace of V³ (per-letter t^{eQaQb}, ribbon twist θ^{Q²w}) equals tr(V³) for every t, θ and integer charge assignment (u1Trace_borromean, sorry-free). V³ is pure and every self-writhe is 0. §K: for an invariant form, a trivalent vertex with a central leg, or with all three legs along one direction, has weight 0, so U(1) charges reach the Kontsevich integral only via struts. §P: with the ruled photon, γ(0,0,qh)γ(0,0,−q⁻¹h) = V³ on the weight space (photon_product_eq_borWord). STILL OPEN: (b) holds only within the class. c3 from a NON-central photon coupling (electroweak-mixed u(2)), which needs mixed-leg structure constants, is not excluded. Status kept todo.
