---
# qou-0z7n
title: 'MI-2: cauchyMul_order is FALSE as stated — refute, restate, prove the envelope upper bound'
status: in-progress
type: task
created_at: 2026-08-08T15:44:37Z
updated_at: 2026-08-08T15:44:37Z
---

Branch: `claude/sorry-audit-joo5` (qou).
File: `content/quantum-observable-universe/lean/QOU/Mathlib/QGevreyOrder.lean`.

## The finding

`cauchyMul_order` (the one cited `sorry` in the file) is **false as stated**, not
merely open. It quantifies over an arbitrary normed field `K` with no
non-cancellation hypothesis, and `IsQGevreyOrder` is a *limit* statement, so:

    a := q^(s·n²/2)   (order s = 2, via the file's own `order_of_rpow_gaussian`)
    b := 0            (order t = 0, since `Real.log 0 = 0` ⇒ every ratio is 0)
    a ⋆ b = 0         (order 0)
    cauchyEnvelope 2 0 = max 2 0 = 2 ≠ 0

so the theorem would give `IsQGevreyOrder q 2 0`, contradicting `order_unique`.
A `sorry` in front of a false proposition is worse than an open gap: closing it
would close `False`, and anything downstream of it is unsound. (Nothing in-tree
imports this file's `cauchyMul_order` yet, so no live consumer is affected.)

The file's own docstring already half-flags this — "the `≥` direction
additionally needs a non-cancellation hypothesis on the leading coefficients"
and the numerics were run with "positive/no-cancel coefficients" — but the
hypothesis never made it into the statement.

## Disposition

Mirrors the in-repo `SnWedderburnPartitionBridge.freeProjClaim_false`
precedent — refute the over-general form by machine proof, then state the true
one.

1. `cauchyMul_order_unhypothesised_false` — machine-proved refutation. DONE
2. Restate `cauchyMul_order` over `ℝ` with strictly positive coefficients (no
   cancellation possible), which is exactly the regime the file's numerics
   verified. Cited `sorry` retained — the Laplace/saddle assembly is still
   genuine open work. DONE
3. Convert as much of the gap as possible into sorry-free content:
   - `cauchyEnvelope_add_le` — `E(s+ε,t+ε) ≤ E(s,t)+ε` (the four-branch case
     analysis of the closed form). DONE
   - `cauchyMul_norm_le_envelope` — global Gaussian bounds on `a`, `b` ⇒ the
     envelope bound on `a ⋆ b`. Assembles the two existing sorry-free lemmas.
     DONE
   - `exists_global_gaussian_bound` — limit form ⇒ *global* (not just eventual)
     Gaussian bound, by summing the finite initial segment. DONE
   - `cauchyMul_norm_eventually_le` — **the whole `≤` direction, unconditional
     and sorry-free**: for every `ε > 0`, eventually
     `‖(a⋆b) n‖ ≤ q^((E(s,t)+ε)·n²/2)`. DONE

After (3) the residual cited `sorry` is only the `≥` (lower / non-cancellation)
direction; the upper direction is no longer cited at all.

## Note for whoever closes the residual sorry

State the lower bound in *norm* form too, not in `logb` form: `Real.log 0 = 0`
makes `logb q ‖x‖` return `0` at `x = 0`, which is what lets the refutation
above go through and would silently poison any `logb`-shaped upper bound when
`E(s,t) < 0`.

## COLLISION (2026-08-08, on integrating `main`)

A sibling found the **same falsity independently** and landed it first:
`fd603a0270 lean(MI-2): cauchyMul_order was FALSE -- add the hypothesis, and
prove the true half`. Merging `origin/main` conflicted on this file. Resolution:
**take main's version wholesale**, then re-apply only what is genuinely mine.

Their fix is better in two ways and I kept it:

* **Stronger witness.** They refute with `a n = q^{n²}` against its formal
  inverse — *two factors of equal positive order whose product has order 0*.
  That is normalization-robust: whatever positive order the convention assigns
  `a` it assigns the same to `b`, and `cauchyEnvelope` is positive on `s,t > 0`,
  so no rescaling of the definition rescues the statement. My witness (`b = 0`)
  leans on the `Real.log 0 = 0` junk value and could be waved away as a
  convention artefact.
* **More general repair.** They added a `NoCancellation` predicate and kept the
  theorem over an arbitrary normed field, rather than restricting to `ℝ` with
  positive coefficients as I did. Strictly more useful — if it can be proved.

They also already had `envelope_shift_le` (my `cauchyEnvelope_add_le`) and
`QGevreyBound` + `cauchyMul_bound` (a cleaner bound-form `≤`, absorbing the
`(n+1)` term count via `n+1 ≤ 2ⁿ`), plus a whole q-Gevrey *level* layer my branch
never had.

## What survives as mine

Kept, adapted to their names and definitions:

* `cauchyMul_order_of_pos` — the law **proved** for positive real coefficients.
  Their `cauchyMul_order` is still `sorry`; this is a genuine partial discharge
  of it, not a parallel statement.
* `noCancellation_of_pos` — positivity ⇒ their `NoCancellation`, with `c = 1`.
  Pairs with their `not_noCancellation_of_cauchyMul_eventually_zero` (which shows
  it can fail) to pin the hypothesis as a real side condition: neither vacuous
  nor automatic. Neither of us had this.
* `cauchyMul_order_unhypothesised_false` — a fully machine-checked Lean
  refutation needing no external witness. Theirs proves the *hypothesis fails* on
  a pair whose construction lives in a Python file; mine proves the *statement*
  false inside Lean. Complementary, and both are now in the file with a note
  saying which is stronger as evidence and which as proof.
* The MI-4 `≥` machinery, and the two bridges `qGevreyBound_of_isQGevreyOrder` /
  `coeff_le_of_qGevreyBound` that let the `≥` proof consume *their*
  `cauchyMul_bound` rather than duplicating the `≤` analysis.

Dropped as duplicates of theirs: `cauchyEnvelope_add_le`,
`cauchyMul_norm_le_envelope`, `eventually_linear_le_rpow_sq`,
`cauchyMul_norm_eventually_le`.
