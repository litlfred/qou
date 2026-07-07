*For every partition $\lambda$ of $n \leq 7$, the single-generator
character $\chi_\lambda(\sigma)$ is a rational function of $q$
expressible as $c_\lambda \cdot h$ where $h = q - q^{-1}$ and
$c_\lambda \in \mathbb{Q}(q^2)$.*

*Self-conjugate partitions have integer coefficients:*

| Partition | $\chi(\sigma)/h$ | Note |
|:---------:|:----------------:|:----:|
| $[2,1]$ | $1$ | standard rep |
| $[3,1,1]$ | $3$ | H$_{5}$ Wigner |
| $[3,2,1]$ | $8$ | H$_{6}$ dominant (36% Plancherel) |
| $[4,1,1,1]$ | $10$ | H$_{7}$ self-conjugate |

*Pair characters (exact in $q$):*

$$\chi_{[3,1,1]}(\sigma_i \sigma_{i+1}) = h^2 = (q-q^{-1})^2$$
$$\chi_{[3,1,1]}(\sigma_i \sigma_j)_{|i-j|\geq 2} = h^2 - 2$$
$$\chi_{[3,1,1]}(\sigma_i \sigma_{i+1} \sigma_{i+2}) = -h$$

*Computed via seminormal form: $a_\rho = h/(1-q^{-2\rho})$
summed over standard Young tableaux.* $\square$
