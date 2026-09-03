# chain_bond_arrangement_dependence_probe — full output (2026-08-31)

Verbatim run of `computations/chain_bond_arrangement_dependence_probe.py`. Regenerate with:

    python3 -u computations/chain_bond_arrangement_dependence_probe.py

```
chain_bond_arrangement_dependence_probe
==============================================================================
q0 (proton pin)  = 1.1099785827513808076
z  = markov_z(q) = 0.6126880371464652516
h  = hecke_h(q)  = 0.20906029879563931543
delta            = 0.0013757108070270960086

STEP 1 — the hypothesis of ChainBondOrderDependence.not_orderIndependent_of_ne
  L_pp = z                  = 0.6126880371464652516
  L_pn = z - h(1/2 - d/4)   = 0.50822978937673896258
  L_nn = z - h              = 0.40362773835082593616
  L_pp - L_nn = h           = 0.20906029879563931543
  L_pp - L_pn               = 0.10445824776972628902
  L_pn - L_nn               = 0.10460205102591302641
  hypothesis  L_pp != L_nn                : True
  all three pairwise distinct             : True
  => the theorem's antecedent HOLDS at the live pin, so its conclusion
     applies to this producer: the chain product is arrangement-dependent
     at every A >= 3.  What follows measures by how much.

STEP 2 — the spread over arrangements, and where the producer sits
  'canonical' = the ordering closed_form_ratio hardcodes, ['p']*Z+['n']*N
 nucleus   Z   N   #ord  #bondsets              min              max      max/min  canon rank
      3H   1   2      3          2     0.2051356404     0.2582975188    1.2591548         1/2
     3He   2   1      3          2     0.2582975188     0.3113863121    1.2055335         2/2
     4He   2   2      6          4     0.1042560433     0.1582557998    1.5179532         2/4
     6Li   3   3     20          7     0.0257822992    0.04087708043    1.5854707         3/7
     7Li   3   4     35          8    0.01040645111    0.01723299267    1.6559913         3/8
     9Be   4   5    126         11   0.002573493369   0.004451239247    1.7296486        4/11
     12C   6   6    924         16   0.000389926597  0.0007044344271    1.8065821        6/16
     14N   7   7   3432         19   9.642802342e-5  0.0001819536647    1.8869376        6/19

STEP 3 — the canonical arrangement against the extremes
  rel = (v_canon - v) / v_canon,  i.e. how far the reported number would
  move if a different arrangement of the SAME (Z, N) were chosen.
 nucleus          canonical      vs min      vs max   canon bonds   argmin bonds   argmax bonds
      3H     0.205135640449         0.0   -0.259155     (0, 1, 1)      (0, 1, 1)      (0, 2, 0)
     3He     0.311386312073    0.170492         0.0     (1, 1, 0)      (0, 2, 0)      (1, 1, 0)
     4He     0.125684152895    0.170492   -0.259155     (1, 1, 1)      (0, 2, 1)      (1, 2, 0)
     6Li    0.0310814254087    0.170492   -0.315161     (2, 1, 2)      (1, 2, 2)      (1, 4, 0)
     7Li    0.0125453254424    0.170492   -0.373658     (2, 1, 3)      (1, 2, 3)      (0, 6, 0)
     9Be   0.00310243247048    0.170492   -0.434758     (3, 1, 4)      (2, 2, 4)      (0, 8, 0)
     12C  0.000470069575457    0.170492   -0.498575     (5, 1, 5)      (4, 2, 5)     (1, 10, 0)
     14N  0.000116247212635    0.170492    -0.56523     (6, 1, 6)      (5, 2, 6)     (1, 12, 0)

  The 'vs min' column is constant, and the argmin column says why:
  canonical is (n_pp, 1, n_nn) and argmin is (n_pp - 1, 2, n_nn) -- exactly
  one pp -> pn swap, so everything else cancels and the ratio is
      1 - L_pn/L_pp  =  h(1/2 - d/4) / z,
  independent of A, Z and N.  Checked, not asserted:
      predicted  h(1/2-d/4)/z = 0.17049173712649978482
      observed   1 - vmin/vcanon = 0.17049173712649978482
      agree to 1e-40 on all 7 nuclei with n_pp >= 1: True

STEP 4 — why the canonical ordering is always an EXTREME, not a middle
  The chain product depends on the arrangement only through (n_pp, n_pn,
  n_nn).  ['p']*Z+['n']*N attains the MINIMUM possible n_pn (exactly 1 for
  Z,N >= 1), which is the interface-minimality the module docstring cites.
 nucleus  canon n_pn  min n_pn  max n_pn  canon is argmin?
      3H           1         1         2              True
     3He           1         1         2              True
     4He           1         1         3              True
     6Li           1         1         5              True
     7Li           1         1         6              True
     9Be           1         1         8              True
     12C           1         1        11              True
     14N           1         1        13              True

Reading
------------------------------------------------------------------------------
  * The antecedent of not_orderIndependent_of_ne HOLDS for this producer:
    L_pp - L_nn = h != 0 at the live pin, exactly.  So the theorem applies
    and the chain observable is arrangement-dependent at every A >= 3.
  * The producer resolves that dependence by HARDCODING one arrangement,
    the interface-minimal ['p']*Z+['n']*N.  That is a cost property, not
    a selection rule -- the same gap qou-48is records for the
    complete-graph path, where the orbit identity ranges over S_Z x S_N
    and so never compares two different arrangements.
  * Scope (a).  The spread measured above is the size of an undetermined
    convention factor, not evidence that the chain is the wrong bond set.
```
