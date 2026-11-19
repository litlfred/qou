Let $(\mathbf{C}, \otimes, \mathbf{1})$ be a :refterm[monoidal category]{#monoidal-category}. Let $V$ be an object with dual $V^{\vee}$, evaluation $\mathrm{ev} \colon V \otimes V^{\vee} \to \mathbf{1}$, and coevaluation $\mathrm{coev} \colon \mathbf{1} \to V^{\vee} \otimes V$. The **snake identities** are the equations making $(\mathrm{ev}, \mathrm{coev})$ exhibit $V^{\vee}$ as a :refterm[right dual]{#right-dual} of $V$:

```tex
\begin{equation}\label{eq:snake-identities}
\begin{gathered}
\begin{tikzcd}[row sep=2em, column sep=2.5em]
  V
    \ar[r, "\mathrm{id} \otimes \mathrm{coev}"]
    \ar[dr, "\mathrm{id}_V"']
  & V \otimes V^{\vee} \otimes V
    \ar[d, "\mathrm{ev} \otimes \mathrm{id}"]
  \\
  & V
\end{tikzcd}
\\[-0.5em]
\text{\small (left snake identity)}
\end{gathered}
\qquad\qquad
\begin{gathered}
\begin{tikzcd}[row sep=2em, column sep=2.5em]
  V^{\vee}
    \ar[r, "\mathrm{coev} \otimes \mathrm{id}"]
    \ar[dr, "\mathrm{id}_{V^{\vee}}"']
  & V^{\vee} \otimes V \otimes V^{\vee}
    \ar[d, "\mathrm{id} \otimes \mathrm{ev}"]
  \\
  & V^{\vee}
\end{tikzcd}
\\[-0.5em]
\text{\small (right snake identity)}
\end{gathered}
\end{equation}
```

The pair forms an :defterm[exact pairing]{#exact-pairing}.
