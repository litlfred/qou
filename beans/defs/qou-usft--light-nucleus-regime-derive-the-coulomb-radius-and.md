---
# qou-usft
title: 'Light-nucleus regime: derive the Coulomb radius AND density shape from binding + q-CLT, not r0*A^(1/3)'
status: in-progress
pr: 8192
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-mass
created_at: 2026-08-09T10:35:13Z
updated_at: 2026-10-10T07:15:57Z
parent: qou-8lxd
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

## RESULT 5 — should q-geometry be in EM too? YES, and it is NOT negligible

Owner asked whether the q-deformation is just negligible at q0 = 1.110. It is
not, and the reason is that the anomaly being chased is small:

    h  = q - 1/q        = 0.2090603    (20.91 %)
    h^2                 = 0.0437062    ( 4.371 %)
    hbar_q = (q-1)/q    = 0.0990817    ( 9.908 %)
    h^3                 = 0.0091372    ( 0.914 %)

    Nolen-Schiffer anomaly           ~ 7 %
    density-shape ambiguity (R3)     = 7.3 %

An O(h^2) q-geometry correction is 4.4 % and an O(h) one is 20.9 %. BOTH are
comparable to or larger than the 7 % being explained. So q-geometry corrections
cannot be dropped as small -- they are the same order as the signal. q0 looks
close to 1, but h is 21 %, and that is the number that matters.

## RESULT 6 — corpus consistency on geometry: the EM sector is the outlier

Swept. 710 files under computations/ carry q-deformed or hyperbolic geometry
(q_int, quantum dimensions, hyperbolic volumes). The ENTIRE nuclear EM-sector
geometry is two lines of classical Euclidean:

    coulomb_energy.py:76   return R0_FM * A ** (1.0 / 3.0)
    coulomb_energy.py:86   return 0.6 * Z*(Z-1) * ALPHA_HBAR_C_MEV_FM / nuclear_radius_fm(A)

Four separate classical imports in those two lines:
  1. r0 = 1.2 fm            empirical saturation constant (fails at A<=4, R1)
  2. A^(1/3)                classical saturated-sphere scaling, Euclidean
  3. 3/5                    uniform-BALL shape factor (the 7.3 % ambiguity, R3)
  4. ALPHA_HBAR_C = 1.43996 CODATA alpha_EM -- NOT the framework's derived one
plus float64 throughout, against the standing no-float64 directive.

Point 4 is the sharpest: `ALPHA_EM_INV_DERIVED` / `_alpha_em_inv_derived`
EXISTS and is used in the meson EM sector
(meson_em_sinh_closed_form.py:42,162,192), so the framework already derives
alpha_EM from q and already uses it elsewhere. The nuclear EM sector simply does
not call it. That is not a derivation gap, it is an unwired one.

So the consistency answer is: the framework is q-deformed in the strong sector
and in the meson EM sector, and CLASSICAL in the nuclear EM sector. The
Nolen-Schiffer work sits exactly on that seam, which is why it keeps producing
cancellations rather than signal.

## REVISED NEXT (ordered by cheapness x leverage)

- [ ] 1. Wire the DERIVED alpha_EM into coulomb_energy.py. Pure wiring, the
         object already exists and is already used in the meson sector. Also
         de-float64 while touching it.
- [ ] 2. Replace r0*A^(1/3) with the binding length for A<=4 (R1: -31.8 % ->
         -6.3 %). Uses framework-predicted binding energies.
- [ ] 3. Compute the q-Gaussian shape factor f and place it against
         0.4547 / 0.4648 / 0.4886. CAUTION: Tsallis q and quantum-group q are
         DIFFERENT parameters -- do not feed q0 = 1.10998 into a Tsallis
         q-Gaussian, that is a category error.
- [ ] 4. Only then quote a CDE, with shape derived rather than assumed, and
         check it is not another cancellation before claiming anything.

## STEP 1 DONE — derived alpha_EM wired (commit a188542f)

  1/alpha_EM derived 137.035935094 vs CODATA 137.035999177 (468 ppb)
  E_C(3He) 0.998413 -> 0.9984161199 (+3.625 ppm). mpmath end to end.
