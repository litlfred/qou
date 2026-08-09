---
# qou-pin6
title: 'pentagon_reduction_li2q witness is stale by 5 ORDERS OF MAGNITUDE on T1_atom — unrelated to q0, held out of the load_q_50dps migration'
status: todo
type: task
priority: normal
created_at: 2026-08-08T23:10:00Z
updated_at: 2026-08-08T23:10:00Z
---

Held out of the 2026-08-08 `load_q_50dps` default-flip migration, deliberately,
after the value audit caught it. Same discipline as `qou-pin3`: an anchor
migration is bookkeeping, and a substantive change must not ride in on one.

## What the audit saw

`pentagon_reduction_li2q` is one of the 15 producers whose q₀ moved when
`_li_2_q_util.load_q_50dps()`'s default flipped from the muon pinning witness to
the caller's own resolved pin. Regenerating it moved 18 fields by far more than
an 11.5 ppb q₀ shift can produce — `T1_atom` by **five orders of magnitude**:

    atom   committed        regenerated
    D      4.5283072561     0.0000305810737
    T      2.4610392279     0.0000019192797
    3He    1.4866054031     0.0000022644584

`ratio_pred_over_AME` and `B_MeV_first_plus_T3` move with it (up to 5.0e-02).

## Why it is NOT the q₀ flip — a three-way run, not an inference

Ran the producer under BOTH arms in the same container:

    arm A   pre-flip  `_li_2_q_util.py` + `q0_anchor_manifest.json` from HEAD
    arm B   post-flip working-tree versions

    atom | committed        | arm A (pre-flip)   | arm B (post-flip)
    D    | 4.5283072561032  | 0.0000305810737085 | 0.0000305810737085
    T    | 2.4610392278924  | 0.0000019192796920 | 0.0000019192796920
    3He  | 1.4866054030558  | 0.0000022644583563 | 0.0000022644583563

Arms A and B are **bit-identical**. Both differ from the committed witness by
5 orders. So the flip contributes nothing here (its own A/B delta is 1.154e-08,
exactly the layer separation) — the producer's `T1` computation changed at some
point and the witness was never regenerated.

This is why the audit compares run-vs-run and not committed-vs-run: diffing
against a committed witness measures the change under test **plus** whatever
staleness the file already carried, and attributes all of it to the change.

## Next step

Find the commit that changed `T1_atom`'s definition and decide whether the
current code or the committed witness is right — a 5-order move in a per-atom
tower term is either a real correction or a real regression, and it is not
knowable from the witness alone. `git log -p --follow computations/pentagon_reduction_li2q.py`
over the T1 block is the place to start.

Only then regenerate, as its own change with its own justification.

## Held out mechanically, not by memory

`computations/audits/load_q_50dps_flip_regenerate.py` carries
`HOLD_OUT = {"pentagon_reduction_li2q"}` with this evidence inline, and the
hold-out gates both `--apply` and `--audit-only`. Re-running the migration will
not silently pick it back up.


## SECOND INSTANCE 2026-08-08 — `probe_9b_gate_interface_algebra`

Found the same way, during the UNDETERMINED-pin triage. Its witness records
`muon` while the code resolves proton (tnjb class), so it was a declaration
candidate — but regenerating it flips `allPassed` True → False on two
assertions, both **cross-witness comparisons**:

    structural_constants_match_probe1     0.0      -> 7.330992e-07  (tol 1e-09)
    m3_residuals_match_hpower_witness     5.82e-15 -> 2.894e-06     (tol 1e-09)

**Proven pre-existing, not caused by the 2026-08-08 anchor work.** Ran the
producer from a `git worktree` at the base commit `d8d22890` — before any of
that day's changes — and it emits **bit-identical** failing values. So the
committed witness is stale and the producer has been unable to reproduce it
since before this branch existed.

Not declared, deliberately. Declaring it would convert an UNDETERMINED pin into
a **DECL_MISMATCH**, which is worse: the declaration only pays off once the
witness matches, and it cannot be regenerated without committing an assertion
failure.

Next step is the same shape as pentagon's: find what moved
`structural_constants_match_probe1` away from its comparison target, decide
whether the current code or the committed witness is right, then regenerate as
its own change. Both comparison targets are other witnesses, so the answer may
be that one of THEM is the stale side.

Held out mechanically in `computations/audits/q0_undetermined_triage.py`
(`HOLD_OUT`), with this evidence inline.


## THIRD AND FOURTH INSTANCES 2026-08-08 — surfaced by the qou-pin5 stamping work

Adding a `stamp_staleness_metadata` call cannot change a computed value — it
mutates metadata keys on an already-built payload. So when regeneration moved
values in two of the 14, that movement was pre-existing staleness being exposed.

Confirmed rather than argued: reverted the edit, ran the **unmodified HEAD**
producer, and got the same moved values.

    option_e_probe1_derive_1plusq_over_2
        decisive_fit_test.required_factor_muon
            committed 1.0537173577644955…  HEAD rerun 1.0535280770898103…
        residual_muon_pct    0.12070979 -> 0.13869784   (|Δrel| 1.3e-01)
        residual_proton_pct  0.12069868 -> 0.13868673
      Note this is a muon-vs-proton COMPARISON probe (the class the owner ruled
      legitimate), so both layers moving together points at a shared upstream
      input, not at an anchor question.

    rho_w_crystal_vertex_trace
        by_partition[0].chi_lambda_cached
            committed 1.5597586581034162…  HEAD rerun 1.5598702809528043…
        by_partition[1].chi_lambda_cached
            committed 3.2158908784733051…  HEAD rerun 3.2163178980816625…
        crosscheck_abs_err moves by |Δrel| 1.0 — the field whose whole job is to
        detect exactly this.
      The name says `chi_lambda_CACHED`: the likely story is a χ cache that was
      rebuilt while this witness was not.

