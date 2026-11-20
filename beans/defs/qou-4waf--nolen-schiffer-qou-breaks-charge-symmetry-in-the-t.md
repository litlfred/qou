---
# qou-4waf
title: 'Nolen-Schiffer: QOU breaks charge symmetry in the TOPOLOGICAL channel, not the flavour channel'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T10:23:06Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-10v9
---


Branch: claude/anchor-followups-2026-08-08. From the writhe/double-count work
(qou-6nd0, commit 0f608066).

## 1. The code mis-named it. Two effects, OPPOSITE SIGNS.

coulomb_energy.py said the uniform sphere "over-estimates ... by ~5-10 % (the
Nolen-Schiffer anomaly)". Both halves are wrong: the over-estimate is 30.7 %,
and it is not the NSA. Measured at A=3:

    r0 = 1.2 fm geometry     E_C = 0.998413 MeV   +30.7 %   OVER
    measured charge radius   E_C = 0.680772 MeV   -10.9 %   UNDER
    experiment (3He-3H)            0.7638   MeV

(a) GEOMETRY, +30.7 %. r0=1.2 fm is a heavy-nucleus constant. At A=3 it gives
    R = 1.7307 fm; 3He's rms charge radius is 1.9661 fm, so the equivalent
    uniform R = sqrt(5/3)*r_rms = 2.5382 fm and the implied r0 is 1.760 fm, not
    1.2. Fixable by using the measured radius -- at the cost of importing an
    experimental input the framework otherwise avoids. NOT a derivation gap,
    an input choice.
(b) NOLEN-SCHIFFER, -10.9 %. Opposite direction: with the Coulomb done properly,
    theory falls SHORT by +0.083028 MeV at A=3 (~7 % for medium nuclei). This is
    a REAL derivation gap and is the standard evidence for charge-symmetry
    breaking in the strong NN force. Ref: Nolen & Schiffer, Ann. Rev. Nucl. Sci.
    19 (1969) 471. No literature search needed -- direction and magnitude are
    textbook; the docstring just needs the citation.

## 2. Can the Standard Model / eightfold way inform it? YES -- and it localises
## a real QOU defect.

In the SM the NSA residual is strong CSB, sourced by m_d - m_u and rho-omega
mixing: FLAVOUR effects, i.e. eightfold-way content.

QOU HAS a flavour-breaking parameter: delta = flavor_split_leading =
(q-1)^2(1-q^-4)/3 = 0.00137571080703, PROVEN.

**But it is in the wrong channel, and this is Lean-proved.** delta enters ONLY
the p-n bond (`d_pn = -h(1/2 - delta/4)`), and
`QOU.QBeta.InterfaceScalar.mirror_split_eq_L_diff` proves the mirror split is
alpha*(L_nn - L_pp) -- the p-n bond CANCELS EXACTLY. So delta contributes
IDENTICALLY ZERO to the mirror split. Meanwhile the split QOU does produce comes
from sigma vs sigma^-1, a crossing-sign assignment with NO flavour content.

    QOU breaks charge symmetry topologically where the eightfold way says it
    must break it in flavour.

## 3. Magnitudes bracket the target -- and BOTH current options are wrong

Required strong CSB at A=3: +0.083028 MeV.

    sigma/sigma^-1 + writhe (current)   0.76532019 MeV    9.22x TOO BIG
    gg flavour-blind (charge-symmetric) 0.0        MeV    misses entirely
    alpha*delta (flavour split)         0.00575870 MeV   14.4x TOO SMALL

Note this REVISES the conclusion in 0f608066. I wrote there that the strong
mirror split's target is exactly 0 by charge symmetry. That is wrong at the
0.083 MeV level: nature has small but NONZERO strong CSB, which is precisely
what the NSA measures. So the gg probe's exact zero is not the right answer
either -- it is much closer than the current 9.2x over-break, but it removes a
term nature has.

## 4. NOT chased (recorded so nobody re-fishes)

alpha*delta/h = 0.0275 MeV is 0.33x the target and is the closest single
combination tried. That is fishing, not derivation -- there is no argument for
dividing by h. Do not wire it.

## Next

- The honest fix is (2): give delta a channel that survives the mirror
  difference, i.e. let flavour breaking reach the LIKE-nucleon bonds, not only
  p-n. That is a structural change to the bond assignment, not a constant.
- Then the target is a derived +0.083 MeV, and the NSA becomes a TEST of QOU's
  flavour sector rather than a nuisance in the EM sector.
- Separately: coulomb_energy.py holds float64 literals (ALPHA_HBAR_C_MEV_FM =
  1.43996, R0_FM = 1.2) against the standing no-float64 directive.

## PRECISION NOTE on the numbers above (added same day)

Separating what is literature from what this bean computed:

  * DIRECTION (proper Coulomb undershoots experiment) -- standard, definitional.
  * ~7 % for medium-mass mirror pairs -- standard literature figure. Its
    UNIFORMITY across a wide mass range is what makes it an anomaly rather than
    a modelling defect.
  * -10.9 % / +0.083028 MeV at A=3 -- **NOT a literature value.** That is this
    bean's own equivalent-uniform-sphere estimate (sqrt(5/3)*r_rms), far cruder
    than the Faddeev calculations with realistic NN potentials that the
    published A=3 residual comes from. Published A=3 shortfalls are roughly
    0.06-0.08 MeV, so the estimate lands in the right range -- but "my estimate
    agrees with the range" is not "this is the standard number", and it was
    briefly written up as the latter. Corrected.

