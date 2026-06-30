## Proof

By the Markov property
([Jones–Markov trace](#thm:jones-markov-trace)) together with trace
cyclicity, applying $\mathrm{tr}_M$ to $\sigma_0 \sigma_1 \sigma_0$:

1. $\mathrm{tr}_M(\sigma_0 \sigma_1 \sigma_0)
   = \mathrm{tr}_M(\sigma_0^2 \sigma_1)$
   (trace cyclicity — move the rightmost $\sigma_0$ to the front so
   the **top** generator $\sigma_1$ sits once at the end of the word)

2. $\mathrm{tr}_M(\sigma_0^2 \sigma_1)
   = z \cdot \mathrm{tr}_M(\sigma_0^2)$
   (Markov property on $\sigma_1$, the **maximal-index** generator,
   appearing once at the end)

3. $\mathrm{tr}_M(\sigma_0^2) = h z + 1$
   (Hecke relation $\sigma_0^2 = h\sigma_0 + 1$ with $h = q - q^{-1}$,
   and $\mathrm{tr}_M(\sigma_0) = z$)

Therefore $\mathrm{tr}_M(\sigma_0 \sigma_1 \sigma_0)
= z(hz + 1) = hz^2 + z$.

The naive multiplicative value $z^3 =
\mathrm{tr}_M(\sigma_0)\,\mathrm{tr}_M(\sigma_1)\,\mathrm{tr}_M(\sigma_0)$
assumes each generator reduces independently — valid only for
**non-adjacent** (commuting) generators.  For the trefoil
$\sigma_0 \sigma_1 \sigma_0$ the adjacent generators satisfy the braid
relation $\sigma_0 \sigma_1 \sigma_0 = \sigma_1 \sigma_0 \sigma_1$, so
the Markov recursion above — not multiplicativity — gives the value.
The result is the canonical coefficient $\alpha_3 = hz^2 + z$, verified
by the `pyhecke` Markov-trace engine
(`computations/corrected-markov-trace.witness.json`).

## Impact

The earlier value $z^3$ was an artifact of applying the Markov
reduction to the **minimal**-index generator $\sigma_0$ rather than to
the top generator $\sigma_1$.  With the correct trace $hz^2 + z$:

- it agrees with the canonical $\alpha_3$ ladder already used
  throughout the mass-coefficient computations, so no separate
  "corrected" single-knot trace is required;
- the nucleon mass ordering $\mathfrak{m}_{\mathfrak{n}} >
  \mathfrak{m}_{\mathfrak{p}}$ is an experimental fact whose
  categorical account rests on the Borromean-baryon trace, **not** on
  this single trefoil trace; the earlier $z^3$-based "restoration" was
  invalid and is withdrawn
  ([mass ordering](#rem:mass-ordering-corrected)).
