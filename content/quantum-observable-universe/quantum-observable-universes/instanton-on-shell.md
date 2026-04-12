On an instanton background ([categorical instanton](#def:categorical-instanton)),
the curvature is $\star_q$-self-dual: $\star_q F_\nabla = F_\nabla$.
The Bogomolny decomposition ([self-duality](#prop:categorical-self-duality))
gives

$$
  \lVert F_\nabla \rVert^2
  = 
  \lVert F_\nabla^+ \rVert^2 + \lVert F_\nabla^- \rVert^2
  = 
  c_2(A) + 2\lVert F_\nabla^- \rVert^2,
$$

where $c_2(A)$ is the second Chern number (a topological invariant).
The instanton condition forces $F_\nabla^- = 0$, so the gauge sector
of the Lagrangian becomes purely topological:

$$
  \mathcal{D}_\nabla^{2} =  F_\nabla^+ =  c_2(A).
$$

The full Lagrangian ([categorical Lagrangian](#def:categorical-lagrangian))
therefore simplifies on-shell:

$$
  \mathcal{L}_q\big|_{\text{instanton}}
  = 
  c_2(A)
  + 
  \psi^* \otimes \mathcal{D}_\nabla\psi.
$$

```tex
\begin{equation}\label{eq:instanton-on-shell-cd}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \mathcal{L}_q \ar[r, equals]
  & \mathcal{D}_\nabla^2 + \psi^* \otimes \mathcal{D}_\nabla\psi
    \ar[d, "\text{instanton}"] \\
  & c_2(A) + \psi^* \otimes \mathcal{D}_\nabla\psi
\end{tikzcd}
\end{equation}
```

This has three consequences:

1. **No dynamical gauge degrees of freedom beyond topology.**
   The connection is determined (up to gauge equivalence) by the knot
   type $K$ of the localized knot
   ([knot--particle dictionary](#rem:knot-particle-dictionary)).  The
   topological sector $c_2(A)$ is fixed by $K$.

2. **All physics is in the matter equation.**
   On an instanton, varying $\psi$ gives
   $\mathcal{D}_\nabla\psi = 0$
   ([variational equations](#prop:variational-equations)), which completely
   determines the propagation of the state.

3. **The wavefront is determined by the background topology.**
   The Green's function of $\mathcal{D}_\nabla$ depends on the
   instanton $\nabla$, which in turn depends on the knot type of the
   material through which $\psi$ propagates.  Different materials
   (different $K$, different $c_2$) produce different diffraction
   patterns --- a prediction unique to QOU.
