Work in the rank-two Hecke algebra $H_2(q) = \mathrm{span}\{1, \sigma\}$, where $\sigma^2 = h\,\sigma + 1$ with $h = q - q^{-1}$. The inverse crossing is $\sigma^{-1} = \sigma - h$, since $\sigma(\sigma - h) = 1$. The Markov trace on $H_2(q)$ is $\mathrm{tr}_M(a + b\,\sigma) = a + z\,b$, and we take $z = q^3/(q^2+1)$.

The Borromean braid of a nucleon with quarks $(q_1, q_2, q_3)$ has six crossings organised into three pairs of strands. Each pair crosses once positively and once negatively, so its linking number is zero. Weight the positive crossing by the dressed quark Skein mass $\mu_a$ of the first strand and the negative crossing by $\mu_b$ of the second. Here $\mu_a$ is the mass contribution of a single quark strand including its strong-field dressing from the Hopf-link interaction with the color background. The pair Skein mass is the Markov trace of the weighted crossing element:

$$
  \mathcal{S}_{ab}(q)
  = \mathrm{tr}_M\!\left(\mu_a\,\sigma + \mu_b\,\sigma^{-1}\right)
  = \mu_a\,\mathrm{tr}_M(\sigma) + \mu_b\,\mathrm{tr}_M(\sigma - h)
  = \mu_a\, z + \mu_b\,(z - h).
$$

Now $z = q^3/(q^2+1)$ and

$$
  z - h = \frac{q^3}{q^2+1} - q + q^{-1} = \frac{q^{-1}}{q^2+1},
$$

so

$$
  \mathcal{S}_{ab}(q) = \frac{q^{3}\mu_a + q^{-1}\mu_b}{q^{2} + 1}.
$$

At $q = 1$ this is $(\mu_a + \mu_b)/2$. The difference $\mathcal{S}_{ab} - \mathcal{S}_{ba} = (q^3 - q^{-1})(\mu_a - \mu_b)/(q^2+1) = (q - q^{-1})(\mu_a - \mu_b)$, since $q^3 - q^{-1} = (q - q^{-1})(q^2+1)$. The total nucleon mass is the sum over the three pairs of strands:

$$
  m_N
  =
  \mathcal{S}_{q_1 q_2}(q)
  + \mathcal{S}_{q_1 q_3}(q)
  + \mathcal{S}_{q_2 q_3}(q).
$$

$\square$
