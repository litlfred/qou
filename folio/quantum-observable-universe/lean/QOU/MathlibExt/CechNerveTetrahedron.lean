import QOU.MathlibExt.CechCofinalCover

/-!
# The degree of Čech `H²` on a four-set cover (nerve of the tetrahedron boundary)

Surface case of route R3 (C-5a), step C1a. Let `U : Fin 4 → Opens X` be a family
in which every intersection of at most three members is nonempty and
preconnected (`TetCover U`), and let `G` be a discrete commutative topological
group. Continuous `G`-valued functions on a preconnected set are constant, so a
2-cochain of the cover is a function on ordered triples of `Fin 4`.

## Results, all sorry-free

* `deg`: `c ↦ c₁₂₃ · c₀₂₃⁻¹ · c₀₁₃ · c₀₁₂⁻¹`, the alternating sum over the four
  faces.
* `deg_rel`: cohomologous cocycles have the same degree.
* `exists_coboundary_of_deg_eq_one`: a cocycle of degree `1` is the coboundary of
  the constant 1-cochain `w_ij = c₀ᵢⱼ`.
* `degH2_eq_one_iff`: hence `deg` detects the trivial class of `H²(U, G)`.
* `deg_map`: `deg` is natural in the coefficient group.
* `rel_of_deg_eq`, `degH2_injective`: equal degrees force cohomologous
  cocycles.
* `faceCocycle`, `degH2_surjective`: if no point lies in all four sets, the
  cocycle with value `g` on the oriented face `(1,2,3)` has degree `g`.
* `h2EquivOfEmptyQuad`, `cechH2EquivOfEmptyQuad`: hence `H²(U, G) ≃ G`, and the
  same for the cover-level Čech `H²`.
* `kummerSurfaceData_tet`: a `KummerSurfaceData` instance for the admissibility
  predicate `(· = tetCover U)`.

## What this does NOT do

The instance is **cover-level only**. Its colimit is over the single cover
`tetCover U`, not over all open covers, so it is not a statement about `Ȟ²` of
`X`. Comparing with the full colimit (Leray / survival, step C2) is open, as is
the concrete cover of the 2-sphere (step C1b). Bean `qou-skn4`.

-- Ref: [manuscript] lifting-and-descent, route R3, surface step C1
-/
open CategoryTheory Opposite TopologicalSpace
namespace QOU.CentralExtension.Cech
open CechGerbe

variable {X : Type} [TopologicalSpace X] {G : Type} [TopologicalSpace G] [CommGroup G]
  [IsTopologicalGroup G] [DiscreteTopology G]

omit [CommGroup G] [IsTopologicalGroup G] in
theorem sec_const_of_preconnected {W : Opens X} (hW : IsPreconnected (W : Set X))
    (f : C(W, G)) (x y : W) : f x = f y := by
  haveI := isPreconnected_iff_preconnectedSpace.1 hW
  exact PreconnectedSpace.constant inferInstance f.continuous

/-- Hypotheses on a four-set open family: all intersections of at most three
members are nonempty and preconnected. -/
structure TetCover (U : Fin 4 → Opens X) : Prop where
  ne3 : ∀ i j k, ((U i ⊓ U j ⊓ U k : Opens X) : Set X).Nonempty
  pre3 : ∀ i j k, IsPreconnected ((U i ⊓ U j ⊓ U k : Opens X) : Set X)
  pre2 : ∀ i j, IsPreconnected ((U i ⊓ U j : Opens X) : Set X)

variable {U : Fin 4 → Opens X} (hU : TetCover U)

/-- the chosen point of a triple intersection -/
noncomputable def tpt (i j k : Fin 4) : (U i ⊓ U j ⊓ U k : Opens X) :=
  ⟨(hU.ne3 i j k).some, (hU.ne3 i j k).some_mem⟩

/-- Value of a 2-cochain on the triple `(i,j,k)`. -/
noncomputable def val (c : TwoCochain U (contPresheaf X G)) (i j k : Fin 4) : G :=
  sec (c.ev i j k (homOfLE (inf_le_left.trans inf_le_left) : (U i ⊓ U j ⊓ U k : Opens X) ⟶ U i)
    (homOfLE (inf_le_left.trans inf_le_right)) (homOfLE inf_le_right)) (tpt hU i j k)

