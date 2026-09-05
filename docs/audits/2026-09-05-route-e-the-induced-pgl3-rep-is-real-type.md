# Route E: the induced PGL(3) representation is real type — and the route narrows to one knot

**Date:** 2026-09-05
**Beans:** `qou-g1m8`, `qou-960k`, `qou-52fu`, epic `qou-2q85`
**Lean:** `QOU/Eightfold/SymSquareHolonomyIsRealType.lean`,
`QOU/Eightfold/AmphichiralHolonomyIsSelfDual.lean` — both sorry-free,
`lean`-direct exit 0; the core theorems depend on **no axioms at all**.

## 0. What route E had to exhibit

`Sym2GateFSTrichotomy.gate_forces_complex_of_dim_three` (sorry-free) proves a
three-dimensional object passing the Sym² gate must contain a **complex-type**
irrep. Real and quaternionic constructions are excluded as a class. Route E's
obligation, after the 2026-09-04 screen, was therefore: exhibit
`ρ₃ : π₁(S³∖K) → PGL(3,ℂ)` with `ρ₃ ≇ ρ̄₃`.

This audit does the computation the obligation asks for — **structurally rather
than numerically**, which is what formalize-first requires when a one-line
invariant prunes the class.

## 1. The main result: the cheap construction is the wrong type, for every knot

There is one free way to get three dimensions out of a hyperbolic complement:
take the hyperbolic holonomy `ρ₂ : π₁ → SL(2,ℂ)` and post-compose with the
symmetric square `Sym² : SL(2,ℂ) → SL(3,ℂ)` — the adjoint representation,
`dim Sym²(V₂) = 3`.

**That composite is self-dual, hence real or quaternionic, hence excluded.**

* every `SL(2)` representation is self-dual (the invariant alternating form
  gives `V ≅ V*`) — carried as the hypothesis `SelfDualSource`;
* `Sym²` **preserves self-duality**: `symSquare_selfDual_of_selfDual`, proved
  from `V* ≅ V` by congruence and `Sym²(V*) ≅ (Sym² V)*` by compatibility;
* a self-dual three-dimensional candidate fails the gate
  (`selfDual_candidate_not_three`, the contrapositive of
  `even_dimOf_of_selfDual`), and a real-type one fails outright via
  `real_triple_fails_gate`.

**This does not depend on the knot.** Not on hyperbolicity, not on
amphichirality, not on the Milnor invariant. It is a property of the map
`SL(2) → SL(3)`, so it prunes `4₁`, `3₁` and `𝓑₃` at once.

What survives: a `ρ₃` in the `PGL(3,ℂ)` character variety **away from the image
of `PGL(2,ℂ)`** — a genuine higher-Teichmüller deformation (Fock–Goncharov;
the Garoufalidis–Goerner–Zickert gluing equations of
`library/arxiv-1207.6711v1`). That is a sharper obligation than the one it
replaces: it says where *not* to look.

## 2. The independent argument, and what it adds

`AmphichiralHolonomyIsSelfDual` prunes from a different direction, and it keeps
working for a `ρ₃` that is **not** induced — where §1 has nothing to say.

For a hyperbolic 3-manifold the conjugate of a holonomy is the holonomy of the
**mirror** (`MirrorConjugate`, carried explicitly). An amphichiral knot has
`mirror K = K`. Composing: `ρ̄_K ≅ ρ_K`, self-dual, excluded.

Applied to the dictionary's three knots:

| knot | role | status | route E |
|---|---|---|---|
| `4₁` figure-eight | Higgs / mass | **amphichiral**, said in five places (`self-dual-higgs-real-volume.md:1`, `knot-particle-dictionary.md:24`, `binding-knots-visual-inventory.md:60`, `cohomological-embedding-table2-data.md:12`, `figure-eight-reeb-theta-value.md:9`) | **pruned** |
| `3₁` trefoil | electron | chiral, but a **torus knot** — `Vol = 0`, Seifert-fibred, no hyperbolic holonomy to conjugate | **no such holonomy exists** |
| `𝓑₃` Borromean | baryon | the corpus asserts it is **not** mirror-equivalent — *"the Milnor triple linking number `μ̄(123) = ±1` distinguishes the Borromean link `𝓑₃` from its mirror `𝓑₃^σ`. No Reidemeister sequence connects them."* (`time-reversal-energy-barrier.md:17`) | **survives §2** |

