import QOU.Mathlib.HomotopyLifting
import QOU.Mathlib.HomotopyGroupFunctor

/-!
# QOU.Mathlib.FibrationExactness — exactness at the middle spot

Bean `qou-de7r`. For `p : E → B` with `p e = b` and `F = p⁻¹(b)`, the sequence

    π_N(F, e) → π_N(E, e) → π_N(B, b)

is exact at `π_N(E, e)`. That is the theorem this file proves, and it is the
only spot of the homotopy long exact sequence that can be reached without the
connecting map.

## What is proved

* `fibre_comp_eq_const` — the composite is trivial. No hypothesis at all:
  `p ∘ ι` is the constant map `b`, because that is what it means to be the
  fibre, so `homotopyGroupMap_const` finishes it.
* `exists_preimage_of_map_eq_const` — the converse, **from the stationary
  relative homotopy lifting property**. A class in `π_N(E, e)` killed by `p_*`
  comes from the fibre.
* `homotopyGroupMap_eq_const_iff` — the two together, as an iff, at the level
  of pointed sets: no group structure, hence no `Nonempty N`, is needed to
  state or prove it.
* `range_homotopyGroupHom_eq_ker` — the same statement as `range = ker` of
  `MonoidHom`s, once `N` is nonempty with decidable equality so that Mathlib's
  group structure exists.
* `injective_homotopyGroupHom_of_subsingleton_fibre` — a vanishing `π_N(F)`
  makes `p_*` injective. The topological instance of
  `LongExactSequence.injective_iff_prev_eq_zero`, and the reason one exact spot
  is already worth something.
* `pi_range_eq_ker` — the same, spelled at `Fin (n + 1)` so that it is visibly
  about `π_{n+1}`; `pi_eq_homotopyGroup` records that Mathlib's
  `HomotopyGroup.Pi` is that group definitionally.
* `Prod.homotopyGroupMap_fst_eq_const_iff` — the theorem instantiated at a
  trivial bundle `B × F → B`, where the lifting hypothesis is discharged
  outright by `Prod.hasHomotopyLiftingPropertyRel_fst`. This is what keeps the
  main theorem from being a statement about the empty set of fibrations.

## What is assumed, and why exactly that

The hypothesis is `HasHomotopyLiftingPropertyRel p (N → I) (Cube.boundary N)`:
homotopies that do not move on the boundary of the cube lift to homotopies that
do not move on the boundary of the cube.

The plain homotopy lifting property is **not** enough, and the reason is worth
stating because it is the whole difficulty. Lifting a nullhomotopy of `p ∘ g`
does produce a map `Iᴺ → E` landing in `F`. But the lifted homotopy is
unconstrained on `∂Iᴺ`, so the endpoint need not send `∂Iᴺ` to the basepoint —
it is not an element of `Ω^N e` at all, and there is no class to exhibit.
Pinning the boundary is the content, not the bookkeeping.

Classically the two properties agree for cubes, via the pair homeomorphism
`(Iⁿ × I, Iⁿ × {0} ∪ ∂Iⁿ × I) ≅ (Iⁿ × I, Iⁿ × {0})`. That homeomorphism is
**not proved** in this development; it is named `SerreCubePairBridge` in
`QOU.Mathlib.HomotopyLifting` and is used nowhere. So a reader converting a
Serre fibration into the hypothesis below still has that step to do.

## What is missing

The connecting map `δ : π_n(B, b) → π_{n-1}(F, e)` and exactness at the two
other spots. `δ` is where the degree shift enters, and Mathlib's `GenLoop` gives
no ready handle on it: it would need the identification of `π_n(E, F, e)` with
`π_n(B, b)`, hence relative homotopy groups, which Mathlib does not have either.
Nothing here is a step towards it beyond the lifting predicate, and nothing here
should be read as one.

Consequently this does **not** yet feed `QOU.Mathlib.LongExactSequence`: that
structure wants `R`-modules and `ℤ`-indexed maps exact at every spot, and what
is proved here is one spot of a sequence of (generally non-abelian) groups.

-- Ref: [leitner2026] quantum-observable-universe/quantum-observable-universes
-/

namespace QOU.Mathlib.FibrationExactness

open unitInterval ContinuousMap QOU.Mathlib.HomotopyLifting QOU.Mathlib.HomotopyGroupFunctor

universe uN uE uB uF

variable {E : Type uE} {B : Type uB} [TopologicalSpace E] [TopologicalSpace B]

/-- **The fibre** of `p` over `b`, as a subspace of `E`. -/
def Fibre (p : C(E, B)) (b : B) : Set E := p ⁻¹' {b}

@[simp] theorem mem_fibre {p : C(E, B)} {b : B} {w : E} : w ∈ Fibre p b ↔ p w = b := Iff.rfl

/-- **The inclusion of the fibre**, `F ↪ E`. -/
def fibreIncl (p : C(E, B)) (b : B) : C(Fibre p b, E) := ⟨Subtype.val, continuous_subtype_val⟩

@[simp] theorem fibreIncl_apply {p : C(E, B)} {b : B} (w : Fibre p b) :
    fibreIncl p b w = (w : E) := rfl

