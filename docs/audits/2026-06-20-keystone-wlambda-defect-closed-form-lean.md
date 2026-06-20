# W_λ defect closed form — Lean formalization (2026-06-20)

**Status:** audit — formalize-first follow-up. Discharges the deferred Lean
opportunity flagged in
[`2026-06-20-keystone-wlambda-C-n-closed-form.md`](2026-06-20-keystone-wlambda-C-n-closed-form.md)
("Identity I … is a clean candidate for a Lean lemma; deferred — the sandbox Lean
toolchain is currently network-blocked"). The toolchain is available this session
(Mathlib oleans restored from the `lake-cache/qou-v4-24-0` branch), so the result
is now a checked theorem.

## What is formalized

[`content/quantum-observable-universe/lean/QOU/BraidKnot/WLambdaDefectClosedForm.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/WLambdaDefectClosedForm.lean)
(namespace `QOU.BraidKnot.WLambdaDefect`, base ring `ℤ`). **Verified sorry-free
via lean-direct** (`lean` exit 0).

The q-Plancherel partition-function defect `1 − Z(n) = C(n)·h² + O(h⁴)` has its
coefficient `24·C(n) = 2M(n) − S_n − 2n`, where `S_n = Σ_{k=1}^n (k²−1)` and
`M(n)` is the Plancherel-expected squared-hook sum. The single
representation-theoretic input is the compute-verified **Identity I**
(`M(n) = n(3n−1)/2`, checked in exact integer arithmetic for `n = 2..14` in the
producing script); it is carried in cleared form `twoM n = n(3n−1)`.

| Lean decl | statement |
|---|---|
| `twoM`, `sixS`, `n144C` | cleared-denominator defs of `2M(n)`, `6S_n`, `144C(n)` |
| `n144C_closed_form` | `144·C(n) = −n(n−1)(2n−13)` — the cubic (pure `ring`) |
| `n144C_table` | reproduces #2525's `24·C(n) = 3,7,10,10,5,−7,−28` (n=2..8) |
| `n144C_pos` | `C(n) > 0` for `2 ≤ n ≤ 6` |
| `n144C_neg` | `C(n) < 0` for `n ≥ 7` — the exact n=7 sign change |

## What this buys

- **The keystone C(n) result is now a checked theorem, not a verified table.**
  The collapse from Identity I + the `S_n` formula to the cubic
  `−n(n−1)(2n−13)` is a `ring` identity; the sign change at `n = 7` is the linear
  factor `(2n−13)` crossing zero, proved by `interval_cases` (positive regime) and
  positivity (negative regime). Off-by-one drift in the cubic is now impossible.
- **Constraint for the geometric frontier, at proof level.** Per the parent
  audit, any `S¹`-equivariant index realizing `W_λ` (the owner-gated #2503 DG
  plan) must reproduce a sub-leading heat-kernel coefficient *exactly* equal to
  `−n(n−1)(2n−13)/144`. That falsifiable target is now machine-checked.

## Scope / discipline

- **Conditional on Identity I.** The Plancherel mean `M(n) = n(3n−1)/2` is carried
  as a definition (compute-verified n=2..14), not re-proved from RSK/Plancherel
  theory (that would need machinery not readily available in Mathlib). The
  *algebraic collapse* and the *sign change* — the parts that were merely tabulated
  — are proved outright. This mirrors the §3b conditional-input discipline: the
  single named input is explicit, everything downstream is verified.
- **No archimedean input, no fit.** Pure `ℤ`; `q₀` and the 210 ppb target never
  appear. The geometric realization of `W_λ` stays owner-gated; no physical claim
  is introduced.

## References

- [`2026-06-20-keystone-wlambda-C-n-closed-form.md`](2026-06-20-keystone-wlambda-C-n-closed-form.md) — the closed-form derivation (main `ffcbcde3`).
- [`2026-06-20-keystone-wlambda-Z-defect-n-scaling.md`](2026-06-20-keystone-wlambda-Z-defect-n-scaling.md) — the defect's n-scaling (PR #2525).
- `content/quantum-observable-universe/lean/QOU/BraidKnot/WLambdaDefectClosedForm.lean` — this formalization.
