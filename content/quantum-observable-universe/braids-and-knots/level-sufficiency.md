**Proposition.**
*Let $K$ be a closed braid admitting Hecke normal forms at two
confinement levels:*

$$
  T_w^{\mathrm{coarse}} \in H_{n_0}(q),
  \qquad
  T_w^{\mathrm{fine}} \in H_{n_1}(q),
  \qquad
  n_0 \le n_1,
$$

*related by the confinement reduction
([confinement LP](#prop:confinement-lp),
[topological confinement](#prop:confinement-topological)).
Let $k_{\max}(K, q, n)$ denote the witnessed partition truncation
of $K$ represented at strand count $n$
([confinement level](#def:confinement-level)).  Suppose
$k_{\max}(K, q, n_0) \le n_0$.  Then:*

$$
  \mathrm{tr}_M\bigl(T_w^{\mathrm{coarse}}\bigr)
  \;=\;
  \mathrm{tr}_M\bigl(T_w^{\mathrm{fine}}\bigr)
  \quad\text{in }\mathbb{C}(q).
$$

*Consequently, for any trace-class invariant $\mathcal{F}$ of $K$
that factors through $\mathrm{tr}_M$ — including mass
$\mathfrak{m}(K)$, binding $B(K)$, and the Jones polynomial — the
coarsest representation at which
$k_{\max}(K, q, n) \le n$ is **computationally sufficient**:
unfolding to any deeper level is superfluous for $\mathcal{F}(K)$.*

*Proof.*
*The Ocneanu–Jones Markov trace
$\mathrm{tr}_M: H_\bullet(q) \to \mathbb{C}(q)$ is a compatible
family along the tower of Hecke inclusions
$H_n(q) \hookrightarrow H_{n+1}(q)$, with
$\mathrm{tr}_M \circ \iota = \mathrm{tr}_M$ (Markov property).
The fine NF $T_w^{\mathrm{fine}}$ is obtained from
$T_w^{\mathrm{coarse}}$ by unfolding $n_1 - n_0$ additional strand
groups through the confinement reduction; each unfolded group is
a closed sub-braid realising a confined knot operator
([confinement operator selection](#prop:confinement-operator-selection)),
so its image in $H_{n_1}(q) / \iota(H_{n_0}(q))$ lies in the
Frobenius cone
$G\vec{x} \ge 0$
([confinement LP](#prop:confinement-lp))
and cannot contribute a non-identity Markov peel — by
Gram indefiniteness
([topological confinement](#prop:confinement-topological))
the only energetic minimum of the unfolded block is
$\mathrm{tr}_M = 0$.*

*Partition content: the hypothesis
$k_{\max}(K, q, n_0) \le n_0$ asserts that every Wedderburn block
$\lambda \vdash k$ with $k > n_0$ has zero projection in
$T_w^{\mathrm{coarse}}$.  Hecke-inclusion compatibility of the
Markov trace
([Jones 1987](https://doi.org/10.2307/1971403))
preserves this vanishing under $\iota$, so the additional blocks
$\lambda \vdash k$ with $n_0 < k \le n_1$ accessible at the fine
level contribute zero.  Thus
$\mathrm{tr}_M(T_w^{\mathrm{fine}}) = \mathrm{tr}_M(\iota\,T_w^{\mathrm{coarse}})
= \mathrm{tr}_M(T_w^{\mathrm{coarse}})$.
$\square$*

**Converse (unfolding necessity).**
*If $k_{\max}(K, q, n_0) > n_0$ — the witnessed partition content
exceeds the coarse strand count — then no representation in
$H_{n_0}(q)$ exists, and unfolding to the smallest level $n_1$
with $k_{\max}(K, q, n_1) \le n_1$ is strictly required.  In
particular, magic shell closure
([confinement level](#def:confinement-level), magic configurations)
and SDP cross-channel constraints that force
$k_{\max} > n_0$ are the only triggers for unfolding.*
