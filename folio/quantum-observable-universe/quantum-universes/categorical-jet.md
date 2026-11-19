Let $(\mathbf{C}, A, \tau)$ be a [quantum universe](#def:quantum-universe) with connection $\nabla$ ([categorical connection](#def:categorical-connection)). The **jet object** is

$$
  J^1(A) := A \otimes_{\mathbf{C}} \Omega^1(A),
$$

where $\Omega^1(A) = \ker(\mu \colon A \otimes A \to A)$ is the bimodule of Kähler differentials. The jet object fits into the universal extension

```tex
\begin{equation}\label{eq:jet-ses}
\begin{tikzcd}[column sep=2.5em]
  0 \ar[r]
  & A \otimes \Omega^1(A) \ar[r]
  & J^1(A) \ar[r, "j^1"]
  & A \ar[r]
  & 0
\end{tikzcd}
\end{equation}
```

where $j^1 \colon J^1(A) \to A$ is the jet evaluation.
