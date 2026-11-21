*Proof sketch.*
By Schur–Weyl duality at level $n = 3$ in three dimensions ([Schur–Weyl mass decomposition](#prop:schur-weyl-mass-decomposition)), the $\mathrm{S}_3$-module

$$
  V \;:=\; \bigotimes_{k=1}^{3}\, T_{c_k}\mathbf{C}
  \;\cong\; R\,\langle dc_1/dz,\ dc_2/dz,\ dc_3/dz\rangle
$$

decomposes into isotypic components labelled by partitions of $3$:

$$
  V \;\cong\; V_{(3)} \;\oplus\; V_{(1,1,1)} \;\oplus\; V_{(2,1)}
  \;=\; \mathrm{Sym}^3 \;\oplus\; \mathrm{Alt}^3 \;\oplus\; \mathrm{Std}^{\oplus 2}.
$$

The dimensions are $\dim_R V_{(3)} = 1$, $\dim_R V_{(1,1,1)} = 1$, $\dim_R V_{(2,1)} = 2$, summing to $4$. However, since $V$ is the rank-$3$ permutation representation of $\mathrm{S}_3$, $V \cong V_{(3)} \oplus V_{(2,1)}$. The rank-$1$ alternating piece sits inside the exterior cube $\Lambda^3 V$. The relevant isotype is therefore the top exterior power.

By the Frobenius character formula ([Frobenius universal](#thm:frobenius-codim-universal)) applied to $\mathrm{S}_3$, the projector onto the sign isotype of any $\mathrm{S}_3$-module $W$ is

$$
  \pi_{\mathrm{Alt}}
  \;=\;
  \frac{1}{|\mathrm{S}_3|} \sum_{\sigma \in \mathrm{S}_3}
    \mathrm{sgn}(\sigma)\, \sigma
  \;=\;
  \frac{1}{6}\bigl(
    \mathrm{id} - (12) - (13) - (23) + (123) + (132)
  \bigr).
$$

Applied to $dc_1/dz \otimes dc_2/dz \otimes dc_3/dz \in V^{\otimes 3}$, this projector yields the antisymmetrisation

$$
  \pi_{\mathrm{Alt}}\bigl(dc_1/dz \otimes dc_2/dz \otimes dc_3/dz\bigr)
  \;=\;
  \frac{1}{6} \sum_{\sigma \in \mathrm{S}_3}
    \mathrm{sgn}(\sigma)\,
    \bigotimes_{k=1}^{3} dc_{\sigma(k)}/dz.
$$

Write $v_k := dc_k/dz$. Under the canonical isomorphism $\Lambda^3 V \cong R$, the antisymmetrised tensor maps to $v_1 \wedge v_2 \wedge v_3$. On the diagonal frame $\bigl(v_k\, e_k\bigr)_{k=1}^{3}$ this is $\bigl(\prod_k v_k\bigr)\, e_1 \wedge e_2 \wedge e_3$. The sign change under sheet exchange is carried by $e_1 \wedge e_2 \wedge e_3$, not by the coefficient: after the identification $e_1 \wedge e_2 \wedge e_3 \mapsto 1$, which is not $\mathrm{S}_3$-equivariant, the scalar $\prod_k v_k$ is symmetric. So the product is not a sign-isotypic scalar.

The sign-isotypic scalars are the antisymmetric polynomials in $v_1, v_2, v_3$. Applying $\pi_{\mathrm{Alt}}$ to the monomial $v_1^0 v_2^1 v_3^2$ gives $\tfrac{1}{6}\sum_{\sigma} \mathrm{sgn}(\sigma)\, v_{\sigma(2)}\, v_{\sigma(3)}^2$, which is $\tfrac{1}{6}$ times the $3 \times 3$ Vandermonde determinant. Its cofactor expansion factors as

$$
  (v_2 v_3^2 - v_3 v_2^2) - v_1 (v_3^2 - v_2^2) + v_1^2 (v_3 - v_2)
  \;=\;
  (v_2 - v_1)(v_3 - v_1)(v_3 - v_2)
  \;=\; \lambda_{\mathrm{baryon}},
$$

an identity in any commutative ring (Lean: `QOU.Archimedean.baryonProductFromAlt`). Every antisymmetric polynomial is divisible by each $v_j - v_i$, hence by $\lambda_{\mathrm{baryon}}$, with symmetric quotient; so $\lambda_{\mathrm{baryon}}$ spans the lowest-degree part of the sign isotype.

**$R$-rationality.** By implicit differentiation $v_k = -(\partial F/\partial z)/(\partial F/\partial c)$ at $(z, c_k)$, a rational function of $c_k$ over $R(z)$. The ratio $\lambda_{\mathrm{baryon}} / V_3(c_1, c_2, c_3)$ is symmetric in the roots, hence lies in $R(z)$, and the squared Vandermonde of the roots is the discriminant of the cubic ([color-tube cubic](#rem:color-tube-cubic)):

$$
  V_3(c_1, c_2, c_3)^2
  \;=\;
  \prod_{1 \leq i < j \leq 3} (c_i - c_j)^2
  \;=\;
  \Delta(z)
  \;\in\; R[z].
$$

So $\lambda_{\mathrm{baryon}}^2 \in R(z)$, and $\lambda_{\mathrm{baryon}}$ itself lies in $R(z)\bigl(\sqrt{\Delta(z)}\bigr)$. $\square$

The sum $\sum_k dc_k/dz$ spans the degree-one part of the trivial isotype $V_{(3)}$, the integrand for a symmetric trion. The baryon sits in the antisymmetric colour singlet $\mathrm{Alt}^3$, selecting the velocity Vandermonde. This algebraic selection requires no input from the Picard–Lefschetz machinery. Both the Vandermonde and $\pi_{\mathrm{Alt}}$ are defined over $R$; the baryon integrand evaluation remains $R$-rational until the archimedean fibre functor $\tau$ is applied.

This algebraic choice of the sign block, combined with the scalar weight $w_\lambda$ from the Markov trace ([categorical mass as Markov trace](#prop:categorical-mass-markov)), fully determines the baryon integrand $\lambda_{\mathrm{baryon}}$.

**Scope of the selection — derived versus input.** Two claims must be kept apart. That $\mathrm{Alt}^3$ is a *genuinely non-trivial* one-dimensional representation is **derived**: the monodromy of the color-tube cubic $F$ around its discriminant is the full $\mathrm{S}_3$, computed exactly over $R = \mathbb{Q}[z]$ (irreducibility over $\mathbb{C}(z)$ gives transitivity; the depressed quadratic is coprime to $\Delta$, so every one of the six simple branch points carries a transposition, and a transitive subgroup of $\mathrm{S}_3$ with a transposition is $\mathrm{S}_3$) and confirmed at $50$ digits by transporting the three sheets around all six branch points — every loop returns a transposition and the six generate $\mathrm{S}_3$ ([monodromy witness](../../../computations/probes/bring-cubic-monodromy-probe.witness.json)). Had the group been only $A_3$, the sign line would coincide with the trivial one and selecting $\mathrm{Alt}^3$ would carry no information; the surjectivity onto $\{\pm 1\}$ rules that out. What remains an **input** — not derived from the categorical substrate — is that the physical baryon *occupies* $\mathrm{Alt}^3$ rather than the trivial or standard isotype: this is the color-singlet (confinement) condition. Stating the occupation as a derivation would conflate an invariant of the fibre (the non-trivial sign line, which the geometry supplies) with the channel of the state (which it does not), and is the standing open item.
