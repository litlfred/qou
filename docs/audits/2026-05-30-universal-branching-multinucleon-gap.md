# Universal-branching plan — A-nucleon free-baseline formula correction

**Authored:** 2026-05-30
**Branch:** `claude/track-b-skew-syt-count-2026-05-30` (PR [#1515](https://github.com/litlfred/qou/pull/1515))
**Trigger:** Scoping Gap #2 ("inter-nucleon σ correction") of
[`UNIVERSAL-BRANCHING-PLAN.md`](../../computations/UNIVERSAL-BRANCHING-PLAN.md)
revealed that the plan's "free baseline" formula is mathematically
incorrect AND that the inter-nucleon σ machinery is already
implemented in the canonical compute path.

## Headline

1. **Gap #2 is already implemented** in
   [`canonical_tr_m_via_branching.py`](../../computations/canonical_tr_m_via_branching.py)
   via the operator-valued Wenzl branching (Wenzl 1988), consuming
   [`lr_coefficients.py`](../../computations/substrate/lr_coefficients.py)
   (Littlewood-Richardson coefficients) and the cached interface
   operators `A^λ_{ξν}(I)` extracted by
   [`A_operator_extract_at_level.py`](../../computations/a_operator/A_operator_extract_at_level.py).
   The plan doc lagged behind the implementation.

2. **The plan's "free baseline" formula is wrong.** Replacing the
   multi-LR coefficient with `f^{λ/concat(μ_1, …, μ_A)}` (skew-SYT
   count of the sorted concatenation) does not in general equal the
   LR coefficient. Two counterexamples:

   | λ | (μ_1, μ_2) | concat | `f^{λ/concat}` | LR `c^λ_{μ_1,μ_2}` |
   |---|---|---|---:|---:|
   | (2,2) | (1,1), (1,1) | (1,1,1,1) | 0 (length 4 ≮ 2) | 1 |
   | (3,3) | (2,1), (2,1) | (2,2,1,1) | 0 (containment fails) | 1 |

   These follow from the Schur expansions `s_{(1,1)}² = s_{(2,2)} +
   s_{(2,1,1)} + s_{(1,1,1,1)}` and `s_{(2,1)}² = s_{(4,2)} +
   s_{(4,1,1)} + s_{(3,3)} + 2 s_{(3,2,1)} + s_{(3,1,1,1)} +
   s_{(2,2,2)} + s_{(2,2,1,1)}`. Verified numerically against
   `pyhecke.skew_syt.skew_syt_count` (PR [#1515](https://github.com/litlfred/qou/pull/1515)).

## The correct math

For A nucleons `K_i ∈ H_3(q)` embedded as the **disconnected
tensor** `K_1 ⊗ K_2 ⊗ … ⊗ K_A ∈ H_3^{⊗A} ⊂ H_{3A}` (where the
embedding omits the inter-nucleon generators σ_3, σ_6, …, σ_{3(A-1)}),
the branching of the H_{3A}-irrep `ρ_λ` is

    ρ_λ ↓ H_3^{⊗A} = ⊕_{(μ_1, …, μ_A), μ_i ⊢ 3} c^λ_{μ_1,…,μ_A} (ρ_{μ_1} ⊠ … ⊠ ρ_{μ_A})

where `c^λ_{μ_1,…,μ_A}` is the iterated Littlewood-Richardson
coefficient, equivalently `⟨s_{μ_1} · s_{μ_2} · … · s_{μ_A},
s_λ⟩` in the symmetric-function Hall inner product. Taking traces:

    χ^λ(K_1 ⊗ … ⊗ K_A) = Σ_{μ_1,…,μ_A ⊢ 3} c^λ_{μ_1,…,μ_A} · ∏_i χ^{μ_i}_{K_i}

To re-introduce the **inter-nucleon σ_{3k} generators** (the
"correction" of Gap #2), the operator-valued Wenzl identity adds a
non-trivial operator `A^λ_{μ_i, μ_{i+1}}(I_{i,i+1})` on the tensor
factor `V_{μ_i} ⊗ V_{μ_{i+1}}` for each interface, where
`I_{i,i+1} ∈ {pp, pn, nn}` is the interface type. This is precisely
sub-lemma 2.1 implemented in
[`canonical_tr_m_via_branching.py`](../../computations/canonical_tr_m_via_branching.py)
lines 1-25.

## Where my Gap #1 fits

The skew-SYT primitive
[`pyhecke.skew_syt.skew_syt_count`](../../tools/pyhecke/python/pyhecke/skew_syt.py)
from PR [#1515](https://github.com/litlfred/qou/pull/1515)
correctly closes the **single-K case** formalized in
[`universal-braid-branching.lean`](../../content/quantum-observable-universe/mass-theory/universal-braid-branching.lean):

    χ^λ(K) = f^{λ/[3]} χ_K^sym + f^{λ/[2,1]} χ_K^std + f^{λ/[1³]} χ_K^alt

for a single 3-strand braid `K ∈ H_3` embedded in `H_k` via the
standard inclusion of the first two generators. Here μ ranges over
the three partitions of 3, and `f^{λ/μ}` is exactly the skew-SYT
count. This module remains useful as the primitive for that
formalized case; **the plan doc's misleading "extension to A
nucleons" should not be implemented using this primitive**.

## Action items

1. **Update [`UNIVERSAL-BRANCHING-PLAN.md`](../../computations/UNIVERSAL-BRANCHING-PLAN.md)**
   to:
   - Mark Gap #2 closed (already implemented in
     `canonical_tr_m_via_branching.py` + `lr_coefficients.py`).
   - Correct the "Extension to A nucleons" section: use the
     iterated LR coefficient `c^λ_{μ_1,…,μ_A}`, not `f^{λ/concat}`.
   - Reference this finding doc.

2. **Keep `pyhecke.skew_syt`** as the canonical primitive for the
   single-K universal branching formula (`prop:universal-braid-branching`).

3. **No new compute needed** — Gap #2 is already wired. If
   `compute_chi_lambda_via_branching` lacks a witness emission or
   cross-check at A=4, that is a *separate* (smaller) testing task,
   not a derivation gap.

## References

- Wenzl (1988), "Hecke algebras of type A_n and subfactors", Invent. Math. 92.
- Stanley, *Enumerative Combinatorics Vol 2*, §7.10 (LR rule), §7.16 (skew SYT).
- Existing canonical infra:
  [`canonical_tr_m_via_branching.py`](../../computations/canonical_tr_m_via_branching.py),
  [`lr_coefficients.py`](../../computations/substrate/lr_coefficients.py),
  [`A_operator_extract_at_level.py`](../../computations/a_operator/A_operator_extract_at_level.py).
- Formalized single-K statement:
  [`universal-braid-branching.lean`](../../content/quantum-observable-universe/mass-theory/universal-braid-branching.lean).
