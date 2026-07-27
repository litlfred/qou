# Milnor-parity sign law for A-component Brunnian binding clusters

**Date:** 2026-07-27
**PR:** #4389 (`claude/deltalambda-milnor-parity-sign-law-2026-07-27`)
**Consolidates:** #4360 (A=3 Borromean, proved `+`) + #4378 (A=4 Helium, measured `−`)
**Scope:** Δ_λ / binding-cluster sign structure (Option E, sign leg)
**Free parameters introduced:** 0

## What this is

A single Lean file,
[`QOU/MassTheory/MilnorParitySignLaw.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/MilnorParitySignLaw.lean),
that formalizes the observed pattern across the two known Brunnian binding-cluster
orders as an **A-indexed law**, while keeping the differing epistemic status of the
two data points visible in the Lean types.

The length-`A` iterated commutator (Borromean `w₃` at A=3; `w₄ = [[A₀₁,A₁₂],A₂₃]`
at A=4) is a genuine `A`-component Brunnian link. Its trace deficit
`1 − τ_A` against the `A`-component unlink is the irreducible `A`-body cluster
`c_A = E₀·(1 − τ_A)`. The two observed features:

1. **Leading Milnor order = `2(A−1)`** in `h = q − q⁻¹`.
2. **Deficit sign = `(−1)^(A−1)`**: A=3 → `+`, A=4 → `−`.

## Epistemic split (the point of the exercise)

| A | source | order law | sign | how established |
|---|--------|-----------|------|-----------------|
| 3 (Borromean, #4360) | `BorromeanThreeBodyCluster.lean` | `O(h⁴)=2(3−1)` | `+` | **PROVED** — closed form `1−τ_Borr = h⁴(3+h²)/(h²+4) ≥ 0` |
| 4 (Helium, #4378) | `HeliumBrunnianDeficitMeasured.lean` | `O(h⁶)=2(4−1)`, n≈6.06 | `−` | **MEASURED** — τ_L₄≈1.000146>1, cited witness (no closed form) |

Because the A=4 sign is *measured*, a flat `theorem : sign = (−1)^(A−1)` would
restate a measured input as a proved premise — the "conditional-proved ≠
premise-established" / "sorry-free ≠ derived" trap. The file avoids this.

## What is PROVED vs CONDITIONAL vs OPEN (per Lean declaration)

**Proved, sorry-free:**
- `borromean_deficit_order` — A=3 deficit factors as `h^(leadingOrder 3)·r(h)` with
  `r(0)=3/4≠0`; the leading Milnor order of the A=3 deficit is exactly `4 = 2(3−1)`.
- `tauBorromean_lt_one` — A=3 sign `+` (deficit `> 0` for `h≠0`), from the closed form.
- `paritySign_of_odd` / `paritySign_of_even` — the convention `(−1)^(A−1)`
  (odd A → `+1`, even A → `−1`).
- `sign_law_of_crossing` — **the star conditional theorem**: given `E₀>0`, `A≥1`,
  and the explicit `CrossingPattern` hypothesis (`τ_A<1` for odd A, `τ_A>1` for
  even A), the cluster sign equals `paritySign A = (−1)^(A−1)`.
- `sign_law_A3` — A=3 instance; crossing hypothesis discharged by the **proved**
  `τ_Borr < 1`. Sign `+`, fully proved.
- `sign_law_A4_measured` — A=4 instance; crossing hypothesis discharged by the
  **measured** `τ_L₄ > 1` (cited). Sign `−`. The measurement is the input, and the
  declaration name says `_measured`.
- `sign_law_general` — §3b-cond conditional: modulo the open conjecture class, the
  sign law holds at every `A ≥ 2`.

**Measured inputs (recorded as `def`s, NOT theorems):**
- `tauL4Measured := 1.000145898` (τ_L₄, #4378 witness).
- `tauL4MeasuredOrder := 6.06` (measured leading order; no theorem asserts `=6`).

**Open (conjecture, no instance):**
- `MilnorParitySignConjecture (τ : ℕ → ℝ → ℝ)` — content-bearing primary conjecture
  class asserting the crossing pattern at **all** `A ≥ 2`. It carries **no
  instance**: the honest open state. Confirmed at A=3 (proved) and A=4 (measured)
  only; no general topological derivation of the order or the crossing sign exists
  in the corpus. Fabricating an instance would launder the two-point pattern into a
  universal claim (forbidden).

## Sign-law convention (settled from the two data points)

`sign(1 − τ_A) = (−1)^(A−1)`:
- A=3 → `(−1)² = +1` → deficit `+` ✓ (proved)
- A=4 → `(−1)³ = −1` → deficit `−` ✓ (measured)

(Equivalently `(−1)^(A+1)`; the file uses `(−1)^(A−1)` with ℕ-subtraction,
well-defined for `A ≥ 1`.)

## Anti-fit / anti-laundering compliance

- No fitted constant. The only numeric literals are the two `def`s recording the
  #4378 measurement, each named `Measured` and carrying a `-- Ref:` to the witness.
- `μ₃`, `μ₄` (the residual moments) enter neither any statement nor any proof; the
  file makes **sign** claims only, never a magnitude/Δ_λ closure.
- The general law is a conjecture with no instance — not wired to any dashboard or
  production script.
- The order law is proved only for A=3 (from the closed form); the general order
  claim is part of the open conjecture, not asserted as a theorem.

## Verification

`lean`-direct (self-contained, `import Mathlib.Tactic` only), toolchain
`leanprover/lean4:v4.24.0`. Sorry-free, axiom-clean (no `sorry`, no added `axiom`).

## Relation to the sources

This file does **not** modify #4360 or #4378. It restates their trace closed
form (A=3) and measured value (A=4) locally and cites them, then adds the A-indexed
consolidation layer (order index, parity sign, conditional law, general conjecture).
