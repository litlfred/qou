---
# qou-ep0a
title: 'Infra: general-n Markov trace stabilization in Lean — τ-functor F3 (trace realization)'
status: in-progress
type: feature
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-07-18T23:52:24Z
updated_at: 2026-11-16T18:30:00Z
parent: qou-rtxm
---

τ F3 = categorical trace realized as tr_M = Σ_λ y_λ χ^λ. Framework-open at general n: the Markov stabilization tr_{n+1}∘ι = tr_n. n=2 (TMCorrespondence) and n=3 (H3.trM, obsH3_cyclic) are concrete/proved sorry-free; generalize. Feeds observationFrame = ev∘tr_M (derived cyclic in PR #4028).

## 2026-11-16 — General-`n` Markov Trace Tower Stabilization Formalized (`litlfred/qou#8148`)

- **Lean 4 formalization (`0` `sorry`, generic `R` per §7c):** `folio/quantum-observable-universe/lean/QOU/Torsion/MarkovTraceTowerStabilization.lean` (wired into `folio/quantum-observable-universe/lean/QOU.lean`, commit `b1cda0ed48b69b13bf48c75340c8f842a671b780`, PR `https://github.com/litlfred/qou/pull/8148`), complementing `QOU/Torsion/MassTraceMarkov.lean` and `QOU/Torsion/MassTraceMarkovClass.lean`:
  - Defines `MarkovTraceTower R A` over generic commutative ring `R` with tower inclusions `incl n : A n → A (n + 1)` ($\iota_n$), new-strand generators `gen n : A (n + 1)` ($g_n$), traces `tr n : A n → R` ($\operatorname{tr}_n$), and Markov parameter `z : R` satisfying **(M1)** F3 stabilization $\operatorname{tr}_{n+1}(\iota_n(x)) = \operatorname{tr}_n(x)$, **(M2)** Markov reduction $\operatorname{tr}_{n+1}(\iota_n(x) g_n) = z \operatorname{tr}_n(x)$, and **(M3)** trace cyclicity.
  - Proves by induction on $k$ that `tr_iterated_inclusion` ($\operatorname{tr}_{n+k}(\iota_{n,n+k}(x)) = \operatorname{tr}_n(x)$) and `tr_stabilized_word` ($\operatorname{tr}_{n+k}(\iota_{n,n+k}(x) g_n \cdots g_{n+k-1}) = z^k \operatorname{tr}_n(x)$) hold for all $n, k \in \mathbb{N}$.
  - Defines `observationFrame = ev ∘ tr_n` and proves `observationFrame_iterIncl` and `observationFrame_conj` (conjugation invariance).
  - Proves `wedderburn_branching_stabilizes`: the Wedderburn weight conservation law $y_\lambda = \sum_{\mu \succ \lambda} y_\mu$ under character restriction $\chi^\mu(\iota_n(x)) = \sum_{\lambda \prec \mu} \chi^\lambda(x)$ implies F3 stabilization $\operatorname{tr}_{n+1}(\iota_n(x)) = \operatorname{tr}_n(x)$, with concrete $n = 2 \to 3$ branching and non-vacuity theorems (`classical_branching_n2_to_n3_exact`, `non_vacuity_markov_tower_and_branching`).
- Kept at `status: in-progress` pending PR merge and owner review.
