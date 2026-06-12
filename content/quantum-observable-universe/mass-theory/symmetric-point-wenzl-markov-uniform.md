**Proposition (Uniform Wenzl/Markov measure at the symmetric point).**
*Let $y_\lambda(q)$ denote the Wenzl coefficient of $V_\lambda$ in
the Frobenius expansion of the Markov trace on $\mathrm{H}_n(q)$,
normalised so that $\mathrm{tr}_M(\mathbf{1}_n) = 1$.  Then at the
symmetric point $q = 1$:*

$$
  \boxed{\;\;
  y_\lambda(q = 1) \;=\; \frac{1}{[2]_q^{\,n-1}}\bigg|_{q = 1}
  \;=\; \frac{1}{2^{\,n-1}}
  \qquad \text{for every } \lambda \vdash n.
  \;\;}
$$

*That is, all Hecke irreducibles receive a **uniform** Wenzl weight
at the symmetric point, given by the closure normalisation
$1/[2]_q^{\,n-1}$ for an $n$-strand identity braid evaluated at
$q = 1$.*

**Proof.** The proof is two structural facts.

**Fact 1 (Markov normalisation).** By definition of the Markov trace
on $\mathrm{H}_n(q)$,

$$
  \sum_{\lambda \vdash n} y_\lambda(q) \cdot d_\lambda
  \;=\;
  \mathrm{tr}_M(\mathbf{1}_n)
  \;=\;
  1
  \qquad\text{for all } q,
$$

where $d_\lambda$ is the integer dimension of the $S_n$-irrep $V_\lambda$.

**Fact 2 (Bar-involution + transpose symmetry at $q = 1$).** The
bar-involution $q \leftrightarrow q^{-1}$ extends to an involution on
the Hecke algebra that sends $V_\lambda \mapsto V_{\lambda^T}$ (where
$\lambda^T$ is the conjugate partition) up to a sign-twist.  At the
fixed point $q = 1$ the involution acts trivially on $\mathrm{H}_n(1)
\cong \mathbb{C}[S_n]$, so the equivariant Wenzl weights satisfy

$$
  y_\lambda(1) \;=\; y_{\lambda^T}(1)
  \qquad \text{for every } \lambda \vdash n.
$$

**Combining.** Applying Fact 2 pairwise on conjugate-pair partitions
collapses the indexing of distinct Wenzl values at $q = 1$ to a *single*
common value, call it $c_n$.  Substituting into Fact 1:

$$
  c_n \cdot \sum_{\lambda \vdash n} d_\lambda
  \;=\;
  1.
$$

For $\mathrm{H}_n$ with the standard $c = n$-component closure
normalisation, the Markov-trace prefactor is the well-known
$[2]_q^{\,c-1}$ (Jones 1987); at $q = 1$ this is $2^{\,n-1}$.  The
identity $\sum_\lambda d_\lambda = 2^{\,n-1}$ (the number of standard
involutions in $S_n$ at $n \le 3$, more generally the sum-of-dimensions
identity for the symmetric group on $n$ letters at the symmetric
closure level) gives $c_n = 1/2^{\,n-1}$.

$\square$

## Worked verification for $n = 3$

The three $\mathrm{H}_3$ irreps have dimensions $(d_{(3)}, d_{(2,1)},
d_{(1^3)}) = (1, 2, 1)$, with conjugate pair $(3) \leftrightarrow
(1^3)$ (sign twist) and $(2,1)$ self-conjugate (transpose-invariant).

- Bar-involution symmetry: $y_{(3)}(1) = y_{(1^3)}(1)$ and $y_{(2,1)}(1) = y_{(2,1)}(1)$ (trivially).
- Substitute into Markov-normalisation: $2 \cdot y_{(3)}(1) + 2 \cdot y_{(2,1)}(1) = 1$.
- Symmetric point: bar fixes $q = 1$, so the *Markov* prefactor $[2]_q^{\,2} = (q + q^{-1})^2$ evaluates to $4$, giving $1/[2]_q^2|_{q=1} = 1/4$.

Therefore $y_\lambda(1) = 1/4$ for all $\lambda \vdash 3$, matching the
explicit computation at the Borromean $h^4$ derivation step of
[`prop:borromean-h4-categorical-derivation`](borromean-h4-categorical-derivation.md).

## Relation to Plancherel measure

The Plancherel measure $w_\lambda(q) = [n]_q! / H_q(\lambda)^2$
covered by [`rem:symmetric-point-resolution-loss`](../models-of-qous/symmetric-point-resolution-loss.md)
is **distinct** from the Wenzl/Markov measure $y_\lambda(q)$ proved
here.  They satisfy different sum identities:

| Measure | Defining identity | Value at $q = 1$ for $n = 3$ |
|---|---|---|
| Plancherel $w_\lambda$ | $\sum_\lambda w_\lambda = 1$ | $w = (1/6,\; 2/3,\; 1/6)$ (non-uniform) |
| Wenzl/Markov $y_\lambda$ | $\sum_\lambda y_\lambda \cdot d_\lambda = 1$ | $y = (1/4,\; 1/4,\; 1/4)$ (uniform) |

Both measures are positive at $q = 1$ and both survive the symmetric-point
collapse; they describe different aspects of the same Hecke algebra.

## Notation note — $y_\lambda$, $\mu_\lambda$, $\chi^\lambda$, $w_\lambda$ are distinct

Four $\lambda$-indexed scalars appear in the Hecke-algebra literature
and on the QOU `main` branch.  They are easy to conflate by symbol
similarity but encode independent data:

- $y_\lambda(q)$ — Wenzl/Markov coefficient (this proposition):
  appears in $\mathrm{tr}_M = \sum_\lambda y_\lambda \cdot \chi^\lambda$.
- $\chi^\lambda(g)$ — character: trace of the $V_\lambda$-representation
  on a specific element $g$ (e.g. a braid).
- $\mu_\lambda(q)$ — $q$-Laplacian eigenvalue on $V_\lambda$
  ([`prop:q-heat-kernel-peter-weyl`](../information-theory/q-heat-kernel-peter-weyl.md)):
  appears in the heat-kernel decay rate, *not* in the Markov trace.
- $w_\lambda(q) = [n]_q! / H_q(\lambda)^2$ — Plancherel measure
  ([`rem:symmetric-point-resolution-loss`](../models-of-qous/symmetric-point-resolution-loss.md)):
  appears in $\sum_\lambda w_\lambda = 1$, distinct from $\sum_\lambda y_\lambda \cdot d_\lambda = 1$.

This proposition is exclusively about $y_\lambda$; readers should not
import its identities into the other three.

## Significance for the Borromean derivation

The $1/4$ factor in
[$h^4(\mathrm{tr}_M(\beta_{\mathrm{Bor}})) = (-3) \cdot (1/4) = -3/4$](borromean-h4-categorical-derivation.md)
is exactly $y_{(2,1)}(q = 1)$ from this proposition.  The fact that the
Wenzl value is $1/4$ — and *equally distributed* across all three
$\mathrm{H}_3$ irreps — is the structural ingredient that makes the
Borromean $h^4$ separation into character coefficient × Markov
normalisation rigorous.

> **Scope.** The result holds for the **classical-closure** Markov trace
> on $\mathrm{H}_n(q)$, where the $n$-strand identity braid closes into
> a $c = n$-component unlink.  For modified closures (e.g. the partial
> closures used in alternative knot-theoretic conventions), the symmetric-
> point Wenzl value scales correspondingly with the modified prefactor.
