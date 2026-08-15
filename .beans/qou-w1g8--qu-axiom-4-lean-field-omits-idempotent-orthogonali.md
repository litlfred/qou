---
# qou-w1g8
title: QU axiom 4 Lean field omits idempotent orthogonality + completeness (needs Preadditive)
status: todo
type: task
created_at: 2026-08-15T00:23:28Z
updated_at: 2026-08-15T00:23:28Z
---


## What is and is not encoded

`QuantumUniverse.blocks/centralIdem/frobWeight/dimQ` (landed #5021) encodes:
finitely many blocks, an idempotent endomorphism per block, non-vanishing
Frobenius weight and quantum dimension.

It does NOT encode mutual orthogonality of the idempotents
(`b ≠ b' → p_b ≫ p_b' = 0`) or completeness of their sum (`Σ p_b = 𝟙`).
`QuantumUniverse` carries neither prerequisite, but **the two gaps cost
differently** and should not be worked as one:

| gap | needs | cost |
|---|---|---|
| orthogonality `p_b ≫ p_b' = 0` | `HasZeroMorphisms` — a zero morphism, nothing more | cheap |
| completeness `Σ p_b = 𝟙` | `Preadditive` — `AddCommGroup (X ⟶ Y)` for the finite sum | needs the decision below |

Orthogonality is addable on its own and is the larger share of what
"semisimple" is doing here. (Caught by Copilot on #5047; the first draft of
this bean, and the Lean docstrings merged in #5021, conflated the two.)

So the field as written is satisfied by a structure with idempotents that
overlap and do not span. That is weaker than "semisimple" and the docstring says
so, but the gap is real: the axiom's NAME promises Wedderburn and its TYPE
delivers less.

## The fix has a prerequisite
Adding `[Preadditive C]` to `QuantumUniverse` is the obvious route and is a
bigger decision than this bean — it changes what a quantum universe is, and the
paper's `R`-linear phrasing may already imply it (check `def:rigid-monoidal-category`
§"We say C is R-linear ..."). Do not add the instance without deciding that
question first.
