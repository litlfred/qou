Let $(\mathbf{C}, A, \tau)$ be a quantum universe with $A$ commutative over a commutative ring $R$, let $I = \ker(m \colon A \otimes A \to A)$, and let $J^1(A) = (A \otimes A)/I^2$ be the [jet object](#def:categorical-jet). The section $\ell \colon A \to J^1(A)$, $a \mapsto [a \otimes 1]$, and the jet evaluation $j^1 \colon J^1(A) \to A$ induced by $m$ are algebra maps with $j^1 \circ \ell = \mathrm{id}_A$, so $A$ is a direct summand of $J^1(A)$ ([jet object splitting](#lem:jet-prolongation-categorical-jet)). The jet object does not in general inherit the Frobenius–Hopf structure of $A$: over a field $k$ of characteristic zero and for $A = k[X]$ with $X$ primitive, no multiplicative comultiplication on $J^1(A)$ is compatible with both jet sections $a \mapsto [a \otimes 1]$ and $a \mapsto [1 \otimes a]$. The prolongation object of the brane tower is therefore the tangent algebra $T(A) = \mathrm{Sym}_A(\Omega^1_{A/R})$, of which $J^1(A)$ is the degree-$\le 1$ part ([jet prolongation](#prop:jet-prolongation)).

```tex
\begin{equation}\label{eq:jet-prolongation-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  A \ar[r, hook, "\ell"] \ar[rr, bend right=25, "\mathrm{id}_A"']
  & J^1(A) \ar[r, two heads, "j^1"]
  & A
\end{tikzcd}
\qquad\text{(jet splitting)}
\end{equation}
```
