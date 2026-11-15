The quaternionic basis used in the spectral resolvents is rigidly determined by the $\mathrm{SU}(2)$ structure group of the principal bundle.

First, the unit quaternions $\mathrm{Sp}(1) = \{\mathbf{q} \in \mathbb{H} : \lvert\mathbf{q}\rvert = 1\}$ are isomorphic to $\mathrm{SU}(2)$ via:
$$
  a + b\mathbf{i} + c\mathbf{j} + d\mathbf{k}
   \longmapsto 
  \begin{pmatrix} a + bi & -c + di \\ c + di & a - bi \end{pmatrix}.
$$
This maps the Pauli generators $e_a$ to the half-quaternion basis $\frac{1}{2}\mathbf{i}, \frac{1}{2}\mathbf{j}, \frac{1}{2}\mathbf{k}$.

Second, the purely imaginary quaternions $\mathrm{Im}\mathbb{H}$ form a $3$-dimensional Lie algebra under the commutator bracket $[p, q] = pq - qp$. In the half-quaternion basis, the structure constants exactly match $[e_a, e_b] = \epsilon_{abc}e_c$.

Third, conjugation by a unit quaternion $\mathbf{q}$ acts on $\mathrm{Im}\mathbb{H} \cong \mathbb{R}^3$ via orientation-preserving rotation:
$$
  \mathrm{Ad}_{\mathbf{q}}\colon
  \mathbf{v}  \longmapsto  \mathbf{q}\mathbf{v}\mathbf{q}^{*}.
$$
This adjoint representation is the double cover $\mathrm{Sp}(1) \twoheadrightarrow \mathrm{SO}(3)$. The $\mathrm{SO}(3)$ holonomy of the chiral sheets lifts directly to $\mathrm{Sp}(1)$ conjugation in the quaternion basis.

Thus, writing spectral resolvents in the $\{\mathbf{i}, \mathbf{j}, \mathbf{k}\}$ basis equates to expanding an $\mathfrak{su}(2)$-valued $1$-form along the structure group's Lie algebra generators. The spatial-temporal decomposition $(\omega_1 \mid \omega_2, \omega_3)$ corresponds exactly to splitting $\mathfrak{su}(2) \cong \mathfrak{u}(1) \oplus \mathfrak{m}$ into the Cartan subalgebra and its orthogonal complement.
