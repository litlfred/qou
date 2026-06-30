For nuclei with **even mass number** $A$, the raw character
sum is negative
([parity regime](#thm:parity-regime-selection)).
The physical Q-value is obtained by restricting the sum to
**Frobenius-positive** configurations — those where both
parent and daughter have non-negative Markov traces.

## Statement

**Proposition.**
*For even $A$: a channel configuration
$(c_1, \ldots, c_A) \in \{\mathrm{triv}, \mathrm{conf},
\mathrm{unconf}, \mathrm{sign}\}^A$ is* Frobenius-positive
*if and only if:*

$$
  m_{e,\mathrm{par}} = \prod_{m=1}^{A} G_{n_m}(c_m) \geq 0
  \quad \text{and} \quad
  m_{e,\mathrm{dau}} = \prod_{m=1}^{A} G_{n'_m}(c_m) \geq 0
$$

*The sign of each configuration product is determined by the
spectator factor.  A fraction $2^{-(A+1)}$ of the configurations —
$2^{A-1}$ out of $4^A$ — are excluded.*

## Connection to the confinement LP

The Frobenius positivity constraint is the continuous
analogue of the LP feasibility constraint
$Gx \geq 0$ in the
[confinement LP](#prop:confinement-lp).
In the discrete (branching) setting, it acts as a
**configuration filter**: only configurations that produce
non-negative mass elements for both
parent and daughter nuclei contribute to the Q-value.

## Computational complexity

For the ${}^6\mathrm{He} \to {}^6\mathrm{Li}$ decay ($A = 6$):
$4^6 = 4096$ configurations, of which $2^5 = 32$ are excluded.
The Frobenius-filtered sum gives
$Q \approx 3.637$ MeV (experiment: $3.508$ MeV, error $+3.68\%$).

For large even $A$ (e.g. ${}^{14}\mathrm{C}$, $A = 14$):
$4^{14} = 268{,}435{,}456$ configurations require either
enumeration or a closed-form simplification of the
Frobenius-filtered sum.