So on the non-induced side, route E's whole remaining surface is the Borromean
link — the carrier the eightfold decuplet actually needs.

## 3. 🛑 A tension this audit does NOT resolve

The classical literature calls the Borromean rings **amphichiral**. The corpus
asserts the opposite for its `𝓑₃`, via `μ̄(123)`.

Both can be true of different objects — `μ̄(123)` is an invariant of an
*ordered, oriented* link and changes sign under mirroring, while the classical
amphichirality is realised by a homeomorphism that may permute components. The
corpus does not say which it means, and **nothing here adjudicates it.**

That question is now the whole of the non-induced half of route E. If the
classical reading wins, §2 prunes `𝓑₃` as well and route E closes on every knot
in the dictionary. If the corpus's reading wins, `𝓑₃` is the one place left.
It is small, sharp, checkable, and far cheaper than the PGL(3,ℂ) computation it
would replace.

## 3-bis. RESOLVED, same day — and it resolves AGAINST route E

§3 left the Borromean question open. It is settled, and the two statements were
never in conflict.

**`μ̄(123)` is negated by two independent operations**: mirroring, and
transposing two components (`μ̄` of length three is cyclically symmetric and
antisymmetric under a transposition). So `mirror ∘ swap` **preserves** it, and
an invariant negated by both is blind to the difference between `L` and
`mirror (swap L)` — `QOU/Eightfold/MirrorSwapCompatibility.lean`
(`negBoth_comp_fixes`, `cannot_distinguish_mirror_swap`, sorry-free). That is
exactly how the Borromean rings are amphichiral: the mirror is isotopic to the
original *after exchanging two components*.

So `time-reversal-energy-barrier.md:17` is **correct for the ordered, oriented
link** — with labels fixed, `μ̄` does separate `𝓑₃` from `𝓑₃^σ`, and the same
file proves that half too (`distinguishes_bare_mirror`). It does **not**
contradict amphichirality of the unordered link or of the complement.

**Route E's object is the complement**, and its holonomy does not see component
labels. The complement admits an orientation-reversing self-homeomorphism, and
by **Mostow rigidity** — already cited in the corpus at
`swampland-island-of-consistency.md:11` and
`approach-to-exceptional-divisor.md:11` — the discrete faithful representation
is unique up to conjugation and complex conjugation. Hence
`ρ̄_geom ≅ ρ_geom ∘ φ ≅ ρ_geom`: **self-dual**, and §2 prunes it.

**Route E is therefore closed on all three knots of the dictionary, for
geometric holonomies** — `4₁` by amphichirality, `3₁` for having no hyperbolic
holonomy at all, `𝓑₃` by this argument. With §1 pruning every `Sym²`-induced
representation regardless of knot, what survives is **only a genuinely
non-geometric `PGL(3,ℂ)` representation**: a Fock–Goncharov deformation away
from the `PGL(2)` locus. That is a route, not a construction, and nobody has
built one.

**What is NOT proved here:** that the Borromean rings are amphichiral (the
classical fact, cited) and Mostow rigidity (cited, and already load-bearing
elsewhere in the corpus). What *is* proved is the compatibility — that the
appearance of a contradiction was an artifact of reading an ordered-link claim
as a claim about the complement.

## 4. Scope, stated plainly

**Scope-(a) throughout.** §1 excludes the `Sym²`-induced representation; §2
excludes the holonomy of an amphichiral knot. Neither excludes a `PGL(3,ℂ)`
representation that is neither induced nor a holonomy, and route E is not
refuted.

