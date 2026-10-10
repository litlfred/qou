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
