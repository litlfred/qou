import QOU.Mathlib.SYTHookFormulaBetaProdMonoid
import QOU.Mathlib.ColLenRowLensBridge
import QOU.Mathlib.HookLengthFormula
import QOU.QBeta.WenzlWeightVanishing

/-!
# QOU.Mathlib.HookProductMonoidBridge — the list↔diagram hook bridge, in any commutative monoid

`HookLengthFormula.hookLengthProduct_eq_prodHooks` identifies the geometric cell product
`∏_{c∈μ} h(c)` with the corpus list product `prodHooks μ.rowLens`, over `ℕ`.  Its proof is
reindexing — `prod_biUnion` over rows, then columns — and its only content is `hookLength_eq_of_mem`
plus `ColLenRowLensBridge.colLen_rowLens`, both statements about the hook's **argument**.  So it
generalises the same way as the rest of the `SYTBeta` chain:

    ∏_{c ∈ μ.cells} f (h_μ(c)) = prodHooksF f μ.rowLens.

This is the encoding bridge the general-`r` branching route needs: everything proved in `SYTBeta` is
List-encoded, and `QBeta.WenzlWeight.schurPrincipal` is `YoungDiagram`-encoded.

The three reindexing lemmas are re-proved here rather than reused because the corpus versions are
`private`, and `row_prod` is `ℕ`-valued.  They are left **public** here — unlike the corpus versions —
because the content side (`ContentProductRows`) needs exactly the same reindexing.

## Base ring (§7c)

Generic `[CommMonoid M]`.  Nothing archimedean; arguments stay in `ℕ`.

LaTeX label: `lem:hook-product-monoid-bridge`
-/

namespace QOU.Mathlib.SYTBeta

open YoungDiagram

variable {M : Type*} [CommMonoid M]

/-- Cells partition into rows `{0, …, colLen 0 − 1}`. -/
theorem cells_biUnion' (μ : YoungDiagram) :
    μ.cells = (Finset.range (μ.colLen 0)).biUnion μ.row := by
  ext ⟨i, j⟩
  simp only [mem_cells, Finset.mem_biUnion, Finset.mem_range, mem_row_iff]
  constructor
  · intro hij
    exact ⟨i, lt_of_lt_of_le (mem_iff_lt_colLen.mp hij)
      (μ.colLen_anti 0 j (Nat.zero_le j)), hij, rfl⟩
  · rintro ⟨i', _, hij, rfl⟩; exact hij

theorem rows_disjoint (μ : YoungDiagram) (n : ℕ) :
    (↑(Finset.range n) : Set ℕ).PairwiseDisjoint μ.row := by
  intro i _ i' _ hne
  rw [Function.onFun, Finset.disjoint_left]
  rintro ⟨a, b⟩ hc hc'
  rw [mem_row_iff] at hc hc'
  exact hne (hc.2.symm.trans hc'.2)

/-- Product over a row = product over its column range, valued in any commutative monoid. -/
theorem row_prodF (μ : YoungDiagram) (g : ℕ × ℕ → M) (i : ℕ) :
    ∏ c ∈ μ.row i, g c = ∏ j ∈ Finset.range (μ.rowLen i), g (i, j) := by
  rw [show μ.row i = (Finset.range (μ.rowLen i)).image (fun j => (i, j)) from ?_,
    Finset.prod_image (fun a _ b _ h => by simpa using h)]
  ext ⟨a, b⟩
  simp only [mem_row_iff, Finset.mem_image, Finset.mem_range]
  constructor
  · rintro ⟨hab, rfl⟩; exact ⟨b, mem_iff_lt_rowLen.mp hab, rfl⟩
  · rintro ⟨j, hj, heq⟩
    obtain ⟨rfl, rfl⟩ := Prod.ext_iff.mp heq
    exact ⟨mem_iff_lt_rowLen.mpr hj, rfl⟩

/-- **The list↔diagram hook bridge, in any commutative monoid.**

`∏_{c ∈ μ.cells} f(h_μ(c)) = prodHooksF f μ.rowLens`.

At `f = id` over `(ℕ, ×)` this is `hookLengthProduct_eq_prodHooks`; at `f n = 1 − Qⁿ` it carries the
q-analogue of the hook product from the `YoungDiagram` side, where `schurPrincipal` lives, to the
List side, where the β-number machinery is proved. -/
theorem prodHooksF_rowLens (f : ℕ → M) (μ : YoungDiagram) :
    ∏ c ∈ μ.cells, f (μ.hookLength c.1 c.2) = prodHooksF f μ.rowLens := by
  rw [cells_biUnion' μ, Finset.prod_biUnion (rows_disjoint μ (μ.colLen 0)),
    prodHooksF, list_range_map_prod', ← length_rowLens]
  refine Finset.prod_congr rfl (fun i hi => ?_)
  rw [Finset.mem_range, length_rowLens] at hi
  rw [row_prodF]
  have hgetD : μ.rowLens.getD i 0 = μ.rowLen i := by
    rw [List.getD_eq_getElem?_getD,
      List.getElem?_eq_getElem (by rw [length_rowLens]; exact hi),
      Option.getD_some, get_rowLens]
  rw [hgetD, list_range_map_prod']
  refine Finset.prod_congr rfl (fun j hj => ?_)
  rw [Finset.mem_range] at hj
  rw [YoungDiagram.hookLength_eq_of_mem μ (mem_iff_lt_rowLen.mpr hj), colLen_rowLens]

/-- The q-instance of the bridge. -/
theorem prodHooksF_rowLens_one_sub_pow {R : Type*} [CommRing R] (Q : R) (μ : YoungDiagram) :
    ∏ c ∈ μ.cells, (1 - Q ^ (μ.hookLength c.1 c.2)) = prodHooksF (fun n => 1 - Q ^ n) μ.rowLens :=
  prodHooksF_rowLens (fun n => 1 - Q ^ n) μ

/-! ## The third hook notion

`QBeta.WenzlWeight.hook` — the one `schurPrincipal` is actually defined with — is a *third* spelling,
`(rowLen i − j) + (colLen j − i) − 1`.  On a cell that is exactly `hookLength_eq_of_mem`'s closed
form, so the two agree definitionally once that rewrite is made.  Recorded because a route that
stopped at `YoungDiagram.hookLength` would still not reach `schurPrincipal`. -/

theorem wenzlHook_eq_hookLength {μ : YoungDiagram} {x : ℕ × ℕ} (hx : x ∈ μ.cells) :
    QOU.QBeta.WenzlWeight.hook μ x = μ.hookLength x.1 x.2 := by
  have hmem : (x.1, x.2) ∈ μ := by simpa using (YoungDiagram.mem_cells x).mp hx
  rw [YoungDiagram.hookLength_eq_of_mem μ hmem]
  rfl

/-- **The bridge in the form `schurPrincipal` needs it**: its own hook product, over the cells of a
`YoungDiagram`, is the List-encoded `prodHooksF` that the β-number machinery is proved for. -/
theorem prodHooksF_rowLens_wenzl (f : ℕ → M) (μ : YoungDiagram) :
    ∏ c ∈ μ.cells, f (QOU.QBeta.WenzlWeight.hook μ c) = prodHooksF f μ.rowLens := by
  rw [← prodHooksF_rowLens f μ]
  exact Finset.prod_congr rfl fun c hc => by rw [wenzlHook_eq_hookLength hc]

end QOU.Mathlib.SYTBeta
