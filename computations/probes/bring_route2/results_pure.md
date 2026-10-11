# Route 2, Part A of `preregistration-pure.md`: results

Recipe committed before the run (8a228b5c01). Producer: `pure_probe.py`. **3/3 checks pass.** Integer arithmetic is used for SL(2,ℤ); mpmath at 80 dps for lengths. No Q_β, CODATA or mass input. Nothing is ranked.

## 1. The γγ words now have a Bring loop, and it is well defined

The three placements of each pure braid (A1) **agree to 25 digits**. So the rule is not ambiguous for any γγ word, and none needed the "ambiguous" verdict.

| γγ word | SL(2,ℤ) trace | how placed | trace in Δ(2,4,5) (abs) | r | Bring loop L |
|---|---|---|---|---|---|
| (σ₀σ₁⁻¹)¹ | 3 | 3-cycle, via g³ | 5.2360679775 (= 3 + √5) | 5 | 16.16921667511886513803487 |
| (σ₀σ₁⁻¹)² | 7 | 3-cycle, via g³ | 25.416… | 5 | 32.33843335023773027606973 |
| **(σ₀σ₁⁻¹)³, the core** | 18 | pure, all three placements | 5.2360679775 (= 3 + √5) | 5 | **16.16921667511886513803487** |
| (σ₀σ₁⁻¹)⁴ | 47 | 3-cycle, via g³ | 643.99… | 5 | 64.67686670047546055213947 |
| (σ₀σ₁⁻¹)⁵ | 123 | 3-cycle, via g³ | 3244.1… | 1 | 16.16921667511886513803487 |
| (σ₀σ₁⁻¹)⁶ | 322 | pure, all three placements | 25.416… | 5 | 32.33843335023773027606973 |

Here r is the smallest power that closes on Bring's surface, and L = r · 2 arccosh(|tr|/2).

Two notes on reading the table:
- **(σ₀σ₁⁻¹)¹ and the core have the same value by construction.** A3 sends k = 1 to g³, which *is* the core.
- **(σ₀σ₁⁻¹)¹⁵, which is the k = 5 row via g³, traces the same closed geodesic as the core.** Its Δ(2,4,5) image is the 5th power of the core's, and since r drops from 5 to 1, it closes in one turn.

So the length is a property of the **closed loop on Bring**, not of the word: different powers can land on the same loop.

**Checks**
1. The 8 signed nucleon terms reproduce `results_signed.json` exactly. The rule does not change them, since each fixes exactly one point.
2. Every placement lies in Γ₀(2).
3. For k = 1, 2, 4, 5, the value via g³ equals the value computed directly on (σ₀σ₁⁻¹)^{3k}.

## 2. Side by side with the signed nucleon terms (data only, no ranking)

| element | Bring loop L |
|---|---|
| γγ core (σ₀σ₁⁻¹)³ | 16.1692 |
| proton terms σ₀^± σ₁^± | 9.2064, 15.9431, 6.3677, 20.4442 |
| neutron terms | 6.3677, 20.4442, 23.0159, no loop |

Adding the quark and gluon letters to the core moves the loop, in both directions, depending on the signs in the ud letters.

**Observation, not tested:** the core's length 16.16921667511886513803487 equals, to 25 digits, the length of one positive 11-letter braid in `results_rules11.json` (trace 22, period (1,2,2,2)). Whether that is the **same loop** (via the symmetry rule of `preregistration-sameloop.md`) was not checked.

## 3. What this changes

- The statement in `results_signed.md` §3, "route 2 cannot see γγ words", described the old rule. With Part A, every γγ word has a Bring loop, and the placement choice does not matter for them.
- **Part B (energy of the four-braid sum) is not computed.** It waits on the owner's choice among B1–B4. The default is B4: no energy for sums.
