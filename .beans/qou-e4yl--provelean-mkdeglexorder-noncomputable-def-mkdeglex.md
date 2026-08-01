---
# qou-e4yl
title: 'PROVE(lean): mkDegLexOrder — noncomputable def mkDegLexOrder {G : Type u} [DecidableEq G] (rank : G → ℕ) (rank_inj : Fu [cited bergman1978]'
status: todo
type: task
tags:
    - lean
    - cited-sorry
    - paper-ugb
    - tractable
    - cite-bergman1978
created_at: 2026-08-01T23:31:10Z
updated_at: 2026-08-01T23:31:10Z
parent: qou-k1mq
---

**File:** `UGB/GrobnerShirshov/AlgOps.lean` (UGB)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/unital-groebner-bases/lean/UGB/GrobnerShirshov/AlgOps.lean

### `mkDegLexOrder`  —  line 293  ·  tier **T** (tractable-in-Mathlib-today)
- **Proposition:** `noncomputable def mkDegLexOrder {G : Type u} [DecidableEq G] (rank : G → ℕ) (rank_inj : Function.Injective rank) : AdmissibleOrder G where lt := fun a b => a.length < b.length ∨ (a.length = b.length ∧ List.Lex (fun x y => rank x < rank y) a b) trichotomy `
- **Cited:** `[bergman1978]`
  - [bergman1978] Bergman (1978), *The diamond lemma for ring theory* — https://doi.org/10.1016/0001-8708(78)90010-5
- **Tractability:** deg-lex admissible order well-foundedness; Mathlib's List.Lex well-foundedness + Nat measure supply the ingredients.
- **Next step:** Formalize now — Mathlib ingredients exist. Prove the stated goal directly, keep sorry-free.
