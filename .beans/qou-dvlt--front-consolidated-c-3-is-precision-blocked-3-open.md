---
# qou-dvlt
title: 'FRONT (consolidated): c_3 is precision-blocked — 3 open beans, 0 decidable tests'
status: todo
type: milestone
created_at: 2026-08-15T11:22:44Z
updated_at: 2026-08-15T11:22:44Z
---


Consolidates `qou-qb8e`, `qou-qb8g`, `qou-kh7e` — all `todo`, all the same front.
They stay open (each still holds its own detail); this bean is the front-level
state so a new agent does not have to reconstruct it from four correction
histories.

## THE HEADLINE: the front is PRECISION-blocked, not idea-blocked

After ~60 probes (40 Phi_b witnesses alone, ~20 D-ladder arms, the whole A_omega
arc), **neither channel of the c_3 gate resolves anything**:

    channel          resolution                              short by
    magnitude        sigma(c_3) = +/-1.262 = 61% of |c_3|     0.03 sigma is the
                                                             "agreement"
    zero location    sigma(q*_S) = 3.29e-7 vs a 1.28e-8       25.7x
                     genericity-window image
    swing            RESOLVED (+/-7.6e-7) but CIRCULAR        n/a — it factors as
                                                             (mu-p tension) x dc_3/dq

**More probes cannot help.** The deliverable of the whole front is three
thresholds on the same experimental lever:

    25.68x sharper Q_beta  ->  zero-location test resolves at the mu-p scale
    31.98x                 ->  proton c_3 ~ -Vol(4_1) reaches 1 sigma
    130.3x                 ->  muon                    reaches 1 sigma

computed by three independent routes, ordering sensibly. That is a real result,
but it is an EXPERIMENTAL one.

## Why it took ~60 probes to notice

`sigma(c_3) = sigma(Q_beta)/(Q_N2 u^3)` is one line of error propagation. The
`1/u^3 ~ 1.6e6` amplification was the HEADLINE of the 2026-07-12 capstone. The
derivative was known; nobody multiplied it by the input error. The same formula
was read for its consequence for *signal* and never for *noise*.

## The state-integral route (front (a)) — already built, and degenerate

`computations/qbeta/phi_b_evaluator.py` exists, validated (10/10 battery), and
its SUBSTRATE regime already sits at the point front (a) was going to build:
`arg b = +pi/4` gives `q = e^{2 pi i b^2} = 1/q0`. So "build the carrier at
1/q0" is **done**.

**But the modular dual is `|q~| ~ 1e-165`** (its own docstring, line 18-19), so
Phi_b degenerates toward the compact form on the mass face. The GZ *pair*
structure — which `BarInvolutionDomainObstruction` (PR #5093) says is exactly
what a single series cannot supply — is numerically ABSENT at the substrate.
The second entry is 1e-165.

That is a bad sign for (a) as stated and should be settled before more is built.

## Attack options, honestly ranked

  A. **STOP; redirect.** The front is precision-blocked. Default choice.
  B. **Is the 1e-165 dual degeneracy intrinsic or an arg-b artifact?** Cheap,
     decisive, and it determines whether (a) is alive at all. Do this before
     any further carrier work.
  C. **Find a decay-face observable whose sigma does NOT carry 1/u^3.** The
     swing is the only resolved quantity and it is circular; is there another?
     This is the only route to a testable c_3 claim without new experiment.
  D. **Write the 26x/32x/130x up as a measurement proposal.** Turns the front's
     actual deliverable into something a nuclear-physics reader can act on.

Do NOT: another magnitude match on |S_leak|; another Borel/Leroy/Stokes/Ecalle
probe on the D-ladder; another evaluation-point choice for J(4_1) (bar-invariant,
PR #5098); a seventh fitted ansatz.

## The self-correction rate is the tell

`qb8g` has had FOUR corrections, alternating direction. `qb8e` has had THREE
front-state corrections, each declaring the previous framing malformed. On
2026-08-15 alone I corrected my own published conclusion twice within hours
(#5084's "evaluate at 1/q0" -> #5098's "bar-invariant, 1/q0 is no better").

When a front's dominant output is corrections to its own framing, it is not
converging. It is oscillating around an unmeasurable target.

## Merged 2026-08-15

  #5074 q*_S is not a third determination (12 sites)
  #5001 which pin the numbers use
  #5084 Habiro evaluation trichotomy (Lean)
  #5093 bar-involution domain obstruction (Lean) + (H1) is 0.03 sigma
  #5098 4_1 cyclotomic term is bar-invariant (Lean)
