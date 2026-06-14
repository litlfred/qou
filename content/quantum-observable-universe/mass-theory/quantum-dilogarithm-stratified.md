**Proposition (partition-depth stratification of $\Phi_q$).**

*Let $A = H_n(R, q)$ be a semisimple Hecke algebra at generic $q$, and
let* $Z(A) = \bigoplus_{\lambda \vdash n} R \cdot e_\lambda$ *be its
centre. Decompose the centre by GB-depth of partitions
([curvature-rank stratification](#prop:curvature-rank-gb-stratification)):*

$$
  Z(A) \;=\; \bigoplus_{k \geq 0} Z^{(k)}(A),
  \qquad
  Z^{(k)}(A) \;=\; \mathrm{span}_R\bigl\{e_\lambda : \mathrm{depth}_{\mathrm{GB}}(\lambda) = k\bigr\}.
$$

*The analytic quantum dilogarithm
([quantum dilogarithm](#cor:quantum-dilogarithm))
$\Phi_q(z_i) = \prod_{k=1}^{\infty}(1 - q^{-k} z_i)^{-1}$ at the $i$-th
exceptional divisor admits a centre-stratified expansion: there exist
$Z^{(k)}(A)$-valued coefficients $\phi_q^{(k)}(z_i) \in Z^{(k)}(A)$
such that, on every $T_w \in H_n(R, q)$ with $\mathrm{supp}(T_w) \subseteq Z(A)$,*

$$
  \mathrm{tr}_M\!\bigl(\Phi_q(z_i) \cdot T_w\bigr)
  \;=\;
  \sum_{k = 0}^{\infty}
    \bigl\langle \phi_q^{(k)}(z_i),\, T_w \bigr\rangle,
$$

*where $\langle \cdot, \cdot \rangle$ is the Frobenius pairing on $Z(A)$.
Moreover, the depth-$k$ coefficient* $\phi_q^{(k)}(z_i)$ *is the
**Frobenius dual** of the truncation increment*

$$
  \phi_q^{(k)}(z_i)
  \;\equiv\;
  \Bigl(\Phi_q^{[\leq k]}(z_i) - \Phi_q^{[\leq k-1]}(z_i)\Bigr) \cdot \mathbf{1}_{Z^{(k)}(A)}
  \pmod{\bigoplus_{\ell \neq k} Z^{(\ell)}(A)},
$$

*so the partial sum $\Phi_q^{[\leq k]}(z_i) = \sum_{j=0}^{k}\phi_q^{(j)}(z_i)$
captures exactly the $\bigoplus_{j \leq k} Z^{(j)}(A)$-content of
$\Phi_q(z_i)$.*

*The truncation $\Phi_q^{[\leq k]}(z_i)$ is the $|q| > 1$ Faddeev
form of the same partial product written in the $|q| < 1$ convention
in ([q-Pochhammer partial product](#def:q-pochhammer-partial-product));
the conventions agree under $q \mapsto q^{-1}$ and the explicit
denominator polynomial $(x; q)_n$ is recorded there.*

**Corollary (truncation = projection onto NF-support depth).**
*For $T_w$ with NF support depth*
$k_\star(T_w) = \max_{\lambda \in \mathrm{supp}(T_w)} \mathrm{depth}_{\mathrm{GB}}(\lambda)$,

$$
  \mathrm{tr}_M\!\bigl(\Phi_q(z_i) \cdot T_w\bigr)
  \;=\;
  \mathrm{tr}_M\!\bigl(\Phi_q^{[\leq k_\star(T_w)]}(z_i) \cdot T_w\bigr),
$$

*because all $\phi_q^{(k)}(z_i)$ for $k > k_\star(T_w)$ pair to zero
with $T_w$ under the Frobenius pairing (they live in centre strata
$Z^{(k)}(A)$ with $k > k_\star(T_w)$, on which $T_w$ has zero
projection by definition of $k_\star$). The analytic infinite product
truncates to a finite product as a Frobenius-paired identity, with
the truncation depth structurally determined by $T_w$'s NF support.*

## Why this resolves Step 4 of [$\Phi_q$ categorical truncation](#prop:phi-q-categorical-truncation)

[Cor: quantum dilogarithm](#cor:quantum-dilogarithm) gives the
analytic identity $\mathrm{tr}_{\mathrm{trans}}(\varrho, p_i) = \Phi_q(z_i)$ as
the level-$i$ archimedean torsion volume — but as an *analytic*
(infinite-product) object, with no curvature-rank stratification
visible.

This proposition refines that identity by exposing the
partition-depth filtration of $\Phi_q(z_i)$ inside $Z(A)$. The bridge
is the Frobenius pairing: while the analytic product $\Phi_q(z_i)$
diverges at $|z_i| \to q$, its **Frobenius pairing with any specific
$T_w$** evaluates to a *finite* sum over the $\leq k_\star(T_w)$
depth-strata of the centre. The $|\hat V|\approx 1$ ill-conditioning is
then a property of the analytic representation, not of the
Frobenius-paired categorical mass.
