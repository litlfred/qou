<!-- FILE_START: weight-decomposition-intro.md -->
Having identified $G \cong \mathrm{SU}(2)$ and labeled the simple objects $V_j$ by spin, we isolate the rank-one maximal torus $T \subset G$ that diagonalizes every $V_j$. This allows us to read off the weight decomposition of differential forms. The maximal torus is defined categorically as the largest subgroup acting diagonally on the weight subcategory of the fundamental object. This decomposition splits any form uniquely into a weight-zero (horizontal) component and a non-zero-weight (vertical) component. The horizontal forms, carrying integer spin, correspond geometrically to bosons, while mixed forms carry half-integer spin and correspond to fermions. This splitting establishes the geometric origin of spin-statistics directly from the categorical structure.
<!-- FILE_END: weight-decomposition-intro.md -->

<!-- FILE_START: maximal-torus.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with fundamental object $V$. The weight subcategory $\langle V \rangle \subset \mathbf{C}$ is the full subcategory whose objects are direct sums of the weight spaces of $V$. The **maximal torus** $T$ of the gauge group is the subgroup of natural automorphisms that act diagonally on each weight space of $V$:

$$
  T = \mathrm{Aut}^{\otimes}(\tau|_{\langle V \rangle}) \subset G.
$$

```tex
\begin{equation}\label{eq:maximal-torus-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  T \ar[r, hook] \ar[d, "\mathrm{diag}"']
  & G \ar[d] \\
  \mathrm{Aut}(\tau(V))
  & \mathrm{Aut}^{\otimes}(\tau) \ar[l]
\end{tikzcd}
\end{equation}
```

Equivalently, $T$ is the largest subgroup of $G$ under which every object in $\langle V \rangle$ decomposes into one-dimensional eigenspaces.
<!-- FILE_END: maximal-torus.md -->

<!-- FILE_START: maximal-torus-su2.md -->
For the fundamental representation $V = \mathbb{C}^2$ of $\mathrm{SU}(2)$, the weight decomposition is $V = \mathbb{C} e_+ \oplus \mathbb{C} e_-$. The weight subcategory $\langle V \rangle$ consists of representations that decompose strictly into these weight spaces. The maximal torus is therefore the diagonal subgroup $\mathrm{U}(1) \subset \mathrm{SU}(2)$, which acts on $e_{\pm}$ by $e^{\pm i\varTheta}$.
<!-- FILE_END: maximal-torus-su2.md -->

<!-- FILE_START: weight-decomposition.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with maximal torus $T$. The $T$-action extends to the non-commutative de Rham forms $\Omega^k(A)$, inducing a $\mathbb{Z}$-grading by weights. Let $\pi_H$ and $\pi_V$ denote the projections onto the weight-zero and non-zero-weight summands, respectively. This gives the **weight decomposition**, where every form $\alpha$ splits uniquely:

```tex
\begin{equation}\label{eq:weight-decomposition-cd}
\begin{tikzcd}[row sep=2em, column sep=3em]
  & \Omega^k(A) \ar[dl, "\pi_H"'] \ar[dr, "\pi_V"] & \\
  \Omega^k_H(A) \ar[rr, hook, "\oplus"']
  & & \Omega^k_V(A)
\end{tikzcd}
\qquad \alpha = \alpha_H + \alpha_V.
\end{equation}
```

The horizontal component $\alpha_H = \pi_H(\alpha)$ is invariant under $T$. The vertical component $\alpha_V = \pi_V(\alpha)$ carries non-zero weight. We say a form is purely horizontal if and only if $\alpha_V = 0$.
<!-- FILE_END: weight-decomposition.md -->

<!-- FILE_START: weight-decomposition-exists.md -->
For any quantum observable universe, the complementary projectors $\pi_H$ and $\pi_V$ exist on $\Omega^k(A)$ and satisfy $\pi_H + \pi_V = \mathrm{id}$, alongside the idempotency conditions $\pi_H^2 = \pi_H$ and $\pi_V^2 = \pi_V$.
<!-- FILE_END: weight-decomposition-exists.md -->

<!-- FILE_START: weight-decomposition-su2.md -->
For $\mathrm{SU}(2)$, the weight decomposition is constructed explicitly via torus averaging. The maximal torus $T = \mathrm{U}(1)$ acts on the coordinate ring $A = \mathcal{O}(\mathrm{SU}(2))$ by left translation. On the matrix generators $\alpha, \beta, \bar\alpha, \bar\beta$, the action is diagonal, rescaling each generator by a phase.

For any integer weight $m \in \mathbb{Z}$, the isotypic projector is the Fourier integral:

$$
  e_m(f) = \frac{1}{2\pi}\int_0^{2\pi}
    e^{-im\varTheta}\,(t_\varTheta \cdot f)\,d\varTheta.
$$

The horizontal projector is $\pi_H = e_0$, while the vertical projector is $\pi_V = \sum_{m \neq 0} e_m$. The decomposition extends to the differential forms $\Omega^k(A)$ via the Leibniz rule. Complementarity $\pi_H + \pi_V = \mathrm{id}$ follows from Fourier completeness, and idempotency from the orthogonality of characters.
<!-- FILE_END: weight-decomposition-su2.md -->

<!-- FILE_START: reeb-physical.md -->
The geometric decomposition $\alpha = \alpha_H + \alpha_V$ enforces the spin-statistics connection at the categorical level. Purely horizontal forms carry integer spin and act as bosons, while forms with non-trivial vertical components carry half-integer spin and act as fermions.
<!-- FILE_END: reeb-physical.md -->

