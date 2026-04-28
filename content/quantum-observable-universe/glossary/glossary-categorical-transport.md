Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
instanton $\nabla$ ([categorical instanton](#def:categorical-instanton)) and
$q$-deformed exterior derivative $d_q$
([categorical $q$-exterior derivative](#def:categorical-q-ext-deriv)). The
:defterm[categorical transport equation]{#categorical-transport} for a section $\psi \in \tau(J^1(A))$
([categorical jet](#def:categorical-jet)) is

```tex
\begin{equation}\label{eq:categorical-transport}
  \hbar_q\pi_V(\nabla\psi) =  \hat{H}_q(\psi),
\end{equation}
```

where $\hat{H}_q \colon \tau(J^1(A)) \to \tau(J^1(A))$ is the
*$q$-Hamiltonian* endomorphism
$\hat{H}_q = -\tfrac{1}{2}\hbar_q\Delta_q + V_q$
(with $V_q$ the potential arising from the curvature $F_\nabla$).
The following diagram encodes the transport as the bottom row of the
main commutative diagram:

```tex
\begin{equation}\label{eq:transport-cd}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \tau(J^1(A)) \ar[r, "\nabla"] \ar[d, "j^1"']
  & \tau(J^1(A)) \otimes \Omega^1 \ar[d, "\pi_V"] \\
  \tau(A) \ar[r, "\hat{H}_q"']
  & \tau(J^1(A))
\end{tikzcd}
\end{equation}
```
