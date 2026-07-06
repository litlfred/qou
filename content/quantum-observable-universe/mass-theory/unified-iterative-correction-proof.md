*Proof.*
By [prop:mass-coefficient-shadow-price](#prop:mass-coefficient-shadow-price),
the BW coefficient of partition $\lambda$ is the LP-dual variable
$u_\lambda^* = C_\lambda \cdot S_\lambda(Z, N, A)$.  The
categorical scale $C_\lambda = m_e \cdot H_q(\lambda)$ (the
$q$-hook product over the Young diagram of $\lambda$) is the
universal constant determined by the partition algebra, with no
nuclear data; the scaling function $S_\lambda(Z, N, A)$ is
realised at each step as $\ln|\mathrm{tr}\,\mathbf{M}_\lambda^{(0..A)}| -
\ln d_\lambda$ via the Young seminormal representation.

For $\lambda = (2,2) \vdash 4$ this recovers the dedicated Wigner
identity ([prop:wigner-np-pairing](#prop:wigner-np-pairing)):
$H_q((2,2)) = [3]_q \cdot [2]_q^2$; for $\lambda = (2,1) \vdash 3$
it reproduces the volume / surface / Coulomb decomposition
through their image under the Wedderburn embedding; for higher
partitions it adds the form-factor, $pn$-correlation, and
${[3,2,1]}$ pn-invisible corrections.

By the [Markov-trace normalization](#prop:wedderburn-trace-identity)
(the per-level budget is the Hecke-level scale $[k]_q!$, $k$ fixed), the dual
shadow prices satisfy a single budget constraint per Hecke
level; by Frobenius reciprocity
([prop:mass-coefficient-shadow-price](#prop:mass-coefficient-shadow-price),
branching corollary), shadow prices at level $k+1$ are
determined by those at level $k$.  Telescoping per-step log-trace
differences across $k = 1, \ldots, A$ yields the closed-form
$B_\lambda$.

The Kerov $q$-hook walk \cite{kerov1996} gives the iterative
Markov-chain interpretation of $\mathrm{tr}\,\mathbf{M}_\lambda^{(0..k)}$
as a transition kernel on the Young lattice; the
Féray–Méliot $q$-Plancherel CLT \cite{feray-meliot2012}
guarantees the asymptotic convergence of the accumulator at
rate $O(1/\sqrt{A})$ across Hecke levels.

The three legacy mechanisms specialise:
- *deuteron ($A = 2$, dedicated $\alpha_{\mathrm{Borromean}}
  \cdot \hat V_e$):* the $A = 2$ slice of the LP-dual
  accumulator, dominated by the $(2,1)$ and $(2,2)$ shadow
  prices;
- *knot factor ($A = 3, 4$, dedicated $a(N) = 1 - h^2,
  (1 - h^2)^2$):* the $A = 3, 4$ slices of the LP-dual
  accumulator, where the $(2,1)$ and $(3,1)$ contributions
  reproduce the figure-eight and Borromean amphicheiral factors;
- *Wigner energy ($k \geq 5$, dedicated
  $-\Delta_W \cdot T(T+1)/A$):* the $k = 4, 5$ self-conjugate
  shadow prices ($\lambda = (2,2)$ and $(3,1,1)$), which
  vanish on isolated $pn$ crossings (extremal cancellation,
  [prop:confined-knot-binding](#prop:confined-knot-binding))
  but are nonzero on collective $pn$ patterns.

$\square$

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
