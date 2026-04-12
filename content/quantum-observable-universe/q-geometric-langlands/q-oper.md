Let $\check{G}_q$ be the $q$-Langlands dual group
([q-Langlands dual](#def:q-langlands-dual)) and
$\check{\mathfrak{b}}_q \subset \check{\mathfrak{g}}_q$ a Borel
subalgebra of its Lie algebra.  A **$q$-oper** on the brane curve
$X$ is a $q$-flat connection
([q-flat connection](#def:q-flat-connection))

$$
  (\mathcal{P}_{\check{G}_q}, \nabla_q)
$$

on a $\check{G}_q$-bundle $\mathcal{P}_{\check{G}_q} \to X$, together
with a $\check{B}_q$-reduction $\mathcal{P}_{\check{B}_q} \subset
\mathcal{P}_{\check{G}_q}$, satisfying the **$q$-oper condition**:
the $q$-connection $\nabla_q$ is *transverse* to the Borel reduction
in the sense that for each simple root $\alpha_i$ of $\check{G}_q$,
the component of $\nabla_q$ along $\check{\mathfrak{g}}_{-\alpha_i}$
is non-vanishing:

$$
  \mathrm{pr}_{-\alpha_i}(\nabla_q \bmod \check{\mathfrak{b}}_q)
  \neq 0
  \quad \text{for all simple roots } \alpha_i.
$$

For $\check{G}_q = \mathrm{SU}_{q^{-1}}(2)$, a $q$-oper on $X$ is a
rank-$2$ $q$-flat bundle with an invariant line subbundle $\mathcal{L}
\subset \mathcal{V}$ such that $\nabla_q(\mathcal{L}) \not\subset
\mathcal{L} \otimes \Omega^1_q$.  The $q$-oper is then equivalent
to a $q$-deformed projective connection (Sturm--Liouville operator):

$$
  \partial_q^2 + t(z), \qquad
  t(z) \in H^0(X, \Omega_q^{\otimes 2}).
$$

We denote the moduli of $q$-opers by $\mathrm{Op}_{\check{G}_q}(X)$.
