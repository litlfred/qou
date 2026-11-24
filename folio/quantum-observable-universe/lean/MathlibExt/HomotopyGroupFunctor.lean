import Mathlib.Topology.Homotopy.HomotopyGroup
import Mathlib.Tactic

/-!
# QOU.Mathlib.HomotopyGroupFunctor — `π_n` of a map

Bean `qou-de7r`. Mathlib defines `HomotopyGroup N X x` but **not the induced
map**: a survey of `Mathlib.Topology.Homotopy.HomotopyGroup` by enumerating its
declarations turns up `GenLoop.transAt`, `symmAt`, `toLoop`, `fromLoop`, `copy`,
the group instances and the `π₀`/`π₁` comparison equivalences — and no `map`,
on either `GenLoop` or `HomotopyGroup`. Without it `π_n` is a family of groups
with no morphisms between them, which is not enough to state any exact sequence.

This file supplies the missing arrow and its functoriality.

## What is proved

* `genLoopMap f hf g = f ∘ g` — a based map pushes a based cube forward. The
  boundary condition survives because `f` sends the old basepoint to the new
  one, which is the entire content of `hf`.
* `homotopyGroupMap f hf : π_N(X, x) → π_N(Y, y)`, well defined on classes.
  Mathlib's `ContinuousMap.HomotopicRel.comp_continuousMap` does the work; the
  only thing added is the observation that it applies verbatim, since
  `GenLoop.Homotopic` *is* `HomotopicRel` relative to `Cube.boundary N`.
* Functoriality: `homotopyGroupMap_id`, `homotopyGroupMap_comp`.
* `homotopyGroupMap_const` — a constant map induces the trivial map. This is
  the half of exactness at the middle spot that needs no fibration, and it is
  the reason `p ∘ ι` being constant on the fibre is worth writing down.
