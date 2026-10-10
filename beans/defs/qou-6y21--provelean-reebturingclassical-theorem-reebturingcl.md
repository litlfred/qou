---
# qou-6y21
title: 'PROVE(lean): ReebTuringClassical — theorem ReebTuringClassical : ∃ halts : ℕ → Prop, ¬ ∃ dec : ℕ → Bool, ∀ n, halts n ↔ dec n [cited cardona2021]'
status: completed
type: task
priority: normal
tags:
    - paper-qou
    - tractable
    - cite-cardona2021
    - reorg-2026-10-04
    - lean
    - cited-sorry
created_at: 2026-08-01T23:31:05Z
updated_at: 2026-10-04T15:22:44Z
parent: qou-k1mq
---

**File:** `QOU/Information/ReebTuringClassical.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/quantum-observable-universe/lean/QOU/Information/ReebTuringClassical.lean

### `ReebTuringClassical`  —  line 34  ·  tier **T** (tractable-in-Mathlib-today)
- **Proposition:** `theorem ReebTuringClassical : ∃ halts : ℕ → Prop, ¬ ∃ dec : ℕ → Bool, ∀ n, halts n ↔ dec n = true `
- **Cited:** `[cardona2021]`
  - [cardona2021] Cardona, Miranda, Peralta-Salas, Presas (2021), *Constructing Turing complete Euler flows in dimension 3* — https://doi.org/10.1073/pnas.2026818118
- **Tractability:** ∃ an undecidable predicate on ℕ; Mathlib computability (ComputablePred / halting undecidability) supplies the ingredients.
- **Next step:** Formalize now — Mathlib ingredients exist. Prove the stated goal directly, keep sorry-free.



## Summary of Changes

Closed 2026-10-04 in the work-plan reorganisation: the work has landed on main. Evidence: [M] k1mq child: no real sorry left in target file. ReebTuringClassical theorem uncond, 0 sorry
