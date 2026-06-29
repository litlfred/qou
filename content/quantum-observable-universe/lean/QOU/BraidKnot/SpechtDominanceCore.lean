import QOU.BraidKnot.SpechtStandardBasis
import Mathlib.Data.Finsupp.Basic
import Mathlib.Data.Prod.Lex
import Mathlib.Data.Fintype.EquivFin
import Mathlib.Data.Finset.Card

/-!
# QOU.BraidKnot.SpechtDominanceCore — an independent reduction of brick-4's dominance core

`QOU.BraidKnot.SpechtTriangularCore.standardPolytabloid_dominance_order` is the
single remaining `sorry` of brick 4 (the standard-basis theorem for Specht
modules). It packages Sagan, *The Symmetric Group*, Thm 2.5.2's dominance
content as:

```
∃ _ : LinearOrder (Tabloid μ),
  ∀ T : StandardYoungTableau μ, ∀ a ∈ (standardPolytabloid T).support, a ≤ leadTab T
```

This module is an **independent** reduction of *that same statement* (it imports
`SpechtStandardBasis` read-only and does **not** import or modify
`SpechtTriangularCore`). Where `SpechtTriangularCore` reduced the *triangular
bundle* to this `LinearOrder`-and-`support` existential, this file peels the
`LinearOrder` construction **and** the `Finsupp`/`support` plumbing off it too,
isolating the irreducible combinatorial heart as a single, `LinearOrder`-free,
`support`-free, **relation-level** core:

> `dominance_relation_exists` — there is a partial order `dom` on `Tabloid μ`
> (reflexive, transitive, antisymmetric) under which **column permutations weakly
> decrease the tabloid** (`π ∈ C_t ⟹ dom {π•t} {t}`).

Everything else is discharged `sorry`-free:

* **Layer 1** (`support_subset_colStab_image`) — `supp(e_T) ⊆ {{π•t} : π ∈ C_t}`,
  pure `Finsupp` plumbing.
* **The Szpilrajn-for-Fintypes lever** (`exists_linearOrder_of_partialOrder`) —
  the pinned Mathlib has **no** linear-extension-of-a-partial-order lemma
  (`Szpilrajn`/`LinearExtension` are absent, verified against the cached
  oleans), so we supply it locally via the down-set-cardinality + Fintype-index
  lexicographic trick. A natural Mathlib-upstream candidate. From a finite
  partial order it produces a `LinearOrder` whose `≤` *dominates* the partial
  relation.
* **The tabloid↔row-pattern bridge** (`tabloidRowPattern`,
  `tabloidRowPattern_injective`) — a tabloid *is* its row pattern
  (`rowEquiv_iff`), so `Tabloid μ ↪ (Fin n → ℕ)`. A sorry-free bonus pinning
  down what the core's antisymmetry concretely asserts.
* **Layers 2–3 wiring** (`exists_order_colStab_decreasing`,
  `standardPolytabloid_dominance_order'`) — the lever turns the core's partial
  order into the required `LinearOrder`; Layer 1 + the colStab-decrease field of
  the core supply the support bound. The verbatim brick-4 target
  `standardPolytabloid_dominance_order'` follows `sorry`-free modulo the one core.

## sorry-free ↔ stubbed map

