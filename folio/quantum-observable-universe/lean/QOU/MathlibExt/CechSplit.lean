import QOU.MathlibExt.CechNerveValues

/-!
# Splitting one set of a cover leaves Čech `H²` unchanged

Step P2 of the C2 comparison (route R3, surface case). Let `U : ι → Opens X` be a
family with preconnected pairwise and triple intersections, and cut one member
`U v` into two open pieces `A, B` with `A ∪ B = U v`. The new family
`splitFam U v A B`, indexed by `Option ι` (`none ↦ A`, `some v ↦ B`,
`some i ↦ U i`), refines `U` along `splitR v`. If the new family also has
preconnected pairwise and triple intersections, pulling back is a bijection
`H²(U, G) → H²(splitFam U v A B, G)` for every discrete commutative group `G`.

In nerve terms this is an edge contraction. The link condition it needs
(`A` and `B` both meet `σ` ⇒ `A ∩ B` meets `σ`) is not a hypothesis: it follows
from preconnectedness of the triple intersections of `U` (`split_link`).

## Results, all sorry-free

* `split_link`: a preconnected set inside `A ∪ B` that meets both meets `A ∩ B`.
* `split_inj_core`, `split_surj_core`: the statement on nerve values, with
  values in any additive commutative group.
* `split_pull_bijective`: the statement on `H²`.

## What this does NOT do

It does not produce the fine covers of the sphere; that is steps P3 and P4
(`CechSphereFine`, `CechSphereGood`), which prove `HemiComputesCech`.

-- Ref: [manuscript] lifting-and-descent, route R3, surface step C2
-/
open CategoryTheory Opposite TopologicalSpace
namespace QOU.CentralExtension.Cech
open CechGerbe

variable {X : Type} [TopologicalSpace X]

/-- Triple intersection is nonempty. -/
abbrev N3 {κ : Type} (W : κ → Opens X) (i j k : κ) : Prop :=
  ((W i ⊓ W j ⊓ W k : Opens X) : Set X).Nonempty

/-- Quadruple intersection is nonempty. -/
abbrev N4 {κ : Type} (W : κ → Opens X) (i j k l : κ) : Prop :=
  ((W i ⊓ W j ⊓ W k ⊓ W l : Opens X) : Set X).Nonempty

theorem n3_iff {κ : Type} (W : κ → Opens X) (i j k : κ) :
    N3 W i j k ↔ ∃ t, t ∈ W i ∧ t ∈ W j ∧ t ∈ W k := by
  simp only [N3, Set.Nonempty, Opens.coe_inf, Set.mem_inter_iff, SetLike.mem_coe, and_assoc]

theorem n4_iff {κ : Type} (W : κ → Opens X) (i j k l : κ) :
    N4 W i j k l ↔ ∃ t, t ∈ W i ∧ t ∈ W j ∧ t ∈ W k ∧ t ∈ W l := by
  simp only [N4, Set.Nonempty, Opens.coe_inf, Set.mem_inter_iff, SetLike.mem_coe, and_assoc]

variable {ι : Type}

open Classical in
/-- The family obtained by cutting `U v` into `A` (index `none`) and `B`
(index `some v`). -/
noncomputable def splitFam (U : ι → Opens X) (v : ι) (A B : Opens X) : Option ι → Opens X
  | none => A
  | some i => if i = v then B else U i

/-- The index map of the refinement `splitFam U v A B → U`. -/
def splitR (v : ι) : Option ι → ι := fun x => x.elim v id

variable {U : ι → Opens X} {v : ι} {A B : Opens X}

@[simp] theorem splitR_none : splitR v none = v := rfl
@[simp] theorem splitR_some (i : ι) : splitR v (some i) = i := rfl
@[simp] theorem splitFam_none : splitFam U v A B none = A := rfl
@[simp] theorem splitFam_some_v : splitFam U v A B (some v) = B := by simp [splitFam]

