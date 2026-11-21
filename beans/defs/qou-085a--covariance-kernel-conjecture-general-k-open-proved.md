---
# qou-085a
title: 'covariance_kernel_conjecture: general k open; proved k<=8 in Lean'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T10:50:58Z
updated_at: 2026-11-21T12:20:00Z
parent: qou-m6dn
---


`QOU/BraidsAndKnots/YoungDiagramKernel.lean`:

    kernelValue k = Σ_{λ⊢k} (f^λ)³ · (Σ_□ c(□)² − C(k,2))
    covariance_kernel_conjecture (k : ℕ) : kernelValue k ≤ 0

## Status: genuinely open, and the only survivor of the qou-octr sweep

Eight sibling `sorry`s in that sweep were refutable. This one is not: the §9
small-instance check finds nothing. Evaluated in Lean —

    k :      0  1  2   3    4     5      6        7         8           9            10
    value:   0  0  0  -4  -16  -320  -10400  -163520  -3224704  -106339296  -4722309120

Zero at `k ≤ 2`, strictly negative from `k = 3`.

## Proved here

`covariance_kernel_le_zero_of_le_eight (k : ℕ) (hk : k ≤ 8) : kernelValue k ≤ 0`
— `interval_cases k <;> decide`, kernel evaluation, **no `native_decide`**.
`kernelValue` is fully computable, so every instance decides; the bound is 8
because the partition enumeration and `sytDim` cost grows quickly.

That upgrades part of the file's "verified `k ≤ 30` computationally" from an
external Python claim to a machine-checked one.

## Why the general case is hard

The dimension is **cubed**. `Σ_λ (f^λ)³ ω₃(λ)` is therefore *not* the Plancherel
expectation of `ω₃` (that would need `(f^λ)²/k!`), so the standard
`E_Planch[ω₃] = 0` identity does not apply. The file's own note routes it
through Biane–Śniady / Kerov-CLT character-ratio anti-correlation, which is
research-level.

## Next, cheaply

- Push the decidable range up (`k ≤ 10` or 12) if kernel reduction holds — pure
  compute-time, no new mathematics.
- Check whether `Σ_λ (f^λ)³ ω₃(λ)` has a hook-content closed form; the values
  grow fast and smoothly, which suggests one.

## 2026-11-21: status refresh and a negative probe (hecke-gs-conj sibling (session_01Qmmkt5sJX34MCerjRMERJN))
- "Push the decidable range up" is already done on main: `YoungDiagramKernel.lean` has `kernelValue_nonpos_of_le_twenty` (3 ≤ k ≤ 20, kernel `decide`, no native_decide). The k ≤ 8 lemma above is the old floor.
- The Jucys–Murphy identity Σ_□ c² = C(k,2) + |C₃|·χ^λ(3-cycle)/f^λ (in that file's docstring) gives kernelValue(k) = |C₃|·a(k) with a(k) = Σ_λ (f^λ)² χ^λ(3-cycle). Exact values a(3..11) = −2, −2, −16, −260, −2336, −28792, −632972, −19676288, −536156728.
- Pre-registered probe (hypothesis: a(k) is P-recursive with order ≤ 3 and coefficient degree ≤ 3; pass = a recurrence fitted on k ≤ ~25 predicts every held-out k ≤ 40 exactly; exact integer arithmetic): FAIL, no recurrence in that range (the nullspace is empty for all 12 (order, degree) pairs). Scope (a): this rules out only a low-order holonomic closed form, not a closed form of another shape, and says nothing about the sign. The "hook-content closed form" lead is not supported. Probe: `computations/probes/covariance_kernel_precursive_probe.py` on branch `claude/hecke-gs-conj-drain-2026-11-21`.
Conjecture unchanged, open.

Premise check vs `docs/coordination/owner-rulings.md` (main 2ae54ab40, 2026-11-21, owner request to drop old results): no superseded premise. kernelValue is pure S_k combinatorics (Plancherel, contents), independent of q, photon, trace convention or any fitted value.
