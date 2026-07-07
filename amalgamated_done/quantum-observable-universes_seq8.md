<!-- FILE_START: differential-structures-fiber-adjoint-intro.md -->
We now introduce the fibre-adjoint involution, closing the differential-structure machinery. This involution provides the projector onto coadjoint orbits and governs the substrate's radial coordinate. We first establish the fibre-functor atlas and define the involution. We then extract the radial coordinate, confirm its well-definedness under the Reeb flow, and specialize the involution to $\mathrm{SU}(2)$ in preparation for constructing the connection.
<!-- FILE_END: differential-structures-fiber-adjoint-intro.md -->

<!-- FILE_START: fibre-functor-atlas.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with gauge group $G$. Every fibre functor $\tau' \colon \mathbf{C} \to \mathbf{Vect}_R$ serves as an affine chart, realizing the abstract categorical data over $R$. The canonical functor $\tau$ yields the contact affine chart on $\mathbb{P}(V)$. For any two fibre functors, the space of monoidal natural isomorphisms forms a $G$-torsor; each isomorphism acts as a transition function changing affine coordinates. Functorial composition automatically enforces the cocycle condition. Consequently, the category of all fibre functors forms a $G$-gerbe, serving as the affine atlas of the quantum universe.
<!-- FILE_END: fibre-functor-atlas.md -->

<!-- FILE_START: substrate-radial-coordinate.md -->
Within the contact affine chart $U_\xi$, the substrate parameter $q$ governs the radial coordinate. As $q \to \infty$ in the deep-quantum limit, the affine coordinate $Z \to 0$. Conversely, as $q \to 1$ at the classical boundary, $Z \to \infty$. The $q$-deformed Reeb flow rotates the phase of $Z$ according to:

$$
  \mathcal{L}_\xi Z =  J\hbar_q Z,
$$

where $\hbar_q = 1 - q^{-1}$ is the quantum Planck constant and $J$ is the complex structure on the horizontal distribution $H$.
<!-- FILE_END: substrate-radial-coordinate.md -->

<!-- FILE_START: fiber-adjoint-involution.md -->
The Frobenius form $\int_A \colon A \to \mathbf{1}$ induces an isomorphism $A \xrightarrow{ \sim } A^{\vee}$. Under this self-duality, the projective line object $\mathbb{P}(V)$ embeds into the adjoint object $\mathrm{Ad}(A)$ as the coadjoint orbit of a highest-weight vector. This assignment $\sigma \colon \mathbb{P}(V) \hookrightarrow \mathrm{Ad}(A)$ is an involution, entirely determining $\mathbb{P}(V)$ from $\mathrm{Ad}(A)$ and vice versa. The non-degeneracy of the Frobenius pairing then forces the observability condition $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$.

```tex
\begin{equation}\label{eq:fiber-adjoint-involution-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \mathbb{P}(V)
    \ar[r, hook, "\sigma"]
    \ar[d, "\cong"']
  & \mathrm{Ad}(A)
    \ar[d, "\cong", "\int_A"'] \\
  G/T
    \ar[r, hook, "\text{coadjoint orbit}"]
  & A^{\vee}
\end{tikzcd}
\end{equation}
```
<!-- FILE_END: fiber-adjoint-involution.md -->

<!-- FILE_START: fai-projector-coadjoint-orbit.md -->
Let $V \in \mathbf{C}$ be the standard representation, and let $\rho \colon V \to V$ be a rank-1 projector. The traceless component $\sigma(\rho) = \rho - \tfrac{1}{2}\mathrm{id}_V \in \mathrm{Ad}(A)$ satisfies the involution $(2\sigma(\rho))^2 = \mathrm{id}_V$. This map $\sigma$ identifies $\mathbb{P}(V) \cong G/T$ with a closed coadjoint orbit in $\mathrm{Ad}(A)$.
<!-- FILE_END: fai-projector-coadjoint-orbit.md -->

<!-- FILE_START: fiber-adjoint-su2.md -->
For $G = \mathrm{SU}(2)$ and $V = \mathbb{C}^2$, the projective line is $\mathbb{P}^1(\mathbb{C})$, and the adjoint object is $\mathfrak{su}(2) \cong \mathbb{R}^3$. The embedding $\sigma$ maps a line $\ell = \mathrm{span}(v)$ to the traceless projector:

$$
  \sigma([\ell]) =
  \frac{v v^{\dagger}}{\lVert v \rVert^2}
  - \tfrac{1}{2}\mathrm{id}_V
  \in \mathfrak{su}(2).
$$

This identifies $\mathbb{P}^1(\mathbb{C})$ with the unit 2-sphere $S^2 \subset \mathfrak{su}(2)$, the coadjoint orbit of $\tfrac{1}{2}\mathrm{diag}(i, -i)$. Observability immediately follows: any $G$-fixed point in $\mathfrak{su}(2)$ would be a scalar matrix, but the only traceless scalar is zero, ensuring $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$.
<!-- FILE_END: fiber-adjoint-su2.md -->

<!-- FILE_START: connection-su2.md -->
On $A = \mathcal{O}(\mathrm{SU}(2))$ with its left-invariant calculus $\Omega^1(A) = \mathrm{span}\{\omega_1, \omega_2, \omega_3\}$, a connection is a covariant derivative $\nabla f = df + \mathcal{A} \cdot f$, where $\mathcal{A} \in \Omega^1(A)$ is the connection 1-form. It satisfies the Leibniz rule $\nabla(fg) = (\nabla f)g + f(dg)$. The curvature $F_\nabla = d\mathcal{A} + \mathcal{A} \wedge \mathcal{A} \in \Omega^2(A)$ is strictly $A$-linear. Upon deformation by $q$, this differential structure lifts to the Woronowicz left-covariant calculus on $\mathcal{O}_q(\mathrm{SU}(2))$. We use the left-covariant formulation explicitly, as the failure of bi-covariance controls the deformation of the exterior derivative.
<!-- FILE_END: connection-su2.md -->
