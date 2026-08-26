---
# qou-8pl3
title: 'PLAUSIBLE-NOT-PROVED: routes to N = 3 for the flavour fundamental'
status: todo
type: task
priority: normal
created_at: 2026-08-06T00:00:00Z
updated_at: 2026-08-26T03:24:21Z
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
