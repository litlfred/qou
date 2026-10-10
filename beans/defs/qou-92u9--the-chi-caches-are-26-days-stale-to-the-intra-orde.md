---
# qou-92u9
title: The chi caches are 26 days stale to the intra-ordering change, and it refutes the O3' atom-independence result
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-05T19:25:18Z
updated_at: 2026-10-04T15:24:53Z
---


## The fact

The six `chi-<atom>-h<n>-at-q0-50dps.witness.json` caches were computed
**2026-08-10**.  `atom_braid_word_3A`'s intra-nucleon ordering changed
**2026-09-05** (bean `qou-hu1f`, owner ruling, commits `7db032fb48` /
`deb9ff5728`): each nucleon's confinement core is now ALTERNATING
(`intra_order="borromean"`, the default) where it was GROUPED.

Their producer is `chi_at_q0_via_hoefsmit_mpfr.py`, which calls
`atom_braid_word_3A(Z, N)` at **line 96 with no `intra_order`** — so a fresh run
today produces the borromean word and the committed caches do not.
**🛑 CORRECTED — I first wrote "import-cone staleness: the producer's own source
is byte-stable".  It is not.**  `chi_at_q0_via_hoefsmit_mpfr.py` changed **three
times** after the caches were built — `52c68267f2` (2026-08-15), `41f517bf17`
(2026-08-23) and `d151898dd6` (2026-08-30, *"fix(L1): pin-specific numerical chi
caches — 5/6 atoms certified 1 ppQ"*), the last a fix **about these caches** that
did not regenerate them.  So this is **both** self-staleness and import-cone
staleness.

**🛑 AND MY EXPLANATION FOR WHY NEITHER WAS DETECTED WAS ALSO WRONG — corrected
the same session.**  I wrote that the caches carry `scriptFile: None` with a
`scriptHash` matching no file, so *"no checker knows what to hash"*, and proposed
emitting `scriptFile` as a cheap independent fix.

The observations were right; the inference was not.  `save_witness` writes a
**`producer`** field, and every stale cache carried
`producer: chi_at_q0_via_hoefsmit_mpfr.py` — resolvable — beside
`scriptHash c36a8a393fcd` against the producer's then-current `815a026e9591`.
**The drift was plainly visible to ordinary detection keyed on the field these
tools use.**  It was not undetectable; it was *undetected* — nothing ran the
check, which is what the dispatch-only workflow posture predicts.

So the proposed `scriptFile` fix is **unnecessary** — the provenance already
exists under another key.  Proposing it repeated the byte-stable error: reasoning
from one field's absence without checking whether a sibling carried the same
information.

**And my "3,610 scanned, none flagged" reading was wrong too.**  That audit's own
header says `SELF-stale (already caught): 597  (excluded below)` — it EXCLUDES
self-stale witnesses by design, deferring to the validator that covers them.
Their absence from its report is the exclusion working, not blindness.  Third
wrong inference from the same habit: reading an absence as evidence.

**What survives:** two classes, and only the second needs new tooling.  SELF-
staleness (the producer's three edits) is detectable today and was simply not
checked.  IMPORT-CONE staleness (the callee changing on 2026-09-05) is invisible
to `scriptHash` by construction, because the producer is byte-identical across
that change — that half is real.

Measured (`chi_caches_predate_the_intra_ordering_change_probe.py`, 4/4):

    committed cache vs GROUPED     3.13e-50 (tritium), 2.64e-50 (helium-3)
    committed cache vs BORROMEAN   1.318             , 1.215        RELATIVE

Not a drift — a different number.

## It is NOT a per-atom rescale, so `qou-hu1f`'s R_quark does not cover it

`|chi_borromean / chi_grouped|` spans **12.04x** (tritium) and **11.29x**
(helium-3) across the two-row partitions, and **`[8,1]` and `[5,4]` CHANGE SIGN**
in both.  `qou-hu1f` measured the ordering change's blast radius carefully and
split it — log-ratio routes provably immune, difference routes scaling by one
per-atom factor `R_quark` (3.785x–14.325x) — but **it does not mention these
caches or `chi_at_q0_via_hoefsmit_mpfr` at all** (grepped: 0 hits).  A single
scalar per atom cannot describe a surface with sign flips in it.

## 🛑 It refutes a published result

`argmin(t) == argmin(w)` — the O3' selection's atom-independence, measured 6/6
and merged in **#6841** and **#6847** — holds under grouped and **fails** under
borromean:

    tritium    grouped    argmin(t) = [5,4] = argmin(w)          AGREE
    tritium    borromean  argmin(t) = [7,2], argmin(w) = [5,4]   DIFFER

`o3prime_selection_is_atom_independent_probe.py` states its own falsifier as
*"a single row where argmin(t) != argmin(w) would refute it"*.  Tritium under
the live ordering **is** that row.  The dim-vs-`|chi|` concordance moves the
same way: 9/10 and 10/10 → **6/10 and 6/10**.

That probe now opens with a scoping banner saying every figure in it is
GROUPED-CONDITIONAL.  Nothing was deleted — the measurements are correct for the
grouped ordering, and the structural findings (w is a monotone reparametrisation
of the content sum; the selection margin is thin; the mirror flip acts
per-partition) are about method and shape, which transfer.  The headline does
not.

## Blast radius

**84 live (non-deprecated) scripts** read these caches, `aK_via_lp_dual_full.py`
among them, and through it `a-K-via-lp-dual-full.witness.json` and everything
computed from it.

## The decision, which is the OWNER'S and is deliberately not taken here

Regenerate the caches, or not.  Cost: 84 consumers move, plus a **22.5-minute**
helium-4 recompute (`compute_time_sec` 1352.39 in its own witness; A≤3 is under
a second each).  This is the same boundary `qou-hu1f` reached on the same day,
in its own words: a change of this size *"needs an owner ruling, not a probe"*.

The probe establishes the fix is NEEDED and measures what it would move.  It
does not make it, and it writes nothing — `incremental=False` returns without
touching disk, which matters because the incremental path persists each
partition as it goes and would overwrite the very caches being measured.

## What to check next if it is regenerated

Whether the O3' arc's structural findings survive re-measurement, in this order:
the content-sum monotonicity of `w` (predicted untouched — `w` does not depend
on the word at all), then the anti-correlation, then the margin.  `w`-side facts
are predicted safe; every `chi`-side fact is open.


## Both options measured (2026-09-05) — all six atoms

| finding | GROUPED (committed) | BORROMEAN (live) | |
|---|---|---|---|
| `argmin(t) == argmin(w)` | 6/6 rows | **4/6 rows** | moves |
| `w` monotone in content sum | 49/49 | 49/49 | **invariant** |
| `conc(w,|chi|) == conc(c,|chi|)` | 6/6 rows | 6/6 rows | **invariant** |
| anti-correlation `conc(w,|chi|)` | 9/49 | **25/49** | **changes sign** |
| `dim`~`|chi|` concordance | 43/48 | **21/48** | moves |
| worst selection margin | 2.108x | **10.069x** | moves |
| flattened on every row | True | **False** | moves |

The `w`/`chi` split was **predicted before measurement** and holds exactly: `w`
is a function of the partition and `q` alone (verified identical to `<1e-45`).

**Two rows flip, and where they land was also predicted.**  Tritium `[5,4]` ->
`[7,2]` and helium-4 `[6,6]` -> `[7,5]` — exactly two of the three partitions
already flagged as carrying a `dim`-vs-`|chi|` inversion under grouped.  The O3'
probe had written *"a discordant partition that also happened to be the
runner-up is what a flip would look like"* before this measurement existed.
Deuteron's `[4,2]`, the third, does not flip.

**COST, corrected.**  A≤3: under **three seconds** for all five, both orderings.
Helium-4: **423 s** (~7 min) on the non-incremental path.  A full six-atom
regeneration is **about seven minutes**, not the 22.5 implied by helium-4's own
`compute_time_sec` 1352.39 — that figure is the INCREMENTAL path.

**INVISIBILITY, measured not inferred.**
`witness_import_cone_staleness_audit.py` — the detector built for exactly this —
scanned **3,610 witnesses and flagged none of the six**.

**A third action, independent of the regenerate/leave choice:** make the producer
emit `scriptFile`.  That single missing field is what defeats both staleness
classes; with it, ordinary `scriptHash` drift catches the next producer edit
automatically.  Cheap, uncontroversial, and it converts prose into a gate.


## OUTCOME: regenerated (owner ruling "regen", 2026-09-05)

Rebuilt with `--fresh` on the canonical producer path.

**`--fresh` was load-bearing.** The resume check compares stored-vs-current
`q_0`, and `q_0` did not change — only the ordering did. Without it the run
would have resumed, kept every stale partition, and stamped the result current.

**The stale set was EIGHT, not six.**  `chi-diproton-h6` and `chi-dineutron-h6`
(both built 2026-08-16, same `scriptHash c36a8a393fcd`) were invisible because
they are not in `aK_via_lp_dual_full.py`'s `ATOM_CHI` — the *consumer* list I had
been reasoning from.  They are in the *producer's* `ATOMS` map.  Both regenerated.

Generalises: enumerating a producer's outputs from one consumer's list
undercounts by whatever that consumer does not use.  Index on the `producer`
field instead — it finds all eleven witnesses this producer has written.


## Downstream sweep: measured, scoped, NOT executed (2026-09-05)

**75 committed witnesses** are produced by scripts that read a chi cache and were
computed before the regeneration.  Triaged on the axis that decides the work:

    carry an ABSOLUTE-looking field (tr_M / mass / binding / energy)   64
    ratio-only                                                        11   predicted immune

**The propagation rule, measured on `a-K-via-lp-dual-full` (before/after in
git):**

    atom       tr_M before -> after        factor      qou-hu1f R_quark
    proton     1.145760 -> 0.629328        1.8206      (not listed)
    neutron    0.987744 -> 0.475134        2.0789      (not listed)
    deuteron   0.575172 -> 0.151968        3.7848      3.785
    tritium    0.229310 -> 0.029144        7.8682      7.868
    helium-3   0.403767 -> 0.058596        6.8907      6.891
    helium-4   0.160974 -> 0.011237       14.3248     14.325

    a_K^C (the quantity that producer exists to report):  ZERO change, all six.

So `qou-hu1f`'s split is confirmed on a producer that bean never examined:
**ratio routes are immune; the aggregate trace scales by R_quark exactly.**

**🛑 BUT THE RULE DOES NOT EXTEND TO PER-PARTITION QUANTITIES, and I nearly said
it did.**  Re-running `delta_lambda_2row_stratum_analysis.py` (24 ms) moved 181
numeric fields by factors spanning **11.8x to 51.2x within one witness** — and
51.24 is exactly the helium-4 `|chi_borromean/chi_grouped|` spread.  Per-partition
characters move by per-partition factors, including sign changes.  **Only the
aggregate `tr_M` is closed-form**; anything reporting per-lambda values must be
re-run, not rescaled.

**🛑 CORRECTED — "several are long computes" was inferred, not measured, and it
is false.**  Every one of the 67 stale witnesses with a recorded `durationMs`
runs in **under 60 seconds**; 63 of them in under one second, and the slowest in
the whole set is `delta_lambda_empirical_tabulation` at **36.1 s**.  The full
sweep is a couple of minutes of compute, not the multi-hour job I implied when I
scoped it as a follow-up.  I read "84 consumers" as "expensive" without opening
the durations.  The sweep was therefore RUN, not deferred — see below.

**Also stale and NOT regenerated: the muon-anchor chi caches**
(`chi-{tritium,helium-3,helium-4}-h9/h12-at-q0-50dps-muon.witness.json`).  I ran
the producer at its default (proton) anchor only.  Those belong to the ideal
CAL-2 layer and are a separate anchor decision.


## Sweep outcome (2026-09-05) — run, triaged, and it found a defect CLASS

64 downstream producers run: **53 exit 0, 8 exit 1, 3 timed out**; 50 witnesses
refreshed.  Four of the eleven non-zero exits are correct behaviour and two
predate this work, so it is not a defect list.

**The three timeouts were budget artifacts, confirmed.**  Re-run with a real
budget: `chi_4he_binding_lossless` **665 s** exit 0, `chi_4he_via_rust_lossless`
**586 s** exit 0, both writing clean witnesses.  My 180 s ceiling was simply
below their cost.  The third is still running.

**🛑 THE EXACT-ZERO RADICAL PROXY WAS IN THREE PROBES — and the corpus already
had a correct implementation none of them used.**

    computations/live_channels.py:103   is_live(y_lambda, tol=DEAD_TOL)
                                        DEAD_TOL = 1e-30

Forty orders clear of the 1e-73 residual, and its docstring settles the
definition: *"Defined by the weight, not by the row count."*  Its own
`!= 0` is only the fallback for objects `float()` refuses.

  * `o3prime_selection_is_atom_independent_probe` — mine; sent `tau_tail` into
    a 77! enumeration (a process I later found had been burning CPU for 3h17m).
  * `ak_lp_dual_quotient_probe` — reported `degen` on every atom, which READS
    as "O3' is degenerate" and actually meant the line had stopped separating
    two populations.  I nearly reported it as a finding.
  * `o3prime_quotient_lp_solve_probe` — the #6752 probe itself.

All three now on the library.  Also fixed in `ak_lp_dual_quotient_probe`: a
`max(abs(r["_ppm"]))` with no None guard, while the line two above it and the
serialization line both guard for exactly that case.

**THE POSITIVE RESULT, by two independent routes.**  With the proxy fixed,
`o3prime_quotient_lp_solve_probe` is **5/5 against the regenerated data**, and
`ak_lp_dual_quotient_probe` gives `y0*_quot` nonzero on all six atoms where the
ambient is 0 (0.0694 / 0.0920 / 0.0108 / 0.00315 / 0.00619 / 0.000296).  So
**O3''s pricing of the net constraint — the defect #6752 was chosen to repair —
SURVIVES the ordering change.**  The selection claims built on top of it did
not; the pricing repair did.  All four of `ak_lp_dual_quotient`'s assertions are
invariant across the regeneration.

**Recorded on `qou-hu1f` instead of here**, being that ruling's consequence: the
alternating word is non-monotone for EVERY atom where the grouped word was
monotone for every atom, so `reduced_block_kernel.chi_all_lambda_reduced_block`
refuses it outright.  That is the executable form of the "each generator's
letters must be contiguous" fact that bean already carries.


## Final: the three timeouts resolved — 2 were budget artifacts, 1 is genuinely long

    chi_4he_binding_lossless          665 s   exit 0   clean witness
    chi_4he_via_rust_lossless         586 s   exit 0   clean witness
    qbeta_interface_w_deciding_test  2400 s   exit 124 TIMED OUT AGAIN

**🛑 I called this "a third confirmation that those three were budget artifacts"
while it was still running.  It was not.**  Two were; this one needs **more than
40 minutes** and remains unrun.  It reached section 3 of 3 ("THE DECIDING TEST")
and was killed mid-table, so it is working, not broken — but it is not cheap
either, and my 180 s ceiling was never the binding constraint for it.

It wrote **nothing**: its witness still carries `computedAt 2026-09-03T06:32:21`
from commit `2e68bb647d` (*"qou-bmz8: the interface route is CLOSED — the
deciding test is negative"*).  So that witness is the one remaining piece of the
chi-cache downstream that this regeneration has **not** refreshed.

**What that means for `qou-bmz8`.**  Its negative verdict was computed on the
pre-regeneration caches.  Whether "the interface route is closed" survives the
new ordering is **untested** — and the O3′ arc is a live demonstration that a
verdict of that shape can invert.  Not asserted either way here; flagged so it
is not read as confirmed.

Re-running it needs a budget well past 40 minutes and is the last open item on
this bean.

## 2026-09-14 — the `scriptFile` conclusion above was right about the FIELD and wrong about the READER

This bean corrected itself once already, concluding the proposed `scriptFile`
fix was **"unnecessary — the provenance already exists under another key"**,
because `save_witness` writes `producer` and every stale cache carried
`producer: chi_at_q0_via_hoefsmit_mpfr.py`.

That is true of the information and false of the tooling.
`witness_import_cone_staleness_audit.py` — the audit whose whole job is the
direction self- and upstream-staleness miss — read

    script_file = w.get("scriptFile")
    if not script_file:
        continue

and `continue`d **silently, into no bucket**, so its four summary counts did not
add up to `witnesses scanned` and nothing said why. Measured today:

    witnesses with no scriptFile              399
      ...of which DO carry producer            42   <- recoverable, dropped
      ...of which carry neither               357

**The six caches this bean is about are among the 42.** So the audit that would
have flagged them could not see them — not because the provenance was missing,
but because the reader looked under one key. "The information exists" and "the
checker reads it" are different claims, and this bean asserted the first as
though it settled the second.

**Fixed.** The audit now falls back to `producer` (taking `Path(...).name`,
since `producer` is sometimes a path where the index is keyed by basename) and
COUNTS what it still cannot resolve. Re-run, the summary is honest:

    no scriptFile, used producer : 42   <- were silently dropped before 2026-09-14
    no producer field at all     : 357  <- still invisible; nothing names their producer

Downstream, `SELF-stale` moved 613 -> 632 and `no usable computedAt` 73 -> 96:
the recovered 42 now get processed and land in existing buckets rather than
vanishing. Most are self-stale, i.e. already covered by the validator this audit
defers to — which is the outcome this bean predicted, now actually demonstrated
instead of assumed.

**Still open here:** the 357 with neither key. Nothing in those files names a
producer, so no cone can be walked for them at all. That is a genuine remaining
blind spot and it is now reported as one instead of being invisible.



## Summary of Changes

Closed 2026-10-04 in the work-plan reorganisation: the work has landed on main. Evidence: [M] main 5f106338e5 2026-09-06: 'close(qou-92u9): the third timeout is genuinely long, not a budget artifact — and I said otherwise while it was still ru'; bean not touched after
