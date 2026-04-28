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

For A nucleons K_i ∈ H_3(q) (disconnected tensor, free baseline):

    χ_free(λ) = Σ_{(μ_1,...,μ_A), μ_i⊢3} f^{λ/(μ_1⊔...⊔μ_A)}
                · Π_i χ^{μ_i}(K_i)

This factorizes the atom character through per-nucleon H_3 channel
characters weighted by skew-SYT counts. **Only 3^A terms** per λ
(not matrix exponentiation).

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

- Skew-SYT count `f^{λ/μ}` for general λ ⊢ 3A, μ = μ_1 ⊔ ... ⊔ μ_A
  needs a generating-function implementation (hook formula for
  skew shapes, or direct enumeration).
- Inter-nucleon σ correction term needs derivation (not trivially
  a product of H_3 characters).

Both are well-defined categorical quantities (per
`prop:universal-braid-branching`); implementing them is a
substantial refactor beyond this session's scope but well-posed.
