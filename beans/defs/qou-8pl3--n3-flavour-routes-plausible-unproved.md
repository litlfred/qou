---
# qou-8pl3
title: 'PLAUSIBLE-NOT-PROVED: routes to N = 3 for the flavour fundamental'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-flavour
created_at: 2026-08-06T00:00:00Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-8lxd
---

## UPDATE 2026-08-07 — the obstruction half is now PROVED

`QOU/Eightfold/RowCapObstruction.lean` (sorry-free, lean-direct exit 0):

* `weyl_dim_alt_eq_zero_iff` : `dim V_{(1³)} = C(N,3) = 0  ↔  N < 3`
* `decuplet_forces_three`    : `dim V_{(3)} = 10  →  N = 3`
* `singlet_forces_three`     : `dim V_{(1³)} = 1  →  N = 3`
* `schur_weyl_cube_split_two_three` : `8 = 4+4+0` at N=2, `27 = 10+16+1` at N=3

So `N = 2` is a **scope-(b) structural exclusion** from carrying the
eightfold-way decomposition, with the justifying invariant cited (the
Schur-Weyl row cap `ℓ(λ) ≤ N`). The chapter previously stated this; it is now
a theorem. Wired as the `lean:` sibling of `prop:schur-weyl-eightfold`.

**This does not narrow the search.** It excludes N=2 from *hosting* the
decomposition; it says nothing against any route below that produces N=3.
If anything it raises the value of Route A/B, because the target is now
sharply characterised: produce `dim V = 3`, and the decuplet/octet/singlet
structure follows by the arithmetic already proved.

## The blocker

Quantum Schur-Weyl duality gives the eightfold-way multiplets only when the
fibre has `dim V = N = 3`. The single-fibre tower yields a quantum form of
`SU(2)`, `dim V = 2`. The row cap `ℓ(λ) <= dim V` then **kills the
antisymmetric partition `(1³)`** — at `N = 2` the decomposition is
`4·1 + 2·2 = 8 = 2³`, with no singlet. No choice of `q` restores it: the cap is
on the dimension, not the deformation.

Every flavour statement in the chapter is conditional on this. It is the
chapter's principal open problem.

## Route A — multi-fibre groupoid (plausible, untried)

Construct a three-dimensional object `W` in the multi-fibre groupoid whose
symmetric square `Sym²(W)` is irreducible (carries no singlet). Inequivalent
fibre objects whose interaction space is 3-dimensional. **Nothing has been
built.** Tracked historically as T3b.

Constraint to respect: the `SU(2)`-emergence theorem says the tensor-automorphism
gauge group of a *single* fibre is exactly `SU(2)`, so any `N = 3` must come from
groupoid-level structure — multi-strand, framing, or inter-fibre. A construction
placing it inside `Aut^⊗(τ)` of one fibre contradicts a proved theorem.

## Route B — octonionic `G_2` stabiliser (partial, and possibly the wrong target)

The Günaydin–Gürsey decomposition `Im(𝕆) ≅ ℝ ⊕ ℂ³` under `SU(3) ⊂ G_2` supplies a
non-self-dual triple, and the `3`/`3̄` of `PSL(2,7)` are complex conjugate as
required.

**Two gaps.** (i) The `Sym²` gate "pass" is a literature decomposition; the Lean
file proves only arithmetic (bean `qou-sym2`). (ii) **This route produces
colour, not flavour.** Whether the octonionic `SU(3)` can also serve as flavour
is item 4 of the chapter's open problems and is untested — and the chapter's own
obstruction audit argues they cannot both come from the same construction, since
the `Sym²` gate excludes the icosahedral colour triple `T_1` while the `G_2`
route passes it.

## What would settle it

Either construction, explicitly, with `Sym²` irreducibility checked against the
actual constructed object rather than cited. A **negative** is equally valuable:
a proof that no groupoid-level `N = 3` exists compatible with the `SU(2)`
fibre theorem would refute the eightfold-way chapter's premise outright, which is
worth knowing.

## Scope discipline

