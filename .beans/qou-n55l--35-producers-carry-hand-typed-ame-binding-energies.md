---
# qou-n55l
title: 35 producers carry hand-typed AME binding energies that disagree with the vendored table
status: todo
type: task
created_at: 2026-08-24T13:14:06Z
updated_at: 2026-08-24T13:14:06Z
---

NOT SWEPT. 35 producers, and the numbers MOVE in every witness they write --
this is a data correction, not a representational one. Many sit in other
arcs' territory (the deltalambda cluster especially). Recording the evidence
and the scope; the sweep is a decision.

Found while fixing catalan-binding, which had the same defect and IS fixed
(9a3c2b06c).

THE FOUR WRONG LITERALS, against codata_constants.ame_binding_mev over the
vendored AME2020 table:

    typed        canonical        delta MeV     relative
    2.22452      2.2245662        4.62e-5       2.08e-5     D
    8.48180      8.4817962        3.80e-6       4.48e-7     T
    7.71804      7.71804132       1.32e-6       1.71e-7     3He
    28.29567     28.2956624       7.60e-6       2.69e-7     4He

and in catalan-binding, already fixed, the worst single one:

    32.0         31.9939872       6.013e-3      1.88e-4     6Li

EXTENT
  40 files carry at least one of the four literals.
  35 of those use them in unambiguous AME context -- the literal is on a line
     mentioning AME / binding / deuteron / tritium, or within two lines of
     one. Examples that leave no doubt:
       deltalambda/deuteron_trefoil_qinvariant_closed_form_probe.py:48
           B_D = mp.mpf("2.22452")              # MeV, AME2020 deuteron binding
       deltalambda/deltalambda_extensivity_gap_synthesis_probe.py:45
           B_AME = {'D': 2.22452, 'T': 8.48180, '3He': 7.71804, '4He': 28.29567}
       deltalambda/deltalambda_binding_cross_isotope_probe.py:63
           B_AME_MEV = {"d": "2.22452", "t": "8.48180", ...}
  5 remain ambiguous (no AME word nearby) and would need reading before
     being touched: mass_at_3A_proper.py, phase5/phase3_triton_binding_
     convention_b.py, probes/b4_value_cumulant_target_probe.py,
     sweeps/light_isotope_sweep.py, unified_lift.py.

WHY THIS IS THE DOCUMENTED FAILURE MODE, NOT A NEW ONE
`codata_constants.ame_binding_mev`'s docstring says it exists because
"consumers working over a *table* of nuclides (mass sweeps, binding ladders)
need the same source for arbitrary (Z, A), and without a public entry point
they hand-type the rest -- which is exactly how `mass_table_ppb.py` ended up
with eleven typed literals sitting up to 1.6e-5 away from this table". That
accessor exists. 35 producers still hand-type.

NOTE the literals are not all float64 -- several are `mp.mpf("2.22452")`,
i.e. carried at full precision. Full precision of the WRONG NUMBER. This is a
correctness issue that the float64 audits cannot see, and it would survive
any amount of precision work.

SUGGESTED SHAPE
  1. Decide whether 2e-5 relative on D matters for each consumer. For probes
     quoting "targets -B_AME/m_e" to 5 decimals it may not; for anything
     computing a ppb-level residual it certainly does.
  2. If sweeping: replace with ame_binding_mev(Z, A), re-run each producer,
     diff each witness, and expect err_pct-style outputs to move (catalan's
     6Li err_pct moved 0.0123 points).
  3. Read the 5 ambiguous files before touching them.
