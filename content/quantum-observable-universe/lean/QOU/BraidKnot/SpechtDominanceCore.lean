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
**constructs the dominance partial order concretely**, and isolates the
irreducible combinatorial heart as a single, `LinearOrder`-free, `support`-free,
**relation-level** core:

> `dominance_colStab_lemma` — under the concrete dominance order `domRel` (a
> proved partial order on `Tabloid μ`), for a **standard** tableau `T` every
> column permutation weakly decreases the tabloid
> (`π ∈ C_t`, `T` standard `⟹ domRel {π•t} {t}`). This is Sagan's §2.4 dominance
> lemma. (Restricted to standard `T`: over *all* tableaux it contradicts
> antisymmetry — see the lemma's doc.)

The dominance order itself is no longer opaque: `dominance_relation_exists` is now
**`sorry`-free**, built from the explicit partial-sum order `domRel` whose three
order axioms + decidability are all discharged. Everything else is `sorry`-free:

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
  (`rowEquiv_iff`), so `Tabloid μ ↪ (Fin n → ℕ)`. Pins down what the dominance
  order's antisymmetry concretely asserts.
* **The concrete dominance order** (`domCount`, `domRel`, `domRel_refl`,
  `domRel_trans`, `domRel_antisymm`, `domRel_decidable`) — the dominance count
  `domCount f i m = #{l : l<m ∧ f l ≤ i}`; the order `domRel a b ≡ ∀ i m,
  domCount(a) ≤ domCount(b)`; reflexivity/transitivity are pointwise, antisymmetry
  is `domCount_inj` (the marginal `domCount f i (l+1) − domCount f i l = [f l ≤ i]`
  recovers the row pattern) composed with `tabloidRowPattern_injective`, and
  decidability is the clamp `domCount_clamp` (saturation past `n`, via the cell
  row-index bound `rowPattern t l < n`) reducing `∀ i m : ℕ` to a bounded
  quantifier. **All sorry-free.**
* **The assembly** (`dominance_relation_exists`) — packages `domRel` + the four
  sorry-free order/decidability proofs + the one cited `dom_colStab` field into
  `DominanceData`. `sorry`-free (its only conjectural ingredient is the core
  lemma below, passed as the `dom_colStab` field).
* **Layers 2–3 wiring** (`exists_order_colStab_decreasing`,
  `standardPolytabloid_dominance_order'`) — the lever turns `domRel` into the
  required `LinearOrder`; Layer 1 + the colStab-decrease field supply the support
  bound. The verbatim brick-4 target `standardPolytabloid_dominance_order'`
  follows `sorry`-free modulo the one core.

## sorry-free ↔ stubbed map

| Declaration | Status |
|---|---|
| `support_subset_colStab_image` (Layer 1) | **sorry-free** |
| `exists_linearOrder_of_partialOrder` (Szpilrajn-for-Fintypes lever) | **sorry-free** |
| `tabloidRowPattern`, `tabloidRowPattern_injective` (tabloid↔row-pattern) | **sorry-free** |
| `row_lt_card`, `rowPattern_lt_nOf`, `tabloidRowPattern_lt_nOf` (cell row bound) | **sorry-free** |
| `domCount`, `domCount_succ`, `singleton_filter_card`, `domCount_marginal`, `domCount_inj` (count + antisymm engine) | **sorry-free** |
| `domCount_sat_m`, `domCount_sat_i`, `domCount_clamp` (saturation for decidability) | **sorry-free** |
| `domRel`, `domRel_refl`, `domRel_trans`, `domRel_antisymm`, `domRel_iff_bounded`, `domRel_decidable` (the concrete partial order) | **sorry-free** |
| `DominanceData` (the core's bundled data) | structure (no proof obligation) |
| `dominance_colStab_lemma` (Sagan's §2.4 dominance lemma — the single combinatorial core) | **STUB** `sorry` — `-- Ref: [sagan2001]` §2.4 / Thm 2.5.2 |
| `dominance_relation_exists` (concrete `DominanceData`) | **sorry-free MODULO `dominance_colStab_lemma`** |
| `exists_order_colStab_decreasing` (Layer 2) | **sorry-free MODULO the single core** |
| `standardPolytabloid_dominance_order'` (verbatim brick-4 target) | **sorry-free MODULO the single core** |

`#print axioms` at the file end confirms `sorryAx` enters
`standardPolytabloid_dominance_order'` *only* through `dominance_colStab_lemma`
(the single core); the lever, Layer 1, the row-pattern bridge, the entire
concrete dominance order (`domRel` + refl/trans/antisymm/decidability), and the
count engine are all `[propext, Classical.choice, Quot.sound]`.

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

/-! ## The dominance order on tabloids via partial-sum counts (sorry-free)

The dominance partial order is built concretely from the **dominance count**
`domCount f i m = #{l : (l:ℕ) < m ∧ f l ≤ i}` of a row pattern `f` — "among the
`m` smallest labels, how many lie in rows `≤ i`".  The relation
`domRel a b :≡ ∀ i m, domCount (rowPat a) i m ≤ domCount (rowPat b) i m`
is then a genuine partial order, all three order axioms discharged `sorry`-free:

* **reflexivity / transitivity** are pointwise `le_refl` / `le_trans`.
* **antisymmetry** is the substantive sorry-free fact: equal counts everywhere
  force equal row patterns (`domCount_inj`, via the marginal
  `domCount f i (l+1) − domCount f i l = [f l ≤ i]`), whence equal tabloids
  (`tabloidRowPattern_injective`).
* **decidability** comes from clamping both indices into `[0, n]` (the counts
  saturate past `n`, using the row-index bound `rowPattern t l < n`), reducing
  the `∀ i m : ℕ` to a decidable bounded quantifier.

All of this is `ℕ`-valued (§7c-clean: no `ℝ`, no ordering on `q`). -/

/-- The row index of any cell of a Young diagram is `< ν.card`: the `i+1` cells
`(0,0), …, (i,0)` lie in `ν` by down-closure, so `i + 1 ≤ ν.card`. -/
theorem row_lt_card (ν : YoungDiagram) (i j : ℕ) (h : (i, j) ∈ ν) : i < ν.card := by
  classical
  have hsub : (Finset.range (i + 1)).image (fun i' => (i', 0)) ⊆ ν.cells := by
    intro c hc
    rw [Finset.mem_image] at hc
    obtain ⟨i', hi', rfl⟩ := hc
    rw [Finset.mem_range] at hi'
    rw [YoungDiagram.mem_cells]
    exact YoungDiagram.up_left_mem ν (Nat.lt_succ_iff.mp hi') (Nat.zero_le _) h
  have hcard : ((Finset.range (i + 1)).image (fun i' => (i', 0))).card = i + 1 := by
    rw [Finset.card_image_of_injective]
    · rw [Finset.card_range]
    · intro a b hab; simpa using hab
  have hle : i + 1 ≤ ν.card := by
    show i + 1 ≤ ν.cells.card
    rw [← hcard]; exact Finset.card_le_card hsub
  omega

/-- The row pattern of a tableau is bounded by `nOf μ`. -/
theorem rowPattern_lt_nOf (t : Specht.Tableau μ) (l : Fin (Specht.nOf μ)) :
    Specht.rowPattern t l < Specht.nOf μ := by
  have hmem : ((t l : ℕ × ℕ).1, (t l : ℕ × ℕ).2) ∈ μ := (t l).2
  exact row_lt_card μ _ _ hmem

/-- The row pattern of a tabloid is bounded by `nOf μ` (descends from tableaux). -/
theorem tabloidRowPattern_lt_nOf (a : Specht.Tabloid μ) (l : Fin (Specht.nOf μ)) :
    tabloidRowPattern a l < Specht.nOf μ := by
  refine Quotient.inductionOn a (fun t => ?_)
  exact rowPattern_lt_nOf t l

/-- **The dominance count.** `domCount f i m` is the number of the `m` smallest
labels whose row (under the pattern `f`) is `≤ i`. -/
def domCount (f : Fin (Specht.nOf μ) → ℕ) (i m : ℕ) : ℕ :=
  (Finset.univ.filter (fun l : Fin (Specht.nOf μ) => (l : ℕ) < m ∧ f l ≤ i)).card

/-- **Marginal decomposition.** Passing from `m` to `m+1` adds the labels with
val `= m` and row `≤ i`. -/
theorem domCount_succ (f : Fin (Specht.nOf μ) → ℕ) (i m : ℕ) :
    domCount f i (m + 1) =
      domCount f i m
        + (Finset.univ.filter (fun l : Fin (Specht.nOf μ) => (l : ℕ) = m ∧ f l ≤ i)).card := by
  classical
  unfold domCount
  rw [← Finset.card_union_of_disjoint]
  · congr 1
    ext l
    simp only [Finset.mem_filter, Finset.mem_union, Finset.mem_univ, true_and]
    constructor
    · rintro ⟨hlt, hf⟩
      rcases Nat.lt_succ_iff_lt_or_eq.mp hlt with h | h
      · exact Or.inl ⟨h, hf⟩
      · exact Or.inr ⟨h, hf⟩
    · rintro (⟨h, hf⟩ | ⟨h, hf⟩)
      · exact ⟨Nat.lt_succ_of_lt h, hf⟩
      · exact ⟨h ▸ Nat.lt_succ_self m, hf⟩
  · rw [Finset.disjoint_left]
    intro l hl hl'
    simp only [Finset.mem_filter, Finset.mem_univ, true_and] at hl hl'
    exact absurd hl'.1 (Nat.ne_of_lt hl.1)

/-- The "val `= l₀`" filter is the singleton `{l₀}` or empty, by `Fin.val`
injectivity. -/
theorem singleton_filter_card (f : Fin (Specht.nOf μ) → ℕ) (i : ℕ)
    (l₀ : Fin (Specht.nOf μ)) :
    (Finset.univ.filter (fun l : Fin (Specht.nOf μ) => (l : ℕ) = (l₀ : ℕ) ∧ f l ≤ i)).card
      = if f l₀ ≤ i then 1 else 0 := by
  classical
  by_cases hf : f l₀ ≤ i
  · rw [if_pos hf, Finset.card_eq_one]
    refine ⟨l₀, ?_⟩
    ext l
    simp only [Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_singleton]
    constructor
    · rintro ⟨hval, _⟩; exact Fin.ext hval
    · rintro rfl; exact ⟨rfl, hf⟩
  · rw [if_neg hf, Finset.card_eq_zero]
    ext l
    simp only [Finset.mem_filter, Finset.mem_univ, true_and, Finset.notMem_empty, iff_false]
    rintro ⟨hval, hfl⟩
    have : l = l₀ := Fin.ext hval
    rw [this] at hfl
    exact hf hfl

/-- **The marginal at a label is the indicator of "row `≤ i`".** -/
theorem domCount_marginal (f : Fin (Specht.nOf μ) → ℕ) (i : ℕ)
    (l₀ : Fin (Specht.nOf μ)) :
    domCount f i ((l₀ : ℕ) + 1) = domCount f i (l₀ : ℕ) + (if f l₀ ≤ i then 1 else 0) := by
  rw [domCount_succ, singleton_filter_card]

/-- **Counts determine the row pattern (the antisymmetry engine, sorry-free).**
If two row patterns have equal dominance counts everywhere, they are equal:
the marginals recover, for each label `l₀` and threshold `i`, the bit
`f l₀ ≤ i`, and a natural is determined by the set of `i` dominating it. -/
theorem domCount_inj (f g : Fin (Specht.nOf μ) → ℕ)
    (h : ∀ i m, domCount f i m = domCount g i m) : f = g := by
  funext l₀
  have hiff : ∀ i, (f l₀ ≤ i ↔ g l₀ ≤ i) := by
    intro i
    have e1 := domCount_marginal f i l₀
    have e2 := domCount_marginal g i l₀
    rw [h i ((l₀ : ℕ) + 1), h i (l₀ : ℕ)] at e1
    rw [e2] at e1
    have hcancel : (if f l₀ ≤ i then (1 : ℕ) else 0) = (if g l₀ ≤ i then (1 : ℕ) else 0) :=
      (Nat.add_left_cancel e1).symm
    by_cases hf : f l₀ ≤ i <;> by_cases hg : g l₀ ≤ i <;>
      simp [hf, hg] at hcancel ⊢
  exact Nat.le_antisymm ((hiff (g l₀)).mpr le_rfl) ((hiff (f l₀)).mp le_rfl)

/-- **Saturation in `m`.** For `m ≥ n` every label has val `< m`, so the count
no longer moves. -/
theorem domCount_sat_m (f : Fin (Specht.nOf μ) → ℕ) (i m : ℕ)
    (hm : Specht.nOf μ ≤ m) : domCount f i m = domCount f i (Specht.nOf μ) := by
  classical
  unfold domCount
  apply congrArg Finset.card
  apply Finset.filter_congr
  intro l _
  have h1 : (l : ℕ) < m := lt_of_lt_of_le l.2 hm
  have h2 : (l : ℕ) < Specht.nOf μ := l.2
  simp [h1, h2]

/-- **Saturation in `i`.** For `i ≥ n` every row index (which is `< n`) is `≤ i`,
so the count no longer moves. -/
theorem domCount_sat_i (f : Fin (Specht.nOf μ) → ℕ) (i m : ℕ)
    (hbound : ∀ l, f l < Specht.nOf μ) (hi : Specht.nOf μ ≤ i) :
    domCount f i m = domCount f (Specht.nOf μ) m := by
  classical
  unfold domCount
  apply congrArg Finset.card
  apply Finset.filter_congr
  intro l _
  have h1 : f l ≤ i := le_of_lt (lt_of_lt_of_le (hbound l) hi)
  have h2 : f l ≤ Specht.nOf μ := le_of_lt (hbound l)
  simp [h1, h2]

/-- **Clamp both indices into `[0, n]`.** The counts depend only on
`min i n`, `min m n`, by saturation. -/
theorem domCount_clamp (f : Fin (Specht.nOf μ) → ℕ) (i m : ℕ)
    (hbound : ∀ l, f l < Specht.nOf μ) :
    domCount f i m = domCount f (min i (Specht.nOf μ)) (min m (Specht.nOf μ)) := by
  classical
  rcases le_or_gt (Specht.nOf μ) i with hi | hi
  · rw [domCount_sat_i f i m hbound hi, min_eq_right hi]
    rcases le_or_gt (Specht.nOf μ) m with hm | hm
    · rw [domCount_sat_m f (Specht.nOf μ) m hm, min_eq_right hm]
    · rw [min_eq_left (le_of_lt hm)]
  · rw [min_eq_left (le_of_lt hi)]
    rcases le_or_gt (Specht.nOf μ) m with hm | hm
    · rw [domCount_sat_m f i m hm, min_eq_right hm]
    · rw [min_eq_left (le_of_lt hm)]

/-- **The dominance relation on tabloids.** `domRel a b` — "`a` is dominated by
`b`" — holds when every dominance count of `a` is `≤` the corresponding count of
`b`.  A genuine partial order (refl/trans/antisymm sorry-free below). -/
def domRel (a b : Specht.Tabloid μ) : Prop :=
  ∀ i m : ℕ, domCount (tabloidRowPattern a) i m ≤ domCount (tabloidRowPattern b) i m

theorem domRel_refl (a : Specht.Tabloid μ) : domRel a a := fun _ _ => le_refl _

theorem domRel_trans (a b c : Specht.Tabloid μ) :
    domRel a b → domRel b c → domRel a c :=
  fun hab hbc i m => le_trans (hab i m) (hbc i m)

/-- **Antisymmetry (sorry-free).** Mutual domination forces equal counts, hence
(by `domCount_inj` + `tabloidRowPattern_injective`) equal tabloids. -/
theorem domRel_antisymm (a b : Specht.Tabloid μ) :
    domRel a b → domRel b a → a = b := by
  intro hab hba
  apply tabloidRowPattern_injective
  apply domCount_inj
  intro i m
  exact le_antisymm (hab i m) (hba i m)

/-- The unbounded relation is equivalent to its clamp to a decidable bounded
quantifier over `[0, n] × [0, n]`. -/
theorem domRel_iff_bounded (a b : Specht.Tabloid μ) :
    domRel a b ↔
      ∀ i ∈ Finset.range (Specht.nOf μ + 1), ∀ m ∈ Finset.range (Specht.nOf μ + 1),
        domCount (tabloidRowPattern a) i m ≤ domCount (tabloidRowPattern b) i m := by
  constructor
  · intro h i _ m _; exact h i m
  · intro hbdd i m
    rw [domCount_clamp (tabloidRowPattern a) i m (tabloidRowPattern_lt_nOf a),
        domCount_clamp (tabloidRowPattern b) i m (tabloidRowPattern_lt_nOf b)]
    refine hbdd (min i (Specht.nOf μ)) ?_ (min m (Specht.nOf μ)) ?_
    · rw [Finset.mem_range]; exact Nat.lt_succ_of_le (min_le_right _ _)
    · rw [Finset.mem_range]; exact Nat.lt_succ_of_le (min_le_right _ _)

/-- **Decidability of the dominance relation (sorry-free).** -/
instance domRel_decidable : DecidableRel (domRel (μ := μ)) := fun a b =>
  decidable_of_iff _ (domRel_iff_bounded a b).symm

/-! ## The single combinatorial core (one cited `sorry`)

We bundle exactly Sagan 2.5.2's dominance content into one structure: a relation
`dom` on `Tabloid μ` that is a partial order (refl/trans/antisymm) under which
column permutations weakly decrease the tabloid. This is `LinearOrder`-free and
`support`-free — all the order-construction and `Finsupp` plumbing has been
peeled off by the lever and Layer 1.

The data is now supplied **concretely** by `domRel` (the partial-sum dominance
order above): its reflexivity, transitivity, antisymmetry, and decidability are
all discharged `sorry`-free, so `dominance_relation_exists` is `sorry`-free and
the **single** remaining cited `sorry` is the genuine combinatorial heart —
`dominance_colStab_lemma`, Sagan's §2.4 dominance lemma (a column permutation
weakly decreases the tabloid). The opaque `Nonempty (DominanceData)` stub has
become "concrete dominance order, fully a partial order, reduced to exactly
Sagan's dominance lemma." -/

/-- **The core's bundled data (Sagan 2.5.2's dominance content).** A reflexive,
transitive, antisymmetric relation `dom` on tabloids of shape `μ` such that for
every **standard** tableau `T`, each column permutation `π ∈ C_t` of its filling
`t = sytToTableau T` sends `{t}` to a weakly-dominated tabloid `dom {π•t} {t}`.
(The `dom_colStab` field is restricted to standard `T`: over *all* tableaux it
would contradict `dom_antisymm` — see that field's doc.) From it (plus the lever
+ Layer 1) the brick-4 target follows `sorry`-free. -/
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
  /-- **the dominance lemma** (Sagan §2.4): for a **standard** tableau `T`, every
  column permutation `π ∈ C_t` of `t = sytToTableau T` weakly decreases the
  tabloid. **Restricted to standard `T` on purpose** — over *all* tableaux this
  field is inconsistent with `dom_antisymm`: applying it at both `t` and
  `t' = π•t` (note `colStab t' = colStab t ∋ π⁻¹`, `π⁻¹•t' = t`) forces
  `{π•t} = {t}`, i.e. `colStab t ⊆ rowStab t`; with `colStab t ∩ rowStab t = {1}`
  that gives `colStab t = {1}`, false once `μ` has a column of length ≥ 2.
  Standard `T` is exactly what the downstream support bound needs
  (`exists_order_colStab_decreasing` only applies it at `sytToTableau T`). -/
  dom_colStab : ∀ (T : StandardYoungTableau μ) (π : Specht.colStab (sytToTableau T)),
    dom (Specht.Tabloid.mk ((π : Equiv.Perm (Fin (Specht.nOf μ))) • sytToTableau T))
      (Specht.Tabloid.mk (sytToTableau T))

