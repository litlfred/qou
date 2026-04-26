The Hopf comultiplication $\Delta \colon A \to A \otimes A$ of the
Frobenius--Hopf object is coassociative but *not* cocommutative
when $q \neq 1$.  Let $\sigma$ denote the tensor flip.  The
cocommutativity square

```tex
\begin{equation}\label{eq:non-cocommutativity}
\begin{tikzcd}[row sep=2.5em, column sep=3.5em]
  A
    \ar[r, "\Delta"]
    \ar[d, "\Delta"']
  & A \otimes A
    \ar[d, "\sigma"]
  \\
  A \otimes A
    \ar[r, equal]
  & A \otimes A
\end{tikzcd}
\quad\text{commutes}\;\Longleftrightarrow\; q \to 1\ \text{(symmetric-braiding limit)}.
\end{equation}
```

For $q \neq 1$ the failure is controlled by the universal $R$-matrix:
$\sigma \circ \Delta = \mathrm{Ad}_{R_q} \circ \Delta$,
where $R_1 = 1 \otimes 1$ recovers cocommutativity at $q = 1$.
This non-cocommutativity is the algebraic origin of quantum
uncertainty: it prevents simultaneous diagonalisation of comultiplication
and its transpose, which in turn prevents independent observations from
commuting ([two-observer parallelogram](#rem:two-observer-parallelogram)).