theorem ev_apply (c : TwoCochain U (contPresheaf X G)) (i j k : Fin 4) {T : Opens X}
    (a : T ⟶ U i) (b : T ⟶ U j) (d : T ⟶ U k) (x : T) :
    sec (c.ev i j k a b d) x = val hU c i j k := by
  have hT : T ≤ U i ⊓ U j ⊓ U k := le_inf (le_inf (leOfHom a) (leOfHom b)) (leOfHom d)
  have e := c.ev_precomp i j k (homOfLE hT)
    (homOfLE (inf_le_left.trans inf_le_left) : (U i ⊓ U j ⊓ U k : Opens X) ⟶ U i)
    (homOfLE (inf_le_left.trans inf_le_right)) (homOfLE inf_le_right)
  rw [Subsingleton.elim (homOfLE hT ≫ _) a, Subsingleton.elim (homOfLE hT ≫ _) b,
    Subsingleton.elim (homOfLE hT ≫ _) d] at e
  rw [← e]
  exact sec_const_of_preconnected (hU.pre3 i j k) _ _ _


/-- Value of a 1-cochain on the pair `(i,j)`. -/
noncomputable def val1 (α : PresheafOfGroups.OneCochain (contPresheaf X G) U) (i j : Fin 4) : G :=
  sec (α.ev i j (homOfLE inf_le_left : (U i ⊓ U j : Opens X) ⟶ U i) (homOfLE inf_le_right))
    ⟨(tpt hU i j j).1, (tpt hU i j j).2.1⟩

theorem ev1_apply (α : PresheafOfGroups.OneCochain (contPresheaf X G) U) (i j : Fin 4)
    {T : Opens X} (a : T ⟶ U i) (b : T ⟶ U j) (x : T) :
    sec (α.ev i j a b) x = val1 hU α i j := by
  have hT : T ≤ U i ⊓ U j := le_inf (leOfHom a) (leOfHom b)
  have e := α.ev_precomp i j (homOfLE hT)
    (homOfLE inf_le_left : (U i ⊓ U j : Opens X) ⟶ U i) (homOfLE inf_le_right)
  rw [Subsingleton.elim (homOfLE hT ≫ _) a, Subsingleton.elim (homOfLE hT ≫ _) b] at e
  rw [← e]
  exact sec_const_of_preconnected (hU.pre2 i j) _ _ _

/-- The four indices are pairwise distinct. -/
def AllDistinct (i j k l : Fin 4) : Prop := i ≠ j ∧ i ≠ k ∧ i ≠ l ∧ j ≠ k ∧ j ≠ l ∧ k ≠ l
instance (i j k l : Fin 4) : Decidable (AllDistinct i j k l) := by unfold AllDistinct; infer_instance

include hU in
theorem quad_nonempty (i j k l : Fin 4) (h : ¬ AllDistinct i j k l) :
    ((U i ⊓ U j ⊓ U k ⊓ U l : Opens X) : Set X).Nonempty := by
  simp only [AllDistinct, not_and_or, not_not] at h
  rcases h with h | h | h | h | h | h <;> subst h
  · obtain ⟨x, hx⟩ := hU.ne3 i k l; exact ⟨x, ⟨⟨⟨hx.1.1, hx.1.1⟩, hx.1.2⟩, hx.2⟩⟩
  · obtain ⟨x, hx⟩ := hU.ne3 i j l; exact ⟨x, ⟨⟨⟨hx.1.1, hx.1.2⟩, hx.1.1⟩, hx.2⟩⟩
  · obtain ⟨x, hx⟩ := hU.ne3 i j k; exact ⟨x, ⟨⟨⟨hx.1.1, hx.1.2⟩, hx.2⟩, hx.1.1⟩⟩
  · obtain ⟨x, hx⟩ := hU.ne3 i j l; exact ⟨x, ⟨⟨⟨hx.1.1, hx.1.2⟩, hx.1.2⟩, hx.2⟩⟩
  · obtain ⟨x, hx⟩ := hU.ne3 i j k; exact ⟨x, ⟨⟨⟨hx.1.1, hx.1.2⟩, hx.2⟩, hx.1.2⟩⟩
  · obtain ⟨x, hx⟩ := hU.ne3 i j k; exact ⟨x, ⟨⟨⟨hx.1.1, hx.1.2⟩, hx.2⟩, hx.2⟩⟩

