*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Proposition.**
Let $\sigma$ denote the cyclic generator of $\mathbb{Z}_5$, and write its
induced action on regular functions on the left.
On Bring's surface the first Lagrange resolvent $w_1$ is an eigenvector
of $\sigma$ with eigenvalue $\zeta_5^{-1}$
([prop:lagrange-resolvent-transform](#prop:lagrange-resolvent-transform));
on $\mathcal{X}_5$ the coordinate $x$ is an eigenvector of $\sigma$
with the same eigenvalue
([prop:x5-z5-automorphism](#prop:x5-z5-automorphism)).
Consequently there is a canonical $\mathbb{Z}_5$-equivariant
identification

$$
  \mathcal{O}(\mathcal{X}_5)_{\zeta_5^{-1}}
   \overset{\sim}{\longrightarrow}
   \mathcal{O}(\mathcal{B}_{\mathrm{Br}})_{\zeta_5^{-1}},
  \qquad
  x  \longmapsto  w_1,
$$

of the weight-$(-1)$ isotypical components of the coordinate rings,
and this identification extends to a $\mathbb{Z}_5$-equivariant map of
graded rings on the entire $\mathbb{Z}_5$-isotypical decomposition by
sending $x^{k} \mapsto w_1^{\,k}$ for $0 \leq k \leq 4$ (with $x^5$ and
$w_1^{\,5}$ both invariant).

*Proof.*
Eigenvalue on $\mathcal{X}_5$: the automorphism $\phi_5(x, y) = (\zeta_5 x, y)$
pulls back the coordinate function $x$ to
$(\phi_5^{-1})^{*}(x) = \zeta_5^{-1} x$ under the left-action convention
$\sigma \cdot f = f \circ \sigma^{-1}$, so $x$ is an eigenvector with
eigenvalue $\zeta_5^{-1}$.

Eigenvalue on Bring: the cyclic permutation $\sigma(x_j) = x_{j+1}$
diagonalises on the Lagrange resolvents as $\sigma(w_k) = \zeta_5^{-k} w_k$
([prop:lagrange-resolvent-transform](#prop:lagrange-resolvent-transform));
specialising to $k = 1$ gives $\sigma(w_1) = \zeta_5^{-1} w_1$.

Both $x$ and $w_1$ span their respective weight-$(-1)$ eigenspaces
(one-dimensional in each coordinate ring).  The linear map
$x \mapsto w_1$ is therefore a canonical $\mathbb{Z}_5$-equivariant
isomorphism of weight-$(-1)$ subspaces, and the extension to powers
$x^{k} \mapsto w_1^{\,k}$ carries weight $\zeta_5^{-k}$ on both sides,
hence is $\mathbb{Z}_5$-equivariant on the five-term cyclic isotypical
decomposition.  $\square$

**Remark on the geometric content.**  This identification is
categorical, not a morphism of curves.  By Riemann--Hurwitz there is
no non-constant curve morphism $\mathcal{X}_5 \to \mathcal{B}_{\mathrm{Br}}$
($g = 2 < 4$), and $\mathcal{B}_{\mathrm{Br}}$ has no genus-$2$ Galois
quotient ($S_5$ has no subgroups of index $2$ or $3$ with the requisite
ramification).  What the proposition asserts is a compatibility of
$\mathbb{Z}_5$-graded observables under the Lagrange ordering: the
same categorical weight-$(-1)$ coordinate parametrises the single
$\mathrm{U}(1)$ phase tube of
[rem:u1-phase-tube](#rem:u1-phase-tube) and the first Fourier mode
of Bring's geometry.  See
[rem:x5-bring-prym-jacobian](#rem:x5-bring-prym-jacobian) for the
parallel structure at the level of Jacobians.
