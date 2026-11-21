import QOU.MathlibExt.CechGenus4Space

/-!
# `H²` of the open-star cover of the genus-4 surface (route R3, step S2b)

Let `U4` be the open-star cover of the realised genus-4 surface `Surf`
(`CechGenus4Space`), and `G` a discrete commutative topological group. A
2-cochain is a function on ordered triples of vertices (`nval`,
`CechNerveValues`), and its degree `degS` is the combinatorial degree of
`CechGenus4Degree`.

## Results, all sorry-free

* `rel_of_degS_eq`, `degH2_injective`: equal degrees force cohomologous cocycles.
* `degS_ofNval`, `degH2_surjective`: every `g : G` is a degree.
* `h2Equiv`: hence `H²(U4, G) ≃ G`.
* `degH2_eq_one_iff`: the degree detects the trivial class.
* `deg_map`: the combinatorial degree commutes with additive maps of
  coefficients (naturality on the cover is left for step S4).

## What this does NOT do

This is `H²` of ONE cover. It does not compare with the colimit `Ȟ²` over all
open covers (steps S3–S4), and it does not identify `Surf` with Bring's curve.
Bean `qou-skn4`.

-- Ref: [manuscript] lifting-and-descent, route R3, surface step S2
-/
open CategoryTheory Opposite TopologicalSpace

namespace QOU.CentralExtension.Cech.Genus4

open CechGerbe
open NerveNormalize (IsCocycle V2 V1 w1 w2)

local notation "NC" => NerveNormalize.cob

theorem U4_inter4 (i j k l : Fin 19) :
    ((U4 i ⊓ U4 j ⊓ U4 k ⊓ U4 l : Opens Surf) : Set Surf) =
      {x : Surf | ∀ v ∈ ({i, j, k, l} : Finset (Fin 19)), 0 < x.1 v} := by
  ext x; simp [U4, star, and_assoc]

/-- Four stars meet iff the four vertices lie in one face. -/
theorem star4_nonempty_iff (i j k l : Fin 19) :
    ((U4 i ⊓ U4 j ⊓ U4 k ⊓ U4 l : Opens Surf) : Set Surf).Nonempty ↔ Q4 {i, j, k, l} := by
  show _ ↔ ∃ f, ({i, j, k, l} : Finset (Fin 19)) ⊆ face4 f
  rw [U4_inter4, ← inter_nonempty_iff face4 (by simp : ({i, j, k, l} : Finset (Fin 19)).Nonempty),
    ← star_set_eq, Set.image_nonempty]

/-! ### Linear algebra of the degree -/

section Lin

variable {A B : Type} [AddCommGroup A] [AddCommGroup B]

