---
# qou-pc85
title: 'EM-linking route 2: the MUTUAL O''Hara channel is integrable WITHOUT O''Hara''s theorem — no diagonal singularity, so bounded+measurable suffices (qou-o6ml)'
status: todo
type: task
priority: normal
created_at: 2026-09-13T09:22:10Z
updated_at: 2026-09-13T10:35:03Z
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