theorem splitFam_some_ne {i : ι} (h : i ≠ v) : splitFam U v A B (some i) = U i := by
  simp [splitFam, h]

theorem splitFam_le (hA : A ≤ U v) (hB : B ≤ U v) (x : Option ι) :
    splitFam U v A B x ≤ U (splitR v x) := by
  cases x with
  | none => exact hA
  | some i =>
    by_cases h : i = v
    · subst h; simpa using hB
    · rw [splitFam_some_ne h]; rfl

theorem mem_splitFam_of {t : X} (x : Option ι) (htA : t ∈ A) (htB : t ∈ B)
    (htU : t ∈ U (splitR v x)) : t ∈ splitFam U v A B x := by
  cases x with
  | none => exact htA
  | some i =>
    by_cases h : i = v
    · subst h; simpa using htB
    · rw [splitFam_some_ne h]; exact htU

theorem mem_splitFam_some_of {t : X} (i : ι) (htB : t ∈ B) (htU : t ∈ U i) :
    t ∈ splitFam U v A B (some i) := by
  by_cases h : i = v
  · subst h; simpa using htB
  · rw [splitFam_some_ne h]; exact htU

/-- **The link condition.** A preconnected set inside `A ∪ B` meeting both `A`
and `B` meets `A ∩ B`. -/
theorem split_link {P : Set X} (hP : IsPreconnected P) (hPAB : ∀ t ∈ P, t ∈ A ∨ t ∈ B)
    {s t : X} (hs : s ∈ P) (hsA : s ∈ A) (ht : t ∈ P) (htB : t ∈ B) :
    ∃ u ∈ P, u ∈ A ∧ u ∈ B := by
  obtain ⟨u, hu, huA, huB⟩ := hP (A : Set X) (B : Set X) A.isOpen B.isOpen
    (fun t ht => hPAB t ht) ⟨s, hs, hsA⟩ ⟨t, ht, htB⟩
  exact ⟨u, hu, huA, huB⟩

theorem mem_A_or_B (hcov : U v ≤ A ⊔ B) {t : X} (ht : t ∈ U v) : t ∈ A ∨ t ∈ B := by
  have := hcov ht
  have h2 : t ∈ (A : Set X) ∪ B := by rw [← Opens.coe_sup]; exact this
  exact h2

/-! ### Injectivity on values -/

