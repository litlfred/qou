**Proposition.**
*Every per-partition contribution to the binding energy is the
LP-dual shadow price of that partition's Frobenius positivity
constraint, multiplied by its $q$-hook product and accumulated
step by step from $A = 1$ over the per-step (Young seminormal)
trace of the NF transition.  No special-case branching is
required for any value of $A$.*

*The unified accumulator is, for any partition $\lambda \vdash k$
($k = 2, \ldots, K$):*

$$
  B_\lambda(Z, N)
  = m_e \cdot H_q(\lambda) \cdot u_\lambda \cdot
    \big( \ln\big| \mathrm{tr}\, \mathbf{M}_\lambda^{(0..A)} \big|
          - \ln d_\lambda \big),
$$

*and the total unified correction is the sum:*

$$
  B_{\mathrm{unified}}(Z, N) = \sum_{\lambda} B_\lambda(Z, N).
$$

*Components:*
- *$H_q(\lambda) = \prod_{x \in \lambda} [h_x(\lambda)]_q$ is the
  $q$-hook product (the categorical scale $C_\lambda = m_e \cdot
  H_q(\lambda)$ — for $\lambda = (2,2)$ this is
  $[3]_q \cdot [2]_q^2 \approx 6.29$ MeV, the empirical Wigner
  scale \cite{satula1997});*
- *$u_\lambda = w_\lambda / d_\lambda - 1/[k]_q!$ is the LP-dual
  shadow price of $\lambda$'s Frobenius positivity constraint
  ([prop:mass-coefficient-shadow-price](#prop:mass-coefficient-shadow-price));
  the constant $1/[k]_q!$ is the dual variable of the
  normalisation $\mathbf{1}^T x = n_{\mathrm{target}}$ (the
  smallest $w_\lambda / d_\lambda$ across partitions of $k$,
  attained by the trivial sym/alt one-dimensional reps);*
- *$d_\lambda = \dim(\lambda)$ is the classical dimension (number
  of standard Young tableaux);*
- *$\mathbf{M}_\lambda^{(0..A)}$ is the Young-seminormal-form
  matrix product over all NF crossings introduced through
  step $A$, embedded into the Hecke generators
  $\sigma_1, \ldots, \sigma_{k-1}$ of $H_k(R, q)$ with cyclic
  generator index.*

*One-dimensional representations have $w_\lambda / d_\lambda =
1/[k]_q!$ (so $u_\lambda = 0$); they contribute nothing to
$B_{\mathrm{unified}}$.  Only mixing partitions
($d_\lambda \geq 2$) carry shadow-price weight.*

*Per-step formulation (energy-additive, restartable witness):*

$$
  \Delta B_\lambda(\mathrm{step}\ k)
  = m_e \cdot H_q(\lambda) \cdot u_\lambda \cdot
    \Big( \ln\big| \mathrm{tr}\, \mathbf{M}_\lambda^{(0..k)} \big|
        - \ln\big| \mathrm{tr}\, \mathbf{M}_\lambda^{(0..k-1)} \big| \Big),
$$

*so witness rows
$(A, Z_k, N_k, \mathrm{nuc}, \{\Delta B_\lambda\}_\lambda,
\mathrm{cumulative})$ uniquely determine the next.*

**Algorithm summary** (one block, no special cases, $A = 1$ onward):

```
for k in 2..K_PARTITION_MAX:
  for partition λ of k:
    H_q(λ)   = ∏_{x∈λ} [h_x]_q
    d_λ      = #SYT(λ)
    w_λ      = d_q(λ)^2 / [k]_q!
    y_λ      = w_λ / d_λ − 1/[k]_q!
    σ_1..σ_{k−1} = YSN matrices in λ
for step = 1..A:
  for each partition λ:
    M_λ      ← M_λ × ∏(c*σ_g + d*I) over new crossings at this step
    ΔB_λ     = m_e * H_q(λ) * y_λ * (ln|Tr M_λ| − previous)
    cumulative_λ += ΔB_λ
    record witness row
B_unified = Σ_λ cumulative_λ
```

**Witness:** `mass-qvalue-by-level.witness.json` — every isotope
($^1$H to $^{208}$Pb), per-step rows recording per-partition
contributions; restartable from any
$(A, Z_k, N_k, \{\ln|\mathrm{tr}|_\lambda\}, \mathrm{cumulative})$.

**Comparison snapshot** (binding energy at $k = 5$, MeV):

See [Table](#tbl:unified-iterative-correction-table-data).

The unified path uses **one** symbolic algorithm with **zero**
fitted parameters and **no special-case branches**.  The
discrepancy between the two paths quantifies the residual that
the LP-dual accumulator over $k \leq K_{\max}$ does not absorb;
extending $K_{\max}$ above $6$ adds further partitions, with
shadow prices and $q$-hooks computed by the same formulas.

*Formal asymptotic content. The Féray–Méliot rate $O(1/\sqrt{A})$
has $\ordw(\text{accumulator}) = -\tfrac{1}{2}\,\ordw(A)$ in the surreal valuation;
see [Big-O via $\ordw$](#rem:conway-normal-form) and the
[body asymptotics catalog](#rem:body-asymptotics-catalog).*
