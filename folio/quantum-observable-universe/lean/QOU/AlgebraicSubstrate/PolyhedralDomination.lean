import QOU.AlgebraicSubstrate.DominationSqueeze

/-!
# QOU.AlgebraicSubstrate.PolyhedralDomination — the squeeze as a face test

Bean `qou-filh`. `Domination` values in a **linearly** ordered `Γ`. The natural
invariant of a q-difference equation is not a number but its **Newton polygon**,
valued in a *lattice*-ordered group (`ℤⁿ`/`ℚⁿ`): a linear order appears only
after choosing a **supporting functional**, i.e. selecting a face.

This file makes that precise, and the payoff is the translation asked for:

> an archimedean inequality *"cost exceeds budget"* becomes
> **"some supporting functional strictly separates the two valuation points"**
> — an LP-feasibility / face-membership question on the polyhedron.

`squeeze_of_face_separation` is that statement. `Face.toDomination` is why it
works: **every face specialises a polyhedral valuation to an ordinary
`Domination`**, so the whole `DominationSqueeze` toolkit applies face-by-face.

## Reading it as Newton polygons

For a linear q-difference equation the Newton polygon's slopes are the
q-Gevrey orders of its formal solutions (Ramis–Sauloy–Zhang). The corpus
already carries the one-dimensional shadow — `QOU.Mathlib.QGevreyOrder`'s
`IsQGevreyOrder q s a`, with the same reference — and that file's own docstring
lists the **Newton-polygon convolution law** as out of scope. That law is
exactly `le_val_add` here, now stated in the polyhedral (`⊓`) form it wants.

* a point of `Γ` = a Newton-polygon exponent/slope datum;
* `⊓` = the polyhedral meet (the lower hull of a sum contains the meet);
* a `Face` = a supporting functional; picking one picks a face;
* `Face.toDomination` = restricting attention to that face;
* face separation = the LP feasibility test that replaces the inequality.

## Honesty about the trivial face

`Face` is satisfiable by the constant-`⊤` functional, which separates nothing.
So a `Face` alone asserts nothing — exactly the situation `trivialError_bound`
records for `SurrealParallelTransportBound`. That is stated here as
`trivialFace` + `trivialFace_separates_nothing` rather than left as a trap: a
face carries information only once it is exhibited to separate something, which
is what `Separates` and `squeeze_of_face_separation` require.

## Scope

This is the *structural* translation. It does **not** construct the Newton
polygon of any particular QOU q-difference equation, and it does not decide any
inequality on its own — it says which question to hand to an LP solver. Building
an actual `PolyDomination` from the framework's q-difference data is the
remaining work under `qou-filh`.
-/

namespace QOU.AlgebraicSubstrate

variable {A : Type*} [AddCommGroup A]

/-- **Polyhedral domination** — a valuation into a *lattice*-ordered value
object, with the ultrametric bound stated via the meet `⊓` rather than `min`.

`Domination` is the special case where `Γ` is linearly ordered (then `⊓ = min`),
so nothing is lost; what is gained is that the value of an element can be a
polygon datum rather than a single grade. -/
structure PolyDomination (A : Type*) [AddCommGroup A]
    (Γ : Type*) [SemilatticeInf Γ] where
  /-- Polyhedral grade — a Newton-polygon datum, not necessarily a number. -/
  val : A → WithTop Γ
  /-- Zero is infinitely deep. -/
  val_zero : val 0 = ⊤
  /-- Negation preserves the polygon. -/
  val_neg : ∀ a, val (-a) = val a
  /-- Newton-polygon / ultrametric law in polyhedral form. -/
  le_val_add : ∀ a b, val a ⊓ val b ≤ val (a + b)

variable {Γ : Type*} [SemilatticeInf Γ] {Δ : Type*} [LinearOrder Δ]

/-- **A supporting functional — a choice of face.**

`φ` sends polygon data to a linearly ordered scale, carrying the polyhedral meet
to `min`. Choosing such a `φ` is choosing the direction in which the polygon is
read, i.e. selecting a face. -/
structure Face (P : PolyDomination A Γ) (Δ : Type*) [LinearOrder Δ] where
  /-- The functional, already lifted to the `⊤`-adjoined value object. -/
  φ : WithTop Γ → WithTop Δ
  /-- Depth is preserved. -/
  map_top : φ ⊤ = ⊤
  /-- The polyhedral meet becomes the linear `min` — this is what makes the
      face a legitimate reading of the polygon. -/
  map_inf : ∀ x y, φ (x ⊓ y) = min (φ x) (φ y)
  /-- The functional is monotone (implied by `map_inf`, kept as a field so the
      specialisation below needs no lattice lemmas). -/
  mono : ∀ {x y}, x ≤ y → φ x ≤ φ y

