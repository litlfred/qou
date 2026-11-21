*Under the [pair Skein mass formula](#lem:pair-skein-mass-formula), write $\mathcal{S}_{ab} = (q\mu_a + q^{-1}\mu_b)/(q^{1/2} + q^{-1/2})$ and take the nucleon masses to be*

$$
  m_p = \mathcal{S}_{\mathfrak{u}\mathfrak{u}} + 2\,\mathcal{S}_{\mathfrak{u}\mathfrak{d}},
  \qquad
  m_n = 2\,\mathcal{S}_{\mathfrak{u}\mathfrak{d}} + \mathcal{S}_{\mathfrak{d}\mathfrak{d}},
$$

*where $\mu_{\mathfrak{u}}$ and $\mu_{\mathfrak{d}}$ are the dressed quark masses. Then:*

*(i) The splitting is exactly*

$$
  m_n - m_p = \frac{[2]_q}{q^{1/2} + q^{-1/2}}\,(\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}),
  \qquad [2]_q = q + q^{-1}.
$$

*(ii) The map $(\mu_{\mathfrak{u}}, \mu_{\mathfrak{d}}) \mapsto (m_p, m_n)$ is linear, and its determinant is $3\,[2]_q^2/(q^{1/2}+q^{-1/2})^2$. Whenever $[2]_q \neq 0$ it is invertible, so each pair $(m_p, m_n)$ comes from exactly one pair $(\mu_{\mathfrak{u}}, \mu_{\mathfrak{d}})$.*

**Scope.** Part (ii) means that reproducing the measured proton and neutron masses with this formula is a change of variables, not a prediction: the dressed quark masses can always be chosen to fit. The formula carries predictive content only if the dressed masses are fixed independently. The only such input on record is the ratio in [the substrate flavor split](#prop:flavor-split-substrate). That proposition's own proof calls the per-quark split a phenomenological ansatz chosen by its agreement with experiment, so it does not yet supply an independent input. Absolute masses in MeV are not predictions in any case: the electron mass fixes the MeV scale by definition.

**Convention.** The denominator $q^{1/2} + q^{-1/2}$ is the reciprocal of the excised convention-C Markov weight, so both parts hold in the convention-C frame, like the pair Skein formula itself. Re-deriving that formula under the canonical weight $z = q^3/(q^2+1)$ is open.
