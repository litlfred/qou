*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Proposition.**
*For any braid $K$ on $3$ strands and any partition $\lambda \vdash k$
with $k \geq 3$, the Frobenius character of $K$ in the irreducible
representation $\rho_\lambda$ of $H_k(R, q)$ is:*

$$
  \chi(K, \lambda)
  = f^{\lambda/[3]} \cdot \chi_K^{\mathrm{sym}}
  + f^{\lambda/[2{,}1]} \cdot \chi_K^{\mathrm{std}}
  + f^{\lambda/[1^3]} \cdot \chi_K^{\mathrm{alt}}
$$

*where $f^{\lambda/\mu} = |\mathrm{SYT}(\lambda/\mu)|$ counts
saturated chains from $\mu$ to $\lambda$ in Young's lattice, and
the three base characters are computed once from the Hoefsmit
seminormal form
([Hoefsmit seminormal form](#prop:hoefsmit-seminormal-form)):*

| *Knot $K$* | *$\chi_K^{\mathrm{sym}}$* | *$\chi_K^{\mathrm{std}}$* | *$\chi_K^{\mathrm{alt}}$* |
|:---:|:---:|:---:|:---:|
| *$4_1$ (figure-eight)* | *$1$* | *$2 - [3]_q$* | *$1$* |
| *$B_3$ (Borromean)* | *$1$* | *$(2 - [3])([3]^2 - 4[3] + 1)$* | *$1$* |
| *unknot (identity)* | *$1$* | *$2$* | *$1$* |
