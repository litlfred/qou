---
# qou-zfs6
title: 'Discriminating observable for route 2: Mobius invariance / FHW bound / minimiser as Lean gates'
status: in-progress
type: task
priority: normal
created_at: 2026-09-13T11:56:17Z
updated_at: 2026-09-13T15:00:58Z
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


## 🛑 I OVER-CLAIMED "the FHW bound is now held" — the STATEMENT is, half the PROOF is, and its other half cites a work whose identity is UNRESOLVED

Earlier today I recorded that `arxiv-math-9301212v1` (Bryson–Freedman–He–Wang,
Bull. AMS 28(1) 1993) puts the crossing bound `2πc([γ]) + 4 ≤ E(γ)` in the
library as its **Theorem D**. That is true and stands. Reading the *proof*
rather than the statement sharpens it three ways.

### 1. Theorem D's proof is two halves, and only one is in this document

Verbatim from the ingested text:

```
Proof of Theorem D. Theorem 2.5 of [FH] gives the inequality
                    c([γ]) ≤ c(γ) ≤ E(γ)/2π
for proper rectifiable lines. According to the Möbius Invariance Property, the
energy will increase by exactly 4 if a Möbius transformation is used to move the
line off infinity and into closed position. □
```

So the bound decomposes as **`c ≤ E/2π` (imported from [FH] Thm 2.5, NOT proved
here) + exactly 4 (from the Möbius Invariance Property, which IS proved here in
full)**. My earlier phrasing — "citing the bound is unblocked; the proof is still
not held" — was too coarse in the safe direction but still wrong: *half* the
proof is held, and it is the half that this corpus's own Lean work is about.

### 2. 🛑 [FH] IS NOT DEMONSTRABLY `freedman1994`

The announcement's reference list reads:

```
[FH] M. H. Freedman and Z.-X. He, On the 'energy' of knots and unknots (to appear).
[O1] Jun O'Hara, Energy of a knot, Topology 30 (1991), 241–247.
```

`[O1]` matches `ohara1991` exactly. **`[FH]` does not match `freedman1994`**, on
two independent fields:

| | `[FH]`, as cited 1993 | `freedman1994` in references.ts |
|---|---|---|
| authors | Freedman, He — **two** | Freedman, He, **Wang** — three |
| title | *On the 'energy' of knots and unknots* | *Möbius energy of knots and unknots* |

Subject and timing match, so the natural reading is that [FH] is the preprint
that became the Annals paper with Wang added and the title changed. **That is a
guess and is recorded as one.** Resolving it needs the Annals text or a
bibliographic lookup, and both are egress-blocked here (see `qou-6xt9`'s route
table). The alternative — that [FH] is a distinct Freedman–He paper — is not
excluded by anything held.

**Why it matters rather than being pedantry:** if they are different works, then
a citation of `[freedman1994]` for "Theorem 2.5" points at a source that does
not contain it. Nothing in the corpus cites a numbered theorem of
`freedman1994` today, so nothing is currently wrong — this is a trap to avoid,
not a defect to fix.

### 3. What IS now verifiable against held text: `qou-zfs6`'s assumed inversion laws

`qou-zfs6` records, honestly, *"ASSUMED, cited, not derived: the two classical
inversion laws … ([ohara1991], [freedman1994])"*. The announcement's Möbius
Invariance proof is present in full and uses exactly that structure — its
equation (2) carries the Jacobian factors

```
Eε(I ∘ γ) = ∫∫ ( 1/|I∘γ(u) − I∘γ(v)|²  −  1/D(I∘γ(u), I∘γ(v))² )
              × ‖I′(γ(u))‖ · ‖I′(γ(v))‖  du dv
```

which is the second assumed law (`|I(γ(s))′| = 1/|γ(s)−a|²`) appearing as the
arclength density, and it is the same cancellation `qou-zfs6` §7 formalises —
*"the arclength Jacobians 1/|γ−a|² are exactly what cancel the chord factors"*.
The first law is then applied in the step the text calls *"a short calculation
(using the law of cosines)"*.

So those two laws move from **cited-but-unreadable-here** to **cited and
checkable against held text** — though note the document attributes the
*calculation* to itself, not to [O1]/[FH], so the `([ohara1991],
[freedman1994])` attribution in the bean is still not verified by this find; what
is verified is that the laws are standard and used exactly as assumed.

### Nothing here changes any Lean

`mobiusInvariant_forces_inverse_square` and its siblings are untouched — they are
proved from the invariance hypothesis, not from these citations. The
realisable-triples question `qou-zfs6` stays open on is also untouched: this
document quantifies over actual space curves, so it says nothing about whether
the characterisation survives on realisable distance triples only.
