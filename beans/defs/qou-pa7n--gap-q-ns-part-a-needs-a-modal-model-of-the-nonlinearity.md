---
# qou-pa7n
title: 'GAP: q-NS Part A needs a modal model of the actual nonlinearity (triads + Parseval) to be stated non-vacuously'
status: in-progress
type: task
priority: normal
tags:
    - needs-owner
created_at: 2026-11-27T18:05:00Z
updated_at: 2026-11-28T02:44:08Z
parent: qou-innq
---

After the owner weakened property 3 of `thm:q-ns-wellposedness` (2026-11-27, card "Weaken decay clause, keep Part A"), the modal law in `QNsWellposednessContext` reads `d/dt|v̂_k| ≤ −ν_q[k]_q²|v̂_k| + T_k` with `T_k` free data.

**What was attempted.** Stating Part A of `conj:regularity-breakdown` as a primary-conjecture class over that context, with substrate-fixed data.

**Why it fails.** The class links neither the amplitudes `|v̂_k|` to the energy (no Parseval field) nor `T_k` to a triad nonlinearity. `junkContext` (`QOU/FluidDynamics/q_ns_enstrophy_order_parameter.lean`) satisfies every field with datum `δ_{k,1}` and has unbounded enstrophy as `q → 1⁺` (`partA_trivial_over_weakened_class`, sorry-free). So Part A over this class is trivially true.

**What a non-vacuous carrier needs.**
- Parseval: `‖v‖² = Σ_k |v̂_k|²`.
- `T_k` given by a triad sum with Biot–Savart structure, conserving energy in total (`Σ_k` of the energy transfer `= 0`).
- Infinitely many modes. On a finite complex (DEC model, PR #9434) the enstrophy is at most `λ_max·E` with `λ_max` bounded as `q → 1⁺`, so Part A fails on every finite truncation.

**Next honest step.** Formalise a modal q-NS model with those three properties (or the DEC model with a mode-count parameter `N` and a limit `N → ∞`), then state Part A over it as a content-bearing class with no instance.

Stays open (rule 13a): its subject is an open conjecture.

## 2026-11-27 progress (owner picks: "Modal triad model + Parseval" and "the DEC to infinity"; PR #9537)

- `q_ns_modal_triad.lean` (sorry-free). The modes are SU_q(2) Peter–Weyl labels and the triads follow the generic-q fusion rule. `TriadCoeff` couplings are supported on fusion triads and conserve the Parseval energy triad by triad. Proved: Galerkin energy conservation, support growth (modes `≤ m` feed only modes `≤ 2m`), and `dE/dt = −2νΩ`. `partA_fails_on_truncation` (scope (b)) gives `sup_t Ω ≤ [N]_{q0}²·E(0)` on every truncation to modes `≤ N`, for every coefficient system and every `ν ≥ 0`. Non-vacuity: `kraichnan` and `singleMode`.
- `q_ns_dec_refinement.lean` (sorry-free). Given an enstrophy-skew advection (hypothesis `hens`, the 2D property), the enstrophy of the 2-complex DEC model is nonincreasing at every resolution and every `ν ≥ 0`. So mesh refinement of a 2D model cannot carry Part A.
- Audit: `docs/audits/2026-11-27-qns-part-a-triad-model-and-dec-refinement.md`.

**Still open.** Part A needs infinitely many modes, and in the DEC picture it needs three dimensions. The missing pieces are the q-Clebsch–Gordan coefficients of `μ∘(v⊗∇_q v)` and a 3-complex DEC model (gap bean `qou-q3dc`). Do not close: Part A is an open conjecture.

## 2026-11-27T20:41:00Z — triad front (thread "Part A of conj:regularity-breakdown"), PR #9681

- Property 3 vs anomaly: already settled by 9a8e9d9 (owner card "Weaken decay clause, keep Part A"). Property 3 is now a modal balance with transfer T_k, so it does not forbid an anomaly. Property 2 (the energy inequality) does not forbid one either.
- On the block K[ζ]: the X₊X₋ pair budget term is 2νq² times the energy rate of u̇ = −νLu, h(u·Lu) ≥ 0, and that flow dissipates (q_ns_block_viscous_dissipation.lean).
- A candidate triad coupling: X₊ζ^{j+1}·X₋ζ^{k+1} = [j+1]_{q²}[k+1]_{q²}(q ζ^{j+k+1} + q² ζ^{j+k+2}). That is forward-only in ζ-degree, with coefficients ≥ (j+1)(k+1) for q ≥ 1 (q_ns_block_pair_cascade.lean). Sorry-free.
- Still open: (i) that this pair product is the q-NS advection (no ∇_q on O_q(SU(2))); (ii) the coefficients in the little q-Jacobi basis; (iii) a transfer lower bound along a solution; (iv) Part A. This bean stays open.

2026-11-28: surreal reading formalised (PR #9986, q_ns_qlegendre_surreal_band.lean): for q-1 infinitesimal, Rc q s >= (s+1)^2/32 for every s : N, so no standard mode decouples; the band cutoff sits at an infinite index ~log(1/delta)/delta, needing hypernatural indices (open). Chapter intro status account #9977, placeholder relabels #9980. Part A itself stays open.
