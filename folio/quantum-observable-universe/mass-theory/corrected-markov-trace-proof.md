## Proof

Use the properties of the Markov trace
([Jones–Markov trace](#thm:jones-markov-trace)): it is linear, satisfies
$\mathrm{tr}_M(ab) = \mathrm{tr}_M(ba)$ and $\mathrm{tr}_M(1) = 1$, and
satisfies $\mathrm{tr}_M(x\sigma_n) = z\,\mathrm{tr}_M(x)$ only when
$x \in H_n(q)$, that is, when $\sigma_n$ is the largest generator in the
word and does not occur in $x$.

1. By cyclicity,
   $\mathrm{tr}_M(\sigma_0 \sigma_1 \sigma_0)
   = \mathrm{tr}_M(\sigma_0^2 \sigma_1)$.

2. Here $\sigma_0^2 \in H_2(q)$ and $\sigma_1$ is the largest generator,
   so the Markov property gives
   $\mathrm{tr}_M(\sigma_0^2 \sigma_1) = z\,\mathrm{tr}_M(\sigma_0^2)$.

3. By the Hecke relation $\sigma_0^2 = h\sigma_0 + 1$,
   $\mathrm{tr}_M(\sigma_0^2) = hz + 1$.

Therefore $\mathrm{tr}_M(\sigma_0 \sigma_1 \sigma_0) = z(hz + 1) = hz^2 + z$.
$\square$

The value $z^3$ is obtained by peeling the outer $\sigma_0$ with the
Markov property. That step is invalid, because $\sigma_0$ is not the
largest generator of $\sigma_0\sigma_1\sigma_0$.
