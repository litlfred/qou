A jet object packages an element of $A$ together with its infinitesimal variation. Let $(\mathbf{C}, A, \tau)$ be a [quantum universe](#def:quantum-universe) over a commutative ring $R$ with connection $\nabla$ ([categorical connection](#def:categorical-connection)), and assume $A$ is commutative, so that $I = \ker(\mu \colon A \otimes A \to A)$ is an ideal of $A \otimes A$. The **jet object** is the first-jet module

$$
  J^1(A) := (A \otimes A)/I^2 .
$$

The section $\ell(a) = [a \otimes 1]$ and the retraction $r \colon J^1(A) \to A$ induced by $\mu$ satisfy $r \circ \ell = \mathrm{id}_A$, and $\ker r = I/I^2$, which is the module $\Omega^1_{A/R}$ of Kähler differentials. The jet object therefore fits into the split extension

```tex
\begin{equation}\label{eq:jet-ses}
\begin{tikzcd}[column sep=2.5em]
  0 \ar[r]
  & \Omega^1_{A/R} \ar[r]
  & J^1(A) \ar[r, "j^1"]
  & A \ar[r]
  & 0
\end{tikzcd}
\end{equation}
```

where $j^1 = r$ is the jet evaluation.
