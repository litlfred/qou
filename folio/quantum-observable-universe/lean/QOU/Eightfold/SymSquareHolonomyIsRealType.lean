import QOU.Eightfold.Sym2GateFSTrichotomy

/-!
# QOU.Eightfold.SymSquareHolonomyIsRealType — the induced PGL(3) rep is real type

Route E asks for a three-dimensional object of **complex** Frobenius–Schur type
(`Sym2GateFSTrichotomy.gate_forces_complex_of_dim_three`).  There is one obvious
way to get a three-dimensional representation out of a hyperbolic knot
complement, and this file shows it is the **wrong type**, for every knot at once.

## The construction, and why it fails

A hyperbolic structure supplies `ρ₂ : π₁(S³∖K) → SL(2,ℂ)`.  The free way to
reach three dimensions is to post-compose with the symmetric square,
`Sym² : SL(2,ℂ) → SL(3,ℂ)` — the adjoint representation, `dim Sym²(V₂) = 3`.

That composite is **self-dual**, hence real or quaternionic, hence excluded:

* every `SL(2)` representation is self-dual, because the invariant alternating
  form gives `V ≅ V*` (carried as the hypothesis `SelfDualSource`);
* `Sym²` **preserves self-duality**: `V ≅ V*` gives
  `Sym² V ≅ Sym²(V*) ≅ (Sym² V)*` (`symSquare_selfDual_of_selfDual`);
* a self-dual three-dimensional candidate fails the `Sym²` gate
  (`Sym2GateFSTrichotomy`, via the even-dimension argument).

So the induced object is real type and `real_triple_fails_gate` disposes of it
in one line.  **This does not depend on the knot** — not on hyperbolicity, not
on amphichirality, not on the Milnor invariant.  It is a property of the map
`SL(2) → SL(3)`.

## What this leaves of route E

Route E is not refuted; its **cheap** construction is.  A surviving `ρ₃` must
lie in the `PGL(3,ℂ)` character variety **away from the image of `PGL(2,ℂ)`** —
a genuine higher-Teichmüller deformation (Fock–Goncharov coordinates, the
Garoufalidis–Goerner–Zickert gluing equations of `library/arxiv-1207.6711v1`),
not the composite above.  That is a sharper obligation than "exhibit `ρ₃` with
`ρ₃ ≇ ρ̄₃`": it says *where* to look and, more usefully, where not to.

It also subsumes the companion `AmphichiralHolonomyIsSelfDual` for induced
representations: that file prunes `4₁` by amphichirality; this one prunes the
`Sym²`-induced representation of **every** knot, `4₁`, `3₁` and `𝓑₃` alike.
The companion still does work the moment a *non-induced* `ρ₃` appears, because
the mirror argument does not care how `ρ₃` was built.

## Honest scope

**Scope-(a).**  Two hypotheses are carried rather than derived, and named so a
reader can see the borrow: `SelfDualSource` (every source-group representation
is self-dual — the `SL(2)` symplectic form) and the `FSType` identification of
the resulting self-duality.  Neither is proved here; both are standard, and the
second is deliberately *not* collapsed into the first, since `ρ ≅ ρ*` and a
Frobenius–Schur label are different assertions.

## Base ring (§7c)

No ring and no archimedean content: an abstract duality and an equivalence.

-- Ref: [fulton-harris1991] §11 (Frobenius–Schur; `Sym²` of the standard `SL(2)`
-- representation is the adjoint, and is orthogonal).
-- Ref: [leitner2026] `docs/audits/2026-09-04-route-e-screened-against-the-trichotomy.md`.
-/

namespace QOU.Eightfold.SymSquareHolonomyIsRealType

open QOU.Eightfold.Sym2GateFSTrichotomy

variable {Rep : Type*}

/-! ## 1. Self-duality, abstractly -/

/-- `V` is self-dual: isomorphic to its own dual. -/
def IsSelfDual (dual : Rep → Rep) (iso : Rep → Rep → Prop) (V : Rep) : Prop :=
  iso (dual V) V

/-- Every representation of the source group is self-dual — the `SL(2)`
symplectic form.  Carried as a hypothesis so the theorem names its borrow. -/
def SelfDualSource (dual : Rep → Rep) (iso : Rep → Rep → Prop) : Prop :=
  ∀ V : Rep, IsSelfDual dual iso V

