---
# qou-pc85
title: 'EM-linking route 2: the MUTUAL O''Hara channel is integrable WITHOUT O''Hara''s theorem — no diagonal singularity, so bounded+measurable suffices (qou-o6ml)'
status: in-progress
pr: 8306
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-13T09:22:10Z
updated_at: 2026-10-04T15:18:59Z
parent: qou-v2om
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


## THE LIBRARY HOLDS NO KNOT-ENERGY SOURCE (corpus-grep path 5, both tiers)

Ran path 5 on this arc's own subject matter while merging main up. Result is
a clean negative, and the first pass reported the OPPOSITE.

SCOPE OF THE CLAIM (per the negatives rule): measured the LIBRARY SURFACE --
library/*/sections/, library/*/ocr/, and INDEX.md -- not the literature.
O'Hara 1991, Freedman-He-Wang 1994 and Doyle-Schramm exist; this corpus does
not hold them. "We have not ingested it" and "it does not exist" are
different claims and only the first was measured.

STRICT GREP (word-boundary O'Hara, Mobius energy, energy of knots, knot
energies, ropelength, self-repulsive energ) across BOTH tiers: ZERO
documents. INDEX.md: zero rows. uploads/ queue: 1 PDF, the astro-ph
r-process one, nothing pending on this subject.

THE FIRST PASS SAID EIGHT, AND ALL EIGHT WERE FALSE. The alternation had a
bare unanchored `ohara`, which matched four separate SURNAMES:
  Manoharan   arxiv-hep-th-9811173v1
  Shinohara   arxiv-2501.00914v2, m4-24, arxiv-2602.15276v1
  Nohara      arxiv-1006.1099v3
  Iohara      arxiv-2404.03933v2
The seventh (arxiv-0705.1468v1) matched a real string "knot energy" in
"Knots in the Skyrme-Faddeev model" -- SOLITON energy, a different object,
so a true string match and a subject false positive. The eighth matched
nothing on re-check.

NEW BLIND-SPOT CLASS, OPPOSITE DIRECTION TO ALL 35 CATALOGUED ROWS. Every
row in docs/audits/2026-08-15-detector-blindness-taxonomy.md is a detector
MISSING something, and the failure mode is a false all-clear. This is a
detector OVER-matching, and its failure mode is a false COVERED: an agent
running my first grep concludes "eight documents cover knot energy, path 5
is satisfied" and stops. That is worse than a miss, because a miss leaves
you looking and this does not. Substring surnames are the mechanism and
they are not rare -- four distinct ones in eight hits.

WHY IT MATTERS TO THE ARC, three ways:

1. qou-bn8e (the self/diagonal channel) GENUINELY NEEDS O'Hara's theorem,
   and the corpus does not hold the paper proving it. That is a gap in the
   arc, not in this bean.
2. It raises the value of this PR's section 1 prune. The mutual channel
   needing no O'Hara result is not merely an economy -- it is the only part
   of route 2 that can proceed at all without an unheld source.
3. It is a candidate ANSWER to the discriminating-observable blocker rather
   than more of the blocker. The knot-energy literature carries exactly the
   discriminating properties route 2 lacks: Mobius invariance, the
   Freedman-He-Wang crossing bound E(K) >= 2*pi*c(K) + 4, minimiser
   existence. Nothing in the corpus separates candidate kernels partly
   because the corpus holds nothing that would.

NOT ACTED ON. Ingest is owner-gated (main's own log: "ingest the 7 remaining
uploads (owner-approved)") and is neither a precision fix nor corpus-derived,
so it falls under the 2026-09-07 ask-first rule. Reported, not done.


## 🟩 The library NOW HOLDS the knot-energy literature — 11 sources, incl. O'Hara's original

This bean's own path-5 finding — *"the library holds NO knot-energy source, and my
first grep said the opposite"* — was **true as measured, and the sources were on
disk the whole time**, one directory away from where path 5 looks.

They were in **`uploads/`**, the incoming queue. AGENTS.md: *"corpus-grep path 5
searches `library/` only, so anything still in `uploads/` is invisible to it — an
un-ingested paper will not be found by any 'has the corpus got this?' check,
which is exactly how a held source gets re-derived."* That is this bean, exactly.

Ingested 2026-09-13 (`pdf-structure.py` → `migrate-uploads-to-library.py --apply`
→ `summarize-library.py --apply`), 14 ok / 0 failed:

| doc-id | work |
|---|---|
| `1-s20-0040938391900102-main` | **O'Hara, _Energy of a Knot_, Topology 1991** — the primary |
| `arxiv-1111.6782v2` | Blatt & Reiter, *Stationary Points of O'Hara's Knot Energies* |
| `arxiv-1202.5426v2` | *Hard analysis meets critical knots* — stationary points of the Möbius energy |
| `arxiv-1308.2499v1` | Blatt & Reiter, *Towards a regularity theory for integral Menger curvature* |
| `arxiv-1904.13129v1` | Vorderobermeier, *regularity of critical points for O'Hara's knot energies* |
| `arxiv-1905.06064v1` | Blatt, Reiter & Schikorra, *On O'Hara knot energies I: regularity for critical knots* |
| `arxiv-1908.11677v1` | Kawakami, *Variational formulae and estimates of O'Hara's knot energies* |
| `arxiv-2103.07383v1` | Steenebrügge, *Analyticity of critical points of the generalized integral Menger curvature* |
| `arxiv-2208.12678v4` | Lipton & Nair, *Stationary curves under the Möbius–Plateau energy* |
| `arxiv-2505.02719v2` | Freches, Schumacher, Steenebrügge et al., *Palais–Smale condition in geometric knot theory* |
| `arxiv-2512.02998v1` | Blatt, Gilsbach, Reiter et al., *Stability of knot equivalence at low regularity, symmetric critical knots* |

Measured on the same greps, before → after:

```
tier 1 (INDEX.md) knot-energy rows        0  ->  4
documents mentioning O'Hara (tier 3)           14
O'Hara's own paper greppable                   yes
```

## What this changes for this arc, and what it does NOT

**Does not** retract or confirm anything here. The O2 gate, the mutual-channel
retraction (`b6f0259fe`), the arbitrary-density proof (`bbacee7d9`) and the
orientation-blindness result (`a5694110b`) all stand on their own Lean and are
untouched by what the library holds.

**Does** mean the next pass on this arc can run path 5 for real. In particular
`1905.06064v1` (regularity for critical knots) and `2505.02719v2` (Palais–Smale)
are on exactly the variational question the O2 gate sits in, and **none of them
had been read** when the gate was argued — they could not be.

So: **re-run path 5 before the next "this is open" or "no theorem exists"
declaration on this arc.** The three tiers are cheap now
(`grep -i <topic> library/INDEX.md`, then `summary.json`, then
`grep -rln <topic> library/<doc-id>/sections/`).

## Caution, so the next agent does not over-read this

These are **ingested, not read**. `structure.json` + `sections/` make them
greppable; nobody has adjudicated whether any of them supplies the O'Hara
theorem the mutual channel was said not to need. Holding a source and having
checked it are different claims — that distinction is what `qou-pc85` was
originally about.
