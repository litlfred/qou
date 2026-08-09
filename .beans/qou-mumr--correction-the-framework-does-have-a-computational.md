---
# qou-mumr
title: 'CORRECTION: the framework DOES have a computational length -- distance is a Reeb step count, ell_P == 1'
status: todo
type: task
created_at: 2026-08-09T11:02:55Z
updated_at: 2026-08-09T11:02:55Z
---


Branch: claude/anchor-followups-2026-08-08.

## I WAS WRONG. Retracting a claim I made twice today.

I wrote, in qou-usft and in the coulomb_energy.py docstring, that "the framework
has never constructed a position-space geometry at all -- everything it has is
trace-space or hyperbolic-volume", and concluded that r0, A^(1/3) and the 3/5
shape factor have NO derived counterpart to wire in. The owner said that was
wrong and pointed at a computational Planck length. They are right.

`content/quantum-observable-universe/information-theory/discrete-planck-step.md:35`

    One Planck length of flow. After one Planck step, the Reeb flow displaces a
    state by exactly one Planck length:

        ell_P(q) = hbar_q * t_P = (1 - q^-1) * q/(q-1) = 1.

    "The Planck length identically evaluates to 1 over any field."

Also `fluid-dynamics/p5-counterexample.md:4`: "The separation d is measured in
units of the Planck length ell_q = (q-1)/q."

So the framework HAS a length, and more than that it has a notion of DISTANCE:
**distance in spacetime is computational** -- it is a COUNT of Reeb/Planck
steps, with ell_P == 1 by construction and "no sub-step resolution"
(discrete-planck-step.md:33). Distance is integer-valued, not a real number.

## Why this matters, and it reframes the whole EM line

qou-usft concluded the Coulomb work was blocked because no position-space object
exists. That conclusion is WRONG as stated. What is actually true is narrower
and more useful:

  * a nuclear radius in this framework is a STEP COUNT, not a length in fm;
  * converting a step count to fm needs the unit-system map, and
    `observations/g-q-closed-form.md:64` says exactly that -- G_Newton "enters as
    a unit-system datum, not as a fit parameter on q", fixing ell_P, m_P, t_P
    onto metres;
  * so the charge "density" is a distribution over a DISCRETE step lattice, not
    a continuous rho(r). The uniform-ball / Gaussian / exponential shape factors
    computed in qou-usft are all CONTINUUM objects and may all be the wrong
    class of answer.

That last point is the live one. The 7.3 % shape spread I measured was across
three continuum profiles. If the framework's density lives on an integer step
lattice, the right calculation is a LATTICE Coulomb sum, not an integral, and
the shape factor f must be recomputed in that setting.

## Status of the sweep

A full corpus search on derived length / distance / metric recovery, and on the
computational-QFT / quantum-gravity source the owner recalls, was dispatched and
is still running at the time of writing. This bean records only what was
verified by direct grep. The sweep may find more -- in particular whether any
construction recovers a METRIC (not just a length unit), which is what a real
rho(r) would need.

## Corrections owed elsewhere

  * qou-usft "STEP 4" section and its "WHAT WOULD ACTUALLY UNBLOCK THIS" -- the
    "no position-space density exists" framing must be narrowed to "no CONTINUUM
    density; the native object is a discrete step lattice, and the continuum
    shape factors may be the wrong class".
  * computations/coulomb_energy.py -- the R0_FM comment block repeats the same
    over-claim.
Both left for the sweep's result so they are corrected once, with the full
picture, rather than twice.
