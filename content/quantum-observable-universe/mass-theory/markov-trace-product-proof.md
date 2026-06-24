The Markov trace processes the product by peeling
generators from the right.  At each step, $\sigma_i$ is the
rightmost (largest-index) generator in the remaining word, and
the Markov property gives:

$$
  \mathrm{tr}_M(\cdots (a_i \sigma_i + b_i))
  = 
  (z \cdot a_i + b_i) \cdot \mathrm{tr}_M(\cdots).
$$

This works because:

1. The chain at $\sigma_i$ reduces to $a_i \sigma_i + b_i$ (linear
   in $\sigma_i$ and the identity).
2. The Markov property
   $\mathrm{tr}_M(x \sigma_n) = z\mathrm{tr}_M(x)$ applies to
   the $\sigma_i$ term.
3. Generator $\sigma_i$ is the rightmost active generator, so the
   Markov property applies directly.
4. The remaining word involves only $\sigma_0, \ldots, \sigma_{i-1}$,
   independent of $\sigma_i$.

Applying this recursively from $i = n-2$ down to $i = 0$ gives the
product formula.
$\qquad\blacksquare$
