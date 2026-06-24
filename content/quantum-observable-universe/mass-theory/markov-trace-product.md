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
Numerically at $q_0$: vertex-product $z^3 \approx 0.1245$
vs canonical $hz^2 + z \approx 0.5514$ (4.4$\times$ off).
(Earlier versions of this block had these two values swapped;
fixed.)

The product formula remains valid for the **nuclear
Garside element** (where generators are distant) and for
braids whose Hecke reduction separates generators into
independent chains.
