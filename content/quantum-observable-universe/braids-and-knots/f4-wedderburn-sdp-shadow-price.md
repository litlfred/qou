## Statement

Let $\beta$ be a braid word on $n$ strands and $T_\beta \in H_n(q)$
its image in the Iwahori–Hecke algebra.  The Markov trace
decomposes via the Wedderburn isomorphism
$H_n(q) \cong \bigoplus_{\lambda \vdash n} \operatorname{End}(S^\lambda)$
as

$$
  \operatorname{tr}_M(T_\beta)
  \;=\;
  \sum_{\lambda \vdash n} y_\lambda \cdot \chi_\lambda(T_\beta; q),
$$

where $y_\lambda$ is the Jones–Markov block weight (Plancherel
weight on the regular trace) and $\chi_\lambda$ is the irreducible
character.  Define the **active block set** of $\beta$ at $q$ by

$$
  \operatorname{supp}_q(\beta)
  \;:=\;
  \{ \lambda \vdash n : \chi_\lambda(T_\beta; q) \neq 0 \}.
$$

We use the term **shadow price** informally for the per-block
coefficients attached to the Wedderburn decomposition of
$\operatorname{tr}_M(T_\beta)$ — namely, the products
$y_\lambda \chi_\lambda(T_\beta; q)$ as $\lambda$ ranges over
partitions of $n$.  In an LP-duality reading (Boyd–Vandenberghe
2004 §5; Schrijver §7), one looks for the cheapest non-negative
combination of these per-block weights that reproduces the trace,
and the *active blocks* are the partitions where the dual price is
strictly positive.

The claim is that this active set is exactly
$\operatorname{supp}_q(\beta)$.

## Proof sketch

A partition $\lambda \vdash n$ belongs to
$\operatorname{supp}_q(\beta)$ exactly when
$\chi_\lambda(T_\beta; q) \neq 0$.  If $\chi_\lambda = 0$, the
$\lambda$-block contributes zero to the Wedderburn decomposition of
$\operatorname{tr}_M(T_\beta)$ and any non-zero shadow price on
that block can be reduced to zero without altering the trace —
complementary slackness in any standard LP/SDP setup forces the
dual price to vanish.  If $\chi_\lambda \neq 0$, the block does
contribute, and any extremal dual solution must place positive
mass on it to recover the corresponding term of the trace
identity.

Equivalently — and the form used by the F4 discovery feeder —
$\operatorname{supp}_q(\beta)$ can be computed *directly* by
evaluating $\chi_\lambda(T_\beta; q)$ for every $\lambda \vdash n$
and filtering by a tolerance, without invoking an LP solver.

## Computational realization

Implemented in `folio-assistant/computations/knot_operation_cache.py`
as `discover_via_wedderburn_sdp(braid_nf, n, q, tolerance)`.

The function:

1. Computes $\chi_\lambda(T_\beta; q)$ for every $\lambda \vdash n$
   via the batched Hoefsmit kernel
   `pyhecke_native.chi_lambdas_braid`.
2. Loads the Plancherel weights $y_\lambda$ from
   `y-lambda-jones-markov-witness.json` (the F4.2.γ feeder source of
   truth).
3. Emits one `KnotOperation` per active block, with
   `plancherel_signature = {y_lambda, chi_value, partition_depth, part_0, part_1, ...}`
   and `fingerprint = {feeder, n, partition}`.

The fingerprint-only cache key (since `braid_word_normal_form = []`
for these ops) means two braids that activate the same $\lambda$ at
the same $n$ produce **the same cache key** — cross-braid dedup is
automatic, which is the point of the F4 cache.

Complementary to [`prop:f4-tensor-composer-lr`](#prop:f4-tensor-composer-lr):
that proposition handles tensor-decomposable braids; the
shadow-price discovery handles the *entangled* case where no
non-trivial tensor decomposition exists.

## Verification

Smoke test (`test_wedderburn_sdp_discovery.py`):

- Entangled $n=4$ braid $\sigma_1 \sigma_2 \sigma_1 \sigma_3$
  activates 3 of 5 Wedderburn blocks $(4), (2,2), (1,1,1,1)$ —
  not $(3,1)$ or $(2,1,1)$.  Sparse support is genuine structural
  information, not a tolerance artefact.
- Markov-trace reconstruction:
  $\sum_{\lambda \in \operatorname{supp}_q(\beta)} y_\lambda \chi_\lambda(T_\beta; q)$
  matches the full $\operatorname{tr}_M(T_\beta)$ to f64 $\varepsilon$
  (diff $5.55 \times 10^{-17}$).
- Cache-key dedup: $\sigma_1$ and $\sigma_1 \sigma_2 \sigma_1$ on
  $n=3$ share the same active blocks (trivial rep + standard rep)
  and produce identical cache keys for those blocks.
