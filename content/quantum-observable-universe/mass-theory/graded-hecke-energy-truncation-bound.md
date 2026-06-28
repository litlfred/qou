**Proposition (graded Hecke energy truncation bound).**
*Let $\hat{\beta}_K$ be the closure of a braid $\mathcal{B}_K \in B_n$, let
$\mathfrak{M}_K$ be the stable highest-weight KLR module
\cite{khovanovlauda2009, brundankleshchev2009} associated to
$\hat{\beta}_K$, and let*

$$
  P_K(q) \;=\; \sum_{d \in \mathbb{Z}}
    \dim_R \mathrm{Hom}_{\mathcal{K}_n}(P_d, \mathfrak{M}_K) \, q^d
  \;\in\; \mathbb{Z}_{\geq 0}[q^{\pm 1/2}]
$$

*be the mass-spectrum generating function of $K$
([mass-spectrum generating function](#rem:mass-spectrum-generating-function)).
Then $P_K(q)$ has at most $\ell(K, q_0) + 1$ nonzero terms, where
$\ell(K, q_0)$ is the
[confinement level](#def:confinement-level)
of $K$ at the substrate value $q_0$.*

## Computational consequence

For numerical evaluation of $\mathrm{tr}_M(T_w(\mathcal{B}_K), q_0) =
P_K(q_0)$, only the grades $d \in \{0, 1, \ldots, \ell(K, q_0)\}$
need to be enumerated. The naive enumeration over all $p(n)$
partitions of the $n$ strands of $\mathcal{B}_K$ overcounts:
many partitions contribute zero or negligibly to the relevant
grades. **The truncation reduces the effective work from $p(n)$
partitions to at most $\ell(K, q_0) + 1$ effective grades.**

Empirically at $q_0 \approx 1.110$:

See [Table](#tbl:graded-hecke-energy-truncation-bound-table-data).

Speedups assume $\ell(K, q_0) + 1$ effective grades vs $p(n)$
partitions; conservative since the per-grade cost is comparable.

## Stratified-cache compatibility

The result also enables **resumable** numerical evaluation: a
partial cache `chi-{atom}-h{n}.witness.json` can be made
graded-stratified, so partial completion at grade $\ell^\star$
exposes $\mathrm{tr}_{M, \leq \ell^\star}(\mathcal{B}_K)$ immediately.
Resuming becomes a matter of picking up at grade $\ell^\star + 1$
rather than partition $i+1$ — a structural property the partition-
indexed cache does not have.

## Empirical witness

[`computations/probes/graded_hecke_energy_probe.py`](https://github.com/litlfred/qou/blob/claude/wire-applied-uniqueness-mass-table/computations/probes/graded_hecke_energy_probe.py)
demonstrates the stratification on the proton/neutron/deuteron
braids at the canonical $q_0$, emitting per-grade $c_d$ values
and confirming the truncation bound holds. Output:
`graded-hecke-energy-probe.witness.json`.
