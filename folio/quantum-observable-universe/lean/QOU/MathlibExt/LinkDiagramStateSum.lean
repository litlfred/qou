import QOU.MathlibExt.LinkDiagramCode
import Mathlib.Algebra.BigOperators.Pi
import Mathlib.Logic.Equiv.Fin.Basic
import Mathlib.Data.Fintype.Pi
import Mathlib.Data.Fintype.Prod
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Tactic.Ring
import Mathlib.Algebra.BigOperators.Ring.Finset

/-!
# State sums on link diagram codes

A `Model R ι` assigns to each crossing sign a tensor `X s (uin) (uout) (oin) (oout) ∈ R`, indexed
by labels in a finite set `ι`. The value of a code over a finite edge type `E` is the sum over all
labellings `L : E → ι` of

* the product of the crossing tensors at the labels of their four edges,
* `1` or `0` for each join `(a, b)`, according to whether `L a = L b`,
* `1` or `0` for each edge that does not occur in the code, according to whether it carries the
  base label (so unused edges do not change the value).

This file proves, for an abstract model, the invariance statements that turn local identities of
the tensors into invariance of the value under the moves of `LinkDiagramCode`.

-- Ref: [kauffman1987] Kauffman, "State models and the Jones polynomial", Topology 26 (1987)
-- Ref: [turaev1988] Turaev, "The Yang–Baxter equation and invariants of links", Invent. Math. 92
-/

namespace QOU.MathlibExt.PL.Diagram

open Finset

universe u

variable {R : Type*} [CommRing R] {ι : Type*} [Fintype ι] [DecidableEq ι]

/-- A state-sum model: crossing tensors indexed by the sign and the labels of
`(uin, uout, oin, oout)`, and a base label for unused edges. -/
structure Model (R ι : Type*) where
  X : Bool → ι → ι → ι → ι → R
  base : ι

/-! ### Splitting a sum over labellings at one edge -/

section Split

variable {E : Type u} [Fintype E] [DecidableEq E]

