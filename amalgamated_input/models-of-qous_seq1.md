<!-- FILE_START: models-of-qous-intro.md -->
The QOU axioms admit realisations across diverse ground fields and geometric settings. This chapter separates the universal features forced by the axioms from the model-dependent features fixed by the ground ring and fibre geometry.

The Jones model arising from $\mathbf{Rep}(\mathrm{SU}_q(2))$ serves as our concrete anchor. Around it, we place the wider landscape: archimedean realisations (Calabi–Yau, ALE spaces), $p$-adic quantum groups via Drinfeld's theory, finite-field models, and Witt-vector models. Each model instantiates the QOU axioms with different fibre geometry and ground rings. This illustrates the flexibility of the categorical framework while exposing the universal structural constraints. We survey this landscape through the physical interpretation of the $q$-weighted Yang–Mills–Levi functional and the main commutative diagram relating categorical and differential structures.
<!-- FILE_END: models-of-qous-intro.md -->

<!-- FILE_START: q-yang-mills-levi.md -->
Let $(\mathbf{C}, \varTheta, G, \mathcal{S})$ be an archimedean quantum observable universe with instanton connection $A$ and substrate parameter $q$. To couple the instanton energy to the substrate, we weight the self-dual curvature by the local Levi-form magnitude $q(p)$. Regions where $F_A^+$ overlaps the Levi form $L_\varTheta$ contribute more strongly. The **$q$-weighted Yang–Mills–Levi functional** is

$$
  \mathfrak{S}_q[A, \varTheta]
  =  \int_M q(p)\lVert F_A^+|_H \rVert^2
        \varTheta \wedge (d\varTheta)^n,
$$

where $q(p) = 1 + \lvert\langle L_\varTheta, F_A^+\rangle\rvert(p)$.
<!-- FILE_END: q-yang-mills-levi.md -->

<!-- FILE_START: main-commutative-diagram.md -->
This square exhibits the Einstein-type field equation and the Schrödinger evolution as two faces of a single commuting diagram. The substrate coupling $q$ ties the gravitational and quantum dynamics together.

Let $(\mathbf{C}, \varTheta, G, \mathcal{S})$ be an archimedean quantum observable universe with instanton connection $A$ and substrate parameter $q$. Let $\mathfrak{E}$ denote the Euler–Lagrange operator of the $q$-weighted Yang–Mills–Levi functional $\mathfrak{S}_q$. Let $\nabla^A$ denote parallel transport along $A$. The upper-left object $J^1\mathcal{S}$ is the space of $1$-jets of sections of the state bundle $\mathcal{S}$ (encoding the state and its first-order derivatives). The following diagram commutes:

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

The top row sends a jet to the Einstein-type field equation via the Euler–Lagrange operator. The left column evaluates a jet at a fibre point to produce a linearised section. The right column implements the coupling through the substrate field $q$. The bottom row applies the parallel-transport equation whose linearisation is the Schrödinger equation.
<!-- FILE_END: main-commutative-diagram.md -->

