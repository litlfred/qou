---
# qou-l4q3
title: 'GAP: qbeta_habiro_integrality_kill_test''s hardcoded N3_WITNESS_* constants are stale'
status: completed
type: task
priority: normal
created_at: 2026-08-30T14:43:39Z
updated_at: 2026-09-06T12:40:20Z
---

Re-running `qbeta_habiro_integrality_kill_test` (one of the `qou-tekx` "merely
stale" 11) **flips three of its six assertions from passed to FAILED**, with
values moving 41–59 orders of magnitude:

    b_matches_N3_witness            1.8111358157653425e-71  -> 2.280110649365846e-12
    QN2_matches_N3_witness         -8.656884150198534e-52   -> 0.00047030329121502756
    c3_matches_N3_witness_additive -6.568668276257924e-44   -> -972.0518295477506

**This is not a pin shift** — 11.5 ppb cannot do that.

**The split is diagnostic.** The three assertions that still PASS are the
self-contained symbolic ones (`b_squared_three_forms_agree_symbolically` 1.0,
`basis_invariance_h_hbar_verified` 1.0,
`bare_alpha4_equals_minus_three_quarters_exact` −0.75). **All three that fail
are the `*_matches_N3_witness` cross-checks.** So the producer's own
mathematics is intact; what has moved is its agreement with an external
reference.

**Mechanism:** those references are **hardcoded constants** in the script —
`N3_WITNESS_B`, `N3_WITNESS_QN2`, `N3_WITNESS_C3` — frozen from the N3 producer
chain as it stood on 2026-07-11, while the script computes that chain live at
the current anchor. Same frozen-companion shape as
`keystone_wrt_schurweyl_plancherel_4count_probe` (bean `qou-tekx`).
`scriptHash` has also moved `bb3c24b120f2` → `a3a021205a8d`, so the script
itself changed since the witness was written.

**The producer is not defective — it is correctly detecting that its frozen
references are stale.** The guard is working.

**The failing witness was NOT committed.** Refreshing the three constants means
running the N3 chain and adopting its current values, which moves numbers and
needs its own diff; do not do it as an idle refresh.

Note the upstream was corrected in `126edfa8929` ("a float64 q_0 in the Habiro
witness — the gate went RED, fixed at the producer"), which is a plausible
proximate cause but is **not** established here as the whole of it, since the
script changed too.


## Independently reproduced 2026-09-06, and a second staleness alongside it

Hit this while draining bucket B of the raw-float64 backlog (`qou-r47m`). A
fresh run of the **unmodified** producer on `main` reproduces all three
failures with the same deltas — `b_matches_N3_witness` 2.28e-12,
`QN2_matches_N3_witness` 0.00047, `c3_matches_N3_witness_additive` 972.0
against tolerances of 1e-25 / 1e-25 / 1e-20 — so this is not container drift
and not the pin.

**Second staleness, not previously recorded here:** the committed witness is
also stale in its raw-float64 count. `raw-float64-baseline.json` carries
**241** for it; a fresh run writes **323**. So the file on `main` is behind its
own producer in two independent dimensions at once.

**Consequence for a precision drain, which is why this bean blocked one.** The
producer's `sigma_exp` / `sigma_anchor` / `dist_to_Z` / `dist_to_ZSqrt3` rows
and its `empirical_c3` block route cleanly through `fmt` — that patch takes it
**241 -> 15** (the residue is the `ASSERTIONS` tuples). But landing the drain
means committing a regenerated witness whose `allPassed` flips **True ->
False**, i.e. burying a substantive assertion regression inside a
serialization commit. Held back deliberately; the drain is ready and should
land *after* this bean, not before, so the flip is reviewed on its own terms.

The honest reading of `main` today: this witness asserts `allPassed: true` for
three cross-checks its own producer fails.


## RESOLVED 2026-09-06 — root cause is an ANCHOR MISMATCH, not stale copies alone

The frozen-constants diagnosis above is right about the mechanism and
incomplete about the cause. Measured from primary sources:

**The N3 witness this probe cross-checks against is PROTON-pinned; the probe
was comparing its MUON chain to it.** `q-beta-operator-valued-N3.witness.json`
moved to the experimental pin under the 2026-08-07 owner directive and this
probe never followed. That is the layer straddle AGENTS.md forbids, sitting
inside a cross-check.

Decisive measurement — the probe's own `chain()` against the committed N3
witness, at 60 dps:

| quantity | at the muon anchor | at the proton anchor |
|---|---|---|
| `b` | 3.44e-10 | **1.6e-61** |
| `QN2` | -2.38e-8 | **-8.7e-52** |
| `c3` | 0.0497 | **-2.3e-43** |

So the probe's chain reproduces that witness *exactly* at proton and misses at
muon by the μ–p separation. The three "failures" were one root cause.

**And the frozen literals were a THIRD anchor.** `b` at the *retired*
self-certified muon pin is `0.86758406730714238696`, matching the frozen
`N3_WITNESS_B` to **5.3e-19** — so the constants were snapshotted from the
chain at a pin that has since been retired twice over. Three vintages of "the
muon q₀" were in play at once, which is exactly the trap
`muon_pin_three_values_probe` exists to name.

**Fix (both halves).** Cross-checks now compare `CH["proton"]`, and the three
reference values are **read from the committed N3 witness at run time** instead
of frozen as literals — a copy cannot track its source, which is what let this
go stale silently.

**No tolerance was widened.** The floors are unchanged at 1e-25 / 1e-25 /
1e-20 and the residuals clear them by 20+ orders of magnitude: 5.43e-71,
8.66e-52, 2.33e-43. All 6 assertions pass.

**The bean's own reading was correct and worth keeping**: *"the producer is not
defective — it is correctly detecting that its frozen references are stale."*
The guard did its job for two months; what was missing was the anchor.

The drain this blocked is landed with it: **241 -> 0** raw-float64 fields.
