**Proposition.**
*For any partition $\lambda \vdash k$ and substrate parameter $q > 1$,
the Frobenius character of the figure-eight braid
$4_1 = \sigma_0\sigma_1^{-1}\sigma_0^{-1}\sigma_1$ in the irreducible
representation $\rho_\lambda$ of $H_k(R, q)$ is determined by three
branching multiplicities in Young's lattice:*

$$
  \chi(4_1, \lambda)
  = \bigl(f^{\lambda/[3]} + f^{\lambda/[1^3]} - f^{\lambda/[2{,}1]}\bigr)
  \;-\; f^{\lambda/[2{,}1]} \cdot h^2
$$

*where $f^{\lambda/\mu} = |\mathrm{SYT}(\lambda/\mu)|$ is the number of
standard Young tableaux of skew shape $\lambda/\mu$
(equivalently, the number of saturated chains from $\mu$ to $\lambda$
in Young's lattice), and $h = q - q^{-1}$.*

*The two components are:*

- *$a_\lambda = f^{\lambda/[3]} + f^{\lambda/[1^3]} - f^{\lambda/[2{,}1]}$:
  the classical part (the $S_k$ character of the 3-cycle $(123)$
  embedded in $S_k$).*
- *$b_\lambda = -f^{\lambda/[2{,}1]}$:
  the $q$-deformation correction, always $\leq 0$.*

*Verified to machine precision ($< 10^{-12}$) against explicit Hoefsmit
seminormal matrix computation for all 191 partitions at $k = 3$ through
$k = 11$.*

**Archimedean specialisation (§7c).** This block is stated over the real field $\mathbb{R}$ — the archimedean side of the substrate wall: its constructs are real-valued (physical observables, real-analytic bounds, or numerical evaluations at the substrate parameter $q_0$) rather than generic-ring $q$-deformation data. The generic categorical / $q$-deformation machinery it draws on is stated over an abstract coefficient ring in its own blocks; only the archimedean realisation is specialised here.
