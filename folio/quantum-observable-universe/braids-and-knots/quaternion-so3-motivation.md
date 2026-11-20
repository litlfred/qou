The quaternionic basis used in the spectral resolvents is rigidly determined by the $\mathrm{SU}(2)$ structure group of the principal bundle.

The group of unit quaternions $\mathrm{Sp}(1) = \{\mathbf{q} \in \mathbb{H} : \lvert\mathbf{q}\rvert = 1\}$ is isomorphic to $\mathrm{SU}(2)$ via the matrix realization
$$
  a + b\mathbf{i} + c\mathbf{j} + d\mathbf{k}
   \longmapsto 
  \begin{pmatrix} a + bi & -c + di \\ c + di & a - bi \end{pmatrix},
$$
which maps the Pauli generators $e_a$ to the half-quaternion basis $\frac{1}{2}\mathbf{i}, \frac{1}{2}\mathbf{j}, \frac{1}{2}\mathbf{k}$. Under the commutator bracket $[p, q] = pq - qp$, the purely imaginary subspace $\mathrm{Im}\mathbb{H}$ forms a three-dimensional Lie algebra whose structure constants in the half-quaternion basis satisfy $[e_a, e_b] = \epsilon_{abc}e_c$.

Conjugation by a unit quaternion $\mathbf{q}$ acts on $\mathrm{Im}\mathbb{H} \cong \mathbb{R}^3$ by orientation-preserving rotation,
$$
  \mathrm{Ad}_{\mathbf{q}}\colon
  \mathbf{v}  \longmapsto  \mathbf{q}\mathbf{v}\mathbf{q}^{*}.
$$
This adjoint action realizes the universal double cover $\mathrm{Sp}(1) \twoheadrightarrow \mathrm{SO}(3)$, so the $\mathrm{SO}(3)$ holonomy of the chiral sheets lifts canonically to $\mathrm{Sp}(1)$ conjugation in the quaternion basis. Expanding spectral resolvents in the $\{\mathbf{i}, \mathbf{j}, \mathbf{k}\}$ basis therefore coincides with expanding an $\mathfrak{su}(2)$-valued one-form along the structure group's Lie algebra generators, and the spatial-temporal decomposition $(\omega_1 \mid \omega_2, \omega_3)$ reflects the Cartan splitting $\mathfrak{su}(2) \cong \mathfrak{u}(1) \oplus \mathfrak{m}$.