/-- `Sym²` commutes with dualisation up to isomorphism, and `iso` is a
congruence for it.  The two halves the next theorem needs, bundled. -/
structure SymSquareDualCompatible (sym dual : Rep → Rep) (iso : Rep → Rep → Prop) : Prop where
  /-- `Sym²(V*) ≅ (Sym² V)*`. -/
  commutes : ∀ V, iso (sym (dual V)) (dual (sym V))
  /-- `iso` is respected by `Sym²`. -/
  congr : ∀ V W, iso V W → iso (sym V) (sym W)
  /-- `iso` is transitive. -/
  trans : ∀ U V W, iso U V → iso V W → iso U W
  /-- `iso` is symmetric. -/
  symm : ∀ V W, iso V W → iso W V

/-! ## 2. `Sym²` preserves self-duality -/

/-- **The structural step.**  If `V` is self-dual then so is `Sym² V`.

`V* ≅ V` gives `Sym²(V*) ≅ Sym² V` by congruence, and `Sym²(V*) ≅ (Sym² V)*`
by compatibility; transitivity closes it. -/
theorem symSquare_selfDual_of_selfDual
    {sym dual : Rep → Rep} {iso : Rep → Rep → Prop}
    (hc : SymSquareDualCompatible sym dual iso)
    {V : Rep} (hV : IsSelfDual dual iso V) :
    IsSelfDual dual iso (sym V) := by
  -- `Sym²(V*) ≅ Sym² V`, from `V* ≅ V` by congruence.
  have h1 : iso (sym (dual V)) (sym V) := hc.congr _ _ hV
  -- `commutes` runs `Sym²(V*) ≅ (Sym² V)*`; symmetry turns it round.
  have h2 : iso (dual (sym V)) (sym (dual V)) := hc.symm _ _ (hc.commutes V)
  exact hc.trans _ _ _ h2 h1

/-- **Every induced three-dimensional object is self-dual.**  Combining
`SelfDualSource` with §2: whatever `V` the source supplies, `Sym² V` is
self-dual — so the composite `π₁ → SL(2) → SL(3)` can never be complex type. -/
theorem induced_is_selfDual
    {sym dual : Rep → Rep} {iso : Rep → Rep → Prop}
    (hsrc : SelfDualSource dual iso)
    (hc : SymSquareDualCompatible sym dual iso)
    (V : Rep) :
    IsSelfDual dual iso (sym V) :=
  symSquare_selfDual_of_selfDual hc (hsrc V)

/-! ## 3. Composition with the gate -/

/-- **The route-E prune.**  A self-dual candidate is not the missing
three-dimensional flavour object.  Stated over the companion's model; the
`hsd` hypothesis is the `FSType` reading of §2's self-duality and is
deliberately not derived from it (see the scope note). -/
theorem selfDual_candidate_not_three {S : Finset ℕ} {fs : ℕ → FSType}
    {m dualIdx d : ℕ → ℕ}
    (hgate : Passes S fs m dualIdx)
    (hq : QuaternionicEvenDim S fs d)
    (hsd : ∀ i ∈ S, (fs i).SelfDual) :
    dimOf S m d ≠ 3 := by
  intro hdim
  obtain ⟨c, hc⟩ := even_dimOf_of_selfDual hgate hq hsd
  omega

/-- **The real-type instance, in one line.**  A real-type irrep occurring with
positive multiplicity fails the gate outright — the `Sym²`-induced case, once
its Frobenius–Schur label is read as `real`. -/
theorem realType_induced_fails_gate {S : Finset ℕ} {fs : ℕ → FSType}
    {m dualIdx : ℕ → ℕ} {i : ℕ}
    (hi : i ∈ S) (hr : fs i = .real) (hpos : 0 < m i) :
    ¬ Passes S fs m dualIdx :=
  real_triple_fails_gate hi hr hpos

/-- Iterated symmetric-square preservation of self-duality: if `V` is self-dual,
then applying `sym` twice (`sym (sym V)`) also preserves self-duality. -/
theorem symSquare_iterated_selfDual_of_selfDual
    {sym dual : Rep → Rep} {iso : Rep → Rep → Prop}
    (hc : SymSquareDualCompatible sym dual iso)
    {V : Rep} (hV : IsSelfDual dual iso V) :
    IsSelfDual dual iso (sym (sym V)) :=
  symSquare_selfDual_of_selfDual hc (symSquare_selfDual_of_selfDual hc hV)

end QOU.Eightfold.SymSquareHolonomyIsRealType
