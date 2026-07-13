<!-- FILE_START: su2-emergence-example.md -->
Consider the representation category $\mathbf{C} = \mathrm{Rep}(\mathrm{SU}(2))$ with the standard forgetful functor $\tau$. The volume constraint requires $\det(g_V) = 1$. Specifically, the alternating form $\epsilon(v \wedge w) = v_1 w_2 - v_2 w_1$ on $V = \mathbb{C}^2$ is $\mathrm{SU}(2)$-invariant. Any tensor automorphism $g$ must preserve $\epsilon$, forcing $g_V \in \mathrm{SL}(2, \mathbb{C})$. The dagger structure enforces unitarity, $g_V^{-1} = g_V^{\dagger}$, reducing the group from $\mathrm{SL}(2, \mathbb{C})$ to its compact real form $\mathrm{SU}(2)$. We conclude that $G = \mathrm{Aut}^{\otimes}(\tau) \cong \mathrm{SU}(2)$, recovering the gauge group entirely from the categorical axioms.
<!-- FILE_END: su2-emergence-example.md -->

<!-- FILE_START: spin-labels.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe. Because $G = \mathrm{Aut}^{\otimes}(\tau) \cong \mathrm{SU}(2)$, the simple objects of $\mathbf{C}$ are indexed by a spin label $j \in \{0, \tfrac12, 1, \tfrac32, \ldots\}$, with $V_j$ denoting the simple object of categorical dimension $2j + 1$. The fundamental object is $V = V_{1/2}$, the unique simple object of dimension 2. The adjoint object is $V_1 \cong \mathrm{Ad}(A)$, of dimension 3.

```tex
\begin{equation}\label{eq:spin-labels-diagram}
\begin{tikzcd}[column sep=2em]
  V_0 = \mathbf{1} & V_{1/2} = V & V_1 = \mathrm{Ad}(A) & V_{3/2} & \cdots
\end{tikzcd}
\qquad (\dim V_j = 2j+1)
\end{equation}
```
<!-- FILE_END: spin-labels.md -->

<!-- FILE_START: spin-labels-su2.md -->
For $\mathbf{C} = \mathrm{Rep}(\mathrm{SU}(2))$, the simple objects are the irreducible representations $V_j \cong \mathbb{C}^{2j+1}$:

```tex
\begin{equation}\label{eq:spin-decomposition}
\begin{tikzcd}[row sep=1.5em, column sep=1.5em]
  V_0 \ar[d, phantom, "\cong"] & V_{1/2} \ar[d, phantom, "\cong"]
    & V_1 \ar[d, phantom, "\cong"] & V_{3/2} \ar[d, phantom, "\cong"]
    & \cdots \\
  \mathbb{C} & \mathbb{C}^2 & \mathbb{C}^3 & \mathbb{C}^4 & \cdots
\end{tikzcd}
\end{equation}
```

Concretely:
- $V_0 = \mathbb{C}$ is the trivial representation.
- $V_{1/2} = \mathbb{C}^2$ is the defining representation, functioning as the fundamental object $V$.
- $V_1 = \mathfrak{su}(2)_{\mathbb{C}} \cong \mathbb{C}^3$ is the adjoint representation, acting as $\mathrm{Ad}(A)$.
- $V_{3/2} = \mathrm{Sym}^3(\mathbb{C}^2) \cong \mathbb{C}^4$ corresponds to homogeneous cubics in two variables.

Every finite-dimensional representation decomposes as $W \cong \bigoplus_j V_j^{\oplus m_j}$. The polynomial ring $\mathbb{C}[z] = \bigoplus_{n \geq 0} \mathrm{Sym}^n V$ serves as the coordinate ring of the projective line $\mathbb{P}(V)$, where each homogeneous component $\mathrm{Sym}^n V \cong V_{n/2}$ is an irreducible representation of dimension $n + 1$.
<!-- FILE_END: spin-labels-su2.md -->

<!-- FILE_START: spin-half-representation.md -->
Once the categorical gauge group is identified as $\mathrm{SU}(2)$, the abstract fundamental object $V$ acquires its concrete incarnation as the spin-$\tfrac{1}{2}$ representation:

$$
  V_{1/2} = \tau(V) \cong \mathbb{C}^2.
$$

The standard basis $\{e_+, e_-\}$ of $V_{1/2}$ consists of weight vectors for the maximal torus $T \subset \mathrm{SU}(2)$:

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

splits the tensor square into the antisymmetric singlet $\Lambda^2 V_{1/2}$ and the symmetric triplet $\mathrm{Sym}^2 V_{1/2}$. This exemplifies tensor generation: all simple objects $V_j$ arise as summands of $V_{1/2}^{\otimes 2j}$.
<!-- FILE_END: spin-half-representation.md -->