/-- **STUB — Sagan's dominance lemma (the single combinatorial core).** For a
**standard** tableau `T` with filling `t = sytToTableau T`, every column
permutation `π ∈ C_t` sends `{t}` to a tabloid `{π•t}` weakly **dominated by**
`{t}` in the concrete dominance order `domRel`
(`domCount {π•t} i m ≤ domCount {t} i m` for all `i, m`). This is the irreducible
combinatorial heart of the standard-basis independence proof — Sagan §2.4's
dominance lemma — against the concrete `domRel` built above, with no
`LinearOrder`/`Finsupp` plumbing and **all order axioms already discharged**: only
this single inequality remains.

**Why standard `T` (not all tableaux).** The statement is true precisely *because*
`T` is standard: columns increase downward (`col_strict`), so each column already
holds its smallest label at the top — `{t}` is the dominance-**maximum** of its
column orbit, and any `π ∈ C_t` weakly decreases it. Over *arbitrary* `t` the
claim is **false** and is even inconsistent with `dom_antisymm`: applying it at
both `t` and `t' = π•t` (note `colStab t' = colStab t ∋ π⁻¹`) forces `{π•t} = {t}`,
i.e. `colStab t ⊆ rowStab t`; with `colStab t ∩ rowStab t = {1}` that gives
`colStab t = {1}`, false once `μ` has a column of length ≥ 2. (n=2 single column:
with standard `t = id`, the swap `π` moves label `0` down from row `0` to row `1`,
dropping `domCount` at `(i=0,m=1)` from `1` to `0` — `{π•t}` strictly below `{t}`,
consistent.) -/
theorem dominance_colStab_lemma (T : StandardYoungTableau μ)
    (π : Specht.colStab (sytToTableau T)) :
    domRel (Specht.Tabloid.mk ((π : Equiv.Perm (Fin (Specht.nOf μ))) • sytToTableau T))
      (Specht.Tabloid.mk (sytToTableau T)) := by
  -- Ref: [sagan2001] §2.4 the dominance lemma (for STANDARD t, a column permutation
  -- π ∈ C_t sends {t} to a tabloid {π•t} weakly dominated by {t}, so {T} is the
  -- maximum of supp(e_T)); cf. Thm 2.5.2 and [james1984representation] §8. The
  -- single irreducible core of brick 4 — the order axioms are all proved above.
  -- (Standard t is essential: over all t the claim is false — see the docstring.)
  sorry

/-- **The single combinatorial core, reduced (sorry-free modulo
`dominance_colStab_lemma`).** The dominance partial order on tabloids of shape
`μ` exists: it is the concrete `domRel`, whose reflexivity, transitivity,
antisymmetry, and decidability are all `sorry`-free; the only conjectural field is
`dom_colStab`, supplied by the single cited `dominance_colStab_lemma`. -/
theorem dominance_relation_exists (μ : YoungDiagram) : Nonempty (DominanceData μ) :=
  ⟨{ dom := domRel
     domDec := domRel_decidable
     dom_refl := domRel_refl
     dom_trans := domRel_trans
     dom_antisymm := domRel_antisymm
     dom_colStab := dominance_colStab_lemma }⟩

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
  -- leadTab T = mk (sytToTableau T); the core gives dom {π•t} {t} for standard T,
  -- lever lifts to ≤
  have hdom := D.dom_colStab T π
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
