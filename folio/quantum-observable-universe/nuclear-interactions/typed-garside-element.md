**Definition.**
*Let $\mathcal{A}(Z, N)$ be a nucleus with $A = Z + N$ nucleons in ordering $(t_0, \ldots, t_{A-1})$ where $t_i \in \{p, n\}$. The **typed Garside element** is the element $\mathcal{G}(t_0, \ldots, t_{A-1}) \in H_A(q)$ built by the Garside staircase with typed crossings.*

**Construction.**
The Garside staircase has $A - 1$ levels. At level $\ell$, strand $\ell + 1$ crosses all earlier strands from right to left. Each crossing is typed by the nucleon pair $(t_j, t_{\ell+1})$:

```tex
\begin{equation}\label{eq:typed-garside}
  \mathcal{G}(t_0, \ldots, t_{A-1})
  \;=\;
  \prod_{\ell=0}^{A-2}
  \;\prod_{j=\ell}^{0}
  C(t_j,\, t_{\ell+1};\, \sigma_j),
\end{equation}
```

where $C(f_i, f_j; \sigma_k) = \sigma_k + d(f_i, f_j)$ is the typed crossing operator with coefficients:

$$
  d(p, p) = 0, \qquad
  d(n, n) = -(q - q^{-1}), \qquad
  d(p, n) = d(n, p) = -\tfrac{1}{2}(q - q^{-1}).
$$

The result is reduced to Gröbner–Shirshov normal form under the braiding-induced ordering.
