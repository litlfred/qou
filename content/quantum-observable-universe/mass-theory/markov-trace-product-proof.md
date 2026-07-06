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

For the trefoil-like element $\sigma_0\sigma_1\sigma_0$
with adjacent generators $\sigma_0$ and $\sigma_1$: the naïve
vertex volume product gives $z^3$, but the **correct Markov
trace** (Ocneanu--Wenzl recursion) is $hz^2 + z$
([corrected Markov trace](#prop:corrected-markov-trace);
[Markov-bug audit](https://github.com/litlfred/qou/blob/main/docs/audits/-trm5-markov-bug.md)).
canonical at $q_0$: vertex-product $z^3 \approx 0.1245$
vs canonical $hz^2 + z \approx 0.5514$ (4.4$\times$ off).
(Earlier versions of this block had these two values swapped;
fixed.)

The product formula remains valid for the **nuclear
Garside element** (where generators are distant) and for
braids whose Hecke reduction separates generators into
independent chains.
