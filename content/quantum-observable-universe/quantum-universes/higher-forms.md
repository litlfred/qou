Let $(\mathbf{C}, A, \tau)$ be a quantum universe with differential
calculus $\Omega^1(A)$ ([quantum universe](#def:quantum-universe)). To
assemble a graded differential calculus — the setting in which curvature
and de Rham cohomology are later defined — the first-order forms
$\Omega^1(A)$ must be extended to forms of every degree. The
**higher differential forms** are the graded $A$-bimodule

$$
  \Omega^k(A) =  \bigwedge\nolimits_A^k \Omega^1(A),
  \qquad k = 0, 1, 2, \ldots
$$

(exterior powers of the $A$-bimodule $\Omega^1(A)$ in $\mathbf{C}$),
with $\Omega^0(A) = A$ and $\Omega^1(A)$ the first-order forms already in
hand; the $\mathrm{SU}(2)$ instance is worked out in the
[higher-forms example](#ex:higher-forms-su2). For an object $V$ in $\mathbf{C}$,
$\Lambda^k V$ denotes the $k$-th exterior power of $V$ in the sense
of rigid monoidal categories. The differential
$d \colon \Omega^k(A) \to \Omega^{k+1}(A)$ extends the universal
derivation by the graded Leibniz rule, and satisfies $d^2 = 0$.

```tex
\begin{equation}\label{eq:de-rham-complex}
\begin{tikzcd}[column sep=2.5em]
  A = \Omega^0(A) \ar[r, "d"]
  & \Omega^1(A) \ar[r, "d"]
  & \Omega^2(A) \ar[r, "d"]
  & \cdots
\end{tikzcd}
\qquad (d^2 = 0)
\end{equation}
```
