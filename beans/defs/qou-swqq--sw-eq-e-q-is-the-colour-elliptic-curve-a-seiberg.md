---
# qou-swqq
title: 'SW = E_q: is the colour elliptic curve a Seiberg-Witten curve? (NOT new — the 2026-06-08 audit already names it; disc(E_q) is degree 12, irreducible, 0 real roots)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-colour
created_at: 2026-08-30T02:45:00Z
updated_at: 2026-11-16T17:50:00Z
parent: qou-8lxd
---

## Status Update (PR `litlfred/qou#8140`, `468e210bfac6c8438bd4b6331f2fa807f91853e8`)

Claimed `in-progress` under `Q-8LXD-1` alongside `qou-q6lw`, `qou-tekm`, `qou-pa2f`, and `qou-v5fp`. Kept `in-progress` per owner decision policy.

Owner proposal, 2026-08-30, branch claude/arithmetic-upgrade-pending-543abd (PR #6052).
Recorded with its red-team per the standing critical-distance license.

CORRECTION TO THIS BEAN'S FIRST REVISION. It was first written as "SW = Q_q" and
roasted on that reading. Q_q in this corpus is the q-deformed QUANTUM PRESSURE of
rem:madelung-fluid, a scalar field -- the wrong object. The intended claim is E_q,
the COLOUR ELLIPTIC CURVE of prop:color-elliptic / descartes-elliptic-curve. Most of
the first roast was aimed at the wrong target and is retracted below; the incidental
Q_q finding is kept at the end because it is true and was measured.

## THIS IS NOT NEW — cite the audit, do not re-declare it open

docs/audits/2026-06-08-nonabelian-stokes-sw-period-already-live.md, section "The one
genuinely open piece", already states it:

    "E_q = the Seiberg-Witten curve. lambda_SW lives on S_c = P^1 with the elliptic
     structure of descartes-elliptic-curve (E_q). Verifying E_q = a Seiberg-Witten
     curve (match j-invariant / period lattice; the (m,n) torus-knot winding = the
     period cycles) is the remaining non-trivial identification."

So this bean is a MEASUREMENT against a live open item, not a new declaration.

## The object

E_q, over Q(sqrt q) with s = sqrt q:

    y^2 = x^3 + p x + r
    p = (2s^4 + s^3 - 2s^2 - s + 2) / (3 s^2)
    r = 5(s^2 + s - 1)(4s^4 - s^3 - 4s^2 + s + 4) / (27 s^3)

## MEASURED THIS SESSION (sympy exact, no float in the algebra)

disc(E_q) = -16 * N(s) / s^6  with

    N(s) = 16s^12 + 24s^11 - 61s^10 - 70s^9 + 135s^8 + 114s^7 - 164s^6
           - 114s^5 + 135s^4 + 70s^3 - 61s^2 - 24s + 16

  * N is IRREDUCIBLE over Q (sympy factor_list: single factor, multiplicity 1).
  * N has 12 roots, and ZERO of them are real (nroots, 25 digits).
  * Symmetry: s^12 * N(1/s) = N(-s)  exactly. So the discriminant is invariant under
    s -> -1/s, i.e. the bar-involution q -> 1/q composed with a branch flip.
  * E_q is SMOOTH at the substrate: N(sqrt q0) = 25.912... != 0 at the proton pin.
  * j(E_q) = 256 (2s^4 + s^3 - 2s^2 - s + 2)^3 / N(s);  j(q0) = 129.8603466...

## ROAST (against the E_q reading)

1. THE FIBRE COUNT IS THE OBSTRUCTION, AND IT IS 12 vs 2. The SU(2) N=2 SYM
   Seiberg-Witten curve is CHARACTERISED by having exactly TWO singular fibres on the
   Coulomb branch -- the monopole and the dyon, where BPS states go massless. That is
   not decoration; it IS the physics of Seiberg-Witten. E_q's discriminant has TWELVE
   roots. For the identification you need a principled reason why 12 collapses to 2.

2. AND IRREDUCIBILITY BLOCKS THE OBVIOUS ESCAPE. The natural move is "only two of the
   twelve are the physical ones". N is irreducible over Q, so its Galois group acts
   transitively on the roots: NO rational condition distinguishes a sub-pair. Any
   selection of two must come from outside Q -- which is an extra input needing its
   own justification, not a free choice.

3. ZERO REAL ROOTS vs A REAL COULOMB BRANCH. All 12 singular fibres sit at complex s.
   The SW u-plane singularities are at u = +-Lambda^2, real for real Lambda^2. So the
   q-family is nowhere singular over the reals while the SW family's whole content is
   its real singularities. NOTE THE SCOPE: this does not by itself refute "E_q is a SW
   curve", because E_q is a family over the SUBSTRATE modulus q and SW is a family
   over the COULOMB modulus u -- different base parameters. It refutes the naive
   reading "the q-family IS the u-family", and it means any q <-> u map is not
   real-to-real.

4. NAMING THE MODULUS MAP IS THE ACTUAL WORK. E_q is a one-parameter family in q; SW
   is a family in u with a scale Lambda. Until someone writes the map q <-> u (and
   says where Lambda comes from), "E_q = the SW curve" has no content to check. This
   is the (a)-scope gap, and it is where a session should start.

5. j-MATCHING IS NECESSARY, NOT SUFFICIENT -- AND WEAKER THAN IT LOOKS. The audit
   proposes matching the j-invariant. Equal j means isomorphic over the algebraic
   CLOSURE only; it leaves the quadratic twist free, and the twist is exactly what
   records which cycle is the monopole. A j-match would be suggestive and would settle
   nothing.

6. DEFINED OVER Q(sqrt q), NOT Q(q). The coefficients need s = sqrt q. So the
   sqrt-branch is entangled with the bar-involution -- consistent with the measured
   s -> -1/s symmetry above, and it means the SW side must be told what the branch is.

7. SHARING "IS AN ELLIPTIC CURVE IN ONE PARAMETER" IS NOT EVIDENCE. There are a great
   many such families. The identification must be FORCED by structure -- the audit's
   own candidate is "(m,n) torus-knot winding = the period cycles" -- not merely
   permitted by both objects being genus 1.

## What would make it real

The audit's structural candidate, not the j-match: show the (m,n) torus-knot winding
reproduces the SW period CYCLES, with an explicit q <-> u map, and account for the
12 vs 2 fibre count. Absent that, this stays a resemblance.

Literature is HELD, not needed from outside: library/arxiv-alg-geom-9705010v1
(Donagi, SW integrable systems), arxiv-hep-th-9408099v1 (SW original),
arxiv-hep-th-0206161v1 (Nekrasov), arxiv-1908.07065v3 (quantum SW curve),
pjm-v154-n1-p09-s and sigma12-065 (Bring period matrix, both).

Default if nothing happens: nothing changes. No content block, no Lean, no compute
depends on the identification; the audit already records it as open and it stays open.

## RETRACTED: the first revision's Q_q roast

Aimed at the wrong object. Of its six objections, four DO NOT APPLY to E_q:
  - "type error, field vs number" -- E_q vs SW curve is curve vs curve, type-correct;
  - "rho-dependence" -- E_q does not depend on a fluid solution;
  - "refuted at q=1 because Q_q -> 0 while a_D^(n) = I(n)/n >= 1" -- that is a fact
    about the quantum pressure, NOT about E_q. E_q does not vanish at q=1. THE
    KILLER OBJECTION EVAPORATES under the corrected reading;
  - "hbar_q^2 on opposite sides" -- a Q_q bookkeeping point.
Two survive in modified form and are kept above as 7 and (in the Omega-background
sense) a caution on any quantum-SW-curve route.

INCIDENTALLY ESTABLISHED AND STILL TRUE: SW period != Q_q under the literal reading,
since Q_q -> 0 as q -> 1 while a_D^(n)|_{q=1} = I(n)/n >= 1 is positive and grows at
least factorially (QOU.Mass.SWPeriodSuperExponential, PR #6052). Also corpus-grepped:
SW and Q_q meet NOWHERE in the corpus. Recorded in case anyone proposes that reading.
