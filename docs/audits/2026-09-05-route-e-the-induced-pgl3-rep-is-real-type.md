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
the Garoufalidis–Thurston–Zickert gluing equations of
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
