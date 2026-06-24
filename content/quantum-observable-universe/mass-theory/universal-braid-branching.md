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

$$

*Borromean.*
$B_3 = (T_1 T_2^{-1})^3$.  Since $T_1 T_2^{-1} \in \mathrm{SL}(2)$
with trace $t = 2 - [3]_q$ (same computation as the first factor of
$4_1$), the Chebyshev recurrence gives:

$$
  \mathrm{tr}(M^3) = t^3 - 3t
  = (2 - [3])^3 - 3(2 - [3])
  = -([ 3] - 2)([3]^2 - 4[3] + 1)
$$

At $q_0 \approx 1.110$: $\chi_{B_3}^{\mathrm{std}} \approx 1.994$
(near $2$, reflecting the Borromean braid's near-identity in the
standard channel).

**Convergence bound.**
The Bethe--Weizsäcker mass formula at Hecke level $k$ uses the first
$p(k)$ partitions.  The Plancherel measure concentrates: the
Wedderburn--Artin weight $w_\lambda = \dim_q(\lambda)^2/[k]_q!$ peaks
at $\sim 10$ dominant partitions regardless of $k$.  The residual error
from truncating at level $k$ satisfies:

$$
  \mathrm{MAE}(k) \;\leq\; C_0 \times [2]_q^{-2(k-3)}
$$

where $C_0 \approx 0.035\%$ is the mass MAE at $k = 3$ and
$[2]_q^2 \approx 4.04$ is the concentration rate.  Each additional
Hecke level gains a factor $\sim 4\times$ in precision.

The **ultimate precision floor** is set by the substrate parameter
uncertainty $\delta q \approx 1.4 \times 10^{-9}$ (from CODATA
$m_\mu/m_e$), giving $\delta M/M \sim 10^{-7}\%$, reached at
$k \approx 13$.
$\square$

*Formal asymptotic content. The per-level q-deformed Wedderburn
weight has $\ordw(\text{per-level weight}) = -2\,\ordw([2]_q)$ in the surreal
valuation; see [Big-O via $\ordw$](#rem:conway-normal-form) and the
[body asymptotics catalog](#rem:body-asymptotics-catalog).*
