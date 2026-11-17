---
# qou-e9le
title: three producers compute 70 provably-zero characters — the two-row cap is proved in Lean and unused in compute
status: in-progress
pr: 8307
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-26T06:46:25Z
updated_at: 2026-11-17T10:37:00Z
parent: qou-5vkl
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


## 2026-08-26 — the trap is in the CACHED route; the COMPUTED route is already exact

`computations/qbeta/qbeta_two_row_zeros_exact_on_computed_route_probe.py` (3/3),
from PR #5864. Read-only: runs no producer, writes no cache.

**Two distinct routes, not variants of one implementation.**

| route | mechanism | >N-row weight |
|---|---|---|
| **cached** — `wedderburn_jones_markov._load_y_lambda_at_q0_witness` | reads `y-lambda-at-q0.witness.json`, built by `y_lambda_at_q0_cache.py` | **solver residue ~1e-73** — the trap this bean tracks |
| **computed** — `y_lambda_su_n(n, q, N)` | evaluates `schur_principal(sh, N, q)` directly | **exactly `0.0`** |

The computed route's zero is **structural**: a Schur function of a shape with
more rows than variables vanishes identically, so it is not a convergence
outcome at all.

**Measured at N = 2 (convention D), n = 2..9** — 0, 1, 2, 4, 7, 11, 17, 25
over-row shapes, **67 in total**, and every one satisfies `v == 0`, not
"below tolerance".

Checked across n **deliberately**: a single-n check would not have been
evidence. I had just been burned treating an n = 3 identity as general
(`qbeta_rank_one_identity_is_n3_only_probe` — that one *failed* at n = 4), so
the same standard applies here.

**What it changes for the three producers.** The row-count remedy is right and
remains the safe general fix, because a consumer cannot tell which route its `y`
arrived by. But there is a second option that removes the question entirely:
on the computed route a truthiness check is *already correct*. Worth knowing
before rewriting three call sites around a new predicate.

**Not claimed:** that the cached witness is wrong. Its residues are ~1e-73 and
move no number; the defect is only that they defeat a `None`/truthiness prune.


## Round 55 Update (2026-11-17, PR #8307)

Applied the Convention-D two-row partition filter (`len(shape_t) <= 2` per `QOU.MassTheory.TwoRowCapDerived.traceSum_eq_twoRow_of_wenzl`) in `computations/chi_4he_via_rust_lossless.py` and `computations/chi_via_rust_lossless.py` (matching `computations/block_swap_binding.py`), and replaced `int(float(...))` with `int(mp.nint(mp.mpf(str(...))))` in `chi_via_rust_lossless.py` (PR #8307, commit `cf8ca11962518083f27bc0a2ce60447359b28381`).
