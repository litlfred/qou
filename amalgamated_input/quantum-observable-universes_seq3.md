<!-- FILE_START: su2-emergence-example.md -->
Continuing [Examples](#ex:frobenius-su2)--[Example](#ex:dagger-su2), let
$\mathbf{C} = \mathrm{Rep}(\mathrm{SU}(2))$,
$A = \mathcal{O}(\mathrm{SU}(2))$, $\tau$ the forgetful functor.

1. *Volume constraint* $\Rightarrow$ $\det(g_V) = 1$.
   The alternating form $\epsilon(v \wedge w) = v_1 w_2 - v_2 w_1$
   on $V = \mathbb{C}^2$ is $\mathrm{SU}(2)$-invariant. Any tensor
   automorphism $g$ preserves $\epsilon$, forcing
   $g_V \in \mathrm{SL}(2, \mathbb{C})$.
2. *Dagger structure* $\Rightarrow$ unitarity.
   The dagger on $\mathrm{Rep}(\mathrm{SU}(2))$
   ([dagger on $\mathrm{SU}(2)$](#ex:dagger-su2)) forces
   $g_V^{-1} = g_V^{\dagger}$, cutting from
   $\mathrm{SL}(2, \mathbb{C})$ to its compact real form
   $\mathrm{SU}(2)$.
3. *Conclusion.*
   $G = \mathrm{Aut}^{\otimes}(\tau) \cong \mathrm{SU}(2)$,
   recovering the input gauge group from the categorical axioms
   alone.
<!-- FILE_END: su2-emergence-example.md -->

<!-- FILE_START: spin-labels.md -->
Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def:quantum-observable-universe)). Because
$G = \mathrm{Aut}^{\otimes}(\tau) \cong \mathrm{SU}(2)$
([$\mathrm{SU}(2)$ emergence](#thm:su2-emergence)), the simple objects of $\mathbf{C}$
are indexed by a *spin* label $j \in \{0, \tfrac12, 1, \tfrac32, \ldots\}$, with $V_j$ denoting the simple object of
categorical dimension $2j + 1$.
The *fundamental object* is $V = V_{1/2}$, the unique simple object
of categorical dimension $2$. The *adjoint object* is
$V_1 \cong \mathrm{Ad}(A)$, of dimension $3$.

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
Continuing [QOU on $\mathrm{SU}(2)$](#ex:qou-su2), the simple objects of
$\mathbf{C} = \mathrm{Rep}(\mathrm{SU}(2))$ are the irreducible
representations $V_j \cong \mathbb{C}^{2j+1}$:

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

In concrete terms:

- $V_0 = \mathbb{C}$ (the trivial representation: $g \cdot z = z$).
- $V_{1/2} = \mathbb{C}^2$ (the defining representation:
  $g \cdot v = gv$ by matrix multiplication). This is the
  fundamental object $V$.
- $V_1 = \mathfrak{su}(2)_{\mathbb{C}} \cong \mathbb{C}^3$
  (the adjoint representation: $g \cdot X = gXg^{-1}$). This is
  $\mathrm{Ad}(A)$.
- $V_{3/2} = \mathrm{Sym}^3(\mathbb{C}^2) \cong \mathbb{C}^4$
  (homogeneous cubics in two variables).

Every finite-dimensional representation decomposes as
$W \cong \bigoplus_j V_j^{\oplus m_j}$, with multiplicities
$m_j \in \mathbb{N}$. The polynomial ring
$\mathbb{C}[z] = \bigoplus_{n \geq 0} \mathrm{Sym}^n V$ is the
coordinate ring of $\mathbb{P}^1(\mathbb{C}) = \mathbb{P}(V)$
([projective line object](#def:projective-line-object)), and each homogeneous
component $\mathrm{Sym}^n V \cong V_{n/2}$ is an irreducible
representation of dimension $n + 1$.
<!-- FILE_END: spin-labels-su2.md -->

<!-- FILE_START: spin-half-representation.md -->
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
<!-- FILE_END: spin-half-representation.md -->

