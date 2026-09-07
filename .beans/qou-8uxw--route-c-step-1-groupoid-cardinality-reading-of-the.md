---
# qou-8uxw
title: 'Route C step 1: groupoid-cardinality reading of the q=1 component-count cross term (Baez–Hoffnung–Walker)'
status: in-progress
type: task
priority: normal
created_at: 2026-09-06T03:31:25Z
updated_at: 2026-09-07T09:03:48Z
parent: qou-2akx
---

## 2026-09-06 — MEASURED: POSITIVE and exact at q = 1

At q = 1 with z = 1/N the Markov trace on QS_n is the normalised character of S_n on V^{⊗n}, dim V = N: N^{c(w)}/N^n — and the character of a permutation representation is a Burnside FIXED-POINT COUNT (w-invariant colourings of the strands are constant on cycles). Verified exactly on all 24 permutations of S_4 at N = 2, 3 (interleaving_cross_term_closures_probe.py, 13/13). The two words fix 2 and 8 two-colourings; the difference −6 is the T1 probe's [2]_q⁴·Δ|_{q=1}. Lean QOU/Mass/CrossTermFixedPointCount.lean pins both counts by `decide` (16-element searches) and sequential = s₂.

Groupoidification reading (Baez–Hoffnung–Walker): the character is the degroupoidified span X ← X^w → X, so the ORDER-ZERO cross term is a groupoid cardinality. The 16-dim spin-½ quantum trace degenerates to exactly this count at q = 1 (R-matrix → swap), so the q-deformation is a q-count of fixed points (μ-weighted quantum trace). OPEN step 2: is that q-count itself a groupoid cardinality (Hecke algebra as a groupoid algebra, BHW §Hecke / flag varieties over F_q — note q there is a prime power, the framework's q₀ ≈ 1.11 is not)? Not attempted here.



## 2026-09-07 — STEP 2 MEASURED: NEGATIVE for the unweighted reading, invariant named

Probe computations/probes/route_c_step2_pivotal_vs_count_probe.py (17/17, exact sympy; proton pin only for the diagnostic numbers). On V^{⊗4} the ordinary trace (the count-shaped / BHW reading, z_J = (3q − q⁻¹)/4) and the framework's convention-D pivotal trace (z_D = q³/(q²+1)) share the Burnside count at q = 1 AND the slope there, and split at second order: z_J − z_D = −(q²−1)²/(4q(q²+1)), exactly. The structural reason the unweighted count is not the framework's object: it is NOT a Markov trace — the partial trace of R over the closed strand is diag(2q − q⁻¹, q), scalar iff q² = 1 (Lean QOU.Mass.RouteCPivotalVsCount, sorry-free), and the Markov property fails on 4 of 6 elements of S₃; the pivotal weight makes the partial trace q²·𝟙. Integrality does NOT separate the two (2⁴tr_J and [2]⁴tr_D are both integer Laurent polynomials on all 24 words of S₄). n = 4 pair: Δ_J = −(4q⁶+3q²−1)/(16q³) vs Δ_D = −q³Φ₃Φ₆/Φ₄³; at the pin Δ_J/Δ_D = 1.0085. CONSEQUENCE: the framework's q-deformation of the fixed-point count is the K-WEIGHTED count (weight q^{#0−#1} per colouring); a BHW groupoidification of route C's q-count needs a weighted groupoid cardinality, which the held BHW paper does not supply. Open: whether a weighted (graded) groupoid cardinality reading exists — a literature question, not a computation.