/-- The cocycle identity on the values, wherever the quadruple intersection meets. -/
theorem val_cocycle (c : TwoCocycle U (contPresheaf X G)) (i j k l : Fin 4)
    (h : ¬ AllDistinct i j k l) :
    val hU c.toTwoCochain i j k * val hU c.toTwoCochain i k l =
      val hU c.toTwoCochain j k l * val hU c.toTwoCochain i j l := by
  obtain ⟨x, hx⟩ := quad_nonempty hU i j k l h
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
  rwa [m, m, ev_apply hU, ev_apply hU, ev_apply hU, ev_apply hU] at e

theorem tet_coboundary {A : Type*} [AddCommGroup A] (V : Fin 4 → Fin 4 → Fin 4 → A)
    (hc : ∀ i j k l, ¬ AllDistinct i j k l → V i j k + V i k l = V j k l + V i j l)
    (hd : V 1 2 3 - V 0 2 3 + V 0 1 3 - V 0 1 2 = 0) (i j k : Fin 4) :
    V i j k = V 0 i j + V 0 j k - V 0 i k := by
  have hA : ∀ i j k, ¬ AllDistinct 0 i j k → V i j k = V 0 i j + V 0 j k - V 0 i k :=
    fun i j k h => eq_sub_iff_add_eq.2 (hc 0 i j k h).symm
  have cyc : ∀ a b c, ¬ AllDistinct a b c a → ¬ AllDistinct 0 a c a → ¬ AllDistinct 0 a b a →
      V a b c = V 0 a b + V 0 b c - V 0 a c → V b c a = V 0 b c + V 0 c a - V 0 b a :=
    fun a b c h1 h2 h3 hp => by
      linear_combination (norm := abel) hp + hA a c a h2 - hA a b a h3 - hc a b c a h1
  have swp : ∀ a b c, ¬ AllDistinct a b c b → ¬ AllDistinct 0 b c b → ¬ AllDistinct 0 a b b →
      V a b c = V 0 a b + V 0 b c - V 0 a c → V a c b = V 0 a c + V 0 c b - V 0 a b :=
    fun a b c h1 h2 h3 hp => by
      linear_combination (norm := abel) hc a b c b h1 + hA b c b h2 + hA a b b h3 - hp
  have h123 : V 1 2 3 = V 0 1 2 + V 0 2 3 - V 0 1 3 := by linear_combination (norm := abel) hd
  have h231 := cyc 1 2 3 (by decide) (by decide) (by decide) h123
  have h312 := cyc 2 3 1 (by decide) (by decide) (by decide) h231
  have h132 := swp 1 2 3 (by decide) (by decide) (by decide) h123
  have h321 := cyc 1 3 2 (by decide) (by decide) (by decide) h132
  have h213 := cyc 3 2 1 (by decide) (by decide) (by decide) h321
  by_cases h : AllDistinct 0 i j k
  · fin_cases i <;> fin_cases j <;> fin_cases k <;> simp [AllDistinct] at h ⊢ <;> assumption
  · exact hA i j k h

/-- **The degree** of a 2-cochain: the alternating product of its values on the
four faces of the tetrahedron, `c(1,2,3) c(0,2,3)⁻¹ c(0,1,3) c(0,1,2)⁻¹`. -/
noncomputable def deg (c : TwoCochain U (contPresheaf X G)) : G :=
  val hU c 1 2 3 * (val hU c 0 2 3)⁻¹ * val hU c 0 1 3 * (val hU c 0 1 2)⁻¹

theorem val_one (i j k : Fin 4) :
    val hU (TwoCocycle.one : TwoCocycle U (contPresheaf X G)).toTwoCochain i j k = 1 := rfl

