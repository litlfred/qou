---
# qou-6au4
title: 'RESULT: the mu-p tension is already convention-D — re-deriving the pins is a no-op'
status: completed
type: task
priority: normal
created_at: 2026-08-24T20:12:01Z
updated_at: 2026-08-24T20:12:40Z
---

## The question

Convention D became canonical on 2026-08-15; `z` moved 0.4993 -> 0.6127
(+22.70 %) and alpha* moved 14.741 % as a direct consequence (bean qou-2zjp).
So: does the mu-p tension (11.537118 ppb in q0, ~240 ppb in m_p) survive
re-derivation under D, or is it a convention-C artifact?

## Answer: it is ALREADY the convention-D number. Nothing to re-derive.

**The muon pin has no Markov parameter.**

    q = 1 / (1 - sqrt( Vol(4_1) / (m_mu/m_e) ))

Vol(4_1) = 2*Cl_2(pi/3) is a hyperbolic volume; m_mu/m_e is CODATA. No braid,
no trace, no z. Convention-independent in the strongest sense -- the question
does not arise.

**The proton pin's closed-form trace is already D.** Its solver uses

    |tr_M(beta_Bor)| = (4 + h^2 - 3h^4 - h^6)/(h^2 + 4),   h = q - 1/q

for beta_Bor = (s1 s2^-1)^3 in B_3. I computed the Ocneanu trace of that braid
in H_3(q) with z SYMBOLIC -- algebra built from sigma^2 = (q - 1/q) sigma + 1,
the braid relation, sigma^-1 = sigma - (q - 1/q), and tr(x s2 y) = z tr(xy) --
then substituted each convention:

    D  z = q^3/(q^2+1)   raw(z) - closed_form  ==  0   exactly, all q
    C  z = sqrt(q)/(q+1) raw(z) - closed_form  ==  nonzero, half-integer powers

The D result is a symbolic zero from sympy.simplify, not numerical agreement.
Numerically at the proton pin: closed 0.99856216383679, D 0.99856216383679,
C 0.99836662258572.

The half-integer powers in the C residual are the structural tell: C is
z = sqrt(q)/(q+1), so any C-frame closed form in h = q - 1/q must carry sqrt(q).
This one does not, and could not.

## What this changes

CLOSED: "re-derive the two q0 pins under convention D". No-op. I had
recommended exactly this an hour earlier; the premise was wrong.

STRENGTHENED: the tension is convention-independent, so it cannot be explained
away as an artifact of a superseded trace convention. That escape route is
measured shut, which makes it a better target than it was.

UNCHANGED: irreducibility, the ~240 ppb floor, and the rule that fitting below
the floor models the tension as signal. Also unchanged: the proton formula's
own ~6.7 % formula-to-exact gap, which is four orders of magnitude larger than
the tension sitting on top of it and is where the physics work actually is.

## The generalisable bit

"Derived before the C->D commit" is NOT the same as "C-frame". A quantity is
convention-dependent only if z reaches its arithmetic. The first test is a
timestamp and answers nothing; the second is decidable in closed form and took
one symbolic substitution. Same distinction that separated the 4 genuinely
stale producers from the 1 false positive in qou-2zjp's candidate set.

Audit: docs/audits/2026-08-24-mu-p-tension-is-already-convention-d.md
