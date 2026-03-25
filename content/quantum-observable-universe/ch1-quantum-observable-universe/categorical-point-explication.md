In the archimedean realisation $A = \mathcal{O}(G)$, a categorical point
$p \colon \mathbf{1} \to A$ is a character $\mathrm{ev}_g \colon f \mapsto f(g)$
for some $g \in G$; equivalently, a point of the group $G$.  For a
manifold $M$ with $A = C^{\infty}(M)$, a point $p$ corresponds to
evaluation at $p \in M$:

```tex
\begin{equation}\label{eq:point-diagram}
\begin{tikzcd}[column sep=2.5em]
  \{*\} \ar[r, "p"]
  & M
\end{tikzcd}
\qquad\longleftrightarrow\qquad
\begin{tikzcd}[column sep=2.5em]
  \mathbf{1} \ar[r, "p"]
  & A
\end{tikzcd}
\end{equation}
```

The *augmentation ideal* at $p$ is
$\mathfrak{m}_p = \ker(p^* \colon A \to \mathbf{1})$, where
$p^* = \int_A \circ \mu(p \otimes -)$.  The *germ* of $A$
at $p$ is the quotient $A / \mathfrak{m}_p^2$, which captures the
first-order behaviour of $A$ near $p$.