* `homotopyGroupHom` — the same map as a `MonoidHom`, for `N` nonempty with
  decidable equality (Mathlib's hypotheses for the group structure). `map_mul`
  reduces to `f (if P then u else v) = if P then f u else f v`, because
  `GenLoop.transAt` carries an explicit pointwise formula through
  `GenLoop.copy`.

## What is assumed

Nothing. There is no fibration hypothesis anywhere in this file — an induced
map exists for any based continuous map, and saying so separately from the
lifting theory is what keeps the fibration hypothesis in
`FibrationExactness.lean` honest about where it is actually used.

## Index type

`N` is an arbitrary type throughout, matching Mathlib, rather than `Fin n`.
`HomotopyGroup.Pi n X x` (`π_ n X x`) is `HomotopyGroup (Fin n) X x`, so every
result here specialises to it; stating them for `Fin n` only would have been a
gratuitous restriction, and `Cube.boundary` never needed the finiteness.

-- Ref: [leitner2026] quantum-observable-universe/quantum-observable-universes
-/

namespace QOU.Mathlib.HomotopyGroupFunctor

open unitInterval ContinuousMap

universe uN uX uY uZ

variable {N : Type uN} {X : Type uX} {Y : Type uY} {Z : Type uZ}
  [TopologicalSpace X] [TopologicalSpace Y] [TopologicalSpace Z]
  {x : X} {y : Y} {z : Z}

/-- **Pushing a based cube forward.** If `f x = y`, post-composition with `f`
    carries `Ω^N x` into `Ω^N y`: the composite is continuous, and on
    `Cube.boundary N` it takes the value `f x = y`. -/
def genLoopMap (f : C(X, Y)) (hf : f x = y) (g : GenLoop N X x) : GenLoop N Y y :=
  ⟨f.comp (g : C(N → I, X)), fun t ht => by
    show f ((g : C(N → I, X)) t) = y
    rw [g.2 t ht, hf]⟩

@[simp] theorem genLoopMap_coe (f : C(X, Y)) (hf : f x = y) (g : GenLoop N X x) :
    ((genLoopMap f hf g : GenLoop N Y y) : C(N → I, Y)) = f.comp (g : C(N → I, X)) :=
  rfl

@[simp] theorem genLoopMap_apply (f : C(X, Y)) (hf : f x = y) (g : GenLoop N X x)
    (t : N → I) : genLoopMap f hf g t = f (g t) :=
  rfl

/-- Post-composition respects homotopy rel the boundary — so it descends to
    homotopy classes. This is `ContinuousMap.HomotopicRel.comp_continuousMap`
    with no adaptation, because `GenLoop.Homotopic` unfolds to `HomotopicRel`
    relative to `Cube.boundary N`. -/
theorem genLoopMap_homotopic (f : C(X, Y)) (hf : f x = y) {g₁ g₂ : GenLoop N X x}
    (h : GenLoop.Homotopic g₁ g₂) :
    GenLoop.Homotopic (genLoopMap f hf g₁) (genLoopMap f hf g₂) :=
  h.comp_continuousMap f

/-- **The induced map on homotopy groups**, `π_N(X, x) → π_N(Y, y)`. -/
def homotopyGroupMap (f : C(X, Y)) (hf : f x = y) :
    HomotopyGroup N X x → HomotopyGroup N Y y :=
  Quotient.map (genLoopMap f hf) fun _ _ h => genLoopMap_homotopic f hf h

@[simp] theorem homotopyGroupMap_mk (f : C(X, Y)) (hf : f x = y) (g : GenLoop N X x) :
    homotopyGroupMap (N := N) f hf ⟦g⟧ = ⟦genLoopMap f hf g⟧ :=
  rfl

/-- Functoriality, first half: the identity induces the identity. -/
@[simp] theorem homotopyGroupMap_id (x : X) :
    homotopyGroupMap (N := N) (x := x) (y := x) (ContinuousMap.id X) rfl = id := by
  funext q
  induction q using Quotient.inductionOn with
  | _ g => exact congrArg _ (GenLoop.ext _ _ fun _ => rfl)

/-- Functoriality, second half: a composite induces the composite. Stated with
    the two basepoint equations separate rather than derived, so it can be used
    in either direction without rewriting under a proof term. -/
theorem homotopyGroupMap_comp (f : C(X, Y)) (hf : f x = y) (g : C(Y, Z)) (hg : g y = z) :
    homotopyGroupMap (N := N) (g.comp f) (by rw [ContinuousMap.comp_apply, hf, hg]) =
      homotopyGroupMap g hg ∘ homotopyGroupMap f hf := by
  funext q
  induction q using Quotient.inductionOn with
  | _ a => exact congrArg _ (GenLoop.ext _ _ fun _ => rfl)

/-- A constant map kills every class. The induced map factors through
    `π_N(point)`, which is trivial — but no such factorisation is needed: the
    pushforward of any cube along a constant map *is* the constant cube, on the
    nose.

    This is the easy half of exactness at the middle spot of the fibration
    sequence. `p ∘ ι` is constant on the fibre for the reason the fibre exists,
    so `p_* ∘ ι_* = 1` with no lifting property in sight. -/
@[simp] theorem homotopyGroupMap_const (q : HomotopyGroup N X x) :
    homotopyGroupMap (ContinuousMap.const X y) rfl q = ⟦GenLoop.const⟧ := by
  induction q using Quotient.inductionOn with
  | _ g => exact congrArg _ (GenLoop.ext _ _ fun _ => rfl)

section Group

variable [DecidableEq N]

/-- Post-composition commutes with `GenLoop.transAt`.

    `transAt` is built as a `GenLoop.copy` of `fromLoop (toLoop a ⬝ toLoop b)`
    whose *stated* underlying function is the explicit reparametrised
    `if ↑(t i) ≤ 1/2 then a … else b …`. So the claim is
    `f (if P then u else v) = if P then f u else f v`, i.e. `apply_ite` — no
    path-algebra reasoning is needed at all. -/
theorem genLoopMap_transAt (f : C(X, Y)) (hf : f x = y) (i : N) (a b : GenLoop N X x) :
    genLoopMap f hf (GenLoop.transAt i a b) =
      GenLoop.transAt i (genLoopMap f hf a) (genLoopMap f hf b) := by
  refine GenLoop.ext _ _ fun t => ?_
  show f (GenLoop.transAt i a b t) = GenLoop.transAt i _ _ t
  simp only [GenLoop.transAt, GenLoop.coe_copy]
  exact apply_ite (f ·) _ _ _

variable [Nonempty N]

/-- The unit is the class of the constant cube — Mathlib's `HomotopyGroup.one_def`
    restated as a `simp` lemma in the direction rewriting wants. -/
theorem one_eq_const_mk :
    (1 : HomotopyGroup N X x) = ⟦GenLoop.const⟧ :=
  HomotopyGroup.one_def

/-- **The induced map is a group homomorphism** (for `N` nonempty, which is
    Mathlib's hypothesis for `π_N` being a group at all). -/
def homotopyGroupHom (f : C(X, Y)) (hf : f x = y) :
    HomotopyGroup N X x →* HomotopyGroup N Y y where
  toFun := homotopyGroupMap f hf
  map_one' := by
    rw [one_eq_const_mk (N := N) (x := x), homotopyGroupMap_mk,
      one_eq_const_mk (N := N) (x := y)]
    exact congrArg _ (GenLoop.ext _ _ fun _ => hf)
  map_mul' a b := by
    induction a using Quotient.inductionOn with
    | _ a =>
      induction b using Quotient.inductionOn with
      | _ b =>
        simp only [HomotopyGroup.mul_spec (i := Classical.arbitrary N), homotopyGroupMap_mk,
          genLoopMap_transAt]

@[simp] theorem homotopyGroupHom_apply (f : C(X, Y)) (hf : f x = y) (q : HomotopyGroup N X x) :
    homotopyGroupHom f hf q = homotopyGroupMap f hf q :=
  rfl

/-- The homomorphism induced by a constant map is trivial. The group-theoretic
    form of `homotopyGroupMap_const`, which is what a statement about kernels
    consumes. -/
theorem homotopyGroupHom_const :
    homotopyGroupHom (N := N) (x := x) (ContinuousMap.const X y) rfl = 1 := by
  ext q
  simpa using (one_eq_const_mk (N := N) (x := y)).symm

end Group

end QOU.Mathlib.HomotopyGroupFunctor
