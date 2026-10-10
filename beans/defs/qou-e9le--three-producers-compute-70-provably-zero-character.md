---
# qou-e9le
title: three producers compute 70 provably-zero characters — the two-row cap is proved in Lean and unused in compute
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-26T06:46:25Z
updated_at: 2026-10-10T10:32:41Z
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


## 2026-10-10 — a THIRD route carries the residue, and it reached an exact-zero assertion (session session_01ST9RpvTF7JHNdUNafrjf9J, PR #7551)
**The proton y_λ table is the source, not only the 'cached' y-lambda-at-q0 route.** `computations/y-lambda-mpfr-proton-witness.json` (default of `tr_m_wenzl_bridge_mpfr._load_y_lambda` / `load_y_lambda_for_q0` for the proton pin) stores **every** ≥3-row entry for n = 3..12 as residue — **287 entries, |y| from 1.0e-73 to 3.9e-72**. n ≥ 13 entries are exact 0, and the MUON table (`y-lambda-mpfr-witness.json`) is exact 0 at every n. Measured by reading both tables, mpf comparison `!= 0`.
**Propagation:** `chi_at_q0_via_hoefsmit_mpfr.py` copies these into `chi-deuteron-h6-at-q0-50dps.witness.json` (7 residue entries at n=6), which `rho_w_crystal_vertex_trace.py` read, which made three exact-zero SUPPORT assertions in `probes/delta_lambda_closure_tl_support_probe.py` FAIL spuriously. Fixed at `rho_w` with the row-count remedy this bean recommends (snap ℓ>2 to exact 0, refuse above 10^-(dps-10)), commit 3d8010bc52.
**Consumer audit (73 readers of the cache or the loader), grep for zero-tests / log / division / sign on y:** no wrong NUMBER found. `probes/lr_hecke_character_probe.py:183` prunes on `y_lam == 0` — residue only costs extra terms × ~1e-72 (compute, not value). `brng_*` probes take log|y| of the DOMINANT (two-row) block only. `audits/y_lambda_two_row_cap_gate.py` already tolerates ~1e-73. Caveat: a grep is not a proof of absence; a consumer testing zero by an unforeseen spelling would be missed.
**Root-cause option, NOT taken (owner call):** make `regenerate_y_lambda_mpfr.py` emit exact 0 for ℓ(λ) > N (as the computed route already does) and regenerate the proton table. Fixes all 73 readers at once; moves no recorded number above ~1e-72; but rewrites a central input table.


## 2026-10-10 CORRECTION to the entry above (same session)
**'287 entries' was my arithmetic error; the count is 223.** The per-n counts I listed (1, 2, 4, 7, 11, 17, 25, 36, 50, 70 for n = 3..12) sum to 223; I mis-added them. Re-measured by a second, independent walk of the table (mpf, 0 < |y| < 1e-60 on ℓ ≥ 3). The wrong figure also appears in commit cbf8611031's message (pushed; not rewritten) and in my chat report; nothing else repeated it.
**Downstream measured:** 14 witnesses copy the residue into their own payload — chi_at_q0_via_hoefsmit_mpfr caches (deuteron/diproton/dineutron h6, tritium/³He h9, ⁴He h12, proton/neutron h3), a-K-via-lp-dual(-full), two Rust matrix-M caches (⁴He h12, deuteron h6 90dps), probe-pauli-young the3 signtest, probe-d-delta-lambda-terms. Owner approved (2026-10-10, '1 and downstream'): producer fix + proton-table regeneration + those 14; in progress.
