---
# qou-7xl8
title: "EPIC: Two-Term Categorical Mass & Splitting Decomposition (Δm_QCD + Δm_QED from ℒ_q = \U0001D49F_∇² + ψ*⊗\U0001D49F_∇ψ) — Formalize-First Lean Proofs, Cottingham Self-Energy, and 211 ppb μ–p Tension"
status: completed
type: epic
priority: critical
tags:
    - convention-d
    - 1ppq
    - cottingham
created_at: 2026-11-18T19:52:23Z
updated_at: 2026-11-20T17:30:00Z
---

Master epic for deriving, formalizing in Lean 4 (over real QOU/Mathlib types, 0 sorry, 0 axiom, adversarially checked), and auditing the downstream compute/1ppQ consequences of the two-term categorical mass and isospin-splitting decomposition:

  τ(ℒ_q(∇, ψ)) = τ(𝒟_∇²) + τ(ψ* ⊗ 𝒟_∇ψ)  ⟹  Δm_np = Δm_QCD + Δm_QED

1. **Mathematical foundation**:
   - In `QOU.BraidsAndKnots.NucleonWeightSpaceTraces` and `NucleonWeightSpaceSecondOrder`, the intertwiner `P(q)` makes every pure braid word and every ω-symmetric U_q(sl₂) insertion (`FE + EF`) identical on the proton `(2,1)` and neutron `(1,2)` weight spaces, so Term 1 (`𝒟_∇²` / Cartan weight `K^{⊗3} = q^{±1}`) sees only the strong isovector shift (`t_n / t_p = q⁻²`).
   - By the Gell-Mann–Nishijima formula `Q = (1/6)I + T³`, the electromagnetic charge operator mixes an ω-even hypercharge scalar (`1/6`) with an ω-odd isovector (`T³`). Its quadratic two-photon Cottingham / Coulomb-Compton operators (`Σ Q_i²`, `Σ_{i<j} Q_i Q_j`, and crossing-coupled `Q_{12}, Q_{23}`) break the `P(q)` intertwiner (`P(q) Q_{12}^{(p)} ≠ Q_{12}^{(n)} P(q)`), yielding the negative electromagnetic self-energy shift `Δm_QED < 0` that opposes `Δm_QCD > 0`.
2. **Claim-level citations & mandatory Lean proofs**:
   - All citations to the newly ingested Cottingham / Compton subtraction function / lattice QCD+QED papers (`borsanyi-et-al-2015`, `gasser-leutwyler-rusetsky-2020-epjc`, `gasser-leutwyler-rusetsky-2021`, `walker-loud-carlson-miller-2012`, `can-qcdsf-2025`, `horsley-et-al-2016-qcd-qed`) and Hecke idempotent / modified quantum dimension / Stokes papers (`aiston-morton-1997`, `hadji-morton-2009`, `geer-patureau-mirand-turaev-2009`, `geer-patureau-mirand-turaev-2013`, `yekutieli2015`, `broda2002`, `pimsner-popa-1986`, `jones2015vonneumann`) must link to exact `library/<doc-id>/blocks/<block-id>` claim nodes.
   - Every cited mathematical claim must be proved in Lean 4 over real `QOU.*` and `Mathlib.*` imports (`scripts/lean-verify.sh`), followed by an adversarial review pass (`lean-proof-vacuity-audit`, `lean-borrowed-name-audit.py`, `lean-definition-collapsed-audit.py`).


---

**2026-11-20 — PR #8565 (`claude/two-term-qed-derivation-2026-11-20`), `QEDHigherOrderCovariance.lean` (17 thms, sorry-free, lean-direct exit 0) + `computations/probes/two_term_qed_derivation_joint_pin_probe.py` + `docs/audits/2026-11-20-two-term-qed-derivation.md`.**
- All-orders local class: covariance forces y_ab = t·x_ab with one t in {0, −h} (`exact_local_covariant`); the exact per-pair rescaling factor on V³ is 1 (`facU_borromean`), so the second-order (two-insertion) term of the local class is 0 for p and n.
- Naive photon-exchange double sum D is not braid-covariant (shifts by −(Q0Q1)² under σ1σ1⁻¹); its completion S²/2 = 0 on V³.
- No degree≤2 (order-α) charge weight couples to μ̄₁₂₃ (`quad_alternating_eq_zero`). The even degree-4 c₃ μ̄² term remains the only braid-dependent survivor; c₃ still underived.
- Joint pin (scope (a), conditional on α_em form B): α_em pins q0 +0.053 ppb from the proton identity, the muon identity +11.614 ppb. A proton-only term reaching m_μ sends α⁻¹ to +79.00 ppb. So no proton-side term (derived or not) satisfies m_μ and α_em together; the evidence points at the muon carrier (qou-6gf9).

**2026-11-20T17:30Z — OWNER RULING (Carl, 16:44): the L2 scorecard scores OPTION 2, the covariant all-pairs insertion Q₁₂+Q₂₃+Q₁₃ with the derived weighting Tr(K^{⊗3}·)/[2]_q³ (PR #8591).** Its connected part is ≡ 0 on V³ (Lean `NucleonWeightSpaceQTrace.deltaT_allPairs_connected_eq_zero`, sorry-free), so every scored two-term row equals its one-term row. Options 1 (adjacent, connected, −m_e·t), 3 and 4 stay as unscored labelled rows. Implemented in #8591 (commits 764f905a1c, e64a4240dc, 5ec37345d6 and later): `insertion=None` + derived = all-pairs is the canonical default in two_term_qtrace_weighting, canonical_mass, derived_masses, qbeta_utils, qou_substrate.q_two_term_borromean_at (pin = one-term proton pin to 50 digits), m_p substrate identity, free-neutron-decay, isotope compute, dashboard, scorecard (scored_form two_term_covariant_all_pairs_qtrace). Scorecard moved main(plain) → adjacent-derived → ruled: m_μ +8.058 → +128.0 → **+211.2 ppb (970.2×, = one-term)**; Q_β 1.672e8 → 1.669e8 → 1.668e8 ppb; m_n 1.392e5 → 1.390e5 → 1.389e5; Δ_pn 1.011e8 → 1.010e8 → 1.009e8; headline 1/6 unchanged. Content blocks neutron-proton-mass-splitting and isospin-mass-split-em-localisation now state the ruled form with a dated note that +0.2201 / −0.3317 keV / 8.06 ppb (0.37σ) were the 1/3-normalised plain adjacent weighting; the probe does not close the μ–p tension. derived_masses default pin moved muon → proton (qou-aj91; Q_β +30.37 ppb rel.). The ruling settles the insertion and weighting of the two-term QED probe only; it derives no non-zero Q_β/Δ_pn contribution, so the open question of this bean (what ε is, and the u/d derivation) is untouched. Bean stays open (rule 13a).
