Let $(\mathcal{C}, A, \omega)$ be a quantum observable universe
([Definition](#def:quantum-observable-universe)) equipped with
substrate parameter $q$ ([Definition](#def:substrate-parameter)),
$q$-Hodge star $\star_q$ ([Definition](#def:q-hodge-star)),
a connection $\nabla$ ([Definition](#def:categorical-connection)),
and a section $\psi \colon \mathbf{1} \to A$ (a "state").
The *categorical action* is the $R$-valued functional

```tex
\begin{equation}\label{eq:categorical-action}
  \mathcal{S}_q[\nabla,\, \lambda,\, \psi]
  \;=\;
  \underbrace{%
    \mathrm{tr}\bigl(q \cdot R_\lambda\bigr)
  }_{\text{gravity}}
  \;+\;
  \underbrace{%
    \lambda \circ \mathrm{tr}_A\bigl(
      F_\nabla \wedge_q \star_q F_\nabla
    \bigr)
  }_{\text{gauge}}
  \;+\;
  \underbrace{%
    \lambda\bigl(\psi^* \cdot D_\nabla\,\psi\bigr)
  }_{\text{matter}},
\end{equation}
```

with notation as in [Remark](#rem:categorical-action-notation).
