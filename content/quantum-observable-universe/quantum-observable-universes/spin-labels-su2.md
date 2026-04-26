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
