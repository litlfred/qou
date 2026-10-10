---
# qou-e9le
title: three producers compute 70 provably-zero characters — the two-row cap is proved in Lean and unused in compute
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-26T06:46:25Z
updated_at: 2026-10-10T12:39:39Z
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


## 2026-10-10 — exact-zero y table + downstream regenerated (owner: '1 and downstream')
- `regenerate_y_lambda_mpfr.py`: ℓ(λ)>2 weights now taken from the structural Schur zero (`y_lambda_su_n`, factor [0]_q), written "0" only if that value is exactly 0 AND the Wenzl residue ≤ 10^-(dps-10), else REFUSE. Two-row weights still from Wenzl, cross-checked to 1e-60. Also restores the dropped `q0Value`.
- Proton table: 98 two-row entries byte-identical to HEAD (verified independently); 1497 ≥3-row entries exactly 0 (223 changed from residue). Second writer `y_lambda_tower_infra.py` (n=13..18) left as at HEAD (its own gate fails pre-existing, 2.05e-50 > 1e-60 at n=13 — not touched).
- Regenerated: 8 hoefsmit χ caches (only ℓ>2 y/contribution fields moved; chi and tr_M_at_q0 byte-identical — spot-verified ⁴He and ²H), ⁴He matrix-M cache, a-K-via-lp-dual (a_K unchanged), probe-pauli-young signtest (sign_census was counting signs of solver residue on 25/30 partitions: {+11,−19} → {+1,−4,0:25}), probe-d-delta-lambda-terms (also refreshed stale non-y fields from changed upstream witnesses; two-arm run confirms those are staleness, not this change; allPassed False→True).
- **NOT applied, two findings:** (1) `a-K-via-lp-dual-full`: its ℓ>2 duals were scaled by the residue (5931.63 → 0.593163; chirality_dual_sum 5932.63 → 1.5932); the LP is degenerate there and the producer already says it needs re-posing on the two-row quotient — regenerated copy NOT committed. (2) `chi-deuteron-h6-at-q0-90dps-matrix-m`: rerun moves χ O(1) and tr_M 2.17545 → 1.45470 — staleness independent of y (likely word change), no named consumer — NOT committed. Both await owner.


## 2026-10-10 — (A) done: aK_via_lp_dual_full re-posed on the two-row quotient

- The degeneracy was **not** caused by the data. Each vanishing ℓ≥3 block was a zero-cost column with a vacuous `0·x ≥ 0` row, i.e. a free variable that absorbed the net constraint. That is exactly the radical vector `v` in `y_0_eq_zero_of_radical`. Round-off in the old y-table then set the three-row duals (e.g. proton [1,1,1] u* 5931.6 → 0.593 after the exact-zero regen: a scale artifact).
- Producer now drops ℓ>2 blocks, and refuses (SystemExit) unless each dropped `y_lambda` and `contribution` is **exactly** 0. Dropped counts are 1/1/7/25/25/70; no zero-cost two-row column remains.
- Result: every atom is feasible with gap ≤ 7e-42. y0* = 0.0694 (p), 0.0920 (n), 0.0108 (d), 0.0031 (t), 0.0062 (³He), 0.0003 (⁴He).
- a_K^dual = 13.98 / 10.11 / 188.7 / 923.6 / 384.8 / 17734 against the closed form C = 1 / 1 / 1.209 / 0.956 / 0.956 / 0.915. **Scope-(a) negative for the block-diagonal projector basis only.** The proposition's LP is over the full Hecke basis, which is still open.
- Author note added to `mass-coefficient-shadow-price.ts`.
- probe-float64-guard: 9 hits both before and after (all pre-existing).


## 2026-10-10 — (B) done: 90-dps deuteron matrix-M cache refreshed

- `chi-deuteron-h6-at-q0-90dps-matrix-m` and its summary sibling `chi-at-q0-matrix-m-deuteron` disagreed with their own producer, `chi_at_q0_via_matrix_m_mpfr.py`. tr_M was 2.17545 recorded and 1.45470 live.
- The two 1-dim characters are byte-identical: χ(6) = 11.0214 and χ(1⁶) = −0.0907. Every higher-dimensional χ moved by O(1). So the crossing signs agree and only the word ORDER differs, consistent with the 2026-09-05 grouped→interleaved word change (inferred from the pattern, not bisected).
- The re-run reproduces the earlier regeneration byte-for-byte. The producer's own cross-check against `chi_q_via_gp` gives 11/11 at 1e-85.
- NOT a contradiction with `chi-deuteron-h6-at-q0-50dps` (tr_M 0.152). That cache declares convention `colour-weighted-averaged-crossing`; the 90-dps one declares `sign-only-crossings`. They are different objects.
- No code consumer (orphan-witness triage Tier C). The 90-dps file is in the sign-only convention, not the R3-canonical colour weighting. Whether to retire it is left open here.