theorem deg_sub (V V' : Fin 19 → Fin 19 → Fin 19 → A) :
    deg (fun i j k => V i j k - V' i j k) = deg V - deg V' := by
  have h := deg_add (fun i j k => V i j k - V' i j k) V'
  simp only [sub_add_cancel] at h
  exact eq_sub_of_add_eq h.symm

theorem V2_map (φ : A →+ B) (V : Fin 19 → Fin 19 → Fin 19 → A) (a b c : Fin 19) :
    V2 (fun i j k => φ (V i j k)) a b c = φ (V2 V a b c) := by
  simp only [V2, V1, w1, w2, NerveNormalize.cob]
  split_ifs <;> simp [map_add, map_sub]

theorem deg_map (φ : A →+ B) (V : Fin 19 → Fin 19 → Fin 19 → A) :
    deg (fun i j k => φ (V i j k)) = φ (deg V) := by
  simp only [deg, V2_map, map_sum]

end Lin

/-! ### The degree of a cochain on the star cover -/

variable {G : Type} [TopologicalSpace G] [CommGroup G] [IsTopologicalGroup G]
  [DiscreteTopology G]

/-- Values of a 2-cochain, written additively. -/
noncomputable def vals (c : TwoCochain U4 (contPresheaf Surf G)) (i j k : Fin 19) :
    Additive G :=
  Additive.ofMul (nval c i j k)

theorem vals_cocycle (c : TwoCocycle U4 (contPresheaf Surf G)) :
    IsCocycle Q4 (vals c.toTwoCochain) := fun i j k l hq => by
  have e := congrArg Additive.ofMul
    (nval_cocycle connFamily_star c i j k l ((star4_nonempty_iff i j k l).mpr hq))
  simpa only [vals, ofMul_mul] using e

/-- **The degree** of a 2-cochain of the star cover. -/
noncomputable def degS (c : TwoCochain U4 (contPresheaf Surf G)) : G :=
  Additive.toMul (deg (vals c))

theorem degS_rel {c₁ c₂ : TwoCocycle U4 (contPresheaf Surf G)} (h : TwoCocycle.Rel c₁ c₂) :
    degS c₂.toTwoCochain = degS c₁.toTwoCochain := by
  obtain ⟨w, hw⟩ := (rel_iff_nval connFamily_star c₁ c₂).mp h
  unfold degS
  congr 1
  refine deg_eq_of_rel (fun i j => Additive.ofMul (w i j)) fun a b c hq => ?_
  have e := congrArg Additive.ofMul (hw a b c ((star3_nonempty_iff a b c).mpr hq))
  simp only [ofMul_mul, ofMul_inv] at e
  simp only [vals, NerveNormalize.cob, e, sub_eq_add_neg]

/-- **Equal degrees force cohomologous cocycles.** -/
theorem rel_of_degS_eq (c₁ c₂ : TwoCocycle U4 (contPresheaf Surf G))
    (hd : degS c₁.toTwoCochain = degS c₂.toTwoCochain) : TwoCocycle.Rel c₁ c₂ := by
  rw [rel_iff_nval connFamily_star]
  set V : Fin 19 → Fin 19 → Fin 19 → Additive G := fun i j k =>
    vals c₂.toTwoCochain i j k - vals c₁.toTwoCochain i j k
  have hV : IsCocycle Q4 V := fun i j k l hq => by
    have e₁ := vals_cocycle c₁ i j k l hq
    have e₂ := vals_cocycle c₂ i j k l hq
    simp only [V]; linear_combination (norm := abel) e₂ - e₁
  have hd' : deg V = 0 := by
    simp only [V]; rw [deg_sub]
    have := congrArg Additive.ofMul hd
    simp only [degS, ofMul_toMul] at this
    rw [this, sub_self]
  obtain ⟨w, hw⟩ := exists_cob_of_deg_eq_zero hV hd'
  refine ⟨fun i j => Additive.toMul (w i j), fun i j k hne => ?_⟩
  have e := hw i j k ((star3_nonempty_iff i j k).mp hne)
  apply Additive.ofMul.injective
  simp only [ofMul_mul, ofMul_inv, ofMul_toMul]
  simp only [V, vals, NerveNormalize.cob] at e
  linear_combination (norm := abel) e

/-- The degree on `H²` of the star cover. -/
noncomputable def degH2 : H2 U4 (contPresheaf Surf G) → G :=
  Quot.lift (fun c => degS c.toTwoCochain) (fun _ _ h => (degS_rel h).symm)

theorem degH2_injective : Function.Injective (degH2 (G := G)) := by
  intro x y h
  induction x using Quot.ind with
  | mk c₁ =>
    induction y using Quot.ind with
    | mk c₂ => exact Quot.sound (rel_of_degS_eq c₁ c₂ h)

/-- The cocycle realising degree `g`. -/
noncomputable def gCocycle (g : G) : TwoCocycle U4 (contPresheaf Surf G) :=
  ofNval (fun i j k => Additive.toMul (Vg (Additive.ofMul g) i j k)) fun i j k l hne => by
    have e := Vg_cocycle (Additive.ofMul g) i j k l ((star4_nonempty_iff i j k l).mp hne)
    apply Additive.ofMul.injective
    simpa only [ofMul_mul, ofMul_toMul] using e

omit [DiscreteTopology G] in
theorem degS_gCocycle (g : G) : degS (gCocycle g).toTwoCochain = g := by
  unfold degS
  rw [deg_congr (V' := Vg (Additive.ofMul g)) fun a b c hq => by
    simp only [vals, gCocycle]
    rw [nval_ofNval _ _ a b c ((star3_nonempty_iff a b c).mpr hq), ofMul_toMul]]
  rw [deg_Vg, toMul_ofMul]

theorem degH2_surjective : Function.Surjective (degH2 (G := G)) :=
  fun g => ⟨Quot.mk _ (gCocycle g), degS_gCocycle g⟩

/-- **`H²` of the star cover is `G`.** -/
noncomputable def h2Equiv : H2 U4 (contPresheaf Surf G) ≃ G :=
  Equiv.ofBijective degH2 ⟨degH2_injective, degH2_surjective⟩

omit [DiscreteTopology G] in
theorem degS_one : degS (TwoCocycle.one : TwoCocycle U4 (contPresheaf Surf G)).toTwoCochain = 1 := by
  have h0 : vals (TwoCocycle.one : TwoCocycle U4 (contPresheaf Surf G)).toTwoCochain =
      fun _ _ _ => 0 := by
    funext i j k
    simp only [vals]
    unfold nval; split_ifs <;> rfl
  rw [degS, h0]
  have : deg (fun _ _ _ => (0 : Additive G)) = 0 := by simp [deg, V2_zero]
  rw [this]; rfl

/-- **The degree detects the trivial class.** -/
theorem degH2_eq_one_iff (c : TwoCocycle U4 (contPresheaf Surf G)) :
    degS c.toTwoCochain = 1 ↔ TwoCocycle.Rel TwoCocycle.one c := by
  constructor
  · intro h; exact rel_of_degS_eq _ _ (by rw [degS_one, h])
  · intro h; rw [degS_rel h, degS_one]

end QOU.CentralExtension.Cech.Genus4
