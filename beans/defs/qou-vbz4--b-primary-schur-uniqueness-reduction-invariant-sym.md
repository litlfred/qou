---
# qou-vbz4
title: 'B (PRIMARY): Schur-uniqueness reduction — invariant symmetric forms on irreducible std unique up to scalar ⇒ Markov Gram ∝ Hodge Gram (Lean core + reduce to scale c + S₅-equivariance premise)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-24T16:54:55Z
updated_at: 2026-11-16T17:58:00Z
parent: qou-3l2l
---

## 2026-11-16 — Owner Ruling `Q-3L2L-1 = 1` Executed (`litlfred/qou#8141`)

- **Lean 4 formalization (`0` `sorry`, generic `{R : Type u}` per §7c):** `folio/quantum-observable-universe/lean/QOU/AlphaEM/StdBlockHoefsmitMarkovSchur.lean` (wired into `folio/quantum-observable-universe/lean/QOU.lean`, commit `593cd323f3c15de52fd2e46e8f2346c6fd815c68`, PR `https://github.com/litlfred/qou/pull/8141`), complementing the on-`main` `QOU/Archimedean/SchurInvariantFormProportional.lean`, `QOU/Archimedean/MatrixSchurCommutant.lean`, `QOU/Archimedean/MarkovGramRealSymm.lean`, and `QOU/Archimedean/InvariantFormTransport.lean`:
  - Formalizes `InvariantFormInSchurLine` over generic `R` on `SYT41 × SYT41` and proves `schur_invariantForm_proportional` ($B_1(u,v) = c \cdot B_2(u,v)$ with $c = \text{markov\_norm} \cdot \text{hodge\_norm}^{-1}$), uniqueness `schur_scalar_unique`, and invertibility `schur_scalar_unit` ($c \cdot c^{-1} = 1$, $c^{-1} \cdot c = 1$).
  - Proves the non-vacuity theorem `non_vacuity_unaligned_not_proportional`: without the $S_5$-equivariant intertwiner $U$, the raw isogeny-frame Hodge diagonal $(5, 5, 5, 1)$ is NOT entrywise proportional to the classical Hoefsmit diagonal $(576, 432, 384, 360)$ over $\mathbb{Z}$, establishing that the $S_5$-equivariance / intertwiner premise is load-bearing.
- **50-dps `mpmath` + exact rational/symbolic probe & witness:** `computations/alpha_em/std_block_hoefsmit_markov_schur_probe.py` and `computations/alpha_em/std-block-hoefsmit-markov-schur.witness.json` (9/9 assertions PASS), certifying 1-dimensionality (`nullity == 1`) of the symmetric contravariant-form space on $V_{(4,1)}$ and the exact rational intertwiner transport $W^T M_S W = 10 \cdot \mathrm{diag}(1, 3/4, 2/3, 5/8)$ ($\det W = 5$, $c_{q=1} = 1/10$) between the Braden–Northover Hodge Gram $M_S = 5 I_4 - J_4$ and the Hoefsmit diagonal Gram.
- Kept at `status: in-progress` pending PR merge and owner review.

