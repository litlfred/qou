*Let $A$ be an algebra over a commutative ring, and let $\sigma_0, \sigma_1 \in A$
satisfy the relations of $H_3(q)$:
$\sigma_i^2 = h\,\sigma_i + 1$ and $\sigma_0\sigma_1\sigma_0 = \sigma_1\sigma_0\sigma_1$,
where $h = q - q^{-1}$. Put $V = \sigma_0\sigma_1^{-1} = \sigma_0\sigma_1 - h\,\sigma_0$. Then*

$$
  V^3 = 1 + h^2 V - h^2 V^2,
  \qquad\text{equivalently}\qquad
  (V - 1)\bigl(V^2 + (1 + h^2)V + 1\bigr) = 0,
$$

*and*

$$
  (\sigma_0\sigma_1^{-1})^3 = (1 + q h V)\,(1 - q^{-1} h V).
$$

*Each factor has the four-term form $1 + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varphi_{01}\sigma_0\sigma_1$
with $\varphi_1 = 0$:*

$$
  1 + q h V = 1 - q h^2\,\sigma_0 + q h\,\sigma_0\sigma_1,
  \qquad
  1 - q^{-1} h V = 1 + q^{-1} h^2\,\sigma_0 - q^{-1} h\,\sigma_0\sigma_1 .
$$

*The two factors commute.*

**Proof.** In the right-associated words of $\sigma_0, \sigma_1$, rewrite
$\sigma_0\sigma_0 \mapsto h\sigma_0 + 1$, $\sigma_1\sigma_1 \mapsto h\sigma_1 + 1$ and
$\sigma_1\sigma_0\sigma_1 \mapsto \sigma_0\sigma_1\sigma_0$. This gives

$$
  V^2 = \sigma_1\sigma_0 - h^2\,\sigma_0\sigma_1 - h\,\sigma_1 + h^3\,\sigma_0 + h^2,
$$

$$
  V^3 = -h^2\,\sigma_1\sigma_0 + h^3\,\sigma_1 + (1 - h^4) + (h^4 + h^2)\,\sigma_0\sigma_1 - (h^5 + h^3)\,\sigma_0 ,
$$

and comparing the two gives the cubic relation. The product of the two factors is
$1 + (q - q^{-1}) h V - h^2 V^2 = 1 + h^2 V - h^2 V^2$. The factors are polynomials
in $V$, so they commute. $\square$

The Lean statement holds in every algebra that satisfies the relations, so it holds
in $H_3(q)$ itself and in each of its representations. It uses no division, no
ordering and no value of $q$.

**Relation to the braid used for $\mathrm{tr}_M(\beta_{\mathrm{Bor}})$.** In
[the closed-form proposition](#prop:borromean-markov-trace-closed-form) the braid
is written $(\sigma_1^{-1}\sigma_2)^3$ with generators numbered from 1. Relabelled
to $\sigma_0, \sigma_1$, that is $(\sigma_0^{-1}\sigma_1)^3$. The flip
$\sigma_0 \leftrightarrow \sigma_1$ (conjugation by the half twist) sends it to
$(\sigma_1^{-1}\sigma_0)^3 = \sigma_1^{-1}(\sigma_0\sigma_1^{-1})^3\sigma_1$. So the two
braids are conjugate and have the same Markov trace. The identity above is for
$(\sigma_0\sigma_1^{-1})^3$.

**Scope.** The identity says that $\beta_{\mathrm{Bor}}$, read as a Hecke element,
is a product of two four-term photons with weights set by the two eigenvalues
$q$ and $-q^{-1}$ of $\sigma_i$. It does not select $\beta_{\mathrm{Bor}}$: products of
two such photons reach almost every element of $H_3(q)$. It changes no number. Because the two
factors commute, the order of the photons cannot distinguish the proton from the
neutron.
