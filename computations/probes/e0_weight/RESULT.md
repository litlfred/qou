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

---

# Addendum 1 result: tower-level objects (prereg commit 622bdfe7ae1)

**Verdict: none of the four preregistered tower candidates equals w = ℏ_q/q². No derivation.**
Exact arithmetic in ℚ(q) (`e0_weight_tower_probe.py`, output in `e0_weight_tower_probe_result.txt`).

The invariant is ord₁, the order of vanishing at q = 1. For the target, ord₁(w) = 1, with leading coefficient w/(q−1) → 1.

| candidate | ord₁ | verdict |
|---|---|---|
| T1 brane tower: (ℏ_q²λ)ⁿ, Σ, 1/(1−ℏ_q²) − 1 | 2n, 2, 2 | excluded, order ≥ 2 |
| T2 Markov stabilisation: z_Dⁿ, z_D/(1−z_D) | 0 | excluded, value at 1 is non-zero |
| T3 levels and partial sums of Σ_{k≥2} q⁻ᵏ | 0 (full sum: −1) | excluded |
| T4 skein difference h·τ(β) | 1, coefficient 2·2^{c−n} | first-order match iff c = n − 1. Never equal: it would need τ(β) = 1/(q²(q+1)), which has a pole at q = −1, while every word trace is finite there |

**Lean.** `QOU/QBeta/E0WeightAllWords.lean`, all sorry-free on the standard axioms:
- `traceD_ne_weight`: every single word, any number of strands.
- `ne_weight_of_tendsto_ne_zero`: covers T2 and T3.
- `hbar_sq_mul_ne_weight`: covers T1, for any λ finite at q = 1.
- `skein_first_order`: the T4 coefficient.

**Not in Lean.** The T4 exact exclusion is a rational-function argument; it needs the numerator as a Laurent polynomial.

**Scope.**
- T1, T2, T3 and the single-word result are scope-(b) exclusions. The invariant is the order of vanishing at q = 1, and it is proved.
- T4 is scope-(a) as computed, with a hand proof of the exact exclusion.
- What the measurement leaves: w agrees to first order with the skein difference of a word whose closure has n − 1 components (for example h·z_D). The closest canonical tower operation is therefore σ − σ⁻¹ = h, and the missing piece is a factor that is 1/2 at q = 1 and is not a single trace. Free linear combinations of traces were not searched, by design: over ℤ[q^±] the combination w·τ(1) already equals w, so solving for coefficients would be fitting.

---

# Addendum 2 result: the exact factor beyond h/2 (prereg commit f27ce7f9483)

**Verdict: no derivation. Neither preregistered route equals w = ℏ_q/q².** Both predictions stated in
the prereg hold. Exact ℚ(q) (`e0_weight_framed_link_probe.py`, output in `..._result.txt`).

| route | object | ord₁ | leading coeff | verdict |
|---|---|---|---|---|
| R2 | 3₁ excess, ratio / difference | 2 | — | excluded (order) |
| R2 | 4₁ (muon knot) excess, ratio / difference | 2 | — | excluded (order) |
| R3 | Hopf⁺ excess, ratio / difference | 1 | −3 / −12 | excluded (coefficient) |
| R3 | Hopf⁻ excess, ratio / difference | 1 | +3 / +12 | excluded (coefficient) |
| R3 | electron σ₁σ₂σ₁ closure (= Hopf⁺) | 1 | −3 / −12 | excluded (coefficient) |

Closed form: Hopf⁺ ratio − 1 = −q⁻²·h·[3]/[2]. That is the same q⁻² framing as w, times a
skein difference h, times a loop ratio [3]/[2] that is 3/2 at q = 1. The 4₁ excess is
(q⁶ − 1)(q² − 1)/q⁴, of second order, as predicted for every knot.

**What the result fixes.**
1. Read as a link invariant, the "h/2" of Addendum 1 is a linking-number effect. It appears only
   for linked pairs, and there with coefficient proportional to lk times 3/2, not 1/2.
2. A knot excess, including the muon knot's, can never supply w: it is second order at q = 1.
3. The q⁻² in w does have a framed counterpart, the q^{−2·wr} framing at writhe 1. The remaining
   factor is ℏ_q = 1 − q⁻¹, which is h/(1 + q). That is a one-sided deficit, not a symmetric
   skein difference. No canonical Hecke or link object tested so far produces 1/(1 + q).

**Not done, by the prereg rule:** rescaling, extra powers of q, and combinations of routes.
The match q⁻²·(something) is suggestive. But choosing the something to equal ℏ_q is exactly the
step that would be a fit.
