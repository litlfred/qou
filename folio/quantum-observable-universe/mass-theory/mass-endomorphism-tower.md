*The mass of a vortex $\varrho$ with braid representative $\beta \in B_n$ and $n - 1$ generators evaluates as:*

$$
  \mathfrak{m}(\varrho)
  =
  \Bigl\lvert \prod_{i=0}^{n-2} \hat{V}_i^{\mathrm{full}} \Bigr\rvert
  -
  \sum_{i=0}^{n-2}
    \mathrm{Li}_2^q\!\bigl(-\lvert\hat{V}_i^{\mathrm{full}}\rvert\bigr)
  -
  \sum_{0 \leq i < j \leq n-2}
    z^2 \cdot \mathrm{Li}_2^q\!\bigl(-\lvert\hat{V}_i^{\mathrm{full}}
      \cdot \hat{V}_j^{\mathrm{full}}\rvert\bigr),
$$

*where $z = q^{3}/(q^{2}+1)$ is the Markov parameter (**convention D**) and $\mathrm{Li}_2^q$ is the symmetric q-dilogarithm $\mathrm{Li}_2^q(z) = \sum_{n \geq 1} z^n / (n \cdot [n]_q)$.*

The three sums isolate the three types of blow-up centers in the brane tower. The descended term is the base-level regular-representation trace. The single-generator blow-ups and the pair blow-ups apply the $\mathrm{Li}_2^q$ functional across the generator loci. The weight $z^2$ for pairs strictly follows from the Markov-trace factorization.

The comparison at $q_0$ behind the choice of $\mathrm{Li}_2^q$ over the Faddeev $\Phi_q$ form is recorded in [this remark](#rem:mass-endomorphism-tower-phi-q-history).
