import QOU.MathlibExt.CechSphereFine
import QOU.MathlibExt.CechSphereComparison

/-!
# The hemisphere cover computes `Ȟ²(S²)` (step C2)

Step P4 of the C2 comparison (route R3, surface case). A box of hemisphere
coordinates with both sides at most `η` has diameter less than `24 η` on the
sphere. By the Lebesgue number lemma, the fine reached box families of
`exists_fine` refine any open cover of `S²`, so every open cover has a good
refinement relative to the hemisphere cover, and `hemiComputesCech_of_good`
gives the instance `HemiComputesCech G` for every discrete commutative
topological group `G`.

This makes `sphereEquiv`, `sphereEquiv_eq_one_iff` and `sphereEquiv_map`, and
the sphere Kummer data built on them, unconditional.

## Results, all sorry-free

* `dist_lt_of_mem_box`: the diameter bound.
* `hasGoodRefinement_sphere`: every open cover of `S²` has a good refinement.
* `instance : HemiComputesCech G`.
* `kummerSurfaceData_sphere'`: `KummerSurfaceData` on `S²` over all open covers,
  with no hypothesis.

-- Ref: [manuscript] lifting-and-descent, route R3, surface step C2
Bean `qou-skn4`.
-/
open CategoryTheory TopologicalSpace
namespace QOU.CentralExtension.Cech

local notation "E3" => EuclideanSpace ℝ (Fin 3)
open CechGerbe

/-! ### Diameter of a small box -/

theorem tsgn_sq (i : Fin 4) (k : Fin 3) : tsgn i k ^ 2 = 1 := by
  fin_cases i <;> fin_cases k <;> simp [tsgn]

theorem abs_coord_le_one (p : S2) (k : Fin 3) : |p.1 k| ≤ 1 := by
  have hs := sphere_sq p
  rw [abs_le]
  fin_cases k <;> simp <;> constructor <;> nlinarith [sq_nonneg (p.1 0), sq_nonneg (p.1 1),
    sq_nonneg (p.1 2)]

theorem abs_tsgn (i : Fin 4) (k : Fin 3) : |tsgn i k| = 1 := by
  rcases sq_eq_one_iff.1 (tsgn_sq i k) with h | h <;> simp [h]

theorem mul_le_one_of_tsgn (i : Fin 4) (k : Fin 3) (p : S2) : tsgn i k * p.1 k ≤ 1 := by
  have h := abs_coord_le_one p k
  calc tsgn i k * p.1 k ≤ |tsgn i k * p.1 k| := le_abs_self _
    _ = |p.1 k| := by rw [abs_mul, abs_tsgn, one_mul]
    _ ≤ 1 := h

theorem tfun_le_three (i : Fin 4) (p : S2) : tfun i p.1 ≤ 3 := by
  rw [tfun_apply]
  linarith [mul_le_one_of_tsgn i 0 p, mul_le_one_of_tsgn i 1 p, mul_le_one_of_tsgn i 2 p]

