<!-- FILE_START: differential-structures-fiber-adjoint-intro.md -->
The preceding sub-section developed the categorical Reeb derivation
and its projective-line / contact-affine setup. This sub-section
introduces the fibre-adjoint involution that the Reeb derivation
consumes: the projector onto coadjoint orbits, the substrate's
radial coordinate (with proof), and the involution's SU(2)
specialisation. The blocks close out the differential-structure
machinery and prepare the substrate-radial coordinate's role in
the SU(2) connection construction (next section).

The arc proceeds in two layers.  The first half fixes the
fibre-adjoint involution and its existence-uniqueness pair, and
records the projector onto coadjoint orbits that drives the
substrate-radial decomposition.  The second half exhibits the
substrate-radial coordinate with its proof of well-definedness,
specialises the involution to $\mathrm{SU}(2)$ for the concrete
case, and closes with the construction's interface to the next
section's connection blocks.
<!-- FILE_END: differential-structures-fiber-adjoint-intro.md -->

<!-- FILE_START: fibre-functor-atlas.md -->
**Proposition.**
*Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe
with $G = \mathrm{Aut}^{\otimes}(\tau)$
([Tannaka–Krein](#rem:tannaka-krein-overview)). In the following,
$\tau', \tau''$ denote arbitrary fibre functors on $\mathbf{C}$
(not the canonical $\tau$). Then:*

1. **(Charts.)** *Each fibre functor
 $\tau' \colon \mathbf{C} \to \mathbf{Vect}_R$ is an
 affine chart: a concrete realisation of the abstract
 categorical data as linear algebra over $R$. The contact
 affine chart on $\mathbb{P}(V)$
 ([contact affine chart](#def:contact-affine-chart)) is the
 chart associated to the canonical fibre functor $\tau$.*

2. **(Transitions.)** *For any two fibre functors
 $\tau', \tau''$, the set of monoidal natural isomorphisms
 $\tau' \xrightarrow{\sim} \tau''$ is a $G$-torsor. Each
 such isomorphism is a transition function: a change of
 affine coordinates relating the two observers' descriptions
 of the same categorical data.*

3. **(Cocycle condition.)** *Given three fibre functors
 $\tau', \tau'', \tau'''$ with transition isomorphisms
 $g_{01}, g_{12}, g_{02}$, functoriality of composition
 forces $g_{02} = g_{12} \circ g_{01}$. The cocycle
 condition is not imposed — it is automatic.*

4. **(Atlas.)** *The category of all fibre functors on
 $\mathbf{C}$, with monoidal natural isomorphisms as
 morphisms, is a $G$-gerbe: a connected groupoid on which
 $G$ acts transitively. This is the **affine atlas**
 of the quantum observable universe.*
<!-- FILE_END: fibre-functor-atlas.md -->

<!-- FILE_START: substrate-radial-coordinate.md -->
Within the contact affine chart $U_\xi$
([contact affine chart](#def:contact-affine-chart)), the substrate
parameter $q$ ([substrate parameter](#def:substrate-parameter))
governs the radial and phase coordinates of the state. Let $Z$ be the
affine coordinate of a state. Then $Z \to 0$ as $q \to \infty$
(deep-quantum origin) and $Z \to \infty$ as $q \to 1$ (classical
boundary). The $q$-deformed Reeb flow rotates the phase of $Z$:

$$
  \mathcal{L}_\xiZ =  J\hbar_qZ,
$$

where $\hbar_q = 1 - q^{-1}$
([quantum Planck constant](#def:quantum-planck-constant)) and $J$ is
the complex structure on $H$.
<!-- FILE_END: substrate-radial-coordinate.md -->

<!-- FILE_START: fiber-adjoint-involution.md -->
Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def:quantum-observable-universe)). The Frobenius form
$\int_A \colon A \to \mathbf{1}$ induces an isomorphism
$A \xrightarrow{ \sim } A^{\vee}$ (the Frobenius self-duality), under
which:

1. the projective line object $\mathbb{P}(V)$
   ([projective line object](#def:projective-line-object)) embeds in the adjoint
   object $\mathrm{Ad}(A)$ as the coadjoint orbit of a highest-weight
   vector;
2. the assignment $\sigma \colon \mathbb{P}(V) \hookrightarrow \mathrm{Ad}(A)$ is an involution in the sense that $\sigma$
   determines $\mathbb{P}(V)$ from $\mathrm{Ad}(A)$ and vice versa;
3. the non-degeneracy of the [Frobenius pairing](#def:frobenius-pairing) forces the
   observability condition:

   $$
     \mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0.
   $$

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
\qquad\text{(fibre--adjoint involution)}
\end{equation}
```
<!-- FILE_END: fiber-adjoint-involution.md -->

<!-- FILE_START: fai-projector-coadjoint-orbit.md -->
**Lemma.**
*Let $V \in \mathbf{C}$ be the standard representation (categorical
dimension $2$), and let $\rho \colon V \to V$ be a rank-$1$ projector.
The traceless component
$\sigma(\rho) = \rho - \tfrac{1}{2}\mathrm{id}_V \in \mathrm{Ad}(A)$
satisfies $(2\sigma(\rho))^2 = \mathrm{id}_V$ (an involution), and
$\sigma$ identifies $\mathbb{P}(V) \cong G/T$ with a closed
coadjoint orbit in $\mathrm{Ad}(A)$.*
<!-- FILE_END: fai-projector-coadjoint-orbit.md -->

<!-- FILE_START: fiber-adjoint-su2.md -->
Continuing [projective line on $\mathrm{SU}(2)$](#ex:projective-line-su2), take
$G = \mathrm{SU}(2)$, $T = \mathrm{U}(1)$, and
$V = \mathbb{C}^2$. The projective line object is
$\mathbb{P}(V) = \mathbb{P}^1(\mathbb{C})$, and the adjoint object is
$\mathrm{Ad}(A) \cong \mathfrak{su}(2) \cong \mathbb{R}^3$
(trace-free skew-Hermitian $2 \times 2$ matrices under the Killing
form). The embedding $\sigma$ sends a line
$\ell = \mathrm{span}(v) \subset \mathbb{C}^2$ to the rank-$1$
projector

$$
  \sigma([\ell]) =
  \frac{v v^{\dagger}}{\lVert v \rVert^2}
  - \tfrac{1}{2}\mathrm{id}_V
  \in \mathfrak{su}(2).
$$

This identifies $\mathbb{P}^1(\mathbb{C})$ with the unit $2$-sphere
$S^2 \subset \mathfrak{su}(2)$ (the coadjoint orbit of
$\tfrac{1}{2}\mathrm{diag}(i, -i)$). Observability follows:
a $G$-fixed point in $\mathfrak{su}(2)$ would be a matrix commuting
with all of $\mathrm{SU}(2)$, hence a scalar --- but trace-free matrices
have no non-zero scalars, so
$\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$.
<!-- FILE_END: fiber-adjoint-su2.md -->

<!-- FILE_START: connection-su2.md -->
Continuing [fibre adjoint on $\mathrm{SU}(2)$](#ex:fiber-adjoint-su2), take
$A = \mathcal{O}(\mathrm{SU}(2))$ with its left-invariant calculus
$\Omega^1(A) = \mathrm{span}\{\omega_1, \omega_2, \omega_3\}$
([higher forms on $\mathrm{SU}(2)$](#ex:higher-forms-su2)). A
connection is a covariant derivative
$\nabla f = df + \mathcal{A} \cdot f$ for $f \in A$, where
$\mathcal{A} = A_1\omega_1 + A_2\omega_2 + A_3\omega_3$ is the
connection $1$-form. The Leibniz triangle says
$\nabla(fg) = (\nabla f)g + f(dg)$. The curvature is the $2$-form
$F_\nabla = d\mathcal{A} + \mathcal{A} \wedge \mathcal{A} \in \Omega^2(A)$,
which is $A$-linear ($F_\nabla(f \cdot s) = f \cdot F_\nabla(s)$).
(When the substrate parameter $q$ is introduced in
[substrate parameter](#def:substrate-parameter), this calculus deforms to the
Woronowicz left-covariant $3D$ differential calculus on
$\mathcal{O}_q(\mathrm{SU}(2))$ \cite{woronowicz1987-twisted-su2}.  We rely
throughout on the \emph{left-covariant} (left-invariant) $3D$ calculus
of \cite{woronowicz1987-twisted-su2}; this calculus is not bi-covariant,
and the distinction matters for the deformation theory of $d$ away from
the classical limit $q = 1$.)
<!-- FILE_END: connection-su2.md -->

