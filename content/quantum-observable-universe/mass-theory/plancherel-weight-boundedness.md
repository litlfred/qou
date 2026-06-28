**Proposition (Plancherel weights are a probability distribution).**
*Working over $A = H_n(R, q)$ at generic $q$ (so $A$ is semisimple),
the canonical Plancherel weights*

$$
  w_\lambda \;:=\; \frac{(\dim V_\lambda)^2}{n!},
  \qquad \lambda \,\vdash\, n,
$$

*— with $\dim V_\lambda = f_\lambda \in \mathbb{Z}_{>0}$ the classical
dimension of the Hecke irrep (number of standard Young tableaux of
shape $\lambda$) — satisfy the two probability-distribution axioms:*

1. *(Non-negativity.) Each $w_\lambda \in [0, 1]$.*
2. *(Normalisation.)*
   $$
     \sum_{\lambda \,\vdash\, n} w_\lambda \;=\; 1
     \quad \text{exactly in } \mathbb{Q}.
   $$

*Proof.*
The classical Plancherel identity for the symmetric-group regular
representation, lifted to the Hecke algebra via the Wedderburn--Artin
decomposition
([Wedderburn trace](#prop:wedderburn-trace-identity)):

$$
  \dim_\mathbb{Q} A \;=\; n!
  \;=\; \sum_{\lambda \,\vdash\, n} (\dim V_\lambda)^2.
$$

(The Hecke irrep dimensions $\dim V_\lambda$ are $q$-independent for
generic $q$ — they coincide with the symmetric-group irrep
dimensions $f_\lambda$.)  Dividing by $n!$ proves (2).  Each summand
is a non-negative ratio bounded by the total sum, proving (1).
$\square$

**Corollary (convergence of curvature-rank functionals).**
*The strata-sum
$\mathfrak{m}^{(k)}_{q,\mathcal{K}}(\mathcal{T})
= \sum_{\lambda \in \Lambda_k}
   w_\lambda \cdot \log\bigl|\!\int_{A_\lambda}\!\rho(\beta_\mathcal{K})
   \cdot \mathcal{T}\bigr|$
of the unified mass formula
([unified mass formula](#prop:unified-curvature-rank-mass-formula))
is bounded by $\sup_{\lambda \in \Lambda_k} \bigl|\log
\bigl|\!\int_{A_\lambda}\!\cdot\bigr|\bigr| \cdot \sum_{\lambda
\in \Lambda_k} w_\lambda \leq \sup |\log|\!\int|\!|$, since
$\sum_{\lambda \in \Lambda_k} w_\lambda \leq \sum_\lambda w_\lambda
= 1$.*

*The total mass functional
$\mathfrak{m}_{q,\mathcal{K}}(\mathcal{T}) = \sum_k \alpha_k
\mathfrak{m}^{(k)}_{q,\mathcal{K}}(\mathcal{T})$ is therefore
absolutely convergent for any bounded $|\alpha_k|$, with no
super-exponential divergence at large $n$.*

**Why this matters for mass-tower computations.**

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

**Plancherel distribution at $q_0 = 1.109978595554181\ldots$ (50 dps) (small $n$).**

See [Table](#tbl:plancherel-weight-boundedness-table-data).

Full tables for $n \in \{3, 4, 5, 6, 9, 12\}$ — including q-deformed
dimensions, signed content (chirality marker $= 0$), and
depth-stratified groupings used by mass-tower computations — are in
[`computations/wedderburn-strata-witness.json`](#).
