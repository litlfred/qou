# Proof: the metallic-ratio hierarchy of the Hecke scalar

**Date:** 2026-06-08
**Branch:** `claude/gallant-bohr-w9f6a6` (PR #1999)
**Owner ask:** "lets try and prove my assertions" (the q-hierarchy /
metallic-ratio / involution claims).
**Lean formalization:** [`QOU/AlgebraicSubstrate/MetallicHierarchy.lean`](../../content/quantum-observable-universe/lean/QOU/AlgebraicSubstrate/MetallicHierarchy.lean)
**Verification status:** hand-proof complete and rigorous (below); Lean
file committed; **local machine-check blocked** by a sandbox Lean-env
issue (lake-cache restore was clobbered by `lake`'s package
re-resolution — Mathlib oleans removed; from-source rebuild out of
budget). To be machine-verified by CI / a clean-env session.

## What is being proved

The Iwahori–Hecke generator satisfies `σ² = (q − q⁻¹)σ + 1`, so the
**structural scalar of the braiding is `q − q⁻¹`**. The owner's assertion:
the special `q` values form a hierarchy at the **metallic ratios**, tied
to the bar involution and (for golden) the roots of unity.

Define the `n`-th metallic ratio `δ_n := (n + √(n²+4))/2` (golden `δ_1=φ`,
silver `δ_2=1+√2`, bronze `δ_3`).

### Theorem 1 (metallic characterization)
For real `q > 0` and integer `n ≥ 0`:
`q − q⁻¹ = n  ⟺  q = δ_n`.

### Theorem 2 (bar-involution pairing)
`δ_n⁻¹ = δ_n − n`. Equivalently the involution `q ↦ q⁻¹` sends `δ_n` to
its sub-unit mirror `1/δ_n`, and the two roots of `x² − nx − 1` are `δ_n`
and `−1/δ_n` (the second is the eigenvalue-conjugate via `q ↦ −q⁻¹`).

### Corollary (golden is the first rung)
`δ_1 = φ = (1+√5)/2`. Since `q₀ − q₀⁻¹ = 0.2091 < 1`, the substrate sits
below golden: golden is the **first** metallic resonance above `q₀`.

## Proof of Theorem 1

Write `s := √(n²+4) > 0`, so `s² = n² + 4` and `s ≥ n` (because
`s² = n²+4 ≥ n²` with both sides `≥ 0`).

**(⇒)** Assume `q − q⁻¹ = n`. Multiply by `q > 0`:
`q² − 1 = nq`, i.e. **`q² − nq − 1 = 0`**.
Then
`(2q − n)² = 4q² − 4nq + n² = 4(q² − nq) + n² = 4·1 + n² = n² + 4 = s²`,
using `q² − nq = 1`. Hence `(2q − n − s)(2q − n + s) = 0`. The second
factor is positive: `2q − n + s = 2q + (s − n) > 0` since `q > 0` and
`s ≥ n`. Therefore `2q − n − s = 0`, i.e. `q = (n + s)/2 = δ_n`. ∎

**(⇐)** Assume `q = δ_n = (n+s)/2`. Then
`q² = (n+s)²/4 = (n² + 2ns + s²)/4 = (n² + 2ns + n² + 4)/4 = (n² + ns + 2)/2`,
while `nq + 1 = n(n+s)/2 + 1 = (n² + ns + 2)/2`. So **`q² = nq + 1`**, and
`q − q⁻¹ = (q² − 1)/q = (nq + 1 − 1)/q = nq/q = n`. ∎

## Proof of Theorem 2

`δ_n` is a root of `x² − nx − 1 = 0` (shown above: `δ_n² = nδ_n + 1`).
Divide by `δ_n > 0`: `δ_n − n = 1 + δ_n⁻¹ − ... ` — directly,
`δ_n⁻¹ = (δ_n² − nδ_n)/δ_n · (1/δ_n)`… cleanly: from `δ_n² = nδ_n + 1`,
`δ_n⁻¹ = δ_n − n` ⟺ `1 = δ_n(δ_n − n) = δ_n² − nδ_n = 1`. ✓ ∎

The other root of `x² − nx − 1` is `−1/δ_n` (product of roots `= −1`, sum
`= n`), which is the image of `δ_n` under the eigenvalue involution
`q ↦ −q⁻¹`.

## Roots-of-unity remark (golden is the unique join — not re-proved here)

On `|q| = 1`, `q + q⁻¹ = 2cos θ`. The standard identity
`φ = 2cos(π/5)` makes `φ = [2]_q` at the 10th root of unity `q = e^{iπ/5}`
(the Fibonacci-anyon quantum dimension). So golden lies on **both** the
real-metallic ladder (`q−q⁻¹ = 1`) and the root-of-unity ladder
(`q+q⁻¹ = φ`). Silver (`δ_2 > 2`) is **not** a `2cos(π/k)` value, so the
root-of-unity tie is special to golden. (`φ = 2cos(π/5)` is in Mathlib as
`Real.cos_pi_div_five`-type lemmas; left for the wired-block version.)

## What is now established vs. still conjectural

| claim | status |
|-------|--------|
| metallic ratios = real `q>1` with `q−q⁻¹ ∈ ℤ⁺` | **proved** (Thm 1) |
| bar-involution pairing `δ_n⁻¹ = δ_n − n` | **proved** (Thm 2) |
| golden = first rung above `q₀` | **proved** (Cor) |
| golden = `2cos(π/5)` = Fibonacci dimension | standard (Mathlib) |
| a *physical* structural transition occurs at `q = φ` | **conjectural** — needs the confinement-filtration `J^ℓ(q)` to reorganize as `q−q⁻¹` crosses 1 (q-regime follow-up) |
| phase symmetry = `Aut(link)`; electron-shell crystal splitting | **conjectural** (see `2026-06-08-phase-symmetry-from-knot-operators-model.md`) |

So the **algebraic backbone of the q-hierarchy is proved**; the physical
transition claims remain conjectures to be tested at the (deferred)
upper-q follow-up. This is the formalize-first payoff: the structural
ladder is pinned before any q-sweep scan.
