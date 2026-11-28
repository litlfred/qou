Write $[2]_q = q + 1$ and $[3]_q = q^2 + q + 1$ in the Laurent polynomial ring $\mathbb{Z}[q^{\pm 1}]$, where Bézout's identity $[3]_q - q[2]_q = 1$ makes $[2]_q$ and $[3]_q$ coprime. Define the partial affine $[2]_q$-division map $\mathcal{C}_q$ on $\mathbb{Z}[q^{\pm 1}]$ by

$$
\mathcal{C}_q(P) =
\begin{cases}
  P / [2]_q & \text{if } P(-1) = 0,\\[4pt]
  \bigl([3]_q P + 1\bigr) / [2]_q & \text{if } P(-1) = -1,
\end{cases}
$$

and call a sequence $(P_j)_{j \ge 0}$ *domain-stable* if $P_j(-1) \in \{0, -1\}$ and $P_{j+1} = \mathcal{C}_q(P_j)$ for all $j \ge 0$. The propositions below classify all periodic orbits of $\mathcal{C}_q$ in $\mathbb{Z}[q^{\pm 1}]$, show that evaluation at $q = 1$ projects any domain-stable sequence onto the integer Syracuse map $n \mapsto n/2$ or $(3n + 1)/2$, and prove by $\mathbb{F}_2[q]$ reduction that every domain-stable sequence with bounded exponent window is eventually periodic.
