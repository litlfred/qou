Let $\beta \in B_n$ be a braid on $n$ strands and let
$\rho(\beta) \in H_n(R, q)$ be its image under the Hecke quotient
([Jones--Markov trace](#thm:jones-markov-trace)).  After Hecke
reduction, the element $\rho(\beta)$ decomposes as a product of
**generator chains**: for each generator $\sigma_i$
($i = 0, \ldots, n-2$), the crossings at $\sigma_i$ reduce to a
linear combination $a_i \sigma_i + b_i$ with
$a_i, b_i \in \mathbb{Z}[q^{\pm 1}]$.

**Theorem.**  The Markov trace factors as a product over generators:

$$
  \mathrm{tr}_M\!\bigl(\rho(\beta)\bigr)
  = 
  \prod_{i=0}^{n-2} \hat{V}_i(q),
  \qquad
  \hat{V}_i(q) =  z \cdot a_i + b_i,
$$

where $z = 1/(q^{1/2} + q^{-1/2})$ is the Markov trace parameter.
Each $\hat{V}_i$ is the **vertex volume** at generator $\sigma_i$
--- the evaluation of the vertex operator $Y(\sigma_i, z_i)$ at
the $i$-th insertion point on the exceptional divisor
([vertex operator](#def:vertex-operator)).

**Proof.**  The Markov trace processes the product by peeling
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
product formula.  $\square$

## Caveat: non-adjacent generators only

The product factorization requires that the generators
$\sigma_i$ at each reduction step are **non-adjacent** —
that is, step 4 above (independence of the remaining word
from $\sigma_i$) must hold.  When generators are adjacent
(e.g. $\sigma_0 \sigma_1 \sigma_0$ in the trefoil), the
Yang–Baxter relation $\sigma_0 \sigma_1 \sigma_0 =
\sigma_1 \sigma_0 \sigma_1$ creates dependencies that
invalidate the factorization.

For the Borromean braid $\mathcal{B}_3 = (\sigma_0
\sigma_1^{-1})^3$ with adjacent generators $\sigma_0$
and $\sigma_1$: the vertex volume product gives
$hz^2 + z$, but the correct Markov trace is $z^3$
([corrected Markov trace](#prop:corrected-markov-trace)).

The product formula remains valid for the **nuclear
Garside element** (where generators are distant) and for
braids whose Hecke reduction separates generators into
independent chains.

