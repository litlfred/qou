---
# qou-8uxw
title: 'Route C step 1: groupoid-cardinality reading of the q=1 component-count cross term (Baez–Hoffnung–Walker)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-06T03:31:25Z
updated_at: 2026-11-17T07:34:00Z
parent: qou-v2om
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


## 2026-09-13 — STEP 4 of the plan is DONE, and it was not 4–8 h of new mathematics: it was already proved under another bean's name

`docs/audits/2026-09-07-route-c-step3-and-kz-level-plans.md` §A step 4 reads
*"formalise gap-multiplicativity for disjoint blocks with interior bond crossings
(the `MarkovBondFactor` general-`A` gap, `qou-g8i1`) — this is what turns (i)
into scope-(b) for all `A`"*, costed **4–8 h, high risk ("needs the cross-level
Markov axiom the class lacks")**.

**That axiom is the `qou-gr3t` hypothesis, and `qou-gr3t` discharged it this
morning.** `QOU.Hecke.InteriorMarkovOfBraidedTower.interiorMarkov_of_braided`
(#7265, merged `386cc36a05`) proves `InteriorMarkov` on **every** `BraidedTower`
— the three Iwahori–Hecke relations, nothing about the trace beyond the Markov
axioms — via `HeckeSandwichReduces.disjointBlock_of_braided` (`qou-301d`).
Composed with `tr_bondWord_of_interiorMarkov`, the general-`A` bond product for
arbitrary **non-monotone** block words follows unconditionally there.

What was still missing between the two was a **shape**, not a theorem: the
bond-word result carries blocks between the bonds, while `MarkovBondFactor`'s
gap is quoted for the bare product of bond letters. `QOU/Hecke/PureBondChainProduct.lean`
(new, PR #7337, sorry-free, `lean`-direct exit 0, axioms
`propext, Classical.choice, Quot.sound`) closes it:
`tr ((σ_{g₀}+d₀)·(σ_{g₁}+d₁)·⋯) = ∏_k (z + d_k)` for strictly increasing bonds,
conditionally on `InteriorMarkov` and then on every braided tower.

**Consequence for route C, stated with its limits.** A1's `b₃ ≡ 0` on the
canonical non-monotone word was scope-(b) *at `A = 3`*, with the `n = 9`
polynomial identity as invariant. On any braided tower it now holds for a chain
of **arbitrarily many** bonds with arbitrary blocks between them — which is
exactly what step 4 existed to buy. The route-C conclusion therefore strengthens
in the direction it already pointed: **a route-C `b₃` needs a non-chain word
class or something outside the trace.** No production number moves.

**Three limits, or this gets over-quoted** (all three are in the file's own
docstring):

1. The coefficient is `1`, not a general `c_k` — `c • σ + d` factors only over a
   field, and the ring is a bare `CommRing`. Not a restriction on the corpus:
   all three production bond types carry `c = 1` (`f_pp`, `f_nn`, `f_pn`), as
   `MarkovBondFactor`'s own docstring lists them.
2. It is proved in the **tower** class, not in `MarkovBondFactor`'s
   `QOU.Hecke.MarkovTrace n q A`, which is fixed-level and single-algebra with
   **no filtration** and therefore cannot even *state* "`a` below the bond, `b`
   above it". That is precisely what "the class does not yet carry" recorded,
   and it stays true of that class; transporting the result there is a separate
   bridge, not done.
3. A braided tower is **not yet the production trace** — the Ocneanu trace of
   `H_n(q)` at `z = q³/(q²+1)` is proved unique as a
   `HeckeCoset.MarkovTraceFamily` and is not packaged as an
   `OcneanuTrace.MarkovTrace` (`qou-gr3t` remaining item, `qou-0fmb`).

Step 1 (S2 Lean) was correctly declined on 2026-09-07 as definitional; step 3
(S1) landed as `WeightedCountConvolution`. So the plan's queue is now clear
except for the packaging in limit 3.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-07 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-15 — re-scoped by the γγ rule

The owner ruled that the γγ selection rule also covers the nuclear bond letters. Any number in this bean computed on the single-crossing interface letters of `atom_braid_word_3A` (`d_k`, `μ_e`, the chain law `∏(z_D + d_k)`, the `b₃` magnitudes −1.2277 / −0.7973 MeV, or a sign map on that word) is now a record of a superseded word, not a current result. Lean results stated for generic bond weights are unaffected. The redo waits on a γγ-selected word per nucleus (PR #7876). Record: `docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md`. The bean stays open.

## Round 63 Update (PR #8257)
- Formalized in PR https://github.com/litlfred/qou/pull/8257 (head `18cf0bc120a9baf3be0677bec0817855b4de7a7a`, Commit 1 `2b12359f227b0dc628cdd0df3e8f7f2f6ff6c5ca`, `scriptHash: 1bf530249a70`).