namespace Face

variable {P : PolyDomination A Γ} (F : Face P Δ)

/-- **Every face specialises a polyhedral valuation to a `Domination`.**

This is the bridge: after choosing a face, the entire `DominationSqueeze`
toolkit — strict domination, non-cancellation, the tower lemmas — applies
verbatim. -/
def toDomination : Domination A Δ where
  val := F.φ ∘ P.val
  val_zero := by simp [Function.comp, P.val_zero, F.map_top]
  val_neg a := by simp [Function.comp, P.val_neg]
  le_val_add a b := by
    simpa [Function.comp, F.map_inf] using F.mono (P.le_val_add a b)

@[simp] theorem toDomination_val (a : A) :
    (F.toDomination).val a = F.φ (P.val a) := by
  dsimp [toDomination]

/-- The face **separates** `a` from `b` when it reads `a` as strictly
dominant. This is the LP-feasibility predicate. -/
def Separates (a b : A) : Prop := F.φ (P.val a) < F.φ (P.val b)

end Face

/-- **The face-membership test — the translation.**

An archimedean inequality *"the cost strictly exceeds the budget, so the budget
cannot absorb it"* is replaced by a question about the Newton polygon: **does
some supporting functional strictly separate the two valuation points?** If one
does, the conclusion follows with no ordered field, no `ℝ`, and no surreals.

That question — *is this point strictly below that one along some admissible
direction* — is exactly an LP feasibility test on the polyhedron. -/
theorem squeeze_of_face_separation {P : PolyDomination A Γ} (F : Face P Δ)
    {cost budget : A} (h : F.Separates cost budget) : cost + budget ≠ 0 :=
  (F.toDomination).add_ne_zero_of_val_lt h

/-- Separation also pins the grade of the sum on that face: the dominant
term's reading survives. -/
theorem face_val_add_eq {P : PolyDomination A Γ} (F : Face P Δ)
    {cost budget : A} (h : F.Separates cost budget) :
    F.φ (P.val (cost + budget)) = F.φ (P.val cost) :=
  (F.toDomination).val_add_eq_of_lt h

/-! ## The trivial face, stated rather than hidden -/

/-- The constant-`⊤` functional. It is a legitimate `Face` and separates
nothing. -/
def trivialFace (P : PolyDomination A Γ) : Face P Δ where
  φ := fun _ => ⊤
  map_top := rfl
  map_inf := by simp
  mono := by simp

/-- **A `Face` on its own asserts nothing.** The trivial face separates no pair,
so `squeeze_of_face_separation` has content only for a face exhibited to
separate — the LP test must actually be *run*, not merely posited. -/
theorem trivialFace_separates_nothing (P : PolyDomination A Γ) (a b : A) :
    ¬ (trivialFace (Δ := Δ) P).Separates a b := by
  dsimp [Face.Separates, trivialFace]
  exact lt_irrefl ⊤

/-- Face separation is asymmetric and forces the difference `cost - budget` to be
non-zero via negation invariance of the polyhedral valuation. -/
theorem squeeze_sub_of_face_separation {P : PolyDomination A Γ} (F : Face P Δ)
    {cost budget : A} (h : F.Separates cost budget) :
    ¬ F.Separates budget cost ∧ cost - budget ≠ 0 := by
  constructor
  · dsimp [Face.Separates] at h ⊢
    exact lt_asymm h
  · have hneg : F.Separates cost (-budget) := by
      dsimp [Face.Separates] at h ⊢
      rw [P.val_neg]
      exact h
    have hadd : cost + (-budget) ≠ 0 := squeeze_of_face_separation F hneg
    rwa [sub_eq_add_neg]

/-! ## `Domination` is the one-face case -/

/-- Every ordinary `Domination` is a `PolyDomination` on a linear order — the
polygon has a single face. So the polyhedral setting is a strict generalisation
and nothing already proved is lost. -/
def Domination.toPoly {Δ : Type*} [LinearOrder Δ] (D : Domination A Δ) :
    PolyDomination A Δ where
  val := D.val
  val_zero := D.val_zero
  val_neg := D.val_neg
  le_val_add a b := D.le_val_add a b

end QOU.AlgebraicSubstrate
