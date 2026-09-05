---
# qou-92u9
title: The chi caches are 26 days stale to the intra-ordering change, and it refutes the O3' atom-independence result
status: todo
type: task
created_at: 2026-09-05T19:25:18Z
updated_at: 2026-09-05T19:25:18Z
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
**Import-cone staleness**: the producer's own source is byte-stable, so a
file-local `git diff` cannot see it.

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
