---
# qou-we9a
title: 'GAP: pivotal transport identity qDimObj(Xᘁ) = leftQDim X — rtqd''s last residual'
status: completed
type: task
priority: normal
created_at: 2026-08-26T17:01:29Z
updated_at: 2026-08-26T17:29:57Z
---


## Status 2026-08-26: the GOAL is closed, this identity is NOT

I opened this to prove the pivotal transport identity qDimObj (Xdual) = leftQDim X, as
rtqd's last residual. That is NOT what happened, and the distinction matters.

rtqd's actual goal -- qDimObj (Xdual) = qDimObj X -- is now proved outright by a route
that does not pass through transport at all (see rtqd, and
QOU/MathlibExt/BraidedQuantumDimension.lean). So this bean is no longer BLOCKING anything.

The transport identity itself remains unproved. It stays a hypothesis of
qDim_conj_of_pivotalTransport and friends, which remain valid conditional theorems. Worth
having on its own account -- it relates the two traces, which the unconditional route says
nothing about -- but it is no longer on anyone's critical path.

Left OPEN rather than scrapped: it is a real statement, still unproved, and the file that
carries it still carries it as a hypothesis.



## RESOLVED 2026-08-26 -- characterised, not proved, and that IS the answer

The transport identity qDimObj (Xdual) = leftQDim X is NOT unconditionally provable, and
this bean now says exactly why rather than leaving it open indefinitely. Three theorems,
all sorry-free, in KeystonePivotalSpherical.lean:

1. transport_iff_spherical -- TRANSPORT AND SPHERICALITY ARE EQUIVALENT, unconditionally,
   modulo the conjugation symmetry that closed rtqd. KeystonePivotalSpherical presents
   them as two independent classical inputs. They are not independent: each follows from
   the other in one rewrite. The residual was never two conditions of which one might
   fall -- it is ONE condition wearing two names.

   Consequence: transport cannot be proved unconditionally, because sphericality cannot.
   The left and right traces genuinely differ in a general braided rigid category; a
   category where they agree is what "spherical" NAMES.

2. pivotalTransport_of_symmetric -- transport holds outright in any SYMMETRIC right-rigid
   category, from the corpus's own leftQDim_eq_qDimObj_of_symmetric. The first
   unconditional case.

3. qDim_twist_eq_leftQDim -- THE EXACT OBSTRUCTION. Inserting the twist factor
   theta_{Xdual} tensor theta_X into the right trace produces the left trace on the nose.
   Proof: the Joyal-Street balancing axiom turns the double braiding into
   theta_{Xdual tensor X} dressed by the component twists, then naturality of theta
   against eta >> beta-inverse absorbs the whole theta_{Xdual tensor X} since theta_unit
   is the identity.

   This kills the obvious next move. Now that a ribbon structure exists one wants the
   classical `ribbon => spherical`. IT DOES NOT APPLY. That theorem is about the TWISTED
   trace, in which theta is already inserted; qDimObj and leftQDim are the TWISTLESS
   traces, and between those the twist is not a normalisation but the ENTIRE difference. A
   ribbon structure gives theta_{Xdual} = (theta_X)dual, relating the factor's two halves
   -- it does not make the factor vanish.

Scope (a) on point 3: a statement about THESE two definitions, not a claim that no twisted
formulation closes.

NON-VACUITY: a mutant with the twist factor deleted from the statement fails to compile, so
the factor is load-bearing rather than decorative.
