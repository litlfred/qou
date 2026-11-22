import QOU.MathlibExt.CechNerveTetrahedron

/-!
# Čech 2-cochains on a cover with connected intersections are nerve values

Step P1 of the C2 comparison (route R3, surface case). Let `U : ι → Opens X` be
any family whose pairwise and triple intersections are preconnected
(`ConnFamily U`; empty intersections are allowed), and let `G` be a discrete
commutative topological group. A continuous `G`-valued function on a
preconnected set is constant, so a 2-cochain of `contPresheaf X G` on `U` is
determined by one value per index triple with nonempty intersection. This file
makes that precise for an arbitrary index type, generalizing the four-set
layer of `CechNerveTetrahedron`.

## Results, all sorry-free

* `nval`, `nval1`: the value of a 2-cochain on a triple and of a 1-cochain on a
  pair (defined to be `1` on empty intersections).
* `nev_apply`, `nev1_apply`: every component evaluates to that value.
* `nval_cocycle`: the cocycle identity on the values of every quadruple with
  nonempty intersection.
* `rel_iff_nval`: two cocycles are cohomologous exactly when their values
  differ by `w_ij w_jk w_ik⁻¹` on every nonempty triple, for some function
  `w : ι → ι → G`.
* `ofNval`, `nval_ofNval`: conversely, any function on triples satisfying the
  cocycle identity on nonempty quadruples is the value function of a cocycle.
* `nval_pull`: values pull back along a refinement by reindexing.

## What this does NOT do

It is the bookkeeping layer only. It does not compare `H²` of two covers; that
is the split lemma (step P2). The colimit statement `HemiComputesCech` is
proved in `CechSphereGood`.

-- Ref: [manuscript] lifting-and-descent, route R3, surface step C2
-/
open CategoryTheory Opposite TopologicalSpace
namespace QOU.CentralExtension.Cech
open CechGerbe

variable {X : Type} [TopologicalSpace X] {G : Type} [TopologicalSpace G] [CommGroup G]
  [IsTopologicalGroup G] [DiscreteTopology G]

/-- An open family whose pairwise and triple intersections are preconnected. -/
structure ConnFamily {ι : Type} (U : ι → Opens X) : Prop where
  pre3 : ∀ i j k, IsPreconnected ((U i ⊓ U j ⊓ U k : Opens X) : Set X)
  pre2 : ∀ i j, IsPreconnected ((U i ⊓ U j : Opens X) : Set X)

variable {ι : Type} {U : ι → Opens X}

open Classical in
/-- Value of a 2-cochain on the triple `(i,j,k)`; `1` if the triple
intersection is empty. -/
noncomputable def nval (c : TwoCochain U (contPresheaf X G)) (i j k : ι) : G :=
  if h : ((U i ⊓ U j ⊓ U k : Opens X) : Set X).Nonempty then
    sec (c.ev i j k (homOfLE (inf_le_left.trans inf_le_left) :
      (U i ⊓ U j ⊓ U k : Opens X) ⟶ U i)
      (homOfLE (inf_le_left.trans inf_le_right)) (homOfLE inf_le_right))
      ⟨h.some, h.some_mem⟩
  else 1

theorem nev_apply (hU : ConnFamily U) (c : TwoCochain U (contPresheaf X G)) (i j k : ι)
    {T : Opens X} (a : T ⟶ U i) (b : T ⟶ U j) (d : T ⟶ U k) (x : T) :
    sec (c.ev i j k a b d) x = nval c i j k := by
  have hT : T ≤ U i ⊓ U j ⊓ U k := le_inf (le_inf (leOfHom a) (leOfHom b)) (leOfHom d)
  have hne : ((U i ⊓ U j ⊓ U k : Opens X) : Set X).Nonempty := ⟨x.1, hT x.2⟩
  have e := c.ev_precomp i j k (homOfLE hT)
    (homOfLE (inf_le_left.trans inf_le_left) : (U i ⊓ U j ⊓ U k : Opens X) ⟶ U i)
    (homOfLE (inf_le_left.trans inf_le_right)) (homOfLE inf_le_right)
  rw [Subsingleton.elim (homOfLE hT ≫ _) a, Subsingleton.elim (homOfLE hT ≫ _) b,
    Subsingleton.elim (homOfLE hT ≫ _) d] at e
  rw [← e, nval, dif_pos hne]
  exact sec_const_of_preconnected (hU.pre3 i j k) _ _ _

