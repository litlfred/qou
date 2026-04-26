**Enumeration claim.**
The unified mass formula
([unified mass formula](#prop:unified-curvature-rank-mass-formula))
exhausts the Wedderburn decomposition of $A = H_n(R, q)$:
**every** partition $\lambda \vdash n$ appears in **exactly one**
curvature-rank stratum, and Plancherel completeness $\sum_\lambda
w_\lambda = 1$ certifies that no contribution is missed.

**Stratification map.**
By
([curvature-rank stratification](#prop:curvature-rank-gb-stratification)),
each central idempotent $e_\lambda \in Z(A)$ has a well-defined
GB-filtration depth $\mathrm{depth}(\lambda) =
\mathrm{height}(\lambda) - 1 \in \{0, 1, \ldots, n - 1\}$.  The
strata

$$
  \Lambda_k \;:=\; \{\lambda \,\vdash\, n \,:\, \mathrm{depth}(\lambda) = k\},
  \qquad k \in \{0, 1, \ldots, n - 1\},
$$

partition the set of partitions of $n$.  The mass functional
restricts to each stratum as

$$
  \mathfrak{m}^{(k)}_{q,\mathcal{K}}(\mathcal{T})
  \;=\; \sum_{\lambda \in \Lambda_k}
    w_\lambda \cdot \log\Bigl|\!\int_{A_\lambda}\!\rho(\beta_\mathcal{K}) \cdot \mathcal{T}\Bigr|,
$$

and the total is
$\mathfrak{m}_{q,\mathcal{K}}(\mathcal{T}) = \sum_{k=0}^{n-1} \alpha_k \cdot
\mathfrak{m}^{(k)}_{q,\mathcal{K}}(\mathcal{T})$.

**Small-$n$ enumeration.**

*Partitions of $n$, organised by depth $k = \mathrm{height}(\lambda)
- 1$:*

| $n$ | $\Lambda_0$ | $\Lambda_1$ | $\Lambda_2$ | $\Lambda_3$ | $\Lambda_{\geq 4}$ | $\#\{\lambda \vdash n\}$ |
|---|---|---|---|---|---|---|
| $2$ | $(2)$ | $(1,1)$ | — | — | — | $2$ |
| $3$ | $(3)$ | $(2,1)$ | $(1,1,1)$ | — | — | $3$ |
| $4$ | $(4)$ | $(3,1),(2,2)$ | $(2,1,1)$ | $(1^4)$ | — | $5$ |
| $5$ | $(5)$ | $(4,1),(3,2)$ | $(3,1,1),(2,2,1)$ | $(2,1^3)$ | $(1^5)$ | $7$ |
| $9$ | $(9)$ | $(8,1)\ldots(5,4)$ | $(7,1,1)\ldots(3,3,3)$ | $(6,1^3)\ldots(3,3,1,1,1)$ | $\geq$ remaining | $30$ |

*Each $\lambda$ enters exactly one column.  The total count agrees
with the partition number $p(n)$.*

**Plancherel completeness check.**
*The Wedderburn trace identity
([Wedderburn trace](#prop:wedderburn-trace-identity)) gives
$\sum_{\lambda \vdash n} \dim_q^2 V_\lambda = [n]_q!$ in $R$, hence*

$$
  \sum_{k = 0}^{n - 1} \sum_{\lambda \in \Lambda_k} w_\lambda
  \;=\;
  \sum_{\lambda \,\vdash\, n} w_\lambda
  \;=\; 1 \,\in\, R \otimes \mathbb{Q}.
$$

*Summing over all strata recovers Plancherel mass $1$, so the
stratified formula reproduces the full Markov trace exactly.  Any
quantity expressible as a Markov-trace evaluation on $A$ is captured
by enumerating $\{\Lambda_k\}_{k=0}^{n-1}$.*

**Mapping to the legacy "six terms".**
The historical 6-term/7-term decomposition of the unified mass
formula
([unified mass formula §legacy mapping](#prop:unified-curvature-rank-mass-formula))
groups strata as Term $1 = k{=}0$, Term $2 = k{=}1$, Term $3 = k{=}2$,
Term $5 = $ chirality projection inside $k \geq 2$, Term $6 = k{=}3$,
Term $7 = k \geq 4$.  Term $4$ is the universal Frobenius co-Casimir
$\sum_\lambda 1/\dim_q V_\lambda$, a complementary weighting that
runs over **all** $\lambda$ but with multiplicative (not additive)
role.  The 6/7-term language is therefore a coarsening of the
$k$-stratification — no partitions are dropped.

**Consequences.**

1. *No missed channels.* Any nuclear observable computed from a
   Markov-trace evaluation on $H_n(R, q)$ — mass, $Q$-value, knot
   factor, $F_{\mathrm{Pauli}}$, $\alpha_{\mathrm{EM}}$ correction
   — admits a finite Wedderburn-block expansion bounded by
   $\sum_\lambda w_\lambda = 1$.

2. *Plancherel boundedness.* Each stratum $\mathfrak{m}^{(k)}$ is
   bounded by $\sum_{\lambda \in \Lambda_k} w_\lambda \leq 1$;
   no super-exponential divergence.

3. *Falsifiability.* If a numerical observable lies outside the
   Plancherel-bounded sum over $\Lambda_0 \cup \cdots \cup
   \Lambda_{n-1}$, the framework is falsified.  Empirically the
   $A \leq 60$ certificates fit within Plancherel bounds
   ([mass-formula validation](#rem:mass-formula-validation)).
