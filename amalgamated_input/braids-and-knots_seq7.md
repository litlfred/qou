<!-- FILE_START: su2-so3-intro.md -->
The groups $\mathrm{SU}(2)$ and $\mathrm{SO}(3)$ serve as the natural gauge groups on the substrate and archimedean sides, respectively. We fix their bases, clarify the first-order Taylor relation between their generators, and establish the quaternionic picture of $\mathrm{SO}(3)$ necessary for identifying $\mathrm{SU}_q(2)$ as the substrate deformation of $\mathrm{SU}(2)$.
<!-- FILE_END: su2-so3-intro.md -->

<!-- FILE_START: su2-basis.md -->
Write $\tau_1,\tau_2,\tau_3$ for the Pauli matrices and define the basis:
```tex
\begin{equation}\label{eq:su2-basis}
  e_a=-\tfrac{i}{2}\tau_a,\qquad a=1,2,3.
\end{equation}
```
The Lie bracket is:
```tex
\begin{equation}\label{eq:su2-commutator}
  [e_a,e_b]=\epsilon_{abc}e_c.
\end{equation}
```
<!-- FILE_END: su2-basis.md -->

<!-- FILE_START: first-order-taylor.md -->
The Lie bracket captures the first-order behaviour of the group operation. For elements $A,B$ near the identity:
$$
  e^A e^B =  e^{A+B+\tfrac{1}{2}[A,B]+\cdots}.
$$
The commutator $[e_a,e_b]$ acts as the first-order Taylor polynomial of the non-commutativity. Higher-order corrections forming the full Baker--Campbell--Hausdorff series encode the complete nonlinear group law.
<!-- FILE_END: first-order-taylor.md -->

<!-- FILE_START: so3-generators.md -->
Under the adjoint map to $\mathrm{SO}(3)$, the generators of $\mathrm{Dic}_3$ have images:
```tex
\begin{equation}\label{eq:so3-generators}
  R_\alpha
  =\begin{pmatrix}
    -\frac{1}{2}&-\frac{\sqrt{3}}{2}&0\\[3pt]
    \frac{\sqrt{3}}{2}&-\frac{1}{2}&0\\[3pt]
    0&0&1
  \end{pmatrix},\qquad
  R_\beta
  =\begin{pmatrix}
    1&0&0\\[2pt]
    0&-1&0\\[2pt]
    0&0&-1
  \end{pmatrix}.
\end{equation}
```
The operator $R_\alpha$ is a $2\pi/3$ rotation about the $e_3$-axis representing a 3-cycle, and $R_\beta$ is a $\pi$ rotation about $e_1$ representing a 2-cycle.
<!-- FILE_END: so3-generators.md -->

<!-- FILE_START: quaternion-so3-motivation.md -->
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

Thus, writing spectral resolvents in the $\{\mathbf{i}, \mathbf{j}, \mathbf{k}\}$ basis equates to expanding an $\mathfrak{su}(2)$-valued $1$-form along the structure group's Lie algebra generators. The spatial-temporal decomposition $(\omega_1 \mid \omega_2, \omega_3)$ corresponds perfectly to splitting $\mathfrak{su}(2) \cong \mathfrak{u}(1) \oplus \mathfrak{m}$ into the Cartan subalgebra and its orthogonal complement.
<!-- FILE_END: quaternion-so3-motivation.md -->

