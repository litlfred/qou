Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def\:quantum-observable-universe)).
A *categorical action* on $(\mathbf{C}, A, \tau)$ is a morphism
$\mathfrak{S} \colon \mathbf{1} \to \mathbf{1}$ of the form

```tex
\begin{equation}\label{eq:categorical-action}
  \mathfrak{S}
  = 
  \mathrm{ev}_A
    \circ
    \bigl(\mathrm{id}_{A^\vee} \otimes \Phi\bigr)
    \circ
    \mathrm{coev}_A,
\end{equation}
```

where $\Phi \in \mathrm{End}_{\mathbf{C}}(A)$ is called the
*physics endomorphism*.

```tex
\begin{equation}\label{eq:categorical-action-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \mathbf{1}
    \ar[r, "\mathrm{coev}_A"]
    \ar[rr, bend right=25, "\mathfrak{S}"']
  & A \otimes A^{\vee}
    \ar[r, "\Phi \otimes \mathrm{id}"]
  & A \otimes A^{\vee}
    \ar[r, "\mathrm{ev}_A"]
  & \mathbf{1}
\end{tikzcd}
\qquad\text{(categorical action)}
\end{equation}
```

The evaluation $\mathrm{ev}_A \colon A^\vee \otimes A \to \mathbf{1}$
and coevaluation $\mathrm{coev}_A \colon \mathbf{1} \to A \otimes A^\vee$
are the structure maps of the rigid duality on $A$
([rigid :refterm[monoidal category]{#monoidal-category}](#def\:rigid-monoidal-category)).  Composing
them with an inserted endomorphism produces the categorical trace:

$$
  \mathfrak{S} = \mathrm{tr}(\Phi).
$$

As a string diagram, the action is a single closed loop with $\Phi$
inserted --- the morphism $\mathbf{1} \to \mathbf{1}$ obtained by
"tracing out" the internal degrees of freedom of $A$.  The rigid
structure provides the integration; the physics endomorphism encodes the
dynamics.

The trace $\mathrm{tr}(\Phi)$ used here is the categorical trace of an
endomorphism of a dualizable object in a balanced monoidal category
\cite{stolz-teichner-2012}.  Cf.\ the spectral-action trace
$\mathrm{Tr}\,\chi(D/\Lambda)$ \cite{chamseddine-connes-1997}.
