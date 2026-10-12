# What PR #7733 measured, and what it implies

Owner request on #7733, 2026-10-12: *"Please provide here a better explanation of the what you just measured and the implications of it. Please provide both a physical and mathematical context."*

Register (AGENTS.md, "the paper is a mathematical model"): everything below is a statement about model objects. "Collision", "colour" and "confined" are names for constructions in H_n(q). Nothing here is compared with data, and nothing is selected.

## 1. The question in one paragraph

A γγ collision is modelled as one vertex V = σ_iσ_{i+1}⁻¹ acting on three adjacent strands. Stacking three vertices on the **same** three strands gives V³, the nucleon core, and that element passes reading 3 (the ruled confinement test). #7733 asked what happens if each successive collision lands on **new** strands, so that the element climbs the strand count H₃ → H₅ → H₇ → H₉ the way a production cascade would. The extra strands are then closed, and reading 3 is tested at every level, as the owner ruled.

**Answer:** no climbing placement passes, for either vertex, up to 9 strands. Only same-strand collisions pass, at k = 3 and k = 6. The reason is visible already at q = 1, before any deformation, and it is short. Section 3 gives it.

## 2. Mathematical context

**The algebra.** H_n(q) is the Iwahori–Hecke algebra of the braid group B_n. Its generators satisfy σ² = hσ + 1 with h = q − q⁻¹, so σ⁻¹ = σ − h. At q = 1 it is the group algebra of the symmetric group S_n, and σ_i becomes the transposition (i, i+1).

**The trace and its weights.** Convention D fixes the Markov parameter z = q³/(q²+1). Its weights y_λ vanish on every partition with three or more rows, and on two-row shapes they are

    y_(a,b) = [a − b + 1]_q / [2]_q^n.

So the trace sees only the SU(2) part of H_n: two-row λ ↔ spin (a − b)/2 (Schur–Weyl duality with U_q(sl₂) on n copies of the spin-½ representation). At q = 1 the trace is exactly the normalised trace of S_n permuting the factors of (ℚ²)^{⊗n}.

**Closing a strand.** The Markov conditional expectation E: H_{m+1} → H_m is E(a) = a and E(aσ_m b) = z·ab. At q = 1 it is the normalised **partial trace over one qubit**. On a permutation π it acts by a simple rule:

- if the closed strand is fixed by π, then E(π) = π;
- otherwise E(π) = ½·π̂, where π̂ is π with that point cut out of its cycle.

Iterating, closing n − 3 strands sends π to 2^{−c}·π̂ with π̂ ∈ S₃.

**Reading 3 at level 3.** On H₃ the test is χ_(3) ≥ 0 and χ_(2,1) ≥ 0, where (3) is spin 3/2 and (2,1) is spin ½. At q = 1 on S₃, χ_(2,1) takes the value 2 on the identity, 0 on a transposition and −1 on a 3-cycle. So:

> **At q = 1, reading 3 at level 3 fails exactly when the closed-down permutation is a 3-cycle.**

This is the whole mechanism of the negative result.

## 3. Why climbing fails, at q = 1, for every k

Each vertex V_i at q = 1 is the 3-cycle (i, i+1, i+2). The cycle type of the product depends only on how consecutive vertices overlap. Measured for every row of #7733, and it holds for all k by the same argument:

| shift s | how consecutive collisions overlap | cycle type of W at q = 1 | after closing down to 3 strands | χ_(2,1) at q = 1 |
|---|---|---|---|---|
| 0 | all on the same 3 strands | identity if 3 ∣ k, otherwise a 3-cycle | the same | 2 or −1 |
| ±2 | share one strand | one (2k+1)-cycle | one 3-cycle | −4^{−(k−1)} |
| +3 | disjoint | k separate 3-cycles | one 3-cycle (the others close to ¼ each) | −4^{−(k−1)} |
| −1 | share two strands | k odd: one (k+2)-cycle; k even: two (k+2)/2-cycles | k odd: a 3-cycle; k even: a transposition | k odd: −2^{−(k−1)}; k even: 0 |
| +1 | share two strands, telescopes | σ₀σ_k⁻¹: two transpositions | a transposition | 0 |

