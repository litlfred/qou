/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLCollinear
import Mathlib.Analysis.Normed.Module.Basic
import Mathlib.Topology.Compactness.Compact
import Mathlib.Topology.Algebra.Module.Basic

set_option autoImplicit false

/-!
# Robustness of Δ-move conditions (issue #8902, isotopy-to-Δ bridge, local stability part 1)

A Δ-move asks that a triangle meet the link only in one edge. Every such condition splits into
two kinds of statement about a segment `e` and a triangle `T`:

* `e ∩ T = ∅`, for edges far from the triangle;
* `e ∩ T ⊆ {o}`, for an edge that shares the vertex `o` with the triangle.

This file proves that both kinds **survive small motions** of all the points involved, as long as
the triangle does not degenerate at the shared vertex. That is what makes "every sufficiently
small perturbation of a link is Δ-equivalent to it" provable with a compactness argument rather
than with explicit angle estimates.

## What is a DEFINITION here

* `triParams` — the parameter triangle `{(s, t) | 0 ≤ s, 0 ≤ t, s + t ≤ 1}`.
* `triPt a b c (s, t) = a + s • (b - a) + t • (c - a)`.

## What is a THEOREM here

* `isCompact_triParams`, `convexHull_triple_eq_image` — the triangle is the compact image
  `triPt a b c '' triParams`.
* `eventually_forall_mem_of_isCompact` — an open condition holding over a compact parameter set at
  `x₀` holds over it for all `x` near `x₀`.
* `eventually_segment_inter_convexHull_eq_empty` — disjointness persists.
* `eventually_segment_inter_convexHull_subset` — touching only at a shared vertex `o` persists,
  given `o ∉ [y, z]` and `w ≠ o`.
-/

namespace QOU.MathlibExt.PL

open Set Filter Topology

section
variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

/-- The closed triangle of parameters `s, t ≥ 0`, `s + t ≤ 1`. -/
def triParams : Set (ℝ × ℝ) := {p | 0 ≤ p.1 ∧ 0 ≤ p.2 ∧ p.1 + p.2 ≤ 1}

lemma isCompact_triParams : IsCompact triParams := by
  refine ((isCompact_Icc (a := (0:ℝ)) (b := 1)).prod
    (isCompact_Icc (a := (0:ℝ)) (b := 1))).of_isClosed_subset ?_ ?_
  · exact (isClosed_le continuous_const continuous_fst).inter
      ((isClosed_le continuous_const continuous_snd).inter
        (isClosed_le (continuous_fst.add continuous_snd) continuous_const))
  · rintro ⟨s, t⟩ ⟨hs, ht, hst⟩
    exact ⟨⟨hs, by linarith⟩, ⟨ht, by linarith⟩⟩

/-- The triangle with vertices `a, b, c`, parametrized. -/
def triPt (a b c : E) (p : ℝ × ℝ) : E := a + p.1 • (b - a) + p.2 • (c - a)