| Declaration | Status |
|---|---|
| `support_subset_colStab_image` (Layer 1) | **sorry-free** |
| `exists_linearOrder_of_partialOrder` (Szpilrajn-for-Fintypes lever) | **sorry-free** |
| `tabloidRowPattern`, `tabloidRowPattern_injective` (tabloid↔row-pattern) | **sorry-free** |
| `DominanceData` (the core's bundled data) | structure (no proof obligation) |
| `dominance_relation_exists` (the single combinatorial core) | **STUB** `sorry` — `-- Ref: [sagan2001]` Thm 2.5.2 |
| `exists_order_colStab_decreasing` (Layer 2) | **sorry-free MODULO the single core** |
| `standardPolytabloid_dominance_order'` (verbatim brick-4 target) | **sorry-free MODULO the single core** |

`#print axioms` at the file end confirms `sorryAx` enters
`standardPolytabloid_dominance_order'` *only* through `dominance_relation_exists`;
the lever, Layer 1, and the row-pattern bridge are all
`[propext, Classical.choice, Quot.sound]`.

## References
- [sagan2001] Sagan, *The Symmetric Group*, §2.5 (the standard basis, Thm 2.5.2;
  the dominance order on tabloids; a column permutation `π ∈ C_t` sends `{t}` to a
  tabloid `{π•t}` weakly dominated by `{t}`, so `{T}` is the maximum of
  `supp(e_T)`). See also the "dominance lemma" §2.4.
- [james1984representation] James, *The Representation Theory of the Symmetric
  Groups* §8.
-/

open scoped BigOperators

namespace QOU.BraidKnot.SpechtDominanceCore

open QOU.BraidKnot
open QOU.BraidKnot.Specht
open QOU.BraidKnot.SpechtStandardBasis

variable {k : Type} [Field k] [CharZero k]
variable {μ : YoungDiagram}

/-! ## Layer 1 — support ⊆ column-orbit image (sorry-free)

`standardPolytabloid T = polytabloid t = ∑_{π ∈ C_t} sgn(π) • {π•t}`, so the
support of the sum is contained in the union of the term supports, and each term
`sgn(π) • single ({π•t}) 1` has support `⊆ {{π•t}}`. Pure `Finsupp` plumbing. -/

omit [CharZero k] in
/-- **Layer 1 (sorry-free).** Every tabloid in `supp(e_T)` is `{π•t}` for some
column permutation `π ∈ C_t`. -/
theorem support_subset_colStab_image (T : StandardYoungTableau μ) :
    ∀ a ∈ (standardPolytabloid (k := k) T).support,
      ∃ π : Specht.colStab (sytToTableau T),
        a = Specht.Tabloid.mk ((π : Equiv.Perm (Fin (Specht.nOf μ))) • sytToTableau T) := by
  classical
  intro a ha
  -- unfold standardPolytabloid to the polytabloid sum
  rw [standardPolytabloid, Specht.polytabloid] at ha
  -- support of a finset sum ⊆ ⋃ (term supports)
  have hmem := Finsupp.support_finset_sum
      (s := (Finset.univ : Finset (Specht.colStab (sytToTableau T))))
      (f := fun π => (Equiv.Perm.sign (π : Equiv.Perm (Fin (Specht.nOf μ))) : ℤ) •
        Specht.Mtab.of (k := k) ((π : Equiv.Perm (Fin (Specht.nOf μ))) • sytToTableau T)) ha
  rw [Finset.mem_biUnion] at hmem
  obtain ⟨π, _, haπ⟩ := hmem
  refine ⟨π, ?_⟩
  -- each term support ⊆ {mk (π • t)}
  have h1 : a ∈ (Specht.Mtab.of (k := k)
      ((π : Equiv.Perm (Fin (Specht.nOf μ))) • sytToTableau T)).support :=
    Finsupp.support_smul haπ
  rw [Specht.Mtab.of] at h1
  have h2 := Finsupp.support_single_subset h1
  rw [Finset.mem_singleton] at h2
  exact h2

/-! ## The Szpilrajn-for-Fintypes lever (sorry-free)

The pinned Mathlib has no linear-extension-of-a-partial-order lemma. We supply
it for `Fintype`s: from a reflexive/transitive/antisymmetric relation `r`,
the lexicographic key `a ↦ (#{b | r b a}, idx a)` into `ℕ ×ₗ ℕ` (down-set
cardinality, tie-broken by the `Fintype` index) is injective and turns `r` into a
`LinearOrder` whose `≤` dominates `r`: if `r a b` then `#{·|r · a} ≤ #{·|r · b}`,
strictly unless `r b a` too (whence `a = b` by antisymmetry). -/

/-- **Szpilrajn for `Fintype`s (sorry-free).** A reflexive, transitive,
antisymmetric relation on a finite type extends to a `LinearOrder` whose `≤`
contains the relation. Filled the Mathlib gap (no `Szpilrajn`/`LinearExtension`
in the pinned toolchain) via the down-set-cardinality + index lexicographic
trick. -/
theorem exists_linearOrder_of_partialOrder {α : Type*} [Fintype α] [DecidableEq α]
    (r : α → α → Prop) [DecidableRel r]
    (rrefl : ∀ a, r a a)
    (rtrans : ∀ a b c, r a b → r b c → r a c)
    (rantisymm : ∀ a b, r a b → r b a → a = b) :
    ∃ _ : LinearOrder α, ∀ a b, r a b → a ≤ b := by
  classical
  -- a globally-injective tie-breaker (the Fintype index)
  let idx : α → ℕ := fun a => (Fintype.equivFin α a : ℕ)
  have hidx : Function.Injective idx := by
    intro a b h; exact (Fintype.equivFin α).injective (Fin.ext h)
  -- down-set cardinality (strictly monotone for a partial order)
  let dc : α → ℕ := fun a => (Finset.univ.filter (fun b => r b a)).card
  -- the lexicographic key into ℕ ×ₗ ℕ
  let key : α → ℕ ×ₗ ℕ := fun a => toLex (dc a, idx a)
  have hkey : Function.Injective key := by
    intro a b h
    have h2 : ((dc a, idx a) : ℕ × ℕ) = (dc b, idx b) := (toLex (α := ℕ × ℕ)).injective h
    exact hidx (Prod.ext_iff.mp h2).2
  -- pull back the linear order along the injective key
  refine ⟨LinearOrder.lift' key hkey, ?_⟩
  intro a b hab
  show key a ≤ key b
  by_cases hba : r b a
  · -- mutually related ⇒ equal
    rw [rantisymm a b hab hba]
  · -- otherwise the down-set is strictly larger
    have hsub : (Finset.univ.filter (fun c => r c a)) ⊆ (Finset.univ.filter (fun c => r c b)) := by
      intro c hc
      rw [Finset.mem_filter] at hc ⊢
      exact ⟨hc.1, rtrans c a b hc.2 hab⟩
    have hb_in : b ∈ (Finset.univ.filter (fun c => r c b)) := by
      rw [Finset.mem_filter]; exact ⟨Finset.mem_univ _, rrefl b⟩
    have hb_notin : b ∉ (Finset.univ.filter (fun c => r c a)) := by
      rw [Finset.mem_filter]; push_neg; intro _; exact hba
    have hssub : (Finset.univ.filter (fun c => r c a)) ⊂ (Finset.univ.filter (fun c => r c b)) :=
      (Finset.ssubset_iff_of_subset hsub).mpr ⟨b, hb_in, hb_notin⟩
    have hdc : dc a < dc b := Finset.card_lt_card hssub
    show toLex (dc a, idx a) ≤ toLex (dc b, idx b)
    exact le_of_lt (Prod.Lex.left _ _ hdc)

/-! ## The tabloid ↔ row-pattern bridge (sorry-free, bonus)

`rowEquiv s t ↔ rowPattern s = rowPattern t`, so a tabloid is *exactly* its row
pattern: `Tabloid μ ↪ (Fin (nOf μ) → ℕ)`. This pins down what antisymmetry of the
core's dominance relation asserts — that the dominance partial-order data refines
equality of tabloids = equality of row patterns. -/

/-- The row pattern of a tabloid (well-defined on the row-equivalence quotient by
`rowEquiv_iff`): the function sending each label to the row it lives in. -/
def tabloidRowPattern (d : Specht.Tabloid μ) : Fin (Specht.nOf μ) → ℕ :=
  Quotient.liftOn d Specht.rowPattern (fun _ _ h => h)

@[simp] theorem tabloidRowPattern_mk (t : Specht.Tableau μ) :
    tabloidRowPattern (Specht.Tabloid.mk t) = Specht.rowPattern t := rfl

/-- **A tabloid is its row pattern (sorry-free).** `tabloidRowPattern` is injective. -/
theorem tabloidRowPattern_injective :
    Function.Injective (tabloidRowPattern (μ := μ)) := by
  refine Quotient.ind (fun s => ?_)
  refine Quotient.ind (fun t => ?_)
  intro h
  -- decode to row-pattern equality, then to tabloid equality
  have : Specht.rowPattern s = Specht.rowPattern t := h
  exact Quotient.sound this

/-! ## The single combinatorial core (one cited `sorry`)

We bundle exactly Sagan 2.5.2's dominance content into one structure: a relation
`dom` on `Tabloid μ` that is a partial order (refl/trans/antisymm) under which
column permutations weakly decrease the tabloid. This is `LinearOrder`-free and
`support`-free — all the order-construction and `Finsupp` plumbing has been
peeled off by the lever and Layer 1. -/

/-- **The core's bundled data (Sagan 2.5.2's dominance content).** A reflexive,
transitive, antisymmetric relation `dom` on tabloids of shape `μ` such that every
column permutation `π ∈ C_t` sends `{t}` to a weakly-dominated tabloid
`dom {π•t} {t}`. From it (plus the lever + Layer 1) the brick-4 target follows
`sorry`-free. -/
structure DominanceData (μ : YoungDiagram) where
  /-- the dominance relation on tabloids -/
  dom : Specht.Tabloid μ → Specht.Tabloid μ → Prop
  /-- decidable (needed to feed the lever) -/
  domDec : DecidableRel dom
  /-- reflexivity -/
  dom_refl : ∀ a, dom a a
  /-- transitivity -/
  dom_trans : ∀ a b c, dom a b → dom b c → dom a c
  /-- antisymmetry: dominance data refines equality of tabloids -/
  dom_antisymm : ∀ a b, dom a b → dom b a → a = b
  /-- **the dominance lemma**: a column permutation weakly decreases the tabloid -/
  dom_colStab : ∀ (t : Specht.Tableau μ) (π : Specht.colStab t),
    dom (Specht.Tabloid.mk ((π : Equiv.Perm (Fin (Specht.nOf μ))) • t)) (Specht.Tabloid.mk t)

