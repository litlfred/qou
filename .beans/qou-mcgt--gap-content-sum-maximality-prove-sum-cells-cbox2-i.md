---
# qou-mcgt
title: 'GAP: content-sum maximality — prove Sum_cells c(box)^2 is maximised over non-extremal partitions of k at (k-1,1) (closes step D of the w_std tower growth bound)'
status: todo
type: task
created_at: 2026-08-11T11:11:58Z
updated_at: 2026-08-11T11:11:58Z
---


## The statement

For `λ ⊢ k` with `λ ∉ {(k), (1ᵏ)}` (i.e. at least 2 rows AND at least 2 columns):

    C₂(λ) := Σ_□ c(□)²  ≤  C₂((k−1,1)) = Σ_{j=0}^{k−2} j² + 1,

with equality exactly on the conjugate pair `{(k−1,1), (2,1^{k−2})}`.

Equivalently, in the form the downstream needs:

    ρ := max_{λ non-extremal} r(λ) = 1 − 3/(k−1),
    r(λ) = χ^λ(3-cycle)/f^λ = 3(C₂(λ) − C(k,2)) / (k(k−1)(k−2)).

## Why it matters — it is the last input to step (D)

Chain (see `qou-x66y`, PR #4973):

| step | status |
|---|---|
| (A) branching identity | corpus, exact |
| (B) Plancherel identity, `T₂ = 0` | corpus, exact |
| (C) cube-moment bound | Lean sorry-free (`sum_sq_pow_three_le`) |
| (D) transfer | **blocked on THIS**; all downstream algebra Lean sorry-free |
| RSK/Burnside `Σ(f^λ)² = k!` | open, separate |

The extremal split (`T3_lt_of_extremal_split`, `T3_le_explicit_c`) takes `ρ < 1`
as a hypothesis and delivers `T₃ ≤ c·T₁` with `c < 1`; that chains through
`ratio_bound_of_T3_le` (`ε = 2(1−c)/(1+2c) ≍ 4/(3(k−1))`) into
`cube_moment_le_of_ratio_bound`. **Only `ρ < 1` is missing**, and only
polynomially — a uniform constant is NOT needed, since `T₁` is
super-exponential.

## Verified, not proved

`computations/probes/wstd_extremal_split_probe.py` (k ≤ 13) and an extended check
to **k = 24**: the off-extremal maximiser is exactly `{(k−1,1), (2,1^{k−2})}` at
every k, and the gap `C₂((k)) − C₂((k−1,1)) = (k−1)² − 1` exactly (checked
k = 5,10,15,20,24).

## Proof strategy

1. **`C₂` is conjugation-invariant** (contents negate under `λ ↦ λ'`), so
   maximisers come in conjugate pairs — this *explains* the observed tie and
   halves the work: WLOG `λ₁ ≥ ℓ(λ)`.
2. **Exchange argument.** If `λ` is non-extremal with `λ₁ < k−1`, moving the last
   cell of the last row to the end of row 0 keeps it non-extremal and strictly
   increases `C₂` (the cell moves from content `λ_ℓ−1−(ℓ−1)` to content `λ₁`,
   and under the WLOG the latter has strictly larger square). Iterating drives
   any non-extremal `λ` to `(k−1,1)`.
3. The `(k−1)²−1` gap then follows by direct computation:
   `Σ_{j=0}^{k−1}j² − (Σ_{j=0}^{k−2}j² + 1) = (k−1)² − 1`.

Step 2 needs care where the WLOG is tight (tall-thin shapes), which is exactly
where the conjugate branch takes over. Elementary, but a real induction — needs
Mathlib partition API.

## Weaker sufficient version (if the sharp one is hard)

Any `ρ ≤ 1 − δ(k)` with `δ` decaying polynomially suffices. So a crude bound
`C₂(λ) ≤ C₂((k)) − c·k²` for non-extremal `λ`, any explicit `c > 0`, closes (D)
just as well. Do NOT spend effort on sharpness that the downstream discards.

## Coordination

Bean `A1 (deep bet): exact/semi-exact evaluation of T3 = Σ(f)²χ(3-cyc) via
content-sum formulas` works the **same `T₃` object** by a different route
(exact evaluation vs. this extremal bound). Not a duplicate — that one seeks a
closed form, this one only needs an inequality — but coordinate before either is
wired.
