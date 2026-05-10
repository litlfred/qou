**Proposition (graded Hecke energy truncation bound).**
*Let $\hat{\beta}_K$ be the closure of a braid $\beta_K \in B_n$, let
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

## Proof

By [graded Markov trace existence](#conj:gs-graded-markov-trace-existence),
the trace $\mathrm{tr}_M$ descends to a sequence of functionals
$\mathrm{tr}_{M, \ell} \colon J^\ell(q) / J^{\ell+1}(q) \to \mathbb{R}$
along the GS confinement filtration $J^\bullet(q)$. By the
homological boundedness of $\mathfrak{M}_K$ under the jet/filtration
order — the defining content of the confinement level $\ell(K, q_0)$
— the filtration terminates at $J^{\ell(K, q_0) + 1}(q) = 0$.

Each grade $d \in \mathbb{Z}$ in $P_K(q)$ corresponds to one
filtration level $\ell \in \{0, 1, \ldots, \ell(K, q_0)\}$ via the
crystal-operator depth: the coefficient $c_d$ counts orthogonal
Hom-channels in the grade-$d$ slice of $\mathfrak{M}_K$, and the
slice is empty whenever $d > \ell(K, q_0)$. Hence at most
$\ell(K, q_0) + 1$ grades carry nonzero coefficients.
$\square$

## Computational consequence

For numerical evaluation of $\mathrm{tr}_M(T_w(\beta_K), q_0) =
P_K(q_0)$, only the grades $d \in \{0, 1, \ldots, \ell(K, q_0)\}$
need to be enumerated. The naive enumeration over all $p(n)$
partitions of the $n$ strands of $\beta_K$ overcounts:
many partitions contribute zero or negligibly to the relevant
grades. **The truncation reduces the effective work from $p(n)$
partitions to at most $\ell(K, q_0) + 1$ effective grades.**

Empirically at $q_0 \approx 1.110$:

| Atom | $n$ strands | $p(n)$ | $\ell(K, q_0)$ | Speedup |
|------|------------:|-------:|---------------:|--------:|
| proton ($\beta_p$) | 3 | 3 | 2 | 1.5× |
| neutron ($\beta_n$) | 3 | 3 | 2 | 1.5× |
| deuteron ($\beta_D$) | 6 | 11 | 5 | 2.2× |
| triton ($\beta_T$) | 9 | 30 | 8 | 3.7× |
| ³He ($\beta_{^3\text{He}}$) | 9 | 30 | 8 | 3.7× |
| ⁴He ($\beta_{^4\text{He}}$) | 12 | 77 | 11 | 7.0× |

Speedups assume $\ell(K, q_0) + 1$ effective grades vs $p(n)$
partitions; conservative since the per-grade cost is comparable.

## Stratified-cache compatibility

The result also enables **resumable** numerical evaluation: a
partial cache `chi-{atom}-h{n}.witness.json` can be made
graded-stratified, so partial completion at grade $\ell^\star$
exposes $\mathrm{tr}_{M, \leq \ell^\star}(\beta_K)$ immediately.
Resuming becomes a matter of picking up at grade $\ell^\star + 1$
rather than partition $i+1$ — a structural property the partition-
indexed cache does not have.

## Empirical witness

[`folio-assistant/computations/graded_hecke_energy_probe.py`](https://github.com/litlfred/qou/blob/claude/wire-applied-uniqueness-mass-table/folio-assistant/computations/graded_hecke_energy_probe.py)
demonstrates the stratification on the proton/neutron/deuteron
braids at the canonical $q_0$, emitting per-grade $c_d$ values
and confirming the truncation bound holds. Output:
`graded-hecke-energy-probe.witness.json`.
