Let $(\mathcal{C}, A, \tau)$ be a
([quantum observable universe](#def:quantum-observable-universe)).
A *categorical action* on $(\mathcal{C}, A, \tau)$ is a morphism
$\mathcal{S} \colon \mathbf{1} \to \mathbf{1}$ of the form

```tex
\begin{equation}\label{eq:categorical-action}
  \mathcal{S}
  \;=\;
  \mathrm{ev}_A
    \;\circ\;
    \bigl(\mathrm{id}_{A^\vee} \otimes \Phi\bigr)
    \;\circ\;
    \mathrm{coev}_A,
\end{equation}
```

where $\Phi \in \mathrm{End}_{\mathcal{C}}(A)$ is called the
*physics endomorphism*.

The evaluation $\mathrm{ev}_A \colon A^\vee \otimes A \to \mathbf{1}$
and coevaluation $\mathrm{coev}_A \colon \mathbf{1} \to A \otimes A^\vee$
are the structure maps of the rigid duality on $A$
([rigid monoidal category](#def:rigid-monoidal-category)).  Composing
them with an inserted endomorphism produces the categorical trace:

$$
  \mathcal{S} = \mathrm{tr}(\Phi).
$$

As a string diagram, the action is a single closed loop with $\Phi$
inserted --- the morphism $\mathbf{1} \to \mathbf{1}$ obtained by
"tracing out" the internal degrees of freedom of $A$.  The rigid
structure provides the integration; the physics endomorphism encodes the
dynamics.
