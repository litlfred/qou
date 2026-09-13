---
# qou-pc85
title: 'EM-linking route 2: the MUTUAL O''Hara channel is integrable WITHOUT O''Hara''s theorem — no diagonal singularity, so bounded+measurable suffices (qou-o6ml)'
status: todo
type: task
priority: normal
created_at: 2026-09-13T09:22:10Z
updated_at: 2026-09-13T11:12:39Z
---

## LANDED (PR #7284) — the prune, and it is sorry-free

The mutual O'Hara channel is integrable WITHOUT O'Hara's theorem.

WHY IT LOOKED EXPENSIVE: the DIAGONAL. On one component, as s -> t the ambient
distance goes to zero and 1/|gamma(s)-gamma(t)|^2 blows up; that the intrinsic
subtraction still leaves something finite IS O'Hara's theorem -- analysis, not
infrastructure.

WHY IT IS NOT: qou-o6ml owns only the pairwise/linking channel (the self term is
qou-bn8e's by that bean's own split), and the mutual integrand has NO DIAGONAL --
LinkEmbedding.disjoint says distinct components never meet. So the singular
behaviour that makes O'Hara hard never arises in the channel this bean needs, and
the mutual term is integrable by the ordinary route: bounded + measurable on a
finite-measure domain.

PROVED (6 decls, all [propext, Classical.choice, Quot.sound], no sorryAx):
  mutualIntegrand_le_of_uniformSeparation    the 1/delta^2 bound
  mutualIntegrand_nonneg_of_ne               the lower half
  disjoint_not_imp_uniformSeparation         THE GUARD -- see below
  mutualIntegrand_intervalIntegrable         the Mathlib conclusion
  innerPairEnergy_nonneg / _le               a real intervalIntegral, bound carried

THE GUARD IS THE LOAD-BEARING ONE. A concrete two-component link, disjoint
everywhere and uniformly separated nowhere, proving `disjoint` does NOT give the
bound. Without it a later reader could "simplify" HasUniformSeparation away by
appealing to disjoint, and every bound in the file would silently go vacuous --
exactly the failure mode that produced four vacuous declarations in
QOU.MobiusEnergy before 2026-08-30.

ASSUMED, visible: the uniform gap (automatic for disjoint COMPACT components;
this is where compactness enters) and measurability of sep. Neither is the
conclusion in disguise.

NOT CLAIMED: the self/diagonal channel (still needs O'Hara, is qou-bn8e's), and
NOTHING about reproducing kappa(A) -- PR #7080 retired that gate. This is
admissibility, not confirmation.

## ENVIRONMENT TRAPS (cost most of the pass; next agent should not re-pay)

1. THE CACHED OLEAN IS OLDER THAN THE SOURCE. QOU/MobiusEnergy.olean is dated
   Aug 8 and predates the 2026-08-30 roast fix, so it has no LinkEmbedding and no
   ambientDist. A naive lean-direct run reports "unknown identifier
   LinkEmbedding" + a spurious `sorry` warning -- errors describing the SNAPSHOT,
   not the file. AGENTS.md's snapshot trap, running in the OLDER direction.
2. TWO MATHLIB TREES. Root workspace: 3469 oleans incl. Geometry/Manifold and
   MeasureTheory/Integral/IntervalIntegral. Paper tree: 1902, neither. LEAN_PATH
   must put ROOT first or every QOU import dies on a "missing" manifold olean
   that is in fact present. scripts/lean-shadow-verify.sh auto-detects the PAPER
   tree and hits this.
3. LEAN DOES NOT FALL THROUGH. It commits to the first LEAN_PATH root containing
   a QOU/ dir. So a shadow must be a hardlinked copy of the WHOLE QOU tree
   (cp -al, no disk cost) with the stale module UNLINKED before rebuild. Verified
   by inode that nothing writes through into the real cache.

Working recipe: cp -al root QOU tree to shadow; rm the stale module; rebuild it
with LEAN_PATH=shadow:rootpackages:rootbuild (ABSOLUTE paths); then compile.
MobiusEnergy rebuilds from source in 5.2 s.