theorem deg_one : deg hU (TwoCocycle.one : TwoCocycle U (contPresheaf X G)).toTwoCochain = 1 := by
  simp [deg, val_one]

/-- The degree is invariant under coboundaries. -/
theorem deg_rel {c₁ c₂ : TwoCocycle U (contPresheaf X G)} (h : TwoCocycle.Rel c₁ c₂) :
    deg hU c₂.toTwoCochain = deg hU c₁.toTwoCochain := by
  obtain ⟨α, hα⟩ := h
  have hv : ∀ i j k, val hU c₂.toTwoCochain i j k =
      val hU c₁.toTwoCochain i j k * (val1 hU α i j * val1 hU α j k * (val1 hU α i k)⁻¹) := by
    intro i j k
    have e := congrArg (fun f => sec f (tpt hU i j k)) (hα i j k
      (homOfLE (inf_le_left.trans inf_le_left) : (U i ⊓ U j ⊓ U k : Opens X) ⟶ U i)
      (homOfLE (inf_le_left.trans inf_le_right)) (homOfLE inf_le_right))
    simp only at e
    have m : ∀ f g : (contPresheaf X G).obj (op (U i ⊓ U j ⊓ U k)), sec (f * g) (tpt hU i j k) =
        sec f (tpt hU i j k) * sec g (tpt hU i j k) := fun _ _ => rfl
    have n : ∀ f : (contPresheaf X G).obj (op (U i ⊓ U j ⊓ U k)), sec f⁻¹ (tpt hU i j k) =
        (sec f (tpt hU i j k))⁻¹ := fun _ => rfl
    rw [m, m, m, n, ev1_apply hU, ev1_apply hU, ev1_apply hU] at e
    exact e
  apply Additive.ofMul.injective
  simp only [deg, hv, ofMul_mul, ofMul_inv]
  abel


/-- The constant 1-cochain with values `w i j`. -/
def constOneCochain (w : Fin 4 → Fin 4 → G) : PresheafOfGroups.OneCochain (contPresheaf X G) U where
  ev i j T _ _ := (ContinuousMap.const T (w i j) : C(T, G))
  ev_precomp _ _ _ _ _ _ _ := rfl

/-- **Degree one forces a coboundary.** A 2-cocycle of degree `1` is the
coboundary of the constant 1-cochain `(i,j) ↦ c(0,i,j)`. -/
theorem exists_coboundary_of_deg_eq_one (c : TwoCocycle U (contPresheaf X G))
    (hd : deg hU c.toTwoCochain = 1) :
    ∃ α : PresheafOfGroups.OneCochain (contPresheaf X G) U, ∀ (i j k : Fin 4) ⦃T : Opens X⦄
      (a : T ⟶ U i) (b : T ⟶ U j) (d : T ⟶ U k),
      c.ev i j k a b d = α.ev i j a b * α.ev j k b d * (α.ev i k a d)⁻¹ := by
  set V : Fin 4 → Fin 4 → Fin 4 → Additive G :=
    fun i j k => Additive.ofMul (val hU c.toTwoCochain i j k)
  have hc : ∀ i j k l, ¬ AllDistinct i j k l → V i j k + V i k l = V j k l + V i j l :=
    fun i j k l h => by
      simp only [V, ← ofMul_mul, val_cocycle hU c i j k l h]
  have hd' : V 1 2 3 - V 0 2 3 + V 0 1 3 - V 0 1 2 = 0 := by
    have := congrArg Additive.ofMul hd
    simp only [deg, ofMul_mul, ofMul_inv, ofMul_one] at this
    simp only [V, sub_eq_add_neg]; exact this
  refine ⟨constOneCochain (fun i j => val hU c.toTwoCochain 0 i j), fun i j k T a b d => ?_⟩
  apply ContinuousMap.ext
  intro x
  change sec (c.ev i j k a b d) x = _
  rw [ev_apply hU]
  have e := tet_coboundary V hc hd' i j k
  change val hU c.toTwoCochain i j k = val hU c.toTwoCochain 0 i j * val hU c.toTwoCochain 0 j k *
    (val hU c.toTwoCochain 0 i k)⁻¹
  apply Additive.ofMul.injective
  change V i j k = _
  rw [e]; simp only [V, ofMul_mul, ofMul_inv, sub_eq_add_neg]


