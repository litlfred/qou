---
# qou-8uxw
title: 'Route C step 1: groupoid-cardinality reading of the q=1 component-count cross term (Baez–Hoffnung–Walker)'
status: in-progress
type: task
priority: normal
created_at: 2026-09-06T03:31:25Z
updated_at: 2026-09-06T03:42:37Z
parent: qou-2akx
---

## 2026-09-06 — MEASURED: POSITIVE and exact at q = 1

At q = 1 with z = 1/N the Markov trace on QS_n is the normalised character of S_n on V^{⊗n}, dim V = N: N^{c(w)}/N^n — and the character of a permutation representation is a Burnside FIXED-POINT COUNT (w-invariant colourings of the strands are constant on cycles). Verified exactly on all 24 permutations of S_4 at N = 2, 3 (interleaving_cross_term_closures_probe.py, 13/13). The two words fix 2 and 8 two-colourings; the difference −6 is the T1 probe's [2]_q⁴·Δ|_{q=1}. Lean QOU/Mass/CrossTermFixedPointCount.lean pins both counts by `decide` (16-element searches) and sequential = s₂.

Groupoidification reading (Baez–Hoffnung–Walker): the character is the degroupoidified span X ← X^w → X, so the ORDER-ZERO cross term is a groupoid cardinality. The 16-dim spin-½ quantum trace degenerates to exactly this count at q = 1 (R-matrix → swap), so the q-deformation is a q-count of fixed points (μ-weighted quantum trace). OPEN step 2: is that q-count itself a groupoid cardinality (Hecke algebra as a groupoid algebra, BHW §Hecke / flag varieties over F_q — note q there is a prime power, the framework's q₀ ≈ 1.11 is not)? Not attempted here.
