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

/-- **Replacing two joins by a two-crossing piece.** Let `xs` be crossings mentioning exactly the
edges `a, b, c, d, e₁, f₁`, with weight `G` of their labels. If summing `G` over the labels of the
internal edges `e₁, f₁` gives `1` when `a, b` and `c, d` carry equal labels and `0` otherwise, then
replacing the joins `(a, b), (c, d)` by `xs` does not change the value. -/
theorem value_pair_of (R₀ : Code E) (xs : Multiset (Crossing E)) (a b c d e₁ f₁ : E)
    (G : ι → ι → ι → ι → ι → ι → R)
    (he : ¬ R₀.Occurs e₁) (hf : ¬ R₀.Occurs f₁) (hef : e₁ ≠ f₁)
    (hbd : ∀ x ∈ ({a, b, c, d} : Set E), x ≠ e₁ ∧ x ≠ f₁)
    (hocc : ∀ e, (Code.ofXs xs).Occurs e ↔
      ((a = e ∨ b = e) ∨ (c = e ∨ d = e)) ∨ (e₁ = e ∨ f₁ = e))
    (hxw : ∀ L : E → ι, xw M xs L = G (L a) (L b) (L c) (L d) (L e₁) (L f₁))
    (hG : ∀ a b c d : ι, ∑ i, ∑ j, G a b c d i j = if a = b ∧ c = d then 1 else 0) :
    value M (R₀ + Code.ofJs {(a, b), (c, d)}) = value M (R₀ + Code.ofXs xs) := by
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
    rw [occurs_ofJs_pair, hocc]
    have h1 : e₁ ≠ e := Ne.symm heT.1
    have h2 : f₁ ≠ e := Ne.symm heT.2
    tauto
  · intro v
    rw [sum_glue_pair e₁ f₁ hef M.base, sum_glue_pair e₁ f₁ hef M.base]
    set L₀ := glue {e₁, f₁} (fun _ => M.base) v
    have hnot : e₁ ∉ ({f₁} : Finset E) := by simpa using hef
    have hupd : ∀ i j,
        (Function.update (Function.update L₀ e₁ i) f₁ j e₁ = i ∧
          Function.update (Function.update L₀ e₁ i) f₁ j f₁ = j) ∧
        ∀ x, x ≠ e₁ → x ≠ f₁ → Function.update (Function.update L₀ e₁ i) f₁ j x = L₀ x :=
      fun i j => ⟨⟨by simp [hef], by simp⟩, fun x h1 h2 => by simp [h1, h2]⟩
    have hlhs : ∀ i j, loc M {e₁, f₁} (Code.ofJs {(a, b), (c, d)})
        (Function.update (Function.update L₀ e₁ i) f₁ j) =
        if i = M.base then if j = M.base then
          (if L₀ a = L₀ b then 1 else 0) * (if L₀ c = L₀ d then 1 else 0) else 0 else 0 := by
      intro i j
      have hn1 : ¬ (Code.ofJs {(a, b), (c, d)} : Code E).Occurs e₁ := by
        rw [occurs_ofJs_pair]; tauto
      have hn2 : ¬ (Code.ofJs {(a, b), (c, d)} : Code E).Occurs f₁ := by
        rw [occurs_ofJs_pair]; tauto
      obtain ⟨⟨h1, h2⟩, hx⟩ := hupd i j
      simp only [loc]
      rw [Finset.prod_insert hnot, Finset.prod_singleton]
      simp only [uf, if_neg hn1, if_neg hn2]
      rw [h1, h2]
      simp only [xw, jw, Code.ofJs, Multiset.map_zero, Multiset.prod_zero, one_mul,
        Multiset.insert_eq_cons, Multiset.map_cons, Multiset.map_singleton, Multiset.prod_cons,
        Multiset.prod_singleton, hx a hae haf, hx b hbe hbf, hx c hce hcf, hx d hde hdf]
      by_cases hi : i = M.base <;> by_cases hj : j = M.base <;> simp [hi, hj]
    have hrhs : ∀ i j, loc M {e₁, f₁} (Code.ofXs xs)
        (Function.update (Function.update L₀ e₁ i) f₁ j) =
        G (L₀ a) (L₀ b) (L₀ c) (L₀ d) i j := by
      intro i j
      have ho1 : (Code.ofXs xs).Occurs e₁ := by rw [hocc]; tauto
      have ho2 : (Code.ofXs xs).Occurs f₁ := by rw [hocc]; tauto
      obtain ⟨⟨h1, h2⟩, hx⟩ := hupd i j
      simp only [loc]
      rw [Finset.prod_insert hnot, Finset.prod_singleton]
      simp only [uf, if_pos ho1, if_pos ho2, mul_one]
      have hxs : (Code.ofXs xs).xs = xs := rfl
      rw [hxs, hxw, h1, h2, hx a hae haf, hx b hbe hbf, hx c hce hcf, hx d hde hdf]
      simp [jw, Code.ofXs]
    simp only [hlhs, hrhs]
    rw [hG]
    rw [Fintype.sum_eq_single M.base fun x hx => by simp [hx],
      Fintype.sum_eq_single M.base fun x hx => by simp [hx]]
    by_cases hab : L₀ a = L₀ b <;> by_cases hcd : L₀ c = L₀ d <;> simp [hab, hcd]

