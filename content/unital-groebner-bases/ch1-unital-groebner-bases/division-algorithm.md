We describe, for a subset $I \subseteq A$ (not necessarily an ideal), a division
algorithm. One may view [Theorem 2](#thm:ugb-main) as ascribing a meaning to
this algorithm when we make the assumption of the existence of a unital Gröbner
basis for $I$.

**Input:** $R$ a commutative ring with unity, $A$ an $R$-algebra which is free as
an $R$-module and without quasi-zeros, $(B, <)$ an admissible system on $A$, a
subset $I \subseteq A$, and $f \in A$.

**Output:** $\tilde{f} \in I$ and $r \in O(I)$ the remainder of $f$ on division by $I$
so that $f = r + \tilde{f}$.

```tex
\begin{enumerate}
\item Set $i := 0$, $f_0 := f$.
\item While $f_i \neq 0$:
  \begin{enumerate}
  \item $i := i + 1$
  \item If $\nexists\, h \in I$ such that $\LT(h) \mid f$, set $r_i := \LT(f)$ and $f_i := f_{i-1} - r_i$.
  \item Else choose some $h_i \in I$ with $\LT(h_i) \mid f_{i-1}$, choose $\lambda_i \in R^*$, $u_i, v_i \in B$ so that $\lambda_i \LT(u_i \cdot h_i \cdot v_i) = \LT(f_{i-1})$, and set $f_i := f_{i-1} - \lambda_i u_i \cdot h_i \cdot v_i$, $r_i := 0$.
  \end{enumerate}
\item $r := \sum_i r_i$, \quad $\tilde{f} := \sum_i \lambda_i u_i \cdot h_i \cdot v_i = f - r$.
\end{enumerate}
```

We note that, because we do not specify how to choose the $h_i$ (nor the $u_i$
and $v_i$), we do not in general have a unique output.
