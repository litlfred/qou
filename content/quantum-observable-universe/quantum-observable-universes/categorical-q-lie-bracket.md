Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
Reeb derivation $\xi$ ([categorical Reeb derivation](#def:categorical-reeb)) and
substrate parameter $q$ ([substrate parameter](#def:substrate-parameter)).
The **$q$-deformed Lie bracket** on derivations of $A$ is

$$
  [X, Y]_q =  q^{-1}[X, Y]
  + (1 - q^{-1})\bigl(\varTheta_A(X)[\xi, Y]
                        - \varTheta_A(Y)[\xi, X]\bigr),
$$

where $\varTheta_A$ is the canonical $1$-form dual to $\xi$ and
$[X, Y]$ is the commutator of derivations in $\mathbf{C}$.

```tex
\begin{equation}\label{eq:q-lie-bracket-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \mathrm{Der}(A) \otimes \mathrm{Der}(A)
    \ar[r, "{[\cdot,\cdot]}"]
    \ar[d, "{[\cdot,\cdot]_q}"']
  & \mathrm{Der}(A) \\
  \mathrm{Der}(A)
    \ar[ur, equal, "q{=}1"']
\end{tikzcd}
\end{equation}
```