**The one-line reason.** Same-strand collisions compose 3-cycles **on the same three points**, so three of them cancel to the identity. Climbing collisions chain 3-cycles through shared points into **one long cycle**, or leave them disjoint. Closing strands cannot break a cycle apart; it can only shorten it. So a single cycle always survives to level 3 as one 3-cycle, and that has χ_(2,1) < 0.

**What the deformation does.** For s = −1, ±2 and +3 the exact rational function χ_(2,1)(q) has no root on (1, ∞) (#7733 §5). So the q = 1 sign persists for every q > 1, and at q₀ the values are −0.258, −0.0638, −0.0158 for k = 3, 5, 7 at s = −1 (and the same at s = ±2 for the matching n). The deformation shrinks the defect; it never cancels it.

**The two marginal cases.**
- For s = +1, and for s = −1 with k even, the residual at q = 1 is a transposition, so χ_(2,1) = 0. The sign is then decided at order t¹ (t = q − 1).
- For V with s = +1, k ≥ 4, that sign is positive at every level, so these rows formally pass.
- But s = +1 telescopes in the braid group to σ₀σ_k⁻¹ (Lean, `GammaGammaStaircaseTelescopes.lean`). That is two crossings at opposite ends: one isolated photon line, not a collision cascade.
- For V with s = −1, k even, the closed-down element passes at level 3 (χ_(2,1)(q₀) = +0.0209, +0.0052 at k = 4, 6) but fails at a higher level. (For U it already fails at level 3.) That is the "every level" ruling catching what the bottom level misses.

## 4. Physical context (interpretive)

Read the strands as colour lines and V as one γγ → qq̄ event that cyclically permutes three colour lines. At q = 1 (order zero in h, the classical skeleton of the tower) that permutation is a 120° colour rotation.

- **Same strands.** Three rotations on the same three lines make a full 360° turn, and the colour flow closes on itself. That is the k = 3 nucleon core, and it is the only colour-neutral outcome. Reading 3 passes (χ_(2,1) = 2 at q = 1), and the q-deformation first moves it only at order h⁴.
- **Climbing.** If each new event uses fresh lines, the rotations never act on the same triple twice. Tracing out the lines that leave the region (closing strands is a trace over what is not observed) leaves **one uncancelled 120° rotation** on the three lines that remain. A net colour rotation is not colour-neutral, and reading 3 says so with χ_(2,1) < 0. That is already true at q = 1, so it is a statement about the permutation skeleton, not about the deformation.
- **Disjoint events (s = +3).** These are independent. The closure of independent pieces is multiplicative (the corpus's connected-sum statement, `canonical-trace-factorises-over-chain`). Each extra event closes to the positive factor ¼, and the one left over is a single isolated vertex, which on its own is not confined.

**Implication for the programme (my reading, not a ruled result).** Within rigid-shift placement, climbing the strand count does not manufacture confinement. Confinement in this model is a same-strand phenomenon: colour must close on the triple that carries it. So the nucleon tower is built by composing confined triples (as in #7702's H₃ → H₆ → H₉ free products), not by letting single collisions walk up the strands. This is scope (a): it concerns this placement family under this closure. Other closures are the subject of `closures_preregistration.md` and are reported in `closures_results.md`.

## 5. What is and is not established

- **Exact, measured (#7733, 5/5 checks):** the verdict table for s ∈ {0, ±1, ±2, +3}, n ≤ 9, both vertices, top closing.
- **Elementary, for all k (proof in §3, prose only, not Lean):** at q = 1, rigid shifts with |s| ≥ 2 close to a single 3-cycle, so χ_(2,1) < 0. For q > 1 the sign is established only for n ≤ 9, by the exact rational functions.
- **Not established:** non-rigid placements; quark letters; two nucleons. The closure dependence is in `closures_results.md`.
