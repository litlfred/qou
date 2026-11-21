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
by labels in a finite set `ι`, and to each label a unit `K i`, the weight of one full turn. The
value of a code over a finite edge type `E` is the sum over all labellings `L : E → ι` of

* the product of the crossing tensors at the labels of their four edges,
* for each join `(a, b, t)`, `K (L a) ^ t` if `L a = L b` and `0` otherwise,
* `1` or `0` for each edge that does not occur in the code, according to whether it carries the
  base label (so unused edges do not change the value).

This file proves, for an abstract model, the invariance statements that turn local identities of
the tensors into invariance of the value under the moves of `LinkDiagramCode`, and that the
writhe-normalised value is a `ReidemeisterEquiv` invariant for every model satisfying them
(`normValue_eq`). The identity model `idModel` satisfies them.

The quantum `sl₂` model, with `K = diag(q, q⁻¹)`, is an instance: see `LinkDiagramSl2`. No
Jones-polynomial statement follows from this file alone; that needs the value of a braid closure.

-- Ref: [kauffman1987] Kauffman, "State models and the Jones polynomial", Topology 26 (1987)
-- Ref: [turaev1988] Turaev, "The Yang–Baxter equation and invariants of links", Invent. Math. 92
-/

namespace QOU.MathlibExt.PL.Diagram

open Finset

universe u

variable {R : Type*} [CommRing R] {ι : Type*} [Fintype ι] [DecidableEq ι]

/-- A state-sum model: crossing tensors indexed by the sign and the labels of
`(uin, uout, oin, oout)`, the weight `K i` of one full turn of an edge labelled `i`, and a base
label for unused edges. -/
structure Model (R ι : Type*) [Monoid R] where
  X : Bool → ι → ι → ι → ι → R
  K : ι → Rˣ
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

/-- The join part of the weight: a join `(a, b, t)` contributes `K (L a) ^ t` if its ends carry
equal labels, and `0` otherwise. -/
def jw (js : Multiset (E × E × ℤ)) (L : E → ι) : R :=
  (js.map fun j => if L j.1 = L j.2.1 then ((M.K (L j.1) ^ j.2.2 : Rˣ) : R) else 0).prod

open Classical in
/-- The factor of edge `e`: `1` if it occurs in `D`, else whether it carries the base label. -/
noncomputable def uf (D : Code E) (e : E) (L : E → ι) : R :=
  if D.Occurs e then 1 else if L e = M.base then 1 else 0

/-- The weight of a labelling. -/
noncomputable def weight (D : Code E) (L : E → ι) : R :=
  xw M D.xs L * jw M D.js L * ∏ e, uf M D e L

/-- **The state-sum value of a code.** -/
noncomputable def value (D : Code E) : R := ∑ L, weight M D L

omit [Fintype ι] [DecidableEq ι] [Fintype E] [DecidableEq E] in
theorem xw_add (xs ys : Multiset (Crossing E)) (L : E → ι) :
    xw M (xs + ys) L = xw M xs L * xw M ys L := by
  simp [xw, Multiset.map_add, Multiset.prod_add]

