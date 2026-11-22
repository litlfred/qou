import QOU.MathlibExt.CechSubdivCover

/-!
# Fine star covers by longest-edge bisection (route R3, step S3d)

Let `X ⊆ ℝⁿ` and let `T` be a triangulation of `X` that is **linear**: the
homeomorphism sends barycentric coordinates `q` to `∑ q_w P_w` for vertex
positions `P_w ∈ ℝⁿ` (`GTri`). Subdividing an edge `{a, b}` keeps this, with the
new vertex at the midpoint.

Write `e2 v = ∑ vᵢ²`. If every edge of `T` has `e2 ≤ M` and the edge `{a, b}` has
`e2 > 9M/10`, then after subdividing it every edge still has `e2 ≤ M`, the new
edges from the midpoint have `e2 < 31M/40` (Apollonius), and the set of edges with
`e2 > 9M/10` loses `{a, b}`. So finitely many subdivisions bring every edge
below `9M/10`, and `k` rounds below `(9/10)^k M`, while the star cover stays
reached (`reach_subdiv`).

Every point of the star of `w` lies within `√M` of `P_w` in each coordinate, so
the star cover gets arbitrarily fine.

## Results, all sorry-free

* `GTri`, `GTri.subdiv`, `Bounded`, `longs`.
* `apollonius`: `4·e2(m − c) = 2·e2(a − c) + 2·e2(b − c) − e2(a − b)` at the
  midpoint `m`.
* `bounded_subdiv`, `longs_subdiv_card`: one bisection.
* `exists_round`, `exists_fine`: reached star covers with all edges below any
  `ε > 0`.
* `dist_lt_of_mem_fam`: two points of one star are closer than `2√M`.
* `compactSpace_pspace`: realisations are compact.

## What this does NOT do

It does not apply the Lebesgue number lemma or name the genus-4 surface; that is
`CechGenus4Good`. The identification with Bring's curve is a citation, and `hχ`
(Poincaré–Hopf) stays a hypothesis. Bean `qou-skn4`.

-- Ref: [leitner2026] lifting-and-descent, route R3, surface step S3/S4
-/
open CategoryTheory TopologicalSpace
open QOU.CentralExtension.CechGerbe

set_option linter.unusedSectionVars false

namespace QOU.CentralExtension.Cech.PL

/-! ### Compactness of a realisation -/

theorem real4_isCompact {V : Type} [Fintype V] [DecidableEq V] (F : Finset (Finset V)) :
    IsCompact (Real4 F) := by
  have e : Real4 F = (⋂ i, {p : V → ℝ | 0 ≤ p i}) ∩ {p | ∑ i, p i = 1} ∩
      ⋃ f ∈ F, ⋂ i ∈ (Finset.univ.filter (· ∉ f)), {p : V → ℝ | p i ≤ 0} := by
    ext p
    simp only [Real4, Set.mem_inter_iff, Set.mem_iInter, Set.mem_setOf_eq, Set.mem_iUnion,
      Finset.mem_filter, Finset.mem_univ, true_and, exists_prop]
    constructor
    · rintro ⟨h0, h1, f, hf, hpf⟩
      exact ⟨⟨h0, h1⟩, f, hf, fun i hi => not_lt.1 fun h => hi (hpf i h)⟩
    · rintro ⟨⟨h0, h1⟩, f, hf, hpf⟩
      exact ⟨h0, h1, f, hf, fun i h => by_contra fun hi => (not_lt.2 (hpf i hi)) h⟩
  have hc : IsClosed (Real4 F) := by
    rw [e]
    refine ((isClosed_iInter fun i => isClosed_le continuous_const (continuous_apply i)).inter
      (isClosed_eq (continuous_finset_sum _ fun i _ => continuous_apply i) continuous_const)).inter ?_
    exact F.finite_toSet.isClosed_biUnion fun f _ =>
      isClosed_biInter fun i _ => isClosed_le (continuous_apply i) continuous_const
  have hs : Real4 F ⊆ Set.pi Set.univ (fun _ => Set.Icc (0 : ℝ) 1) := by
    rintro p ⟨h0, h1, -⟩ i -
    refine ⟨h0 i, ?_⟩
    rw [← h1]
    exact Finset.single_le_sum (fun j _ => h0 j) (Finset.mem_univ i)
  exact (isCompact_univ_pi fun _ => isCompact_Icc).of_isClosed_subset hc hs

