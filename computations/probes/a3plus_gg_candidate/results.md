# Results: A≥3 chain on the #7741 γγ candidate word

Pre-registration: [`preregistration.md`](preregistration.md), commit `721a0b8bcd`, pushed before
computing. Producer `a3plus_gg_candidate_probe.py`, witness `a3plus-gg-candidate.witness.json`
(1/1 check). χ^λ at 50 dps, convention D, proton q₀. 1845 s, of which 4He is 398 s (free, 24 letters),
731 s (arm L, 42 letters) and about 714 s (arm R, by subtraction).

**Comparison arm. Adopts nothing.** The candidate word is not ruled (#7876).

## Volume-scaled |rel_err| against AME 2020

Production = the committed Borromean-word chain (`binding-a3plus-full-theta-assembly`, PR #8697).

| ρ | column | D | T | ³He | ⁴He |
|---|---|---|---|---|---|
| μ₀ | production | 19.6 % | 82.1 % | 78.5 % | 93.3 % |
| μ₀ | γγ arm L | 90.8 % | 95.5 % | 95.7 % | 97.0 % |
| μ₀ | γγ arm R | 90.8 % | 95.5 % | 95.7 % | 97.0 % |
| m_e | production | 74.8 % | 94.4 % | 93.3 % | 97.9 % |
| m_e | γγ arms | 97.1 % | 98.6 % | 98.6 % | 99.0 % |

The ħ_q-scaled ρ candidates are above 97 % in every column. All errors are under-predictions:
B_pred(μ₀) on the γγ word is 0.205 / 0.380 / 0.336 / 0.861 MeV against AME 2.22 / 8.48 / 7.72 /
28.30 MeV.

## Σ y·dim·|Δθ|

| | D | T | ³He | ⁴He |
|---|---|---|---|---|
| production | 0.14973 | 0.11255 | 0.13900 | 0.078833 |
| γγ arm L | 0.017164 | 0.028115 | 0.028115 | 0.036052 |
| γγ arm R | 0.017164 | 0.028117 | 0.028117 | 0.036053 |

The γγ bond moves the per-block Reeb phases about a tenth as much as the production interface
letters do. T and ³He coincide because p and n are the same word on this candidate; only their AME
targets differ.

## The two site arms agree

L and R differ at the 10⁻⁴ level in Σ|Δθ|, and D is identical in both. So the
bond-site ambiguity left open by #7741 does not move these numbers.

## What this does and does not say

- Scope (a): this chain (Reeb phase sum × ρ × production Vol(K_bind)), this candidate word, the
  four light atoms. It is not a statement about the γγ word in general.
- The chain's Vol(K_bind) and y_λ are the production ones; neither was derived for this word. A
  γγ redo would need both.
- On this chain, with these inputs, the candidate word does not bring the four atoms closer to AME
  than the production word; it is further away for every atom and every ρ.
- Nothing here is a reason to prefer either word. Choosing a word because its numbers are closer
  would be selection against the target.
