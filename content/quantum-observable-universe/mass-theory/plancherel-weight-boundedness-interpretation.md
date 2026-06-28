**Remark (q-deformed alternative).**
The literature also uses a $q$-deformed weight
$\widetilde{w}_\lambda := \dim_q^2 V_\lambda / [n]_q!$, where
$\dim_q V_\lambda$ is the categorical $q$-dimension (a $q$-hook
product).  At generic $q \neq 1$ the sum $\sum_\lambda
\widetilde{w}_\lambda$ deviates from $1$ — empirically $\sim 1.51$ at
$q_0 = 1.109978595554181\ldots$ (50 dps) for $n = 12$ — so $\widetilde{w}$ is **not** a
probability measure.  The q-deformed quantities are recorded in the
witness data
([`wedderburn-strata-witness.json`](#)) for completeness but the
canonical $w_\lambda = (\dim V_\lambda)^2/n!$ is what closes
Plancherel-completeness arguments.

**Significance for mass-tower computations.**

Plancherel-weight boundedness is the formal reason that the
log-pairing $\Phi_k$ in
([universal residue](#prop:plancherel-term-7-formulation)) remains
$O(10)$ even when individual $\int_{A_\lambda}$ values span
$\sim 50$ orders of magnitude
([mass formula validation](#rem:mass-formula-validation)).  The
Plancherel measure compresses the per-$\lambda$ contributions into
a probability average, killing the divergence.  Without this
proposition, the logarithmic-weighting "magic" exploited by
mass-tower computations would be unjustified.