instance compactSpace_pspace {V : Type} [Fintype V] [DecidableEq V] (F : Finset (Finset V)) :
    CompactSpace (PSpace F) :=
  isCompact_iff_compactSpace.1 (real4_isCompact F)

/-! ### Squared length and Apollonius -/

variable {n : ℕ}

/-- Squared Euclidean length. -/
def e2 (v : Fin n → ℝ) : ℝ := ∑ i, v i ^ 2

theorem e2_nonneg (v : Fin n → ℝ) : 0 ≤ e2 v := Finset.sum_nonneg fun i _ => sq_nonneg _

theorem e2_sub_comm (u v : Fin n → ℝ) : e2 (u - v) = e2 (v - u) := by
  unfold e2; congr 1; funext i; simp only [Pi.sub_apply]; ring

theorem e2_self (u : Fin n → ℝ) : e2 (u - u) = 0 := by simp [e2]

theorem sq_le_e2 (v : Fin n → ℝ) (i : Fin n) : v i ^ 2 ≤ e2 v :=
  Finset.single_le_sum (f := fun j => v j ^ 2) (fun j _ => sq_nonneg _) (Finset.mem_univ i)

theorem abs_le_sqrt_e2 (v : Fin n → ℝ) (i : Fin n) : |v i| ≤ Real.sqrt (e2 v) :=
  Real.abs_le_sqrt (sq_le_e2 v i)