Provenance fix, not numerical. Audit flag clear.

Also de-vacuumed the audit's own regression test, which had been asserting the
defect was PRESENT and so kept passing after the fix by matching the docstring
prose describing the old behaviour. Scanner now skips triple-quoted regions.
Second time today an audit passed for the wrong reason -- a test pinned to "the
bug is still here" silently inverts the moment the bug is fixed.

## STEP 2 — RETRACTION. The binding-length radius is NOT parameter-free.

R1 above reported the binding length hbar c/sqrt(2 mu S_sep) cutting the 3He
radius error from -31.8 % to -6.3 %. **That used AME separation energies**, i.e.
an experimental input -- exactly the defect just fixed in step 1. With QOU's OWN
predicted binding it goes the other way:

    QOU chain binding (D + writhe):  2H +27.34 %, 3He -30.37 %, 3H -27.61 %

              S_AME     S_QOU     R(from S_AME)      R(from S_QOU)
    3He      5.49349   2.54159   2.3795 (-6.26 %)   3.4982 (+37.82 %)
    3H       6.25725   3.30691   2.2295 (-1.83 %)   3.0668 (+35.04 %)

Parameter-free, the binding-length radius is WORSE than r0*A^(1/3) and opposite
in sign, because QOU's A=3 binding is ~30 % low. So NOT WIRED. Wiring it would
have imported AME through the back door and looked like a win.

The binding-length SCALING is still the right physics for A<=4 (size set by
separation energy, not saturation). It becomes usable only when QOU's light
binding is right, which makes it downstream of the NN sector, not a fix for it.

## STEP 3 — the shape question, inverted into a target

Rather than guess a q-deformed density, ask what f the CDE actually needs.
With f defined by E_C = f*Z(Z-1)*alpha*hbar_c/r_rms and the measured
r_rms(3He) = 1.9661:

    required f (zero strong CSB)  0.5214134
    Gaussian                      0.488602    0.937 x required
    uniform ball                  0.464758    0.891 x
    exponential                   0.454663    0.872 x

THE REQUIRED f IS ABOVE ALL THREE CLASSICAL SHAPES. It needs a density MORE
centrally concentrated than a Gaussian. So no classical shape closes the CDE by
itself; either the density is more peaked than any classical option, or there is
real strong CSB. Even the Gaussian -- the most peaked classical choice -- leaves
6.29 % unaccounted, which is the Nolen-Schiffer anomaly appearing from the shape
side rather than the radius side.

That is the actionable target for the q-CLT: **f_qCLT must exceed 0.4886 to beat
the best classical shape, and reach 0.5214 to close the CDE alone.** If the
q-deformed density comes out LESS peaked than a Gaussian, the shape route is
dead and the residual is strong CSB, which is the SM's own answer.

CAUTION carried forward: Tsallis q and quantum-group q are different parameters.
Do not feed q0 = 1.10998 into a Tsallis q-Gaussian.

## STATE

- [x] 1. derived alpha_EM wired, de-float64
- [x] 2. binding-length radius EVALUATED and REJECTED as not parameter-free
- [x] 3. shape target derived: f must reach 0.5214 (Gaussian 0.4886 is the
         classical ceiling)
- [ ] 4. compute f for the framework's own q-deformed density and compare
- [ ] 5. only then quote a CDE

## STEP 4 — CANNOT BE COMPUTED. The framework has no spatial charge density.

Went to compute f for the framework's q-deformed density and found there is no
such object. Two checks:

  * `deltalambda/mirror_split_continuum_em_probe.py:34` tiers its own density as
    "MODEL ASSUMPTION (uniform charge density)" -- the corpus already knows this
    is assumed, not derived.
  * the q-CLT is over BONDS / TRACE FACTORS, not position:
        B_qCLT(K)   = alpha * bonds(K) * ell-bar      (per-bond bulk sum)
        B_qCLT_fac  = alpha * Sum_i ln|V_i|           (factorised trace)
    Both live in TRACE space. Neither is a probability distribution over R^3.

