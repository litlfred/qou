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
updated_at: 2026-11-20T19:45:00Z
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

## 2026-11-20 — W9: step 2 parity done, PR #8650

`QOU/RiemannSurface/CombinatorialMapEuler.lean`, sorry-free.
- `euler_even` / `exists_genus`: chi = c(sigma) - c(alpha) + c(sigma alpha) is even, so chi = 2 - 2g with g : Z.
- Proof: the sign homomorphism, via `sign_eq_neg_one_pow` (sign pi = (-1)^(|D| + c(pi))) and `card_cycles`.
- No connectivity is needed.

**Still open in step 2:** g >= 0 for a connected map. In permutation form: if <sigma, alpha> is transitive on D, then c(sigma) + c(alpha) + c(sigma alpha) <= |D| + 2. This is the Riemann–Hurwitz / Euler inequality for maps.
- Triangle inequality plus connectivity gives only N(sigma) + N(alpha) >= n - 1, with N = n - c. That is not enough.
- Needs an edge-deletion induction. Estimate: multi-session.

**Step 3** (triangulation) is unchanged: a Mathlib gap.

## 2026-11-20 — W9: proof plan for g >= 0 (not formalised)

**Target.** If σ, α ∈ Perm D, α is a fixed-point-free involution, and ⟨σ, α⟩ is transitive on D ≠ ∅, then c(σ) + c(α) + c(σα) ≤ |D| + 2.

**Paper proof.**
1. Write α = t₁⋯t_k as k = |D|/2 = c(α) disjoint transpositions, and let σⱼ = σ·t₁⋯tⱼ.
2. **Lemma S:** multiplying by a transposition (a b) changes c by exactly ±1. It is +1 (a split) if a and b are in the same cycle, and −1 (a merge) otherwise.
3. Track the orbit count of ⟨σ, t₁, …, tⱼ⟩:
   - it starts at c(σ) and ends at 1 (transitivity);
   - a split step does not change it, since a and b are already in one orbit;
   - a merge step lowers it by at most 1.
4. So the number of merges is m ≥ c(σ) − 1.
5. Then c(σα) = c(σ) + k − 2m ≤ k − c(σ) + 2, which is the target.

**Mathlib status (searched the olean name strings of `Perm/*`).** There is no Lemma S. The closest results are `card_support_swap_mul` and `support_swap_mul_eq`, which are about supports, not cycle counts. Lemma S must be built from SameCycle(π·swap a b) versus SameCycle π, which is the bulk of the work.

## 2026-11-20 — W9: Lemma S proved, PR #8657

`QOU/RiemannSurface/CycleCountSwap.lean`, sorry-free.
- `numCycles_mul_swap_of_sameCycle` (+1, split) and `numCycles_mul_swap_of_not_sameCycle` (-1, merge).
- Proof: cycles avoiding {a,b} coincide; the cycles meeting {a,b} number 1 or 2; the sign forces an odd change.

#8650 (`euler_even`) merged as `50d2e86bc1`.

**Remaining for g >= 0:**
1. Decompose alpha into disjoint swaps.
2. Track the class count O_j of the equivalence generated by SameCycle sigma plus the pairs added so far. Need: adding a pair lowers O by at most 1, and SameCycle sigma_j is contained in R_j.
3. Invariant: c(sigma_j) <= j - c(sigma) + 2 O_j.