lemma convexHull_triple_eq_image (a b c : E) :
    convexHull ℝ {a, b, c} = triPt a b c '' triParams := by
  apply Subset.antisymm
  · refine convexHull_min ?_ ?_
    · intro x hx
      rcases hx with rfl | rfl | rfl
      · exact ⟨(0, 0), ⟨le_rfl, le_rfl, by norm_num⟩, by simp [triPt]⟩
      · exact ⟨(1, 0), ⟨by norm_num, le_rfl, by norm_num⟩, by simp [triPt]⟩
      · exact ⟨(0, 1), ⟨le_rfl, by norm_num, by norm_num⟩, by simp [triPt]⟩
    · intro x hx y hy α β hα hβ hαβ
      obtain ⟨⟨s, t⟩, ⟨hs, ht, hst⟩, rfl⟩ := hx
      obtain ⟨⟨s', t'⟩, ⟨hs', ht', hst'⟩, rfl⟩ := hy
      refine ⟨(α * s + β * s', α * t + β * t'), ⟨by positivity, by positivity, ?_⟩, ?_⟩
      · nlinarith
      · simp only [triPt, smul_add, add_smul, smul_smul]
        rw [show (α : ℝ) = 1 - β by linarith]
        simp only [sub_smul, one_smul]; abel
  · rintro _ ⟨⟨s, t⟩, ⟨hs, ht, hst⟩, rfl⟩
    have hconv := convex_convexHull ℝ ({a, b, c} : Set E)
    have ha : a ∈ convexHull ℝ ({a, b, c} : Set E) := subset_convexHull ℝ _ (by simp)
    have hb : b ∈ convexHull ℝ ({a, b, c} : Set E) := subset_convexHull ℝ _ (by simp)
    have hc : c ∈ convexHull ℝ ({a, b, c} : Set E) := subset_convexHull ℝ _ (by simp)
    by_cases h0 : s + t = 0
    · have hs0 : s = 0 := by linarith
      have ht0 : t = 0 := by linarith
      subst hs0 ht0; simpa [triPt] using ha
    · have hpos : 0 < s + t := lt_of_le_of_ne (by linarith) (Ne.symm h0)
      have hy : (s / (s + t)) • b + (t / (s + t)) • c ∈ convexHull ℝ ({a, b, c} : Set E) :=
        hconv hb hc (by positivity) (by positivity) (by field_simp)
      have := hconv ha hy (by linarith : 0 ≤ 1 - (s + t)) hpos.le (by ring)
      convert this using 1
      simp only [triPt, smul_add, smul_smul, sub_smul, smul_sub, one_smul]
      field_simp
      module

/-- **Compactness.** If `F x₀ y` lies in an open set for every `y` in a compact `K`, the same holds
for all `x` near `x₀`. -/
theorem eventually_forall_mem_of_isCompact {X Y Z : Type*} [TopologicalSpace X]
    [TopologicalSpace Y] [TopologicalSpace Z] {x₀ : X} {K : Set Y} (hK : IsCompact K)
    {F : X → Y → Z} (hF : Continuous (Function.uncurry F)) {U : Set Z} (hU : IsOpen U)
    (h : ∀ y ∈ K, F x₀ y ∈ U) : ∀ᶠ x in 𝓝 x₀, ∀ y ∈ K, F x y ∈ U :=
  hK.eventually_forall_of_forall_eventually fun y hy =>
    hF.continuousAt.eventually_mem (hU.mem_nhds (h y hy))

variable {X : Type*} [TopologicalSpace X] {x₀ : X}

