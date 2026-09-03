---
# qou-60ew
title: 'Sum case of the ramified shift calculus: can Σ_k c_k σ^k revive the residue slot by cancellation, and what odd-shift forces on the rank-2 A(q,x)'
status: in-progress
type: task
created_at: 2026-09-03T10:34:05Z
updated_at: 2026-09-03T10:41:33Z
---


Continues `qou-4g01` (#6474, merged `e9c390ff7d`). The W1 prune there is for
SINGLE-shift operators; its audit's "Honest scope" leaves the sum case open.

Branch `claude/shift-calculus-sum-case-2026-09-03`.

Plan:
1. Lean: extend `QOU.Mathlib.RamifiedShiftCalculus` with finite sums of shift
   operators (`Σ_k c_k σ^k`): residue slot of a sum = sum of slots; a sum of
   derivative-like terms of shifts 1 and 2 still has a dead residue slot at
   every jet level on a power-series seed (no cancellation can revive what is
   termwise zero); decompose a general element by shift parity; what a
   non-zero residue forces (some term with `c_k(-k) ≠ 0`), and what the (-1)^n
   residual forces on the odd/even parts.
2. Probe: exact sympy check of the sum case, including a NON-vacuity witness
   where two non-derivative terms cancel each other's residue.
3. Audit doc + one scope sentence on the conjecture block.
