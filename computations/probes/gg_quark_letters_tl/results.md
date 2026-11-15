# Quark letters and γγ words in the Jones (Temperley–Lieb) basis: results

Recipe: `preregistration.md` (`59fcf0d0594`), committed before computing. Producer: `gg_quark_letters_tl_probe.py`. Witness: `gg-quark-letters-tl.witness.json`. Exact over ℚ(q). Issue #7777, bean `qou-ales`. Nothing adopted, nothing compared with data.

**3/3 checks pass.**
- **T1:** the Hecke and braid relations hold in TL₃, and e_i is an idempotent with e₀e₁e₀ = [2]⁻²e₀ in the two-row representation.
- **T2:** bar fixes e_i, i.e. q⁻¹ − σ_i⁻¹ = [2]e_i. The first run reported a fail, but that was a comparison bug in the check: it compared two different symbolic spellings of [2]_q, `q + 1/q` and `(q²+1)/q`. The comparison now subtracts exactly and tests for zero. The identity itself is exact.
- **T3:** for all 8 templates and both nucleons, χ_(3) and χ_(2,1) reproduce #7718's committed exact rational functions. So the map H₃ → TL₃ is the one #7718 used.

## 1. Where flavour sits in a letter: outcome (i)

In the basis {1, e₀, e₁, e₀e₁, e₁e₀}, every template letter on generator g is

    L = c · 1 − [2]_q · e_g,

with **the same cap–cup coefficient −[2]_q for every flavour and every pair rule**. Only the through-strand coefficient c changes:

| letter | c |
|---|---|
| σ (u under S+, d under S−) | q |
| σ⁻¹ (d under S+, u under S−) | q⁻¹ |
| ½(σ + σ⁻¹), the averaged ud | [2]_q / 2 |

So in the Jones picture **flavour is a bar-parity datum on the through-strand** (q versus q⁻¹, swapped by the bar involution, which fixes e). The pair content (the cap–cup, i.e. pair creation then annihilation) is **flavour-blind**. The u ↔ d swap S+ ↔ S− is exactly the bar involution on through coefficients.

## 2. The γγ vertex and the core

    V = σ₀σ₁⁻¹ = 1 − [2]q⁻¹·e₀ − [2]q·e₁ + [2]²·e₀e₁.

- The through coefficient is q·q⁻¹ = 1: the vertex's two crossings carry opposite through-parities, one of each.
- Each cap–cup is weighted by the through coefficient of the **other** crossing: e₀, on the positive crossing's generator, by q⁻¹; e₁ by q. At q = 1 both are −2, so the asymmetry is entirely in that q versus q⁻¹ weighting.
- **V³** has through coefficient exactly 1, and all its pair content is O(t²) (t = q − 1) and **odd under the flip**: e₀e₁ ↔ e₁e₀ is ±16t², and e₀ ↔ e₁ is ±16t³. This is #7760's result (V³ − 1 = h²(T_{s₀s₁} − T_{s₁s₀}) + h³(σ₁ − σ₀) + …), rewritten in the Jones basis.
- **U³** = (σ₀σ₁)³ has flip-symmetric pair content at t¹.

## 3. S+ versus S− on the builder nucleons (AVG, k = 0)

Leading order in t of the difference S+AVG − S−AVG, per basis element:

| | 1 | e₀ | e₁ | e₀e₁ | e₁e₀ |
|---|---|---|---|---|---|
| proton | 2t | −4t | −4t | 8t | 32t³ |
| neutron | −2t | −32t⁴ | 32t⁴ | −32t³ | 32t³ |

- **Neutron:** at first order the S± difference is **purely a through-strand difference**. Its pair content differs only at t³ and t⁴, in the flip-odd pattern of the core.
- **Proton:** the S± difference also reaches the pair content at t¹, but **flip-symmetrically** (e₀ and e₁ change equally).
- This is where #7718's reading-3 verdict is decided (at t¹). For the neutron it rests on the through-strand parity alone.

## 4. What this says, and does not say

- **Established (exact):** in the Jones basis, quark flavour in the template is the bar parity of the through-strand coefficient. Pair creation and annihilation carry none of it. The γγ vertex is one crossing of each through-parity, and it cross-weights its two cap–cups.
- **What a derivation would have to supply:** a rule fixing the through coefficient of each produced quark line, q or q⁻¹, from the γγ construction. In this basis that is the whole sign map. The pair (cap–cup) structure cannot supply it, because it is flavour-blind.
- **Not established:** the sign map or the placement. The S± choice stays open (`qou-y2np`, `qou-99qc`); owner option 4 stands.