Scope-(a) throughout. No proved invariant forbids `N = 3`; it is simply not
constructed.


## PROGRESS 2026-08-26 — Route B's T_1-vs-G_2 comparison is now a COROLLARY (PR #5810)

This bean records the chapter's argument that the octonionic SU(3) and the
icosahedral colour triple cannot both come from one construction, "since the
Sym^2 gate excludes the icosahedral colour triple T_1 while the G_2 route
passes it". That is a case analysis over two examples. The actual mechanism is
Frobenius-Schur type -- T_1 is a rotation rep of A_5 subset SO(3) and so REAL,
the Gunaydin-Gursey triple in Im(O) = R + C^3 is COMPLEX -- and neither of the
two existing gate files could state it: Sym2GateMultiplicity models FS = +-1
only, Sym2GateComplexType models FS = 0 only.

QOU/Eightfold/Sym2GateFSTrichotomy.lean unifies them over the full trichotomy
(12 decls, sorry-free, lean-direct exit 0, axioms [propext, Quot.sound] only --
not even Classical.choice):

  gate_forces_complex_of_dim_three   ANY dim-3 object passing the gate contains
                                     a complex-type irrep
  real_triple_fails_gate             the T_1 half, one line, no icosahedron
  even_dimOf_of_selfDual             recovers Sym2GateMultiplicity's conclusion
                                     in the unified language

So real and quaternionic constructions are excluded AS A CLASS, not as two
examples: passing forces real multiplicities to zero, quaternionic dimensions
are even, the total is even, and 3 is odd. Complex type is not one way among
several to reach dimension 3 through this gate -- it is the ONLY way.

Two standard inputs are carried as EXPLICIT HYPOTHESES rather than assumed:
QuaternionicEvenDim (an H-module has even dimension; Sym2GateMultiplicity got
this free from dim = 2j+1, there is no such formula here) and the self-duality
classification. That is deliberate -- the theorem then names exactly what it
needs, and no fact about octonions or icosahedra is among them.

GAP (i) IS UNCHANGED AND I WANT THAT ON THE RECORD. This does NOT prove the
Gunaydin-Gursey triple IS complex type; that remains the cited literature
decomposition, exactly as this bean says. The file establishes what complex type
BUYS and what real type COSTS. The input is still an input, and Route B still
needs it formalised or explicitly cited at the point of use.

WHAT IT CHANGES FOR THE ROUTE: the target is now sharper. Route B does not need
to argue about icosahedra at all -- it needs exactly one thing, that its triple
is complex type. Everything else follows. Conversely any future candidate that
is real or quaternionic is dead on arrival at dimension 3, without further
analysis.


## GAP (i) NARROWED 2026-08-26 — triality certifies complex type (PR #5810)

This bean records Route B gap (i) as: "the Sym^2 gate 'pass' is a literature
decomposition; the Lean file proves only arithmetic". That gap is now SMALLER
and, more usefully, SHARPER.

Chain as it now stands:

  1. gate_forces_complex_of_dim_three (Sym2GateFSTrichotomy) -- ANY dim-3 object
     passing the Sym^2 gate must contain a complex-type irrep. Real and
     quaternionic constructions excluded as a class. DERIVED.
  2. not_selfDual_of_triality_ne_zero (TrialitySelectionRule) -- an object of
     non-vanishing triality is not self-dual. DERIVED.
  3. fundamental_not_selfDual -- the 3 has triality 1, hence complex type.
     DERIVED.
  4. Gunaydin-Gursey: Im(O) = R + C^3 with SU(3) acting on that C^3 in its
     STANDARD FUNDAMENTAL representation. STILL CITED.

Given (4), complex type is no longer an assumption anywhere in the chain. So
what stands between Route B and a complete argument is ONE sharply stated,
citable claim about the octonion decomposition -- not a diffuse "the literature
says the triple passes the gate".

That is worth more than the size of the reduction suggests: a referee can be
pointed at a single sentence of Gunaydin-Gursey 1973 rather than asked to accept
a decomposition-plus-gate-verdict as a package.

