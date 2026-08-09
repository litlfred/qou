---
# qou-usft
title: 'Light-nucleus regime: derive the Coulomb radius AND density shape from binding + q-CLT, not r0*A^(1/3)'
status: in-progress
type: task
created_at: 2026-08-09T10:35:13Z
updated_at: 2026-08-09T10:35:13Z
---


Branch: claude/anchor-followups-2026-08-08. CLAIMED. From qou-4waf (Nolen-Schiffer).

## RESULT 1 — the light-nucleus radius IS derivable, from binding not saturation

`r0*A^(1/3)` assumes density SATURATION, which A<=4 nuclei do not have: they are
few-body quantum systems whose size is set by the separation energy, not by a
constant central density. Using the binding length

    1/kappa = hbar c / sqrt(2 mu S_sep),   mu(d,N) = (2/3) m_N = 625.946 MeV

    system      S_sep     1/kappa    R_meas=sqrt(5/3) r_rms   ratio
    3He (d+p)   5.49349   2.379462   2.538224                 1.0667
    3H  (d+n)   6.25725   2.229519   2.270988                 1.0186

    3He radius error vs measured:
      r0*A^(1/3), r0=1.2      1.7307 fm   -31.81 %
      binding length 1/kappa  2.3795 fm    -6.26 %

A 5x improvement, and from a quantity the FRAMEWORK PREDICTS (binding energies)
rather than an imported constant. This is the light-nucleus fix.

## RESULT 2 — but do NOT claim the improved CDE. Cancellation, again.

    radius used              R (fm)    E_C(3He)    vs expt
    r0*A^(1/3) [shipped]     1.7307    0.998413    +30.72 %
    binding length           2.3795    0.726194     -4.92 %
    measured charge radius   2.5382    0.680772    -10.87 %

The binding length is 6.3 % SMALL, which inflates E_C by ~6.7 %, which partially
covers the Nolen-Schiffer shortfall. Landing nearer experiment is a
CANCELLATION. Third time this pattern has appeared this session (m_avg
composition, writhe/Coulomb mirror, now this). The RADIUS result is real; the
CDE improvement is not a separate win.

## RESULT 3 — owner's q-CLT question, quantified: SHAPE alone is the whole anomaly

sqrt(5/3) is not neutral -- it is the UNIFORM-BALL moment relation, a classical
import. Define shape-only f by E_C = f * Q^2 / r_rms (radius divided out):

    shape           f          E_C(3He) at r_rms=1.9661   vs expt
    uniform ball    0.464758   0.680772 MeV               -10.87 %
    Gaussian        0.488602   0.715699 MeV                -6.29 %
    exponential     0.454663   0.665986 MeV               -12.80 %

    SPREAD FROM SHAPE ALONE = 7.30 % of the uniform value.

That is the SAME SIZE AS THE ENTIRE NOLEN-SCHIFFER ANOMALY (~7 %). Consequence,
and it is the governing constraint on this whole line:

    A radius alone is NOT enough. Any QOU claim about the NSA must derive the
    DENSITY PROFILE, not just a scale, or the shape ambiguity swamps the signal
    it is trying to explain. The real NS analyses dodge this by using the
    MEASURED form factor (a whole radial function), not a parameterised shape.

The q-CLT is the right instrument precisely because it specifies a
DISTRIBUTION, not a scale. `hecke_core_legacy.py:1295,1340` already carries a
q-Gaussian approximation; `binding_single_pipeline_comparison.py` already has
UNIFORM vs FACTORIZED B_qCLT variants. The q-Gaussian's f should be computed and
compared to the three above.

## RESULT 4 — "see if similar errors": YES, same class, at least two sites

  * `deltalambda/mirror_split_continuum_em_probe.py:32` already flags
    "3/5 -> uniform-sphere electrostatic self-energy -- **classical**", and
    :167 confirms it deliberately does NOT use the empirical r0. So that probe
    fixed HALF the import (the radius) and kept the other half (the SHAPE).
    That is exactly the residual error found here, already half-known.
  * `coulomb_energy.py` imports BOTH: r0 = 1.2 fm AND the 3/5 uniform-sphere
    coefficient. Also float64 literals (1.43996, 1.2) against the standing
    no-float64 directive.

So the corpus has q-CLT / q-Gaussian machinery in the STRONG sector and
classical uniform-sphere geometry in the EM sector. The mismatch is the error
class, and it is systematic rather than a one-off.

## NEXT

- [ ] compute the q-Gaussian shape factor f and place it against 0.4547-0.4886
- [ ] derive the A=3 separation energy from QOU rather than AME, closing
      binding -> radius -> E_C entirely inside the framework
- [ ] then, and only then, quote a CDE -- with the shape fixed, not assumed
- [ ] de-float64 coulomb_energy.py
