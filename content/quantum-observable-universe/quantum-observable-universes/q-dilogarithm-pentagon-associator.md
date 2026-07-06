The pentagon relation normalising the
([$q$-dilogarithm](#def:q-dilogarithm)) is the Hopf-algebraic avatar of
the *pentagon axiom* for the
:refterm[monoidal category]{#monoidal-category} $\mathbf{C}$: $\mathrm{Li}_2^q$
is the unique level-2 primitive compatible with the monoidal associator
$\alpha_{X,Y,Z}$.

```tex
\begin{equation}\label{eq:q-dilog-pentagon}
\begin{tikzcd}[row sep=2.5em, column sep=2em]
  (X \otimes Y) \otimes (Z \otimes W)
    \ar[r, "\alpha"]
    \ar[d, "\alpha \otimes \mathrm{id}"']
  &  X \otimes (Y \otimes (Z \otimes W))
    \ar[d, "\mathrm{id} \otimes \alpha"]
  \\
  ((X \otimes Y) \otimes Z) \otimes W
    \ar[r, "\alpha"']
  &  X \otimes ((Y \otimes Z) \otimes W)
\end{tikzcd}
\qquad
\leftrightarrow
\qquad
\mathrm{Li}_2^q\text{-pentagon}
\end{equation}
```
