---
# qou-u2jg
title: 'KEYSTONE: convention D is the UNIQUE non-trivial Markov trace on H3 killing the antisymmetriser -- z is free at n=2, forced at n=3'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T16:17:25Z
updated_at: 2026-11-16T21:54:00Z
parent: qou-rtxm
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

## UPDATE 2026-08-09 -- pushed as far as it goes without the sibling

Commit 10b8dac1d. All sorry-free, lake build exit 0 no warnings, axioms clean;
traceRadical_two_sided depends on NO AXIOMS AT ALL.

### T-list status

  [x] T3. THE RADICAL IS A TWO-SIDED IDEAL. traceRadical_two_sided, from
      associativity and cyclicity alone -- cyclicity used in exactly one place,
      the left-multiplication direction. This is what licenses "work in TL_n" as
      an ALGEBRA statement rather than a vector-space one.
      zero_weight_block_erasable made the quotient harmless; this makes it legal.

  [x] T5. WENZL IS NOW A COROLLARY, NOT A CITATION. vanishing_step +
      vanishing_all_levels derive the >= 3-row vanishing at all n >= 3 from the
      n = 3 pinning. Three inputs, all measured this session:
        * branching coherence, worst residual 1.34e-51 at n = 2..6
        * nonnegativity, zero negative weights at every n tested
        * every >= 3-row shape at n+1 covers a >= 3-row shape at n, for
          n+1 >= 4 -- exhaustive at n+1 = 4,5,6,7, no exceptions. The sole
          exception is (1^3) at n = 3, which is exactly why 3 is the base case.
      Given those the step is one line: a vanishing sum of nonnegatives has
      every term zero.
      HONESTY: the combinatorial input is a HYPOTHESIS in the Lean signature,
      not a formalised fact about Young diagrams. Verified by exhaustion, not
      proved. Stated as a hypothesis deliberately so the dependency is visible
      rather than buried in a sorry.

  [ ] T1. General normalisation [2]^n = sum_k m_k [n-2k+1], m_k = C(n,k)-C(n,k-1).
      OPEN. Needs the multiplicity bookkeeping; n = 3,4 stand as ring identities.
  [ ] T2. sum_k m_k^2 = Catalan(n). OPEN, same reason. Partially mitigated:
      counts_are_catalan now checks 2,5,14,42 against Mathlib's own `catalan`
      rather than this file's arithmetic table, so "= Catalan" is no longer the
      file's claim about itself.
  [ ] T4. Quotient form positive DEFINITE. Gated on T6.
  [~] T6. Meander / TL Gram determinant -- workflow wz3teraa6 in flight on
      whether this closes T4 by CITATION. It also checks a suspected corpus
      confusion: 1/[2]_q = 0.497290545604916 vs convention-C z = 0.499320334,
      only 0.4 % apart and easy to conflate, on DIFFERENT elements (the TL
      generator e_i vs the Hecke generator sigma_i).

### NEW, beyond the T-list

  * THE SHARPEST FORM. conventionD_unique_nontrivial:

        IsConventionD q z   <->   y_(1^3) = 0  AND  y_(2,1) != 0

    Right-hand side = "the trace factors through Temperley-Lieb AND is not the
    one-dimensional character". D is exactly that, nothing else is. This is the
    statement to cite; everything else in the section is scaffolding for it.
  * not_conventionD_of_antisym_survives -- convention C excluded BY DERIVATION,
    not by owner ruling: y_(1^3) = 0.0227449 there, so C is not D.
  * IsConventionD as a consumable predicate (multiplicative -- no q != 0, no
    division). This ANSWERS Ask 3 to the sibling by building it rather than
    negotiating it: nothing was placed in QOU/Hecke/, they take it or ignore it.
  * The closed forms DERIVED rather than measured:
        y_(2,1) (q^2+1)^2 = q^2      y_(3) (q^2+1)^2 = q^4 + 1

### Coordination

Posted to litlfred/qou#4857 twice: intent (comment 5232517970) and progress with
cherry-pick pointers (5232610373). Ledger at
docs/coordination/hecke-tower-and-trace-parameter.md. Subscribed to the PR.
Asks 1 (convention-C prose in their MarkovTraceH2) and 2 (qou-awp7 via the H4A
Wedderburn isomorphism) are still open with them.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-09 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-16 — Convention D H_3(q) Keystone Uniqueness (`QOU.Foundations.ConventionDKeystoneTraceTower`, PR #8214)
- Formalized `h3AntisymWeightNum`, `h3MixedWeightFactor`, `h3MixedWeightConventionDNum`, `h3SymWeightConventionDNum`, `h3_antisym_and_mixed_vanish_at_trivial_branch`, `h3_antisym_vanishes_at_conventionD`, and `conventionD_h3_normalisation_identity` in `folio/quantum-observable-universe/lean/QOU/Foundations/ConventionDKeystoneTraceTower.lean` (pure Lean 4 core, generic `CommRingOps R` per §7c, `0` `sorry`, `0` warnings, `0` vacuity audit hits; wired into `QOU.lean`).
- Commit: `7cc3c04b0719e92286ff6279855cbf3f0b9a7826` | PR: `https://github.com/litlfred/qou/pull/8214`
- Kept at `status: in-progress` per merge-manager protocol.