THE SAME ARITHMETIC FACT DID BOTH JOBS, which is worth noting because it is the
reason this was cheap: 2 being a unit in Z/3 is what makes the grading BLIND to
the flavour/colour identification (the negative, which forced me to retract my
own "testable difference" claim earlier in this session) and what makes it SHARP
about self-duality (the positive here).

STILL OPEN and NOT touched: Route A (multi-fibre groupoid, nothing built);
gap (ii), whether the octonionic SU(3) can serve as flavour rather than colour;
and the flavour-vs-colour identification itself, which TrialitySelectionRule
proves the Z/3 grading cannot see.


## GAP (ii) WORKED 2026-08-26 — the Sym^2 gate CANNOT separate flavour from colour

Gap (ii) asks whether the octonionic SU(3) can serve as flavour rather than
colour, and records the chapter's position that it cannot, because "the Sym^2
gate excludes the icosahedral colour triple T_1 while the G_2 route passes it".

THAT ARGUMENT IS WITHDRAWN. Two defects.

1. DEAD CITATION. eightfold-open-problems.md item 4 attributes it to
   sec:color-algebra. Per eightfold-way.ts that section holds exactly ONE block,
   color-su3-from-g2, which does not mention T_1 at all. The T_1 comparison is
   in schur-weyl-eightfold.md -- and that source is far more careful than item
   4: it says the octonionic 3 is "NOT EXCLUDED by the Sym^2 gate, on a
   decomposition taken from the literature. It is not a machine-checked pass,
   and the file should not be cited as one." Item 4 upgraded that to "the G_2
   route passes it" and built a "cannot" on top.

2. THE INFERENCE DOES NOT GO THROUGH. The premise compares TWO DIFFERENT
   OBJECTS (T_1 fails, octonionic 3 not excluded) and establishes only that
   those two differ. The conclusion is about ONE CONSTRUCTION supplying TWO
   ROLES. The comparison never tests the proposition it is offered as proof of.
   Scope-(a) negative presented as scope-(b) structural exclusion, with no
   invariant cited that would license (b).

3. AND NO STRENGTHENING RESCUES IT -- the gate is PROVABLY BLIND.
   gate_forces_complex_of_dim_three: at dimension 3, passing is equivalent to
   carrying a complex-type irrep. So ANY two 3-dim objects that both pass are
   both complex type and receive the SAME verdict.
   gate_does_not_separate_two_triples exhibits two distinct such objects.
   A flavour triple and a colour triple that each pass are, to this gate,
   indistinguishable.

BOTH OBVIOUS INVARIANTS ARE NOW KNOWN BLIND. The Z/3 grading:
identification_invisible_to_selection_rule (2 is a unit, every verdict
unchanged). The Sym^2 gate: this. A discriminator must be found elsewhere, and
that is now a proved constraint on the search rather than a hunch.

WHAT SURVIVES, and it is stronger than the withdrawn claim in one respect: the
gate gives a CLASS exclusion, not a two-example comparison -- no real or
quaternionic construction whatever reaches dimension 3 through it. T_1's failure
follows from its Frobenius-Schur type (a rotation rep of A_5 subset SO(3), hence
real), not from anything about the icosahedron. real_triple_fails_gate is that
in one line.

ITEM 4 STAYS OPEN. Nothing here decides same/different/groupoid-dual. What is
removed is a false piece of support for one answer; what is added is a proved
reason not to look here again.

Corrected in content (eightfold-open-problems.md item 4 rewritten: over-claim
withdrawn, citation repointed to prop:schur-weyl-eightfold, the two blindness
results cited). Audit:
docs/audits/2026-08-26-sym2-gate-cannot-separate-flavour-from-colour.md


## ROUTE A WORKED 2026-08-26 — the target is now ONE checkable property

Route A is recorded as "construct a three-dimensional object W in the multi-fibre
groupoid whose Sym^2(W) is irreducible. NOTHING HAS BEEN BUILT." Nothing is
built here either -- but the specification is now a theorem instead of "more
structure", and a candidate can be screened before any Sym^2 decomposition.