Both witnesses were REVERTED; the stamping code fix was kept. That is the
conservative combination: the committed witness keeps its (correct, backfilled)
pin and no staleness is swept in, while the next deliberate regeneration will
produce the pin properly.

Next step for both: find what moved the upstream value, decide which side is
right, regenerate as its own change. `crosscheck_abs_err` in the second one is a
built-in oracle — read it first.


## RESOLVED for `rho_w_crystal_vertex_trace` 2026-08-09 — and MY FIRST VERDICT WAS BACKWARDS

The committed `rho-w-crystal-vertex-trace.witness.json` records `crosscheck_abs_err ≈ 1e-49`
against `chi-deuteron-h6-at-q0-50dps.witness.json`. Re-running gives **1.1e-4**. Chasing it
down took two passes, and the first one reached the wrong answer.

### Not a q₀ question

The muon/proton separation moves `chi^[6]` by 8.1e-8 — four orders too small. Running
`rho_w` under `QOU_Q0_ANCHOR=ideal` leaves the crosscheck at 1.115e-4, unchanged. Both
producers are stable and reproduce themselves.

### 🛑 The first verdict, and why it was wrong

Of the partitions of 6 exactly two — `[6]` and `[1^6]` — give **1-dimensional** Hecke reps,
where every generator is a scalar and the braid word collapses to a product. That looked like
an independent arbiter, and it said `rho_w` was right and the cache wrong (matching `rho_w`
to 15 digits, missing the cache by 1.1e-4).

It was **not independent**. The closed form fixed the interface ("averaged") crossing at
`I = s − h/2` — the COLOR-BLIND form — which was read straight out of `rho_w`. Adopting one
disputant's convention and then finding it agrees with that disputant proves nothing.

### The real answer: fit the convention, do not assume it

`canonical_braid_crossings.classify_crossing` maps **two physically distinct** crossings onto
one label:

    d = -h/2                  color-BLIND
    d = -h*(1/2 - delta/4)    color-WEIGHTED p-n interface

Both return `"averaged"`, and `atom_canonical_crossings` returns only `(gen_idx, ctype)`.
**The label is lossy**: a consumer rebuilding operators from it cannot recover which it had.

Fitting `k` = how many averaged crossings take the weighted form
(`computations/audits/chi_interface_convention_fit.py`):

    atom        Z,N   n_avg   fit k   |diff|      Z*N
    proton      1,0     2       0     4.8e-50      0
    neutron     0,1     2       0     2.1e-50      0
    diproton    2,0     4       0     8.6e-50      0
    dineutron   0,2     4       0     9.4e-50      0
    deuteron    1,1     5       1     5.6e-20      1
    tritium     1,2     7       1     5.6e-20      2
    helium-3    2,1     7       1     8.6e-20      2
    helium-4    2,2     9       1     8.7e-20      4

Exact to machine zero in all eight, with **k = 1 exactly when the atom has both a proton and
a neutron**. Note it is NOT `Z*N`, the p-n pair count — the natural guess, ruled out by
tritium, helium-3 and helium-4.

### Verdict, reversed

**The cache is CORRECT.** `chi_at_q0_via_hoefsmit_mpfr` applies the color-weighted interface
on the p-n crossing. `rho_w_crystal_vertex_trace` builds `I_g = sigma_g - (h/2)*1` for EVERY
averaged crossing, dropping `delta` on that one crossing — which is exactly why homogeneous
atoms (p, n, pp, nn, no p-n interface) agree to 1e-50 and every mixed atom does not.

So the committed `rho_w` witness is not merely stale: the producer has a real defect, and its
`crosscheck_abs_err` field is the thing that catches it.

### Two follow-ups

1. **Fix the API, not each consumer.** `classify_crossing` should distinguish the two
   (`averaged` vs `averaged_pn`) or return the coefficient. Every consumer rebuilding
   operators from `atom_canonical_crossings` output inherits this today.
2. **`chi_at_q0_via_hoefsmit_mpfr`'s resume path keys only on partition shape** —
   `already[tuple(entry["partition"])]` — with no q₀ or dps check. Re-running it at a
   different anchor reuses every cached value and re-stamps the CURRENT `q_0_50dps` onto
   them; observed turning a muon-computed cache into one labelled proton without recomputing
   a single χ. It cannot cause the 1.1e-4 (a from-scratch rebuild reproduces it) but it is a
   straddle generator. Its `--help` also advertises `--atoms` while the parser takes
   positional atom names.

Lean: `QOU.MassTheory.OneDimWordCharacter` (sorry-free) proves the word collapse that makes
the fit legitimate. Its `interface_on_trivial_rep` needs `2 ≠ 0` — in characteristic 2 the
identity is false, which `ring` correctly refused before the hypothesis was added.
