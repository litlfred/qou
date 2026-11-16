---
# qou-mxnu
title: 'A (SUPPORT): Wedderburn-block identification — pin the (4,1)/std block of H_n(q) + its explicit Markov weight matrix'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-24T16:54:56Z
updated_at: 2026-11-16T17:58:00Z
parent: qou-3l2l
---


## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-25 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-16 — Owner Ruling `Q-3L2L-1 = 1` Executed (`litlfred/qou#8141`)

- **Lean 4 formalization (`0` `sorry`, generic `{R : Type u}` per §7c):** `folio/quantum-observable-universe/lean/QOU/AlphaEM/StdBlockHoefsmitMarkovSchur.lean` (wired into `folio/quantum-observable-universe/lean/QOU.lean`, commit `593cd323f3c15de52fd2e46e8f2346c6fd815c68`, PR `https://github.com/litlfred/qou/pull/8141`):
  - Formalizes the 4-dimensional standard Young-tableau basis `SYT41` ($T_2, T_3, T_4, T_5$ indexed by the unique leg cell `(1,0)` entry in $\{2,3,4,5\}$), `legEntry_injective`, `legEntry_bounds`, `cellContent`, `cellContent_sum_eq_five` ($\sum_{k=1}^5 c(T,k) = 5$), `axialDist`, `axialDist_ne_zero`, and `axialDist_removable_transitions` ($(-2,+2), (-3,+3), (-4,+4)$ at $s_2, s_3, s_4$).
  - Proves the classical Frame–Robinson–Thrall identity `frame_robinson_thrall_41` ($5! / 30 = 4$), classical Plancherel weight `plancherel_weight_41_classical` ($w_{(4,1)}(1) = 16/120 = 2/15$), and the division-free generic-ring $q$-hook dimension identity `qFact5_eq_qDim41_mul_qHookProd41` ($[5]_q! = [4]_q \cdot \prod_{x \in (4,1)} [h(x)]_q$).
  - Defines the cleared-denominator diagonal Hoefsmit / Markov Gram weights `hoefsmitGramDiag` and matrix `hoefsmitGramMatrix` over generic `R`, proves symmetry `hoefsmitGramMatrix_symm`, off-diagonal orthogonality `hoefsmitGramMatrix_offDiag_zero`, the three exact Hoefsmit contravariant recurrences `hoefsmitGram_recurrence_step12`, `hoefsmitGram_recurrence_step23`, `hoefsmitGram_recurrence_step34` ($\tilde{g}(T_i)([d]_q^2 - 1) = \tilde{g}(T_{i+1})[d]_q^2$ for $d = 2, 3, 4$), and the classical $q \to 1$ specialization `hoefsmitGram_classical_values` ($(576, 432, 384, 360)$) and `hoefsmitGram_classical_ratios` ($(1, 3/4, 2/3, 5/8)$).
- **50-dps `mpmath` + exact rational/symbolic probe & witness:** `computations/alpha_em/std_block_hoefsmit_markov_schur_probe.py` and `computations/alpha_em/std-block-hoefsmit-markov-schur.witness.json` (9/9 assertions PASS at 50 dps / 60 dps working precision, zero `float64`), certifying $d_q(4,1)(q_0) = 4.10968241120794116176\dots$, $w_{(4,1)}(q_0) = 0.12862000417524688333\dots$, Hecke quadratic & braid relations to $< 4 \times 10^{-61}$, and contravariant Gram invariance $\sigma_k^T G_M = G_M \sigma_k$ to $1.1 \times 10^{-61}$.
- Kept at `status: in-progress` pending PR merge and owner review.
