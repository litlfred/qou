Let $(\mathcal{C}, A, \tau)$ be a
([quantum observable universe](#def:quantum-observable-universe)) equipped with
connection $\nabla$ ([categorical connection](#def:categorical-connection)),
substrate parameter $q$ ([substrate parameter](#def:substrate-parameter)),
$q$-Hodge star $\star_q$ ([$q$-Hodge star](#def:q-hodge-star)),
and state $\psi \colon \mathbf{1} \to A$.
Then $(\mathcal{C}, A, \tau)$ determines a unique
([categorical action](#def:categorical-action))

$$
  \mathcal{S}_q
  \;=\;
  \mathrm{tr}(\mathcal{L}_q),
$$

where $\mathcal{L}_q = \mathcal{L}_q(\nabla, \psi)$ is the categorical
Lagrangian ([categorical Lagrangian](#def:categorical-lagrangian)).
The physics endomorphism is $\Phi_q = \mathcal{L}_q$.

The square of the Dirac operator
([categorical Dirac operator](#def:categorical-dirac-operator))
decomposes via the Frobenius--Hopf structure as

$$
  \mathcal{D}_\nabla^{\,2}
  \;=\;
  q \cdot R_{\int} \;+\; \mathrm{tr}_A\!\bigl(
    F_\nabla \wedge_q \star_q F_\nabla
  \bigr),
$$

so the categorical action expands to three terms:

```tex
\begin{equation}\label{eq:canonical-action-decomposition}
  \mathcal{S}_q[\nabla,\, \textstyle\int_A,\, \psi]
  \;=\;
  \underbrace{%
    \mathrm{tr}\bigl(q \cdot R_{\int}\bigr)
  }_{\text{gravity}}
  \;+\;
  \underbrace{%
    \int_A \!\circ\, \mathrm{tr}_A\bigl(
      F_\nabla \wedge_q \star_q F_\nabla
    \bigr)
  }_{\text{gauge}}
  \;+\;
  \underbrace{%
    \int_A\!\bigl(\psi^* \cdot \mathcal{D}_\nabla\,\psi\bigr)
  }_{\text{matter}},
\end{equation}
```

with notation as in [categorical action notation](#rem:categorical-action-notation).
Here $\mathrm{tr} = \mathrm{ev}_A \circ (\mathrm{id}_{A^\vee} \otimes {-})
\circ \mathrm{coev}_A$ is the categorical trace, which plays the role of
spacetime integration; $R_{\int}$ is the Frobenius--Ricci endomorphism;
and $F_\nabla = \nabla^2$ is the curvature.

*Uniqueness* follows from the rigidity of the monoidal structure: the
evaluation and coevaluation maps are determined up to unique isomorphism
by the duality data, and the Frobenius--Hopf axioms fix the decomposition
of $\mathcal{D}_\nabla^2$ into curvature terms.
