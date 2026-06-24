*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Proposition.**
*For each partition $\lambda \vdash n$ and substrate parameter $q > 1$,
the Hoefsmit seminormal form \cite{hoefsmit1974} gives an explicit
matrix representation $\rho_\lambda\colon H_n(R, q) \to M_{d_\lambda}(\mathbb{C})$
where $d_\lambda = |\mathrm{SYT}(\lambda)|$ is the number of standard
Young tableaux of shape $\lambda$.  The generator $\sigma_i$ acts on the
basis of standard tableaux by:*

$$
  \rho_\lambda(\sigma_i)_{ss'}
  =
  \begin{cases}
    a_\rho & s' = s, \\
    b & s' = s_i, \\
    0 & \text{otherwise},
  \end{cases}
$$

*where $s_i$ is the tableau obtained by swapping entries $i$ and $i+1$
in $s$ (if the result is a valid standard tableau), and the matrix
entries are:*

$$
  a_\rho = \frac{q - q^{-1}}{1 - q^{-2\rho}},
  \qquad
  b = \sqrt{a_\rho \cdot a_{-\rho} + 1},
$$

*with $\rho = c(s, i{+}1) - c(s, i)$ the axial distance (content
difference) between the cells containing $i{+}1$ and $i$ in
tableau $s$.*

*These matrices satisfy the Hecke relation
$\sigma_i^2 = (q - q^{-1})\,\sigma_i + 1$ and the braid relation
$\sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1}$, and are the explicit
$R$-matrix evaluations that dictate topological crossings in braid
and knot diagrams.*
