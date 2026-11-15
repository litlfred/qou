## Methodology generalisation

The proof transcribes verbatim to any closed braid $K \in B_n$ whose word factors as $\sigma_{i_1}^{k_1} \sigma_{i_2}^{k_2} \cdots$ with disjoint or commuting generator clusters. Each generator power $\sigma_i^{k}$ reduces via the recurrence $(a_k, b_k)$. We then read the resulting linear combination off the $H_n(q)$ basis. For non-disjoint clusters (e.g., neutron $\sigma_1^6 \sigma_2^4 \sigma_1^{-1}$ with mixed signatures), the same recurrence applies after using $\sigma_i^{-1} = \sigma_i - h$ from the Hecke quadratic.

## Categorical interpretation

This proposition provides the direct categorical-mass anchor for the proton. The formula $\mathrm{tr}_M(\sigma_1^7\sigma_2^4)(q)$ evaluates the Frobenius integral on $H_3(q)$ applied to the canonical atomic-braid representative of the proton's GB-filtration normal form ([`prop:atomic-mass-gb-nf`](#prop:atomic-mass-gb-nf)). The axiomatic derivation makes the construction independent of any representation-theoretic parameterisation.

The contrast with the q-Plancherel-measure trace closed form is strict. The q-Plancherel-measure trace behaves anti-self-reciprocally under $q \leftrightarrow 1/q$ ([`prop:markov-trace-antipode-polynomial-symmetry`](#prop:markov-trace-antipode-polynomial-symmetry)). This Markov-trace closed form does not. The two traces constitute genuinely different categorical objects. Both expand as finite linear combinations of irreducible characters, but they carry different weights ($w_\lambda$ Plancherel vs $y_\lambda$ Jones-Markov, [`prop:mass-coefficient-shadow-price`](#prop:mass-coefficient-shadow-price)).
