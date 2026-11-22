# H17 result: the descent at n = 4 and n = 5 (2026-11-21)

Pre-registration: `h17_preregistration.md`. Script: `h17_descent_n45_probe.py`; output: `h17_descent_n45_probe.out.txt`. The KL computations are exact Laurent integers. The traces are evaluated at the proton q₀.

One fix was made after the first run, a bookkeeping bug only: the reduced-word search used the weighted length as a step count and crashed at n = 4. It now takes the first visit in a breadth-first search over the folded generators. No criterion or word changed.

## Outcome: the pass/fail criterion passes at both n

| | n = 4 | n = 5 |
|---|---|---|
| folded group, weights (b, w) | B₂, (2, 1) | B₂, (2, 3) |
| ambient KL terms of X | 24 | 120 (all of S₅) |
| swapped, dropped by Φ | 16 | 112 |
| 1. Φ(X) ≡ Z mod 2 | **True** | **True** |
| 2. Φ(X) = Z | False | False |

So the weight-3 wall that the wording fix added behaves exactly like the weight-1 wall under the descent. On the chiral cube (T_b T_w⁻¹)³, Lusztig's descent and the naive projection agree mod 2 and differ as Laurent polynomials. This is the same pattern H16 found at n = 6.

## Criterion 3: the two-strand model cannot see the wall weight

The bulk quadratic, the wall quadratic and the B₂ relation 𝒦Ř𝒦Ř = Ř𝒦Ř𝒦 all hold at L = 1 and at L = 3. A follow-up check shows the B₂ relation holds for **every** wall parameter s, symbolically. The model therefore accepts a weight-3 wall, but it cannot single one out. Its traces are reported in the output file and are not interpreted. Two strands carry no n/p split, so no D was formed.

At q₀ the folded and naive words give clearly different traces. At n = 5, for example, the weight-2 trace is −0.210 for Z and +2.431 for Φ(X). As in H16, the choice of descent is visible at q₀.

## What this does not show

- The word is a stand-in. B₂ has only one bulk generator, so the photon vertex σ₀σ₁⁻¹ has no counterpart at n = 4 or 5.
- Passing criterion 1 is necessary, not sufficient. It does not prove conj:type-b-folding-cpt.
- No number here is compared with experiment.
