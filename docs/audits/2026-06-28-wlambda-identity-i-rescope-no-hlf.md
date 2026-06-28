# W_λ keystone — Identity I needs no hook-length formula (gap re-scoped) + W_λ normalization

**Date:** 2026-06-28
**Bean / keystone:** `s5bb` — geometric `W_λ` ([`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md))
**Compute:** [`computations/substrate/wlambda_identity_i_structure_probe.py`](../../computations/substrate/wlambda_identity_i_structure_probe.py)
**Witness:** [`computations/substrate/wlambda-identity-i-structure-probe.witness.json`](../../computations/substrate/wlambda-identity-i-structure-probe.witness.json)

## Context

The `W_λ` keystone has a `q₀`-free, falsifiable sub-target: any index realizing `W_λ` must
reproduce the heat-kernel defect `144·C(n) = −n(n−1)(2n−13)`
([`WLambdaDefectClosedForm.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/WLambdaDefectClosedForm.lean),
sorry-free). Its **one** carried representation-theoretic input is **Identity I**

```
  M(n) = (1/n!) · Σ_{λ⊢n} (f^λ)² · ( Σ_{c∈λ} h_c² )  =  n(3n−1)/2 ,
```

held in the keystone Lean as a compute-verified `def twoM` (n=2..14). The s5-so3 ledger states:
*"Proving Identity I from the partition squared-hook sum needs SYT-dimension / hook-length
infrastructure not currently in Mathlib — a multi-session infra fill."*

## Finding 1 — Identity I needs no hook-length **formula**; the gap is narrower

Writing `E[g] := (1/n!) Σ_λ (f^λ)² g(λ)` (the Plancherel expectation), Identity I is
`E[Σ_c h_c²] = n(3n−1)/2`. The probe verifies, exactly for n=2..14:

| identity | status | infra needed |
|---|---|---|
| `E[Σ_c content(c)²] = C(n,2)` | ✓ | Jucys–Murphy `Σ Xᵢ²` second moment (RSK + center of `ℂ[Sₙ]`); **no HLF** |
| `E[Σ_c h_c²] − E[Σ_c content(c)²] = n²` | ✓ | elementary arm/leg/content (Plancherel mean of a hook–content combination) |
| `Σ_c h_c = n + Σ_i C(λ_i,2) + Σ_j C(λ'_j,2)` | ✓ (single-diagram, elementary) | none |
| arithmetic `C(n,2) + n² = n(3n−1)/2` | ✓ | `ring`/`omega` |

So Identity I **factors** as

```
  E[Σ h_c²]  =  E[Σ content²]  +  n²  =  C(n,2)  +  n²  =  n(3n−1)/2.
```

The **full hook-length formula** `f^λ = n!/∏ h_c` is *not* required to prove Identity I. The
ledger's "needs HLF" is over-stated: the genuine inputs are (1) RSK `Σ_λ (f^λ)² = n!` (Plancherel
normalization), (2) the content second moment `E[Σ content²] = C(n,2)` (Jucys–Murphy / Kerov), and
(3) the residual `E[Σ h² − Σ content²] = n²` (elementary hook–content combinatorics). This re-scopes
the keystone's Identity-I dependency from research-grade HLF to **content-moment + elementary-hook**
infrastructure.

> **Honest scope (a).** The content second moment `E[Σ content²] = C(n,2)` is itself a real theorem
> (the JM second-moment / Kerov polynomial degree-2 case); "no HLF" does not mean "trivial." But it
> is a **different, smaller** gap than the hook-length formula, and the *reduction* of Identity I to
> it is the new, parameter-free result here.

## Finding 2 — W_λ normalization: `Σ_λ d_q(λ)² ≠ [n]_q!` (the `D²` vs `[n]_q!` question)

With the symmetric quantum dimension `d_q(λ) = [n]_q!/∏[h_c]_q`, the probe finds
`Σ_λ d_q(λ)² ≠ [n]_q!` (n=1..6). So `W_λ = d_q²/[n]_q!` does **not** sum to 1 — exactly the open
normalization question the ledger records (*"#2524 proposes `d_q²/D²` (Σ=1) vs `d_q²/[n]_q!`
(Σ≈0.982)"*). The classical `Σ_λ (f^λ)² = n!` is the `q→1` limit, but the q-deformation is the
total-quantum-dimension `D² = Σ_λ d_q²` normalization, not `[n]_q!`. The witness records the per-λ
`W_λ` cyclotomic denominators (the Habiro habitat) for the colored-Σ(2,3,5)-WRT bridge.

## Consequence for the next step

The Identity-I Lean closure splits into:
1. **`ring`/`omega` arithmetic reduction** `C(n,2) + n² = n(3n−1)/2` — trivial, lands now.
2. **Conditional Identity I (§3b-cond)** on the two named inputs (content second moment; `n²`
   residual) — makes the remaining gap explicit and *narrow*.
3. The content second moment — check Mathlib's RSK / symmetric-group character API; if present, the
   gap may close without the multi-session HLF build the ledger anticipated.
