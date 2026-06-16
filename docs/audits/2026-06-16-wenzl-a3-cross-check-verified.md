# Wenzl A≥3 fusion block-decomposition — A=3 cross-check VERIFIED (2026-06-16)

**Branch:** `claude/wenzl-a3-cross-check-2026-06-16`
**Executes:** step 3 (the decisive correctness gate) of the Wenzl A≥3 workplan
[`docs/workplans/2026-06-16-wenzl-branching-a3-unlock.md`](../workplans/2026-06-16-wenzl-branching-a3-unlock.md),
building on the step-1 fusion derivation (PR #2358,
[`2026-06-16-wenzl-a3-fusion-operator-derivation.md`](2026-06-16-wenzl-a3-fusion-operator-derivation.md)).

## Result

The fusion block-decomposition reproduces the **true** 3-nucleon atomic `χ^λ`
(and hence `tr_M = Σ_λ y_λ χ^λ`) at machine precision — exactly the regime where
the old least-squares H₉ extracts failed by **21–42 %**
(`canonical_tr_m_via_branching.py:242`).

| atom | per-λ worst `|χ_true − χ_fusion|` | tr_M (fusion) vs tr_M (true direct) | vs canonical ref |
|---|---|---|---|
| **tritium** (Z=1,N=2) | **1.08e-12** | identical to 13 dp | 2.2e-8 (f64) |
| **³He** (Z=2,N=1) | **1.10e-12** | identical to 13 dp | 5.8e-8 (f64) |

(The ~1e-8 gap to the canonical reference is f64 round-off — both reference and
check run at double precision; the 50-dps witness is the follow-up. The decisive
number is `χ_fusion = χ_true` to 1e-12, which is the structural claim.)

## What was tested

The real 3-nucleon atomic braid splits (6,3) at the second inter-nucleon
interface: `β = β_inner · I · β_outer` with `β_inner ∈ H_6` (strands 1-6 =
nuc1·I₁₂·nuc2), `I` the σ₅ interface (σ_5⁻¹ for tritium, averaged for ³He),
`β_outer ∈ H_3'` (strands 7-9 = nuc3). The convention-free fusion identity

$$\chi^\lambda(\beta_{\text{inner}} I \beta_{\text{outer}})
  = \sum_{\xi\vdash 6,\ \nu\vdash 3}
    \mathrm{Tr}_{V_\lambda}\big[P_\xi P_\nu\,\rho_\lambda(I)\,P_\xi P_\nu\,
      \rho_\lambda(\beta_{\text{inner}}\beta_{\text{outer}})\big]$$

was checked against the true `χ^λ` for every `λ ⊢ 9`, then `y_λ`-weighted into
`tr_M`. This is the (6,3) analogue of the H₆ pre-flight (PR #2358 §4), now on the
**physical atomic interface and inner braid**, not abstract test words.

## Method note — JM isotypic projectors

The block isotypic projectors `P_ξ` (H₆, 11 irreps) and `P_ν` (H₃′, 3 irreps) are
built as Lagrange spectral projectors of the **multiplicative Jucys–Murphy sum**
`C = Σ_k L_k`, `L_{k+1} = σ L_k σ`, which is central in each block sub-algebra
with eigenvalue `Σ_cells q^{2·content}`. This separates **all** partitions at
generic `q` (verified: 11/11 distinct for ⊢6, 3/3 for ⊢3) — the content
*multiset* distinguishes even `(2,2,2)` vs `(3,1,1,1)`, where the integer
content-*sum* collides. No least-squares, no skew→straight basis alignment needed
for the verification.

## Significance

This closes the correctness question the workplan flagged as the decisive gate:
the rank-deficiency of the H₉+ least-squares extracts was a **fitting artefact**,
not a defect of the branching structure. The fusion block-decomposition is exact
at A=3. The remaining work is purely the **operator-form change of basis** (express
`A^λ_{ξν}(I)` as a `V_ξ⊗V_ν` matrix so the recursion works in the small tensor
space, never forming `V_λ`) — that is the *speedup*, now justified by a verified
correctness foundation, not a leap of faith.

## Discipline

f64 cross-check (the structural identity holds to 1e-12); 50-dps witness is the
follow-up. No production value changed (tr_M is already validated via the
transfer); this verifies a faster *route* to the same value. Not wired; no fit;
no 4th calibration. The compute is
[`computations/wenzl_a3_cross_check.py`](../../computations/wenzl_a3_cross_check.py).