/-- **A segment and a triangle that are disjoint stay disjoint** under small motions of their
endpoints and vertices. -/
theorem eventually_segment_inter_convexHull_eq_empty {a b p q r : X → E}
    (ha : Continuous a) (hb : Continuous b) (hp : Continuous p) (hq : Continuous q)
    (hr : Continuous r)
    (h : segment ℝ (a x₀) (b x₀) ∩ convexHull ℝ {p x₀, q x₀, r x₀} = ∅) :
    ∀ᶠ x in 𝓝 x₀, segment ℝ (a x) (b x) ∩ convexHull ℝ {p x, q x, r x} = ∅ := by
  let F : X → ℝ × (ℝ × ℝ) → E := fun x y =>
    (a x + y.1 • (b x - a x)) - triPt (p x) (q x) (r x) y.2
  have hF : Continuous (Function.uncurry F) := by
    simp only [F, triPt, Function.uncurry_def]
    fun_prop
  have key := eventually_forall_mem_of_isCompact (isCompact_Icc.prod isCompact_triParams) hF
    isOpen_ne (x₀ := x₀) (U := {z : E | z ≠ 0}) (by
      rintro ⟨u, st⟩ ⟨hu, hst⟩ h0
      have h0 : a x₀ + u • (b x₀ - a x₀) = triPt (p x₀) (q x₀) (r x₀) st := sub_eq_zero.mp h0
      have h1 : a x₀ + u • (b x₀ - a x₀) ∈ segment ℝ (a x₀) (b x₀) := by
        rw [segment_eq_image']; exact ⟨u, hu, rfl⟩
      have h2 : a x₀ + u • (b x₀ - a x₀) ∈ convexHull ℝ {p x₀, q x₀, r x₀} := by
        rw [convexHull_triple_eq_image, h0]; exact ⟨st, hst, rfl⟩
      have : a x₀ + u • (b x₀ - a x₀) ∈ (∅ : Set E) := h ▸ ⟨h1, h2⟩
      exact this)
  filter_upwards [key] with x hx
  refine eq_empty_iff_forall_notMem.mpr fun v ⟨hv1, hv2⟩ => ?_
  rw [segment_eq_image'] at hv1
  rw [convexHull_triple_eq_image] at hv2
  obtain ⟨u, hu, rfl⟩ := hv1
  obtain ⟨st, hst, hst'⟩ := hv2
  exact hx (u, st) ⟨hu, hst⟩ (sub_eq_zero.mpr hst'.symm)

/-- **A segment that touches a triangle only at a shared vertex keeps doing so** under small
motions, provided the triangle does not degenerate at that vertex (`o ∉ [y, z]`) and the segment
does not collapse (`w ≠ o`). -/
theorem eventually_segment_inter_convexHull_subset {o w y z : X → E}
    (ho : Continuous o) (hw : Continuous w) (hy : Continuous y) (hz : Continuous z)
    (h1 : segment ℝ (o x₀) (w x₀) ∩ convexHull ℝ {o x₀, y x₀, z x₀} ⊆ {o x₀})
    (h2 : o x₀ ∉ segment ℝ (y x₀) (z x₀)) (h3 : w x₀ ≠ o x₀) :
    ∀ᶠ ξ in 𝓝 x₀, segment ℝ (o ξ) (w ξ) ∩ convexHull ℝ {o ξ, y ξ, z ξ} ⊆ {o ξ} := by
  let G : X → ℝ → E := fun ξ l => l • (y ξ - o ξ) + (1 - l) • (z ξ - o ξ)
  have hG : Continuous (Function.uncurry G) := by
    simp only [G, Function.uncurry_def]; fun_prop
  -- step 1: `G x₀` does not vanish on `[0, 1]`
  have hG0 : ∀ l ∈ Icc (0 : ℝ) 1, G x₀ l ≠ 0 := by
    intro l ⟨hl0, hl1⟩ h0
    apply h2
    rw [segment_eq_image]
    refine ⟨1 - l, ⟨by linarith, by linarith⟩, ?_⟩
    have : l • (y x₀ - o x₀) + (1 - l) • (z x₀ - o x₀) = 0 := h0
    have e : (1 - (1 - l)) • y x₀ + (1 - l) • z x₀ = o x₀ + (l • (y x₀ - o x₀) +
        (1 - l) • (z x₀ - o x₀)) := by module
    show (1 - (1 - l)) • y x₀ + (1 - l) • z x₀ = o x₀
    rw [e, this, add_zero]
  -- step 2: a positive lower bound at `x₀`
  obtain ⟨l₀, hl₀, hmin⟩ := (isCompact_Icc (a := (0 : ℝ)) (b := 1)).exists_isMinOn
    ⟨0, le_rfl, zero_le_one⟩ (hG.comp (Continuous.prodMk_right x₀)).norm.continuousOn
  set m₀ := ‖G x₀ l₀‖ with hm₀
  have hm₀pos : 0 < m₀ := norm_pos_iff.mpr (hG0 l₀ hl₀)
  have hbound : ∀ l ∈ Icc (0 : ℝ) 1, m₀ ≤ ‖G x₀ l‖ := fun l hl => hmin hl
  -- step 3: eventually `‖G ξ l‖ > m₀ / 2`
  have ev3 : ∀ᶠ ξ in 𝓝 x₀, ∀ l ∈ Icc (0 : ℝ) 1, G ξ l ∈ {v : E | m₀ / 2 < ‖v‖} :=
    eventually_forall_mem_of_isCompact isCompact_Icc hG
      (isOpen_lt continuous_const continuous_norm)
      (fun l hl => by show m₀ / 2 < ‖G x₀ l‖; linarith [hbound l hl])
  -- step 4: eventually `‖w ξ - o ξ‖ < M`
  set M := ‖w x₀ - o x₀‖ + 1 with hM
  have ev4 : ∀ᶠ ξ in 𝓝 x₀, ‖w ξ - o ξ‖ < M :=
    ((hw.sub ho).norm.continuousAt).eventually_lt continuousAt_const (by linarith)
  -- step 5: at `x₀`, `w - o` is not a bounded multiple of any `G l`
  set R := 2 * M / m₀ with hR
  let H : X → ℝ × ℝ → E := fun ξ p => (w ξ - o ξ) - p.1 • G ξ p.2
  have hH : Continuous (Function.uncurry H) := by
    simp only [H, G, Function.uncurry_def]; fun_prop
  have hH0 : ∀ p ∈ Icc (0 : ℝ) R ×ˢ Icc (0 : ℝ) 1, H x₀ p ∈ {v : E | v ≠ 0} := by
    rintro ⟨μ, l⟩ ⟨⟨hμ0, -⟩, hl0, hl1⟩ h0
    have h0 : w x₀ - o x₀ = μ • G x₀ l := sub_eq_zero.mp h0
    rcases hμ0.lt_or_eq with hμ | rfl
    · set s := min 1 (1 / μ) with hs
      have hs0 : 0 < s := lt_min one_pos (by positivity)
      have hs1 : s ≤ 1 := min_le_left _ _
      have hsμ : s * μ ≤ 1 := by
        calc s * μ ≤ (1 / μ) * μ := by gcongr; exact min_le_right _ _
          _ = 1 := by field_simp
      have hP1 : o x₀ + s • (w x₀ - o x₀) ∈ segment ℝ (o x₀) (w x₀) := by
        rw [segment_eq_image']; exact ⟨s, ⟨hs0.le, hs1⟩, rfl⟩
      have hP2 : o x₀ + s • (w x₀ - o x₀) ∈ convexHull ℝ {o x₀, y x₀, z x₀} := by
        rw [convexHull_triple_eq_image]
        refine ⟨(s * μ * l, s * μ * (1 - l)), ⟨by positivity,
          mul_nonneg (by positivity) (by linarith), by nlinarith⟩, ?_⟩
        rw [h0]; simp only [triPt, G, smul_add, smul_smul]; module
      have hPo := h1 ⟨hP1, hP2⟩
      have : s • (w x₀ - o x₀) = 0 := by
        have := congrArg (· - o x₀) (Set.mem_singleton_iff.mp hPo)
        simpa using this
      exact h3 (sub_eq_zero.mp ((smul_eq_zero.mp this).resolve_left hs0.ne'))
    · exact h3 (sub_eq_zero.mp (by simpa using h0))
  have ev5 := eventually_forall_mem_of_isCompact ((isCompact_Icc).prod isCompact_Icc) hH
    isOpen_ne hH0
  -- step 6: conclude
  filter_upwards [ev3, ev4, ev5] with ξ h3ξ h4ξ h5ξ
  rintro v ⟨hv1, hv2⟩
  rw [segment_eq_image'] at hv1
  rw [convexHull_triple_eq_image] at hv2
  obtain ⟨s, ⟨hs0, hs1⟩, rfl⟩ := hv1
  obtain ⟨⟨α, β⟩, ⟨hα, hβ, hαβ⟩, hv⟩ := hv2
  simp only [triPt] at hv
  rcases hs0.lt_or_eq with hs | rfl
  · rcases (add_nonneg hα hβ).lt_or_eq with hab | hab
    · exfalso
      set l := α / (α + β)
      set μ := (α + β) / s
      have hl0 : 0 ≤ l := by positivity
      have hl1 : l ≤ 1 := by rw [div_le_one hab]; linarith
      have hwo : w ξ - o ξ = μ • G ξ l := by
        have e1 : s • (w ξ - o ξ) = α • (y ξ - o ξ) + β • (z ξ - o ξ) := by
          have := hv.symm
          rw [add_assoc] at this
          exact add_left_cancel this
        have e2 : μ • G ξ l = (1 / s) • (α • (y ξ - o ξ) + β • (z ξ - o ξ)) := by
          simp only [μ, G, l, smul_add, smul_smul]
          have hb : 1 - α / (α + β) = β / (α + β) := by field_simp; ring
          rw [hb]; congr 1 <;> congr 1 <;> field_simp
        rw [e2, ← e1, smul_smul, one_div, inv_mul_cancel₀ hs.ne', one_smul]
      have hGl := h3ξ l ⟨hl0, hl1⟩
      have hμ0 : 0 ≤ μ := by positivity
      have hμR : μ ≤ R := by
        have hn : ‖w ξ - o ξ‖ = μ * ‖G ξ l‖ := by
          rw [hwo, norm_smul, Real.norm_of_nonneg hμ0]
        rw [hR, le_div_iff₀ hm₀pos]
        nlinarith [norm_nonneg (G ξ l)]
      exact h5ξ (μ, l) ⟨⟨hμ0, hμR⟩, hl0, hl1⟩ (sub_eq_zero.mpr hwo)
    · have hα0 : α = 0 := by linarith
      have hβ0 : β = 0 := by linarith
      subst hα0 hβ0
      simp only [zero_smul, add_zero] at hv
      exact hv.symm
  · simp

lemma convexHull_pair_dup (a b : E) : convexHull ℝ {a, b, b} = segment ℝ a b := by
  rw [Set.insert_eq_of_mem (Set.mem_singleton b), convexHull_pair]

/-- **Disjoint segments stay disjoint.** -/
theorem eventually_segment_inter_segment_eq_empty {a b c d : X → E}
    (ha : Continuous a) (hb : Continuous b) (hc : Continuous c) (hd : Continuous d)
    (h : segment ℝ (a x₀) (b x₀) ∩ segment ℝ (c x₀) (d x₀) = ∅) :
    ∀ᶠ x in 𝓝 x₀, segment ℝ (a x) (b x) ∩ segment ℝ (c x) (d x) = ∅ := by
  have := eventually_segment_inter_convexHull_eq_empty ha hb hc hd hd
    (by rwa [convexHull_pair_dup])
  filter_upwards [this] with x hx
  rwa [convexHull_pair_dup] at hx

/-- **Two segments from a common endpoint `o` keep meeting only at `o`**, as long as neither
collapses. -/
theorem eventually_segment_inter_segment_subset {o w y : X → E}
    (ho : Continuous o) (hw : Continuous w) (hy : Continuous y)
    (h1 : segment ℝ (o x₀) (w x₀) ∩ segment ℝ (o x₀) (y x₀) ⊆ {o x₀})
    (hy0 : y x₀ ≠ o x₀) (hw0 : w x₀ ≠ o x₀) :
    ∀ᶠ x in 𝓝 x₀, segment ℝ (o x) (w x) ∩ segment ℝ (o x) (y x) ⊆ {o x} := by
  have := eventually_segment_inter_convexHull_subset ho hw hy hy
    (by rwa [convexHull_pair_dup])
    (by rw [segment_same]; exact fun h => hy0 (Set.mem_singleton_iff.mp h).symm) hw0
  filter_upwards [this] with x hx
  rwa [convexHull_pair_dup] at hx

/-- How one segment of a family meets a triangle `conv{o, y, z}` at the base configuration:
not at all, or only at the vertex `o`, or only at the vertex `y`, which it shares. -/
def SegClass (o y z s t : X → E) : Prop :=
  segment ℝ (s x₀) (t x₀) ∩ convexHull ℝ {o x₀, y x₀, z x₀} = ∅ ∨
  (s = o ∧ t x₀ ≠ o x₀ ∧ segment ℝ (o x₀) (t x₀) ∩ convexHull ℝ {o x₀, y x₀, z x₀} ⊆ {o x₀}) ∨
  (s = y ∧ t x₀ ≠ y x₀ ∧ segment ℝ (y x₀) (t x₀) ∩ convexHull ℝ {o x₀, y x₀, z x₀} ⊆ {y x₀}) ∨
  (t = o ∧ s x₀ ≠ o x₀ ∧ segment ℝ (o x₀) (s x₀) ∩ convexHull ℝ {o x₀, y x₀, z x₀} ⊆ {o x₀}) ∨
  (t = y ∧ s x₀ ≠ y x₀ ∧ segment ℝ (y x₀) (s x₀) ∩ convexHull ℝ {o x₀, y x₀, z x₀} ⊆ {y x₀})

/-- **A finite family of moving segments keeps meeting a moving triangle only at the vertices
`o`, `y`** it meets there at the base configuration, provided neither of those vertices lies on
the opposite side of the triangle. -/
theorem eventually_iUnion_inter_convexHull_subset {J : Type*} [Finite J] {o y z : X → E}
    (ho : Continuous o) (hy : Continuous y) (hz : Continuous z)
    {s t : J → X → E} (hs : ∀ j, Continuous (s j)) (ht : ∀ j, Continuous (t j))
    (hcls : ∀ j, SegClass (x₀ := x₀) o y z (s j) (t j))
    (hno : o x₀ ∉ segment ℝ (y x₀) (z x₀)) (hny : y x₀ ∉ segment ℝ (o x₀) (z x₀)) :
    ∀ᶠ x in 𝓝 x₀, (⋃ j, segment ℝ (s j x) (t j x)) ∩ convexHull ℝ {o x, y x, z x} ⊆
      {o x, y x} := by
  have hcomm : ∀ x, convexHull ℝ {o x, y x, z x} = convexHull ℝ {y x, o x, z x} := fun x => by
    rw [Set.insert_comm]
  -- the two touching cases, for a segment written from the shared vertex
  have touch_o : ∀ u : X → E, Continuous u → u x₀ ≠ o x₀ →
      segment ℝ (o x₀) (u x₀) ∩ convexHull ℝ {o x₀, y x₀, z x₀} ⊆ {o x₀} →
      ∀ᶠ x in 𝓝 x₀, segment ℝ (o x) (u x) ∩ convexHull ℝ {o x, y x, z x} ⊆ {o x, y x} := by
    intro u hu hu0 h
    filter_upwards [eventually_segment_inter_convexHull_subset ho hu hy hz h hno hu0] with x hx
    exact hx.trans (by simp)
  have touch_y : ∀ u : X → E, Continuous u → u x₀ ≠ y x₀ →
      segment ℝ (y x₀) (u x₀) ∩ convexHull ℝ {o x₀, y x₀, z x₀} ⊆ {y x₀} →
      ∀ᶠ x in 𝓝 x₀, segment ℝ (y x) (u x) ∩ convexHull ℝ {o x, y x, z x} ⊆ {o x, y x} := by
    intro u hu hu0 h
    have h' : segment ℝ (y x₀) (u x₀) ∩ convexHull ℝ {y x₀, o x₀, z x₀} ⊆ {y x₀} := by
      rw [← hcomm]; exact h
    filter_upwards [eventually_segment_inter_convexHull_subset hy hu ho hz h' hny hu0] with x hx
    rw [hcomm]
    exact hx.trans (by simp)
  have key : ∀ j, ∀ᶠ x in 𝓝 x₀, segment ℝ (s j x) (t j x) ∩ convexHull ℝ {o x, y x, z x} ⊆
      {o x, y x} := by
    intro j
    rcases hcls j with h | ⟨hso, hto, h⟩ | ⟨hsy, hty, h⟩ | ⟨hto, hso, h⟩ | ⟨hty, hsy, h⟩
    · filter_upwards [eventually_segment_inter_convexHull_eq_empty (hs j) (ht j) ho hy hz h]
        with x hx
      rw [hx]; exact empty_subset _
    · rw [hso]; exact touch_o _ (ht j) hto h
    · rw [hsy]; exact touch_y _ (ht j) hty h
    · rw [hto]; filter_upwards [touch_o _ (hs j) hso h] with x hx
      rwa [segment_symm]
    · rw [hty]; filter_upwards [touch_y _ (hs j) hsy h] with x hx
      rwa [segment_symm]
  filter_upwards [Filter.eventually_all.mpr key] with x hx
  rintro w ⟨hw1, hw2⟩
  obtain ⟨j, hj⟩ := Set.mem_iUnion.mp hw1
  exact hx j ⟨hj, hw2⟩

namespace Polygon

/-- **Simplicity is an open condition on the vertices.** -/
theorem eventually_isSimple {n : ℕ} (hn : 2 ≤ n) {V : X → Fin (n + 1) → E}
    (hV : Continuous V) (h : (⟨n, hn, V x₀⟩ : Polygon E).IsSimple) :
    ∀ᶠ x in 𝓝 x₀, (⟨n, hn, V x⟩ : Polygon E).IsSimple := by
  have hVi : ∀ i, Continuous fun x => V x i := fun i => (continuous_apply i).comp hV
  set P₀ : Polygon E := ⟨n, hn, V x₀⟩
  have hnext : ∀ x, (⟨n, hn, V x⟩ : Polygon E).next = P₀.next := fun _ => rfl
  -- injectivity
  have hinj : ∀ᶠ x in 𝓝 x₀, ∀ i j : Fin (n + 1), i ≠ j → V x i ≠ V x j := by
    refine Filter.eventually_all.mpr fun i => Filter.eventually_all.mpr fun j => ?_
    by_cases hij : i = j
    · exact Filter.Eventually.of_forall fun _ h => absurd hij h
    · have hne : V x₀ i ≠ V x₀ j := fun he => hij (h.1 he)
      filter_upwards [((hVi i).sub (hVi j)).continuousAt.eventually_ne (sub_ne_zero.mpr hne)]
        with x hx
      exact fun _ => sub_ne_zero.mp hx
  -- each pair of edges
  have hpair : ∀ i j : Fin (n + 1), i ≠ j → ∀ᶠ x in 𝓝 x₀,
      segment ℝ (V x i) (V x (P₀.next i)) ∩ segment ℝ (V x j) (V x (P₀.next j)) =
        if j = P₀.next i then {V x j} else if i = P₀.next j then {V x i} else ∅ := by
    intro i j hij
    have h0 := h.2 i j hij
    have hni : P₀.next i ≠ i := P₀.next_ne i
    have hnj : P₀.next j ≠ j := P₀.next_ne j
    have hvne : ∀ a b : Fin (n + 1), a ≠ b → V x₀ a ≠ V x₀ b := fun a b hab he => hab (h.1 he)
    by_cases h1 : j = P₀.next i
    · subst h1
      simp only at h0 ⊢
      have := eventually_segment_inter_segment_subset (hVi (P₀.next i)) (hVi i)
        (hVi (P₀.next (P₀.next i)))
        (by rw [segment_symm]; exact h0.subset)
        (hvne _ _ (P₀.next_ne _)) (hvne _ _ hni.symm)
      filter_upwards [this] with x hx
      apply Subset.antisymm
      · rw [segment_symm]; exact hx
      · rintro _ rfl; exact ⟨right_mem_segment ℝ _ _, left_mem_segment ℝ _ _⟩
    · by_cases h2 : i = P₀.next j
      · subst h2
        simp only [if_neg h1] at h0 ⊢
        have := eventually_segment_inter_segment_subset (hVi (P₀.next j)) (hVi j)
          (hVi (P₀.next (P₀.next j)))
          (by rw [segment_symm, inter_comm]; exact h0.subset)
          (hvne _ _ (P₀.next_ne _)) (hvne _ _ hnj.symm)
        filter_upwards [this] with x hx
        apply Subset.antisymm
        · rw [inter_comm, segment_symm]; exact hx
        · rintro _ rfl; exact ⟨left_mem_segment ℝ _ _, right_mem_segment ℝ _ _⟩
      · simp only [if_neg h1, if_neg h2] at h0 ⊢
        exact eventually_segment_inter_segment_eq_empty (hVi i) (hVi _) (hVi j) (hVi _) h0
  have hall : ∀ᶠ x in 𝓝 x₀, ∀ i j : Fin (n + 1), i ≠ j →
      segment ℝ (V x i) (V x (P₀.next i)) ∩ segment ℝ (V x j) (V x (P₀.next j)) =
        if j = P₀.next i then {V x j} else if i = P₀.next j then {V x i} else ∅ := by
    refine Filter.eventually_all.mpr fun i => Filter.eventually_all.mpr fun j => ?_
    by_cases hij : i = j
    · exact Filter.Eventually.of_forall fun _ h => absurd hij h
    · filter_upwards [hpair i j hij] with x hx using fun _ => hx
  filter_upwards [hinj, hall] with x hx1 hx2
  exact ⟨fun i j he => by_contra fun hij => hx1 i j hij he, fun i j hij => hx2 i j hij⟩

end Polygon

end
end QOU.MathlibExt.PL
