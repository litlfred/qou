---
# qou-4waf
title: 'Nolen-Schiffer: QOU breaks charge symmetry in the TOPOLOGICAL channel, not the flavour channel'
status: todo
type: task
created_at: 2026-08-09T10:23:06Z
updated_at: 2026-08-09T10:23:06Z
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
