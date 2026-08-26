---
# qou-e9le
title: three producers compute 70 provably-zero characters — the two-row cap is proved in Lean and unused in compute
status: todo
type: task
created_at: 2026-08-26T06:46:25Z
updated_at: 2026-08-26T06:46:25Z
---

## The claim

`QOU/MassTheory/TwoRowCapDerived.lean` is sorry-free, `#print axioms`
clean, and proves — for arbitrary observable `χ` and arbitrary `Δ` —

    traceSum_eq_twoRow_of_wenzl     restricting  Σ_λ y_λ χ_λ  to two-row λ
                                    IS AN IDENTITY
    threeRowPart_eq_zero_of_wenzl   the residual share is 0, not "small"
    twoRow_share_eq_one_of_wenzl    the two-row share is exactly 1

Three `computations/` producers perform exactly that sum and **do not use
it**, so they compute the provably-zero terms:

    chi_4he_via_rust_lossless.py
    chi_via_rust_lossless.py
    block_swap_binding.py

At `n = 12` that is **77 characters computed where 7 carry the answer** —
70 of them proved to contribute nothing.

## Why the guard cannot fire on its own

`block_swap_binding.tr_M_of_word` already has the right shape:

    y = y_table.get(st)
    if y is None:
        continue

but `_load_y_lambda(12, ·)` returns **all 77 shapes as nonzero**, so the
guard never fires. Measured:

    two-row  y :  2.3e-4 … 4.0e-3      (7 shapes)
    >2-row   y :  max 1.03e-73         (70 shapes)

~1e-70 apart. The cap holds numerically — those are the residue of
whatever solve produced the table, against a value the Lean says is
exactly zero. The producer has no way to tell `1e-73` from `0` without
either a magnitude threshold or a row-count test, and it does neither.

## What this is NOT

**Not a correctness bug.** The dropped terms are provably zero and the
residue is ~1e-70 below the surviving weights, so the committed numbers
are right. This is wasted compute, not a wrong answer.

**Not established to fix the timeouts.** `block_swap_binding` has now
failed at 25 s, 180 s (twice) and 900 s. The prune is ~11x at `n = 12`.
Whether 11x closes that gap is **unmeasured** — and the early evidence
says probably not on its own: a probe of the 77 characters on a
22-letter synthetic word has run > 20 min without completing 10 of them,
i.e. **> 2 min per character at n = 12**. At 8 words per run even the
pruned 7-shape loop would be ~2 h. Do not sell this as "makes the
producer tractable" until someone measures the real word.

Caveat on that figure: my probe word is dense (every generator 1..11,
twice) and may be pathological relative to the producer's actual word.
The per-character cost is the thing to re-measure, not to inherit.

## Why it is worth doing anyway

This is the formalize-first discipline running in reverse. The invariant
was proved on 2026-08-16 (PR #5242) and the compute never picked it up.
An exact, proved prune that removes 90 % of the work in three producers
is worth wiring whether or not it single-handedly rescues one timeout.

## How it was found

Not by a targeted audit — by asking why `block_swap_binding` times out,
which is the producer the original `qou-wlaf` stall investigation was
about. Its sibling `gram_norm_binding_probe` got the object-dtype fix
(3H 2131 s -> 0.45 s); this one never got anything.

Note also a false start worth not repeating: a first screen reported one
of the four producers as already guarded (`rowguard=1`). That match was
`t[1] <= 2` filtering **braid generator indices**, not partition row
counts. None of them guards on `ell(lambda)`. Same substring-vs-meaning
class as the `elapsed_reduce_sec` mask bug.
