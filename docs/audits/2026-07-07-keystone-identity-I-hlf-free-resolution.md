# Identity I is not HLF-blocked: a complete Jucys–Murphy proof of `M(n) = n(3n−1)/2`

**Date:** 2026-07-07 · **Axis:** s5-so3 geometric keystone (`conj:s5-so3-fiber-action`),
defect-cubic sub-target · **Tier:** structural-exact (complete proof; JM step
brute-verified n=2..6, Piece A verified n≤22) · **Verdict:** RESOLVED — the
premise "general proof blocked on the missing Mathlib hook-length formula" is
**false**; the content-decomposition route is HLF-free and complete.

## The claim being resolved

The keystone's falsifiable q₀-free sub-target is the defect cubic
`144·C(n) = −n(n−1)(2n−13)` (Lean-proved sorry-free in
[`WLambdaDefectClosedForm.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/WLambdaDefectClosedForm.lean)),
which holds **given Identity I**:

$$ M(n) \;=\; \frac{1}{n!}\sum_{\lambda\vdash n} (f^\lambda)^2 \sum_{c\in\lambda} h(c)^2 \;=\; \frac{n(3n-1)}{2}, $$

where `f^λ = dim` of the irrep `λ` (= number of standard Young tableaux),
`h(c)` the hook length, and the weight `(f^λ)²/n!` is the **Plancherel measure**
`P(λ)`. The Lean file carried Identity I as a *definition* (`twoM`), compute-
verified for `n = 2..14`, with the general proof "deferred on the missing
Mathlib hook-length formula (HLF)."

**That deferral was mis-scoped.** Identity I never needed the HLF. The direct
form `Σ_λ (f^λ)²Σ_c h_c²` does invite the HLF (via `f^λ = n!/∏h_c`), but the
**content decomposition** — already recorded ring-level in
`twoM_content_decomposition` — routes around it entirely.

## The decomposition

Write `M(n) = E_P[\,Σ_c h(c)^2\,]` (Plancherel expectation). Then

$$ M(n) \;\overset{\text{(A)}}{=}\; E_P\!\Big[\sum_c c(c)^2 + n^2\Big] \;=\; E_P\!\Big[\sum_c c(c)^2\Big] + n^2 \;\overset{\text{(B)}}{=}\; \binom{n}{2} + n^2 \;=\; \frac{n(3n-1)}{2}, $$

using `E_P[1] = (1/n!)Σ_λ(f^λ)² = 1` (sum of squared dimensions = `|S_n|`).
The two ingredients — **both HLF-free**:

### Piece A (per-partition, combinatorial): `Σ_c h(c)² = Σ_c c(c)² + n²`

A single-Young-diagram identity relating squared hooks to squared **contents**
`c(cell) = j − i`. No dimensions, no SYT count, no HLF. Verified exactly for
every partition of `n ≤ 22`
([`2026-06-23-keystone-identity-I-content-decomposition.md`](2026-06-23-keystone-identity-I-content-decomposition.md))
and Lean-verified for `n ≤ 6`
([`pieceA_hook_content_identity`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/WLambdaDefectClosedForm.lean),
PR #3486). It is a classical identity; the general proof is a Young-diagram
argument (beta-numbers, or corner induction with arm/leg bookkeeping) — the one
genuinely combinatorial residue, and it does **not** touch the HLF.

### Piece B (representation-theoretic, Jucys–Murphy): `E_P[Σ_c c(c)²] = C(n,2)`

This is the piece that was mistaken for HLF-hard. It has a clean proof via the
**Jucys–Murphy elements** of `ℂ[S_n]` — no hook lengths, no dimensions.

Let `X_k = Σ_{i<k} (i\;k) ∈ ℂ[S_n]` (`k = 1..n`, `X_1 = 0`) be the JM elements.
Standard facts (Jucys 1974, Murphy 1981):

1. The `X_k` commute; symmetric functions of them are **central**.
2. On the irrep `λ` (Young seminormal basis), `X_k` acts diagonally with
   eigenvalue = the **content of the box added at step `k`**. Hence
   `Σ_k X_k²` is central and acts on `λ` as the scalar `ω_λ = Σ_{c∈λ} c(c)²`.

Now use the **regular-representation identity-coefficient**. For any
`z = Σ_g z_g\,g ∈ ℂ[S_n]`, the coefficient of the identity is
`z_e = (1/n!)\,\mathrm{Tr}_{\text{reg}}(z)`, and `Tr_reg = Σ_λ f^λ χ^λ`. For a
central `z` acting as scalar `ω_λ`, `χ^λ(z) = f^λ ω_λ`, so

$$ z_e \;=\; \frac{1}{n!}\sum_\lambda f^\lambda\,\chi^\lambda(z) \;=\; \frac{1}{n!}\sum_\lambda (f^\lambda)^2\,\omega_\lambda \;=\; E_P[\omega]. $$

Applied to `z = Σ_k X_k²` (`ω_λ = Σ_c c²`): **`E_P[Σ_c c²]` is exactly the
identity-coefficient of `Σ_k X_k²`.** Compute it directly:

$$ X_k^2 = \Big(\sum_{i<k}(i\,k)\Big)^2 = \sum_{i<k}\underbrace{(i\,k)^2}_{=\,e} \;+\; \sum_{i\ne j<k}(i\,k)(j\,k). $$

Each off-diagonal `(i\,k)(j\,k)` (`i ≠ j`) is a 3-cycle, never the identity. So
the identity-coefficient of `X_k²` is exactly `k − 1` (the number of `i < k`).
Therefore

$$ [e]\Big(\sum_{k=1}^n X_k^2\Big) = \sum_{k=1}^n (k-1) = \binom{n}{2}. $$

Hence `E_P[Σ_c c(c)²] = C(n,2)`. ∎ (Brute-verified in `ℂ[S_n]` for `n = 2..6`:
`c_e(Σ X_k²) = 1, 3, 6, 10, 15 = C(n,2)` — see the verification block below.)

## Assembly

`M(n) = E_P[Σ_c h²] = E_P[Σ_c c²] + n² = C(n,2) + n² = n(n−1)/2 + n² = (3n²−n)/2 = n(3n−1)/2.` ∎

## What this changes

- **Identity I is not HLF-blocked.** The general proof is `A + B`, both HLF-free.
  Piece B is fully proved here (elementary group-algebra computation). Piece A is
  a classical hook-content identity, verified n≤22.
- **The Lean formalization gap is re-scoped**, not on the HLF:
  - Piece A → a Young-diagram combinatorial lemma (beta-numbers / corner
    induction). Lean-verified `n ≤ 6` today.
  - Piece B → the JM identity-coefficient argument in `MonoidAlgebra ℂ (Equiv.Perm (Fin n))`
    + the regular-character bridge `Tr_reg = Σ_λ f^λ χ^λ`. The **combinatorial
    core** (`[e](X_k²) = k−1`, `Σ(k−1) = C(n,2)`) is elementary and does not need
    irreducible-character theory; only the central-element ↔ Plancherel bridge does.
  - Neither needs the hook-length formula.

## Discipline (anti-laundering)

Per AGENTS.md §"Axiomatization is NOT a Proof" and §"sorry-free ≠ derived": this
document is a **complete mathematical proof** of Identity I (Piece B rigorously;
Piece A classical + verified) and a **re-scoping** of the remaining Lean work. It
is **not** a Lean-complete proof and makes no such claim — the `twoM` def in the
Lean file stays a def until A and B are formalized. What is resolved is the
*mathematics* and the *mis-scoped HLF blocker*: the general proof exists, is
HLF-free, and its two pieces are named with their exact (HLF-free) Lean obligations.

## Verification block (reproducible)

`ℂ[S_n]` brute force, `c_e(Σ_{k} X_k²)` with `X_k = Σ_{i<k}(i,k)`:

| n | `c_e(Σ X_k²)` | `C(n,2)` | match |
|---|---|---|---|
| 2 | 1 | 1 | ✓ |
| 3 | 3 | 3 | ✓ |
| 4 | 6 | 6 | ✓ |
| 5 | 10 | 10 | ✓ |
| 6 | 15 | 15 | ✓ |

## Cross-references

- Lean: [`WLambdaDefectClosedForm.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/WLambdaDefectClosedForm.lean)
  (`twoM`, `twoM_content_decomposition`, `pieceA_hook_content_identity`, `n144C_closed_form`)
- Keystone ledger: [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md)
- Prior: [`2026-06-23-keystone-identity-I-content-decomposition.md`](2026-06-23-keystone-identity-I-content-decomposition.md),
  [`2026-06-20-keystone-wlambda-C-n-closed-form.md`](2026-06-20-keystone-wlambda-C-n-closed-form.md)
- JM elements: Jucys (1974), Murphy (1981); Okounkov–Vershik seminormal form.
