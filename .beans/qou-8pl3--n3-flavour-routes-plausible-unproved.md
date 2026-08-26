---
# qou-8pl3
title: 'PLAUSIBLE-NOT-PROVED: routes to N = 3 for the flavour fundamental'
status: todo
type: task
priority: normal
created_at: 2026-08-06T00:00:00Z
updated_at: 2026-08-26T03:42:59Z
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
