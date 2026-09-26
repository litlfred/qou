---
# qou-g1m8
title: 'Route E screened: the ambient outer automorphism does not decide the Sym2 gate'
status: completed
type: task
priority: normal
created_at: 2026-09-04T23:16:00Z
updated_at: 2026-09-04T23:16:36Z
---

SETTLED 2026-09-04. Route E (PGL(3) higher Teichmuller, epic qou-2q85) is still
LIVE -- but its stated rationale does not survive the screen, and the screen
did not exist when the route was assessed.

## The screen it now has to pass

Sym2GateFSTrichotomy.gate_forces_complex_of_dim_three (sorry-free, 2026-08-26):
a three-dimensional object passing the Sym^2 gate MUST contain a complex-type
irrep (FS = 0, X not iso Xbar). Real and quaternionic constructions excluded as
a class -- real multiplicities forced to zero, quaternionic dimensions even,
total even, 3 is odd.

## What the existing audit claimed

docs/audits/2026-08-04-pgl3-higher-teichmuller-assessment.md section 2c:
"The resulting 3-dim fundamental would be non-self-dual (PGL(3) is rank 2 with
non-trivial outer automorphism)."

Premise is about the AMBIENT GROUP; conclusion is about ONE REPRESENTATION.
PGL(3) carries its outer automorphism whatever rho_3 does. SO(3) inside
PGL(3,R) has a three-dimensional standard rep of REAL type, killed by
real_triple_fails_gate in one line -- while PGL(3) still has the outer
automorphism. This is the arity/scope conflation of AGENTS.md "Grep the claim
SHAPE", applied to a POSITIVE claim rather than a negative one.

## Lean

QOU/Eightfold/AmbientInvolutionDoesNotDecideType.lean -- 12 decls, sorry-free,
lean-direct exit 0 in 3.5s, axioms [propext, Quot.sound] (not even
Classical.choice). Consumes the corpus's own gate model rather than restating it.

  fsType_not_determined_by_dual   over ONE fixed fixed-point-free duality
                                  involution, two three-dimensional candidates:
                                  one passes the gate, one fails it
  selfDual_candidate_not_three    THE SCREEN, in the form a route can be held
                                  to: all-self-dual candidate cannot be
                                  three-dimensional and pass, whatever the
                                  ambient outer automorphism does

## NOT a refutation -- scope-(a) throughout

Removes a reason for confidence, replaces it with a checkable obligation:
exhibit rho_3 : pi_1(S^3 minus K) -> PGL(3,C) with rho_3 not iso rho_3-bar (an
image not conjugate into a real form), for the knots the particle dictionary
uses.

ONE CONSEQUENCE PRUNES HALF THE ROUTE: the classical higher-Teichmuller object,
a PGL(3,R) Hitchin representation, lands in the self-dual sector and is
excluded. The surviving branch is PGL(3,C) gluing equations -- which is the
branch the corpus actually holds sources for.

## Correction to qou-960k's inference (not its count)

Re-measured 2026-09-04:
  35   library dirs on "quantum Teichmuller"  = the RANK-1 PGL(2,C)
       quantisation the corpus already uses, NOT rank-2 material
   4   library/*/sections/ dirs on Fock-Goncharov (arxiv-1204.4824v2,
       arxiv-1207.6711v1, arxiv-2304.12545v1, hyperbolicandneumann)
   1   on-point for PGL(n,C): arxiv-1207.6711v1 = Garoufalidis-Thurston-Zickert,
       "Gluing equations for PGL(n,C)-representations of 3-manifolds"
       (109 occurrences of PGL(n, C); the other three mention it once each)

So the rank-2 route has ONE substantive held source, not 35. qou-960k's count
was right; the inference from it was not.

FALSE POSITIVE TO NOT REPEAT: a summary.json-level grep for "Fock" returns
arxiv-1106.2975v1 (Polyanalytic Ginibre Ensembles -- Fock SPACE) and
arxiv-1611.09182v1 (Standard model physics from an algebra?). I made that
misread before running the sections/-level grep for the full name. Run the
sections/ grep.

NOT MEASURED: library/*/ocr/ (25 dirs, sections-grep blind to them) or the PDFs.
corpus_search (path 0) unavailable for a fifth session.

## Next on route E

A COMPUTATION, not a derivation: PGL(3,C) representations of the trefoil,
figure-eight and Borromean complements, Frobenius-Schur type read off each. That
is exactly the 2026-08-04 audit's own section 3 recommendation, and it is now the
only thing route E waits on. Its two other recorded obstructions stand and are
untouched here: not every knot complement admits a PGL(3,C) structure, and the
trefoil complement is Seifert-fibred rather than hyperbolic.

Audit: docs/audits/2026-09-04-route-e-screened-against-the-trichotomy.md
