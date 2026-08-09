---
# qou-u2jg
title: 'KEYSTONE: convention D is the UNIQUE non-trivial Markov trace on H3 killing the antisymmetriser -- z is free at n=2, forced at n=3'
status: in-progress
type: task
priority: normal
created_at: 2026-08-09T16:17:25Z
updated_at: 2026-08-09T16:18:13Z
---


Branch: claude/anchor-followups-2026-08-08.
Lean: QOU/QBeta/TemperleyLiebTower.lean, section ConventionPinning. Sorry-free,
lake build exit 0 no warnings, #print axioms clean on all six theorems
(qint_three_term_pair needs only [propext, Quot.sound]).

## THE RESULT

Impose the three normalisations a Markov trace on H_3(q) must satisfy, in the
Wedderburn basis, with r a formal inverse for q:

  tr(1)      = y_(3) + 2 y_(2,1) + y_(1^3)              = 1
  tr(sigma)  = q y_(3) + (q-r) y_(2,1) - r y_(1^3)      = z
  tr(s0 s1)  = q^2 y_(3) - y_(2,1) + r^2 y_(1^3)        = z^2

Three linear equations, three unknowns. Eliminating and factorising:

  y_(1^3) * (q^2+1)(q^4+q^2+1)  =  q^2 (z - q) (z(q^2+1) - q^3)

So for q > 0 the antisymmetriser dies at EXACTLY TWO values of z:

  z = q               the TRIVIAL branch
  z = q^3/(q^2+1)     CONVENTION D

and z_eq_q_forces_trivial shows the first collapses everything:
y_(3) = 1, y_(2,1) = y_(1^3) = 0 -- the one-dimensional character, no
mixed-symmetry block, hence no isospin structure at all.

  ==> CONVENTION D IS THE UNIQUE NON-TRIVIAL MARKOV TRACE ON H_3(q) WHOSE
      RADICAL CONTAINS THE THREE-STRAND ANTISYMMETRISER.

Convention C is now excluded BY DERIVATION rather than by owner ruling:
z = 1/(q^1/2+q^-1/2) is neither root, which is exactly why y_(1^3) = 0.0227449
there and why C's Gram form is non-singular.

## WHY THIS IS THE KEYSTONE

qou-8iru established H_n/rad = TL_n by MEASUREMENT (n = 2..7, residual
1.34e-51). This DERIVES the n=3 case and makes it a characterisation, not an
observation. The TL identification stops being "what the numbers happen to do"
and becomes "what D is defined by".

## IT COMPOSES WITH THE SIBLING'S WORK -- PR #4857, branch
## claude/post-drain-audit-8hj2

QOU/Hecke/MarkovTraceH2.lean says, correctly, that its z CANNOT be pinned at
n = 2: the class constrains z only through trace_gen, so markovTraceH2 is a
`def` rather than an `instance` because "an instance would have to invent a
value". True at two strands -- H_2(q) is commutative, has one generator, and
every z is admissible.

THIS BEAN SUPPLIES THE MISSING PINNING, and it first becomes available at THREE
strands: z is free at n=2 and forced at n=3, the moment there is a three-row
partition whose weight can be asked to vanish. Their instance supplies the
algebra; this supplies the parameter. Clean division of labour, no overlap.

## DEFECT IN THE SIBLING'S NEW CODE -- flag, do not edit their branch

QOU/Hecke/MarkovTraceH2.lean, written 2026-08-09, says:
  "The mathematical Markov parameter is z = 1/(q^{1/2} + q^{-1/2})"
That is CONVENTION C, named as "the mathematical" parameter, in a file created
the same day the owner excised C. The CODE is convention-agnostic and correctly
so (z is an arbitrary class field) -- the defect is in the PROSE, and it is
exactly the drift docs/coordination/trace-convention-registry.md exists to stop.
It is also fresh drift, which means the registry rule is still being violated by
new work, not just by legacy. Reinforces detangler decision 8: the rule is
enforced by nothing.

## CHERRY-PICK VERDICT: NOTHING NEEDED

My layer is instance-free by construction -- qint_three_term_pair takes
(q r X Y : R) with q*r = 1 and no algebra structure at all, so every theorem
here applies to their H3A/H4A the moment either branch merges. Cherry-picking
253 files into a checkout with an 11-agent workflow actively editing it would be
reckless and buys nothing.

## COROLLARIES, now derived rather than measured

  y_(2,1) = q^2/(q^2+1)^2   = 1/[2]_q^2   = mu_-
  y_(3)   = (q^4+1)/(q^2+1)^2 = [4]_q/[2]_q^3
  y_(2,1) also = -q(z-q)(qz+1)/(q^4+q^2+1) as a function of z

## NEXT ON THE TL / H_k, k >= 4 ARC

  [ ] T1. Generalise the normalisation to all n: [2]^n = sum_k m_k [n-2k+1]
      with m_k = C(n,k) - C(n,k-1), by induction on the three-term recursion
      already proved. Upgrades the n=3,4 arithmetic to every strand count.
  [ ] T2. sum_k (C(n,k)-C(n,k-1))^2 = Catalan(n). Pure combinatorics, no q.
      Gives dim TL_n for all n rather than n = 3,4,5 as arithmetic.
  [ ] T3. The radical is a two-sided IDEAL. State abstractly: in an algebra
      direct sum (+)_lambda A_lambda, any sub-sum is a two-sided ideal. No Hecke
      structure needed, so it does not collide with the sibling.
  [ ] T4. The quotient form is positive DEFINITE, not merely PSD.
  [ ] T5. Propagate the n=3 vanishing UP the tower: if y_(1^3) = 0 at n=3 then
      the ideal it generates is in the kernel of tr_M at every higher n, by the
      Markov property. That would derive the >= 3-row vanishing at all n from
      the n=3 case, replacing the citation to Wenzl.
  [ ] T6. TL_n's diagram-basis Gram determinant is KNOWN in closed form
      (Di Francesco-Golinelli-Guitter meander determinant). If the star form
      equals it, positivity is a CITATION, not a proof obligation. Check first.
