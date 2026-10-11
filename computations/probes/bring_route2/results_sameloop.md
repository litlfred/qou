# Route 2, option 1b: results

Recipe: `preregistration-sameloop.md`, written before this run. mpmath 30 dps, no float64. Producer: `sameloop_probe.py`. **203/203 checks pass.** No Q_β, CODATA or mass input.

## Verdict by the pre-registered test: PASS, and it means less than it sounds

The smallest ropelength, Λ = 2.518874849922577404841967, is attained by **exactly one loop on Bring's surface, up to symmetry**. The bare length L also passes. By the letter of §5, Λ discriminates.

The reason it passes is what matters:

- The 316 fresh 13-letter classes give **194 loops**, and 122 give no loop.
- Those 194 loops are only **10 distinct closed geodesics** on Bring's surface, up to symmetry.
- Inside every group of equal length, every loop is the image of every other under a symmetry of the surface. No equal-length pair failed to match. So, on this set, "same length" and "same loop" coincide.
- Λ and L therefore order the same 10 geodesics. The shortest one also has the smallest Λ.

**The word → loop map is far from one-to-one.** The minimising loop is shared by **90 of the 194** loop-carrying word classes. So Λ selects a **loop**, not a **word**. Any rule that ranks words through their Bring loop inherits a 90-way tie at the top.

## The minimising loop is class A's loop (contaminated, as §0 warned)

The minimiser has L = 4.603183309507916659974173. This is exactly the Bring length of the already-seen class A. The post-hoc regrouping (§6.4, not part of the verdict) puts all 24 of option 1's 11-letter minimisers into **one** symmetry class. Option 1's two GL(2,ℤ) classes were therefore the same loop on the surface, and its "fail" was the symmetry tie that §0 predicted.

## Table (one row per symmetry class)

| L | word classes on it | Λ |
|---|---|---|
| 4.603183309507916659974173 | 90 | **2.518874849922577404841967** |
| 4.795655030616652975799161 | 46 | 2.764248904337735719648352 |
| 6.367650371430213912198113 (gen_grouped's length) | 10 | skipped, collar bound 3.526 |
| 6.94638431969059729373808 | 20 | skipped, bound 4.030 |
| 9.20636661901583… | 10 | skipped, bound 6.286 |
| 11.4170840664345… | 4 | skipped, bound 8.950 |
| 16.1692166751188… | 10 | skipped, bound 16.27 |
| 20.4441602226000… | 2 | skipped, bound 24.78 |
| 23.015916547… | 1 | skipped, bound 30.79 |
| 23.978275153… | 1 | skipped, bound 33.22 |

A class is "skipped" when the rigorous bound Λ ≥ L / asinh(6π/L) already exceeds the computed minimum, so it cannot be the minimiser (§4).

## Checks

1. The class count is 316, by brute force over all 8192 words.
2. Route 2's L is reproduced for class A and gen_grouped to 25 digits.
3. Every loop is found isometric to itself.
4. The post-hoc option 1 regrouping is consistent with `results_option1.json`.
5. **τ invariance:** a second member of the 90-class gives τ = 1.82747598978544, the same to 25 digits.
6. All arithmetic is mpmath; each τ carries its radius certificate.

**Independent cross-check, not pre-registered.** For each of the 184 matches found, I conjugated the first loop's deck element by the matching symmetry. In every case it equals the second loop's deck element, up to sign and inverse. The matches split as 172 orientation-preserving and 12 orientation-reversing. There were 0 failures.

## What this says (scope)

- **(a) Scope-limited negative for word selection.** Ropelength on Bring's surface, with the symmetry rule, does rank loops. But route 2's map sends many words to one loop, so it cannot pick a single braid word: 90 tie at the top.
- **Selected: nothing.**
- **Not established:** whether a finer invariant of the word survives the map, such as the r-fold covering degree or the position of the loop's lift. That would be a new energy, and needs its own pre-registration.