/-- `p` restricted to the fibre is constant. This is the definition of the
    fibre read as an equation between continuous maps, and it is the only
    ingredient in the easy half of exactness. -/
theorem comp_fibreIncl (p : C(E, B)) (b : B) :
    p.comp (fibreIncl p b) = ContinuousMap.const (Fibre p b) b :=
  ContinuousMap.ext fun w => w.2

section Exactness

variable {N : Type uN} (p : C(E, B)) {e : E} {b : B}

/-- **Half of exactness, with no hypothesis.** The composite
    `π_N(F) → π_N(E) → π_N(B)` is trivial, because `p ∘ ι` is constant. -/
theorem fibre_comp_eq_const (he : p e = b)
    (r : HomotopyGroup N (Fibre p b) (⟨e, he⟩ : Fibre p b)) :
    homotopyGroupMap p he (homotopyGroupMap (fibreIncl p b) rfl r)
      = (⟦GenLoop.const⟧ : HomotopyGroup N B b) := by
  induction r using Quotient.inductionOn with
  | _ g =>
    have hg : genLoopMap p he (genLoopMap (fibreIncl p b) rfl g)
        = (GenLoop.const : GenLoop N B b) := GenLoop.ext _ _ fun t => (g t).2
    exact congrArg _ hg

/-- **The other half, and the place the fibration hypothesis is spent.**

    If `p_* ⟦g⟧` is trivial, then `g` is homotopic rel `∂Iᴺ` to a cube that
    lands in the fibre. Lift the nullhomotopy of `p ∘ g`; its endpoint lands in
    `F` because the homotopy ended at `b`, and it is *based* because the lift
    was chosen not to move on `∂Iᴺ`. The lifted homotopy is itself the homotopy
    exhibiting the two classes as equal — no second construction is needed. -/
