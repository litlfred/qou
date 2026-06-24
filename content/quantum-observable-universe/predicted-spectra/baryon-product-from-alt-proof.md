**Step 1 (Schur–Weyl decomposition of the colour tangent module).**
*By Schur–Weyl duality at level $n = 3$ in three dimensions
([Schur–Weyl mass decomposition](#prop:schur-weyl-mass-decomposition)),
the $\mathrm{S}_3$-module*

$$
  V \;:=\; \bigotimes_{k=1}^{3}\, T_{c_k}\mathbf{C}
  \;\cong\; R\,\langle dc_1/dz,\ dc_2/dz,\ dc_3/dz\rangle
$$

*decomposes into isotypic components labelled by partitions of $3$:*

$$
  V \;\cong\; V_{(3)} \;\oplus\; V_{(1,1,1)} \;\oplus\; V_{(2,1)}
  \;=\; \mathrm{Sym}^3 \;\oplus\; \mathrm{Alt}^3 \;\oplus\; \mathrm{Std}^{\oplus 2},
$$

*with $\dim_R V_{(3)} = 1$, $\dim_R V_{(1,1,1)} = 1$,
$\dim_R V_{(2,1)} = 2$, summing to $4$ — but here $V$ is the
rank-$3$ permutation representation of $\mathrm{S}_3$, so $V \cong
V_{(3)} \oplus V_{(2,1)}$ and the rank-$1$ alternating piece sits
inside the *exterior cube* $\Lambda^3 V$.  The relevant isotype is
therefore not $V$ itself but its top exterior power.*

**Step 2 (Alt-projector via the Frobenius character formula).**
*By the Frobenius character formula
([Frobenius universal](#thm:frobenius-codim-universal)) applied
to $\mathrm{S}_3$, the projector onto the sign isotype of any
$\mathrm{S}_3$-module $W$ is*

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

*Applied to the rank-$3$ tensor
$dc_1/dz \otimes dc_2/dz \otimes dc_3/dz \in V^{\otimes 3}$,
this projector returns the antisymmetrisation*

$$
  \pi_{\mathrm{Alt}}\bigl(dc_1/dz \otimes dc_2/dz \otimes dc_3/dz\bigr)
  \;=\;
  \frac{1}{6} \sum_{\sigma \in \mathrm{S}_3}
    \mathrm{sgn}(\sigma)\,
    \bigotimes_{k=1}^{3} dc_{\sigma(k)}/dz.
$$

**Step 3 (Identification with the wedge product).**
*Under the canonical isomorphism
$\Lambda^3 V \cong R$ (top exterior power of a rank-$3$ free module
over $R$ has rank $1$), the antisymmetrised tensor maps to the
wedge product*

$$
  (dc_1/dz) \wedge (dc_2/dz) \wedge (dc_3/dz),
$$

*which, evaluated on the diagonal vector $\bigl((dc_k/dz)\,e_k\bigr)_{k=1}^{3}$
(where $e_1, e_2, e_3$ is the chosen $R$-basis of $V$), gives*

$$
  \bigl((dc_1/dz)\,e_1\bigr) \wedge \bigl((dc_2/dz)\,e_2\bigr)
    \wedge \bigl((dc_3/dz)\,e_3\bigr)
  \;=\;
  \Bigl(\prod_{k=1}^{3} \frac{dc_k}{dz}\Bigr)\,
  e_1 \wedge e_2 \wedge e_3
  \;\longmapsto\;
  \prod_{k=1}^{3} \frac{dc_k}{dz}
$$

*under the basis identification $e_1 \wedge e_2 \wedge e_3 \mapsto 1$.
Note that this is a top exterior power on the rank-$3$ free module $V$
— not a Jacobian determinant of the (scalar-input) root map
$z \mapsto (c_1(z), c_2(z), c_3(z))$, whose differential is a
$3 \times 1$ matrix.  The product structure arises purely from
multilinearity of $\wedge$, not from any change-of-variables identity.*

**Step 4 (Discriminant identity for the Vandermonde square).**
*The squared Vandermonde of the colour-tube roots equals the cubic's
discriminant
([color-tube cubic](#rem:color-tube-cubic)):*

$$
  V_3(c_1, c_2, c_3)^2
  \;=\;
  \prod_{1 \leq i < j \leq 3} (c_i - c_j)^2
  \;=\;
  \Delta(z)
  \;\in\; R[z].
$$

*Combining this with implicit differentiation
$dc_k/dz = -(\partial F/\partial z)|_{(z, c_k)} \big/
(\partial F/\partial c)|_{(z, c_k)}$ along each colour sheet, and
the resultant identity
$J(z) := \prod_{k=1}^{3} (\partial F/\partial c)|_{(z, c_k)}
= \pm\, \Delta(z)$ for the monic cubic $F(z, \cdot)$, the Alt-isotype
representative satisfies*

$$
  \prod_{k=1}^{3} \frac{dc_k}{dz}
  \;=\;
  (-1)^{3}\,
  \frac{V_3(c_1, c_2, c_3)}{J(z)}
  \;=\;
  \pm\,\frac{V_3(c_1, c_2, c_3)}{\Delta(z)},
$$

*so that*

$$
  \Bigl(\prod_{k=1}^{3} \frac{dc_k}{dz}\Bigr)^{2}
  \;=\;
  \frac{V_3(c_1, c_2, c_3)^2}{\Delta(z)^2}
  \;=\;
  \frac{1}{\Delta(z)}
  \;\in\; R(z),
$$

*a manifestly $R$-rational quantity.
$\qquad\blacksquare$
