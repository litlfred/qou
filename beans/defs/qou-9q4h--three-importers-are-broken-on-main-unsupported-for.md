---
# qou-9q4h
title: 'Three importers are broken on main: unsupported format string passed to mpf.__format__'
status: in-progress
type: bug
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-06T10:08:46Z
updated_at: 2026-11-16T19:29:47Z
parent: qou-trd0
---

Found while verifying the `qou-9ies` Vol(4_1) exactification by running all 8
importers of `experimental_constants.VOL_FIGURE_EIGHT`. Three failed — and my
first reading was that my change had broken them. It had not.

## Pre-existing, not mine — baselined both ways

Same three files, same line, same exception, with the ORIGINAL float64 constant
and with the exact one:

    computations/mass-from-q-symbolic.py:356
    computations/rho_f_volume_binding_gap.py:180   (inside a genexpr)
    computations/codata_reconciliation.py:295

    TypeError: unsupported format string passed to mpf.__format__

The other three importers (tau-lepton-nf, knot-particle-generation,
probe_topological_mass_formula) exit 0 in both states.

## The defect

An f-string applies a float format spec to an `mpf`:

    f"≈ {borromean_mass_MeV:.3f} MeV ± {borromean_mass_MeV_err:.3f}"

`mpmath.mpf` does not implement `__format__` for `.3f`. The scripts run to
completion and then die at the PRINT, so the computation is fine and only the
display is broken.

## Why it matters more than a display nit

These are producers. `mass-from-q-symbolic.py` carries the muon-ratio
cross-check and the Borromean nucleon mass scale; `codata_reconciliation.py` is
a reconciliation report. A producer that dies before writing its output is a
producer nobody can run, which is the same class as `qou-mnrd` / `qou-82ur`
(dirty witnesses reaching main because the gate that would catch them cannot
run) — the failure is silent to anyone who does not execute the file.

## The fix, and why it is NOT taken here

One line each. AGENTS.md is explicit on the form: `float(x)` is permitted ONLY
inside an f-string for display, and `mp.nstr` is preferred. So:

    f"{mp.nstr(borromean_mass_MeV, 6)} MeV"        preferred
    f"{float(borromean_mass_MeV):.3f} MeV"          permitted

Not taken in the Vol(4_1) PR because (a) it is a display defect unrelated to the
audit gates that PR is about, and (b) verifying the fix means RUNNING producers
that write witnesses, which then have to be reverted — the contended-file hazard
of qou-v0t8. Worth doing as its own small change where the witness churn can be
managed deliberately.

## Default if nobody acts

The three stay unrunnable. Nothing regresses; they simply cannot be executed to
refresh their own witnesses, so those witnesses can only go staler.

## Progress Update (Round 49 — PR #8170)

- Fixed the remaining `TypeError: unsupported format string passed to mpf.__format__` crash on line 334 of `computations/codata_reconciliation.py` (`float(max_dev):.3f`) and lifted `ppb()`, `codata_uncertainty_ppb()`, and all witness rows/assertions to `mpmath.mpf` serialized via `_precision.fmt` (`0` raw float64 fields in `computations/codata-reconciliation.witness.json`).
- Verified `computations/mass-from-q-symbolic.py`, `computations/rho_f_volume_binding_gap.py`, and `computations/codata_reconciliation.py` all run cleanly and exit `0`.
- PR: https://github.com/litlfred/qou/pull/8170 (`8b83507c7e14547848b5b991bdd3396fc7f3a703`)