## ALL THREE STRUCTURAL GATES NOW HAVE LEAN (2026-09-13, PR #7284)

  even in mu-bar_123      PROVED, and overshot — the channel is BLIND to it.
                          innerPairEnergy_reverse is a real change of variables:
                          the exchange that sends mu-bar -> -mu-bar leaves the
                          energy unchanged. So it is not the odd functional
                          odd_symmetric_functional_vanishes annihilates.
  nonzero at lk = 0       PROVED as the two-sided bracket [1/D^2, 1/delta^2],
                          both endpoints positive, both from distances alone.
                          I deliberately did NOT state "positive even when
                          lk = 0" — in this encoding LinkEmbedding carries no
                          linking data, so that reads as content while being
                          true by vacuity: the exact dressed-up tautology the
                          MobiusEnergy roast found four of.
  O2 / zero-mean          PROVED — but EARNED, not the freebie I claimed. See
                          the correction on qou-o6ml: the mutual channel is
                          UNSUBTRACTED and strictly positive, i.e. in coth's
                          excluded position. Cleared by #7080's closure: zero
                          mean forces the subtraction to be the kernel's own
                          mean, so it is determined not chosen.

12 declarations total, every one [propext, Classical.choice, Quot.sound], no
sorryAx. lean-direct exit 0, zero warnings.

WHAT ROUTE (2) IS NOW BLOCKED ON, and it is not infrastructure. The functional
exists, is finite, and clears every structural gate the corpus has. What it
lacks is a DISCRIMINATING OBSERVABLE: #7080 retired kappa(A), and the three
gates are pass/fail admissibility tests that many candidates would also pass —
clearing them is not evidence for route (2) over any other orientation-blind
candidate. Naming an observable that separates candidates is the open item.


## MEASURE GAP FOUND AND CLOSED (push c73206b124, PR #7284)

Found while answering the author's question about route 2's SHAPE, not by a
detector. The gap was in work already pushed on this bean.

THE GAP. Sections 1-5 stated O2 (zero-mean clearance) against the FLAT
parameter measure ds dt. The O'Hara integrand the mutual term is taken from
carries ARCLENGTH weights |gamma'(s)||gamma'(t)|. Those agree only under
constant-speed parametrisation, and LinkEmbedding carries no derivative data
-- nothing in the structure supplies it. "Zero mean" is a statement ABOUT A
MEASURE, so section 5's clearance was silently assuming a parametrisation the
carrier does not have. Not cosmetic.

THE REPAIR, and the first instinct was WRONG. I proposed writing the
constant-speed condition into a docstring and scoping section 5 to it. That
makes the assumption visible without making it go away -- and a visible
assumption gets quoted as if established. Removed it instead.

Section 6 restates O2 against an ARBITRARY density w:
  weightedPairMean  = (int f*w) / (int w)
  zeroMeanMutualKernelW_integral_zero : int (f - mean)*w = 0
    hyps: IntervalIntegrable w, IntervalIntegrable (f*w), (int w) != 0
  weightedPairMean_one : w = 1 recovers section 5 exactly

w is a bare function, so integrability AND non-degeneracy are explicit
hypotheses -- they cannot be derived from anything LinkEmbedding holds, and
assuming otherwise is what produced the gap. Arclength is now one instance of
w, not a special case that had to hold.

NOT A NEW PARAMETER. The subtraction constant is still FORCED -- it is the
kernel's own w-mean, same shape as c_0 = <coth>_M in #7080. The measure the
mean is taken against changed; nothing became free. Anti-fit position of the
arc untouched.

VERIFIED: lean -DautoImplicit=false -s 65536 exit 0 against the real import
cone (restored cache + hardlinked shadow, no lake build). #print axioms on ALL
NINE decls in the file: [propext, Classical.choice, Quot.sound]. No sorryAx.

BEAN STAYS OPEN. The three gates (even in mubar_123, nonzero at lk = 0, O2)
are ADMISSIBILITY tests -- many candidate kernels pass all three. Route 2
still needs a DISCRIMINATING observable. That is the author's call and is
deliberately not chosen here.
