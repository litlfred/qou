Let $(\mathbf{C}, \varTheta, G, \mathcal{S})$ be an archimedean quantum observable universe with instanton connection $A$ and substrate parameter $q$. Let $\mathrm{EL}$ denote the Euler–Lagrange operator of the $q$-weighted Yang–Mills–Levi functional $\mathfrak{S}_q$. Let $\nabla^A$ denote parallel transport along $A$. The upper-left object $J^1\mathcal{S}$ is the space of $1$-jets of sections of the state bundle $\mathcal{S}$ (encoding the state and its first-order derivatives). The following diagram commutes:

```tex
\[
\begin{tikzcd}[row sep=2.5em, column sep=2.5em]
  J^1\mathcal{S}
    \ar[r, "{\mathrm{EL}[\mathfrak{S}_q]}"]
    \ar[d, "\text{jet evaluation}"']
  & \bigl\{ L_\varTheta : \mathrm{Ric}_{g_\varTheta} = T^{(q)} \bigr\}
    \ar[d, "{q = 1 + \lvert\langle L_\varTheta, F_A^+\rangle\rvert}"]
  \\
  \Gamma(\mathcal{S}_{\mathrm{lin}})
    \ar[r, "\nabla^A"']
  & \bigl\{ \psi : J\hbar_q\iota_{\xi_q}D_A\psi = \hat{H}_q\psi \bigr\}
\end{tikzcd}
\]
```

The reading of each edge — top row, columns, and bottom row — is given in the [diagram interpretation](#rem:main-commutative-diagram-interpretation).
