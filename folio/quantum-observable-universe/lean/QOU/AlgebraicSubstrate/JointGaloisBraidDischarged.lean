import Mathlib.Tactic

/-!
# Joint Galois × braid action — general discharge (conditional class form)

Compiled formalisation of `prop:joint-galois-braid-discharged`.
Sibling narrative at
`stochastic-mechanics/joint-galois-braid-discharged.md`.

The manuscript argues the joint motivic-Galois × braid action commutes
on every bi-filtration cell *structurally*: "the two actions touch
disjoint factors of the bi-filtration's underlying tensor structure."

This file encodes that argument honestly (§3b-cond). The genuine
hypothesis — the disjoint tensor decomposition `Cell ≅ A ⊗ B` on which
the Galois action moves only the `A` factor and the braid action moves
only the `B` factor — is carried as the *fields* of a content-bearing
class. Commutation is then **derived**, not assumed, from those
hypotheses by the bifunctorial interchange law (`galoisA ⊗ id` and
`id ⊗ braidB` act on disjoint coordinates).

The genuinely-unwritten domain math — that the concrete `𝓗_q^{(n,K)}`
with its actual motivic-Galois and braid actions realises this disjoint
split — is the *instance* for the concrete cell, which is left
unbuilt (open primary, §3b-tax): the general theorem below is
fully verified modulo that single named categorical input.
-/

namespace QOU.AlgebraicSubstrate.JointGaloisBraidDischarged

/-- **Conditional-class hypotheses for `prop:joint-galois-braid-discharged`.**

Encodes the manuscript's *structural input* (not its conclusion): the
bi-filtration cell splits as a disjoint tensor product `Cell ≅ A ⊗ B`
(here modeled at the underlying-set level as an injection
`decomp : Cell → A × B`), the motivic-Galois action moves only the `A`
factor (`galois = galoisA ⊗ id`), and the braid action moves only the
`B` factor (`braid = id ⊗ braidB`).

The fields are genuine hypotheses — the disjoint-factor intertwining
equations — from which commutation is *derived* in
`joint_action_discharged`, never assumed. In particular there is no
field asserting "galois commutes with every function"; that would be
the conclusion in disguise. -/
class JointGaloisBraidDecomposition where
  /-- The bi-filtration cell carrier. -/
  Cell : Type
  /-- Left tensor factor — the motivic-Galois action sees only this. -/
  A : Type
  /-- Right tensor factor — the braid action sees only this. -/
  B : Type
  /-- Motivic-Galois group elements. -/
  GaloisAction : Type
  /-- Braid group elements. -/
  BraidAction : Type
  /-- The disjoint tensor decomposition `Cell ↪ A ⊗ B`
      (underlying-set image of the categorical iso). -/
  decomp : Cell → A × B
  /-- A tensor iso is injective on underlying sets: the decomposition
      separates points of the cell. -/
  decomp_inj : Function.Injective decomp
  /-- The motivic-Galois action on the whole cell. -/
  galois : GaloisAction → Cell → Cell
  /-- The braid action on the whole cell. -/
  braid : BraidAction → Cell → Cell
  /-- The motivic-Galois action restricted to the left factor `A`. -/
  galoisA : GaloisAction → A → A
  /-- The braid action restricted to the right factor `B`. -/
  braidB : BraidAction → B → B
  /-- **Disjointness hypothesis (Galois ↦ A-factor).** Under the
      decomposition the Galois action is `galoisA ⊗ id`: it moves the
      `A`-coordinate and fixes the `B`-coordinate. -/
  galois_on_A : ∀ (g : GaloisAction) (x : Cell),
    decomp (galois g x) = (galoisA g (decomp x).1, (decomp x).2)
  /-- **Disjointness hypothesis (braid ↦ B-factor).** Under the
      decomposition the braid action is `id ⊗ braidB`: it moves the
      `B`-coordinate and fixes the `A`-coordinate. -/
  braid_on_B : ∀ (b : BraidAction) (x : Cell),
    decomp (braid b x) = ((decomp x).1, braidB b (decomp x).2)

