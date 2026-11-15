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

It does not produce the fine covers of the sphere (step P3), so the colimit
statement `HemiComputesCech` stays an open conjecture. Bean `qou-skn4`.

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

end QOU.CentralExtension.Cech
