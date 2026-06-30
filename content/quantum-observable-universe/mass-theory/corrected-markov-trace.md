The Markov trace of the trefoil braid
$\sigma_0 \sigma_1 \sigma_0$ is $hz^2 + z$, **not** the naive
multiplicative product $z^3$.  Multiplicativity
$\mathrm{tr}_M(\sigma_0)\,\mathrm{tr}_M(\sigma_1)\,\mathrm{tr}_M(\sigma_0) = z^3$
fails for **adjacent** generators: $\sigma_0$ and $\sigma_1$ satisfy the
braid relation $\sigma_0 \sigma_1 \sigma_0 = \sigma_1 \sigma_0 \sigma_1$
rather than commuting, so the Markov recursion must be applied to the
top generator $\sigma_1$ (see the proof).

## Statement

**Proposition.**

$$
  \mathrm{tr}_M(\sigma_0 \sigma_1 \sigma_0) = h z^2 + z
$$

*where $z = \mathrm{tr}_M(\sigma_i)$ is the Markov parameter and
$h = q - q^{-1}$.  In the canonical $\mathbf{H}_3(q)$ normalisation
($q = s^2$, $z = s/(s^2+1)$) this equals $(s^2 + s - 1)/(s^2 + 1)$ —
the value returned by the canonical `pyhecke` Markov-trace engine
(witness `computations/corrected-markov-trace.witness.json`).  It
coincides with the canonical coefficient $\alpha_3 = hz^2 + z$ derived
in the explicit-$\alpha_k$ proof for $H_3$.  The naive product $z^3$
does **not** apply.*
