# `QGevreyOrder.cauchyMul_order` was a false cited `sorry` — closed by refute-then-restate

**Date:** 2026-08-22 · **Bean:** `qou-zsg6` (CLOSED) · **File:**
[`content/quantum-observable-universe/lean/QOU/Mathlib/QGevreyOrder.lean`](../../content/quantum-observable-universe/lean/QOU/Mathlib/QGevreyOrder.lean)
· **Discipline:** `lean-proof-vacuity-audit` §9 (`proof-no-false-cited-sorry`),
recipe 5 (refute → restate → prove).

## What the residual `sorry` actually was

The last `sorry` in `QGevreyOrder.lean` sat in the general (normed-field)
convolution order law `cauchyMul_order`. The bean note described it as the
*interior-optimum (saddle) case* still needing an `RSZ slope=order` argument.
**That was stale**: the interior saddle `θ* = t/(s+t)` is already proved
sorry-free for positive real coefficients in `cauchyMul_order_of_pos` (the
`⌊θ·n⌋` floor construction + `tendsto_logb_comp`).

The real defect is worse and was pre-flagged in the vacuity audit
([`lean-proof-vacuity-audit.md` §9](../../.claude/skills/local/lean-proof-vacuity-audit.md),
table row `QGevreyOrder.cauchyMul_order`): **the statement is FALSE as written.**
The `hnc : NoCancellation a b` hypothesis added 2026-08-08 to repair the earlier
unhypothesised falsehood does **not** suffice.

### The sharpened counterexample — `NoCancellation` alone is not enough

Over `ℝ`, `q = 2`: take `a n = 2^{n²}` (q-Gevrey order `2`) and `b ≡ 0`
(order `0`). Then `a ⋆ b = 0`, so for every `k`

    c · ‖a_k‖ · ‖b_{n-k}‖ = c · ‖a_k‖ · 0 = 0 ≤ 0 = ‖(a⋆b)_n‖,

i.e. **`NoCancellation` holds vacuously**. Yet the conclusion claims
`a ⋆ b` (identically `0`, order `0`) has order
`cauchyEnvelope 2 0 = max 2 0 = 2`. `order_unique` then forces `0 = 2`.

So `NoCancellation` controls the *product's* norm against its summands but says
nothing when a *factor* vanishes. The genuinely missing hypothesis is
non-vanishing of the factors — exactly what `cauchyMul_order_of_pos` supplies via
strict positivity.

## Fix (recipe 5: refute → restate → prove) — sorry-free

1. **Refute** (`5a`). `cauchyMul_order_noCancellation_insufficient` — a
   machine-proved `¬ ∀ …` with the `b ≡ 0` witness **and `NoCancellation`
   satisfied**, sharpening the existing `cauchyMul_order_unhypothesised_false`
   (which omitted `hnc`). This is what stops the hypothesis being "simplified
   away" later.
2. **Restate** (`5b`). `cauchyMul_order` now carries the forced non-vanishing
   hypotheses `∀ n, a n ≠ 0` and `∀ n, b n ≠ 0`, alongside `hnc`. Both are
   load-bearing and independent: drop `hnc` and the `q^{n²}`/formal-inverse
   cancellation pair refutes the `≥` half; drop non-vanishing and `b ≡ 0`
   refutes it.
3. **Prove** (`5e`). No separate saddle argument. With the factors nonzero the
   norm sequences `A = ‖a‖`, `B = ‖b‖` are strictly positive, so
   `cauchyMul_order_of_pos` gives `A ⋆ B` order `cauchyEnvelope s t`. The genuine
   product's norm is squeezed

       (c/(n+1))·(A⋆B)_n ≤ ‖(a⋆b)_n‖ ≤ (A⋆B)_n

   — upper by the triangle bound `cauchyMul_norm_le_sum`; lower by summing `hnc`
   over the `n+1` indices — and the `n+1` factor contributes `O(log n)` to the
   exponent, washed out by the `n²` denominator (`Real.log(n+1) ≤ n`). The
   theorem is relocated to just after `cauchyMul_order_of_pos`, since its proof
   depends on it.

## Verification

- `lean`-direct **EXIT=0**, sorry-free (agent-verified per *QA is agent-owned*;
  standalone library file, no `.qa.json` sidecar).
- `#print axioms` on both new declarations: `[propext, Classical.choice,
  Quot.sound]` — **no `sorryAx`**.
- The last `sorry` tactic in `QGevreyOrder.lean` is removed; remaining "sorry"
  strings are prose (`sorry-free`, historical references).

## Note for the audit skill

The `lean-proof-vacuity-audit.md` §9 table still lists
`QGevreyOrder.cauchyMul_order` as a worked example of the pattern — kept as
pedagogy (it is exactly what such a defect looks like); this doc records that the
live instance is now closed.
