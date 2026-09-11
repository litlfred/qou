---
# qou-9q4h
title: 'Three importers are broken on main: unsupported format string passed to mpf.__format__'
status: completed
type: bug
priority: normal
created_at: 2026-09-06T10:08:46Z
updated_at: 2026-09-11T15:18:47Z
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


## 2026-09-11 — CLOSED. All three run; the "default if nobody acts" no longer applies.

Off the `qou-bstl` queue. This bean's closing section reads *"**Default if nobody
acts:** the three stay unrunnable"* — someone acted (`0e2e79981ae`, *"three
producers could not run — mpf has no `__format__` for `.3f`"*).

Verified the only way this bean allows, by **running all three**, which it
correctly flagged as the awkward part (they write witnesses, so the run has to be
reverted — the `qou-v0t8` contended-file hazard):

    computations/mass-from-q-symbolic.py        exit 0
    computations/rho_f_volume_binding_gap.py    exit 0
    computations/codata_reconciliation.py       exit 0

No `TypeError: unsupported format string passed to mpf.__format__`, no traceback,
in any of the three. Tree restored afterwards (`git checkout -- computations` +
`git clean`); **0 files changed**, nothing committed.

The consequence this bean was actually worried about is what lifts: these three
can now be executed to refresh their own witnesses, so those witnesses are no
longer condemned to go staler with no way back.

**qou-9q4h closes.**
