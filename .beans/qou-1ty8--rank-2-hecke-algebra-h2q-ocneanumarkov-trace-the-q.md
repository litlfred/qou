---
# qou-1ty8
title: 'Rank-2 Hecke algebra H2(q) + Ocneanu/Markov trace — the q!=1 non-degenerate witness (PR #7203)'
status: completed
type: task
priority: normal
created_at: 2026-09-12T07:46:05Z
updated_at: 2026-09-12T07:46:06Z
---

Delivered PR #7203, branch claude/hecke-markov-functional-2026-09-12, file
content/quantum-observable-universe/lean/QOU/MathlibExt/HeckeRankTwoMarkov.lean.

Built the single-generator Hecke algebra Hecke2 = R[sigma]/(sigma^2 = h*sigma + 1)
as a rank-2 free R-algebra (hand-built CommRing + Algebra, Dioph pattern), with
the Ocneanu/Markov trace tr(a + b*sigma) = a + z*b as a genuine R-linear map.

VERIFIED (lean-verifier, lean-direct v4.24.0, restored cache, -DautoImplicit=false
-s 65536, union-mirror, harness self-checked honest): exit 0, sorry-free, standard
axioms only (propext/Classical.choice/Quot.sound), all 12 public theorems. HEAD
c30bb98e0 (verified at 22a3958f5; final commit removes only proven-unreachable
tactics). Fully lint-clean.

Proves: sigma^2 = h*sigma + 1; sigma a unit (sigma^-1 = sigma - h); tr(1)=1,
tr(sigma)=z, tr(sigma^-1)=z-h; trace property T1; Markov T3/T3' on H1=R*1;
NON-DEGENERACY: markovParam_ne_iff (z != zinv <-> h != 0) and ocneanuTrace_mul_defect
(tr(sigma^2)-tr(sigma)^2 = h*z+1-z^2 = the Hecke quadratic, so non-multiplicative
off its roots) + exists_nonmultiplicative (concrete Q witness).

WHY: the abstract MarkovTrace functional (OcneanuTrace.lean) had two concrete
instances, both degenerate for the q!=1 question: unitMarkovTrace (algebra-trivial)
and the symmetric-group tower witness qou-fq1i (q=1, h=0, z=0). This is the q!=1
witness where the quadratic relation bites. It is free of rank 2 = 2!, so it is
a genuine full-rank H_2 -- the non-vacuous witness qou-nkd8 asks for (at n=2),
NOT a rank-1 model that satisfies the relations vacuously.

DOES NOT CLOSE (still open, by design -- single generator can't instantiate the
infinite MarkovTrace tower): qou-301d (Jones/Markov multiplicativity under the
full tower) and qou-08a2 (the non-commutative H_inf(q) tower + SandwichReduces at
q!=1, by braid rewriting rather than permutation support). Those remain the epic.
Links: qou-fq1i (q=1 tower witness, complementary), qou-nkd8 (rank/vacuity),
qou-301d, qou-08a2.