open Classical in
/-- Value of a 1-cochain on the pair `(i,j)`; `1` if `U i ⊓ U j` is empty. -/
noncomputable def nval1 (α : PresheafOfGroups.OneCochain (contPresheaf X G) U) (i j : ι) : G :=
  if h : ((U i ⊓ U j : Opens X) : Set X).Nonempty then
    sec (α.ev i j (homOfLE inf_le_left : (U i ⊓ U j : Opens X) ⟶ U i) (homOfLE inf_le_right))
      ⟨h.some, h.some_mem⟩
  else 1

theorem nev1_apply (hU : ConnFamily U) (α : PresheafOfGroups.OneCochain (contPresheaf X G) U)
    (i j : ι) {T : Opens X} (a : T ⟶ U i) (b : T ⟶ U j) (x : T) :
    sec (α.ev i j a b) x = nval1 α i j := by
  have hT : T ≤ U i ⊓ U j := le_inf (leOfHom a) (leOfHom b)
  have hne : ((U i ⊓ U j : Opens X) : Set X).Nonempty := ⟨x.1, hT x.2⟩
  have e := α.ev_precomp i j (homOfLE hT)
    (homOfLE inf_le_left : (U i ⊓ U j : Opens X) ⟶ U i) (homOfLE inf_le_right)
  rw [Subsingleton.elim (homOfLE hT ≫ _) a, Subsingleton.elim (homOfLE hT ≫ _) b] at e
  rw [← e, nval1, dif_pos hne]
  exact sec_const_of_preconnected (hU.pre2 i j) _ _ _

/-- The cocycle identity on values, on every quadruple with nonempty
intersection. -/
theorem nval_cocycle (hU : ConnFamily U) (c : TwoCocycle U (contPresheaf X G)) (i j k l : ι)
    (h : ((U i ⊓ U j ⊓ U k ⊓ U l : Opens X) : Set X).Nonempty) :
    nval c.toTwoCochain i j k * nval c.toTwoCochain i k l =
      nval c.toTwoCochain j k l * nval c.toTwoCochain i j l := by
  obtain ⟨x, hx⟩ := h
  set Q : Opens X := U i ⊓ U j ⊓ U k ⊓ U l
  have hi : Q ≤ U i := inf_le_left.trans (inf_le_left.trans inf_le_left)
  have hj : Q ≤ U j := inf_le_left.trans (inf_le_left.trans inf_le_right)
  have hk : Q ≤ U k := inf_le_left.trans inf_le_right
  have hl : Q ≤ U l := inf_le_right
  have e := congrArg (fun f : (contPresheaf X G).obj (op Q) => sec f ⟨x, hx⟩)
    (c.cocycle i j k l (homOfLE hi) (homOfLE hj) (homOfLE hk) (homOfLE hl))
  simp only at e
  have m : ∀ f g : (contPresheaf X G).obj (op Q), sec (f * g) ⟨x, hx⟩ =
      sec f ⟨x, hx⟩ * sec g ⟨x, hx⟩ := fun _ _ => rfl
  rwa [m, m, nev_apply hU, nev_apply hU, nev_apply hU, nev_apply hU] at e

/-- The constant 1-cochain with values `w i j`, on any index type. -/
def nconstOneCochain (w : ι → ι → G) : PresheafOfGroups.OneCochain (contPresheaf X G) U where
  ev i j T _ _ := (ContinuousMap.const T (w i j) : C(T, G))
  ev_precomp _ _ _ _ _ _ _ := rfl

/-- **Cohomology on values.** Two cocycles on a `ConnFamily` are cohomologous
exactly when their values differ by the coboundary of a function on pairs, on
every nonempty triple. -/
theorem rel_iff_nval (hU : ConnFamily U) (c₁ c₂ : TwoCocycle U (contPresheaf X G)) :
    TwoCocycle.Rel c₁ c₂ ↔ ∃ w : ι → ι → G, ∀ i j k,
      ((U i ⊓ U j ⊓ U k : Opens X) : Set X).Nonempty →
      nval c₂.toTwoCochain i j k = nval c₁.toTwoCochain i j k * (w i j * w j k * (w i k)⁻¹) := by
  constructor
  · rintro ⟨α, hα⟩
    refine ⟨nval1 α, fun i j k hne => ?_⟩
    set T : Opens X := U i ⊓ U j ⊓ U k
    have x : T := ⟨hne.some, hne.some_mem⟩
    have e := congrArg (fun f => sec f x) (hα i j k
      (homOfLE (inf_le_left.trans inf_le_left) : T ⟶ U i)
      (homOfLE (inf_le_left.trans inf_le_right)) (homOfLE inf_le_right))
    simp only at e
    have m : ∀ f g : (contPresheaf X G).obj (op T), sec (f * g) x = sec f x * sec g x :=
      fun _ _ => rfl
    have n : ∀ f : (contPresheaf X G).obj (op T), sec f⁻¹ x = (sec f x)⁻¹ := fun _ => rfl
    rwa [m, m, m, n, nev_apply hU, nev_apply hU, nev1_apply hU, nev1_apply hU,
      nev1_apply hU] at e
  · rintro ⟨w, hw⟩
    refine ⟨nconstOneCochain w, fun i j k T a b d => ContinuousMap.ext fun x => ?_⟩
    have hT : T ≤ U i ⊓ U j ⊓ U k := le_inf (le_inf (leOfHom a) (leOfHom b)) (leOfHom d)
    change sec (c₂.ev i j k a b d) x = sec (c₁.ev i j k a b d) x * (w i j * w j k * (w i k)⁻¹)
    rw [nev_apply hU, nev_apply hU]
    exact hw i j k ⟨x.1, hT x.2⟩

