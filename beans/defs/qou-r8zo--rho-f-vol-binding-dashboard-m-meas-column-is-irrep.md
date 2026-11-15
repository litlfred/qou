---
# qou-r8zo
title: 'rho_f_vol_binding_dashboard M_meas column is irreproducible: +-240 eV from every standard route'
status: completed
type: bug
priority: normal
created_at: 2026-08-21T22:02:08Z
updated_at: 2026-08-22T09:53:41Z
---


## What

`computations/probes/rho_f_vol_binding_dashboard.py:32-35` carries an
`M_meas MeV` column — the *measured* nuclear masses the framework's
predictions are scored against. Those four values cannot be reproduced from
any standard route.

Found during the CODATA drain (`qou-7ot6-a`, PR #5423), where they first
looked like a stale CODATA edition. They are not: an edition shift is ~1 ppb
and consistent in sign across nuclides. These are neither.

## Measured

Reference values read from `library/allascii.txt` via `qou_substrate.codata`
(CODATA-2022); AME-2020 atomic masses in u; `B` taken from each row's own
`B_AME` field.

| nuclide | in file | vs `Z·m_p + N·m_n − B` | vs `atomic·u − Z·m_e` |
|---|---|---|---|
| ²H | `1875.612790` | **−155.4 eV** | −141.4 eV |
| ³H | `2808.921136` | +23.7 eV | +12.9 eV |
| ³He | `2808.391611` | +68.2 eV | +78.8 eV |
| ⁴He | `3727.379109` | **−240.7 eV** | −223.9 eV |

Residuals scatter in **both directions** with no common factor, so this is not
a unit slip, not an electron-binding convention, and not a vintage. CODATA
uncertainties on these masses are ~1 eV, so the discrepancies are 100–240 σ.

Note ³He: the drain's earlier scan flagged it at **−0.04 ppb** — essentially
exact — while ²H and ⁴He in the *same table* are 80 ppb out. A single wrong
source would not do that.

## Also affected

`computations/b_over_m_order_probe.py:47-49` shows the same signature:
deuteron and alpha ~−9 ppb, helion −1.47 ppb. Different magnitude, same
"internally inconsistent" shape.

## Why it was NOT fixed

The correct measured values are known — the table above computes them — but
what the column was *meant* to be is not. Replacing four numbers whose
provenance I cannot establish would substitute my guess for the author's
intent in a probe's reference data. The drain's rule is to route consumers at
the registry; that does not license inventing values.

## Impact, so this is neither over- nor under-sold

The dashboard scores framework predictions whose own accuracy at these
nuclides is ~1e-6 relative (~1000 ppb). A reference error of 240 eV on
3727 MeV is 65 ppb — roughly 15× smaller than the discrepancy being measured.
So it **degrades** the dashboard's precision without inverting any verdict it
reports. Worth fixing; not urgent.

## Next step

Someone with the probe's history should say what the column was sourced from.
If the answer is "it should just be the CODATA/AME measured masses", the fix
is registry reads — `M_DEUTERON_MEV_VALIDATION`, `M_HE3_MEV_VALIDATION`,
`M_HE4_MEV_VALIDATION` all now exist and are audited (12/12 in
`codata_table_vintage_audit`); only tritium would need adding.

## RESOLVED 2026-08-22 — and my own verdict in this bean was wrong

I filed this as "irreproducible from every standard route" and left the
values alone. **I never checked the obvious source.** NIST publishes the
nuclear masses directly (deuteron / triton / helion / alpha):

    iso   was            NIST                  error
    2H    1875.612790    1875.61294500     -155.0 eV   (267 sigma)
    3H    2808.921136    2808.92113668       -0.7 eV     (1 sigma)
    3He   2808.391611    2808.39161112       -0.1 eV     (0 sigma)
    4He   3727.379109    3727.3794118      -302.8 eV   (252 sigma)

Two rows landing at 1 and 0 sigma is what IDENTIFIES the intended source.
The two routes this bean tested -- `Z*m_p + N*m_n - B` and
`atomic*u - Z*m_e` -- miss those same two rows by 13 and 78 eV, so
"no route reproduces the column" was a statement about the routes I
happened to try, not about the column. 2H and 4He are simply wrong, by
-82.6 and -81.2 ppb; the shared relative offset says one bad conversion
rather than two typos, but I did not identify what produced it.

Fixed on PR #5439 (`5e79118289`): all four now READ from the table, so
the question cannot recur. Also converted the probe to mpmath end-to-end
(a probe is not exempt from NO-FLOAT64), and marked M_P/M_N `noqa: P31`
-- they are the canonical Hecke energies, not CODATA, and draining them
would be the opposite of correct.

Lesson for the next agent: before writing "irreproducible", enumerate
the sources the corpus actually has a reader for. `codata_table.codata()`
covers 293 NIST quantities including every light nuclear mass.