Using the q-CLT as a spatial charge density would be a CATEGORY ERROR, the same
class as feeding q0 into a Tsallis q-Gaussian. Recorded so the next agent does
not do it: the q-CLT factorises a trace over bonds; it says nothing about where
charge sits.

Nor does the Bozejko-Speicher quantum-group q-Gaussian rescue it directly: it is
a ONE-dimensional measure on a compact interval, and it is defined for
q in (-1,1) while q0 = 1.10998 > 1. Turning it into a 3-D radial charge density
requires an extra modelling assumption, which is precisely the thing being
avoided.

## THIS REVISES RESULT 6 ABOVE

R6 said the EM sector's classical geometry was an inconsistency, and grouped it
with the alpha_EM defect as "unwired, not underived". That was right for
alpha_EM -- the derived object existed, was already used in the meson sector,
and is now wired (step 1). It is WRONG for the geometry:

    alpha_EM   -> was UNWIRED. Fixed.
    r0, A^(1/3), the 3/5 shape -> UNDERIVED. There is no q-deformed
                                  position-space object to wire in their place.

So the EM sector is not classical by oversight. It is classical because the
framework has never constructed a position-space geometry at all -- everything
it has is trace-space or hyperbolic-volume. That is a much larger gap than a
wiring miss, and it is the real reason the Nolen-Schiffer line keeps producing
cancellations: three of the four EM inputs have no derived counterpart to
compare against.

## FINAL STATE OF THIS BEAN

- [x] 1. derived alpha_EM wired + de-float64 (a188542f). Real, small (+3.6 ppm),
         provenance not numerics.
- [x] 2. binding-length radius EVALUATED and REJECTED -- the -6.3 % win used AME
         S_sep; parameter-free it is +37.8 %, worse than r0*A^(1/3).
- [x] 3. shape target derived: f must reach 0.5214 to close the CDE alone;
         Gaussian 0.4886 is the classical ceiling, leaving 6.29 %.
- [x] 4. f for the framework's density: NOT COMPUTABLE -- no such density exists.

## WHAT WOULD ACTUALLY UNBLOCK THIS

Not more EM work. Two prerequisites, both outside this bean:

  1. A POSITION-SPACE density from the framework. Until one exists, the shape
     factor is an assumption and the 7.3 % shape ambiguity swamps the 7 %
     anomaly. This is the blocker for steps 3-5.
  2. QOU's LIGHT-NUCLEUS BINDING (currently 3He -30 %, 3H -28 %). The
     binding-length radius becomes usable the moment this is right, and it is
     the right physics for A<=4. Downstream of the NN sector (qou-kj4v,
     qou-7zob), not of the EM sector.

Recommend this bean go to BLOCKED on those two rather than stay in-progress:
every remaining EM-side step is gated on an object the framework does not have.


## CORRECTION (sweep returned, 2026-08-09) — narrow the step-4 framing

Step 4 above says "the framework has never constructed a position-space geometry
at all" and "no such density exists". The first clause is FALSE and the second
is right for the wrong reason. Corrected in qou-mumr; summarised here so this
bean is not read alone.

WHAT EXISTS: a derived but DIMENSIONLESS Planck length (ell_P = hbar_q*t_P == 1
over any field -- an ANGULAR Reeb displacement, carrying no scale), and several
ASSUMED metrics: Fubini-Study inherited on Bring's surface, the round metric on
P(V) = S^2 with an actual distance function d_{P(V)} gating a force law, and a
base manifold M with a smooth metric and spatial wavenumbers. All declared
archimedean specialisation, i.e. INPUTS.

WHAT DOES NOT: any transport from algebraic/hyperbolic invariants to Euclidean
length, and any 3-space or rho(r). The corpus states the first about ITSELF --
pion_radius_and_cusp_volume_gap_probe.py:56, "there is NO categorical
volume->length transport in the corpus. All corpus lengths arise as Compton
inversions hbar c / mass." And the nearest density ansatz, rho(K) = tr_M(K), is
MACHINE-CHECKED REFUTED in lean/QOU/MassTheory/RadialVolRhoMirrorTest.lean --
it fails the 3H/3He mirror in DIRECTION (C_knot 1.35 vs rho 0.50, straddling 1).

