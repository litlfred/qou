Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def:quantum-observable-universe)) with
categorical Dirac operator $\mathcal{D}_\nabla$
([categorical Dirac operator](#def:categorical-dirac-operator))
and a state $\psi \colon \mathbf{1} \to A$.
The **categorical Lagrangian** is the endomorphism

$$
  \mathcal{L}_q(\nabla, \psi)
  = 
  \mathcal{D}_\nabla^{2}
  + 
  \psi^* \otimes \mathcal{D}_\nabla\psi
   \in  \mathrm{End}_{\mathbf{C}}(A),
$$

where $\psi^* = \int_A \!\circ S(\psi) \colon A \to \mathbf{1}$ is the
adjoint section (antipode composed with the Frobenius form).

```tex
\begin{equation}\label{eq:categorical-lagrangian-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  A \ar[r, "\mathcal{D}_\nabla"]
    \ar[dr, "\mathcal{L}_q(\nabla{,}\psi)"']
  & \Omega^1(A) \otimes A \ar[d, "\mathcal{D}_\nabla + \psi^* \otimes (-)"] \\
  & \mathrm{End}_{\mathbf{C}}(A)
\end{tikzcd}
\qquad\text{(Lagrangian)}
\end{equation}
```

The Lagrangian is an endomorphism of $A$ --- the categorical analog of a
Lagrangian *density* $\mathscr{L}(x)$ before integration over spacetime.
Its first summand $\mathcal{D}_\nabla^2$ encodes the bosonic sector
(gravity + gauge curvature); the second summand encodes the fermionic
coupling of the state to the connection.

Cf.\ the Chamseddine--Connes *spectral action principle*
\cite{chamseddine-connes-1997, connes1996},
$S(D,\psi) = \mathrm{Tr}\,\chi(D/\Lambda) + (\psi, D\psi)$,
whose two summands have the same bosonic / fermion-bilinear shape.