omit [Fintype ι] [DecidableEq ι] [Fintype E] in
theorem update_funSplitAt_symm (e : E) (b i : ι) (g : { j // j ≠ e } → ι) :
    Function.update ((Equiv.funSplitAt e ι).symm (b, g)) e i = (Equiv.funSplitAt e ι).symm (i, g) := by
  funext j
  by_cases h : j = e
  · subst h; simp [Equiv.funSplitAt_symm_apply]
  · simp [Equiv.funSplitAt_symm_apply, h]

/-- **Splitting a labelling sum at an edge.** Summing over all labellings is the same as fixing the
label of `e` to `b` and then summing over the value at `e`. -/
theorem sum_split (e : E) (b : ι) (F : (E → ι) → R) :
    ∑ L, F L = ∑ L, if L e = b then ∑ i, F (Function.update L e i) else 0 := by
  rw [← (Equiv.funSplitAt e ι).symm.sum_comp, ← (Equiv.funSplitAt e ι).symm.sum_comp,
    Fintype.sum_prod_type, Fintype.sum_prod_type, Finset.sum_comm]
  have hx : ∀ x y, (Equiv.funSplitAt e ι).symm (x, y) e = x := fun x y => by
    simp [Equiv.funSplitAt_symm_apply]
  simp only [hx, update_funSplitAt_symm]
  rw [Finset.sum_comm (f := fun x y => if x = b then _ else _)]
  simp only [Finset.sum_ite_eq', Finset.mem_univ, if_true]

end Split

/-! ### The value of a code -/

section Value

variable {E : Type u} [Fintype E] [DecidableEq E] (M : Model R ι)

/-- The crossing part of the weight. -/
def xw (xs : Multiset (Crossing E)) (L : E → ι) : R :=
  (xs.map fun x => M.X x.pos (L x.uin) (L x.uout) (L x.oin) (L x.oout)).prod

/-- The join part of the weight: `1` if every join has equal labels at its ends, else `0`. -/
def jw (js : Multiset (E × E)) (L : E → ι) : R :=
  (js.map fun j => if L j.1 = L j.2 then (1 : R) else 0).prod

open Classical in
/-- The factor of edge `e`: `1` if it occurs in `D`, else whether it carries the base label. -/
noncomputable def uf (D : Code E) (e : E) (L : E → ι) : R :=
  if D.Occurs e then 1 else if L e = M.base then 1 else 0

/-- The weight of a labelling. -/
noncomputable def weight (D : Code E) (L : E → ι) : R :=
  xw M D.xs L * jw D.js L * ∏ e, uf M D e L

/-- **The state-sum value of a code.** -/
noncomputable def value (D : Code E) : R := ∑ L, weight M D L

omit [Fintype ι] [DecidableEq ι] [Fintype E] [DecidableEq E] in
theorem xw_add (xs ys : Multiset (Crossing E)) (L : E → ι) :
    xw M (xs + ys) L = xw M xs L * xw M ys L := by
  simp [xw, Multiset.map_add, Multiset.prod_add]

omit [Fintype ι] [Fintype E] [DecidableEq E] in
theorem jw_add (js ks : Multiset (E × E)) (L : E → ι) :
    jw (R := R) (js + ks) L = jw js L * jw ks L := by
  simp [jw, Multiset.map_add, Multiset.prod_add]

omit [Fintype ι] [DecidableEq ι] [Fintype E] [DecidableEq E] in
theorem xw_congr (xs : Multiset (Crossing E)) {L L' : E → ι}
    (h : ∀ x ∈ xs, ∀ e, x.Mentions e → L e = L' e) : xw M xs L = xw M xs L' := by
  unfold xw
  congr 1
  refine Multiset.map_congr rfl fun x hx => ?_
  have h1 := h x hx
  simp only [Crossing.Mentions] at h1
  rw [h1 _ (Or.inl rfl), h1 _ (Or.inr (Or.inl rfl)), h1 _ (Or.inr (Or.inr (Or.inl rfl))),
    h1 _ (Or.inr (Or.inr (Or.inr rfl)))]

omit [Fintype ι] [Fintype E] [DecidableEq E] in
theorem jw_congr (js : Multiset (E × E)) {L L' : E → ι}
    (h : ∀ j ∈ js, L j.1 = L' j.1 ∧ L j.2 = L' j.2) : jw (R := R) js L = jw js L' := by
  unfold jw
  congr 1
  refine Multiset.map_congr rfl fun j hj => ?_
  rw [(h j hj).1, (h j hj).2]

omit [Fintype E] [DecidableEq E] in
theorem occurs_add (D D' : Code E) (e : E) : (D + D').Occurs e ↔ D.Occurs e ∨ D'.Occurs e := by
  simp only [Code.Occurs, Code.add_xs, Code.add_js, Multiset.mem_add]
  constructor
  · rintro (⟨x, hx | hx, h⟩ | ⟨j, hj | hj, h⟩)
    exacts [Or.inl (Or.inl ⟨x, hx, h⟩), Or.inr (Or.inl ⟨x, hx, h⟩),
      Or.inl (Or.inr ⟨j, hj, h⟩), Or.inr (Or.inr ⟨j, hj, h⟩)]
  · rintro ((⟨x, hx, h⟩ | ⟨j, hj, h⟩) | (⟨x, hx, h⟩ | ⟨j, hj, h⟩))
    exacts [Or.inl ⟨x, Or.inl hx, h⟩, Or.inr ⟨j, Or.inl hj, h⟩,
      Or.inl ⟨x, Or.inr hx, h⟩, Or.inr ⟨j, Or.inr hj, h⟩]

/-- The part of the weight that a local move may change: the crossings and joins of the local
piece `S`, and the unused-edge factors on the internal edges `T`. -/
noncomputable def loc (T : Finset E) (S : Code E) (L : E → ι) : R :=
  xw M S.xs L * jw S.js L * ∏ e ∈ T, uf M S e L

/-- The labellings that agree with `v` off `T` and take the values `u` on `T`. -/
def glue (T : Finset E) (u : { e // e ∈ T } → ι) (v : { e // e ∉ T } → ι) : E → ι :=
  (Equiv.piEquivPiSubtypeProd (· ∈ T) (fun _ => ι)).symm (u, v)

/-- **Local replacement.** Replacing a local piece `S` by `S'` does not change the value, provided
the internal edges `T` do not occur in the rest `R`, the two pieces have the same edges outside
`T`, and the local sums over the internal labels agree for every boundary labelling. -/
theorem value_local (R₀ S S' : Code E) (T : Finset E)
    (hR : ∀ e ∈ T, ¬ R₀.Occurs e)
    (hocc : ∀ e ∉ T, (S.Occurs e ↔ S'.Occurs e))
    (hloc : ∀ v : { e // e ∉ T } → ι,
      ∑ u, loc M T S (glue T u v) = ∑ u, loc M T S' (glue T u v)) :
    value M (R₀ + S) = value M (R₀ + S') := by
  classical
  -- the part of the weight outside the local piece
  let A : (E → ι) → R := fun L =>
    xw M R₀.xs L * jw R₀.js L * ∏ e ∈ univ.filter (· ∉ T), uf M (R₀ + S) e L
  have hsplit : ∀ (S₁ : Code E), (∀ e ∉ T, ((R₀ + S₁).Occurs e ↔ (R₀ + S).Occurs e)) →
      ∀ L, weight M (R₀ + S₁) L = A L * loc M T S₁ L := by
    intro S₁ h₁ L
    simp only [weight, loc, A, Code.add_xs, Code.add_js, xw_add, jw_add]
    rw [← Finset.prod_filter_mul_prod_filter_not univ (· ∈ T)]
    have hT : univ.filter (· ∈ T) = T := by ext; simp
    rw [hT]
    have h1 : ∏ e ∈ T, uf M (R₀ + S₁) e L = ∏ e ∈ T, uf M S₁ e L :=
      Finset.prod_congr rfl fun e he => by
        simp only [uf, occurs_add, hR e he, false_or]
    have h2 : ∏ e ∈ univ.filter (fun e => ¬ e ∈ T), uf M (R₀ + S₁) e L
        = ∏ e ∈ univ.filter (· ∉ T), uf M (R₀ + S) e L :=
      Finset.prod_congr rfl fun e he => by
        simp only [Finset.mem_filter] at he
        simp only [uf, h₁ e he.2]
    rw [h1, h2]
    ring
  have hS : ∀ L, weight M (R₀ + S) L = A L * loc M T S L := hsplit S (fun _ _ => Iff.rfl)
  have hS' : ∀ L, weight M (R₀ + S') L = A L * loc M T S' L := hsplit S' fun e he => by
    simp only [occurs_add, hocc e he]
  -- `A` only sees the labels off `T`
  have hA : ∀ u u' v, A (glue T u v) = A (glue T u' v) := by
    intro u u' v
    have hoff : ∀ e, e ∉ T → glue T u v e = glue T u' v e := fun e he => by
      simp [glue, Equiv.piEquivPiSubtypeProd_symm_apply, he]
    simp only [A]
    congr 1
    · congr 1
      · exact xw_congr M _ fun x hx e hm =>
          hoff e fun heT => hR e heT (Or.inl ⟨x, hx, hm⟩)
      · exact jw_congr _ fun j hj =>
          ⟨hoff _ fun heT => hR _ heT (Or.inr ⟨j, hj, Or.inl rfl⟩),
            hoff _ fun heT => hR _ heT (Or.inr ⟨j, hj, Or.inr rfl⟩)⟩
    · exact Finset.prod_congr rfl fun e he => by
        simp only [Finset.mem_filter] at he
        simp only [uf, hoff e he.2]
  have hsum : ∀ F : (E → ι) → R, ∑ L, F L = ∑ v, ∑ u, F (glue T u v) := by
    intro F
    rw [← (Equiv.piEquivPiSubtypeProd (· ∈ T) (fun _ => ι)).symm.sum_comp,
      Fintype.sum_prod_type, Finset.sum_comm]
    rfl
  unfold value
  rw [Finset.sum_congr rfl fun L _ => hS L, Finset.sum_congr rfl fun L _ => hS' L, hsum, hsum]
  refine Finset.sum_congr rfl fun v _ => ?_
  have hfac : ∀ S₁ : Code E, ∑ u, A (glue T u v) * loc M T S₁ (glue T u v)
      = A (glue T (fun _ => M.base) v) * ∑ u, loc M T S₁ (glue T u v) := fun S₁ => by
    rw [Finset.mul_sum]
    exact Finset.sum_congr rfl fun u _ => by rw [hA u (fun _ => M.base) v]
  rw [hfac, hfac, hloc v]

end Value

end QOU.MathlibExt.PL.Diagram