So this bean's CONCLUSION stands unchanged: r0, A^(1/3), 3/5 and rho(r) have no
derived counterpart, and the EM line is blocked. Only the justification was
overstated. Two cautions carried in: the q-CLT is trace-space, not a spatial
distribution; and the corpus holds TWO incompatible Planck lengths differing by
t_P ~ 10.1 (qou-adwi), so "convert a framework length to fm" is not yet
well-posed either.


## A^(1/3) IS NOT REPAIRABLE FOR LIGHT NUCLEI — measured, 2026-08-09

With the length now CAL-3 (lambdabar_pi = 1.4138 fm, commit 9a1d7680), the
entire remaining A=3 radius error is the A^(1/3) SATURATION assumption. Tested
by solving for the exponent x that R = lambdabar_pi * A^x would need:

    nucleus   r_rms    R_equiv   R/lambdabar_pi     x
    2H        2.1421   2.765439  1.95601          0.9679
    3H        1.7591   2.270988  1.60628          0.4314
    3He       1.9661   2.538224  1.79530          0.5326
    4He       1.6755   2.163061  1.52994          0.3067

A^(1/3) needs x = 0.3333 everywhere. Measured x runs 0.31 -> 0.97, a factor of
three. NO power law fits, and the ordering says why: 4He (x = 0.307, nearly
A^(1/3)) is tightly bound and compact, while 2H (x = 0.968) is a halo -- weakly
bound and enormous. SIZE TRACKS BINDING, NOT NUCLEON COUNT.

So the saturation exponent is not a coefficient to be tuned; it is the wrong
functional form in this regime. Which is the same conclusion the binding-length
route reached independently, from the other direction.

## CONSEQUENCE — the EM sector is now fully gated on the NN sector

Everything importable has been replaced or accounted for:

    alpha_EM      DERIVED (a188542f)      was CODATA
    hbar c        unit conversion         legitimately external
    nuclear length CAL-3 lambdabar_pi     was empirical r0 = 1.2 (9a1d7680)
    A^(1/3)       WRONG FORM for A<=4     needs binding, measured above
    3/5 shape     needs a density         none exists (qou-mumr)

The two remaining items both require the same thing: QOU's light-nucleus binding
energies, currently 2H +27.3 %, 3He -30.4 %, 3H -27.6 %. There is no further EM
work that does not wait on them.

NEXT IS THE NN SECTOR, not this bean. The live handles there:
  * qou-kj4v -- the deuteron is now REACHABLE under D (required d = -0.11945 h,
    inside the Hecke range); the gap is that the derived colour weight
    t = 0.499656 is not the required t = 0.119453. ONE bond, no coordination
    freedom, so this is pure bond-energy error with nothing topological to
    blame. Cleanest target in the framework.
  * qou-7zob -- the ell/space index, needed because Pauli locks spin to isospin
    and a flavour-only interface cannot split 3S1 from 1S0 at all.
  * qou-h7mh -- the coordination/bond-count question for A >= 3.


## Progress Checklist (Round 56 — PR #8192)
- [x] Non-vacuous Lean 4 formalization in `QOU.Eightfold.CPBarParityLevel3ChannelAndWignerS3Pinning` (`0` `sorry`, `0` vacuity audit findings)
- [x] 50-dps `mpmath` probe `computations/probes/cp_bar_parity_level3_channel_and_wigner_s3_pinning_probe.py` and stamped witness `computations/probes/cp-bar-parity-level3-channel-and-wigner-s3-pinning.witness.json` (`allPassed: true`, `scriptHash: d2a06f0c494a`, `scriptCommitSha: c0214e17e49e615dc65e266a92be3d79589d2874`)
- [x] Opened PR `litlfred/qou#8192` (`82fe2aa092fb7be41555f2084a2891bcea71c295`)
- [ ] Awaiting merge and final closure verification