QOU/Eightfold/SelfDualSectorConfinement.lean (4 theorems, sorry-free,
lean-direct exit 0 against the REAL import cone -- Sym2GateFSTrichotomy.olean
exists from the merged PR #5810, so the import resolved against a genuine build,
not a stub):

  selfDual_category_excludes_dim_three   in a category where every irrep is
                                         self-dual, no dim-3 object passes
  single_fibre_su2_excludes_dim_three    the SU(2) case, with the self-duality
                                         of every SU(2) irrep carried as a NAMED
                                         hypothesis rather than assumed
  self_duality_is_the_obstruction        the two halves as one statement
  screen_out_selfDual_candidate          the contrapositive, as a test

THE POINT. gate_forces_complex_of_dim_three says any dim-3 gate pass must be
complex type. selfDual_category_excludes_dim_three says a self-dual category has
none. Every SU(2) irrep is self-dual. So THE PROPERTY A GROUPOID CONSTRUCTION
MUST EXHIBIT IS EXACTLY THE PROPERTY ONE FIBRE LACKS: non-self-duality. Not one
option among several -- the only way anything reaches dim 3 through this gate.

Operationally that is a screening test: ask whether a candidate's
three-dimensional object is isomorphic to its own dual. If yes it is dead,
whatever else it has, and no Sym^2 computation is needed.