/-- The degree on `H²` of the cover. -/
noncomputable def degH2 : H2 U (contPresheaf X G) → G :=
  Quot.lift (fun c => deg hU c.toTwoCochain) (fun _ _ h => (deg_rel hU h).symm)

/-- **The degree detects the class.** On a `TetCover`, a class in `H²` is
trivial exactly when its degree is `1`. -/
theorem degH2_eq_one_iff (x : H2 U (contPresheaf X G)) : degH2 hU x = 1 ↔ x = 1 := by
  induction x using Quot.ind with
  | mk c =>
    change deg hU c.toTwoCochain = 1 ↔ c.class = 1
    rw [TwoCocycle.class_eq_one_iff (contPresheaf_comm (X := X))]
    constructor
    · exact exists_coboundary_of_deg_eq_one hU c
    · rintro ⟨α, hα⟩
      have hr : TwoCocycle.Rel (TwoCocycle.one : TwoCocycle U (contPresheaf X G)) c :=
        ⟨α, fun i j k T a b d => by rw [hα]; exact (one_mul _).symm⟩
      rw [deg_rel hU hr, deg_one]

variable {H : Type} [TopologicalSpace H] [CommGroup H] [IsTopologicalGroup H] [DiscreteTopology H]

/-- The degree is natural in the coefficients. -/
theorem deg_map (φ : G →* H) (hφ : Continuous φ) (c : TwoCocycle U (contPresheaf X G)) :
    deg hU (c.map (postcomp X φ hφ)).toTwoCochain = φ (deg hU c.toTwoCochain) := by
  simp only [deg, map_mul, map_inv]; rfl


/-- The tetrahedral family as a cover of `X` (indices `Fin 4`). -/
def tetCover (U : Fin 4 → Opens X) : Cover.{0} (⊤ : Opens X) :=
  ⟨Fin 4, U, fun _ => homOfLE le_top⟩

theorem tetCover_cof (𝒱 : Cover.{0} (⊤ : Opens X)) (h : 𝒱 = tetCover U) :
    Nonempty ((tetCover U).Refines 𝒱) := by
  subst h; exact ⟨Cover.Refines.id _⟩

/-- The degree on the colimit `Ȟ²` when the only admissible cover is the
tetrahedral one. -/
noncomputable def degCech (x : CechH2 (contPresheaf X G) (· = tetCover U)) : G :=
  degH2 (G := G) hU (toCofinal (contPresheaf_comm (X := X)) (tetCover U) tetCover_cof x)

theorem degCech_map (φ : G →* H) (hφ : Continuous φ)
    (x : CechH2 (contPresheaf X G) (· = tetCover U)) :
    degCech hU (CechH2.map (postcomp X φ hφ) x) = φ (degCech hU x) := by
  induction x using Quot.ind with
  | mk y =>
    change degH2 hU (toCofinalAux (tetCover U) tetCover_cof (y.map _)) =
      φ (degH2 hU (toCofinalAux (tetCover U) tetCover_cof y))
    unfold toCofinalAux
    exact deg_map hU φ hφ (y.c.pull (tetCover_cof y.cov y.adm).some.r
      (tetCover_cof y.cov y.adm).some.f)

theorem degCech_eq_one_iff (x : CechH2 (contPresheaf X G) (· = tetCover U)) :
    degCech hU x = 1 ↔ x = cechClass (Cov := (· = tetCover U)) (tetCover U) rfl TwoCocycle.one := by
  unfold degCech
  rw [degH2_eq_one_iff]
  constructor
  · intro h
    have := toCech_toCofinal (Cov := (· = tetCover U)) (contPresheaf_comm (X := X)) (tetCover U) rfl tetCover_cof x
    rw [h] at this; exact this.symm
  · rintro rfl
    exact toCofinal_toCech (Cov := (· = tetCover U)) (contPresheaf_comm (X := X)) (tetCover U) rfl tetCover_cof 1


