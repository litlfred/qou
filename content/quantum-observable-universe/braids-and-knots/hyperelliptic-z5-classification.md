**Theorem.**
Let $X$ be a smooth projective Riemann surface of minimal genus
satisfying the two conditions

*(i)*  $X$ is hyperelliptic: there exists a degree-$2$ morphism
$\pi \colon X \to \mathbb{P}^1$ with involution $\iota$;

*(ii)* $X$ admits a faithful $\mathbb{Z}_5$ automorphism $\phi$
commuting with $\iota$.

Then $g(X) = 2$ and $X$ is isomorphic to
$\mathcal{X}_5 \colon y^2 = x^5 - 1$
([def:hyperelliptic-quintic](#def:hyperelliptic-quintic)).

*Proof.*
Because $\phi$ commutes with $\iota$ it descends along $\pi$ to an
automorphism $\bar\phi$ of $\mathbb{P}^1$; faithfulness of $\phi$ and
commutativity with $\iota$ force $\bar\phi$ to be an element of order
$5$ in $\mathrm{PGL}_2(\mathbb{C}) = \mathrm{Aut}(\mathbb{P}^1)$.  Every
order-$5$ element of $\mathrm{PGL}_2(\mathbb{C})$ is conjugate to
$x \mapsto \zeta_5 x$, which has exactly two fixed points on
$\mathbb{P}^1$, namely $\{0, \infty\}$.  After Möbius normalisation we
may take $\bar\phi \colon x \mapsto \zeta_5 x$.

Orbits of $\bar\phi$ on $\mathbb{P}^1$ have size $1$ (fixed points:
$0, \infty$) or $5$ (generic orbits
$\{a, \zeta_5 a, \zeta_5^{\,2} a, \zeta_5^{\,3} a, \zeta_5^{\,4} a\}$
for $a \notin \{0, \infty\}$).

The branch divisor of $\pi$ is $\phi$-invariant (since $\phi$ commutes
with $\iota$), hence a $\bar\phi$-invariant subset of $\mathbb{P}^1$.
Its cardinality is therefore a non-negative combination of $1$ and $5$:
$|\mathrm{Branch}(\pi)| \in \{0, 1, 2, 5, 6, 7, 10, 11, 12, \ldots\}$.

By Riemann--Hurwitz,

$$
  |\mathrm{Branch}(\pi)|  =  2g(X) + 2,
$$

so the size is even and at least $4$ (for $g \geq 1$, which is forced
by (ii): a sphere has $\mathrm{Aut}(\mathbb{P}^1) = \mathrm{PGL}_2$
admitting $\mathbb{Z}_5$ but is excluded from hyperelliptic indexing
$g \geq 2$; for $g = 0$ one takes $X = \mathbb{P}^1$ itself, not a
branched double cover).
The smallest admissible $|\mathrm{Branch}(\pi)|$ in the list above that
is even and at least $6$ is $6$, giving $g = 2$.

The combinatorial decomposition of a $\bar\phi$-invariant set of
size $6$ is uniquely a size-$5$ orbit plus one fixed point (there is
no other way to write $6 = 5a + b$ with $a, b \geq 0$ and $b \leq 2$).
The branch divisor is therefore

$$
  \mathrm{Branch}(\pi)
     =   \{\zeta_5^{\,k} a : 0 \leq k \leq 4\}
   \,\cup\,  \{c\}
  \qquad
  \text{for some } a \neq 0, c \in \{0, \infty\}.
$$

After rescaling ($x \mapsto a^{-1} x$) we may take $a = 1$, giving the
orbit $\{1, \zeta_5, \zeta_5^{\,2}, \zeta_5^{\,3}, \zeta_5^{\,4}\}$.
The two choices $c = \infty$ and $c = 0$ yield the equations
$y^2 = x^5 - 1$ and $y^2 = x(x^5 - 1) = x^6 - x$ respectively; the
change of chart $x \mapsto 1/x$, $y \mapsto y/x^3$ sends one to the
other up to sign, which can be absorbed into $y$.  A smooth
hyperelliptic curve of genus $\geq 2$ is determined up to
isomorphism by its branch divisor, so both choices yield isomorphic
curves.

Therefore $X \cong \mathcal{X}_5$. $\square$

**Remarks.**

1.  *Fixed-point symmetry.*  The two $\mathbb{Z}_5$-fixed points $0$
    and $\infty$ of $\mathbb{P}^1$ play symmetric roles: either can
    be chosen as the sixth branch point.  The resulting curves are
    canonically isomorphic, which is why we can speak of
    $\mathcal{X}_5$ in the singular.

2.  *The minimality is tight.*  Dropping minimality allows
    $|\mathrm{Branch}(\pi)| \in \{10, 12, 14, \ldots\}$, giving
    genera $g \in \{4, 5, 6, \ldots\}$.  The $g = 4$ case with two
    size-$5$ orbits is the neighbourhood of Bring's curve; higher
    cases are Galois covers of $\mathcal{X}_5$ or degenerations.

3.  *No condition on "inheritance from Bring".*  Condition (ii)
    asks only for a faithful $\mathbb{Z}_5$, not for that
    $\mathbb{Z}_5$ to be a Sylow subgroup of any larger symmetry
    group.  The identification of this abstract $\mathbb{Z}_5$ with
    the Sylow-5 residue of Bring's $S_5$ is a separate narrative
    assertion, justified by the explicit computation of
    [rem:bring-z5-descent](#rem:bring-z5-descent).
