# H16 result: the six-strand V³ word through the KL descent (2026-11-21)

Pre-registration: `h16_preregistration.md` (written before the run). Script: `h16_descent_v3_probe.py`; output: `h16_descent_v3_probe.out.txt`. Exact Laurent integers at generic v; the D values are mpmath at the proton q₀.

## Outcome: all three criteria behave as pre-registered

| | closed X_T | open X_B |
|---|---|---|
| ambient KL terms | 25 | 50 |
| terms with x ∉ W (swapped, dropped) | 20 | 40 |
| 1. Φ(X) ≡ Z mod 2, coefficientwise | **True** | **True** |
| 2. Φ(X) = Z | False (expected) | False (expected) |

3. Sanity in the H8 representation: bulk braid, wall quadratic and the type-B relation all hold. Then:

| word | D at q₀ | D at q → 1 |
|---|---|---|
| folded Z (Lusztig descent) | **0.94911520554914481986** | 0.99999933333455555315 |
| naive projection Φ(X) | 0.93900102455152553557 | 0.99999933333455555315 |

## What this shows

- **End to end.** The six-strand V³ word, folded by Lusztig's rule (§16.2, §16.7) and traced by the H8 functional, reproduces reading B (bulk q², wall q) to all 20 digits. H10b got that number from the B₃ word directly; H16 gets it starting from the ambient six-strand word.
- **The naive projection is a different object.** Dropping swapped KL terms without the twist gives D = 0.939001. It agrees with the descent only mod 2, and the two coincide at q → 1. So the choice of descent is visible at q₀ (a 1.07 % difference in D), and only Lusztig's twisted descent matches reading B.
- 80 % of the ambient KL terms are swapped pairs. They are what the descent removes.

## What this does not show

- D is a trace ratio, not a mass. No MeV map is used and there is no CODATA comparison.
- This verifies a necessary condition for conj:type-b-folding-cpt at n = 6. It does not prove the conjecture, and it does not fix the photon parameters or the shared λ.
- "Reading B" (fold the physical H_n(q), so v = q) remains the working reading; H16 tests consistency with it, not its correctness.
