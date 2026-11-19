*Proof.*
By [Frobenius shadow-price identity](#prop:mass-coefficient-shadow-price),
the BW coefficient of partition $\lambda$ is the LP-dual variable
$u_\lambda^* = C_\lambda \cdot S_\lambda(Z, N, A)$.  The
categorical scale $C_\lambda = m_e \cdot H_q(\lambda)$ (the
$q$-hook product over the Young diagram of $\lambda$) is the
universal constant determined by the partition algebra, with no
nuclear data; the scaling function $S_\lambda(Z, N, A)$ is
realised at each step as $\ln|\mathrm{tr}\,\mathbf{M}_\lambda^{(0..A)}| -
\ln d_\lambda$ via the Young seminormal representation.

For $\lambda = (2,2) \vdash 4$ this recovers the dedicated Wigner
identity ([$T{=}0$ Wigner $np$ pairing](#prop:wigner-np-pairing)):
$H_q((2,2)) = [3]_q \cdot [2]_q^2$; for $\lambda = (2,1) \vdash 3$
it reproduces the volume / surface / Coulomb decomposition
through their image under the Wedderburn embedding — a step this
proof does **not** discharge, and which the corpus still cannot
supply.

The obstruction is one of shape.  The block-diagonal Wedderburn embedding is a concrete construction, but it has
type $\bigoplus_\lambda M_{f^\lambda} \to M_{n!}$: it assembles blocks
into one matrix rather than splitting one block's scalar $C_{(2,1)}$ into
three coefficients.  The landing in $M_{n!}$ is additionally conditional on
the RSK dimension identity $\sum_\lambda (f^\lambda)^2 = n!$, carried here as an explicit classical combinatorial hypothesis.

That objection is a **theorem** rather than a remark.  The naive form — "three
independent coefficients cannot come from one scalar" — is false, since
one real encodes three set-theoretically.  Under **linearity**, which
this corpus already assumes for the Markov trace, it is true: that trace
factors through the block *traces*, so a functional of that form
supported at a single $\lambda$ is exactly $c_\lambda \cdot
\operatorname{tr}(x_\lambda)$ — one coefficient against one number — and
any three such functionals are linearly dependent, with an explicit dependence relation.

This does not make the clause false; it rules out the route the clause
names, whenever that route is linear, factors through the Markov trace,
and is localised at $(2,1)$.  It also says where the room is, which is
the more useful half: $f^{(2,1)} = 2$, so the block is $M_2(\mathbb{R})$
— **four** real dimensions, of which the trace reads one.  The
information wanted is present in the block and destroyed by tracing it
— itself a theorem: whenever a block
has dimension at least $2$ there are **distinct** decompositions on
which every block trace agrees, so every trace-factoring functional,
the Markov trace included, takes the same value on both.  Instantiating
that at $(2,1)$ needs $f^{(2,1)} = 2$; that value follows from the Frame–Robinson–Thrall
hook-length formula, so non-separation by trace at $(2,1)$ holds
unconditionally.  The general theorems keep the bound as a hypothesis
because they are about any block of dimension $\geq 2$.  The boundary
is real: $f^{(1,1)} = 1$, so at the charge shape the block *is* its
trace and none of this applies.  A derivation reading the block rather than its
trace is not blocked by any of this — and that is constructive
rather than merely permitted: one can exhibit three linearly independent block-reading functionals at
$(2,1)$, the exact complement of the three trace-factoring ones being
dependent.  It does **not** identify those three with volume, surface
and Coulomb; three independent functionals existing is a *necessary*
condition for such a match rather than evidence of one.  So the clause remains an open obligation rather than a
derivation; for higher
partitions it adds the form-factor, $pn$-correlation, and
${[3,2,1]}$ pn-invisible corrections.

By the [Markov-trace normalization](#prop:wedderburn-trace-identity)
(the per-level budget is the Hecke-level scale $[k]_q!$, $k$ fixed), the dual
shadow prices satisfy a single budget constraint per Hecke
level; by Frobenius reciprocity
([Frobenius shadow-price identity](#prop:mass-coefficient-shadow-price),
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
- *Wigner energy ($k = 4$, dedicated
  $-\Delta_W \cdot T(T+1)/A$):* the $k = 4$ self-conjugate
  shadow price $\lambda = (2,2)$, which
  vanishes on isolated $pn$ crossings (extremal cancellation,
  [confined-knot binding decomposition](#prop:confined-knot-binding))
  but is nonzero on collective $pn$ patterns.  Under convention D
  no self-conjugate partition beyond $k = 4$ can contribute:
  self-conjugacy forces $\ell(\lambda) = \lambda_1$, so the row cap
  $\ell(\lambda) \leq 2$ admits only $(1)$, $(2,1)$ and $(2,2)$, and a
  block with $\tilde w_\lambda = 0$ has $C_\lambda = 0$ and hence
  $u_\lambda^* = 0$ at every $(Z, N)$ — the vanishing is upstream of the
  scaling function, so no $S_\lambda$ restores it.

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

Evaluating this recurrence step by step across $^1\mathrm{H}$ through $^{208}\mathrm{Pb}$ records the cumulative per-partition contributions $(A, Z_k, N_k, \{\ln|\mathrm{tr}|_\lambda\})$.

**Comparison snapshot** (binding energy at $k = 5$, MeV):

See [Table](#tbl:unified-iterative-correction-table-data).

Only the $\mathrm{BW}(k{=}5)$ column of that comparison agrees with
experiment ($^3\mathrm{H} \to {}^3\mathrm{He}$: $0.018228$ against
$0.01861$ measured). The NF-trace $Q$-values are not confirmed: their
recorded tolerances were set just above each discrepancy, and a bound
sized to its own miss is a fit.

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
