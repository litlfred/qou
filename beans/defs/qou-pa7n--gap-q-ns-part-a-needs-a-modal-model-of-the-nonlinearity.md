---
# qou-pa7n
title: 'GAP: q-NS Part A needs a modal model of the actual nonlinearity (triads + Parseval) to be stated non-vacuously'
status: todo
type: task
priority: normal
tags:
    - needs-owner
created_at: 2026-11-27T18:05:00Z
updated_at: 2026-11-27T18:05:00Z
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