A CORRECTION I EXPECTED TO MAKE AND DID NOT. I went in believing the chapter's
confinement claim rested on a reason my own earlier work had undercut -- it
says "the search is confined to the groupoid level is now a theorem" and cites
the parity criterion, which Sym2GateFSTrichotomy shows is a SELF-DUAL-SECTOR
theorem that does not bar dim 3 in general. Read the current text before
editing: the chapter already states the self-duality mechanism explicitly ("the
parity argument runs through self-duality: every SU(2) irrep satisfies
V* = V..."), in a paragraph I added in the merged PR. The prose was already
right. So this is prose -> theorem, NOT a correction, and the chapter got a
short pointer rather than a rewrite. Third time this session that reading the
current state prevented a wrong "fix".

WHAT IS NOT DONE, explicitly: no construction, and no demonstration that a
non-self-dual object EXISTS at groupoid level. Route A stays OPEN. What is
settled is a NECESSARY condition and the exact reason the single-fibre case
fails it. Nor does any of it bear on flavour-vs-colour -- both invariants are
still blind to that.


## Route A specification, PR #5819 (2026-08-26)

Route A ('nothing has been built') is NOT closed. What is now settled is a
NECESSARY condition on any candidate:

  SelfDualSectorConfinement.lean, 4 theorems, sorry-free.
  gate_forces_complex_of_dim_three (merged) + every SU(2) irrep self-dual
  => the property a groupoid construction must EXHIBIT is exactly the
     property one fibre LACKS: non-self-duality.

Screening test: is the candidate three-dimensional object isomorphic to its
own dual? If yes it is dead, with no Sym^2 decomposition needed.

Still open: no construction, and no demonstration that a non-self-dual object
EXISTS at groupoid level.


## ROUTE B route-class narrowing 2026-08-26 (PR #5819)

Gap (i) is unchanged: the Gunaydin-Gursey decomposition is still a CITATION
(now properly registered as gunaydin-gursey1973 with the decomposition in its
note, done 2026-08-25). Nothing here derives it.

What IS now settled is which octonionic route Route B may lean on. There are
two in the literature and they are not variants:

  stabiliser route   SU(3) subset G_2 = Aut(O) acting ON Im(O) = R + C^3.
                     Real dimensions balance: 1 + 2*3 = 7.
  identification     lambda_a <-> e_a, generators identified WITH the units.
                     8 generators, 7 units. Excluded.

QOU/Eightfold/OctonionicSu3RankObstruction.lean (4 decls, sorry-free,
lean-direct exit 0, axioms [propext, Classical.choice, Quot.sound]):

  no_faithful_generator_identification   dim 8 -> dim 7 is never injective
  cartan_not_independent_on_one_unit     two multiples of one unit are
                                         dependent, so a rank-2 Cartan
                                         collapses to a line
  no_injective_of_finrank_lt             the general dimension lemma
  not_linearIndependent_of_common_line   the general rank lemma

THE OBSERVATION IS NOT MINE. The 2026-08-25 upload triage already recorded both
defects in prose, on two of the eight papers ('reusing e_3, which is not
injective and not a Lie-algebra map'; 'lambda_8 prop lambda_3 collapses the
Cartan to rank 1, destroying A_2'). I re-derived it independently and only found
that on the corpus-grep. What is new: machine-checked, and stated as a CLASS
exclusion rather than a defect of two named papers, so a third paper doing the
same thing is excluded without being read. Scope-(b), invariants named
(dimension, rank).

Worked instance in docs/audits/2026-08-26-octonionic-su3-two-routes.md: in
arxiv-1107.1559v1 all four of I_3, V_3, U_3, Y are real multiples of i*e_3 by
its own eq (31)-(32), while the text on the same page calls them linearly
independent.

GAP (ii) STILL UNTOUCHED. arxiv-1107.1559v1's TITLE is 'Quaternion-Octonion
SU(3) Flavor Symmetry' -- exactly gap (ii)'s question -- and it does not answer
it; its conclusion argues strong interactions. Worth flagging because a future
agent grepping the question will land on that paper first.


## GAP (ii) DISCRIMINATOR SEARCH 2026-08-26 (PR #5819)

Item 4 ended 'Whatever separates flavour from colour lies elsewhere'. This is
the search for the elsewhere. Two results.

RESULT 1 -- THE TWO KNOWN BLINDNESSES ARE ONE BLINDNESS, AND IT IS A CLASS.
Both gates read only OBJECT-LEVEL data (dimension, Frobenius-Schur type,
triality class), and on that data the two triples COINCIDE, by two different
routes: colour is the C^3 of Im(O) = R + C^3, complex dim (7-1)/2 = 3; flavour
is the fundamental (1,0), Weyl dim 2*1*3/2 = 3; both complex type, both
triality 1.

  no_object_gate_separates      no gate reading only object data separates them
  no_object_invariant_separates same, arbitrary value type
  tensor_cube_gates_also_blind  Sym^3 (10 both) and Lambda^3 (1 both) are
                                functions of dim V alone, so the whole
                                'try another tensor construction on V' family
                                is dead WITHOUT RUNNING ANY OF IT

Scope-(b), invariant named: equal data, equal verdict. So the Sym^2 and Z/3
failures were never repairable and there is no third such gate to look for.

DELIBERATELY NOT CLAIMED: that the two triples are ISOMORPHIC. That would beg
item 4's question -- they are a priori reps of two different groups and whether
those groups are identified is exactly what is open. The claim is only that the
data these gates READ coincides, which is weaker and sufficient.

RESULT 2 -- WHERE ONE CAN LIVE. The obstruction lifts once a gate may read
WHICH YOUNG-SYMMETRY CHANNEL of V tensor V tensor V carries the physical state:
colour is (1^3) antisymmetric (eps_abc), flavour is (3) symmetric for the
decuplet and (2,1) mixed for the octet. Distinct S_3 irreps.
some_channel_gate_separates exhibits such a gate (construction, not existence).

ITEMS 4 AND 7 ARE THE SAME QUESTION. Item 7, seven items down and filed as a
selection-rule problem, already names the location: 'colour antisymmetric and
spin symmetric force flavour symmetric'. Neither item cited the other; both now
do. This raises item 7's stakes -- deriving the colour-antisymmetry constraint
would supply the one input item 4 is missing.

THE CIRCULARITY THIS DOES NOT ESCAPE. The channel assignment is an INPUT. Item
7 says the chapter derives neither the spin factor nor the colour antisymmetry.
So the discriminator is LOCATED, NOT ESTABLISHED. Result 1 (the negative) is
what is settled, and it is the half that redirects the search.

SECOND CANDIDATE, named not pursued: the SYMMETRY-BREAKING SPECTRUM. Flavour
SU(3) is broken and the corpus already has the relations in Lean
(GellMannOkuboIdentity, ColemanGlashowIdentity, DecupletEqualSpacing); colour
SU(3) is exact with no analogue. Also role-data, so Result 1 does not forbid it;
same hazard that colour exactness would be an input unless derived.

VERIFIED: lean-direct exit 0, real import cone. 7 decls, no sorryAx, zero sorry
zero axiom. THREE MUTATION TESTS, each expected to fail and each failing
(octonion dim (7-1)/2 -> /3; flavour FS complex -> real; colourChannel
antisymmetric -> symmetric) -- the decides compute rather than rubber-stamp.


## COORDINATION SWEEP 2026-08-26 — Route A's requirement was ALREADY RECORDED

Ran /coordinate. One sibling overlaps: PR #5744 (Standard Model), same
QOU/Eightfold/ namespace and same N=3 surface. Posted intent there. No file
conflict. No other open PR touches eightfold-way/ or QOU/Eightfold/.

THE FINDING, AND IT CORRECTS THIS PR. Route A's requirement -- 'the groupoid
must supply non-self-duality' -- is NOT new. Bean qou-dwsh (2026-08-03,
priority high, COMPLETED) states it verbatim in its body:

  'Need: a groupoid with inequivalent fibre objects carrying a 3-dim W whose
   fundamental is not self-dual.'

and reaches it by a DIFFERENT route: the row cap. Descartes chi(A) = -6 forces
SU(2), so dim V = 2, so partitions of at most two rows, so the (1^3) block
drops at n=3. My route is the Sym^2 gate + FS trichotomy. Two independent
derivations of one necessary condition -- which is worth having, and is worth
less if presented as a discovery.

Trail: qou-8pl3 -> qou-8p1i (SCRAPPED as duplicate of qou-dwsh) -> qou-dwsh.
LIVE CARRIER for this surface is qou-y7vg (T3g, non-neutral Tannakian gerbe).
qou-8pl3 Route A, qou-8p1i T3b, qou-dwsh, qou-y7vg T3g, and #5744's 'surviving
direction' are ALL THE SAME OPEN PROBLEM under five names.

THE PROCESS GAP, which is the more useful half. This is the SECOND prior-art
miss in this PR (the first: the 2026-08-25 upload triage had the octonionic
Cartan collapse). The two have DIFFERENT causes:
  1. Tranche 2 -- ran the corpus-grep AFTER the work instead of before.
  2. Tranche 1 -- the source was in .beans/, and the AGENTS.md corpus-grep
     checklist HAS NO BEANS PATH. Paths 1-5 are docs/audits, content,
     computations, docs/coordination, library. .beans/ is under none of them,
     and qou-dwsh's sentence exists NOWHERE ELSE.
Added .beans/ as path 6, with the note that COMPLETED and SCRAPPED are the
two statuses that bite -- completed hides an answer, scrapped names the live
carrier.

ALSO FIXED: my own chapter edit tripped voice-author-notes-pollution (major) by
putting a dated work-plan reference into scholarly prose. Rewritten to state
the row-cap derivation as mathematics with no provenance; provenance now lives
in the Lean docstring and the coordination ledger, where it belongs.

NOT A DEFECT, checked and clear: #5744's audit records that route 1's original
argument ('every SU(2) irrep is self-dual, therefore no summand passes the
gate') is INVALID, and that self_duality_does_not_decide_gate exists so it
cannot be re-derived. SelfDualSectorConfinement is superficially that shape. It
already cites Sym2GateParity, carries QuaternionicEvenDim explicitly on all
four theorems, and its header states 'not parity excludes 3 (false in general)
but SU(2) is a self-dual category, and in a self-dual category parity excludes
3'. The guard held.

New ledger: docs/coordination/eightfold-n3-surface.md.


---

**Cross-reference added 2026-08-29** (from PR #5744, answering the ask posted on
that PR from #5819). Route A here — *"construct a three-dimensional object in
the multi-fibre groupoid"* — is not an unclaimed slot. It already has a bean
cluster, under epic **`qou-8lxd`** (EPIC: eightfold way / SM derived from QOU):

| bean | title | status |
|---|---|---|
| `qou-dwsh` | T3b: distinct-fibre groupoid — does a non-self-dual 3-object exist? | **completed** (high) |
| `qou-y7vg` | T3g: non-neutral Tannakian / gerbe — inter-universe flavour | todo |
| `qou-8p1i` | multi-fibre groupoid (T3b) — "the only untouched native route" | **scrapped** |
| `qou-bldy` | T3a: Lean the Sym² gate — SU(3) fundamental admits no invariant symmetric form | completed |

So Route A (here), T3b (`qou-dwsh`) and T3g (`qou-y7vg`) are **three names for
one open problem**, and `qou-8p1i` is the scrapped predecessor — its "only
untouched native route" framing is superseded by `qou-dwsh`.

**Read `qou-dwsh`'s `completed` carefully — it is a SPECIFICATION, not a
construction.** Its body does not build the object; it states what the object
must be:

> Single-fibre `V^{⊗n}` is structurally capped at `gl₂` (Descartes `χ(A) = −6`
> → `SU(2)` → `dim V = 2` → partitions ≤ 2 rows; the `(1³)` block **drops** at
> `n = 3`). So the representation must **not** be a tensor power of one `V`.
> Need: a groupoid with inequivalent fibre objects carrying a 3-dim `W` whose
> fundamental is **not self-dual**.

That is the same necessary condition #5819 reached from the Frobenius–Schur
trichotomy (`gate_forces_complex_of_dim_three`: a dim-3 object through the gate
must supply a **complex**-type summand — and complex type is exactly
"fundamental not self-dual"). Two routes, one condition, independently derived.

**Its stated gate is discharged.** `qou-dwsh` says "Gated on T3a"; T3a is
`qou-bldy`, which is `completed`. So nothing upstream blocks the construction —
what is missing is the construction itself.

Anyone picking this up: read `qou-dwsh` first, then `qou-y7vg`. The setup is
written down; do not re-derive it.

## Cross-reference 2026-09-03 (PR #6458) — the fibre-functor version of Route A is closed

Route A asks for a 3-dim object at the groupoid level. The single-fibre variant
"change the fibre functor so dim tau'(V) = 3" is now excluded scope-(b):
such fibre functors exist (Bichon 2003, real at q0) and preserve fusion rules,
so V^{x3} still has no singlet. Route A proper (a different category / object,
not a summand of V^{x n} and not a re-fibred V) is untouched. See
docs/audits/2026-09-03-fibre-functors-do-not-change-the-category.md §4.


## Progress Update — 2026-11-16 (`litlfred/qou#8155`, `f3af82fd1d99fc5eb05c0bd46bbd812b46330432`)

- **Lean 4 formalization (`folio/quantum-observable-universe/lean/QOU/Eightfold/FlavourCartanOctetDecuplet.lean`, `0` `sorry`, wired into `QOU.lean`)**:
  - Proves `su6_spin_flavour_56_and_condition5_split` combining the single-fibre $N = 2$ row-cap (`weylDimSym3 2 = 4`, `weylDimMixed3 2 = 2`, `weylDimAlt3 2 = 0`) with the $N = 3$ flavour object $W$ (`weylDimSym3 3 = 10`, `weylDimMixed3 3 = 8`, `weylDimAlt3 3 = 1`, $10 + 2 \times 8 + 1 = 27$) to establish the Kronecker decomposition $\dim \mathrm{Sym}^3(\mathbb{C}^3 \otimes \mathbb{C}^2) = 10 \times 4 + 8 \times 2 + 1 \times 0 = 56$.
- **Witness (`computations/probes/flavour-cartan-octet-decuplet-degeneration.witness.json`)**: `allPassed: true` (`q0Anchor: "independent"`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8155, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
