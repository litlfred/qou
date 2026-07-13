Let $(\mathbf{C}, A, \tau)$ be a [quantum universe](#def:quantum-universe). Denote by $\Delta_\mu$ the comultiplication on $A$ dual to $\mu$ under the [Frobenius pairing](#def:frobenius-pairing). This compatibility makes $A$ a Frobenius algebra. The *Frobenius relation* holds:

```tex
\begin{equation}\label{eq:frobenius-relation}
\begin{gathered}
\begin{tikzcd}[row sep=2.5em, column sep=3.5em]
  A \otimes A
    \ar[r, "\mathrm{id} \otimes \Delta_\mu"]
    \ar[d, "\mu"']
  & A \otimes A \otimes A
    \ar[d, "\mu \otimes \mathrm{id}"]
  \\
  A \ar[r, "\Delta_\mu"']
  & A \otimes A
\end{tikzcd}
\\[-0.5em]
\text{\small Frobenius relation: } (\mu \otimes \mathrm{id}) \circ (\mathrm{id} \otimes \Delta_\mu) = \Delta_\mu \circ \mu
\end{gathered}
\end{equation}
```

Sliding a multiplication past a comultiplication yields the same result as composing them.
