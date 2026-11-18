---
# qou-xbh4
title: qbeta_ohtsuki_sixone_kappa_series VOL_6_1 is built at mp.dps=15 — two blocking precision gates red on main
status: in-progress
type: bug
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-21T16:38:15Z
updated_at: 2026-11-18T07:50:47Z
parent: qou-9nnz
---

Found by `/prepare-merge-auto` on PR #5342 (2026-08-21). **Not that branch's
defect** — inherited from `main`, and blocking two gates there right now.

## The offender

`computations/qbeta/qbeta_ohtsuki_sixone_kappa_series.py:166`

    VOL_6_1 = mp.mpf("3.163963228883143983991757529167384812325703962")

46 significant digits, built at **module scope**, while `mp.dps` is still
mpmath's default 15. The literal is parsed and rounded to 53 bits before any
`set_compute_dps()` runs, so the constant is already wrong when it is built —
the digits past ~15 are decoration. Landed by `ae1d692cc6`.

## Two gates, one defect

    import-time dps ratchet    computations/mpf_import_time_dps_audit.py
    module-const precision     computations/module_const_precision_audit.py

Both go red on this single line, which is why they moved together and why the
count looks like two problems. `scripts/precision-gates.sh` therefore **exits 1
on `main`** independently of any branch — verified: the file is present on
`origin/main`, PR #5342 does not touch it, and #5342 touches neither gate's
implementing script.

## Fix

At the producer, per the standing rule — never by widening a baseline. Either
raise the precision before the constant is built, or carry it lazily:

    # option A — raise first
    set_compute_dps()
    VOL_6_1 = mp.mpf("3.163963228883143983991757529167384812325703962")

    # option B — build on demand, so the caller's dps governs
    def vol_6_1(): return mp.mpf("3.16396322888314398399175752916738481232570396")

Option B is preferable if anything imports this module before raising dps.

## Ownership note — why this bean exists

The prepare-merge agent reported both of #5342's inherited offenders as
"already having owners" and filed nothing. Checked, and that is too generous:

- **`qou-6ort`** is the *extraction* arc — getting the 6₁ kappa series out of
  `ki6c.pdf`. It created this file; it is not about this defect.
- **`qou-j6gb`** is the *gate-wiring* bean for `mpf_import_time_dps_audit`, and
  its finding is the 288-item historical backlog. This is a **new arrival on
  top of** that backlog, which is exactly what a ratchet is supposed to
  surface separately — folding it into the backlog bean is how a ratchet's
  signal gets absorbed.

Neither names this line. A defect adjacent to two beans is not a defect that
has an owner.