/-- The class of a cocycle on a `ConnFamily` is trivial exactly when its values
are a coboundary of a function on pairs. -/
theorem class_eq_one_iff_nval (hU : ConnFamily U) (c : TwoCocycle U (contPresheaf X G)) :
    c.class = 1 ↔ ∃ w : ι → ι → G, ∀ i j k,
      ((U i ⊓ U j ⊓ U k : Opens X) : Set X).Nonempty →
      nval c.toTwoCochain i j k = w i j * w j k * (w i k)⁻¹ := by
  have e : c.class = 1 ↔ TwoCocycle.Rel TwoCocycle.one c :=
    TwoCocycle.class_eq_iff (contPresheaf_comm (X := X)) _ _ |>.trans
      ⟨(TwoCocycle.equivalence_rel (contPresheaf_comm (X := X))).symm,
        (TwoCocycle.equivalence_rel (contPresheaf_comm (X := X))).symm⟩
  rw [e, rel_iff_nval hU]
  refine exists_congr fun w => forall_congr' fun i => forall_congr' fun j =>
    forall_congr' fun k => imp_congr_right fun hne => ?_
  have h1 : nval (TwoCocycle.one : TwoCocycle U (contPresheaf X G)).toTwoCochain i j k = 1 := by
    unfold nval; split_ifs; rfl
  rw [h1, one_mul]

/-- The cocycle with constant components `V i j k`, from a function on triples
satisfying the cocycle identity on every nonempty quadruple. -/
def ofNval (V : ι → ι → ι → G)
    (hV : ∀ i j k l, ((U i ⊓ U j ⊓ U k ⊓ U l : Opens X) : Set X).Nonempty →
      V i j k * V i k l = V j k l * V i j l) :
    TwoCocycle U (contPresheaf X G) where
  ev i j k T _ _ _ := (ContinuousMap.const T (V i j k) : C(T, G))
  ev_precomp _ _ _ _ _ _ _ _ _ := rfl
  cocycle i j k l T a b c d := ContinuousMap.ext fun x => by
    have hT : T ≤ U i ⊓ U j ⊓ U k ⊓ U l :=
      le_inf (le_inf (le_inf (leOfHom a) (leOfHom b)) (leOfHom c)) (leOfHom d)
    exact hV i j k l ⟨x.1, hT x.2⟩

omit [DiscreteTopology G] in
theorem nval_ofNval (V : ι → ι → ι → G)
    (hV : ∀ i j k l, ((U i ⊓ U j ⊓ U k ⊓ U l : Opens X) : Set X).Nonempty →
      V i j k * V i k l = V j k l * V i j l) (i j k : ι)
    (hne : ((U i ⊓ U j ⊓ U k : Opens X) : Set X).Nonempty) :
    nval (ofNval V hV).toTwoCochain i j k = V i j k := by
  rw [nval, dif_pos hne]; rfl

/-- **Values pull back by reindexing.** For a refinement `f : W j ⟶ U (r j)` of
`ConnFamily` families, the value of the pulled-back cocycle on a nonempty
triple of `W` is the value of the original cocycle on the image triple. -/
theorem nval_pull {κ : Type} {W : κ → Opens X} (hU : ConnFamily U) (r : κ → ι)
    (f : ∀ j, W j ⟶ U (r j)) (c : TwoCocycle U (contPresheaf X G)) (i j k : κ)
    (hne : ((W i ⊓ W j ⊓ W k : Opens X) : Set X).Nonempty) :
    nval (c.pull r f).toTwoCochain i j k = nval c.toTwoCochain (r i) (r j) (r k) := by
  rw [nval, dif_pos hne]
  change sec (c.ev (r i) (r j) (r k) _ _ _) _ = _
  exact nev_apply hU _ _ _ _ _ _ _ _

end QOU.CentralExtension.Cech