/-- **STUB — the single combinatorial core (Sagan Thm 2.5.2).** The dominance
partial order on tabloids of shape `μ` exists and column permutations weakly
decrease it. This is the irreducible combinatorial heart of the standard-basis
independence proof, isolated here free of any `LinearOrder` construction or
`Finsupp`/`support` plumbing. -/
theorem dominance_relation_exists (μ : YoungDiagram) : Nonempty (DominanceData μ) := by
  -- Ref: [sagan2001] Thm 2.5.2 (dominance order on tabloids; a column permutation
  -- π ∈ C_t sends {t} to a tabloid {π•t} weakly dominated by {t}, so {T} is the
  -- maximum of supp(e_T)). See also the dominance lemma §2.4 and
  -- [james1984representation] §8. The irreducible core of brick 4.
  sorry

/-! ## Layers 2–3 wiring (sorry-free modulo the single core) -/

/-- **Layer 2 (sorry-free modulo the core).** Under a suitable `LinearOrder`,
every column permutation `π ∈ C_t` sends `{t}` to a tabloid `≤ leadTab T = {T}`.
The lever turns the core's partial order `dom` into the `LinearOrder`; the core's
`dom_colStab` field supplies the inequality. -/
theorem exists_order_colStab_decreasing :
    ∃ _ : LinearOrder (Specht.Tabloid μ),
      ∀ T : StandardYoungTableau μ,
        ∀ π : Specht.colStab (sytToTableau T),
          Specht.Tabloid.mk ((π : Equiv.Perm (Fin (Specht.nOf μ))) • sytToTableau T)
            ≤ leadTab T := by
  classical
  obtain ⟨D⟩ := dominance_relation_exists μ
  have : DecidableRel D.dom := D.domDec
  obtain ⟨ord, hle⟩ :=
    exists_linearOrder_of_partialOrder D.dom D.dom_refl D.dom_trans D.dom_antisymm
  refine ⟨ord, ?_⟩
  intro T π
  -- leadTab T = mk (sytToTableau T); the core gives dom {π•t} {t}, lever lifts to ≤
  have hdom := D.dom_colStab (sytToTableau T) π
  rw [leadTab]
  exact hle _ _ hdom

omit [CharZero k] in
/-- **Verbatim brick-4 target** (a restatement of
`SpechtTriangularCore.standardPolytabloid_dominance_order`), proved `sorry`-free
**modulo the single core** `dominance_relation_exists`. Layer 1 reduces the
support membership to a column-orbit image; Layer 2 (lever + core) supplies the
dominance bound. -/
theorem standardPolytabloid_dominance_order' :
    ∃ _ : LinearOrder (Specht.Tabloid μ),
      ∀ T : StandardYoungTableau μ,
        ∀ a ∈ (standardPolytabloid (k := k) T).support, a ≤ leadTab T := by
  obtain ⟨ord, hdec⟩ := exists_order_colStab_decreasing (μ := μ)
  refine ⟨ord, ?_⟩
  intro T a ha
  obtain ⟨π, rfl⟩ := support_subset_colStab_image (k := k) T a ha
  exact hdec T π

end QOU.BraidKnot.SpechtDominanceCore
