# Cross-atom binding overshoot: it GROWS with A (the deuteron's ~2× is not universal)

**Date:** 2026-06-23
**Branch:** `claude/binding-cross-atom-overshoot-2026-06-23`
**Status:** Positive/structural — extends the deuteron flat-baseline/overshoot analysis to ³He and ⁴He.
Atom-dependent result that constrains P_λ. No fit; no P_λ proposed.
**Bean:** [`cbnf`](../../.beans/cbnf--categorical-binding-wiring-no-fitting.md)
**Follows:** [`2026-06-22-gap-a3-deuteron-A-D-overshoot.md`](2026-06-22-gap-a3-deuteron-A-D-overshoot.md) (#2631), [`2026-06-22-gap-a3-deuteron-plambda-flat-baseline-bareven.md`](2026-06-22-gap-a3-deuteron-plambda-flat-baseline-bareven.md) (#2626)
**Script:** [`computations/gap_a3_cross_atom_overshoot_probe.py`](../../computations/gap_a3_cross_atom_overshoot_probe.py)

## The question

#2626/#2631 found, for the deuteron: the flat trace `y_λ χ^λ(β_D)` is **bar-mixed**, and the
flat baseline `A(D)·tr_M` **overshoots** `−B(D)/m_e` by **~2.05×**. The non-fit next step: does the
**same pattern** hold across atoms? Atom-*independence* of the overshoot would be a structural clue;
*variation* constrains P_λ's atom-dependence. This runs D, ³He, ⁴He canonically (`y_lambda_at` q₀ hot
path + `chi_all_lambda`).

## Result — the overshoot grows with A; bar-mix shrinks with A

| atom | n=3A | A | `A(K)` derived | `tr_M(β_K)` | `A·tr_M` | `−B/m_e` | **overshoot** | **bar-mix** |
|------|------|---|----------------|-------------|----------|----------|---------------|-------------|
| D | 6 | 2 | 22.975 | 0.38836 | 8.923 | 4.353 | **2.050** | 0.18942 |
| ³He | 9 | 3 | 209.15 | 0.20658 | 43.206 | 15.10 | **2.861** | 0.07160 |
| ⁴He | 12 | 4 | 3364.6 | 0.05536 | 186.26 | 55.37 | **3.364** | 0.01605 |

Two clear monotone trends:

1. **The overshoot is atom-DEPENDENT and grows with A:** `2.05 → 2.86 → 3.36`. So the deuteron's
   `~2×` is **not universal** — there is no atom-independent overshoot constant (and, correctly, no
   universal "factor-½ P_λ"; the ≈2 flagged as not-pinned in #2631 is now confirmed D-specific). The
   binding redistribution P_λ must **suppress more strongly for heavier atoms**.
2. **The flat-trace bar-mixing SHRINKS with A:** `0.189 → 0.072 → 0.016`. The flat (mass-side)
   distribution becomes progressively more bar-(transpose)-symmetric for heavier atoms, so the
   **bar-symmetrising burden on P_λ is largest for the deuteron** and decreases with A.

(`overshoot/A = 1.02, 0.95, 0.84` is *decreasing*, so the trend is **not** `overshoot = A`; it grows
sub-linearly. No closed form is fitted to three points — that would be numerology.)

## What this constrains (no P_λ proposed)

A single categorical `P_λ(K)` must reproduce **both** trends simultaneously: an **A-growing net
suppression** (effective trace `→ 1/overshoot` of flat: `0.488, 0.350, 0.297`) and an **A-shrinking
bar-symmetrisation** load. That is a genuine two-parameter structural constraint on the open GAP-A-3
projection — and it **rules out** the simplest candidates: a constant `P_λ`, an atom-independent scalar
suppression, and any universal factor-½. The productive `P_λ` must have explicit A-dependence whose
suppression strengthens and whose bar-asymmetry-correction weakens as A grows.

## Critical-distance note

The `A(K)` factors grow steeply (`[3]_q^{2(Z-1)}·(q^{1/2}+q^{-1/2})^{4N}`: A(⁴He)=3365), so each carries
A's ≤2.5% zero-parameter uncertainty (possibly compounding in the exponents). The **monotone overshoot
trend (2.05→2.86→3.36) is far larger than that noise** and is robust; precise overshoot *values* carry
the A-uncertainty. No fit; the underdetermined per-atom P_λ systems are not solved.

No fit; nothing wired; `c_k`/`Δ_λ` cal-anchored.

## Cross-references

- [`2026-06-22-gap-a3-deuteron-A-D-overshoot.md`](2026-06-22-gap-a3-deuteron-A-D-overshoot.md) — the deuteron overshoot (~2.05×) this generalises.
- [`2026-06-22-gap-a3-deuteron-plambda-flat-baseline-bareven.md`](2026-06-22-gap-a3-deuteron-plambda-flat-baseline-bareven.md) — the flat-baseline + bar-even framing.
- [`2026-06-04-gap-a3-brane-tower-level-selection-scope.md`](2026-06-04-gap-a3-brane-tower-level-selection-scope.md) — the A(K) formula + the open P_λ.
