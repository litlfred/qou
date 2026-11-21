import Mathlib.CategoryTheory.Groupoid.Subgroupoid
import Mathlib.AlgebraicTopology.FundamentalGroupoid.SimplyConnected
import Mathlib.Analysis.Convex.Contractible
import Mathlib.Topology.MetricSpace.Pseudo.Lemmas

/-!
# A Lebesgue-number lemma for subgroupoids of the fundamental groupoid

Let `S` be a subgroupoid of the fundamental groupoid of `X`, and `R i` open sets.  If every path
lying inside a single `R i` has its class in `S`, then so does every path whose points all lie in
`⋃ R i` (`Subgroupoid.mem_of_locally`).

The proof subdivides `[0,1]` at a Lebesgue number of the cover `γ⁻¹(R i)`.  Sub-paths are the
images of straight segments of `[0,1]`; since `[0,1]` is simply connected, any two of them with
the same ends are homotopic, so no explicit reparametrisation is needed.
-/

set_option autoImplicit false

namespace QOU.MathlibExt

open CategoryTheory Set unitInterval Metric

/-- The straight segment from `s` to `t` in `[0,1]`. -/
def segI (s t : I) : Path s t where
  toFun u := ⟨(1 - (u : ℝ)) * s + u * t, by
    constructor
    · exact add_nonneg (mul_nonneg (sub_nonneg.2 u.2.2) s.2.1) (mul_nonneg u.2.1 t.2.1)
    · nlinarith [u.2.1, u.2.2, s.2.1, s.2.2, t.2.1, t.2.2]⟩
  continuous_toFun := Continuous.subtype_mk (by fun_prop) _
  source' := by ext; simp
  target' := by ext; simp

lemma segI_apply (s t u : I) : (segI s t u : ℝ) = (1 - (u : ℝ)) * s + u * t := rfl

instance : SimplyConnectedSpace I :=
  haveI : ContractibleSpace I := (convex_Icc (0 : ℝ) 1).contractibleSpace (nonempty_Icc.2 zero_le_one)
  inferInstance

variable {X : Type*} [TopologicalSpace X]

/-- The class of a path as an arrow of the fundamental groupoid. -/
def pathHom {x y : X} (p : Path x y) : FundamentalGroupoid.mk x ⟶ FundamentalGroupoid.mk y := ⟦p⟧

/-- The sub-path of `f` from `f s` to `f t`. -/
def subPath (f : C(I, X)) (s t : I) : Path (f s) (f t) := (segI s t).map f.continuous

theorem subPath_trans (f : C(I, X)) (s t u : I) :
    ((subPath f s t).trans (subPath f t u)).Homotopic (subPath f s u) := by
  unfold subPath
  rw [← Path.map_trans]
  exact (SimplyConnectedSpace.paths_homotopic _ _).map f


