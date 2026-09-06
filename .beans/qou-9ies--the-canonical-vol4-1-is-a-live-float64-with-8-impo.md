---
# qou-9ies
title: The canonical Vol(4_1) is a live float64 with 8 importers, and a 2026-06 audit called it a comment
status: todo
type: task
priority: normal
created_at: 2026-09-06T07:17:23Z
updated_at: 2026-09-06T07:18:12Z
---

Found while hand-reading the 13 witness-copy findings whose source is a RETIRED
`_deprecated/` witness (bean `qou-psjm`). Four of those 13 are `Vol(4_1)` at 31
digits, which looked like the easy drain -- "just import the canonical constant".
Measuring the canonical first is what turned that around.

## NOT mine -- credit where it belongs

`qou-f8lit` (todo, high) already owns the `Vol(4_1)` truncation arc: the Lean
sites, the `...0115970029` WRONG-TAIL variant across six `computations/` sites
plus a witness, and the refutation of
`docs/audits/2026-06-21-constant-consistency-axis2-clean.md`. I re-derived its
figures independently and they hold:

    exact  2*Cl2(pi/3)   2.02988321281930725004240510854904
    Lean carrier         ...25001159780499     rel 1.52e-20   (f8lit: "wrong from sig fig 21")
    the 31-digit Python  ...25004240510854     rel 2.00e-32   CORRECT

## What IS new: a different defect on the same constant

f8lit QUOTES the June audit's sentence -- the value *"survives only as a comment
in `experimental_constants.py`, wrong-tail variants only in `_deprecated/`"* --
and refutes it on the ground that the value was live in executable **Lean**. It
never tests the `experimental_constants.py` clause itself.

That clause is ALSO false, and this is the second, independent falsification of
one audit sentence:

    computations/substrate/experimental_constants.py:199
    VOL_FIGURE_EIGHT     = 2.029883212819307   # +/- 1e-12 (numerical precision)
    VOL_FIGURE_EIGHT_ERR = 1e-12

AST-verified: a LIVE `ast.Assign`, value a Python **float**. Not a comment.

**8 real importers** (an import statement, not a mere mention):

    tools/qou-substrate/python/qou_substrate/__init__.py   <- the package's public API
    tools/qou-substrate/tests/test_smoke.py
    computations/mass-from-q-symbolic.py
    computations/tau-lepton-nf.py
    computations/rho_f_volume_binding_gap.py
    computations/codata_reconciliation.py
    computations/knot-particle-generation.py
    computations/probe_topological_mass_formula.py

This is a DIFFERENT defect from f8lit's. f8lit's variant is WRONG-TAILED (wrong
from digit 21). This one is CORRECT as far as it goes -- a 16-digit truncation at
float64 epsilon -- and its problem is that it is a `float` and it is the canonical
IMPORT TARGET.

## Size it honestly: not a breach, and not nothing

    rel error vs exact          1.48823e-16
    as a fraction of L1 budget  0.149x     (L1 = 1 ppQ = 1e-15 relative)

Propagated through `mass-from-q-symbolic.py`'s `mu_e_from_vol = VOL_FIGURE_EIGHT
/ HBAR_Q_SQ0`:

    m_mu/m_e from float64 Vol  206.76832637067385952
    m_mu/m_e from exact  Vol   206.76832637067389029
    difference                 1.49e-7 ppb

Against an m_mu residual of 211 ppb that is negligible, and I am NOT claiming it
moves any headline number. What it does is spend **15% of the entire L1
compute-precision budget on a single constant**, and inject a Python `float` into
mpmath chains -- the "f64-into-mpmath" class the precision gates already carry as
advisory.

## The framing defect underneath

`Vol(4_1) = 2*Cl2(pi/3)` is an EXACT closed form, computable to any precision.
`experimental_constants.py` files it under "Knot volumes (SnapPy 3.3.2)" with a
declared `VOL_FIGURE_EIGHT_ERR = 1e-12`, i.e. as a NUMERICAL MEASUREMENT with an
uncertainty. That is a category error, and it is why the constant was never
exactified: nobody re-measures a measurement.

## The fix, and why the obvious one is backwards

Do NOT "drain" the four 31-digit sites by importing the canonical -- that is a
**7.4e15x precision DOWNGRADE** and converts an exact constant into a float64.
The arrow points the other way:

  1. Make the canonical exact -- `2 * mp.clsin(2, mp.pi/3)` at ambient dps -- and
     retire `VOL_FIGURE_EIGHT_ERR`, which describes a SnapPy run, not this number.
  2. Check each of the 8 importers still behaves (several do float arithmetic
     with it; an mpf may change a dtype).
  3. THEN the 31-digit literals become cross-checks against the canonical rather
     than the more precise source, and two of the four
     (`kashaev_peak_value_probe.py:170`, `qbeta_aomega_stokes3_tracefield_probe.py:102`)
     already ARE cross-checks against a freshly computed value and are correct as
     written.

## Default if nobody acts

Nothing breaks. The constant stays correct to float64 epsilon, the four 31-digit
sites stay in the witness-copy baseline, and the L1 budget keeps paying 15% for
a constant that could be free. The audit sentence stays wrong in the record.

## Blast radius

`qou_substrate/__init__.py` exports it, so any external reader of that package
gets the float. In-repo, `mass-from-q-symbolic.py` feeds the muon-ratio
cross-check and `probe_topological_mass_formula.py` the topological mass formula
-- both quantities a reader sees.
