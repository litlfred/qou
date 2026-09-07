---
# qou-8uxw
title: 'Route C step 1: groupoid-cardinality reading of the q=1 component-count cross term (Baez–Hoffnung–Walker)'
status: in-progress
type: task
priority: normal
created_at: 2026-09-06T03:31:25Z
updated_at: 2026-09-07T10:03:41Z
parent: qou-2akx
---

## 2026-09-06 — MEASURED: POSITIVE and exact at q = 1

At q = 1 with z = 1/N the Markov trace on QS_n is the normalised character of S_n on V^{⊗n}, dim V = N: N^{c(w)}/N^n — and the character of a permutation representation is a Burnside FIXED-POINT COUNT (w-invariant colourings of the strands are constant on cycles). Verified exactly on all 24 permutations of S_4 at N = 2, 3 (interleaving_cross_term_closures_probe.py, 13/13). The two words fix 2 and 8 two-colourings; the difference −6 is the T1 probe's [2]_q⁴·Δ|_{q=1}. Lean QOU/Mass/CrossTermFixedPointCount.lean pins both counts by `decide` (16-element searches) and sequential = s₂.

Groupoidification reading (Baez–Hoffnung–Walker): the character is the degroupoidified span X ← X^w → X, so the ORDER-ZERO cross term is a groupoid cardinality. The 16-dim spin-½ quantum trace degenerates to exactly this count at q = 1 (R-matrix → swap), so the q-deformation is a q-count of fixed points (μ-weighted quantum trace). OPEN step 2: is that q-count itself a groupoid cardinality (Hecke algebra as a groupoid algebra, BHW §Hecke / flag varieties over F_q — note q there is a prime power, the framework's q₀ ≈ 1.11 is not)? Not attempted here.



## 2026-09-07 — STEP 2 MEASURED: NEGATIVE for the unweighted reading, invariant named

Probe computations/probes/route_c_step2_pivotal_vs_count_probe.py (17/17, exact sympy; proton pin only for the diagnostic numbers). On V^{⊗4} the ordinary trace (the count-shaped / BHW reading, z_J = (3q − q⁻¹)/4) and the framework's convention-D pivotal trace (z_D = q³/(q²+1)) share the Burnside count at q = 1 AND the slope there, and split at second order: z_J − z_D = −(q²−1)²/(4q(q²+1)), exactly. The structural reason the unweighted count is not the framework's object: it is NOT a Markov trace — the partial trace of R over the closed strand is diag(2q − q⁻¹, q), scalar iff q² = 1 (Lean QOU.Mass.RouteCPivotalVsCount, sorry-free), and the Markov property fails on 4 of 6 elements of S₃; the pivotal weight makes the partial trace q²·𝟙. Integrality does NOT separate the two (2⁴tr_J and [2]⁴tr_D are both integer Laurent polynomials on all 24 words of S₄). n = 4 pair: Δ_J = −(4q⁶+3q²−1)/(16q³) vs Δ_D = −q³Φ₃Φ₆/Φ₄³; at the pin Δ_J/Δ_D = 1.0085. CONSEQUENCE: the framework's q-deformation of the fixed-point count is the K-WEIGHTED count (weight q^{#0−#1} per colouring); a BHW groupoidification of route C's q-count needs a weighted groupoid cardinality, which the held BHW paper does not supply. Open: whether a weighted (graded) groupoid cardinality reading exists — a literature question, not a computation.



REFINED same day (checks 18–23 of the same probe): the K-weight is itself a cardinality. With T_w = q^{l(w)}σ_w and Q = q², the per-weight-space traces N_k(w) = q^{l(w)} tr(P_k σ_w) are polynomials in Q, non-negative integers at every prime power Q tested, refined-Burnside at q = 1, and q^{l(w)}[2]^n tr_D(w) = Σ_k q^{n−2k} N_k(w). Since q^{n−2k} = Q^{(n−2k)/2} is |F_Q^{n/2−k}| or |B(F_Q^{k−n/2})| when n is EVEN, the framework's convention-D trace IS a BHW-style groupoid cardinality (of ⊔_k Fix_k(w) × A_k) for even n; for odd n the weight is an odd power of Q^{1/2} (BLM's v) and the F_Q reading fails at the weight. So step 2 is two-sided: unweighted reading NO (Markov failure), K-weighted reading YES for even n. Open: odd n (n = 3A, odd A) — quadratic extension or the v-form. Nothing about b3 yet.



ODD n RESOLVED same day (checks 24–26, 26/26): take the framework's q itself as the prime power p; the counts N_k(w) live over F_{p²} (non-negative integers at Q ∈ {4,9,25,49,64}, all six words of S₃, e.g. N_k(s0) = (Q, 2Q−1, 2Q−1, Q)) and the weights p^{n−2k} are |F_p^{n−2k}| / |B(F_p^{2k−n})| over the index-2 subfield — cardinalities for EVERY n. So the convention-D trace is a BHW groupoid cardinality of ⊔_k Fix_k(w) × A_k for all n; only the unweighted reading fails (Markov). NEXT honest question: the binding functional is a LOG-trace difference — a log of a cardinality is not a cardinality — so whether route C reaches b3 is the §7g extensive-term problem, not a trace question. PR #7030.



2026-09-07: PR #7030 merged (38a4aa45d7). Step 3 (the log-trace question) dispatched to a planning agent (label routec-log); plan to be filed by the parent session.



2026-09-07 PLAN FILED: docs/audits/2026-09-07-route-c-step3-and-kz-level-plans.md §A (agent routec-log, parent-verified). Queue: A1 = exact-in-q bond factorisation of the canonical non-monotone word at n = 9 (the decisive compute), A2 = Lean quantisation of the classical b3 (E₀·ln2·m), A3 = convolution lemma. PR #7035.



2026-09-07 A1 EXECUTED (agent routec-a1, parent re-run 76/76): bond factorisation holds EXACTLY at n = 9 on the canonical non-monotone word for ppn/pnn/ppp/nnn — C(β123)C(free) = C(β12)C(β23) identically in q; each bond contributes q·(z_D + d_bond) exactly. So b3 ≡ 0 on the production chain word at every q-adic order at A = 3 (scope (b), invariant = the identity; general A: MarkovBondFactor general case, qou-g8i1). A route-C b3 needs a non-chain word class or something outside the trace. S1 Lean landed (WeightedCountConvolution). Audit §0b. PR #7035.