/-- **Apollonius.** -/
theorem apollonius (a b c : Fin n → ℝ) :
    4 * e2 ((fun i => (a i + b i) / 2) - c) =
      2 * e2 (a - c) + 2 * e2 (b - c) - e2 (a - b) := by
  unfold e2
  simp only [Finset.mul_sum, ← Finset.sum_sub_distrib, ← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun i _ => ?_
  simp only [Pi.sub_apply]; ring

theorem e2_half (a b : Fin n → ℝ) : e2 ((fun i => (a i + b i) / 2) - a) = e2 (a - b) / 4 := by
  unfold e2
  rw [eq_div_iff (by norm_num : (4:ℝ) ≠ 0), Finset.sum_mul]
  refine Finset.sum_congr rfl fun i _ => ?_
  simp only [Pi.sub_apply]; ring

/-! ### Linear triangulations -/

variable {Ω : Set (Fin n → ℝ)}

/-- A triangulation of `Ω` that is linear in barycentric coordinates. -/
structure GTri (Ω : Set (Fin n → ℝ)) where
  T : Tri Ω
  P : T.V → Fin n → ℝ
  hP : ∀ q : PSpace T.F, (T.H q).1 = fun i => ∑ w, q.1 w * P w i

namespace GTri

variable (S : GTri Ω)

theorem sum_hw_mul {V : Type} [Fintype V] [DecidableEq V] {a b : V} (hab : a ≠ b) (g : V → ℝ) :
    ∑ w, hw a b w * g w = (g a + g b) / 2 := by
  have : ∀ w, hw a b w * g w = (if w = a then g w / 2 else 0) + (if w = b then g w / 2 else 0) := by
    intro w; unfold hw
    by_cases h1 : w = a
    · subst h1; simp [hab]; ring
    · by_cases h2 : w = b
      · subst h2; simp [h1]; ring
      · simp [h1, h2]
  simp only [this, Finset.sum_add_distrib, Finset.sum_ite_eq', Finset.mem_univ, if_true]
  ring

/-- Subdividing an edge of a linear triangulation; the new vertex is the midpoint. -/
noncomputable def subdiv {a b : S.T.V} (hab : a ≠ b) : GTri Ω where
  T := S.T.subdiv hab
  P x := Option.elim x (fun i => (S.P a i + S.P b i) / 2) S.P
  hP q := by
    change (S.T.H (homeo S.T.F hab q)).1 = _
    rw [S.hP]
    funext i
    simp only [homeo_apply, fwd, add_mul, Finset.sum_add_distrib]
    change _ = ∑ x : Option S.T.V, q.1 x * Option.elim x (fun i => (S.P a i + S.P b i) / 2) S.P i
    rw [sum_option]
    simp only [Option.elim]
    rw [add_comm]
    congr 1
    rw [show (∑ w, hw a b w * q.1 none * S.P w i) = q.1 none * ∑ w, hw a b w * S.P w i by
      rw [Finset.mul_sum]; exact Finset.sum_congr rfl fun _ _ => by ring, sum_hw_mul hab]

/-- Every edge has squared length at most `M`. -/
def Bounded (M : ℝ) : Prop :=
  ∀ f ∈ S.T.F, ∀ x ∈ f, ∀ y ∈ f, e2 (S.P x - S.P y) ≤ M

open Classical in
/-- Ordered edges longer than `c`. -/
noncomputable def longs (c : ℝ) : Finset (S.T.V × S.T.V) :=
  Finset.univ.filter fun xy => (∃ f ∈ S.T.F, xy.1 ∈ f ∧ xy.2 ∈ f) ∧ c < e2 (S.P xy.1 - S.P xy.2)

theorem mem_longs {c : ℝ} {x y : S.T.V} :
    (x, y) ∈ S.longs c ↔ (∃ f ∈ S.T.F, x ∈ f ∧ y ∈ f) ∧ c < e2 (S.P x - S.P y) := by
  classical
  simp [longs]

theorem subdiv_P_some {a b : S.T.V} (hab : a ≠ b) (w : S.T.V) :
    (S.subdiv hab).P (some w) = S.P w := rfl

theorem subdiv_P_none {a b : S.T.V} (hab : a ≠ b) :
    (S.subdiv hab).P none = fun i => (S.P a i + S.P b i) / 2 := rfl

/-- The midpoint is close to every vertex of a face through the long edge. -/
theorem e2_mid {M : ℝ} (hB : S.Bounded M) {a b : S.T.V} {f : Finset S.T.V} (hf : f ∈ S.T.F)
    (ha : a ∈ f) (hb : b ∈ f) (hl : 9 * M / 10 < e2 (S.P a - S.P b)) {v : S.T.V} (hv : v ∈ f) :
    e2 ((fun i => (S.P a i + S.P b i) / 2) - S.P v) ≤ 9 * M / 10 := by
  have h := apollonius (S.P a) (S.P b) (S.P v)
  have h1 := hB f hf a ha v hv
  have h2 := hB f hf b hb v hv
  have hM : 0 ≤ M := (e2_nonneg _).trans (hB f hf a ha a ha)
  linarith

theorem bounded_subdiv {M : ℝ} (hB : S.Bounded M) {a b : S.T.V} (hab : a ≠ b)
    (hl : (a, b) ∈ S.longs (9 * M / 10)) :
    (S.subdiv hab).Bounded M ∧
      ((S.subdiv hab).longs (9 * M / 10)).card < (S.longs (9 * M / 10)).card := by
  classical
  obtain ⟨⟨f₀, hf₀, ha₀, hb₀⟩, hl'⟩ := (S.mem_longs).1 hl
  -- pairs of the new complex
  have key : ∀ g ∈ (S.subdiv hab).T.F, ∀ x ∈ g, ∀ y ∈ g,
      e2 ((S.subdiv hab).P x - (S.subdiv hab).P y) ≤ M ∧
      (9 * M / 10 < e2 ((S.subdiv hab).P x - (S.subdiv hab).P y) →
        ∃ u v, x = some u ∧ y = some v ∧ (u, v) ∈ S.longs (9 * M / 10) ∧ (u, v) ≠ (a, b)) := by
    intro g hg x hx y hy
    obtain ⟨f, hf, hsome, hnone⟩ := sub_over hg
    have hM : ∀ {u}, u ∈ f → 0 ≤ M := fun hu => (e2_nonneg _).trans (hB f hf _ hu _ hu)
    cases x with
    | none =>
      obtain ⟨ha, hb⟩ := hnone hx
      have hlab : 9 * M / 10 < e2 (S.P a - S.P b) := by
        have := hl'; exact this
      cases y with
      | none =>
        simp only [sub_self]
        have : e2 (0 : Fin n → ℝ) = 0 := by simp [e2]
        rw [this]
        exact ⟨hM ha, fun h => by linarith [hM ha]⟩
      | some v =>
        have := S.e2_mid hB hf ha hb hlab (hsome v hy)
        rw [subdiv_P_none, subdiv_P_some]
        exact ⟨by linarith [hM ha], fun h => by linarith⟩
    | some u =>
      cases y with
      | none =>
        obtain ⟨ha, hb⟩ := hnone hy
        have := S.e2_mid hB hf ha hb hl' (hsome u hx)
        rw [subdiv_P_none, subdiv_P_some, e2_sub_comm]
        exact ⟨by linarith [hM ha], fun h => by linarith⟩
      | some v =>
        rw [subdiv_P_some, subdiv_P_some]
        refine ⟨hB f hf u (hsome u hx) v (hsome v hy), fun h => ⟨u, v, rfl, rfl,
          (S.mem_longs).2 ⟨⟨f, hf, hsome u hx, hsome v hy⟩, h⟩, fun e => ?_⟩⟩
        simp only [Prod.mk.injEq] at e
        obtain ⟨rfl, rfl⟩ := e
        exact sub_not_both hg ⟨hx, hy⟩
  refine ⟨fun g hg x hx y hy => (key g hg x hx y hy).1, ?_⟩
  have hsub : (S.subdiv hab).longs (9 * M / 10) ⊆
      ((S.longs (9 * M / 10)).erase (a, b)).image (fun uv => (some uv.1, some uv.2)) := by
    intro xy hxy
    obtain ⟨⟨g, hg, hx, hy⟩, hlong⟩ := ((S.subdiv hab).mem_longs (x := xy.1) (y := xy.2)).1 hxy
    obtain ⟨u, v, e1, e2', hm, hne⟩ := (key g hg _ hx _ hy).2 hlong
    exact Finset.mem_image.2 ⟨(u, v), Finset.mem_erase.2 ⟨hne, hm⟩, by
      rw [Prod.ext_iff]; exact ⟨e1.symm, e2'.symm⟩⟩
  calc ((S.subdiv hab).longs (9 * M / 10)).card
      ≤ (((S.longs (9 * M / 10)).erase (a, b)).image _).card := Finset.card_le_card hsub
    _ ≤ ((S.longs (9 * M / 10)).erase (a, b)).card := Finset.card_image_le
    _ < (S.longs (9 * M / 10)).card := Finset.card_erase_lt_of_mem hl

/-! ### Iterating -/

variable {G : Type} [TopologicalSpace G] [CommGroup G] [IsTopologicalGroup G] [DiscreteTopology G]
  {ι₀ : Type} {U₀ : ι₀ → Opens Ω}

/-- One round: all edges `≤ M` become `≤ 9M/10`, keeping the cover reached. -/
theorem round (M : ℝ) (k : ℕ) : ∀ S : GTri Ω, S.Bounded M →
    (S.longs (9 * M / 10)).card ≤ k → Reach G U₀ S.T.fam →
    ∃ S' : GTri Ω, S'.Bounded (9 * M / 10) ∧ Reach G U₀ S'.T.fam := by
  induction k with
  | zero =>
    intro S hB hk hR
    refine ⟨S, fun f hf x hx y hy => ?_, hR⟩
    by_contra h
    have : (x, y) ∈ S.longs (9 * M / 10) := (S.mem_longs).2 ⟨⟨f, hf, hx, hy⟩, not_le.1 h⟩
    have := Finset.card_pos.2 ⟨_, this⟩
    omega
  | succ k ih =>
    intro S hB hk hR
    by_cases hne : (S.longs (9 * M / 10)).Nonempty
    · obtain ⟨⟨a, b⟩, hl⟩ := hne
      have hab : a ≠ b := by
        rintro rfl
        obtain ⟨⟨f, hf, ha, -⟩, h⟩ := (S.mem_longs).1 hl
        rw [e2_self] at h
        have hM := hB f hf a ha a ha
        rw [e2_self] at hM
        linarith
      obtain ⟨hB', hc⟩ := S.bounded_subdiv hB hab hl
      exact ih (S.subdiv hab) hB' (by omega) (S.T.reach_subdiv hab hR)
    · refine ⟨S, fun f hf x hx y hy => ?_, hR⟩
      by_contra h
      exact hne ⟨(x, y), (S.mem_longs).2 ⟨⟨f, hf, hx, hy⟩, not_le.1 h⟩⟩

theorem exists_round (M : ℝ) (S : GTri Ω) (hB : S.Bounded M) (hR : Reach G U₀ S.T.fam) (k : ℕ) :
    ∃ S' : GTri Ω, S'.Bounded (M * (9 / 10) ^ k) ∧ Reach G U₀ S'.T.fam := by
  induction k with
  | zero => exact ⟨S, by simpa using hB, hR⟩
  | succ k ih =>
    obtain ⟨S₁, hB₁, hR₁⟩ := ih
    obtain ⟨S₂, hB₂, hR₂⟩ := round (G := G) (U₀ := U₀) _ _ S₁ hB₁ le_rfl hR₁
    refine ⟨S₂, fun f hf x hx y hy => ?_, hR₂⟩
    have := hB₂ f hf x hx y hy
    rw [pow_succ]; linarith

/-- **Fine reached star covers.** -/
theorem exists_fine (M : ℝ) (S : GTri Ω) (hB : S.Bounded M) (hR : Reach G U₀ S.T.fam)
    {ε : ℝ} (hε : 0 < ε) : ∃ S' : GTri Ω, S'.Bounded ε ∧ Reach G U₀ S'.T.fam := by
  obtain ⟨k, hk⟩ := exists_pow_lt_of_lt_one (show 0 < ε / (|M| + 1) by positivity)
    (show (9 / 10 : ℝ) < 1 by norm_num)
  obtain ⟨S', hB', hR'⟩ := exists_round (G := G) (U₀ := U₀) M S hB hR k
  refine ⟨S', fun f hf x hx y hy => ?_, hR'⟩
  have h1 := hB' f hf x hx y hy
  have hp : 0 ≤ (9 / 10 : ℝ) ^ k := by positivity
  have h2 : M * (9 / 10) ^ k ≤ |M| * (9 / 10) ^ k := mul_le_mul_of_nonneg_right (le_abs_self M) hp
  have h3 : (9 / 10 : ℝ) ^ k * (|M| + 1) < ε := (lt_div_iff₀ (by positivity)).1 hk
  nlinarith [abs_nonneg M]

/-! ### Small stars -/

/-- Every point of the star of `w` is within `√M` of `P_w` in each coordinate. -/
theorem abs_sub_le_of_mem_fam {M : ℝ} (hB : S.Bounded M) {w : S.T.V} {x : Ω}
    (hx : x ∈ S.T.fam w) (i : Fin n) : |x.1 i - S.P w i| ≤ Real.sqrt M := by
  set q := S.T.H.symm x
  have hqx : S.T.H q = x := S.T.H.apply_symm_apply x
  obtain ⟨hq0, hq1, f, hf, hqf⟩ := q.2
  have hw : w ∈ f := hqf w hx
  have hxi : x.1 i = ∑ u, q.1 u * S.P u i := by rw [← hqx, S.hP]
  have e : x.1 i - S.P w i = ∑ u, q.1 u * (S.P u i - S.P w i) := by
    rw [hxi]
    simp only [mul_sub, Finset.sum_sub_distrib, ← Finset.sum_mul, hq1, one_mul]
  rw [e]
  calc |∑ u, q.1 u * (S.P u i - S.P w i)| ≤ ∑ u, |q.1 u * (S.P u i - S.P w i)| :=
        Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ u, q.1 u * Real.sqrt M := by
        refine Finset.sum_le_sum fun u _ => ?_
        rw [abs_mul, abs_of_nonneg (hq0 u)]
        by_cases hu : 0 < q.1 u
        · refine mul_le_mul_of_nonneg_left ?_ (hq0 u)
          refine (abs_le_sqrt_e2 (S.P u - S.P w) i).trans ?_
          exact Real.sqrt_le_sqrt (hB f hf u (hqf u hu) w hw)
        · have : q.1 u = 0 := le_antisymm (not_lt.1 hu) (hq0 u)
          simp [this]
    _ = Real.sqrt M := by rw [← Finset.sum_mul, hq1, one_mul]

/-- **Two points of one star are less than `δ` apart once `2√M < δ`.** -/
theorem dist_lt_of_mem_fam {M δ : ℝ} (hB : S.Bounded M) (hδ : 2 * Real.sqrt M < δ) {w : S.T.V}
    {x y : Ω} (hx : x ∈ S.T.fam w) (hy : y ∈ S.T.fam w) : dist x y < δ := by
  have hδ0 : 0 < δ := lt_of_le_of_lt (by positivity) hδ
  rw [Subtype.dist_eq, dist_pi_lt_iff hδ0]
  intro i
  rw [Real.dist_eq]
  have h1 := S.abs_sub_le_of_mem_fam hB hx i
  have h2 := S.abs_sub_le_of_mem_fam hB hy i
  calc |x.1 i - y.1 i| = |(x.1 i - S.P w i) - (y.1 i - S.P w i)| := by ring_nf
    _ ≤ |x.1 i - S.P w i| + |y.1 i - S.P w i| := abs_sub _ _
    _ < δ := by linarith

end GTri

end QOU.CentralExtension.Cech.PL