Two hypotheses are carried rather than derived, and named in the Lean so the
borrow is visible: `SelfDualSource` (the `SL(2)` symplectic form) and the
`FSType` reading of the resulting self-duality. The second is **deliberately**
not collapsed into the first: `ρ ≅ ρ*` and a Frobenius–Schur label are
different assertions, and identifying them silently is the ambient-vs-instance
conflation this arc exists to correct — the same shape as
`AmbientInvolutionDoesNotDecideType`, and as correction 9 of PR #6584.

## 5. What would settle route E

In increasing cost:

1. **Adjudicate §3** — is the corpus's `𝓑₃` amphichiral or not? A reading
   question, no compute.
2. If it is not: exhibit a `PGL(3,ℂ)` representation of `π₁(S³∖𝓑₃)` outside
   the `Sym²` image, and read off whether its character is real-valued. A
   representation is self-dual iff its character is real, so a single group
   element with non-real trace settles complex type.
3. Only then does the Fock–Goncharov / GTZ machinery earn its cost.

## 6. CORRECTION, same day — the surviving branch has a NAMED, HELD construction

§5 step 3 said *"only then does the Fock–Goncharov / GTZ machinery earn its
cost"*, and §3-bis called the non-geometric branch *"a route, not a
construction, and nobody has built one."* **Both are too pessimistic. It earns
its cost now.**

**The construction is in the literature and the corpus holds the paper.**
`library/arxiv-1207.6711v1` (Garoufalidis–Goerner–Zickert) — already identified
as the one substantive rank-2 holding — states it: *"there are often several
components of representations."* Its **Ptolemy variety** parametrises
**boundary-unipotent** `PGL(n,ℂ)` representations, and the geometric one is a
single component among several. The non-geometric reps are the other components.
Seven further held directories carry Ptolemy / boundary-unipotent material
(`arxiv-0906.1500v4`, `arxiv-1002.0168v2`, `arxiv-1202.6268v2`, `2018sorus020`,
the `ant-v14-n7-s` set).

**A second, independent access route is also held: resurgence.** Twelve library
directories carry alien calculus / trans-series / Stokes constants. The decisive
one is `arxiv-2007.10190v2`, *The Resurgent Structure of Quantum Knot
Invariants*:

> *"Given a hyperbolic knot `K` there is a distinguished critical point `σ₁`
> (the geometric representation…)"*
>
> *"`ξ₃ = 0.43016…`, corresponding to the geometric representation, **its
> conjugate and the real**"*

Trans-series sectors are indexed by critical points — flat connections,
geometric and non-geometric alike — and the Stokes constants are the transition
data. So a non-geometric representation is reachable as **another saddle of the
same asymptotic series**, without building it geometrically. The corpus is
already partway onto this ground: `appendix-surreals/kashaev-surreal.md` cites
Écalle's alien calculus and "Stokes data as integer counts", and
`mass-theory/stokes-dt-bps-bridge.md` and `mass-theory/dt-spectrum-bar-eigenspace.md`
are live blocks.

**🛑 One caution, flagged because the slip would be this file's own.** That
paper distinguishes *"the geometric representation, its conjugate"* as
**different** critical points. Correct for a general hyperbolic knot, and **not**
a contradiction with §3-bis: the Mostow argument applies only where the manifold
is **amphichiral**, and there `ρ` and `ρ̄` coincide; for a chiral knot they do
not. The two statements are about different knots.

**Vocabulary note.** "non-geometric solution / flat connection / component"
returns **zero** library hits; "Ptolemy", "boundary-unipotent", "component of
the character variety" return **eight**. The material was held the whole time
under a name the obvious query does not reach — the fourth instance of that
blind spot in this arc, and the standing cost of `corpus_search` (checklist
path 0) being unavailable.

**The revised obligation**, replacing §5 step 3: take a **non-geometric Ptolemy
component at `n = 3`** for the Borromean complement and read off whether its
character is real-valued. A representation is self-dual iff its character is
real, so a **single group element with non-real trace settles complex type** —
and unlike the geometric component, nothing forces it real. **This computation
has not been done and is not claimed here.**
