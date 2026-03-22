Let $(\mathcal{C}, A, \omega)$ be a quantum observable universe with
instanton $\nabla$ ([Definition](#def:categorical-instanton)) and
$q$-deformed exterior derivative $d_q$
([Definition](#def:categorical-q-ext-deriv)). The *categorical
transport equation* for a section $\psi \in \omega(J^1(A))$
([Definition](#def:categorical-jet)) is

```tex
\begin{equation}\label{eq:categorical-transport}
  \hbar_q\;\pi_V(\nabla\,\psi) \;=\; H_q(\psi),
\end{equation}
```

where $H_q \colon \omega(J^1(A)) \to \omega(J^1(A))$ is the
*$q$-Hamiltonian* endomorphism
$H_q = -\tfrac{1}{2}\hbar_q\,\Delta_q + V_q$
(with $V_q$ the potential arising from the curvature $F_\nabla$).
The following diagram encodes the transport as the bottom row of the
main commutative diagram:

```tex
\begin{equation}\label{eq:transport-cd}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \omega(J^1(A)) \ar[r, "\nabla"] \ar[d, "j^1"']
  & \omega(J^1(A)) \otimes \Omega^1 \ar[d, "\pi_V"] \\
  \omega(A) \ar[r, "H_q"']
  & \omega(J^1(A))
\end{tikzcd}
\end{equation}
```