omit [CommGroup G] [IsTopologicalGroup G] [DiscreteTopology G] in
/-- **`KummerSurfaceData` at the level of one cover.** On any space carrying a
`TetCover`, with the tetrahedral cover as the only admissible cover, the degree
maps exist and have the required properties. This is a statement about the
cover, NOT about the colimit over all open covers (step C2). -/
noncomputable def kummerSurfaceData_tet (n : ℕ) [NeZero n] :
    KummerSurfaceData X n (· = tetCover U) where
  deg x := Multiplicative.toAdd (degCech hU x)
  degN x := ((Multiplicative.toAdd (kappaSection n (degCech hU x)) : ℤ) : ZMod n)
  degN_eq_zero_iff 𝒰 h𝒰 x := by
    subst h𝒰
    rw [ZMod.intCast_zmod_eq_zero_iff_dvd, ← kappa_eq_one_iff, kappa_kappaSection,
      degCech_eq_one_iff]
  degN_map x := by
    rw [degCech_map hU (kappa n) (continuous_kappa n)]
    set d := degCech hU x
    rw [ZMod.intCast_eq_intCast_iff_dvd_sub]
    have h1 : kappa n (d * (kappaSection n (kappa n d))⁻¹) = 1 := by
      rw [map_mul, map_inv, kappa_kappaSection, mul_inv_cancel]
    rw [kappa_eq_one_iff] at h1
    simpa [toAdd_mul, toAdd_inv, sub_eq_add_neg] using h1


/-! ### Surjectivity when no point lies in all four sets -/

/-- The oriented incidence of the triple `(i,j,k)` with the face `{1,2,3}`. -/
def tri (i j k : Fin 4) : ℤ :=
  if (i, j, k) = (1, 2, 3) ∨ (i, j, k) = (2, 3, 1) ∨ (i, j, k) = (3, 1, 2) then 1
  else if (i, j, k) = (1, 3, 2) ∨ (i, j, k) = (3, 2, 1) ∨ (i, j, k) = (2, 1, 3) then -1
  else 0

theorem tri_cocycle : ∀ i j k l : Fin 4, ¬ AllDistinct i j k l →
    tri i j k + tri i k l = tri j k l + tri i j l := by decide

theorem cover_of_allDistinct : ∀ i j k l : Fin 4, AllDistinct i j k l →
    ∀ m : Fin 4, m = i ∨ m = j ∨ m = k ∨ m = l := by decide

omit [IsTopologicalGroup G] [DiscreteTopology G] in
/-- The 2-cocycle with value `g` on the oriented face `(1,2,3)` and `1` elsewhere,
when no point of `X` lies in all four sets. -/
noncomputable def faceCocycle (hE : ∀ x : X, ∃ m : Fin 4, x ∉ U m) (g : G) :
    TwoCocycle U (contPresheaf X G) where
  ev i j k T _ _ _ := (ContinuousMap.const T (g ^ tri i j k) : C(T, G))
  ev_precomp _ _ _ _ _ _ _ _ _ := rfl
  cocycle i j k l T a b c d := by
    by_cases h : AllDistinct i j k l
    · refine ContinuousMap.ext fun x => (?_ : False).elim
      obtain ⟨m, hm⟩ := hE x.1
      rcases cover_of_allDistinct i j k l h m with rfl | rfl | rfl | rfl
      · exact hm (leOfHom a x.2)
      · exact hm (leOfHom b x.2)
      · exact hm (leOfHom c x.2)
      · exact hm (leOfHom d x.2)
    · refine ContinuousMap.ext fun x => ?_
      change g ^ tri i j k * g ^ tri i k l = g ^ tri j k l * g ^ tri i j l
      rw [← zpow_add, ← zpow_add, tri_cocycle i j k l h]

/-- **The degree is onto** when no point lies in all four sets. -/
theorem deg_faceCocycle (hE : ∀ x : X, ∃ m : Fin 4, x ∉ U m) (g : G) :
    deg hU (faceCocycle hE g).toTwoCochain = g := by
  change g ^ tri 1 2 3 * (g ^ tri 0 2 3)⁻¹ * g ^ tri 0 1 3 * (g ^ tri 0 1 2)⁻¹ = g
  simp [tri]