omit [Fintype ι] [DecidableEq ι] [Fintype E] [DecidableEq E] in
theorem occurs_ofXs_bigonAnti (a b c d e₁ f₁ e : E) (s : Bool) :
    (Code.ofXs (bigonAnti a b c d e₁ f₁ s)).Occurs e ↔
      f₁ = e ∨ d = e ∨ a = e ∨ e₁ = e ∨ c = e ∨ b = e := by
  simp only [Code.Occurs, Code.ofXs, bigonAnti, Crossing.Mentions]
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
      value M (R₀ + Code.ofXs (bigonPar a b c d e₁ f₁ s)) :=
  value_pair_of M R₀ _ a b c d e₁ f₁ (fun a b c d i j => M.X s c j a i * M.X (!s) j d i b)
    he hf hef hbd (fun e => by rw [occurs_ofXs_bigonPar]; tauto)
    (fun L => by simp [xw, bigonPar]) hX

/-- **Second Reidemeister move, antiparallel strands.** If the crossing tensors of signs `s` and
`!s` satisfy the antiparallel identity `hX`, the value is unchanged by `r2anti`. -/
theorem value_r2anti (R₀ : Code E) (a b c d e₁ f₁ : E) (s : Bool)
    (he : ¬ R₀.Occurs e₁) (hf : ¬ R₀.Occurs f₁) (hef : e₁ ≠ f₁)
    (hbd : ∀ x ∈ ({a, b, c, d} : Set E), x ≠ e₁ ∧ x ≠ f₁)
    (hX : ∀ a b c d : ι, ∑ i, ∑ j, M.X s j d a i * M.X (!s) c j i b =
      if a = b ∧ c = d then 1 else 0) :
    value M (R₀ + Code.ofJs {(a, b), (c, d)}) =
      value M (R₀ + Code.ofXs (bigonAnti a b c d e₁ f₁ s)) :=
  value_pair_of M R₀ _ a b c d e₁ f₁ (fun a b c d i j => M.X s j d a i * M.X (!s) c j i b)
    he hf hef hbd (fun e => by rw [occurs_ofXs_bigonAnti]; tauto)
    (fun L => by simp [xw, bigonAnti]) hX

end R2

/-! ### The first Reidemeister move -/

section R1

variable {E : Type u} [Fintype E] [DecidableEq E] (M : Model R ι)

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

/-- The weight of a kink with incoming label `x`, outgoing label `y`, and label `i` on the loop. -/
def kinkW (u s : Bool) (x y i : ι) : R :=
  if u then M.X s x i i y else M.X s i y x i

omit [Fintype ι] [DecidableEq ι] [Fintype E] [DecidableEq E] in
theorem occurs_ofXs_kink (a b ℓ e : E) (u s : Bool) :
    (Code.ofXs {kink a b ℓ u s}).Occurs e ↔ (a = e ∨ b = e) ∨ ℓ = e := by
  cases u <;> simp [Code.Occurs, Code.ofXs, kink, Crossing.Mentions] <;> tauto

omit [Fintype ι] [DecidableEq ι] [Fintype E] [DecidableEq E] in
theorem occurs_ofJs_single (a b e : E) :
    (Code.ofJs {(a, b)}).Occurs e ↔ a = e ∨ b = e := by
  simp [Code.Occurs, Code.ofJs]

