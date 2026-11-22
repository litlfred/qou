# Result: E₀'s weight ℏ_q/q² is not any of the six pre-registered Markov traces (2026-11-22)

Prereg: `PREREGISTRATION.md` (commit 89dc8589e37). Probe: `e0_weight_markov_probe.py`, exact over
ℚ(q); output `result.txt`. The trace is checked to be convention D (tr(σ) = q³/(q²+1)).

| candidate | value | vs w = (q−1)/q³ |
|---|---|---|
| C1 tr(σ⁻¹), n=2 | 1/(q(q²+1)) | no |
| C2 y_(2), n=2 | (q²−q+1)(q²+q+1)/(q²+1)² | no |
| C2 y_(1,1), n=2 | q²/(q²+1)² | no |
| C3 tr(σ₀σ₁σ₀), n=3 | q³(q⁴+1)/(q²+1)² | no |
| C3 tr((σ₀σ₁σ₀)⁻¹), n=3 | (q⁴+1)/(q³(q²+1)²) | no |
| C4 tr(σ₀σ₁⁻¹), n=3 | q²/(q²+1)² | no |
| C4 tr((σ₀σ₁⁻¹)³), n=3 | −(q¹²−3q¹⁰+2q⁸−4q⁶+2q⁴−3q²+1)/(q⁴(q²+1)²) | no |

No exact match and no monomial near-match. C5 (dividing by ℏ_q² and testing against 1/(q(q−1)))
is the same test as the first, since w/ℏ_q² = 1/(q(q−1)); the prereg listed it separately by
mistake, and it adds nothing.

**Verdict: scope (a).** None of these six convention-D traces is E₀'s weight. The weight stays open.

**Why single words look unlikely (an argument, not proved in Lean here).** At q = 1 the Jimbo Ř
becomes the swap and K = 1, so the trace of any braid word β ∈ B_n is 2^{c(β)−n} > 0, with c the
number of cycles of its permutation. The weight w = (q−1)/q³ vanishes at q = 1. So w cannot be the
trace of a single braid word. It could still be a signed combination, as σ − σ⁻¹ = h is, or a tower
sum: 1/(q(q−1)) = Σ_{k≥2} q⁻ᵏ. Those were not tested, and testing words or combinations until one
matches would be selection against the target.
