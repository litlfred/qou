---
# qou-unob
title: 'Universal object: the corpus already conjectures a terminal object in C_chi (Bring at chi = -6) — different category from the Ptolemy groupoid'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - needs-owner
created_at: 2026-09-06T10:56:11Z
updated_at: 2026-10-04T15:25:17Z
parent: qou-gwte
---

folio/quantum-observable-universe/brings-surface/universality-general.md:
  "For any admissible Euler characteristic chi, the category C_chi of C quantum
   observable universes with chi(S) = chi should admit a TERMINAL OBJECT
   determined by the unique maximally symmetric Riemann surface of the
   corresponding genus. Bring's curve distinguishes the Descartes case
   chi = -6, but analogous universal objects are expected at other values."

That is the corpus's universal-object claim and it lives in a category of
UNIVERSES, which is NOT a groupoid — so it is not touched by the qou-ptgd
prune, and it is the correct home for a "universal object" statement.
See also terminal-morphism-brings.{md,ts}.

The dialog conflates two different universality claims. Worth stating the
distinction explicitly in the block; worth NOT importing "terminal object"
vocabulary into any Ptolemy/Pachner setting.

## RECORDED 2026-09-06 — distinction written up; the CONJECTURE stays open

Audit §6. The C_chi terminal object is a CONJECTURE in universality-general.md
("should admit a terminal object"), so this bean stays open per AGENTS.md 13a.
What is settled is only that it is untouched by the qou-ptgd prune, because
C_chi is a category of universes and not a groupoid.

## Round 72 Progress (PR #8491)
- De-vacuified and proved genuine Lean 4.24.0 theorems in PR `litlfred/qou#8491` (C1 `0a93eba0e8b5b8ee92b4af6972a325d2dc1a28fd`, C2 `a9b922df9d2baa717878dbac10e60b5a5c341c6e`, 80-dps mpmath witness verified, 0 static audit findings).
