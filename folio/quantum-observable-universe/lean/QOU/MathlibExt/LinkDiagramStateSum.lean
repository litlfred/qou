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

/-! ### Two internal edges -/

section Pair

variable {E : Type u} [Fintype E] [DecidableEq E]

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

end Pair

/-! ### The second Reidemeister move -/

section R2

variable {E : Type u} [Fintype E] [DecidableEq E] (M : Model R ι)

omit [Fintype ι] [DecidableEq ι] [Fintype E] [DecidableEq E] in
theorem occurs_ofJs_pair (a b c d e : E) :
    (Code.ofJs {(a, b), (c, d)}).Occurs e ↔ (a = e ∨ b = e) ∨ (c = e ∨ d = e) := by
  simp [Code.Occurs, Code.ofJs]

omit [Fintype ι] [DecidableEq ι] [Fintype E] [DecidableEq E] in
theorem occurs_ofXs_bigonPar (a b c d e₁ f₁ e : E) (s : Bool) :
    (Code.ofXs (bigonPar a b c d e₁ f₁ s)).Occurs e ↔
      c = e ∨ f₁ = e ∨ a = e ∨ e₁ = e ∨ d = e ∨ b = e := by
  simp only [Code.Occurs, Code.ofXs, bigonPar, Crossing.Mentions]
  simp
  tauto

/-- **Second Reidemeister move, parallel strands.** If the crossing tensors of signs `s` and `!s`
compose to the identity in the sense of `hX`, the value is unchanged by `r2par`. -/
theorem value_r2par (R₀ : Code E) (a b c d e₁ f₁ : E) (s : Bool)
    (he : ¬ R₀.Occurs e₁) (hf : ¬ R₀.Occurs f₁) (hef : e₁ ≠ f₁)
    (hbd : ∀ x ∈ ({a, b, c, d} : Set E), x ≠ e₁ ∧ x ≠ f₁)
    (hX : ∀ a b c d : ι, ∑ i, ∑ j, M.X s c j a i * M.X (!s) j d i b =
      if a = b ∧ c = d then 1 else 0) :
    value M (R₀ + Code.ofJs {(a, b), (c, d)}) =
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
    rw [sum_glue_pair e₁ f₁ hef M.base, sum_glue_pair e₁ f₁ hef M.base]
    set L₀ := glue {e₁, f₁} (fun _ => M.base) v with hL₀
    have hL₀e : L₀ e₁ = M.base := by
      simp [hL₀, glue, Equiv.piEquivPiSubtypeProd_symm_apply]
    have hL₀f : L₀ f₁ = M.base := by
      simp [hL₀, glue, Equiv.piEquivPiSubtypeProd_symm_apply]
    have hnot : e₁ ∉ ({f₁} : Finset E) := by simpa using hef
    -- left side: only the base labels on `e₁, f₁` survive
    have hlhs : ∀ i j, loc M {e₁, f₁} (Code.ofJs {(a, b), (c, d)})
        (Function.update (Function.update L₀ e₁ i) f₁ j) =
        if i = M.base then if j = M.base then
          (if L₀ a = L₀ b then 1 else 0) * (if L₀ c = L₀ d then 1 else 0) else 0 else 0 := by
      intro i j
      have hn1 : ¬ (Code.ofJs {(a, b), (c, d)} : Code E).Occurs e₁ := by
        rw [occurs_ofJs_pair]; tauto
      have hn2 : ¬ (Code.ofJs {(a, b), (c, d)} : Code E).Occurs f₁ := by
        rw [occurs_ofJs_pair]; tauto
      simp only [loc]
      rw [Finset.prod_insert hnot, Finset.prod_singleton]
      simp only [uf, if_neg hn1, if_neg hn2]
      have h1 : Function.update (Function.update L₀ e₁ i) f₁ j e₁ = i := by
        simp [hef]
      have h2 : Function.update (Function.update L₀ e₁ i) f₁ j f₁ = j := by simp
      have hx : ∀ x, x ≠ e₁ → x ≠ f₁ → Function.update (Function.update L₀ e₁ i) f₁ j x = L₀ x :=
        fun x h1 h2 => by simp [h1, h2]
      rw [h1, h2]
      simp only [xw, jw, Code.ofJs, Multiset.map_zero, Multiset.prod_zero, one_mul,
        Multiset.insert_eq_cons, Multiset.map_cons, Multiset.map_singleton, Multiset.prod_cons,
        Multiset.prod_singleton, hx a hae haf, hx b hbe hbf, hx c hce hcf, hx d hde hdf]
      by_cases hi : i = M.base <;> by_cases hj : j = M.base <;> simp [hi, hj]
    have hrhs : ∀ i j, loc M {e₁, f₁} (Code.ofXs (bigonPar a b c d e₁ f₁ s))
        (Function.update (Function.update L₀ e₁ i) f₁ j) =
        M.X s (L₀ c) j (L₀ a) i * M.X (!s) j (L₀ d) i (L₀ b) := by
      intro i j
      have ho1 : (Code.ofXs (bigonPar a b c d e₁ f₁ s)).Occurs e₁ := by
        rw [occurs_ofXs_bigonPar]; tauto
      have ho2 : (Code.ofXs (bigonPar a b c d e₁ f₁ s)).Occurs f₁ := by
        rw [occurs_ofXs_bigonPar]; tauto
      simp only [loc]
      rw [Finset.prod_insert hnot, Finset.prod_singleton]
      simp only [uf, if_pos ho1, if_pos ho2, mul_one]
      have h1 : Function.update (Function.update L₀ e₁ i) f₁ j e₁ = i := by
        simp [hef]
      have h2 : Function.update (Function.update L₀ e₁ i) f₁ j f₁ = j := by simp
      have hx : ∀ x, x ≠ e₁ → x ≠ f₁ → Function.update (Function.update L₀ e₁ i) f₁ j x = L₀ x :=
        fun x h1 h2 => by simp [h1, h2]
      simp only [xw, jw, Code.ofXs, bigonPar, Multiset.map_zero, Multiset.prod_zero, mul_one,
        Multiset.insert_eq_cons, Multiset.map_cons, Multiset.map_singleton, Multiset.prod_cons,
        Multiset.prod_singleton, h1, h2, hx a hae haf, hx b hbe hbf, hx c hce hcf, hx d hde hdf]
    simp only [hlhs, hrhs]
    rw [hX]
    rw [Fintype.sum_eq_single M.base fun x hx => by simp [hx],
      Fintype.sum_eq_single M.base fun x hx => by simp [hx]]
    by_cases hab : L₀ a = L₀ b <;> by_cases hcd : L₀ c = L₀ d <;> simp [hab, hcd]

end R2

end QOU.MathlibExt.PL.Diagram
