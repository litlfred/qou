# Route 2, option 1: results (ropelength Λ = L/τ on fresh words)

> **🛑 CORRECTION 2026-10-11 (`results_signed.md`).** The seen candidates in this file are the generator sequences of `qbeta_candidate_closures_are_links_probe.CANDIDATES`, with the signs erased. The scored nucleon has σ₁⁻¹ in its core and averaged ud letters; it is a sum of four braids. Every statement here about the *seen candidates* is withdrawn. The statements about fresh positive words stand.


Recipe: `preregistration-option1.md`, committed before computing (67fee1b20b).
Producer: `option1_ropelength_probe.py`, mpmath at 30 dps. All 67 checks pass:
- the class count is 94;
- route 2's lengths are reproduced to 25 digits;
- every τ carries a certified search radius.

## Verdict (by the pre-registered rule): Λ FAILS. L FAILS.

There are 89 fresh classes. Of these, 37 carry a loop and 52 do not. No loop crosses itself.

| Λ | how many fresh classes |
|---|---|
| 2.518874849922577404841967 | 24 |
| 2.764248904337735719648352 | 8 |
| not enumerated | 5 |

The 5 non-enumerated loops have a rigorous lower bound above the minimum, from the collar-area bound 2L·sinh τ ≤ 12π.

The minimum is attained by 24 classes. Their SL(2,ℤ) images fall into **2** distinct GL(2,ℤ) conjugacy classes:
- 23 lie in the class of trace 4, continued-fraction period (1, 2);
- 1 (σ₀⁹σ₁²) lies in the class of trace 16, period (2, 7).

Under §4, a tie across distinct GL(2,ℤ) classes is a genuine tie, so **Λ does not discriminate** (scope (a): this energy, alone, on this set). Under §5, it is therefore **not** applied to the already-seen words.

The bare length L fails the same way. L = 4.6031833095… is attained by the same 24 classes, in the same 2 GL(2,ℤ) classes.

## Observations (post-hoc; not part of the verdict)

- **The minimising loop is class A's loop.** Class A (gluon_s1_s0 / gluon_s1_s1) has an SL(2,ℤ) image of trace 4 with period (1, 2). That is the class of 23 of the 24 minimisers, and its length 4.6031833095… matches. So the fresh test mostly rediscovers the class-A loop. Since class A is a seen word, this is CONTAMINATED and carries no evidential weight.
- **The GL(2,ℤ) test is sufficient for "same loop", not necessary.** The map from words to Bring is not injective on conjugacy classes. The trace-16 word may well reach the same closed geodesic, or an isometric copy of it under Bring's 120 symmetries, since Λ and L agree to 25 digits. Deciding that would need conjugacy of the loop elements inside π₁(Bring), which was not pre-registered. Doing it now could flip the verdict to "pass" with the class-A loop as the unique minimiser. **That would be POST-HOC and is not done here.**