theorem degH2_surjective (hE : ∀ x : X, ∃ m : Fin 4, x ∉ U m) :
    Function.Surjective (degH2 (G := G) hU) :=
  fun g => ⟨(faceCocycle hE g).class, deg_faceCocycle hU hE g⟩

/-- **Equal degrees force cohomologous cocycles.** -/
theorem rel_of_deg_eq (c₁ c₂ : TwoCocycle U (contPresheaf X G))
    (hd : deg hU c₁.toTwoCochain = deg hU c₂.toTwoCochain) : TwoCocycle.Rel c₁ c₂ := by
  set V : Fin 4 → Fin 4 → Fin 4 → Additive G := fun i j k =>
    Additive.ofMul (val hU c₂.toTwoCochain i j k) - Additive.ofMul (val hU c₁.toTwoCochain i j k)
  have hc : ∀ i j k l, ¬ AllDistinct i j k l → V i j k + V i k l = V j k l + V i j l :=
    fun i j k l h => by
      have e₁ := congrArg Additive.ofMul (val_cocycle hU c₁ i j k l h)
      have e₂ := congrArg Additive.ofMul (val_cocycle hU c₂ i j k l h)
      simp only [ofMul_mul] at e₁ e₂
      simp only [V]; linear_combination (norm := abel) e₂ - e₁
  have hd' : V 1 2 3 - V 0 2 3 + V 0 1 3 - V 0 1 2 = 0 := by
    have := congrArg Additive.ofMul hd
    simp only [deg, ofMul_mul, ofMul_inv] at this
    simp only [V]; linear_combination (norm := abel) -this
  refine ⟨constOneCochain (fun i j => val hU c₂.toTwoCochain 0 i j *
    (val hU c₁.toTwoCochain 0 i j)⁻¹), fun i j k T a b d => ?_⟩
  apply ContinuousMap.ext
  intro x
  change sec (c₂.ev i j k a b d) x = sec (c₁.ev i j k a b d) x * _
  rw [ev_apply hU, ev_apply hU]
  have e := tet_coboundary V hc hd' i j k
  apply Additive.ofMul.injective
  change Additive.ofMul (val hU c₂.toTwoCochain i j k) = Additive.ofMul
    (val hU c₁.toTwoCochain i j k * ((val hU c₂.toTwoCochain 0 i j *
    (val hU c₁.toTwoCochain 0 i j)⁻¹) * (val hU c₂.toTwoCochain 0 j k *
    (val hU c₁.toTwoCochain 0 j k)⁻¹) * (val hU c₂.toTwoCochain 0 i k *
    (val hU c₁.toTwoCochain 0 i k)⁻¹)⁻¹))
  simp only [V] at e
  simp only [ofMul_mul, ofMul_inv]
  linear_combination (norm := abel) e

theorem degH2_injective : Function.Injective (degH2 (G := G) hU) := by
  intro x y h
  induction x using Quot.ind with
  | mk c₁ =>
    induction y using Quot.ind with
    | mk c₂ => exact Quot.sound (rel_of_deg_eq hU c₁ c₂ h)

/-- **`H²` of the cover is `G`** when no point lies in all four sets. -/
noncomputable def h2EquivOfEmptyQuad (hE : ∀ x : X, ∃ m : Fin 4, x ∉ U m) :
    H2 U (contPresheaf X G) ≃ G :=
  Equiv.ofBijective (degH2 hU) ⟨degH2_injective hU, degH2_surjective hU hE⟩

/-- The cover-level Čech `H²` (admissible covers: `tetCover U` alone) is `G`. -/
noncomputable def cechH2EquivOfEmptyQuad (hE : ∀ x : X, ∃ m : Fin 4, x ∉ U m) :
    CechH2 (contPresheaf X G) (· = tetCover U) ≃ G :=
  (cechH2EquivCofinal (Cov := (· = tetCover U)) (contPresheaf_comm (X := X)) (tetCover U) rfl
    tetCover_cof).trans (h2EquivOfEmptyQuad hU hE)

end QOU.CentralExtension.Cech
