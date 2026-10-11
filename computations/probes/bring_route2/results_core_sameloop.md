# Route 2: the γγ core and the braid 00001100011 trace the same Bring loop

Producer: `core_sameloop_probe.py`. It applies the same-loop rule of `preregistration-sameloop.md` §2 (`sameloop_probe.isometric`) unchanged. It uses no energy, makes no selection, and takes no Q_β, CODATA or mass input.

## Result

The reference is the core (σ₀σ₁⁻¹)³ placed at ∞.

| compared with core@∞ | L | same loop? | orientation |
|---|---|---|---|
| core placed at 0 | 16.16921667511886513803487 | **yes** | + |
| core placed at 1 | 16.16921667511886513803487 | **yes** | + |
| positive word 00001100011 (σ₀σ₀σ₀σ₀σ₁σ₁σ₀σ₀σ₀σ₁σ₁) | 16.16921667511886513803487 | **yes** | + |

So:
1. The three placements of the core give **one** closed geodesic on Bring's surface, not merely three geodesics of equal length. This closes the remaining ambiguity of the pure-braid rule (A1) for the core.
2. The equal-length coincidence noted in `results_pure.md` §2 is a **genuine** coincidence of loops, not just of lengths.

## What it does NOT mean

The two braids are **not** related as braids. The exponent sum (number of σ letters minus number of σ⁻¹ letters) is a conjugacy invariant of B₃: it is 0 for the core and 11 for 00001100011. So the two braids are not conjugate, and they do not even have the same closure.

The route-2 map B₃ → SL(2,ℤ) → Δ(2,4,5) → Bring therefore **identifies non-conjugate braids**. This is expected, since the map factors through a quotient. But it means that "same Bring loop" is a statement about the images, and carries no information about the knot or link.

This is a further limit on route 2 as a *selection* tool, on top of the sign-erasure correction (`results_signed.md`). Two words that the γγ rule treats very differently (one is a γγ word, the other is not) are indistinguishable to route 2.
