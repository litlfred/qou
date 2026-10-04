---
# qou-dvlt
title: 'FRONT (consolidated): c_3 is precision-blocked — 3 open beans, 0 decidable tests'
status: todo
type: feature
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-15T11:22:44Z
updated_at: 2026-10-04T15:15:11Z
parent: qou-avtq
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


---

# OPTION B — EXECUTED 2026-08-15. Answer: INTRINSIC. Front (a) is CLOSED.

Option B asked whether the `|q~| ~ 1e-165` modular-dual suppression at the
substrate is an `arg b` artifact or intrinsic. It is intrinsic, and the reason
is **algebraic, not analytic** — which is why no convention can evade it.

With `b^2 = i y` (forced: a real `q` requires `b^2` purely imaginary):

    log q = -2 pi y ,   log q~ = -2 pi / y   =>   log q * log q~ = 4 pi^2

**The `y` cancels.** After demanding a real `q`, `y` is the only remaining
freedom and the product does not depend on it. Verified at three unrelated `y`
(0.001, 1, 17.25): identical to 20 digits.

Measured at the substrate (probe exit 0, 6/6):

    Re(b^2)                          0.0 exactly
    |q - 1/q0|                       0.0 exactly
    log|q| * log|q~| vs 4 pi^2       relative error 0.0
    balance point |log q| = 2 pi     6.28319
    substrate     |log q|            0.10434    <- 60.2x too close to 1
    forced        |log q~|           378.361    => |q~| ~ 4.8e-165
    q0 needed for |q~| > 1e-16       > 2.92     (substrate is 1.10998)

Lean: `QOU.QBeta.ModularDoubleReciprocity`, sorry-free, 4 declarations, axioms
`[propext, Classical.choice, Quot.sound]`. Stated over a **generic field in a
generic `c`**, because the fact is `(c y)(c / y) = c^2` — putting it that way is
the point, since an algebraic identity leaves nothing to re-choose.

## What this closes

