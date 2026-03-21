Let $(\mathcal{C}, A, \omega)$ be a quantum observable universe
([Definition](#def:quantum-observable-universe)) whose ambient category
$\mathcal{C}$ is braided monoidal with braiding
$c_{X,Y}\colon X\otimes Y \xrightarrow{\;\sim\;} Y\otimes X$.
For each object $V$ in $\mathcal{C}$ and each $n \geq 2$, there is a
group homomorphism
$$
  \rho_n\colon B_n \;\longrightarrow\; \mathrm{Aut}_{\mathcal{C}}(V^{\otimes n})
$$
given on the Artin generators by

```tex
\begin{equation}\label{eq:categorical-braid-rep}
  \rho_n(\sigma_i)
  \;=\;
  \mathrm{id}^{\otimes(i-1)}
  \otimes\, c_{V,V}
  \otimes\, \mathrm{id}^{\otimes(n-i-1)},
  \qquad 1 \leq i \leq n-1.
\end{equation}
```

The braid relation
$\rho_n(\sigma_i)\,\rho_n(\sigma_{i+1})\,\rho_n(\sigma_i)
= \rho_n(\sigma_{i+1})\,\rho_n(\sigma_i)\,\rho_n(\sigma_{i+1})$
is equivalent to the Yang--Baxter equation for the braiding $c_{V,V}$.

---

The hexagon axioms of a braided monoidal category guarantee that
$c_{V,V}$ satisfies the Yang--Baxter equation
$$
  (c \otimes \mathrm{id})
  \circ (\mathrm{id} \otimes c)
  \circ (c \otimes \mathrm{id})
  \;=\;
  (\mathrm{id} \otimes c)
  \circ (c \otimes \mathrm{id})
  \circ (\mathrm{id} \otimes c)
$$
on $V^{\otimes 3}$.  This is exactly the braid relation for adjacent
generators, and the far-commutativity relation
$\sigma_i\sigma_j = \sigma_j\sigma_i$ ($\lvert i-j\rvert \geq 2$) follows
from the naturality of the braiding.  Together these verify the Artin
presentation of $B_n$.