Consequence for section 3: the "required +0.083028 MeV" target is
uncertain at roughly the +/-25 % level, not a sharp number. The ORDER-OF-
MAGNITUDE conclusions survive unchanged -- current sigma/sigma^-1+writhe is
~9x too big, alpha*delta is ~14x too small, gg's exact zero omits a real term --
because those are factors of 9-14 against a target uncertain by ~25 %.

## DISAMBIGUATION: which "delta"/symmetry-breaking channel is which

Owner is right that symmetry was broken earlier via Bring's embedding. But those
are DIFFERENT channels and must not be conflated. At least four distinct objects
share the delta/Delta name in this corpus:

  1. FLAVOUR  delta(q) = flavor_split_leading = (q-1)^2(1-q^-4)/3 = 0.0013757.
     Enters ONLY the p-n bond, d_pn = -h(1/2 - delta/4). PROVEN.
  2. COLOUR   Delta(z), the Bring discriminant. brings-smoothness.md: "the six
     topological defects ... where the discriminant Delta(z) vanishes and two
     color sheets X_i, X_j collide". This is the Bring-embedding breaking the
     owner is recalling -- it is a COLOUR-sheet collision, S_5 automorphism.
  3. Delta-lambda, the entire computations/deltalambda/ cluster. A different
     object again (W-plane / lambda-scale), not a flavour split.
  4. Delta i, the Bring SHELL INDEX difference
     (conj:double-magic-delta-i-bound, |Delta i| <= 1).

WHY IT MATTERS FOR THE NSA. The Nolen-Schiffer residual needs FLAVOUR charge-
symmetry breaking (m_d - m_u, rho-omega mixing). Channel 2 (Bring Delta(z)) is
COLOUR breaking, not flavour -- it cannot supply it. Channel 1 IS flavour but is
Lean-proved to cancel out of the mirror split (mirror_split_eq_L_diff). So:

    the corpus HAS symmetry breaking in the colour channel (Bring) and in the
    flavour channel (delta), and NEITHER reaches the mirror split. What reaches
    the mirror split is the sigma/sigma^-1 crossing sign, which is TOPOLOGICAL
    and carries no flavour or colour content at all.

That is the disambiguation, and it sharpens the gap in section 2 rather than
softening it.

## THE RADIUS QUESTION -- what radius, and can we derive it

WHAT: the equivalent uniform-charge-sphere radius R = sqrt(5/3)*r_rms, i.e. the
radius of the uniform ball with the same Coulomb self-energy. For 3He the rms
CHARGE radius is 1.9661 fm -> R = 2.5382 fm. (Note charge vs point-proton radius
differ: subtracting the proton's own size R_p = 0.841 fm gives r_point ~ 1.777
fm. Which one you use changes E_C at the ~20 % level, so the choice must be
stated.)

HOW IT IS MEASURED (this is why the anomaly is meaningful): elastic electron
scattering, r_ch^2 = -6 dF/dQ^2 at Q^2=0; muonic-atom Lamb shift; isotope
shifts. In the real NSA analysis the radius is an EXPERIMENTAL input, not a
fitted one -- which is exactly what our r0=1.2 fm shortcut is not.

FALSE LEAD, KILLED: the form factor's Q^2 is a MOMENTUM TRANSFER (inverse
length); QOU's q0 = 1.10998 is DIMENSIONLESS. Same letter, unrelated. Do not
identify them.

CAN THE FRAMEWORK DERIVE IT? A route already exists and is already scoped:
computations/deltalambda/pion_radius_and_cusp_volume_gap_probe.py, which names
its own two gaps --
  GAP 1: why the per-nucleon packing length is the pion Compton wavelength
         lambda-bar_pi = hbar/(m_pi c) = 1.4139 fm at coefficient EXACTLY 1
         (measured 0.985 +/- 0.069);
  GAP 2: the hyperbolic-volume -> Euclidean-radius identification behind A^(1/3).
So the SCALE CLASS is argued (Vol(Hopf)=0 kills the W-plane contribution on the
bond channel, leaving CAL-3 / m_pi as the only length), but the COEFFICIENT is
measured, not derived. Companions in the same cluster:
mirror_split_continuum_em_probe.py, deltalambda_coulomb_mirror_split_probe.py.

NEXT on the radius: check whether lambda-bar_pi + the A^(1/3) identification
reproduces R = 2.5382 fm at A=3. It will not out of the box -- A=3 is not a
saturated sphere, and R/lambda-bar_pi = 1.795 -- so the light-nucleus regime
needs its own argument, which is the same place the r0=1.2 fm formula fails.

## Round 69 Update (PR #8249)
- Formalized in `ToffoliDimensionMismatchHeckeOffsetHypernuclearRatioNielsenThurstonAndNolenSchiffer.lean` and verified via 80-dps `mpmath` witness in PR #8249.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8249, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
