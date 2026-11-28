**Conditional on [the aether flavor split conjecture](#conj:flavor-split-aether-mass).**

*Let $\mu \colon \mathbf{Flavor} \to \mathbb{R}_{>0}$ be the flavor dressing functor. Let $m_{\mathfrak{p}}, m_{\mathfrak{n}}$ be the nucleon masses, $M_N = (m_{\mathfrak{p}} + m_{\mathfrak{n}})/2$, and $q > 1$ the aether parameter. The down-up dressed mass splitting is exactly determined by the aether flavor formula:*

$$
  \mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}
  \;=\;
  M_N \cdot \frac{(q - 1)^2 (1 - q^{-4})}{3}
  \cdot
  \frac{q\,(q^{2} + 1)}{q^{4} + 1}
  \;+\;
  O\!\left(\bigl(\Delta m / M_N\bigr)^2\right).
$$

*Dropping the $O$ correction yields the leading-order aether-pure form:*

$$
  \mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}
  \;\approx\;
  \frac{M_N}{3} \cdot
  \hbar_q^2 \cdot h_q \cdot [2]_q \cdot
  \frac{1}{\kappa},
  \qquad
  \kappa = \frac{q^4 + 1}{q\,(q^2 + 1)}.
$$

The CODATA neutron-proton mass difference is no longer an input. The functor extracts the splitting purely from $q_0$ and the scale $M_N$. The individual masses $\mu_{\mathfrak{u}}$ and $\mu_{\mathfrak{d}}$ are then pinned by the baryon-content sum-rule.

Here $\kappa = \mathrm{tr}_M(\sigma + \sigma^{-1})$ at the canonical Markov parameter $z = q^3/(q^2+1)$ is the sum of the two crossing weights of the [pair Skein formula](#lem:pair-skein-mass-formula). It satisfies $q\,\kappa = \mathrm{tr}_M(\sigma^2)$, the Hopf-link trace, and $1/\kappa \le 1$ for $q > 0$.

**What is assumed and what is derived.** Two inputs are assumed. The first is [the aether flavor split conjecture](#conj:flavor-split-aether-mass), read at leading order as the equality $m_{\mathfrak{n}} - m_{\mathfrak{p}} = M_N (q-1)^2(1-q^{-4})/3$. The second is the nucleon form of the [pair Skein mass formula](#lem:pair-skein-mass-formula), $(m_{\mathfrak{n}} - m_{\mathfrak{p}})\,q(q^2 + 1) = (q^4 + 1)(\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}})$. This form is derived from the pair Skein formula when the proton and neutron masses are the sums of their pair masses ([nucleon map](#prop:terminal-resolution)). The $O\!\left((\Delta m / M_N)^2\right)$ correction is absorbed in these inputs. From them the leading-order splitting follows by dividing by $q^4 + 1 > 0$ and substituting. The conjecture is not proved. The leading-order equality is the strongest reading of the conjecture, and [the CODATA comparison](#rem:flavor-split-aether-codata-comparison) records that it is not met exactly at physical values, so the proposition is a statement about the model under that reading.
