# Universal branching rule refactor — plan

## Current state

`atom_per_generator_volumes(Z, N, m_pp, m_pn, m_nn)` accumulates
per-generator `(a, b, sp, ap)` channel state using **H_3 Wedderburn
weights** `w_sym`, `w_std`, `w_alt` uniformly at every generator.

This is **wrong** for A-nucleon atoms: the atom braid lives in
H_{3A}(q), not H_3(q). The correct Wedderburn decomposition sums
over partitions λ ⊢ 3A with weights w_λ(q) = d_q(λ)²/[3A]_q!.

Directly building H_{3A} YSN matrices for all λ ⊢ 3A is expensive
(p(3A) grows fast; p(12) = 77, p(60) ≈ 10⁶).

## Universal branching rule (Ch 3 `universal-braid-branching.md`)

For any K ∈ H_3(q) (3-strand braid) and any λ ⊢ k, k ≥ 3:

    χ(K, λ) = f^{λ/[3]} · χ_K^sym + f^{λ/[2,1]} · χ_K^std + f^{λ/[1³]} · χ_K^alt

where f^{λ/μ} = |SYT(skew shape λ/μ)| = # saturated chains in
Young's lattice from μ to λ.

## Extension to A nucleons (tensor branching)

For A nucleons K_i ∈ H_3(q) (disconnected tensor, free baseline),
the correct decomposition is via the iterated **Littlewood-Richardson
coefficient** `c^λ_{μ_1,…,μ_A}`:

    χ_free(λ) = Σ_{(μ_1,…,μ_A), μ_i ⊢ 3} c^λ_{μ_1,…,μ_A}
                · Π_i χ^{μ_i}(K_i)

where `c^λ_{μ_1,…,μ_A} = ⟨s_{μ_1} · s_{μ_2} · … · s_{μ_A}, s_λ⟩`
in the symmetric-function Hall inner product.

> **Note (2026-05-30).** An earlier draft of this plan used
> `f^{λ/(μ_1 ⊔ … ⊔ μ_A)}` (skew-SYT count of the sorted concatenation)
> in place of the LR coefficient. **That formula is incorrect** —
> see [`docs/audits/2026-05-30-universal-branching-multinucleon-gap.md`](../../docs/audits/2026-05-30-universal-branching-multinucleon-gap.md)
> for counterexamples (e.g. λ=(2,2), μ_1=μ_2=(1,1): `f^{concat}=0`
> but `c^λ=1`).

For atom with inter-nucleon couplings, the inter-nucleon generators
σ_j ∈ H_{3A} must be handled separately. Options:

1. **Left/right-term decomposition**: split σ_j into symmetric and
   antisymmetric pieces via the Hecke relation, accumulate per
   partition.

2. **Young symmetrizer**: apply the idempotents e_μ · e_ν to
   resolve adjacent pair couplings between nucleon blocks.

## Implementation sketch

```python
def atom_character_branching(Z, N, m_pp, m_pn, m_nn, lambda_partition):
    """Compute χ_λ(W_atom) via universal branching rule."""
    A = Z + N
    # Per-nucleon H_3 channel characters
    K_protons  = [h3_characters(proton_cross) for _ in range(Z)]
    K_neutrons = [h3_characters(neutron_cross) for _ in range(N)]
    # Accumulate over partition sequences
    total = 0
    for mu_seq in product([[3],[2,1],[1,1,1]], repeat=A):
        # Verify mu_seq concatenation fits inside lambda
        mu_concat = concatenate_partitions(mu_seq)
        if not fits_inside(mu_concat, lambda_partition):
            continue
        f_lambda_mu = skew_syt_count(lambda_partition, mu_concat)
        prod_chi = 1
        for i, mu in enumerate(mu_seq):
            K_i = K_protons[i] if i < Z else K_neutrons[i - Z]
            prod_chi *= K_i[mu_to_channel(mu)]
        total += f_lambda_mu * prod_chi
    # Apply inter-nucleon σ corrections (m_pp, m_pn, m_nn)
    # ...
    return total
```

## Gap

- ~~Skew-SYT count `f^{λ/μ}` for general λ ⊢ 3A, μ = μ_1 ⊔ ... ⊔ μ_A
  needs a generating-function implementation (hook formula for
  skew shapes, or direct enumeration).~~
  **Closed 2026-05-30** — implemented in
  [`tools/pyhecke/python/pyhecke/skew_syt.py`](../../tools/pyhecke/python/pyhecke/skew_syt.py)
  via Aitken-Steinberg determinant formula. Provides:
  - `skew_syt_count(lambda_, mu)` — exact integer count.
  - `concatenate_partitions(partitions)` — builds μ = μ_1 ⊔ ... ⊔ μ_A.
  - `fits_inside(mu, lambda_)` — containment predicate.

  Validated against straight-shape hook-formula values
  (`f^{(4,3,2,1)} = 768`, `f^{(3,2,1)} = 16`) and Stanley EC2 §7.16
  skew examples (`f^{(3,2)/(1)} = 5`).

  Note: this primitive computes the **single-K** universal-branching
  case (`prop:universal-braid-branching` — one 3-strand braid
  embedded in H_k). For A-nucleon tensors, use LR coefficients (see
  Gap #2 + the [multinucleon gap audit](../../docs/audits/2026-05-30-universal-branching-multinucleon-gap.md)).

- ~~Inter-nucleon σ correction term needs derivation (not trivially
  a product of H_3 characters).~~
  **Closed 2026-05-30 (already implemented)** — the operator-valued
  Wenzl branching identity (Wenzl 1988) is implemented in
  [`canonical_tr_m_via_branching.py`](canonical_tr_m_via_branching.py)
  consuming the LR table from
  [`lr_coefficients.py`](lr_coefficients.py) and the cached
  interface operators `A^λ_{ξν}(I)` from
  [`A_operator_extract_at_level.py`](A_operator_extract_at_level.py).
  The plan doc lagged the implementation; see the
  [multinucleon gap audit](../../docs/audits/2026-05-30-universal-branching-multinucleon-gap.md)
  for the full derivation context and a correction to the
  "free baseline" formula above.

Both Gap #1 and Gap #2 are now closed at the infra level. Remaining
follow-up is **testing / witness emission** for the A-nucleon
combiner at A=4 (⁴He) once the H_12 trio extracts land — a smaller
scope than the original gap framing suggested.
