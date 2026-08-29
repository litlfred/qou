---
# qou-v7ro
title: 'GAP: bridge Magnus coeff mu-bar(12..A)=+/-1 to the QOU Markov-trace deficit leading coefficient (close MilnorExactOrderConjecture)'
status: in-progress
type: task
priority: normal
created_at: 2026-08-01T23:10:14Z
updated_at: 2026-08-29T18:42:54Z
---

## What is proved (branch claude/milnor-exact-order-coefficient-proof-2026-08-01)

`MilnorMagnusCoefficient.lean` (sorry-free, lean-direct exit 0): the length-A
Milnor/Magnus coefficient `μ̄(12…A) = ±1 ≠ 0`, derived by evaluating #4471's Lie
iterated-commutator tower on the elementary matrices `E_{i,i+1}` (faithful
nilpotent rep) → `iterCommTower magnusGen n = (−1)ⁿ • E_{0,n+1}`. The surviving
coefficient is the off-diagonal `(0,A)` matrix coordinate (a NON-cyclic
functional); its cyclic trace is 0 (`trace_magnusGen_realization_eq_zero`),
matching #4480's Route-B `cyclic_trace_kills_iterCommTower`.

## What stays OPEN (this GAP)

`MilnorExactOrderConjecture` (#4471) — the QOU **Markov-trace** deficit
`D_A(h) = 1 − τ_A` leading coefficient ≠ 0 — is NOT closed. The proved Magnus
coefficient lives in the off-diagonal `(0,A)` coordinate; the QOU deficit uses a
**cyclic Markov trace**, which annihilates that off-diagonal element (Route B).
The bridge — that the Markov-trace deficit's order-`2(A−1)` leading coefficient
equals (up to a nonzero normalisation) the off-diagonal Magnus coefficient `±1`
— is the Bar-Natan / Habegger–Masbaum Milnor = leading-Vassiliev theorem
(`BrunnianVassilievBridge`, instance-less in the Vassiliev scaffold).

## Why it failed / what's needed

Mathlib has no Kontsevich-integral / finite-type invariant theory, so the bridge
cannot be discharged from library results. Two sub-obstructions:
  1. **DD-1 factor-of-2 grading** (`MilnorVassilievGrading.lean`): QOU order is
     `2(A−1)` but the standard Milnor Vassiliev degree is `A−1` — the doubling
     (h = 2·sinh ℏ, plus the deficit being a *squared*-magnitude object) must be
     proved, not assumed.
  2. **trace ↔ Magnus-coordinate identification**: connect the cyclic Markov
     trace's degree-`2(A−1)` part to the off-diagonal Magnus coordinate. The
     Jones-polynomial Vassiliev expansion (Bar-Natan) is the route; needs a
     formalised weight-system evaluation on the Brunnian chord diagram.

## Next honest step

Either (a) formalise enough of the Jones-Vassiliev weight system to evaluate the
degree-`2(A−1)` weight on the A-component Brunnian diagram and show it is the
Magnus coefficient (large), or (b) leave `MilnorExactOrderConjecture` /
`BrunnianVassilievBridge` instance-less and keep the honest conditional results.
Do NOT fabricate an instance; do NOT wire `μ̄_A = (3/4)(−2)^{A−3}` as canonical
(it is MEASURED, #4480).
