Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
categorical Hodge star $\star$
([categorical hodge star](#def:categorical-hodge-star)) and substrate
parameter $q$ ([substrate parameter](#def:substrate-parameter)).  The
**$q$-Hodge star** is the $q$-deformed involution
$\star_q \colon \Omega^k(A) \to \Omega^{n-k}(A)$ defined by

$$
  \alpha \wedge_q \star_q \beta
  =  q \cdot \int_A\!\bigl(\alpha^* \cdot \beta\bigr) \mathrm{vol}.
$$

```tex
\begin{equation}\label{eq:q-hodge-star-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \Omega^k(A) \ar[r, "\star_q"] \ar[d, "\star"']
  & \Omega^{n-k}(A) \\
  \Omega^{n-k}(A) \ar[ur, "q \cdot \mathrm{id}"']
\end{tikzcd}
\qquad\text{($q$-Hodge star)}
\end{equation}
```

At $q = 1$ this recovers the categorical Hodge star:
$\star_1 = \star$.  The factor of $q$ rescales the inner product on
forms, coupling the Hodge duality to the local deformation strength.
