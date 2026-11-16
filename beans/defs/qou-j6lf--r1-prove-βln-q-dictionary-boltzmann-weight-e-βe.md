---
# qou-j6lf
title: 'R1: prove β=ln q dictionary — Boltzmann weight e^{-βE_λ} ≡ Frobenius weight y_λ(q); read off E_λ'
status: in-progress
type: task
priority: normal
tags:
    - 8f-qcd
    - reorg-2026-10-04
created_at: 2026-08-02T18:33:15Z
updated_at: 2026-10-10T07:16:10Z
parent: qou-8lxd
---

Near-term. Identify the stat-mech Boltzmann factor with the Frobenius/Markov weight y_λ(q): e^{-β E_λ} = y_λ(q) with β = ln q ⇒ E_λ = -ln y_λ(q)/ln q. Lean: a clean identity over ℝ (archimedean — uses ln). Grounds the 'partitions ARE thermal states' claim. Cross-ref qou-ud3o (Wick: real q=thermal, |q|=1=real-time).

## ✅ PROVED (2026-08-02) — sorry-free Lean

[`QBetaEnergyDictionary.lean`](https://github.com/litlfred/qou/blob/claude/agent-task-662242-vag458/folio/quantum-observable-universe/lean/QOU/QuantumObservableUniverses/QBetaEnergyDictionary.lean),
namespace `QOU.Thermo`, β = ln q (β>0 for q>1 via `logPos_of_one_lt`):

- `boltzmann_energyOf` — read-off correct: `e^{-β·(-ln y/β)} = y` (derive-then-check, β≠0, y>0).
- `energyOf_unique` — the energy is the UNIQUE solution (Boltzmann map injective).
- `energyOf_le_iff` — **order-reversing**: `E_λ₁ ≤ E_λ₂ ↔ y_λ₂ ≤ y_λ₁`. The
  falsifiable physical content — the dominant Wedderburn block (largest
  Frobenius weight) is the GROUND STATE.
- `partition_sum_eq` — `∑_λ d_λ·e^{-βE_λ} = ∑_λ d_λ·y_λ`: the stat-mech
  partition function in energy variables IS the Frobenius weighted sum.

All axiom-clean (`propext, Classical.choice, Quot.sound`); lean-direct exit 0;
wired into `QOU.lean`.

**What this closes:** R1 of the partition-function unification (`qou-3ffh`).
"Partitions = thermal states, β = ln q" is now a proved dictionary, not a
slogan. **What it does NOT close:** it takes y_λ>0 as given (the actual
Frobenius weights are supplied by R2/Schur-Weyl `qou-mpq5`); and it closes
no physics observable — energies are relative to the weights, not absolute
masses. Honest scope: the dictionary is proved; the weights that feed it
are R2's job.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-02 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress (2026-11-16T19:43:48Z)
- **Status:** `in-progress` (awaiting human review; no unilateral closure).
- **PR:** `litlfred/qou#8173` (head `ad97deb87bc648e5c129faba2fa1d69d9619253c`, script commit `bdc558a8f10d26666ba057c81bf22753e6d0aca0`).
- **Summary:** Formalized exact Boltzmann-Frobenius dictionary (beta = ln q, E_lambda = -(ln y_lambda(q))/(ln q)) and energy-ordering theorems in QOU/Eightfold/BoltzmannOSPositivityAndColourSaddle.lean + 50-dps witness probe in PR litlfred/qou#8173 (head ad97deb87bc648e5c129faba2fa1d69d9619253c).