/-- Two unit vectors that are positive multiples `x = s • a`, `y = s' • b`. -/
theorem norm_sub_le_of_rescale {x y a b : E3} {s s' : ℝ} (hs : 0 < s) (hs' : 0 < s')
    (hx : ‖x‖ = 1) (hy : ‖y‖ = 1) (ha : x = s • a) (hb : y = s' • b) :
    ‖x - y‖ ≤ 2 * s * ‖a - b‖ := by
  have hna : ‖a‖ = 1 / s := by
    rw [ha, norm_smul, Real.norm_eq_abs, abs_of_pos hs] at hx
    field_simp; linarith
  have hnb : ‖b‖ = 1 / s' := by
    rw [hb, norm_smul, Real.norm_eq_abs, abs_of_pos hs'] at hy
    field_simp; linarith
  have e : x - y = s • (a - b) + (s - s') • b := by
    rw [ha, hb, smul_sub, sub_smul]; abel
  have h2 : ‖(s - s') • b‖ ≤ s * ‖a - b‖ := by
    rw [norm_smul, Real.norm_eq_abs, hnb]
    have hk : |s - s'| * (1 / s') = s * |1 / s' - 1 / s| := by
      rw [show 1 / s' - 1 / s = (s - s') / (s * s') by field_simp]
      rw [abs_div, abs_mul, abs_of_pos hs, abs_of_pos hs']
      field_simp
    rw [hk]
    have := abs_norm_sub_norm_le b a
    rw [hna, hnb, ← norm_neg (b - a), neg_sub] at this
    exact mul_le_mul_of_nonneg_left this hs.le
  calc ‖x - y‖ = ‖s • (a - b) + (s - s') • b‖ := by rw [e]
    _ ≤ ‖s • (a - b)‖ + ‖(s - s') • b‖ := norm_add_le _ _
    _ ≤ s * ‖a - b‖ + s * ‖a - b‖ := by
        rw [norm_smul, Real.norm_eq_abs, abs_of_pos hs]; linarith
    _ = 2 * s * ‖a - b‖ := by ring

theorem norm_le_sum_abs (v : E3) : ‖v‖ ≤ |v 0| + |v 1| + |v 2| := by
  have h := norm_sq_three v
  have hn := norm_nonneg v
  have : ‖v‖ ^ 2 ≤ (|v 0| + |v 1| + |v 2|) ^ 2 := by
    rw [h]
    nlinarith [sq_abs (v 0), sq_abs (v 1), sq_abs (v 2), abs_nonneg (v 0), abs_nonneg (v 1),
      abs_nonneg (v 2), mul_nonneg (abs_nonneg (v 0)) (abs_nonneg (v 1)),
      mul_nonneg (abs_nonneg (v 0)) (abs_nonneg (v 2)),
      mul_nonneg (abs_nonneg (v 1)) (abs_nonneg (v 2))]
  exact (pow_le_pow_iff_left₀ hn (by positivity) two_ne_zero).1 this

/-- **Diameter bound.** Two points of a box whose sides are below `η` are less
than `24 η` apart. -/
theorem dist_lt_of_mem_box {i : Fin 4} {a b c d η : ℝ} (hab : a < b) (hL : b - a ≤ η)
    (hM : d - c ≤ η) {p p' : S2} (hp : p ∈ box i a b c d) (hp' : p' ∈ box i a b c d) :
    dist p p' < 24 * η := by
  have ht := tfun_pos_of_mem_box hab hp
  have ht' := tfun_pos_of_mem_box hab hp'
  set s := tfun i p.1
  set s' := tfun i p'.1
  obtain ⟨h1, h2, h3, h4⟩ := mem_box.1 hp
  obtain ⟨h1', h2', h3', h4'⟩ := mem_box.1 hp'
  set A : E3 := s⁻¹ • p.1
  set B : E3 := s'⁻¹ • p'.1
  have hA : p.1 = s • A := by simp [A, smul_smul, mul_inv_cancel₀ ht.ne']
  have hB : p'.1 = s' • B := by simp [B, smul_smul, mul_inv_cancel₀ ht'.ne']
  have hx : ‖p.1‖ = 1 := mem_sphere_zero_iff_norm.1 p.2
  have hy : ‖p'.1‖ = 1 := mem_sphere_zero_iff_norm.1 p'.2
  -- coordinates of `A` and `B`
  have cA : ∀ k, A k = p.1 k / s := fun k => by simp [A, div_eq_inv_mul]
  have cB : ∀ k, B k = p'.1 k / s' := fun k => by simp [B, div_eq_inv_mul]
  have d0 : |A 0 - B 0| < η := by
    rw [cA, cB, abs_lt]
    have u1 : a < p.1 0 / s := by rw [lt_div_iff₀ ht]; linarith
    have u2 : p.1 0 / s < b := by rw [div_lt_iff₀ ht]; linarith
    have v1 : a < p'.1 0 / s' := by rw [lt_div_iff₀ ht']; linarith
    have v2 : p'.1 0 / s' < b := by rw [div_lt_iff₀ ht']; linarith
    constructor <;> linarith
  have d1 : |A 1 - B 1| < η := by
    rw [cA, cB, abs_lt]
    have u1 : c < p.1 1 / s := by rw [lt_div_iff₀ ht]; linarith
    have u2 : p.1 1 / s < d := by rw [div_lt_iff₀ ht]; linarith
    have v1 : c < p'.1 1 / s' := by rw [lt_div_iff₀ ht']; linarith
    have v2 : p'.1 1 / s' < d := by rw [div_lt_iff₀ ht']; linarith
    constructor <;> linarith
  -- `tfun i A = 1 = tfun i B` pins the third coordinate
  have tA : tfun i A = 1 := by
    simp only [A, map_smul, smul_eq_mul]; exact inv_mul_cancel₀ ht.ne'
  have tB : tfun i B = 1 := by
    simp only [B, map_smul, smul_eq_mul]; exact inv_mul_cancel₀ ht'.ne'
  rw [tfun_apply] at tA tB
  have d2 : |A 2 - B 2| < 2 * η := by
    have e : tsgn i 2 * (A 2 - B 2) = -(tsgn i 0 * (A 0 - B 0) + tsgn i 1 * (A 1 - B 1)) := by
      linarith
    have habs : ∀ k, |tsgn i k| = 1 := abs_tsgn i
    have := congrArg abs e
    rw [abs_mul, habs, one_mul, abs_neg] at this
    rw [this]
    calc |tsgn i 0 * (A 0 - B 0) + tsgn i 1 * (A 1 - B 1)|
        ≤ |tsgn i 0 * (A 0 - B 0)| + |tsgn i 1 * (A 1 - B 1)| := abs_add_le _ _
      _ = |A 0 - B 0| + |A 1 - B 1| := by rw [abs_mul, abs_mul, habs, habs, one_mul, one_mul]
      _ < 2 * η := by linarith
  have hAB : ‖A - B‖ < 4 * η := by
    have := norm_le_sum_abs (A - B)
    simp only [PiLp.sub_apply] at this
    linarith
  have hbound := norm_sub_le_of_rescale ht ht' hx hy hA hB
  have hs3 : s ≤ 3 := tfun_le_three i p
  rw [Subtype.dist_eq, dist_eq_norm]
  calc ‖p.1 - p'.1‖ ≤ 2 * s * ‖A - B‖ := hbound
    _ ≤ 2 * 3 * ‖A - B‖ := by gcongr
    _ < 2 * 3 * (4 * η) := by linarith [norm_nonneg (A - B)]
    _ = 24 * η := by ring

/-! ### Good refinements and the instance -/

variable (G : Type) [TopologicalSpace G] [CommGroup G] [IsTopologicalGroup G] [DiscreteTopology G]

/-- **Every open cover of `S²` has a good refinement** relative to the hemispheres. -/
theorem hasGoodRefinement_sphere (𝒱 : Cover.{0} (⊤ : Opens S2)) (h𝒱 : IsOpenCover 𝒱) :
    HasGoodRefinement (IsOpenCover (X := S2)) (tetCover hemi) (contPresheaf S2 G) 𝒱 := by
  have hcov : (Set.univ : Set S2) ⊆ ⋃ i, ((𝒱.obj i : Opens S2) : Set S2) := by
    intro x _
    obtain ⟨i, hi⟩ := Opens.mem_iSup.1 (h𝒱 (Set.mem_univ x))
    exact Set.mem_iUnion.2 ⟨i, hi⟩
  obtain ⟨δ, hδ, hleb⟩ := lebesgue_number_lemma_of_metric isCompact_univ
    (fun i => (𝒱.obj i).isOpen) hcov
  have hne : Nonempty 𝒱.ι := by
    obtain ⟨i, -⟩ := Set.mem_iUnion.1 (hcov (Set.mem_univ (vpt 0)))
    exact ⟨i⟩
  obtain ⟨κ, _, D, ⟨r, hr, hbij⟩, hc, hL, hM⟩ :=
    exists_fine (G := G) (show 0 < δ / 24 by positivity)
  -- each box lies in some member of `𝒱`
  have hsub : ∀ j, ∃ i, D.fam j ≤ 𝒱.obj i := by
    intro j
    by_cases hj : ∃ p, p ∈ D.fam j
    · obtain ⟨p, hp⟩ := hj
      obtain ⟨i, hi⟩ := hleb p (Set.mem_univ p)
      refine ⟨i, fun q hq => hi ?_⟩
      rw [Metric.mem_ball]
      have := dist_lt_of_mem_box (D.hab j) (hL j) (hM j) hq hp
      linarith
    · push_neg at hj
      exact ⟨hne.some, fun q hq => absurd hq (hj q)⟩
  choose ρ hρ using hsub
  let W : Cover.{0} (⊤ : Opens S2) := ⟨κ, D.fam, fun _ => homOfLE le_top⟩
  have hW : IsOpenCover W := by
    intro x _
    obtain ⟨j, hj⟩ := hc x
    exact Opens.mem_iSup.2 ⟨j, hj⟩
  refine ⟨W, hW, ⟨⟨ρ, fun j => homOfLE (hρ j), fun _ => Subsingleton.elim _ _⟩⟩,
    ⟨r, fun j => homOfLE (hr j), fun _ => Subsingleton.elim _ _⟩, ?_⟩
  exact hbij

/-- **C2: the four-hemisphere cover computes `Ȟ²(S², G)`.** -/
instance hemiComputesCech_inst : HemiComputesCech G :=
  hemiComputesCech_of_good G (hasGoodRefinement_sphere G)

/-- **C3, now unconditional.** The 2-sphere carries `KummerSurfaceData` over all
open covers. -/
noncomputable def kummerSurfaceData_sphere' (n : ℕ) [NeZero n] :
    KummerSurfaceData S2 n (IsOpenCover (X := S2)) :=
  kummerSurfaceData_sphere n

end QOU.CentralExtension.Cech