theorem exists_preimage_of_map_eq_const (he : p e = b)
    (hlift : HasHomotopyLiftingPropertyRel p (N → I) (Cube.boundary N))
    (g : GenLoop N E e)
    (h : (⟦genLoopMap p he g⟧ : HomotopyGroup N B b) = ⟦GenLoop.const⟧) :
    ∃ r : HomotopyGroup N (Fibre p b) (⟨e, he⟩ : Fibre p b),
      homotopyGroupMap (fibreIncl p b) rfl r = (⟦g⟧ : HomotopyGroup N E e) := by
  obtain ⟨Hr⟩ := Quotient.exact h
  -- `H` is the nullhomotopy of `p ∘ g`, stationary on `∂Iᴺ` because both ends
  -- are the basepoint there.
  set H : C(I × (N → I), B) := Hr.toContinuousMap
  obtain ⟨H', hpH', hH'0, hH'A⟩ := hlift H (g : C(N → I, E))
    (fun t => (Hr.map_zero_left t).symm)
    (fun s t ht => (Hr.eq_fst s ht).trans (Hr.map_zero_left t).symm)
  -- The endpoint of the lift lands in the fibre and is based.
  have hone : ∀ t : N → I, p (H' (1, t)) = b := fun t => by
    rw [hpH' (1, t)]; exact Hr.map_one_left t
  have hcont : Continuous fun t : N → I => H' (1, t) := by fun_prop
  let gF : C(N → I, Fibre p b) := ⟨fun t => ⟨H' (1, t), hone t⟩, hcont.subtype_mk _⟩
  have hmem : gF ∈ GenLoop N (Fibre p b) (⟨e, he⟩ : Fibre p b) := fun t ht =>
    Subtype.ext (by simpa using (hH'A 1 t ht).trans (g.2 t ht))
  refine ⟨⟦⟨gF, hmem⟩⟧, Quotient.sound ⟨?_⟩⟩
  -- `H'` itself is the homotopy rel `∂Iᴺ` from `g` to the new cube.
  exact ContinuousMap.HomotopyRel.symm
    { toContinuousMap := H'
      map_zero_left := hH'0
      map_one_left := fun _ => rfl
      prop' := fun s t ht => hH'A s t ht }

/-- **Exactness at `π_N(E, e)`**, as pointed sets.

    Stated with `⟦GenLoop.const⟧` rather than `1` on purpose: the identity is
    true for every index type `N`, including empty and singleton ones where
    Mathlib's group structure is unavailable. `range_homotopyGroupHom_eq_ker`
    below is the group-theoretic reading, and it is strictly less general. -/
theorem homotopyGroupMap_eq_const_iff (he : p e = b)
    (hlift : HasHomotopyLiftingPropertyRel p (N → I) (Cube.boundary N))
    (q : HomotopyGroup N E e) :
    homotopyGroupMap p he q = (⟦GenLoop.const⟧ : HomotopyGroup N B b) ↔
      ∃ r : HomotopyGroup N (Fibre p b) (⟨e, he⟩ : Fibre p b),
        homotopyGroupMap (fibreIncl p b) rfl r = q := by
  induction q using Quotient.inductionOn with
  | _ g =>
    constructor
    · exact fun h => exists_preimage_of_map_eq_const p he hlift g h
    · rintro ⟨r, hr⟩
      exact hr ▸ fibre_comp_eq_const p he r

end Exactness

section Group

variable {N : Type uN} [DecidableEq N] [Nonempty N] (p : C(E, B)) {e : E} {b : B}

/-- **Exactness at `π_N(E, e)` as `range = ker`.**

    The same theorem as `homotopyGroupMap_eq_const_iff`, phrased the way an
    exact sequence is normally quoted. It needs `Nonempty N` only because that
    is when `π_N` is a group at all — no extra topology is used. -/
theorem range_homotopyGroupHom_eq_ker (he : p e = b)
    (hlift : HasHomotopyLiftingPropertyRel p (N → I) (Cube.boundary N)) :
    (homotopyGroupHom (N := N) (x := (⟨e, he⟩ : Fibre p b)) (y := e)
        (fibreIncl p b) rfl).range =
      (homotopyGroupHom (N := N) p he).ker := by
  ext q
  rw [MonoidHom.mem_range, MonoidHom.mem_ker, one_eq_const_mk (N := N) (x := b)]
  simp only [homotopyGroupHom_apply]
  exact (homotopyGroupMap_eq_const_iff p he hlift q).symm

/-- **A vanishing fibre group makes `p_*` injective.**

    This is `QOU.Mathlib.LongExactSequence.injective_iff_prev_eq_zero` in its
    topological habitat, and it is the reason exactness at one spot is worth
    having on its own: injectivity of `p_*` is not a fact about `p_*`, it is a
    fact about `π_N(F)`. Nothing else in the sequence is needed. -/
theorem injective_homotopyGroupHom_of_subsingleton_fibre (he : p e = b)
    (hlift : HasHomotopyLiftingPropertyRel p (N → I) (Cube.boundary N))
    [Subsingleton (HomotopyGroup N (Fibre p b) (⟨e, he⟩ : Fibre p b))] :
    Function.Injective (homotopyGroupHom (N := N) p he) := by
  rw [← MonoidHom.ker_eq_bot_iff, ← range_homotopyGroupHom_eq_ker p he hlift, eq_bot_iff]
  intro q hq
  obtain ⟨r, rfl⟩ := MonoidHom.mem_range.mp hq
  rw [Subsingleton.elim r 1, map_one]
  exact Subgroup.one_mem _

end Group

section Pi

variable {n : ℕ} (p : C(E, B)) {e : E} {b : B}

/-- `π_n` in Mathlib's `HomotopyGroup.Pi` spelling is the `Fin n`-indexed
    homotopy group, definitionally. Recorded so the results above are visibly
    about `π_n` and not about some neighbouring object. -/
theorem pi_eq_homotopyGroup (m : ℕ) (X : Type*) [TopologicalSpace X] (x : X) :
    HomotopyGroup.Pi m X x = HomotopyGroup (Fin m) X x := rfl

/-- **Exactness at `π_{n+1}(E, e)`**, spelled with `Fin (n + 1)` so that it is
    literally a statement about `π_{n+1}`. `Fin (n + 1)` supplies both
    `DecidableEq` and `Nonempty`, which is exactly why the shift by one is
    there and not an off-by-one. -/
theorem pi_range_eq_ker (he : p e = b)
    (hlift : HasHomotopyLiftingPropertyRel p (Fin (n + 1) → I) (Cube.boundary (Fin (n + 1)))) :
    (homotopyGroupHom (N := Fin (n + 1)) (x := (⟨e, he⟩ : Fibre p b)) (y := e)
        (fibreIncl p b) rfl).range =
      (homotopyGroupHom (N := Fin (n + 1)) p he).ker :=
  range_homotopyGroupHom_eq_ker p he hlift

end Pi

section Trivial

variable {N : Type uN} {F : Type uF} [TopologicalSpace F]

/-- **The hypothesis is not vacuous.** For the projection of a trivial bundle
    the relative lifting property is a theorem, so exactness at the middle spot
    holds unconditionally there.

    A trivial bundle is the case where nothing needs lifting theory: the lift
    is written down. Recorded not because the conclusion is interesting there
    but because it is the witness that the hypothesis of the general theorem is
    satisfiable at all. -/
theorem Prod.homotopyGroupMap_fst_eq_const_iff {w : B × F} {b : B} (he : w.1 = b)
    (q : HomotopyGroup N (B × F) w) :
    homotopyGroupMap (N := N) (ContinuousMap.fst : C(B × F, B)) he q = ⟦GenLoop.const⟧ ↔
      ∃ r : HomotopyGroup N (Fibre (ContinuousMap.fst : C(B × F, B)) b)
          (⟨w, he⟩ : Fibre (ContinuousMap.fst : C(B × F, B)) b),
        homotopyGroupMap (fibreIncl (ContinuousMap.fst : C(B × F, B)) b) rfl r = q :=
  homotopyGroupMap_eq_const_iff (ContinuousMap.fst : C(B × F, B)) he
    (Prod.hasHomotopyLiftingPropertyRel_fst (N → I) (Cube.boundary N)) q

end Trivial

end QOU.Mathlib.FibrationExactness
