---
# qou-6e88
title: 'cauchyMul_order: the statement may need strengthening before it is provable'
status: todo
type: task
created_at: 2026-08-08T07:04:15Z
updated_at: 2026-08-08T12:55:00Z
---

`QOU/Mathlib/QGevreyOrder.lean:261`.

Unlike the other sorries this is not purely a missing proof. Per the
file's own note, the `≥` direction needs a **non-cancellation hypothesis
on the leading coefficients** — in a general normed field the
boundary/saddle term may genuinely cancel, which would make the theorem
as stated FALSE.

So the first task is not to prove it but to decide the right statement:
either add the hypothesis, or restrict the field. Worth settling before
anyone spends effort on a proof.

The `≤` direction is reportedly close: it reduces to two sorry-free
lemmas already in the file (`cauchyMul_norm_le_sum`,
`exponent_le_envelope`) plus an ε-δ assembly. That half may be the
tractable piece.

## SETTLED 2026-08-08 — it is not "may be false", it IS false as stated

Explicit witness: `computations/qbeta/cauchymul_order_cancellation_witness.py`
(+ `.witness.json`). Exact integer arithmetic, q = 2, n <= 14.

    a_n := q^(n^2)        log_q|a_n| = n^2 exactly        -> positive order
    b   := a^{-1}         formal inverse (a_0 = 1 a unit)
    a*b  = (1,0,0,0,...)  the UNIT sequence               -> order 0

The one thing that could have spoiled it -- `b` secretly being of order 0, making
this a divergent times a convergent series rather than genuine cancellation --
does not happen: `log_q|b_n| / n^2` rises monotonically to **0.9949 at n = 14**,
so `b` carries the SAME positive order as `a`.

Two factors of equal positive order; product of order 0. For any envelope
positive on `s,t > 0` -- which `cauchyEnvelope` must be, since its job is to
dominate a product of divergent series -- this gives

    order(a*b) = 0 < E(s,t),

contradicting `>=`.

**Normalization-robust.** The conclusion does not depend on the constant in
`IsQGevreyOrder`: whatever positive order the convention assigns `a`, it assigns
the same to `b`, since their coefficient growth agrees asymptotically. No choice
of normalization rescues the statement.

**So the fix is a HYPOTHESIS, not a proof.** As this bean already anticipated:
add explicit non-cancellation on the leading coefficients, or restrict to a
setting (positivity / suitable field) where the driving subtraction cannot occur.
Nobody should spend a session trying to prove `>=` as currently written.

**The `<=` direction is untouched** and remains the tractable half.

## DONE 2026-08-08 — hypothesis added, `≤` half proved

Both actions this bean called for are landed (`49567bc98`).

**The statement is repaired.** `cauchyMul_order` now carries
`hnc : NoCancellation a b` — eventually some fixed `c > 0` has
`c·‖a_k‖·‖b_{n−k}‖ ≤ ‖(a⋆b)_n‖` for every `k ≤ n`. It constrains the product's
*norm* against its summands' norms and says nothing about its order, so it does
not assume the conclusion. `not_noCancellation_of_cauchyMul_eventually_zero`
(sorry-free) shows it genuinely fails in the witness's situation — otherwise
"add a hypothesis" would be indistinguishable from weakening the statement until
it became true.

**The `≤` half is proved, sorry-free and UNCONDITIONALLY** —
`cauchyMul_bound`. Not via the ε-δ route this bean anticipated: in the header's
own *bound form* (`‖a_n‖ ≤ C·Aⁿ·q^{s n²/2}`) the upper half is finitary, so
there is no ε-δ and no `logb q 0 = 0` wrinkle at vanishing coefficients. It
needs no non-cancellation hypothesis at all — bounding a sum of norms never
requires knowing the terms fail to cancel. Only `≥` was ever false.

Also landed: `envelope_shift_le` — raising both slopes by `δ ≥ 0` raises the
envelope by at most `δ`, the algebraic content of the limit↔bound step.

**What is left is the `≥` half alone** (the file's single remaining `sorry`,
cited): pick `k ≈ θ*·n` attaining the envelope, then apply `hnc` to transfer
that summand's growth to the convolution. It now sits on a statement believed
true rather than one known false.

Verified: `lean`-direct exit 0; `#print axioms` clean on all three new results.
Closing is a human action — leaving status as-is.
