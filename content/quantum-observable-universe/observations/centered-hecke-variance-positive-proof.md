*Proof.* Apply the Hecke quadratic relation $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$ and the Markov property:

$$
  \mathrm{tr}_M(\sigma_i^2)
  = (q - q^{-1}) \mathrm{tr}_M(\sigma_i) + 1
  = (q - q^{-1}) z + 1.
$$

Hence

$$
  \mathrm{tr}_M(\tilde\sigma_i^2)
  =
  \mathrm{tr}_M(\sigma_i^2 - 2 z \sigma_i + z^2)
  =
  (q - q^{-1}) z + 1 - 2 z^2 + z^2
  =
  (q - q^{-1}) z + 1 - z^2.
$$

This is the variance.

**Positivity.** In the Wenzl regime $q^{1/2}+q^{-1/2} > 2$, let $u = q^{1/2}$. The Markov parameter is $z = 1/(u + u^{-1})$. Compute:

$$
  z^2 = \frac{1}{(u + u^{-1})^2}
       = \frac{1}{u^2 + 2 + u^{-2}}
       = \frac{1}{q + 2 + q^{-1}}.
$$

The Wenzl bound $u + u^{-1} > 2$ yields $(u + u^{-1})^2 > 4$, thus $z^2 < 1/4$.

Additionally, $(q - q^{-1}) z = (u^2 - u^{-2}) / (u + u^{-1}) = u - u^{-1}$. For $q > 1$ (the QOU substrate side), $u > 1$, so $u - u^{-1} > 0$.

Therefore,

$$
  \mathrm{Var}(\sigma_i)
  = (u - u^{-1}) + 1 - z^2
  >  0 + 1 - 1/4
  = 3/4
  > 0.
$$

The variance is strictly positive and bounded below by $3/4$ in the Wenzl regime $q > 1$ with $q^{1/2}+q^{-1/2} > 2$.

For $q$ between the two Wenzl roots ($q^{1/2}+q^{-1/2} < 2$, the forbidden non-positive regime), the Markov trace is not positive and the construction fails to yield a tracial state. The proposition is vacuous outside the Wenzl regime. $\square$