/-- **Injectivity on values.** A 2-cocycle on the nerve of `U` whose
pullback to the split family is a coboundary is itself a coboundary. -/
theorem split_inj_core {M : Type*} [AddCommGroup M] (hA : A ≤ U v) (hB : B ≤ U v)
    (hcov : U v ≤ A ⊔ B) (hU : ConnFamily U) (D : ι → ι → ι → M)
    (hD : ∀ i j k l, N4 U i j k l → D i j k + D i k l = D j k l + D i j l)
    (z' : Option ι → Option ι → M)
    (hz : ∀ x y z, N3 (splitFam U v A B) x y z →
      D (splitR v x) (splitR v y) (splitR v z) = z' x y + z' y z - z' x z) :
    ∃ z : ι → ι → M, ∀ i j k, N3 U i j k → D i j k = z i j + z j k - z i k := by
  classical
  set S := splitFam U v A B with hS
  set r : Option ι → ι := splitR v with hr
  have hSle : ∀ x, ∀ t, t ∈ S x → t ∈ U (r x) := fun x t ht => splitFam_le hA hB x ht
  -- step 1: cone off `U v`
  set wv : ι → ι → M := fun i j => D v i j
  have hstep1 : ∀ i j k t, t ∈ U v → t ∈ U i → t ∈ U j → t ∈ U k →
      D i j k = wv i j + wv j k - wv i k := by
    intro i j k t h0 h1 h2 h3
    have := hD v i j k ((n4_iff U v i j k).2 ⟨t, h0, h1, h2, h3⟩)
    simp only [wv]; linear_combination (norm := abel) -this
  set z0 : Option ι → Option ι → M := fun x y => z' x y - wv (r x) (r y)
  -- step 2: `δ z0` vanishes on triples meeting `U v`
  have hE : ∀ x y z t, t ∈ S x → t ∈ S y → t ∈ S z → t ∈ U v →
      z0 x y + z0 y z - z0 x z = 0 := by
    intro x y z t hx hy hz' h0
    have h1 := hz x y z ((n3_iff S x y z).2 ⟨t, hx, hy, hz'⟩)
    have h2 := hstep1 (r x) (r y) (r z) t h0 (hSle x t hx) (hSle y t hy) (hSle z t hz')
    simp only [z0]; linear_combination (norm := abel) h2 - h1
  -- step 3: a 0-cochain making `z0` vanish near `U v`
  set a : Option ι := none
  set b : Option ι := some v
  have hSa : S a = A := rfl
  have hSb : S b = B := splitFam_some_v
  let p : Option ι → M := fun x =>
    if ∃ t, t ∈ A ∧ t ∈ S x then z0 a x else z0 a b + z0 b x
  have hF1 : ∀ x, (∃ t, t ∈ A ∧ t ∈ S x) → (∃ t, t ∈ B ∧ t ∈ S x) →
      z0 a x = z0 a b + z0 b x := by
    rintro x ⟨s, hsA, hsx⟩ ⟨t, htB, htx⟩
    have hP := hU.pre3 v v (r x)
    obtain ⟨u, hu, huA, huB⟩ := split_link (A := A) (B := B) hP
      (fun t ht => mem_A_or_B hcov ht.1.1)
      (s := s) (t := t) ⟨⟨hA hsA, hA hsA⟩, hSle x s hsx⟩ hsA
      ⟨⟨hB htB, hB htB⟩, hSle x t htx⟩ htB
    have hux : u ∈ S x := mem_splitFam_of x huA huB hu.2
    have := hE a b x u huA (hSb ▸ huB) hux (hA huA)
    linear_combination (norm := abel) -this
  have hpB : ∀ x, (∃ t, t ∈ B ∧ t ∈ S x) → p x = z0 a b + z0 b x := by
    intro x hBx
    simp only [p]
    split_ifs with hAx
    · exact hF1 x hAx hBx
    · rfl
  set z'' : Option ι → Option ι → M := fun x y => z0 x y + p x - p y
  have hG : ∀ x y t, t ∈ U v → t ∈ S x → t ∈ S y → z'' x y = 0 := by
    intro x y t h0 hx hy
    rcases mem_A_or_B hcov h0 with htA | htB
    · have hpx : p x = z0 a x := by simp only [p]; rw [if_pos ⟨t, htA, hx⟩]
      have hpy : p y = z0 a y := by simp only [p]; rw [if_pos ⟨t, htA, hy⟩]
      have := hE a x y t htA hx hy h0
      simp only [z'', hpx, hpy]; linear_combination (norm := abel) this
    · have hpx := hpB x ⟨t, htB, hx⟩
      have hpy := hpB y ⟨t, htB, hy⟩
      have := hE b x y t (hSb ▸ htB) hx hy h0
      simp only [z'', hpx, hpy]; linear_combination (norm := abel) this
  -- step 4: descend
  refine ⟨fun i j => (if i = v ∨ j = v then 0 else z'' (some i) (some j)) + wv i j,
    fun i j k hijk => ?_⟩
  obtain ⟨t, hti, htj, htk⟩ := (n3_iff U i j k).1 hijk
  by_cases h0 : t ∈ U v
  · have hpair : ∀ m n, t ∈ U m → t ∈ U n →
        (if m = v ∨ n = v then (0 : M) else z'' (some m) (some n)) = 0 := by
      intro m n hm hn
      split_ifs with hmn
      · rfl
      · push_neg at hmn
        exact hG _ _ t h0 (by rw [hS, splitFam_some_ne hmn.1]; exact hm)
          (by rw [hS, splitFam_some_ne hmn.2]; exact hn)
    beta_reduce
    rw [hpair i j hti htj, hpair j k htj htk, hpair i k hti htk, hstep1 i j k t h0 hti htj htk]
    abel
  · have hne : ∀ m, t ∈ U m → m ≠ v := fun m hm hmv => h0 (hmv ▸ hm)
    have hi := hne i hti; have hj := hne j htj; have hk := hne k htk
    have hT : N3 S (some i) (some j) (some k) := (n3_iff S _ _ _).2
      ⟨t, by rw [hS, splitFam_some_ne hi]; exact hti, by rw [hS, splitFam_some_ne hj]; exact htj,
        by rw [hS, splitFam_some_ne hk]; exact htk⟩
    have := hz _ _ _ hT
    simp only [hr, splitR_some] at this
    simp only [hi, hj, hk, or_self, if_false, z'', z0, hr, splitR_some]
    linear_combination (norm := abel) this

/-! ### Surjectivity on values -/

/-- **Surjectivity on values.** Every 2-cocycle on the nerve of the split
family differs by a coboundary from the pullback of a 2-cocycle on `U`. -/
theorem split_surj_core {M : Type*} [AddCommGroup M] (hA : A ≤ U v) (hB : B ≤ U v)
    (hcov : U v ≤ A ⊔ B) (hU : ConnFamily U) (V' : Option ι → Option ι → Option ι → M)
    (hV' : ∀ x y z w, N4 (splitFam U v A B) x y z w →
      V' x y z + V' x z w = V' y z w + V' x y w) :
    ∃ (V : ι → ι → ι → M) (u : Option ι → Option ι → M),
      (∀ i j k l, N4 U i j k l → V i j k + V i k l = V j k l + V i j l) ∧
      ∀ x y z, N3 (splitFam U v A B) x y z →
        V (splitR v x) (splitR v y) (splitR v z) = V' x y z + (u x y + u y z - u x z) := by
  classical
  set S := splitFam U v A B with hS
  set r : Option ι → ι := splitR v with hr
  have hSle : ∀ x, ∀ t, t ∈ S x → t ∈ U (r x) := fun x t ht => splitFam_le hA hB x ht
  have hSb : ∀ q, q ∈ S (some v) → q ∈ B := fun q h => by rwa [hS, splitFam_some_v] at h
  set u : Option ι → Option ι → M := fun x y => - V' none x y
  set V'' : Option ι → Option ι → Option ι → M := fun x y z => V' x y z + (u x y + u y z - u x z)
  have hV''c : ∀ x y z w, N4 S x y z w → V'' x y z + V'' x z w = V'' y z w + V'' x y w := by
    intro x y z w h
    have := hV' x y z w h
    simp only [V'', u]; linear_combination (norm := abel) this
  -- `V''` vanishes on triples meeting `A`
  have hH3 : ∀ x y z t, t ∈ A → t ∈ S x → t ∈ S y → t ∈ S z → V'' x y z = 0 := by
    intro x y z t hA' hx hy hz
    have := hV' none x y z ((n4_iff S _ _ _ _).2 ⟨t, hA', hx, hy, hz⟩)
    simp only [V'', u]; linear_combination (norm := abel) -this
  set V : ι → ι → ι → M := fun i j k =>
    if N3 S (some i) (some j) (some k) then V'' (some i) (some j) (some k) else 0 with hVdef
  -- `V'' ` is invariant under moving between lifts
  have hK : ∀ x y z, N3 S x y z → V (r x) (r y) (r z) = V'' x y z := by
    intro x y z hT
    obtain ⟨s, hsx, hsy, hsz⟩ := (n3_iff S x y z).1 hT
    by_cases hn : x = none ∨ y = none ∨ z = none
    · have hsA : s ∈ A := by rcases hn with rfl | rfl | rfl <;> assumption
      have hP0 : r x = v ∨ r y = v ∨ r z = v := by
        rcases hn with rfl | rfl | rfl <;> simp [hr]
      rw [hH3 x y z s hsA hsx hsy hsz]
      simp only [hVdef]
      split_ifs with hL
      · obtain ⟨q, hqx, hqy, hqz⟩ := (n3_iff S _ _ _).1 hL
        have hqB : q ∈ B := by
          rcases hn with rfl | rfl | rfl
          · exact hSb q hqx
          · exact hSb q hqy
          · exact hSb q hqz
        have hP := hU.pre3 (r x) (r y) (r z)
        obtain ⟨w, hw, hwA, hwB⟩ := split_link (A := A) (B := B) hP
          (fun t ht => by
            rcases hP0 with h | h | h
            · exact mem_A_or_B hcov (h ▸ ht.1.1)
            · exact mem_A_or_B hcov (h ▸ ht.1.2)
            · exact mem_A_or_B hcov (h ▸ ht.2))
          (s := s) (t := q) ⟨⟨hSle x s hsx, hSle y s hsy⟩, hSle z s hsz⟩ hsA
          ⟨⟨by simpa [hr] using hSle (some (r x)) q hqx,
            by simpa [hr] using hSle (some (r y)) q hqy⟩,
            by simpa [hr] using hSle (some (r z)) q hqz⟩ hqB
        exact hH3 _ _ _ w hwA (mem_splitFam_some_of _ hwB hw.1.1)
          (mem_splitFam_some_of _ hwB hw.1.2) (mem_splitFam_some_of _ hwB hw.2)
      · rfl
    · push_neg at hn
      obtain ⟨i, rfl⟩ := Option.ne_none_iff_exists'.1 hn.1
      obtain ⟨j, rfl⟩ := Option.ne_none_iff_exists'.1 hn.2.1
      obtain ⟨k, rfl⟩ := Option.ne_none_iff_exists'.1 hn.2.2
      simp only [hVdef, hr, splitR_some]
      rw [if_pos hT]
  refine ⟨V, u, fun i j k l h => ?_, fun x y z hT => hK x y z hT⟩
  obtain ⟨t, hti, htj, htk, htl⟩ := (n4_iff U i j k l).1 h
  let lift : ι → Option ι := fun m => if m = v ∧ t ∈ A then none else some m
  have hrl : ∀ m, r (lift m) = m := by
    intro m
    simp only [lift]
    split_ifs with hm
    · simp [hr, hm.1]
    · simp [hr]
  have hmem : ∀ m, t ∈ U m → t ∈ S (lift m) := by
    intro m hm
    simp only [lift]
    split_ifs with hmv
    · exact hmv.2
    · by_cases hv : m = v
      · rcases mem_A_or_B hcov (hv ▸ hm) with h' | h'
        · exact absurd ⟨hv, h'⟩ hmv
        · exact mem_splitFam_some_of m h' hm
      · rw [hS, splitFam_some_ne hv]; exact hm
  have K3 : ∀ m n o, t ∈ U m → t ∈ U n → t ∈ U o → V m n o = V'' (lift m) (lift n) (lift o) := by
    intro m n o hm hn ho
    have := hK _ _ _ ((n3_iff S _ _ _).2 ⟨t, hmem m hm, hmem n hn, hmem o ho⟩)
    rwa [hrl, hrl, hrl] at this
  rw [K3 i j k hti htj htk, K3 i k l hti htk htl, K3 j k l htj htk htl, K3 i j l hti htj htl]
  exact hV''c _ _ _ _ ((n4_iff S _ _ _ _).2 ⟨t, hmem i hti, hmem j htj, hmem k htk, hmem l htl⟩)

/-! ### The statement on `H²` -/

variable {G : Type} [TopologicalSpace G] [CommGroup G] [IsTopologicalGroup G]
  [DiscreteTopology G]

/-- **Splitting one set keeps `H²`.** If `A ∪ B = U v` and both `U` and the
split family have preconnected pairwise and triple intersections, pulling
back along the split is a bijection on `H²` with discrete commutative
coefficients. -/
theorem split_pull_bijective (hA : A ≤ U v) (hB : B ≤ U v) (hcov : U v ≤ A ⊔ B)
    (hU : ConnFamily U) (hU' : ConnFamily (splitFam U v A B)) :
    Function.Bijective (H2.pull (𝒜 := contPresheaf X G) (U := U) (splitR v)
      (fun x => homOfLE (splitFam_le hA hB x))) := by
  have hcomm := contPresheaf_comm (X := X) (G := G)
  constructor
  · intro x y hxy
    induction x using Quot.ind with | mk c₁ => ?_
    induction y using Quot.ind with | mk c₂ => ?_
    change (c₁.pull _ _).class = (c₂.pull _ _).class at hxy
    rw [TwoCocycle.class_eq_iff hcomm] at hxy
    obtain ⟨z', hz'⟩ := (rel_iff_nval hU' _ _).1 hxy
    change c₁.class = c₂.class
    rw [TwoCocycle.class_eq_iff hcomm, rel_iff_nval hU]
    obtain ⟨z, hz⟩ := split_inj_core (M := Additive G) hA hB hcov hU
      (fun i j k => Additive.ofMul (nval c₂.toTwoCochain i j k) -
        Additive.ofMul (nval c₁.toTwoCochain i j k))
      (fun i j k l h => by
        have e1 := congrArg Additive.ofMul (nval_cocycle hU c₁ i j k l h)
        have e2 := congrArg Additive.ofMul (nval_cocycle hU c₂ i j k l h)
        simp only [ofMul_mul] at e1 e2
        beta_reduce
        rw [sub_add_sub_comm, sub_add_sub_comm, e1, e2])
      (fun x y => Additive.ofMul (z' x y))
      (fun x y z hT => by
        have e := hz' x y z hT
        rw [nval_pull hU _ _ _ x y z hT, nval_pull hU _ _ _ x y z hT] at e
        have e' := congrArg Additive.ofMul e
        simp only [ofMul_mul, ofMul_inv] at e'
        beta_reduce
        rw [e']; abel)
    refine ⟨fun i j => Additive.toMul (z i j), fun i j k h => ?_⟩
    apply Additive.ofMul.injective
    have := hz i j k h
    simp only [ofMul_mul, ofMul_inv, ofMul_toMul]
    linear_combination (norm := abel) this
  · intro x'
    induction x' using Quot.ind with | mk c' => ?_
    obtain ⟨V, u, hV, hVu⟩ := split_surj_core (M := Additive G) hA hB hcov hU
      (fun x y z => Additive.ofMul (nval c'.toTwoCochain x y z))
      (fun x y z w h => by
        have e := congrArg Additive.ofMul (nval_cocycle hU' c' x y z w h)
        simpa only [ofMul_mul] using e)
    let c : TwoCocycle U (contPresheaf X G) := ofNval (fun i j k => Additive.toMul (V i j k))
      (fun i j k l h => by
        apply Additive.ofMul.injective
        simp only [ofMul_mul, ofMul_toMul]
        exact hV i j k l h)
    refine ⟨c.class, ?_⟩
    change (c.pull _ _).class = c'.class
    rw [TwoCocycle.class_eq_iff hcomm, rel_iff_nval hU']
    refine ⟨fun x y => Additive.toMul (-u x y), fun x y z hT => ?_⟩
    have hT' : N3 U (splitR v x) (splitR v y) (splitR v z) := by
      obtain ⟨t, h1, h2, h3⟩ := (n3_iff _ _ _ _).1 hT
      exact (n3_iff U _ _ _).2
        ⟨t, splitFam_le hA hB x h1, splitFam_le hA hB y h2, splitFam_le hA hB z h3⟩
    rw [nval_pull hU _ _ _ x y z hT, nval_ofNval _ _ _ _ _ hT']
    apply Additive.ofMul.injective
    have := hVu x y z hT
    simp only [ofMul_mul, ofMul_inv, ofMul_toMul]
    linear_combination (norm := abel) -this

end QOU.CentralExtension.Cech