omit [Fintype ι] [Fintype E] [DecidableEq E] in
theorem jw_add (js ks : Multiset (E × E × ℤ)) (L : E → ι) :
    jw M (js + ks) L = jw M js L * jw M ks L := by
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
theorem jw_congr (js : Multiset (E × E × ℤ)) {L L' : E → ι}
    (h : ∀ j ∈ js, L j.1 = L' j.1 ∧ L j.2.1 = L' j.2.1) : jw M js L = jw M js L' := by
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
  xw M S.xs L * jw M S.js L * ∏ e ∈ T, uf M S e L

/-- The labellings that agree with `v` off `T` and take the values `u` on `T`. -/
def glue (T : Finset E) (u : { e // e ∈ T } → ι) (v : { e // e ∉ T } → ι) : E → ι :=
  (Equiv.piEquivPiSubtypeProd (· ∈ T) (fun _ => ι)).symm (u, v)

/-- **Local replacement up to a scalar.** Replacing a local piece `S` by `S'` multiplies the value
by `κ`, provided the internal edges `T` do not occur in the rest `R₀`, the two pieces have the same
edges outside `T`, and for every boundary labelling the local sum for `S'` is `κ` times the local
sum for `S`. -/
theorem value_local_smul (R₀ S S' : Code E) (T : Finset E) (κ : R)
    (hR : ∀ e ∈ T, ¬ R₀.Occurs e)
    (hocc : ∀ e ∉ T, (S.Occurs e ↔ S'.Occurs e))
    (hloc : ∀ v : { e // e ∉ T } → ι,
      ∑ u, loc M T S' (glue T u v) = κ * ∑ u, loc M T S (glue T u v)) :
    value M (R₀ + S') = κ * value M (R₀ + S) := by
  classical
  -- the part of the weight outside the local piece
  let A : (E → ι) → R := fun L =>
    xw M R₀.xs L * jw M R₀.js L * ∏ e ∈ univ.filter (· ∉ T), uf M (R₀ + S) e L
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
      · exact jw_congr M _ fun j hj =>
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
  rw [Finset.sum_congr rfl fun L _ => hS L, Finset.sum_congr rfl fun L _ => hS' L, hsum, hsum,
    Finset.mul_sum]
  refine Finset.sum_congr rfl fun v _ => ?_
  have hfac : ∀ S₁ : Code E, ∑ u, A (glue T u v) * loc M T S₁ (glue T u v)
      = A (glue T (fun _ => M.base) v) * ∑ u, loc M T S₁ (glue T u v) := fun S₁ => by
    rw [Finset.mul_sum]
    exact Finset.sum_congr rfl fun u _ => by rw [hA u (fun _ => M.base) v]
  rw [hfac, hfac, hloc v]
  ring

/-- **Local replacement.** The case `κ = 1` of `value_local_smul`. -/
theorem value_local (R₀ S S' : Code E) (T : Finset E)
    (hR : ∀ e ∈ T, ¬ R₀.Occurs e)
    (hocc : ∀ e ∉ T, (S.Occurs e ↔ S'.Occurs e))
    (hloc : ∀ v : { e // e ∉ T } → ι,
      ∑ u, loc M T S (glue T u v) = ∑ u, loc M T S' (glue T u v)) :
    value M (R₀ + S) = value M (R₀ + S') := by
  have := value_local_smul M R₀ S' S T 1 hR (fun e he => (hocc e he).symm)
    (fun v => by rw [one_mul, hloc v])
  rw [this, one_mul]

end Value

/-! ### Sums over the labels of internal edges -/

section Glue

variable {E : Type u} [Fintype E] [DecidableEq E]

omit [Fintype E] [DecidableEq ι] in
/-- A sum over the label of one internal edge is a sum over `ι`. -/
theorem sum_glue_single (e : E) (b : ι) (v : { x // x ∉ ({e} : Finset E) } → ι)
    (G : (E → ι) → R) :
    ∑ u, G (glue {e} u v) = ∑ i, G (Function.update (glue {e} (fun _ => b) v) e i) := by
  let φ : ({ x // x ∈ ({e} : Finset E) } → ι) ≃ ι :=
    { toFun := fun u => u ⟨e, by simp⟩
      invFun := fun i _ => i
      left_inv := by
        intro u; funext ⟨x, hx⟩
        simp only [Finset.mem_singleton] at hx
        subst hx; rfl
      right_inv := fun _ => rfl }
  rw [← φ.symm.sum_comp]
  refine Finset.sum_congr rfl fun i _ => congrArg G ?_
  funext x
  simp only [glue, Equiv.piEquivPiSubtypeProd_symm_apply, φ, Equiv.coe_fn_symm_mk,
    Function.update_apply, Finset.mem_singleton]
  by_cases hx : x = e
  · subst hx; simp
  · simp [hx]

omit [Fintype E] [DecidableEq ι] in
/-- A sum over the labels of two internal edges is a double sum over `ι`. -/
theorem sum_glue_pair (e f : E) (hef : e ≠ f) (b : ι) (v : { x // x ∉ ({e, f} : Finset E) } → ι)
    (G : (E → ι) → R) :
    ∑ u, G (glue {e, f} u v) =
      ∑ i, ∑ j, G (Function.update (Function.update (glue {e, f} (fun _ => b) v) e i) f j) := by
  let φ : ({ x // x ∈ ({e, f} : Finset E) } → ι) ≃ ι × ι :=
    { toFun := fun u => (u ⟨e, by simp⟩, u ⟨f, by simp⟩)
      invFun := fun p x => if x.1 = e then p.1 else p.2
      left_inv := by
        intro u; funext ⟨x, hx⟩
        simp only [Finset.mem_insert, Finset.mem_singleton] at hx
        rcases hx with rfl | rfl
        · simp
        · simp [Ne.symm hef]
      right_inv := by intro p; simp [Ne.symm hef] }
  rw [← φ.symm.sum_comp, Fintype.sum_prod_type]
  refine Finset.sum_congr rfl fun i _ => Finset.sum_congr rfl fun j _ => congrArg G ?_
  funext x
  simp only [glue, Equiv.piEquivPiSubtypeProd_symm_apply, φ, Equiv.coe_fn_symm_mk,
    Function.update_apply, Finset.mem_insert, Finset.mem_singleton]
  by_cases hxf : x = f
  · subst hxf; simp [Ne.symm hef]
  · by_cases hxe : x = e
    · subst hxe; simp [hef]
    · simp [hxe, hxf]

omit [Fintype E] [DecidableEq ι] in
/-- A sum over the labels of three internal edges is a triple sum over `ι`. -/
theorem sum_glue_triple (e f g : E) (hef : e ≠ f) (heg : e ≠ g) (hfg : f ≠ g) (b : ι)
    (v : { x // x ∉ ({e, f, g} : Finset E) } → ι) (G : (E → ι) → R) :
    ∑ u, G (glue {e, f, g} u v) =
      ∑ i, ∑ j, ∑ k, G (Function.update (Function.update (Function.update
        (glue {e, f, g} (fun _ => b) v) e i) f j) g k) := by
  let φ : ({ x // x ∈ ({e, f, g} : Finset E) } → ι) ≃ ι × ι × ι :=
    { toFun := fun u => (u ⟨e, by simp⟩, u ⟨f, by simp⟩, u ⟨g, by simp⟩)
      invFun := fun p x => if x.1 = e then p.1 else if x.1 = f then p.2.1 else p.2.2
      left_inv := by
        intro u; funext ⟨x, hx⟩
        simp only [Finset.mem_insert, Finset.mem_singleton] at hx
        rcases hx with rfl | rfl | rfl
        · simp
        · simp [Ne.symm hef]
        · simp [Ne.symm heg, Ne.symm hfg]
      right_inv := by intro p; simp [Ne.symm hef, Ne.symm heg, Ne.symm hfg] }
  rw [← φ.symm.sum_comp, Fintype.sum_prod_type]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [Fintype.sum_prod_type]
  refine Finset.sum_congr rfl fun j _ => Finset.sum_congr rfl fun k _ => congrArg G ?_
  funext x
  simp only [glue, Equiv.piEquivPiSubtypeProd_symm_apply, φ, Equiv.coe_fn_symm_mk,
    Function.update_apply, Finset.mem_insert, Finset.mem_singleton]
  by_cases hxg : x = g
  · subst hxg; simp [Ne.symm heg, Ne.symm hfg]
  · by_cases hxf : x = f
    · subst hxf; simp [Ne.symm hef, hfg]
    · by_cases hxe : x = e
      · subst hxe; simp [hef, heg]
      · simp [hxe, hxf, hxg]

end Glue

/-! ### Local sums -/

section LocalSums

variable {E : Type u} [Fintype E] [DecidableEq E] (M : Model R ι)

omit [Fintype ι] [Fintype E] [DecidableEq E] in
/-- If every internal edge occurs in the local piece, the local weight is its crossings and joins. -/
theorem loc_of_occurs (T : Finset E) (S : Code E) (h : ∀ e ∈ T, S.Occurs e) (L : E → ι) :
    loc M T S L = xw M S.xs L * jw M S.js L := by
  classical
  simp only [loc]
  rw [Finset.prod_eq_one fun e he => by simp [uf, h e he], mul_one]

omit [Fintype E] in
/-- **The local sum of a piece of joins.** If no internal edge occurs in the joins `js`, the local
sum pins every internal edge to the base label. -/
theorem sum_loc_ofJs (T : Finset E) (js : Multiset (E × E × ℤ))
    (hT : ∀ e ∈ T, ¬ (Code.ofJs js).Occurs e) (v : { e // e ∉ T } → ι) :
    ∑ u, loc M T (Code.ofJs js) (glue T u v) = jw M js (glue T (fun _ => M.base) v) := by
  classical
  have hoff : ∀ u e, e ∉ T → glue T u v e = glue T (fun _ => M.base) v e := fun u e he => by
    simp [glue, Equiv.piEquivPiSubtypeProd_symm_apply, he]
  have hon : ∀ u e (he : e ∈ T), glue T u v e = u ⟨e, he⟩ := fun u e he => by
    simp [glue, Equiv.piEquivPiSubtypeProd_symm_apply, he]
  have hj : ∀ u, jw M js (glue T u v) = jw M js (glue T (fun _ => M.base) v) := fun u =>
    jw_congr M js fun j hj => ⟨hoff u _ fun h => hT _ h (Or.inr ⟨j, hj, Or.inl rfl⟩),
      hoff u _ fun h => hT _ h (Or.inr ⟨j, hj, Or.inr rfl⟩)⟩
  have hp : ∀ u, ∏ e ∈ T, uf M (Code.ofJs js) e (glue T u v) =
      ∏ e : { e // e ∈ T }, if u e = M.base then (1 : R) else 0 := by
    intro u
    rw [← Finset.prod_coe_sort]
    refine Finset.prod_congr rfl fun ⟨e, he⟩ _ => ?_
    simp only [uf, if_neg (hT e he), hon u e he]
  have hx : ∀ L, xw M (Code.ofJs js : Code E).xs L = 1 := fun L => by simp [xw, Code.ofJs]
  have hjs : (Code.ofJs js : Code E).js = js := rfl
  simp only [loc, hx, hjs, hj, hp, one_mul]
  rw [← Finset.mul_sum, Fintype.sum_eq_single (fun _ => M.base)]
  · simp
  · intro u hu
    obtain ⟨y, hy⟩ : ∃ y, u y ≠ M.base := by
      by_contra h; push_neg at h; exact hu (funext h)
    exact Finset.prod_eq_zero (Finset.mem_univ y) (by simp [hy])

/-- Collapsing a sum against a Kronecker delta that carries a weight. -/
theorem sum_mul_ite_eq (F : ι → R) (c : R) (i : ι) :
    ∑ j, F j * (if i = j then c else 0) = F i * c := by
  classical
  simp [mul_ite]

end LocalSums

/-! ### Occurrence in the local pieces -/

section Occurs

variable {E : Type u}

theorem occurs_ofJs_single (a b e : E) (t : ℤ) :
    (Code.ofJs {(a, b, t)}).Occurs e ↔ a = e ∨ b = e := by
  simp [Code.Occurs, Code.ofJs]

theorem occurs_ofJs_pair (a b c d e : E) (t t' : ℤ) :
    (Code.ofJs {(a, b, t), (c, d, t')}).Occurs e ↔ (a = e ∨ b = e) ∨ (c = e ∨ d = e) := by
  simp [Code.Occurs, Code.ofJs]

theorem occurs_ofXs_bigonPar (a b c d e₁ f₁ e : E) (s : Bool) :
    (Code.ofXs (bigonPar a b c d e₁ f₁ s)).Occurs e ↔
      c = e ∨ f₁ = e ∨ a = e ∨ e₁ = e ∨ d = e ∨ b = e := by
  simp only [Code.Occurs, Code.ofXs, bigonPar, Crossing.Mentions]
  simp
  tauto

theorem occurs_ofXs_bigonAnti (a b c d e₁ e₂ f₁ e : E) (s : Bool) :
    (Code.ofXs (bigonAnti a b c d e₁ e₂ f₁ s)).Occurs e ↔
      f₁ = e ∨ d = e ∨ a = e ∨ e₁ = e ∨ c = e ∨ e₂ = e ∨ b = e := by
  simp only [Code.Occurs, Code.ofXs, bigonAnti, Crossing.Mentions]
  simp
  tauto

theorem occurs_ofXs_kink (a b ℓ₁ ℓ₂ e : E) (u s : Bool) :
    (Code.ofXs {kink a b ℓ₁ ℓ₂ u s}).Occurs e ↔ (a = e ∨ b = e) ∨ (ℓ₁ = e ∨ ℓ₂ = e) := by
  cases u <;> simp [Code.Occurs, Code.ofXs, kink, Crossing.Mentions] <;> tauto

end Occurs

/-! ### The Reidemeister moves -/

section Moves

variable {E : Type u} [Fintype E] [DecidableEq E] (M : Model R ι)

/-- **Second Reidemeister move, parallel strands.** If the crossing tensors of signs `s` and `!s`
compose to the identity in the sense of `hX`, the value is unchanged by `r2par`. -/
theorem value_r2par (R₀ : Code E) (a b c d e₁ f₁ : E) (s : Bool)
    (he : ¬ R₀.Occurs e₁) (hf : ¬ R₀.Occurs f₁) (hef : e₁ ≠ f₁)
    (hbd : ∀ x ∈ ({a, b, c, d} : Set E), x ≠ e₁ ∧ x ≠ f₁)
    (hX : ∀ a b c d : ι, ∑ i, ∑ j, M.X s c j a i * M.X (!s) j d i b =
      if a = b ∧ c = d then 1 else 0) :
    value M (R₀ + Code.ofJs {(a, b, 0), (c, d, 0)}) =
      value M (R₀ + Code.ofXs (bigonPar a b c d e₁ f₁ s)) := by
  classical
  obtain ⟨hae, haf⟩ := hbd a (by simp)
  obtain ⟨hbe, hbf⟩ := hbd b (by simp)
  obtain ⟨hce, hcf⟩ := hbd c (by simp)
  obtain ⟨hde, hdf⟩ := hbd d (by simp)
  refine value_local M R₀ _ _ {e₁, f₁} ?_ ?_ ?_
  · intro e heT
    simp only [Finset.mem_insert, Finset.mem_singleton] at heT
    rcases heT with rfl | rfl <;> assumption
  · intro e heT
    simp only [Finset.mem_insert, Finset.mem_singleton, not_or] at heT
    rw [occurs_ofJs_pair, occurs_ofXs_bigonPar]
    have h1 : e₁ ≠ e := Ne.symm heT.1
    have h2 : f₁ ≠ e := Ne.symm heT.2
    tauto
  · intro v
    have hTL : ∀ e ∈ ({e₁, f₁} : Finset E), ¬ (Code.ofJs {(a, b, 0), (c, d, 0)}).Occurs e := by
      intro e heT
      simp only [Finset.mem_insert, Finset.mem_singleton] at heT
      rw [occurs_ofJs_pair]
      rcases heT with rfl | rfl <;> tauto
    have hTR : ∀ e ∈ ({e₁, f₁} : Finset E), (Code.ofXs (bigonPar a b c d e₁ f₁ s)).Occurs e := by
      intro e heT
      simp only [Finset.mem_insert, Finset.mem_singleton] at heT
      rw [occurs_ofXs_bigonPar]
      tauto
    rw [sum_loc_ofJs M _ _ hTL v]
    rw [sum_glue_pair e₁ f₁ hef M.base]
    simp only [loc_of_occurs M _ _ hTR]
    set L₀ := glue {e₁, f₁} (fun _ => M.base) v
    have hx : ∀ i j x, x ≠ e₁ → x ≠ f₁ →
        Function.update (Function.update L₀ e₁ i) f₁ j x = L₀ x :=
      fun i j x h1 h2 => by simp [h1, h2]
    have h1 : ∀ i j, Function.update (Function.update L₀ e₁ i) f₁ j e₁ = i :=
      fun i j => by simp [hef]
    simp only [xw, jw, Code.ofXs, bigonPar, Multiset.insert_eq_cons, Multiset.map_cons,
      Multiset.map_singleton, Multiset.map_zero, Multiset.prod_cons, Multiset.prod_singleton,
      Multiset.prod_zero, mul_one, hx _ _ a hae haf, hx _ _ b hbe hbf, hx _ _ c hce hcf,
      hx _ _ d hde hdf, h1, Function.update_self]
    rw [hX]
    by_cases hab : L₀ a = L₀ b <;> by_cases hcd : L₀ c = L₀ d <;> simp [hab, hcd]

/-- **Second Reidemeister move, antiparallel strands.** If the crossing tensors of signs `s` and
`!s`, with one full turn of weight `K ^ bigonTurn s` on the internal over edge, satisfy `hX`, the
value is unchanged by `r2anti`. -/
theorem value_r2anti (R₀ : Code E) (a b c d e₁ e₂ f₁ : E) (s : Bool)
    (hint : ∀ x ∈ ({e₁, e₂, f₁} : Set E), ¬ R₀.Occurs x)
    (h12 : e₁ ≠ e₂) (h1f : e₁ ≠ f₁) (h2f : e₂ ≠ f₁)
    (hbd : ∀ x ∈ ({a, b, c, d} : Set E), x ≠ e₁ ∧ x ≠ e₂ ∧ x ≠ f₁)
    (hX : ∀ a b c d : ι,
      ∑ i, ∑ k, M.X s k d a i * ((M.K i ^ bigonTurn s : Rˣ) : R) * M.X (!s) c k i b =
      if a = b ∧ c = d then ((M.K a ^ bigonTurn s : Rˣ) : R) else 0) :
    value M (R₀ + Code.ofJs {(a, b, bigonTurn s), (c, d, 0)}) =
      value M (R₀ + (Code.ofXs (bigonAnti a b c d e₁ e₂ f₁ s) +
        Code.ofJs {(e₁, e₂, bigonTurn s)})) := by
  classical
  obtain ⟨ha1, ha2, haf⟩ := hbd a (by simp)
  obtain ⟨hb1, hb2, hbf⟩ := hbd b (by simp)
  obtain ⟨hc1, hc2, hcf⟩ := hbd c (by simp)
  obtain ⟨hd1, hd2, hdf⟩ := hbd d (by simp)
  have hocR : ∀ e, (Code.ofXs (bigonAnti a b c d e₁ e₂ f₁ s) +
      Code.ofJs {(e₁, e₂, bigonTurn s)}).Occurs e ↔
      f₁ = e ∨ d = e ∨ a = e ∨ e₁ = e ∨ c = e ∨ e₂ = e ∨ b = e := by
    intro e
    rw [occurs_add, occurs_ofXs_bigonAnti, occurs_ofJs_single]
    tauto
  refine value_local M R₀ _ _ {e₁, e₂, f₁} ?_ ?_ ?_
  · intro e heT
    exact hint e (by simpa using heT)
  · intro e heT
    simp only [Finset.mem_insert, Finset.mem_singleton, not_or] at heT
    rw [occurs_ofJs_pair, hocR]
    have h1 : e₁ ≠ e := Ne.symm heT.1
    have h2 : e₂ ≠ e := Ne.symm heT.2.1
    have h3 : f₁ ≠ e := Ne.symm heT.2.2
    tauto
  · intro v
    have hTL : ∀ e ∈ ({e₁, e₂, f₁} : Finset E),
        ¬ (Code.ofJs {(a, b, bigonTurn s), (c, d, 0)}).Occurs e := by
      intro e heT
      simp only [Finset.mem_insert, Finset.mem_singleton] at heT
      rw [occurs_ofJs_pair]
      rcases heT with rfl | rfl | rfl <;> tauto
    have hTR : ∀ e ∈ ({e₁, e₂, f₁} : Finset E), (Code.ofXs (bigonAnti a b c d e₁ e₂ f₁ s) +
        Code.ofJs {(e₁, e₂, bigonTurn s)}).Occurs e := by
      intro e heT
      simp only [Finset.mem_insert, Finset.mem_singleton] at heT
      rw [hocR]
      tauto
    rw [sum_loc_ofJs M _ _ hTL v]
    rw [sum_glue_triple e₁ e₂ f₁ h12 h1f h2f M.base]
    simp only [loc_of_occurs M _ _ hTR]
    set L₀ := glue {e₁, e₂, f₁} (fun _ => M.base) v
    have hx : ∀ i j k x, x ≠ e₁ → x ≠ e₂ → x ≠ f₁ → Function.update (Function.update
        (Function.update L₀ e₁ i) e₂ j) f₁ k x = L₀ x :=
      fun i j k x h1 h2 h3 => by simp [h1, h2, h3]
    have hi1 : ∀ i j k, Function.update (Function.update (Function.update L₀ e₁ i) e₂ j) f₁ k e₁
        = i := fun i j k => by simp [h12, h1f]
    have hi2 : ∀ i j k, Function.update (Function.update (Function.update L₀ e₁ i) e₂ j) f₁ k e₂
        = j := fun i j k => by simp [h2f]
    simp only [xw, jw, Code.ofXs, Code.ofJs, Code.add_xs, Code.add_js, bigonAnti,
      Multiset.insert_eq_cons, Multiset.map_cons, Multiset.map_singleton,
      Multiset.prod_cons, Multiset.prod_singleton, add_zero,
      zero_add, hx _ _ _ a ha1 ha2 haf, hx _ _ _ b hb1 hb2 hbf, hx _ _ _ c hc1 hc2 hcf,
      hx _ _ _ d hd1 hd2 hdf, hi1, hi2, Function.update_self]
    have hcol : ∀ i, ∑ j, ∑ k, M.X s k (L₀ d) (L₀ a) i * M.X (!s) (L₀ c) k j (L₀ b) *
        (if i = j then ((M.K i ^ bigonTurn s : Rˣ) : R) else 0) =
        ∑ k, M.X s k (L₀ d) (L₀ a) i * ((M.K i ^ bigonTurn s : Rˣ) : R) *
          M.X (!s) (L₀ c) k i (L₀ b) := by
      intro i
      rw [Finset.sum_comm]
      refine Finset.sum_congr rfl fun k _ => ?_
      rw [sum_mul_ite_eq (fun j => M.X s k (L₀ d) (L₀ a) i * M.X (!s) (L₀ c) k j (L₀ b))]
      ring
    rw [Finset.sum_congr rfl fun i _ => hcol i, hX]
    by_cases hab : L₀ a = L₀ b <;> by_cases hcd : L₀ c = L₀ d <;> simp [hab, hcd]

/-- The weight of a kink with incoming label `x`, outgoing label `y`, and label `i` on the loop. -/
def kinkW (u s : Bool) (x y i : ι) : R :=
  if u then M.X s x i i y else M.X s i y x i

omit [Fintype ι] [DecidableEq ι] [Fintype E] [DecidableEq E] in
theorem kinkW_true (s : Bool) (x y i : ι) : kinkW M true s x y i = M.X s x i i y := rfl

omit [Fintype ι] [DecidableEq ι] [Fintype E] [DecidableEq E] in
theorem kinkW_false (s : Bool) (x y i : ι) : kinkW M false s x y i = M.X s i y x i := rfl

omit [Fintype E] [DecidableEq E] in
theorem kink_true (a b ℓ₁ ℓ₂ : E) (s : Bool) : kink a b ℓ₁ ℓ₂ true s = ⟨a, ℓ₁, ℓ₂, b, s⟩ := rfl

omit [Fintype E] [DecidableEq E] in
theorem kink_false (a b ℓ₁ ℓ₂ : E) (s : Bool) : kink a b ℓ₁ ℓ₂ false s = ⟨ℓ₂, b, a, ℓ₁, s⟩ := rfl

/-- **First Reidemeister move, up to a factor.** If closing a strand through a kink of type
`(u, s)`, with the loop turning `kinkTurn u s` times, multiplies the identity by `κ`, then adding
the kink multiplies the value by `κ`. -/
theorem value_r1 (R₀ : Code E) (a b ℓ₁ ℓ₂ : E) (u s : Bool) (κ : R)
    (h₁ : ¬ R₀.Occurs ℓ₁) (h₂ : ¬ R₀.Occurs ℓ₂) (h₁₂ : ℓ₁ ≠ ℓ₂)
    (hbd : ∀ x ∈ ({a, b} : Set E), x ≠ ℓ₁ ∧ x ≠ ℓ₂)
    (hK : ∀ x y : ι, ∑ i, kinkW M u s x y i * ((M.K i ^ kinkTurn u s : Rˣ) : R) =
      κ * if x = y then 1 else 0) :
    value M (R₀ + (Code.ofXs {kink a b ℓ₁ ℓ₂ u s} + Code.ofJs {(ℓ₁, ℓ₂, kinkTurn u s)})) =
      κ * value M (R₀ + Code.ofJs {(a, b, 0)}) := by
  classical
  obtain ⟨ha1, ha2⟩ := hbd a (by simp)
  obtain ⟨hb1, hb2⟩ := hbd b (by simp)
  have hocR : ∀ e, (Code.ofXs {kink a b ℓ₁ ℓ₂ u s} +
      Code.ofJs {(ℓ₁, ℓ₂, kinkTurn u s)}).Occurs e ↔ (a = e ∨ b = e) ∨ (ℓ₁ = e ∨ ℓ₂ = e) := by
    intro e
    rw [occurs_add, occurs_ofXs_kink, occurs_ofJs_single]
    tauto
  refine value_local_smul M R₀ _ _ {ℓ₁, ℓ₂} κ ?_ ?_ ?_
  · intro e heT
    simp only [Finset.mem_insert, Finset.mem_singleton] at heT
    rcases heT with rfl | rfl <;> assumption
  · intro e heT
    simp only [Finset.mem_insert, Finset.mem_singleton, not_or] at heT
    rw [occurs_ofJs_single, hocR]
    have h1 : ℓ₁ ≠ e := Ne.symm heT.1
    have h2 : ℓ₂ ≠ e := Ne.symm heT.2
    tauto
  · intro v
    have hTL : ∀ e ∈ ({ℓ₁, ℓ₂} : Finset E), ¬ (Code.ofJs {(a, b, 0)}).Occurs e := by
      intro e heT
      simp only [Finset.mem_insert, Finset.mem_singleton] at heT
      rw [occurs_ofJs_single]
      rcases heT with rfl | rfl <;> tauto
    have hTR : ∀ e ∈ ({ℓ₁, ℓ₂} : Finset E), (Code.ofXs {kink a b ℓ₁ ℓ₂ u s} +
        Code.ofJs {(ℓ₁, ℓ₂, kinkTurn u s)}).Occurs e := by
      intro e heT
      simp only [Finset.mem_insert, Finset.mem_singleton] at heT
      rw [hocR]
      tauto
    rw [sum_loc_ofJs M _ _ hTL v]
    rw [sum_glue_pair ℓ₁ ℓ₂ h₁₂ M.base]
    simp only [loc_of_occurs M _ _ hTR]
    set L₀ := glue {ℓ₁, ℓ₂} (fun _ => M.base) v
    have hx : ∀ i j x, x ≠ ℓ₁ → x ≠ ℓ₂ →
        Function.update (Function.update L₀ ℓ₁ i) ℓ₂ j x = L₀ x :=
      fun i j x h1 h2 => by simp [h1, h2]
    have h1 : ∀ i j, Function.update (Function.update L₀ ℓ₁ i) ℓ₂ j ℓ₁ = i :=
      fun i j => by simp [h₁₂]
    have hcol : ∀ i, ∑ j, xw M (Code.ofXs {kink a b ℓ₁ ℓ₂ u s} +
        Code.ofJs {(ℓ₁, ℓ₂, kinkTurn u s)}).xs (Function.update (Function.update L₀ ℓ₁ i) ℓ₂ j) *
        jw M (Code.ofXs {kink a b ℓ₁ ℓ₂ u s} + Code.ofJs {(ℓ₁, ℓ₂, kinkTurn u s)}).js
          (Function.update (Function.update L₀ ℓ₁ i) ℓ₂ j) =
        kinkW M u s (L₀ a) (L₀ b) i * ((M.K i ^ kinkTurn u s : Rˣ) : R) := by
      intro i
      simp only [xw, jw, Code.ofXs, Code.ofJs, Code.add_xs, Code.add_js, add_zero, zero_add,
        Multiset.map_singleton, Multiset.prod_singleton, h1, Function.update_self]
      cases u
      · rw [kink_false, kinkW_false]
        simp only [hx _ _ a ha1 ha2, hx _ _ b hb1 hb2, h1, Function.update_self]
        rw [sum_mul_ite_eq (fun j => M.X s j (L₀ b) (L₀ a) i)]
      · rw [kink_true, kinkW_true]
        simp only [hx _ _ a ha1 ha2, hx _ _ b hb1 hb2, h1, Function.update_self]
        rw [sum_mul_ite_eq (fun j => M.X s (L₀ a) i j (L₀ b))]
    rw [Finset.sum_congr rfl fun i _ => hcol i, hK]
    simp only [jw, Multiset.map_singleton, Multiset.prod_singleton, zpow_zero, Units.val_one]

/-- **Merging two joins.** Two consecutive joins through an otherwise unused edge are one join
whose turn is the sum of their turns. -/
theorem value_merge (R₀ : Code E) (a b c : E) (t t' : ℤ)
    (hb : ¬ R₀.Occurs b) (hab : b ≠ a) (hcb : b ≠ c) :
    value M (R₀ + Code.ofJs {(a, b, t), (b, c, t')}) =
      value M (R₀ + Code.ofJs {(a, c, t + t')}) := by
  classical
  refine value_local M R₀ _ _ {b} ?_ ?_ ?_
  · intro e he
    simp only [Finset.mem_singleton] at he
    subst he; exact hb
  · intro e he
    simp only [Finset.mem_singleton] at he
    rw [occurs_ofJs_pair, occurs_ofJs_single]
    have : b ≠ e := Ne.symm he
    tauto
  · intro v
    have hTL : ∀ e ∈ ({b} : Finset E), (Code.ofJs {(a, b, t), (b, c, t')}).Occurs e := by
      intro e he
      simp only [Finset.mem_singleton] at he
      subst he; rw [occurs_ofJs_pair]; tauto
    have hTR : ∀ e ∈ ({b} : Finset E), ¬ (Code.ofJs {(a, c, t + t')}).Occurs e := by
      intro e he
      simp only [Finset.mem_singleton] at he
      subst he; rw [occurs_ofJs_single]
      rintro (h | h)
      exacts [hab h.symm, hcb h.symm]
    rw [sum_loc_ofJs M _ _ hTR v]
    rw [sum_glue_single b M.base]
    simp only [loc_of_occurs M _ _ hTL]
    set L₀ := glue {b} (fun _ => M.base) v
    have hx : ∀ i x, x ≠ b → Function.update L₀ b i x = L₀ x := fun i x h => by simp [h]
    simp only [xw, jw, Code.ofJs, Multiset.insert_eq_cons, Multiset.map_cons,
      Multiset.map_singleton, Multiset.map_zero, Multiset.prod_cons, Multiset.prod_singleton,
      Multiset.prod_zero, one_mul, hx _ a (Ne.symm hab), hx _ c (Ne.symm hcb),
      Function.update_self]
    simp only [ite_mul, zero_mul, Finset.sum_ite_eq, Finset.mem_univ, if_true]
    by_cases hac : L₀ a = L₀ c
    · simp [hac, zpow_add, Units.val_mul]
    · simp [hac]


omit [Fintype ι] [DecidableEq ι] [Fintype E] [DecidableEq E] in
theorem occurs_ofXs_triL (a₀ a₁ a₂ b₀ b₁ b₂ c₀ c₁ c₂ e : E) :
    (Code.ofXs (triL a₀ a₁ a₂ b₀ b₁ b₂ c₀ c₁ c₂)).Occurs e ↔
      a₀ = e ∨ a₁ = e ∨ a₂ = e ∨ b₀ = e ∨ b₁ = e ∨ b₂ = e ∨ c₀ = e ∨ c₁ = e ∨ c₂ = e := by
  simp only [Code.Occurs, Code.ofXs, triL, Crossing.Mentions]
  simp
  tauto

omit [Fintype ι] [DecidableEq ι] [Fintype E] [DecidableEq E] in
theorem occurs_ofXs_triR (a₀ a₁ a₂ b₀ b₁ b₂ c₀ c₁ c₂ e : E) :
    (Code.ofXs (triR a₀ a₁ a₂ b₀ b₁ b₂ c₀ c₁ c₂)).Occurs e ↔
      a₀ = e ∨ a₁ = e ∨ a₂ = e ∨ b₀ = e ∨ b₁ = e ∨ b₂ = e ∨ c₀ = e ∨ c₁ = e ∨ c₂ = e := by
  simp only [Code.Occurs, Code.ofXs, triR, Crossing.Mentions]
  simp
  tauto

/-- **Third Reidemeister move.** If the positive crossing tensor satisfies the Yang–Baxter
identity `hYB`, in which `i, j, k` are the labels of the internal edges `a₁, b₁, c₁`, the value is
unchanged by `r3`. -/
theorem value_r3 (R₀ : Code E) (a₀ a₁ a₂ b₀ b₁ b₂ c₀ c₁ c₂ : E)
    (hint : ∀ x ∈ ({a₁, b₁, c₁} : Set E), ¬ R₀.Occurs x)
    (hab : a₁ ≠ b₁) (hac : a₁ ≠ c₁) (hbc : b₁ ≠ c₁)
    (hbd : ∀ x ∈ ({a₀, a₂, b₀, b₂, c₀, c₂} : Set E), x ≠ a₁ ∧ x ≠ b₁ ∧ x ≠ c₁)
    (hYB : ∀ a₀ a₂ b₀ b₂ c₀ c₂ : ι,
      ∑ i, ∑ j, ∑ k, M.X true b₀ j a₀ i * M.X true c₀ k i a₂ * M.X true k c₂ j b₂ =
      ∑ i, ∑ j, ∑ k, M.X true c₀ k b₀ j * M.X true k c₂ a₀ i * M.X true j b₂ i a₂) :
    value M (R₀ + Code.ofXs (triL a₀ a₁ a₂ b₀ b₁ b₂ c₀ c₁ c₂)) =
      value M (R₀ + Code.ofXs (triR a₀ a₁ a₂ b₀ b₁ b₂ c₀ c₁ c₂)) := by
  classical
  obtain ⟨ha0a, ha0b, ha0c⟩ := hbd a₀ (by simp)
  obtain ⟨ha2a, ha2b, ha2c⟩ := hbd a₂ (by simp)
  obtain ⟨hb0a, hb0b, hb0c⟩ := hbd b₀ (by simp)
  obtain ⟨hb2a, hb2b, hb2c⟩ := hbd b₂ (by simp)
  obtain ⟨hc0a, hc0b, hc0c⟩ := hbd c₀ (by simp)
  obtain ⟨hc2a, hc2b, hc2c⟩ := hbd c₂ (by simp)
  refine value_local M R₀ _ _ {a₁, b₁, c₁} ?_ ?_ ?_
  · intro e heT
    exact hint e (by simpa using heT)
  · intro e _
    rw [occurs_ofXs_triL, occurs_ofXs_triR]
  · intro v
    rw [sum_glue_triple a₁ b₁ c₁ hab hac hbc M.base, sum_glue_triple a₁ b₁ c₁ hab hac hbc M.base]
    set L₀ := glue {a₁, b₁, c₁} (fun _ => M.base) v
    have hT : ∀ (S : Code E), S.Occurs a₁ → S.Occurs b₁ → S.Occurs c₁ → ∀ L,
        loc M {a₁, b₁, c₁} S L = xw M S.xs L * jw M S.js L := by
      intro S h1 h2 h3 L
      simp only [loc]
      rw [Finset.prod_eq_one]
      · ring
      · intro e he
        simp only [Finset.mem_insert, Finset.mem_singleton] at he
        rcases he with rfl | rfl | rfl <;> simp [uf, *]
    rw [Finset.sum_congr rfl fun i _ => Finset.sum_congr rfl fun j _ =>
        Finset.sum_congr rfl fun k _ => hT _ (by rw [occurs_ofXs_triL]; tauto)
          (by rw [occurs_ofXs_triL]; tauto) (by rw [occurs_ofXs_triL]; tauto) _,
      Finset.sum_congr rfl fun i _ => Finset.sum_congr rfl fun j _ =>
        Finset.sum_congr rfl fun k _ => hT _ (by rw [occurs_ofXs_triR]; tauto)
          (by rw [occurs_ofXs_triR]; tauto) (by rw [occurs_ofXs_triR]; tauto) _]
    have hx : ∀ i j k x, x ≠ a₁ → x ≠ b₁ → x ≠ c₁ → Function.update (Function.update
        (Function.update L₀ a₁ i) b₁ j) c₁ k x = L₀ x :=
      fun i j k x h1 h2 h3 => by simp [h1, h2, h3]
    have hia : ∀ i j k, Function.update (Function.update (Function.update L₀ a₁ i) b₁ j) c₁ k a₁
        = i := fun i j k => by simp [hab, hac]
    have hib : ∀ i j k, Function.update (Function.update (Function.update L₀ a₁ i) b₁ j) c₁ k b₁
        = j := fun i j k => by simp [hbc]
    simp only [xw, jw, Code.ofXs, triL, triR, Multiset.map_zero, Multiset.prod_zero, mul_one,
      Multiset.insert_eq_cons, Multiset.map_cons, Multiset.map_singleton, Multiset.prod_cons,
      Multiset.prod_singleton, hx _ _ _ a₀ ha0a ha0b ha0c, hx _ _ _ a₂ ha2a ha2b ha2c,
      hx _ _ _ b₀ hb0a hb0b hb0c, hx _ _ _ b₂ hb2a hb2b hb2c, hx _ _ _ c₀ hc0a hc0b hc0c,
      hx _ _ _ c₂ hc2a hc2b hc2c, Function.update_self, hia, hib]
    convert hYB (L₀ a₀) (L₀ a₂) (L₀ b₀) (L₀ b₂) (L₀ c₀) (L₀ c₂) using 4 <;> ring

end Moves

/-! ### Relabelling and contraction -/

section Relabel

variable {E F : Type u} (M : Model R ι)

omit [Fintype ι] [DecidableEq ι] in
theorem xw_map (f : E → F) (xs : Multiset (Crossing E)) (L : F → ι) :
    xw M (xs.map (Crossing.map f)) L = xw M xs (L ∘ f) := by
  simp [xw, Multiset.map_map, Crossing.map]

omit [Fintype ι] in
theorem jw_map (f : E → F) (js : Multiset (E × E × ℤ)) (L : F → ι) :
    jw M (js.map (Prod.map f (Prod.map f id))) L = jw M js (L ∘ f) := by
  simp [jw, Multiset.map_map]

omit [Fintype ι] [DecidableEq ι] in
theorem occurs_map (f : E → F) (D : Code E) (y : F) :
    (D.map f).Occurs y ↔ ∃ e, D.Occurs e ∧ f e = y := by
  simp only [Code.Occurs, Code.map, Multiset.mem_map, Crossing.Mentions, Crossing.map,
    Prod.map]
  constructor
  · rintro (⟨_, ⟨x, hx, rfl⟩, h⟩ | ⟨_, ⟨j, hj, rfl⟩, h⟩)
    · rcases h with h | h | h | h
      exacts [⟨_, Or.inl ⟨x, hx, Or.inl rfl⟩, h⟩, ⟨_, Or.inl ⟨x, hx, Or.inr (Or.inl rfl)⟩, h⟩,
        ⟨_, Or.inl ⟨x, hx, Or.inr (Or.inr (Or.inl rfl))⟩, h⟩,
        ⟨_, Or.inl ⟨x, hx, Or.inr (Or.inr (Or.inr rfl))⟩, h⟩]
    · rcases h with h | h
      exacts [⟨_, Or.inr ⟨j, hj, Or.inl rfl⟩, h⟩, ⟨_, Or.inr ⟨j, hj, Or.inr rfl⟩, h⟩]
  · rintro ⟨e, (⟨x, hx, h⟩ | ⟨j, hj, h⟩), rfl⟩
    · refine Or.inl ⟨_, ⟨x, hx, rfl⟩, ?_⟩
      rcases h with rfl | rfl | rfl | rfl <;> simp
    · refine Or.inr ⟨_, ⟨j, hj, rfl⟩, ?_⟩
      rcases h with rfl | rfl <;> simp

/-- **Relabelling along an embedding.** The value does not change when a code is moved into a
larger edge type: the new edges do not occur, so they are pinned to the base label. -/
theorem value_embed [Fintype E] [DecidableEq E] [Fintype F] [DecidableEq F]
    (f : E ↪ F) (D : Code E) : value M (D.map f) = value M D := by
  classical
  let φ : (F → ι) ≃ (E → ι) × ({ y // y ∉ Set.range f } → ι) :=
    { toFun := fun L => (L ∘ f, fun y => L y.1)
      invFun := fun p y => if h : y ∈ Set.range f then p.1 h.choose else p.2 ⟨y, h⟩
      left_inv := by
        intro L; funext y
        by_cases h : y ∈ Set.range f
        · simp only [h, dif_pos, Function.comp_apply]; rw [h.choose_spec]
        · simp [h]
      right_inv := by
        rintro ⟨w, v⟩
        refine Prod.ext (funext fun x => ?_) (funext fun ⟨y, hy⟩ => by simp [hy])
        have h : f x ∈ Set.range f := ⟨x, rfl⟩
        simp only [Function.comp_apply, h, dif_pos]
        rw [f.injective h.choose_spec] }
  let A : (E → ι) → R := weight M D
  let B : ({ y // y ∉ Set.range f } → ι) → R := fun v =>
    ∏ y, if v y = M.base then 1 else 0
  have hw : ∀ L, weight M (D.map f) L = A (φ L).1 * B (φ L).2 := by
    intro L
    simp only [weight, A, B, φ, Equiv.coe_fn_mk]
    rw [show (D.map f).xs = D.xs.map (Crossing.map f) from rfl,
      show (D.map f).js = D.js.map (Prod.map f (Prod.map f id)) from rfl, xw_map, jw_map]
    rw [← Finset.prod_filter_mul_prod_filter_not univ (· ∈ Set.range f)]
    have hr : univ.filter (· ∈ Set.range f) = univ.map f := by
      ext y; simp [eq_comm]
    have h1 : ∏ y ∈ univ.filter (· ∈ Set.range f), uf M (D.map f) y L = ∏ e, uf M D e (L ∘ f) := by
      rw [hr, Finset.prod_map]
      refine Finset.prod_congr rfl fun e _ => ?_
      have : (D.map f).Occurs (f e) ↔ D.Occurs e := by
        rw [occurs_map]
        exact ⟨fun ⟨e', h, he'⟩ => f.injective he' ▸ h, fun h => ⟨e, h, rfl⟩⟩
      simp only [uf, this, Function.comp_apply]
    have h2 : ∏ y ∈ univ.filter (fun y => ¬ y ∈ Set.range f), uf M (D.map f) y L =
        ∏ y : { y // y ∉ Set.range f }, if L y.1 = M.base then 1 else 0 := by
      rw [Finset.prod_subtype (p := fun y => y ∉ Set.range f) _ (fun y => by simp)]
      refine Finset.prod_congr rfl fun ⟨y, hy⟩ _ => ?_
      have : ¬ (D.map f).Occurs y := by
        rw [occurs_map]; rintro ⟨e, _, rfl⟩; exact hy ⟨e, rfl⟩
      simp only [uf, this, if_false]
    rw [h1, h2]
    ring
  have hB : ∑ v, B v = 1 := by
    rw [Fintype.sum_eq_single (fun _ => M.base)]
    · simp [B]
    · intro v hv
      obtain ⟨y, hy⟩ : ∃ y, v y ≠ M.base := by
        by_contra h; push_neg at h; exact hv (funext h)
      exact Finset.prod_eq_zero (Finset.mem_univ y) (by simp [hy])
  have hsum : ∑ L, A (φ L).1 * B (φ L).2 =
      ∑ p : (E → ι) × ({ y // y ∉ Set.range f } → ι), A p.1 * B p.2 :=
    φ.sum_comp (fun p => A p.1 * B p.2)
  have hA : A = weight M D := rfl
  clear_value φ A B
  unfold value
  rw [Finset.sum_congr rfl fun L _ => hw L, hsum, Fintype.sum_prod_type, ← Finset.sum_mul_sum]
  rw [hB, mul_one, hA]

/-- **Contracting a join.** Removing the join `(a, b)` and renaming `b` to `a` does not change the
value, provided `a` or `b` occurs elsewhere. -/
theorem value_contract [Fintype E] [DecidableEq E] (R₀ : Code E) (a b : E) (hab : a ≠ b)
    (hR : R₀.Occurs a ∨ R₀.Occurs b) :
    value M (R₀.map (Function.update id b a)) = value M (R₀ + Code.ofJs {(a, b, 0)}) := by
  classical
  set f : E → E := Function.update id b a with hf
  have hfb : ∀ x, f x = if x = b then a else x := fun x => by
    by_cases h : x = b <;> simp [hf, h]
  have hocc : ∀ y, (R₀.map f).Occurs y ↔ (y ≠ b ∧ (R₀.Occurs y ∨ (y = a ∧ R₀.Occurs b))) := by
    intro y
    rw [occurs_map]
    constructor
    · rintro ⟨e, he, rfl⟩
      rw [hfb]
      by_cases h : e = b
      · subst h; simp [hab, he]
      · simp [h, he]
    · rintro ⟨hyb, hy | ⟨rfl, hb⟩⟩
      · exact ⟨y, hy, by rw [hfb, if_neg hyb]⟩
      · exact ⟨b, hb, by rw [hfb, if_pos rfl]⟩
  have hJ : ∀ y, (Code.ofJs {(a, b, 0)} : Code E).Occurs y ↔ a = y ∨ b = y :=
    fun y => occurs_ofJs_single a b y 0
  have hcomp : ∀ L : E → ι, L b = M.base →
      Function.update L b (L a) = L ∘ f := fun L _ => by
    funext x; rw [Function.comp_apply, hfb]
    by_cases h : x = b
    · subst h; simp
    · simp [h]
  unfold value
  rw [sum_split b M.base (weight M (R₀ + Code.ofJs {(a, b, 0)}))]
  refine Finset.sum_congr rfl fun L _ => ?_
  have hpin : weight M (R₀.map f) L = if L b = M.base then weight M (R₀.map f) L else 0 := by
    split_ifs with h
    · rfl
    · have hnb : ¬ (R₀.map f).Occurs b := by rw [hocc]; tauto
      simp only [weight]
      rw [Finset.prod_eq_zero (Finset.mem_univ b) (by simp [uf, hnb, h]), mul_zero]
  rw [hpin]
  split_ifs with hLb
  swap; · rfl
  rw [Fintype.sum_eq_single (L a)]
  · rw [hcomp L hLb]
    simp only [weight, Code.add_xs, Code.add_js, xw_add, jw_add]
    rw [show (R₀.map f).xs = R₀.xs.map (Crossing.map f) from rfl,
      show (R₀.map f).js = R₀.js.map (Prod.map f (Prod.map f id)) from rfl, xw_map, jw_map]
    have hx0 : xw M (Code.ofJs {(a, b, 0)} : Code E).xs (L ∘ f) = 1 := by simp [xw, Code.ofJs]
    have hj0 : jw M (Code.ofJs {(a, b, 0)} : Code E).js (L ∘ f) = 1 := by
      simp [jw, Code.ofJs, hfb, hab]
    rw [hx0, hj0, mul_one, mul_one]
    congr 1
    refine Finset.prod_congr rfl fun e _ => ?_
    by_cases heb : e = b
    · subst heb
      have h1 : (R₀ + Code.ofJs {(a, e, 0)}).Occurs e := by rw [occurs_add, hJ]; tauto
      have h2 : ¬ (R₀.map f).Occurs e := by rw [hocc]; tauto
      simp only [uf, h1, h2, hLb, if_true, if_false]
    · by_cases hea : e = a
      · subst hea
        have h1 : (R₀ + Code.ofJs {(e, b, 0)}).Occurs e := by rw [occurs_add, hJ]; tauto
        have h2 : (R₀.map f).Occurs e := by rw [hocc]; tauto
        simp only [uf, h1, h2, if_true]
      · have h12 : (R₀ + Code.ofJs {(a, b, 0)}).Occurs e ↔ (R₀.map f).Occurs e := by
          rw [occurs_add, hJ, hocc]
          constructor
          · rintro (h | h | h)
            · exact ⟨heb, Or.inl h⟩
            · exact absurd h.symm hea
            · exact absurd h.symm heb
          · rintro ⟨_, h | ⟨h, _⟩⟩
            · exact Or.inl h
            · exact absurd h hea
        simp only [uf, h12, Function.comp_apply, hfb, if_neg heb]
  · intro i hi
    simp only [weight, Code.add_js, jw_add]
    have : jw M (Code.ofJs {(a, b, 0)} : Code E).js (Function.update L b i) = 0 := by
      simp [jw, Code.ofJs, hab, Function.update_apply, Ne.symm hi]
    rw [this]; ring

end Relabel

/-! ### Reidemeister invariance of the normalised value -/

section Invariance

/-- The writhe of a code: positive crossings minus negative crossings. -/
def writhe {E : Type*} (D : Code E) : ℤ := (D.xs.map fun x => if x.pos then (1 : ℤ) else -1).sum

theorem writhe_add {E : Type*} (D D' : Code E) : writhe (D + D') = writhe D + writhe D' := by
  simp [writhe, Multiset.map_add, Multiset.sum_add]

theorem writhe_ofJs {E : Type*} (js : Multiset (E × E × ℤ)) : writhe (Code.ofJs js) = 0 := by
  simp [writhe, Code.ofJs]

theorem writhe_map {E F : Type u} (f : E → F) (D : Code E) : writhe (D.map f) = writhe D := by
  simp [writhe, Code.map, Multiset.map_map, Crossing.map]

/-- The sign `±1` of a crossing sign, as an integer. -/
def signZ (s : Bool) : ℤ := if s then 1 else -1

/-- **The local identities of an invariant model.** `θ` is the framing factor of a kink. The
turn weights `K` enter `r1` (the loop of a kink turns `kinkTurn u s` times) and `r2anti` (the over
strand of an antiparallel bigon turns `bigonTurn s` times). -/
structure Model.Invariant (M : Model R ι) (θ : Rˣ) : Prop where
  r1 : ∀ u s : Bool, ∀ x y : ι,
    ∑ i, kinkW M u s x y i * ((M.K i ^ kinkTurn u s : Rˣ) : R) =
      ((θ ^ signZ s : Rˣ) : R) * if x = y then 1 else 0
  r2par : ∀ s : Bool, ∀ a b c d : ι,
    ∑ i, ∑ j, M.X s c j a i * M.X (!s) j d i b = if a = b ∧ c = d then 1 else 0
  r2anti : ∀ s : Bool, ∀ a b c d : ι,
    ∑ i, ∑ k, M.X s k d a i * ((M.K i ^ bigonTurn s : Rˣ) : R) * M.X (!s) c k i b =
      if a = b ∧ c = d then ((M.K a ^ bigonTurn s : Rˣ) : R) else 0
  r3 : ∀ a₀ a₂ b₀ b₂ c₀ c₂ : ι,
    ∑ i, ∑ j, ∑ k, M.X true b₀ j a₀ i * M.X true c₀ k i a₂ * M.X true k c₂ j b₂ =
    ∑ i, ∑ j, ∑ k, M.X true c₀ k b₀ j * M.X true k c₂ a₀ i * M.X true j b₂ i a₂

/-- **The writhe-normalised value** of a bundled code. -/
noncomputable def normValue (M : Model R ι) (θ : Rˣ) (D : Bundled.{u}) : R :=
  ((θ⁻¹ ^ writhe D.code : Rˣ) : R) * value M D.code

variable {M : Model R ι} {θ : Rˣ}

theorem normValue_eq_of_move (hM : M.Invariant θ) {D D' : Bundled.{u}} (h : Move D D') :
    normValue M θ D = normValue M θ D' := by
  cases h with
  | embed f D =>
    simp only [normValue, writhe_map, value_embed]
  | contract R₀ a b hab hR =>
    simp only [normValue, writhe_map, writhe_add, writhe_ofJs, add_zero,
      value_contract M R₀ a b hab hR]
  | merge R₀ a b c t t' hb hab hcb =>
    simp only [normValue, writhe_add, writhe_ofJs, value_merge M R₀ a b c t t' hb hab hcb]
  | r1 R₀ a b ℓ₁ ℓ₂ u s h₁ h₂ h₁₂ hbd =>
    simp only [normValue]
    rw [value_r1 M R₀ a b ℓ₁ ℓ₂ u s _ h₁ h₂ h₁₂ hbd (hM.r1 u s)]
    have hw : writhe (Code.ofXs {kink a b ℓ₁ ℓ₂ u s} : Code _) = signZ s := by
      cases u <;> simp [writhe, Code.ofXs, kink, signZ]
    simp only [writhe_add, writhe_ofJs, hw, add_zero]
    rw [← mul_assoc, ← Units.val_mul]
    congr 2
    rw [inv_zpow', inv_zpow', ← zpow_add, neg_add, add_assoc, neg_add_cancel, add_zero]
  | r2par R₀ a b c d e₁ f₁ s he hf hef hbd =>
    simp only [normValue]
    rw [← value_r2par M R₀ a b c d e₁ f₁ s he hf hef hbd (hM.r2par s), writhe_add, writhe_add,
      writhe_ofJs]
    congr 4
    cases s <;> simp [writhe, Code.ofXs, bigonPar]
  | r2anti R₀ a b c d e₁ e₂ f₁ s hint h12 h1f h2f hbd =>
    simp only [normValue]
    rw [← value_r2anti M R₀ a b c d e₁ e₂ f₁ s hint h12 h1f h2f hbd (hM.r2anti s)]
    simp only [writhe_add, writhe_ofJs, add_zero]
    congr 4
    cases s <;> simp [writhe, Code.ofXs, bigonAnti]
  | r3 R₀ a₀ a₁ a₂ b₀ b₁ b₂ c₀ c₁ c₂ hint hab hac hbc hbd =>
    simp only [normValue]
    rw [value_r3 M R₀ a₀ a₁ a₂ b₀ b₁ b₂ c₀ c₁ c₂ hint hab hac hbc hbd hM.r3, writhe_add,
      writhe_add]
    rfl

/-- **Invariance.** For a model satisfying the local identities, the writhe-normalised value is an
invariant of Reidemeister equivalence. -/
theorem normValue_eq (hM : M.Invariant θ) {D D' : Bundled.{u}} (h : ReidemeisterEquiv D D') :
    normValue M θ D = normValue M θ D' := by
  induction h with
  | rel _ _ h => exact normValue_eq_of_move hM h
  | refl => rfl
  | symm _ _ _ ih => exact ih.symm
  | trans _ _ _ _ _ ih₁ ih₂ => exact ih₁.trans ih₂

/-! ### The identity model -/

/-- **The identity model**: each crossing passes its labels straight through, and turns have
weight `1`. Its value counts labellings constant along each component. It shows that the local
identities of `Model.Invariant` are consistent; it is not a knot invariant of any interest. -/
def idModel (R : Type*) [CommRing R] (b : ι) : Model R ι where
  X _ uin uout oin oout := if uin = uout ∧ oin = oout then 1 else 0
  K _ := 1
  base := b

theorem idModel_invariant (R : Type*) [CommRing R] (b : ι) : (idModel R b).Invariant 1 where
  r1 u s x y := by
    cases u <;> simp [kinkW, idModel, Finset.sum_ite_eq, ite_and, eq_comm]
  r2par s a b c d := by
    simp only [idModel, ite_and, mul_ite, mul_one, mul_zero]
    simp [Finset.sum_ite_eq, eq_comm]
    split_ifs <;> simp_all
  r2anti s a b c d := by
    simp only [idModel, one_zpow, Units.val_one, mul_one, ite_and, mul_ite, mul_zero]
    simp [Finset.sum_ite_eq, eq_comm]
    split_ifs <;> simp_all
  r3 a₀ a₂ b₀ b₂ c₀ c₂ := by
    simp only [idModel, ite_and, mul_ite, mul_one, mul_zero]
    simp [Finset.sum_ite_eq, eq_comm]
    split_ifs <;> simp_all

end Invariance

end QOU.MathlibExt.PL.Diagram
