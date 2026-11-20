---
# qou-m3tr
title: 'Bring M3: G-equivariant cell structure of a compact Riemann surface, with chi = 2 - 2g (discharges hX/hY of genus_eq_four_of_cellular)'
status: in-progress
type: task
priority: high
tags:
    - for-agy
    - bring-foundations
    - lean
created_at: 2026-11-18T19:26:09Z
updated_at: 2026-11-20T14:40:00Z
parent: qou-qhcr
---
**For agy.** Written 2026-11-18 by the Bring-foundations thread at ofri's request ("bean up for agy to do: C + A"). Parent bean `qou-qhcr` must never be closed.

## Context

Branch `claude/bring-foundations-handover-2026-11-17` (draft PR litlfred/qou#8365, issue #8364) proves genus 4 for the QOU surface from:
an A5 action and an S5 action on one closed surface, plus H¹ = 2W with W irreducible.

- `folio/quantum-observable-universe/lean/QOU/BringsSurface/IrreducibleH1ForcesGenusFour.lean` — the Riemann–Hurwitz arithmetic (core Lean, sorry-free).
- `folio/quantum-observable-universe/lean/QOU/BringsSurface/RiemannHurwitzCellular.lean` — Riemann–Hurwitz proved from orbit–stabilizer (`riemann_hurwitz_cellular`, `rh_of_cellular`), and the capstone `genus_eq_four_of_cellular`. Sorry-free; axioms propext, Classical.choice, Quot.sound.

The capstone still takes these as **hypotheses** (they are named in its signature):
- the cell data `V E F` with `MulAction G` on each;
- `hEA hFA hES hFS`: G acts freely on edges and faces;
- `hXA hXS`: χ(X) = |V| − |E| + |F| = 2 − 2g;
- `hYA hYS`: the quotient orbit counts give χ(X/G) = 2 − 2h.

## Task

Discharge those hypotheses. That means: a compact Riemann surface X of genus g with a finite group G acting holomorphically admits a G-equivariant cell structure with all branch points among the vertices, free action on edges and faces, χ = 2 − 2g, and the quotient complex has χ = 2 − 2h.

This is a large Mathlib gap: Mathlib has no compact Riemann surfaces, no triangulations of surfaces, and no Euler characteristic of a surface. Realistic sub-steps, in order:

1. **Combinatorial surface model first.** Define a finite combinatorial surface (e.g. a rotation system / ribbon graph, or a finite simplicial 2-complex whose links are cycles) with a G-action. Prove that the quotient by a free-on-edges-and-faces action is again such a complex, with orbit sets as its cells. This alone makes `hY` a consequence of `hX` plus the model, and is achievable now.
2. **Genus of the model.** Define genus combinatorially, g := (2 − χ)/2 for a connected orientable model, and prove χ is even. Then `hX` becomes a definition.
3. **Bridge to analysis (open, large).** Show a compact Riemann surface with a holomorphic G-action has such a model. This needs triangulation of compact surfaces, which is not in Mathlib. Treat it as a conditional class (AGENTS.md §3b-cond) carrying the triangulation as a hypothesis, NOT as an axiom, and say so in its name and docstring.

## Rules

- No `sorry` without `-- Ref:` (use `[farkas-kra1992]` §V.1 or `[leitner2026]`). No `: True`, no self-assuming projection. Generic `R`/types where possible (§7c).
- Step 3 must not be counted as "proved". Report what is proved and what stays a hypothesis.
- Ask ofri before opening a math PR in qou. Merge only on his tap.

## How to verify

Lean is not installable via elan here (release.lean-lang.org 403). Download the GitHub release `lean-4.24.0-linux.tar.zst`, decompress it with python `zstandard`, restore Mathlib oleans from branch `cat/folio-assistant-sci/lake-cache/qou-v4-24-0`, and run
`lean -DautoImplicit=false -s 65536 <file>` with LEAN_PATH set to the restored olean dirs. Then run `#print axioms` on new declarations. Do not run `lake build`: it evicts the restored cache.

## 2026-11-20 — W9 (session_01VQDpPcjxVSqN8ELUBjiBHk): not attempted this session

Session time went to M1b (#8532). No M3 progress. Sizing for the next agent:
- Step 1 (the quotient of a combinatorial map / rotation system by a dart-free action is a map whose cells are the orbits) is medium-sized.
- Step 2 (`χ` even for a connected orientable map) is the genus formula and is hard.
- Step 3 (triangulation) is a Mathlib gap. Keep it as a §3b-cond class, never an axiom.

## 2026-11-20 — W9: step 1 done, PR #8570

`QOU/RiemannSurface/CombinatorialMapQuotient.lean`, sorry-free; `lean -DautoImplicit=false -s 65536` exit 0.
- `cycleOrbitsEquiv`: the G-orbits of the cycles of an equivariant dart permutation are in bijection with the cycles of the induced permutation on D/G. Applied to sigma, alpha and sigma*alpha, this gives the V/E/F of the quotient map.
- `quotPerm_involutive` and `quotAlpha_fixedPointFree`: the quotient is again a map when G acts freely on edges.

Open:
- step 2: chi is even, i.e. the genus formula;
- step 3: triangulation of a compact Riemann surface (Mathlib gap);
- hX/hY remain hypotheses of the capstone.
