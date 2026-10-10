# Results: route 2, braid word → Bring geodesic (lengths only)

Run: `python3 -u bring_route2_probe.py` → `results.json`, mpmath 80 dps, exit 0. All 7 checks pass.

| word | SL(2,ℤ) trace | Δ(2,4,5) image | \|tr\| in Δ | r (order in S₅) | Bring length |
|---|---|---|---|---|---|
| nuc9 | 0 | elliptic, order 2 | 0 | 2 | none |
| nuc11_interleaved = gluon_s0_s0 | 2 | elliptic, order 5 (cusp → cone point) | φ = 2cos(π/5) | 5 | none |
| gluon_s0_s1 | 2 | elliptic, order 5 | φ | 5 | none |
| gluon_s1_s0 | 4 | hyperbolic | φ² | 3 | 3·2 arccosh(φ²/2) = 4.6031833095… |
| gluon_s1_s1 | 4 | hyperbolic | φ² | 3 | 4.6031833095… |
| nuc11_gen_grouped | −26 | hyperbolic | 2φ | 3 | 3·2 arccosh(φ) = 6.3676503714… |

The \|tr\| values were recognised by eye as elements of ℤ[φ]. They agree to 80 dps (`results.json`), but this was not proved.

## Facts
- **Two choices that could have mattered do not.** r computed through the S₅ image is the same for all 5 admissible epimorphisms Δ(2,4,5) → S₅. It also equals r from the choice-free congruence test g^r ∈ H₄(5) (Kattan–Singerman (3.1)), done in exact arithmetic.
- **Conjugate pairs agree, as pre-registered.**
- **The γγ core is invisible.** Δ² = (σ₀σ₁)³ ↦ −I, so route 2 sees only the quark and gluon letters. Those are exactly the 5 letters that the 2026-09-13 ruling left unselected.
- **Domain split.** nuc9 lands on the order-2 cone point and class B (which contains the scored element) on the order-5 cone point, the image of the cusp. Neither has a closed geodesic on Bring. Class A and gen_grouped do.

## Not claimed
- **No word is selected.** These are lengths, not an energy (preregistration §2).
- **The domain split decides any "shortest curve" rule, so it is the owner's call.** If a cone-point image counts as length 0, class B "wins". If it counts as undefined, class A is the shortest candidate.

## POST-HOC
- The pre-registered conjugate-pair check first compared *signed* traces. The two class-A words differ by sign (−φ² vs +φ²), which is the same element of PSL(2,ℝ). The check was corrected to compare \|tr\|, which is what the pre-registration meant ("identical outputs" of a PSL quantity). No other change was made.
