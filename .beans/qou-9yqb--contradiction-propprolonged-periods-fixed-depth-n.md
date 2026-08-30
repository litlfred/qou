---
# qou-9yqb
title: 'CONTRADICTION: prop:prolonged-periods-fixed-depth (n-independent kernel) is inconsistent with a_D^(n)=I(n)/n growing super-exponentially — at most one holds'
status: todo
type: task
priority: normal
created_at: 2026-08-30T03:16:24Z
updated_at: 2026-08-30T03:17:39Z
parent: qou-mhj9
---

VERIFIED against primary sources 2026-08-30 (not from a sibling's prose).

## The two claims

(1) prop:prolonged-periods-fixed-depth (content/.../mass-theory/), verbatim:
    "a_D^(n+d) = SUM_{j<d} c_j a_D^(n+j), with **n-independent** kernel c, for
    every n", d <= rank V <= 2g = 8, derived by Cayley-Hamilton on the
    jet-prolongation operator M acting on the Gauss-Manin period space V.

(2) PR #6052 branch claude/arithmetic-upgrade-pending-543abd,
    QOU/Mass/SWPeriodSuperExponential.lean (sorry-free):
      involution_ratio_unbounded    -- I leaves EVERY geometric class
      factorial_le_involution_two_mul -- n! <= I(2n)
      classical_period_ratio_unbounded
    reading a_D^(n)|_{q=1} = lw(n-1) = I(n)/n via prop:sw-classical-jet-exactness.

## Why they cannot both hold

A linear recurrence with CONSTANT coefficients has solutions
SUM_i p_i(n)*lambda_i^n -- at most exponential growth. Elementary form:
|a_{n+d}| <= (SUM_j |c_j|) * max_{j<d} |a_{n+j}| gives |a_n| <= M*K^n with
K = max(1, SUM|c_j|). Super-exponential growth (ratio unbounded) contradicts it.

THE TELL IS IN THEIR OWN LOAD-BEARING STEP. involution_succ_succ reads

    I(n+2) = I(n+1) + (n+1)*I(n)

-- a depth-2 recurrence whose coefficient (n+1) is n-DEPENDENT, which is exactly
what (1) forbids. The n-dependence is sitting in the coefficient, in plain view.

## What must give (one of)

  a. the identification a_D^(n) = I(n)/n (prop:sw-classical-jet-exactness); or
  b. a_D^(n) = phi(M^n v_0) for a FIXED finite-rank M (prop:mi-sw-abelianisation)
     -- if the periods grow super-exponentially they cannot be the orbit of a
     fixed finite-rank operator, whatever V's rank; or
  c. the "n-independent" in (1).

## Status of each side

(2)'s ARITHMETIC is solid and elementary: involution_ratio_unbounded follows from
the recurrence by omega. But (2)'s IDENTIFICATION is not proved -- their own
docstring says Sum_{lam|-n} f^lam = I(n) (RSK) "is open in the corpus", beans
qou-m3xr and qou-jlam, both todo, both blocked on the missing Mathlib
StandardYoungTableau layer. So route (a) is the cheapest suspect BY THEIR OWN
SCOPE NOTE, not by my preference.

## Relation to what already landed

Merged #6059 QOU/MassTheory/BodyOrderRecurrenceDepth.no_equivariant_prolongation
already recorded that something in this cluster must give, via a DIFFERENT route
(Schur on H1(Bring) = W_(4,1)^+2 forces d <= 2 against a proved d >= 3). This is
a SECOND independent crack in the same proposition, arrived at from growth rather
than from equivariance. Two independent routes now say the fixed-depth picture is
in trouble.

## Next unit (cheap, Lean)

Formalize the elementary exponential bound
  |a_n| <= M * K^n  for any depth-d constant-kernel recurrence
and pair it with a super-exponential hypothesis to give False. That converts this
bean from an argument into a machine-checked incompatibility. It does NOT decide
which of (a)/(b)/(c) is wrong -- that is a corpus judgement.

NOT MINE TO RESOLVE: (2) belongs to #6052. Flagged to them on that PR
(issuecomment-5466412367); they were told explicitly I had not read their Lean at
the time. This bean records the verification I have since done.