/-- **First Reidemeister move, up to a factor.** If closing a strand through a kink of type
`(u, s)` multiplies the identity by `κ`, then adding the kink multiplies the value by `κ`. -/
theorem value_r1 (R₀ : Code E) (a b ℓ : E) (u s : Bool) (κ : R)
    (hℓ : ¬ R₀.Occurs ℓ) (ha : ℓ ≠ a) (hb : ℓ ≠ b)
    (hK : ∀ x y : ι, ∑ i, kinkW M u s x y i = κ * if x = y then 1 else 0) :
    value M (R₀ + Code.ofXs {kink a b ℓ u s}) = κ * value M (R₀ + Code.ofJs {(a, b)}) := by
  classical
  refine value_local_smul M R₀ _ _ {ℓ} κ ?_ ?_ ?_
  · intro e he
    simp only [Finset.mem_singleton] at he
    subst he; exact hℓ
  · intro e he
    simp only [Finset.mem_singleton] at he
    rw [occurs_ofJs_single, occurs_ofXs_kink]
    have : ℓ ≠ e := Ne.symm he
    tauto
  · intro v
    rw [sum_glue_single ℓ M.base, sum_glue_single ℓ M.base]
    set L₀ := glue {ℓ} (fun _ => M.base) v
    have hupd : ∀ i, Function.update L₀ ℓ i ℓ = i ∧
        ∀ x, x ≠ ℓ → Function.update L₀ ℓ i x = L₀ x :=
      fun i => ⟨by simp, fun x h => by simp [h]⟩
    have hrhs : ∀ i, loc M {ℓ} (Code.ofJs {(a, b)}) (Function.update L₀ ℓ i) =
        if i = M.base then (if L₀ a = L₀ b then 1 else 0) else 0 := by
      intro i
      have hn : ¬ (Code.ofJs {(a, b)} : Code E).Occurs ℓ := by
        rw [occurs_ofJs_single]; tauto
      obtain ⟨h1, hx⟩ := hupd i
      simp only [loc, Finset.prod_singleton, uf, if_neg hn, h1]
      simp only [xw, jw, Code.ofJs, Multiset.map_zero, Multiset.prod_zero, one_mul,
        Multiset.map_singleton, Multiset.prod_singleton, hx a (Ne.symm ha), hx b (Ne.symm hb)]
      by_cases hi : i = M.base <;> simp [hi]
    have hlhs : ∀ i, loc M {ℓ} (Code.ofXs {kink a b ℓ u s}) (Function.update L₀ ℓ i) =
        kinkW M u s (L₀ a) (L₀ b) i := by
      intro i
      have ho : (Code.ofXs {kink a b ℓ u s} : Code E).Occurs ℓ := by
        rw [occurs_ofXs_kink]; tauto
      obtain ⟨h1, hx⟩ := hupd i
      simp only [loc, Finset.prod_singleton, uf, if_pos ho, mul_one]
      cases u <;>
        simp [xw, jw, Code.ofXs, kink, kinkW, hx a (Ne.symm ha), hx b (Ne.symm hb)]
    simp only [hlhs, hrhs]
    rw [hK, Fintype.sum_eq_single M.base fun x hx => by simp [hx]]
    simp

end R1

/-! ### The third Reidemeister move -/

section R3

variable {E : Type u} [Fintype E] [DecidableEq E] (M : Model R ι)

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
        loc M {a₁, b₁, c₁} S L = xw M S.xs L * jw S.js L := by
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

end R3

/-! ### Relabelling and contraction -/

section Relabel

variable {E F : Type u} (M : Model R ι)

omit [Fintype ι] [DecidableEq ι] in
theorem xw_map (f : E → F) (xs : Multiset (Crossing E)) (L : F → ι) :
    xw M (xs.map (Crossing.map f)) L = xw M xs (L ∘ f) := by
  simp [xw, Multiset.map_map, Crossing.map]

omit [Fintype ι] in
theorem jw_map (f : E → F) (js : Multiset (E × E)) (L : F → ι) :
    jw (R := R) (js.map (Prod.map f f)) L = jw js (L ∘ f) := by
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
      show (D.map f).js = D.js.map (Prod.map f f) from rfl, xw_map, jw_map]
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
    value M (R₀.map (Function.update id b a)) = value M (R₀ + Code.ofJs {(a, b)}) := by
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
  have hJ : ∀ y, (Code.ofJs {(a, b)} : Code E).Occurs y ↔ a = y ∨ b = y :=
    occurs_ofJs_single a b
  have hcomp : ∀ L : E → ι, L b = M.base →
      Function.update L b (L a) = L ∘ f := fun L _ => by
    funext x; rw [Function.comp_apply, hfb]
    by_cases h : x = b
    · subst h; simp
    · simp [h]
  unfold value
  rw [sum_split b M.base (weight M (R₀ + Code.ofJs {(a, b)}))]
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
      show (R₀.map f).js = R₀.js.map (Prod.map f f) from rfl, xw_map, jw_map]
    have hx0 : xw M (Code.ofJs {(a, b)} : Code E).xs (L ∘ f) = 1 := by simp [xw, Code.ofJs]
    have hj0 : jw (R := R) (Code.ofJs {(a, b)} : Code E).js (L ∘ f) = 1 := by
      simp [jw, Code.ofJs, hfb, hab]
    rw [hx0, hj0, mul_one, mul_one]
    congr 1
    refine Finset.prod_congr rfl fun e _ => ?_
    by_cases heb : e = b
    · subst heb
      have h1 : (R₀ + Code.ofJs {(a, e)}).Occurs e := by rw [occurs_add, hJ]; tauto
      have h2 : ¬ (R₀.map f).Occurs e := by rw [hocc]; tauto
      simp only [uf, h1, h2, hLb, if_true, if_false]
    · by_cases hea : e = a
      · subst hea
        have h1 : (R₀ + Code.ofJs {(e, b)}).Occurs e := by rw [occurs_add, hJ]; tauto
        have h2 : (R₀.map f).Occurs e := by rw [hocc]; tauto
        simp only [uf, h1, h2, if_true]
      · have h12 : (R₀ + Code.ofJs {(a, b)}).Occurs e ↔ (R₀.map f).Occurs e := by
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
    have : jw (R := R) (Code.ofJs {(a, b)} : Code E).js (Function.update L b i) = 0 := by
      simp [jw, Code.ofJs, hab, Function.update_apply, Ne.symm hi]
    rw [this]; ring

end Relabel

end QOU.MathlibExt.PL.Diagram
