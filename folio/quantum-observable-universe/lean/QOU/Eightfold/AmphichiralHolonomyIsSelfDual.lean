import QOU.Eightfold.Sym2GateFSTrichotomy

/-!
# QOU.Eightfold.AmphichiralHolonomyIsSelfDual — route E, narrowed to one knot

Route E (`qou-960k`, `qou-g1m8`) proposes a `PGL(3,ℂ)` decoration of the knot
complement as the source of the flavour triple.  `AmbientInvolutionDoesNotDecideType`
established what it must now exhibit: a three-dimensional object of **complex**
Frobenius–Schur type, because `Sym2GateFSTrichotomy.gate_forces_complex_of_dim_three`
excludes real and quaternionic constructions as a class.

This file prunes that obligation using a standard geometric fact together with
a property the corpus already assigns to its own knots, and the result is that
**route E survives on exactly one of the particle dictionary's three knots.**

## The argument

For a hyperbolic 3-manifold, the complex-conjugate of a holonomy representation
is the holonomy of the **mirror** manifold: `ρ̄_K ≅ ρ_{mirror K}` (carried here
as an explicit hypothesis, `MirrorConjugate`, so the theorem names what it
uses).  An **amphichiral** knot satisfies `mirror K = K`.  Composing,
`ρ̄_K ≅ ρ_K` — the holonomy is *self-dual*, hence not complex type, hence
`selfDual_holonomy_not_flavour_triple` says it cannot be the missing
three-dimensional object.

## Applied to the three knots of the dictionary

| knot | role | status | route E |
|---|---|---|---|
| `4₁` figure-eight | Higgs / mass mechanism | **amphichiral** — the corpus says so in five places (`self-dual-higgs-real-volume.md:1`, `knot-particle-dictionary.md:24`, `binding-knots-visual-inventory.md:60`, `cohomological-embedding-table2-data.md:12`, `figure-eight-reeb-theta-value.md:9`) | **pruned** by the theorem below |
| `3₁` trefoil | electron | chiral, but a **torus knot**: `Vol = 0`, complement Seifert-fibred, so no hyperbolic holonomy to conjugate (`knot-particle-dictionary.md:24`; the 2026-08-04 PGL(3) assessment §2d flags the same) | **no holonomy of this kind exists** |
| `𝓑₃` Borromean | baryon | the corpus asserts it is **not** mirror-equivalent: *"the Milnor triple linking number `μ̄(123) = ±1` distinguishes the Borromean link `𝓑₃` from its mirror `𝓑₃^σ`. No Reidemeister sequence connects them."* (`time-reversal-energy-barrier.md:17`) | **survives** |

So route E's whole remaining surface is the Borromean link — which is, and this
is not a coincidence worth passing over, the carrier the eightfold decuplet
actually needs.

## 🛑 One tension, flagged rather than silently resolved

The classical literature calls the Borromean rings **amphichiral**.  The corpus
asserts the opposite for its `𝓑₃` via `μ̄(123)`.  Both can be true of different
objects — `μ̄(123)` is an invariant of an *ordered, oriented* link and changes
sign under mirroring, while the classical amphichirality is realised by a
homeomorphism that may permute components — but the corpus does not say which
it means, and **this file does not adjudicate it.**

That question is now the whole of route E: if the classical reading wins, the
theorem below prunes `𝓑₃` too and route E is closed on every knot in the
dictionary; if the corpus's reading wins, `𝓑₃` is the one place left to look.
It is a small, sharp, checkable question, and it is cheaper than the PGL(3,ℂ)
computation it would replace.

## Scope

**Scope-(a), and narrower than it may read.**  This prunes the *holonomy* route
— a representation arising as the holonomy of a hyperbolic structure.  Route E
could in principle use a `PGL(3,ℂ)` representation that is not a holonomy, and
nothing here touches that.  What is excluded is the specific construction
`qou-52fu` proposed.

## Base ring (§7c)

No ring, no ordering, no archimedean content: the argument is an involution and
an equivalence relation.  The `FSType` half is inherited from the companion.

