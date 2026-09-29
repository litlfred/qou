---
# qou-n04i
title: 'RED-TEAM: m_p = 2(m_μ·F_Bor − 6·m_e) — parameter-free-in-q₀ but fitted-by-selection (β_Bor/q³/2/6)'
status: todo
type: task
priority: normal
created_at: 2026-08-22T20:34:54Z
updated_at: 2026-08-22T20:36:44Z
---

## Findings (2026-08-22) — audit doc docs/audits/2026-08-22-mp-fbor-massformula-redteam.md

VERDICT: one-continuous-parameter (q₀) fit dressed with post-hoc integers + asserted normalization. NOT a parameter-free derivation of m_p/m_e.

DOF: 1 continuous (q₀), consumed by 1 anchor. Production pins q₀ by INVERTING this very formula against m_p/m_e (constants.py:112 _solve_q_proton_f64) → m_p is a machine-precision round-trip, ZERO predictive content. Only non-circular test = μ-p consistency: m_μ/m_e misses 211 ppb (~963× the 100× target).

Per-piece tiers:
- Vol(4₁)=2Cl₂(π/3): DERIVED ✓ (0 DOF)
- convention D: DERIVED ✓ (fibre N=2 from SU(2)-emergence forces z_D; FibreDimensionForcesTL.lean, not CODATA-selected) — genuine bright spot
- |tr_M(β_Bor)| closed form: DERIVED (Lean) given β_Bor+D
- β_Bor=Borromean=proton: SELECTED/CONJECTURAL (conj:proton-borromean-assembly)
- F_Bor's /q³: ASSERTED, breaks bar-symmetry, 37% lever (cites bean qou-24w9)
- integers 2 (dim V_{(2,1)}) & 6 (|S₃|): post-hoc; the −1/12 Ocneanu provenance is REFUTED for β_Bor (trM~q⁻⁴ coeff 1, NOT q⁻¹⁰·−1/12) yet still cited in the live conj + def blocks
- prop:proton-mass-substrate-identity: near-vacuous self-assuming projection (§3b-cond item 5 — just distributes the assumed assembly law)

Sensitivity (60-dps probe): bind=6 uniquely lands μ at 211 ppb (bind=5,7 → ~943,000 ppb); but only because F_Bor pre-normalized so 2·m_μ·F_Bor overshoots m_p by EXACTLY 12.0 m_e. Integer is the residual re-labeled, not derived.

Follow-ups (not done, read-only): (1) scrub refuted −1/12 from conj+def blocks; (2) resolve qou-24w9 /q³; (3) re-label the prop.
