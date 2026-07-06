This square exhibits the Einstein-type field equation (top row target) and the Schrödinger evolution (bottom row target) as two faces of a single commuting diagram. The substrate coupling $q$ on the right column ties the gravitational and quantum dynamics together.

Let $(\mathbf{C}, \varTheta, G, \mathcal{S})$ be an archimedean quantum observable universe with instanton connection $A$ ([instanton](#ex:instanton)) and substrate parameter $q$ ([substrate parameter](#def:substrate-parameter)). Let $\mathfrak{E}$ denote the Euler--Lagrange operator of the $q$-weighted Yang--Mills--Levi functional $\mathfrak{S}_q$ ([$q$-Yang--Mills--Levi functional](#def:q-yang-mills-levi)). Let $\nabla^A$ denote parallel transport along $A$. The upper-left object $J^1\mathcal{S}$ is the space of $1$-jets of sections of the state bundle $\mathcal{S}$ (encoding the state and its first-order derivatives). The following diagram commutes:

```tex
\[
\begin{tikzcd}[row sep=2.5em, column sep=2.5em]
  J^1\mathcal{S}
    \ar[r, "{\mathfrak{E}[\mathfrak{S}_q]}"]
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

The top row sends a jet to the Einstein-type field equation via the Euler--Lagrange operator. The left column evaluates a jet at a fibre point to produce a linearised section. The right column implements the coupling through the substrate field $q$. The bottom row applies the parallel-transport equation whose linearisation is the Schrödinger equation.