-- Ref: [thurston1978] (holonomy of a hyperbolic structure; conjugate holonomy
-- is the mirror's holonomy — carried as the `MirrorConjugate` hypothesis).
-- Ref: [leitner2026] `docs/audits/2026-08-04-pgl3-higher-teichmuller-assessment.md`;
-- `observations/time-reversal-energy-barrier.md` §1.
-/

namespace QOU.Eightfold.AmphichiralHolonomyIsSelfDual

open QOU.Eightfold.Sym2GateFSTrichotomy

/-! ## 1. The geometric setup, with the standard fact as a hypothesis -/

variable {Knot Rep : Type*}

/-- `K` is amphichiral: it is its own mirror. -/
def Amphichiral (mirror : Knot → Knot) (K : Knot) : Prop := mirror K = K

/-- **The standard fact, carried explicitly.**  The dual (complex-conjugate)
of a holonomy representation is the holonomy of the mirror manifold.  Stated
as a hypothesis so the theorem names exactly what it borrows from geometry. -/
def MirrorConjugate (mirror : Knot → Knot) (hol : Knot → Rep) (dual : Rep → Rep)
    (iso : Rep → Rep → Prop) : Prop :=
  ∀ K, iso (dual (hol K)) (hol (mirror K))

/-! ## 2. Amphichiral ⇒ the holonomy is self-dual -/

/-- **An amphichiral knot has a self-dual holonomy.**  No hypothesis on `iso`
beyond the mirror fact is needed: substituting `mirror K = K` into
`MirrorConjugate` is the whole proof. -/
theorem selfDual_of_amphichiral
    {mirror : Knot → Knot} {hol : Knot → Rep} {dual : Rep → Rep}
    {iso : Rep → Rep → Prop}
    (hmc : MirrorConjugate mirror hol dual iso)
    {K : Knot} (hK : Amphichiral mirror K) :
    iso (dual (hol K)) (hol K) := by
  have h := hmc K
  rwa [hK] at h

/-! ## 3. Composition with the Sym² screen

The screen is stated over the trichotomy model of the companion: an object
whose occurring irreps are all self-dual cannot have dimension three and pass
the gate.  Here it is combined with §2 into the statement route E needs. -/

/-- **The screen, restated for a route.**  A candidate all of whose occurring
irreps are self-dual is not three-dimensional-and-passing — the contrapositive
of `even_dimOf_of_selfDual`, which is what makes non-self-duality the single
checkable condition rather than one desideratum among several. -/
theorem selfDual_candidate_not_three {S : Finset ℕ} {fs : ℕ → FSType}
    {m dual d : ℕ → ℕ}
    (hgate : Passes S fs m dual)
    (hq : QuaternionicEvenDim S fs d)
    (hsd : ∀ i ∈ S, (fs i).SelfDual) :
    dimOf S m d ≠ 3 := by
  intro hdim
  obtain ⟨c, hc⟩ := even_dimOf_of_selfDual hgate hq hsd
  omega

/-- **The route-E conclusion for an amphichiral knot.**  If the holonomy's
occurring irreps are self-dual — which §2 delivers from amphichirality — then
the object it carries is not the three-dimensional flavour candidate.

The `hsd` hypothesis is the bridge from the geometric self-duality of §2 to the
representation-theoretic `FSType` of the companion.  It is stated rather than
derived **on purpose**: the two self-dualities are different notions (one is
`ρ̄ ≅ ρ`, the other is a Frobenius–Schur type), and collapsing them silently
would be exactly the ambient-vs-instance conflation this arc has been
correcting.  A user of this theorem must supply the identification. -/
theorem amphichiral_holonomy_not_flavour_triple
    {S : Finset ℕ} {fs : ℕ → FSType} {m dual d : ℕ → ℕ}
    (hgate : Passes S fs m dual)
    (hq : QuaternionicEvenDim S fs d)
    (hsd : ∀ i ∈ S, (fs i).SelfDual) :
    dimOf S m d ≠ 3 :=
  selfDual_candidate_not_three hgate hq hsd

/-! ## 4. The two self-dualities are NOT identified here

Recorded as a theorem so that a later reader cannot mistake §3's hypothesis for
a derivation.  `selfDual_of_amphichiral` produces `iso (dual (hol K)) (hol K)`,
an assertion about a representation and its dual.  `FSType.SelfDual` is an
assertion about a Frobenius–Schur label.  Nothing in this file maps one to the
other, and the statement below is what is actually available: the geometric
half, alone. -/

/-- The geometric half stands on its own, with no `FSType` content. -/
theorem geometric_half_is_all_that_is_derived
    {mirror : Knot → Knot} {hol : Knot → Rep} {dual : Rep → Rep}
    {iso : Rep → Rep → Prop}
    (hmc : MirrorConjugate mirror hol dual iso)
    {K : Knot} (hK : Amphichiral mirror K) :
    iso (dual (hol K)) (hol K) :=
  selfDual_of_amphichiral hmc hK

end QOU.Eightfold.AmphichiralHolonomyIsSelfDual
