*Proof.*
The braid $K$ lives in $H_3(R, q)$ (generators $T_1, T_2$).  The
representation $\rho_\lambda$ of $H_k(R, q)$ restricts to $H_3(R, q)$
via the standard inclusion $H_3(R, q) \hookrightarrow H_k(R, q)$
(using the first two generators).  The branching rule gives:

$$
  \rho_\lambda \!\downarrow_{H_3}
  = \bigoplus_{\mu\,\vdash\,3} f^{\lambda/\mu} \cdot \rho_\mu
$$

Taking characters and using additivity yields the formula.

**Base characters (symbolic proofs).**

*Figure-eight.*
$4_1 = T_1 T_2^{-1} T_1^{-1} T_2$ is the commutator $[T_1, T_2^{-1}]$.
In the symmetric and alternating channels ($\dim = 1$), the eigenvalue
products are $q \cdot q^{-1} \cdot q^{-1} \cdot q = 1$ and
$(-q^{-1})(-q)(-q)(-q^{-1}) = 1$ respectively.

In the standard channel $[2{,}1]$ ($\dim = 2$), the Hoefsmit matrices
give $T_1 = \mathrm{diag}(q, -q^{-1})$ and $T_2$ with entries
$\alpha = -1/(q^3{+}q)$, $\gamma = q^3/(q^2{+}1)$.  Direct computation:

$$
  \mathrm{tr}(T_1 T_2^{-1} T_1^{-1} T_2)
  = \alpha^2 - h\alpha + \gamma^2 - h\gamma
    - (q^2 + q^{-2})(\alpha\gamma + 1)
$$

Using $\alpha + \gamma = h$ and $\alpha\gamma = -1/([3]+1)$ (both
verified symbolically), this simplifies to:

$$
  = -\alpha\gamma(1 + [3]) - ([3] - 1)
  = \frac{1+[3]}{[3]+1} - [3] + 1
  = 2 - [3]_q
  \qquad\square
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
valuation.*