/-- **Proposition (`prop:joint-galois-braid-discharged`, conditional on
    [`JointGaloisBraidDecomposition`]).**

    The joint motivic-Galois × braid action commutes on every
    bi-filtration cell:
    `galois g (braid b x) = braid b (galois g x)`.

    **Derived — not assumed.** Applying `decomp` to both sides, the
    disjoint-factor hypotheses `galois_on_A` and `braid_on_B` send each
    composite to the single pair `(galoisA g a, braidB b b')` — the
    interchange law for `galoisA ⊗ id` and `id ⊗ braidB` acting on
    disjoint coordinates — and injectivity of `decomp` transports the
    equality back to `Cell`. The only unproved input in the chain is the
    class instance for the concrete `𝓗_q^{(n,K)}` (left unbuilt). -/
theorem joint_action_discharged [ctx : JointGaloisBraidDecomposition] :
    ∀ (g : ctx.GaloisAction) (b : ctx.BraidAction) (x : ctx.Cell),
      ctx.galois g (ctx.braid b x) = ctx.braid b (ctx.galois g x) := by
  intro g b x
  -- It suffices to prove the images under the separating decomposition
  -- are equal.
  apply ctx.decomp_inj
  -- Both sides normalise, through the two disjoint-factor hypotheses and
  -- the `Prod` projection reductions, to `(galoisA g a, braidB b b')`.
  simp only [ctx.galois_on_A, ctx.braid_on_B]

/-- Iterated braid-word action on a bi-filtration cell `ctx.Cell`. -/
def braidWordAction [ctx : JointGaloisBraidDecomposition]
    (w : List ctx.BraidAction) (x : ctx.Cell) : ctx.Cell :=
  w.foldr (fun b acc => ctx.braid b acc) x

/-- **Word-level joint Galois × braid commutation.**
    For any motivic-Galois element `g` and any braid word `w`, the Galois
    action commutes with the iterated braid-word action `braidWordAction w`. -/
theorem joint_word_action_discharged [ctx : JointGaloisBraidDecomposition]
    (g : ctx.GaloisAction) (w : List ctx.BraidAction) (x : ctx.Cell) :
    ctx.galois g (braidWordAction w x) = braidWordAction w (ctx.galois g x) := by
  induction w with
  | nil => rfl
  | cons b rest ih =>
      show ctx.galois g (ctx.braid b (braidWordAction rest x))
          = ctx.braid b (braidWordAction rest (ctx.galois g x))
      rw [joint_action_discharged g b, ih]

/-- Canonical cartesian-product model of `JointGaloisBraidDecomposition` for
    any pair of factor types `(A₀, B₀)`: the cell is `A₀ × B₀`, `galois` acts
    by endomorphisms on the left coordinate `A₀`, and `braid` acts by
    endomorphisms on the right coordinate `B₀`. -/
def productJointGaloisBraidDecomposition (A₀ B₀ : Type) :
    JointGaloisBraidDecomposition where
  Cell := A₀ × B₀
  A := A₀
  B := B₀
  GaloisAction := A₀ → A₀
  BraidAction := B₀ → B₀
  decomp := id
  decomp_inj := Function.injective_id
  galois := fun g p => (g p.1, p.2)
  braid := fun b p => (p.1, b p.2)
  galoisA := fun g a => g a
  braidB := fun b b' => b b'
  galois_on_A := fun _ _ => rfl
  braid_on_B := fun _ _ => rfl

/-- `JointGaloisBraidDecomposition` is non-vacuously inhabitable. -/
theorem nonempty_jointGaloisBraidDecomposition :
    Nonempty JointGaloisBraidDecomposition :=
  ⟨productJointGaloisBraidDecomposition ℤ ℤ⟩

-- Ref: [leitner2026] quantum-observable-universe/stochastic-mechanics/joint-galois-braid-discharged.md

end QOU.AlgebraicSubstrate.JointGaloisBraidDischarged