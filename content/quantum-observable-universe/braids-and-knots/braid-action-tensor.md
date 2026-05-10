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

![The Hecke skein triple. The three local strand pictures appearing in the
defining relation of the Iwahori--Hecke algebra $H_n(q)$: a positive crossing
$\sigma_i$ (over-strand running from lower-left to upper-right), its inverse
$\sigma_i^{-1}$ (mirror), and the identity $1$ (two parallel strands).
Time flows downward; the marker tips indicate strand orientation.](rendered/r-matrix-skein-0.svg)

The three pictures are related by the Hecke skein identity

$$
  \sigma_i \;-\; \sigma_i^{-1} \;=\; (q - q^{-1})\cdot 1,
$$

equivalently $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$, which together with
the braid relation
$\sigma_i\sigma_{i+1}\sigma_i = \sigma_{i+1}\sigma_i\sigma_{i+1}$
(the Yang--Baxter equation for $c_{V,V}$, equivalently the third
Reidemeister move) presents the Iwahori--Hecke algebra $H_n(q)$ as a
quotient of the braid-group algebra of $B_n$.