/-- Two paths in a subspace `T` with all points in a simply connected `s ⊆ T` are homotopic. -/
theorem homotopic_of_mem {E : Type*} [TopologicalSpace E] {T s : Set E} (hsT : s ⊆ T)
    [SimplyConnectedSpace s] {x y : T} (p q : Path x y) (hp : ∀ t, (p t : E) ∈ s)
    (hq : ∀ t, (q t : E) ∈ s) : p.Homotopic q := by
  have hx : (x : E) ∈ s := by simpa using hp 0
  have hy : (y : E) ∈ s := by simpa using hp 1
  let lift : ∀ r : Path x y, (∀ t, (r t : E) ∈ s) → Path (⟨x, hx⟩ : s) ⟨y, hy⟩ := fun r hr =>
    { toFun := fun t => ⟨r t, hr t⟩
      continuous_toFun := (continuous_subtype_val.comp r.continuous).subtype_mk _
      source' := Subtype.ext (by simp)
      target' := Subtype.ext (by simp) }
  let ι : C(s, T) := ⟨fun z => ⟨z.1, hsT z.2⟩, continuous_subtype_val.subtype_mk _⟩
  have h := (SimplyConnectedSpace.paths_homotopic (lift p hp) (lift q hq)).map ι
  have e1 : (lift p hp).map ι.continuous = p := Path.ext rfl
  have e2 : (lift q hq).map ι.continuous = q := Path.ext rfl
  rwa [e1, e2] at h

/-- The conjugate of a subgroupoid by a family of anchors `α x : b x ⟶ x`. -/
def Subgroupoid.conjAnchor {G : Type*} [Groupoid G] (S : Subgroupoid G) (b : G → G)
    (α : ∀ x, b x ⟶ x) : Subgroupoid G where
  arrows x y := {p | α x ≫ p ≫ Groupoid.inv (α y) ∈ S.arrows (b x) (b y)}
  inv := by
    intro x y p hp
    simp only [Set.mem_setOf_eq] at hp ⊢
    have := S.inv hp
    simp only [Groupoid.inv_eq_inv] at this ⊢
    convert this using 1
    simp [Category.assoc]
  mul := by
    intro x y z p hp q hq
    simp only [Set.mem_setOf_eq] at hp hq ⊢
    have := S.mul hp hq
    simp only [Groupoid.inv_eq_inv] at this ⊢
    convert this using 1
    simp [Category.assoc]

namespace Subgroupoid

/-- Membership depends only on the underlying map of a path. -/
theorem mem_of_coe_eq (S : Subgroupoid (FundamentalGroupoid X)) {x y x' y' : X} (p : Path x y)
    (q : Path x' y') (hx : x = x') (hy : y = y') (h : ⇑p = ⇑q)
    (hp : (⟦p⟧ : FundamentalGroupoid.mk x ⟶ FundamentalGroupoid.mk y) ∈ S.arrows _ _) :
    (⟦q⟧ : FundamentalGroupoid.mk x' ⟶ FundamentalGroupoid.mk y') ∈ S.arrows _ _ := by
  subst hx hy
  rwa [show q = p from Path.ext h.symm]

/-- **Lebesgue lemma for subgroupoids.** -/
theorem mem_of_locally (S : Subgroupoid (FundamentalGroupoid X)) {ι : Sort*} (R : ι → Set X)
    (hR : ∀ i, IsOpen (R i))
    (hloc : ∀ i {x y : X} (p : Path x y), (∀ t, p t ∈ R i) →
      (⟦p⟧ : FundamentalGroupoid.mk x ⟶ FundamentalGroupoid.mk y) ∈ S.arrows _ _)
    {x y : X} (γ : Path x y) (hγ : ∀ t, ∃ i, γ t ∈ R i) :
    (⟦γ⟧ : FundamentalGroupoid.mk x ⟶ FundamentalGroupoid.mk y) ∈ S.arrows _ _ := by
  set f : C(I, X) := γ.toContinuousMap with hf
  obtain ⟨δ, hδ, hball⟩ := lebesgue_number_lemma_of_metric (s := (univ : Set I)) isCompact_univ
    (c := fun i => f ⁻¹' R i) (fun i => (hR i).preimage f.continuous)
    (fun t _ => mem_iUnion.2 (hγ t))
  have hlocal : ∀ s t : I, dist s t < δ →
      pathHom (subPath f s t) ∈
        S.arrows _ _ := by
    intro s t hst
    obtain ⟨i, hi⟩ := hball s (mem_univ _)
    refine hloc i _ fun u => hi ?_
    rw [mem_ball, Subtype.dist_eq, Real.dist_eq, segI_apply]
    rw [Subtype.dist_eq, Real.dist_eq] at hst
    have h1 : (1 - (u : ℝ)) * s + u * t - s = u * (t - s) := by ring
    rw [h1, abs_mul, abs_of_nonneg u.2.1, abs_sub_comm]
    calc (u : ℝ) * |(s : ℝ) - t| ≤ 1 * |(s : ℝ) - t| :=
          mul_le_mul_of_nonneg_right u.2.2 (abs_nonneg _)
      _ < δ := by rw [one_mul]; exact hst
  have hind : ∀ k : ℕ, ∀ t : I, (t : ℝ) ≤ k * (δ / 2) →
      pathHom (subPath f 0 t) ∈
        S.arrows _ _ := by
    intro k
    induction k with
    | zero =>
      intro t ht
      refine hlocal 0 t ?_
      rw [Subtype.dist_eq, Real.dist_eq]
      simp only [Nat.cast_zero, zero_mul] at ht
      have := t.2.1
      simp only [Icc.coe_zero, zero_sub, abs_neg]
      rw [abs_of_nonneg this]; linarith
    | succ k ih =>
      intro t ht
      set s : I := ⟨max ((t : ℝ) - δ / 2) 0, le_max_right _ _,
        max_le (by linarith [t.2.2]) zero_le_one⟩ with hs
      have hs1 : (s : ℝ) ≤ k * (δ / 2) := by
        show max ((t : ℝ) - δ / 2) 0 ≤ k * (δ / 2)
        refine max_le ?_ (by positivity)
        push_cast at ht; linarith
      have hst : dist s t < δ := by
        rw [Subtype.dist_eq, Real.dist_eq]
        show |max ((t : ℝ) - δ / 2) 0 - t| < δ
        rw [abs_lt]; constructor
        · linarith [le_max_left ((t : ℝ) - δ / 2) 0]
        · have := t.2.1
          rcases le_total ((t : ℝ) - δ / 2) 0 with h | h
          · rw [max_eq_right h]; linarith
          · rw [max_eq_left h]; linarith
      have heq : pathHom (subPath f 0 s) ≫
            pathHom (subPath f s t) =
          pathHom (subPath f 0 t) := by
        simp only [pathHom]
        rw [FundamentalGroupoid.comp_eq, ← Path.Homotopic.comp_lift]
        exact Quotient.sound (subPath_trans f 0 s t)
      rw [← heq]
      exact S.mul (ih s hs1) (hlocal s t hst)
  obtain ⟨k, hk⟩ := exists_nat_ge (2 / δ)
  have h1 : ((1 : I) : ℝ) ≤ k * (δ / 2) := by
    rw [Icc.coe_one]
    calc (1 : ℝ) = 2 / δ * (δ / 2) := by field_simp
      _ ≤ k * (δ / 2) := mul_le_mul_of_nonneg_right hk (by positivity)
  refine mem_of_coe_eq S _ γ γ.source γ.target ?_ (hind k 1 h1)
  funext u
  show γ (segI 0 1 u) = γ u
  congr 1; ext; simp [segI_apply]

end Subgroupoid

end QOU.MathlibExt
