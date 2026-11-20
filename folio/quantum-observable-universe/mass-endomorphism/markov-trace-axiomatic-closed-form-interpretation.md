## Methodology generalisation

The proof transcribes verbatim to any closed braid $K \in B_n$ whose word factors as $\sigma_{i_1}^{k_1} \sigma_{i_2}^{k_2} \cdots$ with disjoint or commuting generator clusters. Each generator power $\sigma_i^{k}$ reduces via the recurrence $(a_k, b_k)$. One then reads the resulting linear combination off the $H_n(q)$ basis. For non-disjoint clusters (e.g., neutron $\sigma_1^6 \sigma_2^4 \sigma_1^{-1}$ with mixed signatures), the same recurrence applies after using $\sigma_i^{-1} = \sigma_i - h$ from the Hecke quadratic.

## Categorical interpretation

This proposition provides the direct categorical-mass anchor for the proton. The formula $\mathrm{tr}_M(\sigma_1^7\sigma_2^4)(q)$ evaluates the Frobenius integral on $H_3(q)$ applied to the canonical atomic-braid representative of the proton's GB-filtration normal form ([Atomic mass as Markov trace of the Gröbner–Shirshov normal form](#prop:atomic-mass-gb-nf)). The axiomatic derivation makes the construction independent of any representation-theoretic parameterisation.

The contrast with the q-Plancherel-measure trace closed form is strict. The q-Plancherel-measure trace behaves anti-self-reciprocally under $q \leftrightarrow 1/q$ ([Antipode-induced polynomial symmetry $q^{20} p(1/q) = -p(q)$ of the proton Markov trace closed form](#prop:markov-trace-antipode-polynomial-symmetry)). This Markov-trace closed form does not. The two traces constitute genuinely different categorical objects. Both expand as finite linear combinations of irreducible characters, but they carry different weights ($w_\lambda$ Plancherel vs $y_\lambda$ Jones-Markov, [Mass-formula coefficients as shadow prices of the Frobenius positivity constraints](#prop:mass-coefficient-shadow-price)).

## Evaluation at $q_0$ and the comparison with measurement

Substituting $h = q - q^{-1}$ and $z = q^{3}/(q^{2}+1)$ into the closed form and evaluating at the substrate parameter $q_0$ gives

$$
  \mathrm{tr}_M(\sigma_1^7 \sigma_2^4)(q_0) \;\approx\; 1.884319\,467.
$$

The closed form is an identity in $\mathbb{Q}(q)$, so the only approximation in this line is the decimal evaluation of $q_0$. The seminormal route, with Hoefsmit representations and the Markov weights $y_\lambda$ solved from the same three axioms, reproduces this value to fourteen digits; that is the precision floor of the comparison, not a bound on the agreement.

**Comparison with measurement.** This is the only point where the block meets data. Dividing the CODATA ratio $m_p/m_e \approx 1836.15$ by the trace gives

$$
  \rho_p^{\mathrm{CODATA}}
   \;=\; \frac{m_p / m_e}{\bigl|\mathrm{tr}_M(\sigma_1^7\sigma_2^4)(q_0)\bigr|}
   \;\approx\; 974.44.
$$

$\rho_p^{\mathrm{CODATA}}$ is read off from the measured ratio. It is a calibration record, not a prediction, and nothing in the statement or the proof depends on it.