`BarInvolutionDomainObstruction` (PR #5093) proved the parity read-off needs a
**pair**, not a single series — the Garoufalidis-Zagier shape, whose second entry
IS this modular dual. `phi_b_evaluator.py` already realises that pair at the
substrate. **Its second entry is 1e-165 there**, and `q0` is an INPUT, so nothing
in the construction can be re-chosen.

**Sitting near 1 IS sitting at the degenerate point of the modular double.** The
framework's own substrate value places it 60x from the balanced point.

So **front (a) as stated is CLOSED**: "build the GZ pair carrier at the
substrate" cannot work, for a proved structural reason rather than for want of
effort.

## Standing prohibition, added

Do NOT re-open the state-integral carrier at the substrate by adjusting `arg b`,
the contour, or the `b` normalisation. The reciprocity is identical in `y`; every
such adjustment lands on the same 4 pi^2.

## What survives

  * The state integral itself. `phi_b_evaluator` is validated (10/10) and its
    NATIVE regime (|q| = 1, roots of unity) is untouched — that is the bar-stable
    locus of PR #5093, where everything works.
  * Option **D** (write the 26x/32x/130x up as a measurement proposal) is now the
    highest-value remaining item on this front.
  * Option **C** (find a decay-face observable whose sigma does not carry 1/u^3)
    is the only route to a testable c_3 claim without new experiment, and is
    untouched by this result.

Options A and B are now spent. The front's honest state: **precision-blocked
(front (e)), and the one structural route out is closed (this note).**


---

# OPTION D — EXECUTED 2026-08-15. The ask is now concrete.

[`docs/audits/2026-08-15-c3-front-measurement-ask.md`](../docs/audits/2026-08-15-c3-front-measurement-ask.md)
+ probe `qbeta_c3_measurement_proposal_budget.py` (exit 0, 4/4).

D turned the bare "26x/32x/130x" into something a nuclear-physics reader can
act on, and produced two findings the bare factors did not carry.

## 1. WHICH number — and one trap

`Q_beta` is reachable two ways:

    direct CAL-3 (PDG 2024 / AME 2020)     sigma = 0.61  eV
    Q_beta = m_n - m_p - m_e, in quadrature sigma = 0.561 eV

**The second is NOT a free 9% improvement, and I nearly published it as one.**
Quadrature assumes independence; AME2020 is a GLOBAL least-squares adjustment,
so `m_n`, `m_p` and the neutron Q-value are correlated outputs of one fit.
Without the covariance — which this repo does not carry — 0.561 eV is a LOWER
BOUND, not the route's precision. All factors are quoted against the direct
0.61 eV, which needs no covariance to be meaningful.

## 2. WHERE the uncertainty lives

    sigma(m_n) = 0.48 eV     73.3 % of the variance
    sigma(m_p) = 0.29 eV     26.7 %
    sigma(m_e) = 0.00016 eV  ~0

**An improvement programme that does not touch the NEUTRON MASS cannot deliver
any of the factors.** That is the actionable sentence, and it is not visible
from the factors alone.

## The table

    target                                        need sigma(Q_b)   factor
    zero-location test resolves at mu-p scale         0.0238 eV     25.7 x
    c_3 ~ -Vol(4_1) at 1 sigma (proton)               0.0191 eV     32.0 x
    c_3 ~ -Vol(4_1) at 1 sigma (muon)                 0.0047 eV    130.3 x

Three independent routes, ordering sensibly — a check on all three, not a
restatement of one.

## Explicitly not claimed

Feasibility, technique, cost. Outside what this repo can assess. The note says
so in its own words: "saying which number to improve is useful; pretending to
know how is not."

And it bears on (H1) in NEITHER direction. 0.03 sigma is not evidence for (H1)
and not evidence against it.

## Front status after A/B/D

    A  stop / redirect          the default, still available
    B  dual degeneracy          EXECUTED -> intrinsic; front (a) closed
    C  decay-face observable    UNTOUCHED — the only route to a testable c_3
                                claim without new experiment
    D  measurement proposal     EXECUTED -> this note

**C is the only remaining item that could change the picture from inside the
theory.** Everything else on this front now waits on an experiment.


---

# OPTION C — EXECUTED 2026-08-15. Affirmative, but NOT as posed.
# Probe `qbeta_c3_slope_filter.py` (exit 0, 5/5).

C asked for a decay-face quantity whose sigma does not carry the `1/u^3`
amplification. **There is one: the cross-anchor SLOPE.** The amplification is
COMMON-MODE and cancels in the difference.

    dc_3/dQ_beta at proton      2068767.790 per MeV
    dc_3/dQ_beta at muon        2068766.549 per MeV
    d(swing)/dQ_beta                 -1.241 per MeV      <- 1.67e6 cancellation

    c_3 VALUE   sigma/|c_3|     60.98 %        unusable (front (e))
    c_3 SLOPE   sigma/|swing|   15.41 ppm      39574x sharper

## THE LIMITATION — state it before the factor, always

`c_3(q) = (Q_beta^exp/Q_N2(q) - 1)/u(q)^3` is **completely determined** once
`Q_beta^exp` is fixed. So `dc_3/dq` is NOT a measurement — it is a computation
from the extractor. The 15.41 ppm is the precision with which the EXTRACTOR's
slope is insensitive to the Q_beta error, **not** a precision with which nature
has told us anything.

The sharpness comes from **experiment cancelling out**. That is why it is sharp.

So the slope tests a candidate derived `c_3(q)` against the FRAMEWORK'S OWN
LADDER SHAPE — theory against theory. **It does not lift the precision block**
established by front (e), and it cannot confirm the framework against nature.
Do not cite 39574x as an experimental precision.

## WHY IT IS STILL WORTH HAVING — it is a FIT-DETECTOR

    value check   61 %      slack  ->  a one-anchor fit passes TRIVIALLY
    slope check   15.4 ppm  slack  ->  a one-anchor fit does NOT

This inverts the usual worry, and it explains the front's history: ~60 probes
produced agreements that meant nothing **because the value check has 61 % of
slack**. Any candidate now has to reproduce the slope within 15 ppm as well, and
a fit to one anchor has no way to do that except by accident.

It cannot tell you a derivation is RIGHT. It will tell you a **fit is a fit**, at
4.6 orders of magnitude better resolution than anything else on this front.

**This is the first cheap discriminator the front has ever had.** Every future
candidate `c_3` should be run through it before anything else.

## Relation to registry section 9e

9e records the swing as "resolved but NOT an independent derivation target",
because it factors as (11.54 ppb mu-p tension) x dc_3/dq. **That is correct and
is not disputed here.** The distinction is between a derivation TARGET and a
test OBSERVABLE: you cannot derive the swing without already having c_3's shape,
but you can certainly CHECK a proposed shape against it. The "circular" label
has been read as disqualifying both uses; only the first is disqualified.

## FRONT STATUS — all four options now spent

    A  stop / redirect          available; now the default
    B  dual degeneracy          EXECUTED -> intrinsic; front (a) closed
    C  observable avoiding 1/u^3  EXECUTED -> the slope; an INTERNAL FILTER,
                                  not an experimental test
    D  measurement proposal     EXECUTED -> the neutron mass, 26x/32x/130x

**Net: the front is closed to theory work that hopes to be VALIDATED, and open
to theory work that is willing to be FALSIFIED by the slope filter.** Those are
different activities and the front should be described as the second from now on.


---

# D SHARPENED + THE LIT QUESTION IS BLOCKED (2026-08-15)

## One measurement or two — this changes the ask

The mass-difference route adds in QUADRATURE, so each input must individually
fall below the target. **`sigma(m_p) = 0.29 eV` alone already exceeds every
target.** So:

    target                              direct Q_beta    m_n      m_p
    zero-location resolves at mu-p         25.7 x      20.2 x   12.2 x
    c_3 ~ -Vol(4_1) 1-sigma (proton)       32.0 x      25.2 x   15.2 x
    c_3 ~ -Vol(4_1) 1-sigma (muon)        130.3 x     102.6 x   62.0 x

  DIRECT route     = ONE measurement improved ~26x
  MASS-DIFF route  = TWO measurements improved ~20x and ~12x

Which is cheaper is a domain question. But the ask is now in the form an
experimentalist works in, not a single factor on a derived quantity.

## The literature question is BLOCKED in this sandbox — do not fake it

**Is sigma(m_n) = 0.48 eV improvable by 20x+, and by what technique?** That is
the next question, and it is NOT answerable from inside this repo.

Attempted and blocked: the paper-search MCP returns zero results for every
query — a bare `"quantum"` arXiv search returns nothing — and the egress proxy
answers 403 to CONNECT. No literature was consulted.

Recorded explicitly because the alternative (plausible sentences about
crystal-diffraction gamma spectrometry or Penning-trap limits, from memory) is
exactly the failure mode this whole front is a case study in. **Whoever picks
this up with working network can close it in one pass.** Nothing else in D
depends on it; every other number traces to a committed witness.
