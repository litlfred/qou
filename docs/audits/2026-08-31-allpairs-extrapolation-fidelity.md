# allpairs_extrapolation_fidelity_probe — full output (2026-08-31)

Verbatim run. Regenerate with:

    python3 -u computations/allpairs_extrapolation_fidelity_probe.py

```
allpairs_extrapolation_fidelity_probe
==============================================================================
Per-bond energies eps = E_0*log(1/f), derived (bean qou-vsqh, #6338):
    f_pp =   0.612688037146   eps_pp = 2.05070969238 MeV
    f_pn =   0.508229789377   eps_pn = 2.833162572 MeV
    f_nn =   0.403627738351   eps_nn = 3.79778293514 MeV
  energies spread by a factor 1.85194 -- which is why a
  mix-blind extrapolation looked unsafe.

THE TEST.  B_allpairs_est = E_0*L*C(A,2)/(A-1), with L measured on the
CHAIN, against the true all-pairs sum over the complete graph's own mix.
 nucleus       chain mix      complete mix         est        true   est/true
       D       (0, 1, 0)         (0, 1, 0)    2.833163    2.833163        1.0
       T       (0, 1, 1)         (0, 2, 1)    9.946418    9.464108    1.05096
     3He       (1, 1, 0)         (1, 2, 0)    7.325808    7.717035   0.949304
     4He       (1, 1, 1)         (1, 4, 1)    17.36331    17.18114     1.0106
     6Li       (2, 1, 2)         (3, 9, 3)    43.59044    43.04394     1.0127
     7Li       (2, 1, 3)        (3, 12, 6)    64.14776    62.93678    1.01924
     7Be       (3, 1, 2)        (6, 12, 3)      58.033    57.69556    1.00585
     12C       (5, 1, 5)      (15, 36, 15)    192.4538    189.7212     1.0144
     16O       (7, 1, 7)      (28, 64, 28)    350.1809    345.0802    1.01478

  worst deviation from 1: 5.096 %
  => my 'type-mix artefact' conjecture is REFUTED (threshold: a mix artefact would have to exceed 10 %)

WHY IT SURVIVES — structural, not luck
  arithmetic mean of eps_pp, eps_nn = 2.924246314
  eps_pn                            = 2.833162572
  gap                               = 3.1148 %

  The bond factors satisfy f_pn = (f_pp + f_nn)/2 + h*delta/4, i.e. f_pn
  is essentially the ARITHMETIC mean of the other two.  Checked:
    (f_pp + f_nn)/2 + h*delta/4 = 0.50822978937673896258
    f_pn                        = 0.50822978937673896258
    |difference|                = 1.33638e-51
    exact to 1e-45: True   (algebraically (z + (z-h))/2 + h*d/4 = z - h/2 + h*d/4 = f_pn;
     the residual is rounding order at 50 dps, not a difference)

  Since eps = -E_0*log f, comparing eps_pn against (eps_pp+eps_nn)/2
  compares log of an arithmetic mean against the arithmetic mean of
  logs.  By Jensen the first is larger, so eps_pn <= (eps_pp+eps_nn)/2
  NECESSARILY -- the sign of the gap is forced, not observed.  Checked
  rather than asserted: eps_pn <= mean is True.
  The gap is SMALL because f_pp/f_nn = 1.51795, close
  to 1, and Jensen's gap vanishes as the arguments coincide.

WHAT THIS DOES NOT RESCUE
------------------------------------------------------------------------------
  The objection from #6346 stands untouched: the complete graph is NOT
  EXPRESSIBLE in the 3A braid word, because a single generator joins
  only consecutive nucleons (QOU.Mass.StrandLayoutForcesChain).  So the
  all-pairs number is an arithmetically faithful evaluation of a bond
  set the word cannot write.  The extrapolation is sound; what it
  extrapolates TO remains unrealised.

  So the 0.61-1.63x all-pairs range from #6364 is not an arithmetic
  artefact -- it is a real evaluation of a hypothetical bond set.  That
  makes it more interesting than I said, and no more realised.
```
