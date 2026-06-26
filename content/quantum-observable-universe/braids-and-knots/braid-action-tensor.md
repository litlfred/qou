Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def:quantum-observable-universe)) whose ambient category
$\mathbf{C}$ is braided monoidal with braiding
$c_{X,Y}\colon X\otimes Y \xrightarrow{ \sim } Y\otimes X$.
For each object $V$ in $\mathbf{C}$ and each $n \geq 2$, there is a
group homomorphism

$$
  \rho_n\colon B_n  \longrightarrow  \mathrm{Aut}_{\mathbf{C}}(V^{\otimes n})
$$

given on the Artin generators by

```tex
\begin{equation}\label{eq:categorical-braid-rep}
  \rho_n(\sigma_i)
  = 
  \mathrm{id}^{\otimes(i-1)}
  \otimes c_{V,V}
  \otimes \mathrm{id}^{\otimes(n-i-1)},
  \qquad 1 \leq i \leq n-1.
\end{equation}
```

The braid relation
$\rho_n(\sigma_i)\rho_n(\sigma_{i+1})\rho_n(\sigma_i) = \rho_n(\sigma_{i+1})\rho_n(\sigma_i)\rho_n(\sigma_{i+1})$
is equivalent to the Yang--Baxter equation for the braiding $c_{V,V}$.
