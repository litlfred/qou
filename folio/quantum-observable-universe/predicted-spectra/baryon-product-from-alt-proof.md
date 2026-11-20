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

Under the canonical isomorphism $\Lambda^3 V \cong R$, the antisymmetrised tensor maps to the wedge product

$$
  (dc_1/dz) \wedge (dc_2/dz) \wedge (dc_3/dz).
$$

Evaluated on the diagonal vector $\bigl((dc_k/dz)\,e_k\bigr)_{k=1}^{3}$ with $R$-basis $\{e_1, e_2, e_3\}$, this yields

$$
  \bigl((dc_1/dz)\,e_1\bigr) \wedge \bigl((dc_2/dz)\,e_2\bigr)
    \wedge \bigl((dc_3/dz)\,e_3\bigr)
  \;=\;
  \Bigl(\prod_{k=1}^{3} \frac{dc_k}{dz}\Bigr)\,
  e_1 \wedge e_2 \wedge e_3
  \;\longmapsto\;
  \prod_{k=1}^{3} \frac{dc_k}{dz}
$$

under the identification $e_1 \wedge e_2 \wedge e_3 \mapsto 1$. This product structure arises solely from multilinearity of $\wedge$.

The squared Vandermonde of the colour-tube roots equals the cubic's discriminant ([color-tube cubic](#rem:color-tube-cubic)):

$$
  V_3(c_1, c_2, c_3)^2
  \;=\;
  \prod_{1 \leq i < j \leq 3} (c_i - c_j)^2
  \;=\;
  \Delta(z)
  \;\in\; R[z].
$$

Using implicit differentiation $dc_k/dz = -(\partial F/\partial z)|_{(z, c_k)} \big/ (\partial F/\partial c)|_{(z, c_k)}$ and the resultant identity $J(z) := \prod_{k=1}^{3} (\partial F/\partial c)|_{(z, c_k)} = \pm\, \Delta(z)$, the Alt-isotype representative satisfies

$$
  \prod_{k=1}^{3} \frac{dc_k}{dz}
  \;=\;
  (-1)^{3}\,
  \frac{V_3(c_1, c_2, c_3)}{J(z)}
  \;=\;
  \pm\,\frac{V_3(c_1, c_2, c_3)}{\Delta(z)}.
$$

Thus

$$
  \Bigl(\prod_{k=1}^{3} \frac{dc_k}{dz}\Bigr)^{2}
  \;=\;
  \frac{V_3(c_1, c_2, c_3)^2}{\Delta(z)^2}
  \;=\;
  \frac{1}{\Delta(z)}
  \;\in\; R(z),
$$

which is manifestly $R$-rational. $\square$

The sum $\sum_k dc_k/dz$ projects onto the trivial isotype $V_{(3)}$ as the integrand for a symmetric trion. The baryon sits in the antisymmetric colour singlet $\mathrm{Alt}^3$, selecting the wedge product. This algebraic selection requires no input from the Picard–Lefschetz machinery. Both the Vandermonde and $\pi_{\mathrm{Alt}}$ are defined over $R$; the baryon integrand evaluation remains $R$-rational until the archimedean fibre functor $\tau$ is applied.

This algebraic choice of the sign block, combined with the scalar weight $w_\lambda$ from the Markov trace ([categorical mass as Markov trace](#prop:categorical-mass-markov)), fully determines the baryon integrand $\lambda_{\mathrm{baryon}}$.

**Scope of the selection — derived versus input.** Two claims must be kept apart. That $\mathrm{Alt}^3$ is a *genuinely non-trivial* one-dimensional representation is **derived**: the monodromy of the color-tube cubic $F$ around its discriminant is the full $\mathrm{S}_3$, computed exactly over $R = \mathbb{Q}[z]$ (irreducibility over $\mathbb{C}(z)$ gives transitivity; the depressed quadratic is coprime to $\Delta$, so every one of the six simple branch points carries a transposition, and a transitive subgroup of $\mathrm{S}_3$ with a transposition is $\mathrm{S}_3$) and confirmed at $50$ digits by transporting the three sheets around all six branch points — every loop returns a transposition and the six generate $\mathrm{S}_3$ ([monodromy witness](../../../computations/probes/bring-cubic-monodromy-probe.witness.json)). Had the group been only $A_3$, the sign line would coincide with the trivial one and selecting $\mathrm{Alt}^3$ would carry no information; the surjectivity onto $\{\pm 1\}$ rules that out. What remains an **input** — not derived from the categorical substrate — is that the physical baryon *occupies* $\mathrm{Alt}^3$ rather than the trivial or standard isotype: this is the color-singlet (confinement) condition. Stating the occupation as a derivation would conflate an invariant of the fibre (the non-trivial sign line, which the geometry supplies) with the channel of the state (which it does not), and is the standing open item.
