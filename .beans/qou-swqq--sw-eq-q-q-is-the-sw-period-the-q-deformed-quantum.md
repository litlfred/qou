---
# qou-swqq
title: 'SW = Q_q: is the SW period the q-deformed quantum pressure? (literal reading REFUTED at q=1; the WKB reading survives)'
status: todo
type: task
priority: normal
created_at: 2026-08-30T02:47:08Z
updated_at: 2026-08-30T02:47:08Z
---

Owner proposal, 2026-08-30, session on branch claude/arithmetic-upgrade-pending-543abd
(PR #6052). Recorded WITH its own red-team, per the standing critical-distance
license. Read the roast before spending a session on this.

## The two objects

SW side, brings-surface + mass-theory:
    a_D^(n) = contour-integral of lambda_SW^(n) over S_c = 2*pi*i * Sum_p Res_p
    prop:sw-period-residue-sum; conjecturally = lw(n-1), the mean quantum
    dimension (conj #1765, prop:sw-prolongation-period-eq-mean-qdim).

Q_q side, fluid-dynamics/madelung-fluid.md (rem:madelung-fluid):
    Q_q = -(hbar_q^2 / 2) * (Delta_q sqrt(rho)) / sqrt(rho),   hbar_q = 1 - 1/q
    the q-deformed quantum pressure (Bohm potential) in the Madelung split of
    the q-deformed Schroedinger equation.

## Corpus-grep: this identification does NOT exist

Ran the six paths before writing. content/brings-surface x madelung/quantum-pressure:
ZERO. content/mass-theory x same: ZERO. docs/coordination: ZERO. The docs/audits,
computations/ and .beans/ hits are all electron-shell material, not this. So SW and
Q_q genuinely never meet in the corpus, and this is new rather than a
re-declaration. The relevant literature IS held and unused for this:
library/arxiv-1908.07065v3, "Non-perturbative approaches to the quantum
Seiberg-Witten curve".

## Why it is not empty motivation

Quantizing the SW curve gives a Schroedinger-type ODE whose WKB expansion produces
hbar-corrected periods. The Bohm quantum potential IS the leading hbar^2 term of the
Madelung/WKB correspondence. So "the SW period's quantum correction is a quantum
pressure" is a real statement in the real literature, not a pun.

## ROAST — the literal reading is REFUTED, and by a result proved this session

1. TYPE ERROR. Q_q is a SCALAR FIELD Q_q(x,t) on the fluid domain, depending on the
   density rho of a particular solution. a_D^(n) is a NUMBER -- a period of a 1-form
   on a Riemann surface, indexed by jet level n. "SW = Q_q" as written equates a
   field with a number. It is not a conjecture yet; it is a type error. A real
   version must say WHICH functional of Q_q equals WHICH period.

2. rho-DEPENDENCE IS FATAL. Q_q depends on the solution's density profile. SW periods
   depend only on the curve's moduli. The identification would make a
   modulus-determined quantity depend on an arbitrary initial condition. Unless rho
   is canonically fixed -- by what? -- the claim is underdetermined or false.

3. THE q=1 LIMITS POINT OPPOSITE WAYS. THIS IS THE KILLER, and it is checkable
   against the corpus today. madelung-fluid.md states: as q -> 1, hbar_q -> 0 and
   Q_q -> 0. But prop:sw-classical-jet-exactness gives a_D^(n)|_{q=1} = I(n)/n, and
   QOU.Mass.SWPeriodSuperExponential (PR #6052, sorry-free) proves that quantity is
   POSITIVE and grows at least FACTORIALLY (n! <= I(2n)). Concretely a_D^(2) = 1,
   a_D^(3) = 4/3, a_D^(6) = 38/3.
       At q = 1:   Q_q = 0     but    a_D^(n) >= 1.
   So the literal identification is FALSE at the one point where both sides are
   independently known. This is a scope-(b) style exclusion of the LITERAL reading
   -- the invariant cited is the classical-period value, which is proved, not
   measured.

4. hbar_q^2 SITS ON OPPOSITE SIDES. The mass formula carries 1/hbar_q^2
   (m = m_e * Vol * rho / hbar_q^2); Q_q carries +hbar_q^2. A naive identification is
   off by hbar_q^4. Any surviving version must say explicitly which side carries it.

5. SHARING A DEFORMATION PARAMETER IS NOT EVIDENCE. Both objects are "q-deformed and
   carry hbar_q". So does half the corpus. That is a shared parameter, not a shared
   identity, and treating it as support is exactly the numerology the
   canonical-derivation discipline exists to catch.

6. TWO DIFFERENT hbar's WEARING ONE NAME. In the quantum-SW-curve literature the
   quantization parameter is the Omega-background / Nekrasov parameter. Here hbar_q
   = 1 - 1/q is a SUBSTRATE MODULUS. Identifying them is an ADDITIONAL assumption
   with its own burden, not a free consequence of both being called hbar.

## What survives, and what to do

NOT "SW = Q_q". The defensible successor is strictly weaker and differently typed:

    Q_q is the leading hbar_q^2 CORRECTION TERM to the SW period under the
    quantized (WKB) SW curve -- not the period itself.

That is consistent with objection 3, because a correction term is allowed to vanish
at q=1 while the leading period does not. It is the version the held literature
actually supports.

Before any session is spent: (a) fix the type -- name the functional of Q_q and the
period it is compared to; (b) state which hbar is which, per objection 6; (c) check
the hbar_q^2 bookkeeping of objection 4. If (a) cannot be done, the item is not ready
to work and should stay here rather than reaching a content block.

Default if nothing happens: nothing changes. No content block, no Lean, no compute
depends on this; the corpus does not contain the claim and does not need it. It is
cheap to ignore.
