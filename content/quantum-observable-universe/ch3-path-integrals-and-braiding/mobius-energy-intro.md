The classical Möbius energy of O'Hara assigns to a closed curve
$\gamma \colon S^1 \to \mathbb{R}^3$ the regularised self-repulsion integral

$$
E(\gamma)
\;=\;
\iint_{S^1 \times S^1}
\!\biggl(\frac{1}{\lvert \gamma(s) - \gamma(t)\rvert^2}
       - \frac{1}{d_\gamma(s,t)^2}\biggr)\,
\lvert \gamma'(s)\rvert\,\lvert \gamma'(t)\rvert\;\mathrm{d}s\,\mathrm{d}t,
$$

where $d_\gamma(s,t)$ is the intrinsic arc-length distance.  This functional
is invariant under Möbius transformations of $\mathbb{R}^3 \cup \{\infty\}
\cong S^3$ and penalises configurations in which non-adjacent strands approach
one another, thereby enforcing a topological "self-avoidance" constraint.

In this section we show that $E(\gamma)$ arises as the leading-order term
of the **categorical mass** $m(\gamma)$ defined by the QOU action
$\mathcal{S}_q$ when the substrate parameter $q \to 1$.  The key
ingredients are the Frobenius--Hopf structure on the fibre algebra $A$
and the categorical volume constraint that fixes the gauge group to
$\mathrm{SU}(2)$.

The categorical derivation simultaneously explains why, for $q \neq 1$,
the energy acquires quantum corrections that prevent the knot from
self-intersecting: the non-cocommutativity of the Hopf comultiplication
provides a geometric barrier controlled by the universal $R$-matrix
$\mathcal{R}$.
