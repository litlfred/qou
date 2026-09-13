---
# qou-zfs6
title: 'Discriminating observable for route 2: Mobius invariance / FHW bound / minimiser as Lean gates'
status: in-progress
type: task
priority: normal
created_at: 2026-09-13T11:56:17Z
updated_at: 2026-09-13T12:41:40Z
---

## LANDED: Mobius invariance IS the discriminator, and it FORCES the kernel

Section 7 of QOU/MobiusMutualChannel.lean. 4 declarations, all
[propext, Classical.choice, Quot.sound], no sorryAx; whole file 29/29 clean,
lean -DautoImplicit=false -s 65536 exit 0, zero warnings.

WHY THIS ONE AND NOT THE OTHER TWO. Option C named three candidate gates.
Formalize-first triage against what LinkEmbedding actually carries (sep, a
real-valued separation; no ambient geometry, no derivative data, no crossing
number):

  Mobius invariance    STATABLE. The inversion transformation law is a
                       statement about DISTANCES, which is the language sep
                       already speaks. Done.
  FHW crossing bound   NOT STATABLE. Needs c(K); LinkEmbedding carries no
                       crossing data, so any Lean statement of it here would be
                       true by vacuity -- the dressed-up tautology the
                       MobiusEnergy roast found four of. It is also a bound on
                       the SELF energy (qou-bn8e's object), not the mutual
                       channel.
  minimiser existence  NOT STATABLE HERE. Needs function-space compactness and
                       lower semicontinuity, i.e. O'Hara's theorem -- the exact
                       analysis the section-1 prune established the mutual
                       channel does not need and does not have.

So C delivers ONE of three, and the other two are recorded as not-statable
rather than skipped.

PROVED (sorry-free):
  mobiusInvariant_forces_inverse_square   f Mobius-invariant against the
      arclength density  ==>  f d = f 1 / d^2. The exponent is not an ansatz
      and not fitted: it is the unique orientation-blind kernel compatible with
      the symmetry. THIS is the discriminating content -- sections 1-6 admit a
      class, this cuts it to a single ray.
  inverse_square_mobiusInvariant          the converse, so the above is not
      vacuous.
  flat_measure_not_mobiusInvariant        the FLAT parameter measure ds dt is
      NOT invariant (witness: chord 1, centres 2 and 1 -> kernel 4 vs 1).

HOW IT COMPOSES WITH SECTION 6. Section 6 proved O2 against an ARBITRARY
density w and said honestly that LinkEmbedding supplies nothing selecting one.
Section 7 selects it: the arclength Jacobians 1/|gamma-a|^2 are exactly what
cancel the chord factors, and the flat measure provably fails. So the free
parameter section 6 left is CLOSED by symmetry, not by choice -- no new degree
of freedom enters.

ASSUMED, cited, not derived: the two classical inversion laws,
  |I(x)-I(y)| = |x-y| / (|x-a|*|y-a|)   and   |I(gamma(s))'| = 1/|gamma(s)-a|^2
([ohara1991], [freedman1994]).

NOT CLAIMED: that the ENERGY (the integral) is Mobius invariant. What is proved
is pointwise invariance of integrand-times-density; promoting that to the
integral needs a change-of-variables argument not done here.

## 🛑 THE ONE LOOSE END, and it is in the hypothesis

MobiusInvariantKernel quantifies over UNCONSTRAINED positive triples
(d, da, db). A realisable triple is three distances among three points of R^3
and must satisfy the triangle inequalities. The witness the proof uses,
(1, 1/d, 1), needs 1/d <= 2, i.e. d >= 1/2 -- so at small chord the conclusion
rests on triples the geometry never presents. da = db = 1/sqrt(d) is realisable
for d <= 4 and fails past it, so neither single family covers (0, inf).

Whether the characterisation survives on realisable triples only is OPEN. It is
not closed by rephrasing: the restricted hypothesis is genuinely weaker. The
caveat is in the theorem's own docstring so it cannot be cited without it.
DO NOT cite this as "the exponent is forced by geometry" -- it is forced by
invariance over all positive triples.

BEAN STAYS OPEN on that sub-item.

MERGED to main as 03ed1c3c8e (PR #7299, issue #7298). Bean STAYS OPEN per AGENTS.md 13a: the realisable-triples question is an open mathematical sub-item, not a recording task. Landing the theorem is not closing the question.
