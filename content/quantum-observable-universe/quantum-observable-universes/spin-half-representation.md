After [$\mathrm{SU}(2)$ emergence](#thm:su2-emergence) identifies
$G = \mathrm{Aut}^{\otimes}(\tau) \cong \mathrm{SU}(2)$, the abstract
fundamental object $V$ acquires its concrete incarnation as the
*spin-$\tfrac{1}{2}$ representation*:

$$
  V_{1/2} =  \tau(V)  \cong  \mathbb{C}^2,
$$

the defining two-dimensional representation of $\mathrm{SU}(2)$.

The [spin label](#prop:spin-labels) indexing $j \in \{0, \tfrac{1}{2}, 1, \tfrac{3}{2}, \ldots\}$ identifies each simple object $V_j$ with
the unique irreducible representation of $\mathrm{SU}(2)$ of dimension
$2j+1$. In particular:

- $V_0 = \mathbf{1}$ (the trivial representation),
- $V_{1/2} = V \cong \mathbb{C}^2$ (the fundamental representation),
- $V_1 = \mathrm{Ad}(A) \cong \mathfrak{su}(2) \cong \mathbb{R}^3$
  (the adjoint representation).

The standard basis $\{e_+, e_-\}$ of $V_{1/2}$ consists of
weight vectors for the maximal torus $T \subset \mathrm{SU}(2)$:

$$
  T \cdot e_{\pm} =  e^{\pm i\varTheta} e_{\pm},
  \qquad
  T = \left\{\!
    \begin{pmatrix} e^{i\varTheta} & 0 \\ 0 & e^{-i\varTheta} \end{pmatrix}
  \right\}.
$$

The Clebsch--Gordan decomposition

$$
  V_{1/2} \otimes V_{1/2}
   \cong 
  V_0  \oplus  V_1
$$

decomposes the tensor square into the singlet (antisymmetric,
$\Lambda^2 V_{1/2}$) and the triplet (symmetric,
$\mathrm{Sym}^2 V_{1/2}$). This is the simplest instance of
[tensor generation](#rem:simple-objects-V): all $V_j$ arise as
summands of $V_{1/2}^{\otimes 2j}$.
