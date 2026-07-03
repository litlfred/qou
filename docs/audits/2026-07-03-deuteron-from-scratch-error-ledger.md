# 2026-07-03 — Deuteron (D) canonical mass + binding from scratch: per-stage error ledger

**Branch:** `claude/d-mass-binding-canonical-aj98ux` · **Bean:** `cexx` (session milestone)

## Goal (owner request, 2026-07-03)

Rebuild the deuteron mass and binding **from scratch** along the canonical
chain — from the substrate / γγ (pair-production) entry point through the
Hecke/Markov trace, the confinement SDP, to the archimedean MeV numbers —
**fully witnessed, no fitted constants, no hardcoded literals**, and with a
**per-stage error ledger**: at every stage of the chain, record the error the
stage introduces against the corresponding experimental anchor, so the owner
can see *where each error is coming from*.

Then, for the D case specifically, assess symbolic-answer prospects for the
four open A≥3-binding items (Δ_λ per-λ weight; α_k assignment rule; many-body
series closed form; mirror-pair magnitude), restricted to what D can decide.

## Status

**IN PROGRESS** — scaffold commit. Stages and findings land in subsequent
commits on this branch; this doc is the ledger of record.

## Planned stage decomposition (γγ → D)

| Stage | Object | Canonical source | Anchor compared | Error recorded |
|---|---|---|---|---|
| S0 | q₀ pin (CAL-2 via m_μ/m_e = Vol(4₁)/ℏ_q²) | `q_parameter.Q_50_DIGIT_STR` / `constants.q_at` | m_μ/m_e (muon) vs m_p/m_e (proton) | μ–p tension (anchor-choice error) |
| S1 | γγ / pair-production entry: photon = crossing operator; e⁺e⁻ / nucleon-pair thresholds | corpus survey (crossing energy E_H, brane crossings) | — | structural (no fit) |
| S2 | Nucleon masses m_p, m_n (muon-anchored Hecke energy, `F_Bor`) | `canonical_mass.py` facade | CODATA m_p, m_n | per-nucleon mass error |
| S3 | Deuteron braid `atom_braid_word_3A(1,1)` → tr_M in H₆; Wedderburn per-λ decomposition | `closed_form_tau_M.py`, Wenzl bridge | — (exact ℚ(q) identity checks) | cross-method L1 error |
| S4 | Confinement SDP / operator selection at A=2, full primal+dual | `lp_dual_solver.py` | — | duality gap |
| S5 | Binding B_D — every non-fitted route: trace-canonical `E₀·Δtr`, depth-stratified tower, Vol(6₂), μ₀·ℏ_q·J_q², Borromean Li₂^q tower | `binding_canonical.py`, `binding_depth_stratified*.py`, `borromean_binding_recompute.py`, `per_braid_tower.py` | AME2020 B_D = 2.2246 MeV | per-route binding error |
| S6 | Deuteron mass m_D = m_p + m_n − B_D | composition | AME2020 m_D | end-to-end error |

## Symbolic-prospect targets (D case)

1. **Δ_λ(D) ≈ 1/h(q₀)** (h(q₀) = q₀^(−15.0002), PROBE-1 observation tier) — exact or near-match?
2. **FR-restricted projector** `χ^λ·χ^λ(e_{K*})` at D (brane-tower plan §7).
3. **α_k at A=2**: the k=3 break is DERIVED (`χ^{(2,1)}(Δ)=0`); the D tower only reaches depth 5 — what does the D-restricted assignment look like symbolically?
4. **Many-body series at A=2**: trivially one bond — D is the base case; what D fixes vs cannot decide.

## Findings

(populated by subsequent commits)
