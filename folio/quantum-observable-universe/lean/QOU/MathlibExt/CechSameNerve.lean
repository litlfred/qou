import QOU.MathlibExt.CechSplit

/-!
# Shrinking a cover without changing its nerve leaves Čech `H²` unchanged

Step P3a of the C2 comparison (route R3, surface case). Let `U : ι → Opens X` and
`V : κ → Opens X` be families with preconnected pairwise and triple
intersections, and let `e : κ ≃ ι` with `V j ≤ U (e j)`. If every nonempty
triple and quadruple intersection of `U` stays nonempty after shrinking to `V`
(the converse is automatic), the two nerves agree, and pulling back along `e`
is a bijection on `H²` with discrete commutative coefficients.

Two uses: shrinking each hemisphere to a bounded box (same index), and
re-indexing a family along an equivalence (`V j = U (e j)`).

## Results, all sorry-free

* `sameNerve_pull_bijective`.
* `reindex_pull_bijective`: the case `V j = U (e j)`.

-- Ref: [manuscript] lifting-and-descent, route R3, surface step C2
Bean `qou-skn4`.
-/
open CategoryTheory Opposite TopologicalSpace
namespace QOU.CentralExtension.Cech
open CechGerbe

variable {X : Type} [TopologicalSpace X]
variable {G : Type} [TopologicalSpace G] [CommGroup G] [IsTopologicalGroup G]
  [DiscreteTopology G]
variable {ι κ : Type} {U : ι → Opens X} {V : κ → Opens X}

/-- **Same nerve, same `H²`.** -/
theorem sameNerve_pull_bijective (e : κ ≃ ι) (hle : ∀ j, V j ≤ U (e j))
    (hU : ConnFamily U) (hV : ConnFamily V)
    (h3 : ∀ i j k, N3 U (e i) (e j) (e k) → N3 V i j k)
    (h4 : ∀ i j k l, N4 U (e i) (e j) (e k) (e l) → N4 V i j k l) :
    Function.Bijective (H2.pull (𝒜 := contPresheaf X G) (U := U) e
      (fun j => homOfLE (hle j))) := by
  have hcomm := contPresheaf_comm (X := X) (G := G)
  have h3' : ∀ i j k : ι, N3 U i j k → N3 V (e.symm i) (e.symm j) (e.symm k) := by
    intro i j k h; apply h3; simpa using h
  constructor
  · intro x y hxy
    induction x using Quot.ind with | mk c₁ => ?_
    induction y using Quot.ind with | mk c₂ => ?_
    change (c₁.pull _ _).class = (c₂.pull _ _).class at hxy
    rw [TwoCocycle.class_eq_iff hcomm] at hxy
    obtain ⟨w, hw⟩ := (rel_iff_nval hV _ _).1 hxy
    change c₁.class = c₂.class
    rw [TwoCocycle.class_eq_iff hcomm, rel_iff_nval hU]
    refine ⟨fun a b => w (e.symm a) (e.symm b), fun a b c hT => ?_⟩
    have hT' := h3' a b c hT
    have := hw _ _ _ hT'
    rw [nval_pull hU _ _ _ _ _ _ hT', nval_pull hU _ _ _ _ _ _ hT'] at this
    simpa using this
  · intro x'
    induction x' using Quot.ind with | mk c' => ?_
    let W : ι → ι → ι → G := fun a b c => nval c'.toTwoCochain (e.symm a) (e.symm b) (e.symm c)
    have hW : ∀ a b c d, N4 U a b c d → W a b c * W a c d = W b c d * W a b d := by
      intro a b c d h
      exact nval_cocycle hV c' _ _ _ _ (h4 _ _ _ _ (by simpa using h))
    let c : TwoCocycle U (contPresheaf X G) := ofNval W hW
    refine ⟨c.class, ?_⟩
    change (c.pull _ _).class = c'.class
    rw [TwoCocycle.class_eq_iff hcomm, rel_iff_nval hV]
    refine ⟨fun _ _ => 1, fun i j k hT => ?_⟩
    have hT' : N3 U (e i) (e j) (e k) := by
      obtain ⟨t, h1, h2, h3⟩ := (n3_iff _ _ _ _).1 hT
      exact (n3_iff U _ _ _).2 ⟨t, hle i h1, hle j h2, hle k h3⟩
    rw [nval_pull hU _ _ _ _ _ _ hT, nval_ofNval _ _ _ _ _ hT']
    simp [W]

/-- **Re-indexing along an equivalence keeps `H²`.** -/
theorem reindex_pull_bijective (e : κ ≃ ι) (hVU : ∀ j, V j = U (e j)) (hU : ConnFamily U) :
    Function.Bijective (H2.pull (𝒜 := contPresheaf X G) (U := U) e
      (fun j => homOfLE (hVU j).le)) := by
  have hV : ConnFamily V := ⟨fun i j k => by rw [hVU, hVU, hVU]; exact hU.pre3 _ _ _,
    fun i j => by rw [hVU, hVU]; exact hU.pre2 _ _⟩
  refine sameNerve_pull_bijective e (fun j => (hVU j).le) hU hV (fun i j k h => ?_)
    (fun i j k l h => ?_)
  · simpa only [N3, hVU] using h
  · simpa only [N4, hVU] using h

end QOU.CentralExtension.Cech
