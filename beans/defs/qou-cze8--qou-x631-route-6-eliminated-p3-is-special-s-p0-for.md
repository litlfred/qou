---
# qou-cze8
title: 'qou-x631 route 6 eliminated: p=3 is special, S_p<=0 for odd p is FALSE (p=5 flips sign)'
status: completed
type: task
priority: normal
created_at: 2026-09-06T13:01:44Z
updated_at: 2026-09-26T11:03:19Z
---


Research on `qou-x631`: `cov(k) = Σ_λ (f^λ)³(Σ_□c(□)² − C(k,2)) ≤ 0`, equivalently
`T₃(k) = Σ_λ (f^λ)² χ^λ(3-cyc) ≤ 0`. Phases 0–2 eliminated five routes. This is a
sixth, plus two exact facts that sharpen what is left.

**The conjecture is not advanced.** Eliminating a route narrows the search; it
does not move toward the proof.

## Route 6, eliminated: the sign is not a property of odd cycles

Write `S_p(k) = Σ_λ (f^λ)² χ^λ(p-cycle, 1^{k−p})`, so `T₃ = S₃`. The natural
generalisation — *"S_p(k) ≤ 0 for every odd p"* — would subsume the conjecture,
and it is **false**:

| p | behaviour, 3 ≤ k ≤ 14 |
|---|---|
| 3 | negative throughout |
| **5** | **+172 (k=7), −840 (k=8), +17644 (k=9), −64702464 (k=12)** — three sign changes |
| **7** | negative through k=11, then **+58661128 at k=12** |
| 9 | positive throughout the range |

So **any proof of `T₃ ≤ 0` must use something specific to p = 3.** An argument
that would also cover p = 5 or p = 7 is provably wrong. That rules out generic
character-positivity on odd classes, monotone couplings blind to p, and anything
phrased for "a fixed cycle type" rather than for the 3-cycle.

**Where the structure says to look.** In Biane's expansion `Σ_p = R_{p+1} +
(lower cumulants)`, p = 3 is the **only** case whose correction is a single
*deterministic* term:

    Σ₃ = R₄ + R₂,   R₂(λ) = k, constant on partitions of k.

So `Σ₃ − E[Σ₃] = R₄ − E[R₄]` exactly, and the conjecture is the clean
single-cumulant statement `Cov_Planch(f^λ, R₄) ≤ 0`. For p = 5 the expansion
mixes `R₆`, `R₄` and `R₂²`, and the sign flips show a mixture inherits nothing
from its parts. This is consistent with the epic's own framing (`Σ̂₃ = R₄ + R₂`,
`E_Planch[R₄] = −k`) and explains *why* that framing was the right one.

## Exact fact A — `S_μ = 0` for every odd μ (one-line proof)

Conjugation `λ ↦ λ'` has `f^{λ'} = f^λ` and `χ^{λ'}(μ) = sgn(μ)·χ^λ(μ)`. For odd
μ the involution pairs terms with opposite sign, and a self-conjugate λ gives
`χ^λ(μ) = −χ^λ(μ) = 0`. The whole family lives on even classes. Verified for
every μ at k ≤ 9.

## Exact fact B — the Plancherel centring is exactly `C(k,2)`

    Σ_λ (f^λ)² (Σ_□ c(□)² − C(k,2)) = 0   for every k.

From Jucys–Murphy, `Σᵢ JMᵢ² = C(k,2)·e + C₃`, so on `S^λ`,
`Σc² − C(k,2) = ω_λ(C₃) = |C₃|·χ^λ(3cyc)/f^λ`; multiplying by `(f^λ)²` and
summing gives `|C₃| Σ_λ f^λ χ^λ(3cyc) = 0`, the regular character off the
identity. So `E_Planch[Σc²] = C(k,2)` **exactly** — the conjecture is purely
about the **bias**, and nothing about the centring is in doubt. Verified k ≤ 15.

This also gives `cov(k) = |C₃|·T₃(k)` with `|C₃| = k(k−1)(k−2)/3 > 0`, i.e. the
epic's stated equivalence, with its mechanism rather than as an assertion.

## Why the numbers can be trusted

Two implementations sharing **no code** agree exactly on the p = 3 column: the
Murnaghan–Nakayama character sum here, and the content/hook-length computation in
`qbeta_covariance_kernel_extend_probe.py`. At k = 12 both give −15073599368. The
probe asserts that agreement as its first check, so a regression in either
invalidates the run rather than passing quietly. Exact integers throughout; the
float64 guard reports no float entry points in either file.

## Also available for route `qou-0ml9`

By RSK, `(f^λ)² = #{w : sh(w) = λ}`, so `T₃(k) = Σ_{w ∈ S_k} χ^{sh(w)}(3-cyc)` —
that route's exact starting point. `QOU.Mathlib.Schensted.rskEquiv` now supplies
`sh(w)` in Lean, axiom-clean (bean `qou-t181`).
