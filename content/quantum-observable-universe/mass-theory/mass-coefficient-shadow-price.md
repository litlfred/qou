**Proposition.**
*Each coefficient of the QOU mass formula
([six-term mass formula](#thm:six-term-mass-formula-complete))
is the shadow price (LP dual variable) of the corresponding
partition's Frobenius positivity constraint in the nuclear
operator selection LP.*

(j-i)$:
   - $c(\lambda) > 0$: volume-type ($A$-dependent)
   - $c(\lambda) = 0$: isospin-type ($T(T+1)/A^p$)
   - $c(\lambda) < 0$: charge-type ($Z$-dependent)

The factorisation is unique because the Wedderburn blocks are
orthogonal under the Frobenius pairing: different partitions
contribute to linearly independent scaling functions.

**Mass-formula decomposition.**  The binding energy is:

$$
  B(Z,N) = \sum_{\lambda} C_\lambda \cdot S_\lambda(Z,N,A)
           \cdot m_e
$$

Each term of the QOU six-term mass formula is one shadow price
$u_\lambda^*$ (or the sum of a conjugate pair
$u_\lambda^* + u_{\lambda'}^*$ when $\lambda' = \lambda^\vee$).
The coefficient $C_\lambda \cdot m_e$ is the shadow price
evaluated at the normalisation point where $S_\lambda = 1$.

**Corollary (coefficient at each level).**
By the [Wedderburn trace identity](#prop:wedderburn-trace-identity),
$\sum_\lambda \dim_q(\lambda)^2 = [k]_q!$.  This constrains the
total shadow-price budget: the trace identity is the dual
feasibility constraint ensuring all $u_\lambda^*$ are consistent.
The budget at level $k$ is $[k]_q!$; the marginal budget from
advancing $k \to k+1$ is $[k+1]_q! - [k]_q! = [k]_q! \cdot ([k+1]_q - 1)$.

**Corollary (branching rule for coefficients).**
The branching $\mathrm{Res}^{H_{k+1}}_{H_k} V_\mu
= \bigoplus_{\lambda} V_\lambda$ induces a constraint on the
level-$(k{+}1)$ shadow prices via Frobenius reciprocity:

$$
  C_\mu = \sum_{\lambda : \lambda \nearrow \mu}
    \frac{\dim_q(\mu)}
         {\sum_{\mu' : \lambda \nearrow \mu'} \dim_q(\mu')}
    \cdot C_\lambda
$$

where $\lambda \nearrow \mu$ denotes that $\mu$ is obtained from
$\lambda$ by adding one cell.  This propagates known coefficients
from level $k$ to level $k{+}1$ without fitting.
$\square$
