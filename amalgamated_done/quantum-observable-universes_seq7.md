<!-- FILE_START: differential-structures-intro.md -->
We now develop the first-order differential structure on the Frobenius--Hopf object $A$. This machinery includes the categorical Reeb derivation, the projective-line object, the affine chart it carries, and the fibre-adjoint involution. None of these structures are imposed externally; each is forced by the QOU axioms. We construct the categorical Reeb derivation $(\xi, \varTheta_A)$ from the weight decomposition and realize it physically within the left-covariant calculus. The function-algebra quotient then forms the projective line object, which carries an intrinsic contact affine chart. Finally, the fibre-adjoint involution embeds the projective line as a coadjoint orbit, establishing the observability axiom directly from the Frobenius pairing.
<!-- FILE_END: differential-structures-intro.md -->

<!-- FILE_START: categorical-reeb.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with maximal torus $T$ and weight decomposition $\pi_H, \pi_V$. The **categorical Reeb derivation** is the endomorphism $\xi \colon A \to A$ generating the $T$-action. It acts as the infinitesimal generator of $T \subset G$ via the adjoint coaction. It satisfies three conditions. First, it generates vertical forms: $\pi_V \circ d = \iota_\xi d\varTheta_A$, where $\varTheta_A \in \Omega^1(A)$ is the canonical $1$-form dual to $\xi$. Second, it is normalized: $\varTheta_A(\xi) = \mathrm{id}_{\mathbf{1}}$. Third, horizontal forms are precisely the kernel of contraction: $\Omega^k_H(A) = \ker(\iota_\xi)$.

```tex
\begin{equation}\label{eq:reeb-decomposition-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \Omega^k(A) \ar[r, "\pi_H"] \ar[d, "\pi_V"']
  & \Omega^k_H(A) \ar[d, hook] \\
  \varTheta_A \wedge \Omega^{k-1}_H(A) \ar[r, hook]
  & \Omega^k(A)
\end{tikzcd}
\end{equation}
```
<!-- FILE_END: categorical-reeb.md -->

<!-- FILE_START: categorical-reeb-exists.md -->
For any quantum observable universe, there exists a unique categorical Reeb derivation $(\xi, \varTheta_A)$ on $A$ satisfying the vertical-generator constraint $\pi_V \circ d = \iota_\xi d\varTheta_A$ and the normalization constraint $\varTheta_A(\xi) = \mathrm{id}_{\mathbf{1}}$.

```tex
\begin{equation}\label{eq:reeb-exists-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  A \ar[r, "\xi"] \ar[d, "d"']
  & A \ar[d, "\varTheta_A"] \\
  \Omega^1(A) \ar[r, "\iota_\xi"']
  & A
\end{tikzcd}
\end{equation}
```
<!-- FILE_END: categorical-reeb-exists.md -->

<!-- FILE_START: categorical-reeb-unique.md -->
The vertical-generator and normalization axioms together fix the derivation along the vertical distribution corresponding to the free $T$-action. The dual form is then uniquely determined by extending to the horizontal distribution via the Maurer--Cartan condition. Therefore, the categorical Reeb derivation is unique.
<!-- FILE_END: categorical-reeb-unique.md -->

<!-- FILE_START: reeb-su2.md -->
For $G = \mathrm{SU}(2)$, the maximal torus $T = \mathrm{U}(1)$ has the generator $\xi = \frac{1}{2}\begin{smallmatrix} 1 & 0 \\ 0 & -1 \end{smallmatrix} \in \mathfrak{su}(2)$. On $A = \mathcal{O}(\mathrm{SU}(2))$, $\xi$ acts as the left-invariant vector field. The canonical $1$-form is $\varTheta_A = \omega_3$, satisfying $\omega_3(\xi) = 1$. The horizontal forms are those with no $\omega_3$ component. In the archimedean realization on a CR manifold $(M, \varTheta)$, $\xi$ operates as the Reeb vector field with $\iota_\xi d\varTheta = 0$.
<!-- FILE_END: reeb-su2.md -->

<!-- FILE_START: categorical-reeb-brings.md -->
On the Bring coordinate ring $\mathcal{O}_q(\mathcal{B})$, we construct the categorical Reeb derivation explicitly. The generator in $\mathfrak{su}(2)$ is $\xi = e_3$. On $A = \mathcal{O}_q(\mathrm{SU}(2))$, $\xi$ acts as the infinitesimal adjoint coaction, acting diagonally on the standard generators. This action defines a derivation. The dual form $\varTheta_A = \omega_3$ is the left-invariant basis element from the Woronowicz 3-dimensional calculus. Normalization holds by definition: $\omega_3(e_3) = 1$. The contact identity $\iota_\xi d\varTheta_A = 0$ follows from the Woronowicz structure equations $d\omega_3 = -q^{-1}\omega_+ \wedge \omega_-$. The $\xi$-action extends $S_5$-equivariantly to the coordinates of Bring's curve. The $8 = 2g$ independent cycles split into eigenspaces of $\xi$ with weights $+1$ and $-1$, precisely matching the fundamental modes.
<!-- FILE_END: categorical-reeb-brings.md -->

<!-- FILE_START: projective-line-object.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe. The **projective line object** is the quotient $\mathbb{P}(V) = G / T$, realized in the category via its function algebra $A^{\mathrm{co}T}$, the $T$-coinvariant subalgebra of $A$. Under the canonical fibre functor, it manifests as the scheme-theoretic projective line $\mathbb{P}^1(R)$.
<!-- FILE_END: projective-line-object.md -->

<!-- FILE_START: projective-line-su2.md -->
For $G = \mathrm{SU}(2)$, the quotient is $\mathbb{P}(V) = \mathrm{SU}(2)/\mathrm{U}(1) \cong \mathbb{P}^1(\mathbb{C})$. A point in $\mathbb{P}^1(\mathbb{C})$ represents a line in $V = \mathbb{C}^2$. The corresponding function algebra is the polynomial ring $\mathbb{C}[z]$ in the affine coordinate $z = v_1 / v_2$.
<!-- FILE_END: projective-line-su2.md -->

<!-- FILE_START: contact-affine-chart.md -->
Let $\mathbb{P}(V)$ be the projective line object. Using the Reeb decomposition, every form splits as $\alpha = \alpha_H + \varTheta \wedge \iota_\xi \alpha$. The **contact affine chart** $U_\xi \subset \mathbb{P}(V)$ is the open dense subset where the Reeb component is non-vanishing:

$$
  U_\xi =  \bigl\{ [\alpha] \in \mathbb{P}(V)
   \big|  \iota_\xi\alpha \neq 0 \bigr\}.
$$

On $U_\xi$, the affine coordinate $Z$ is defined as the ratio of the horizontal component to the vertical Reeb component:

$$
  Z([\alpha]) =  \frac{\alpha_H}{\iota_\xi\alpha}.
$$

```tex
\begin{equation}\label{eq:contact-affine-chart-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  U_\xi \ar[r, hook] \ar[d, "Z"']
  & \mathbb{P}(V) \ar[d, "\cong"] \\
  H = \ker\varTheta \ar[r, hook]
  & \Omega^1_H(A)
\end{tikzcd}
\end{equation}
```

The coordinate $Z$ takes values in the horizontal distribution $H$. The contact form and Reeb vector field thus supply the stereographic projection intrinsically, without external coordinates.
<!-- FILE_END: contact-affine-chart.md -->
