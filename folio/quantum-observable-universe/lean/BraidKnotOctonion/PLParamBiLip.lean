/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import BraidKnotOctonion.PLParamSample
import BraidKnotOctonion.PLInscribed

set_option autoImplicit false

/-!
# The parametrization of a simple polygon is bi-Lipschitz (issue #8902)

For a simple polygon `Q` in a real inner product space, the standard parametrization
`Q.param` of period `1` satisfies a lower bound against the distance on the circle `ℝ / ℤ`:
some `c > 0` has

  `c * min |s - t| (1 - |s - t|) ≤ ‖Q.param s - Q.param t‖`   for `s, t ∈ [0, 1]`.

## What is a THEOREM here

* `exists_pos_forall_le_of_finite` — a finite family of positive reals has a positive lower bound.
* `Polygon.IsSimple.not_sameRay` — at each vertex the two incident edges do not point the same
  way.
* `Polygon.IsSimple.exists_param_sep` — times `γ ≤ t - s ≤ 1 - γ` give points `c γ` apart.
* `Polygon.IsSimple.exists_param_lower` — **the lower bound above.** The proof splits on the
  pieces containing `s` and `t`: the same piece (the edge length), consecutive pieces (the angle
  bound `exists_pos_mul_le_norm_smul_sub` at the shared vertex), and non-consecutive pieces
  (disjoint compact edges are a positive distance apart).
-/

namespace QOU.MathlibExt.PL

open Set Filter Topology

/-- A finite family of positive reals has a positive lower bound. -/
lemma exists_pos_forall_le_of_finite {ι : Type*} [Finite ι] (f : ι → ℝ) (hf : ∀ i, 0 < f i) :
    ∃ c > 0, ∀ i, c ≤ f i := by
  have h : ∀ᶠ c in 𝓝[>] (0 : ℝ), ∀ i, c ≤ f i :=
    eventually_all.mpr fun i => Filter.mem_of_superset (Ioo_mem_nhdsGT (hf i))
      fun c hc => hc.2.le
  obtain ⟨c, hc, hc0⟩ := (h.and self_mem_nhdsWithin).exists
  exact ⟨c, hc0, hc⟩

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

namespace Polygon

variable {Q : Polygon E}

/-- At each vertex the two incident edges do not point the same way. -/
lemma IsSimple.not_sameRay (hQ : Q.IsSimple) (i : Fin (Q.n + 1)) :
    ¬ SameRay ℝ (Q.v i - Q.v (Q.next i)) (Q.v (Q.next (Q.next i)) - Q.v (Q.next i)) := by
  set j := Q.next i
  set k := Q.next j
  have hu : Q.v i - Q.v j ≠ 0 := sub_ne_zero.mpr (hQ.1.ne (Q.next_ne i).symm)
  have hw : Q.v k - Q.v j ≠ 0 := sub_ne_zero.mpr (hQ.1.ne (Q.next_ne j))
  intro hr
  obtain ⟨r₁, r₂, h₁, h₂, he⟩ := hr.exists_pos hu hw
  set x := Q.v j + (r₁ / (r₁ + r₂)) • (Q.v i - Q.v j)
  have hx' : x = Q.v j + (r₂ / (r₁ + r₂)) • (Q.v k - Q.v j) := by
    simp only [x]
    rw [div_eq_mul_inv, div_eq_mul_inv, mul_comm, mul_smul, mul_comm r₂, mul_smul, he]
  have hpos : 0 < r₁ + r₂ := by linarith
  have hxi : x ∈ Q.edge i := by
    rw [edge, segment_symm, segment_eq_image']
    exact ⟨r₁ / (r₁ + r₂), ⟨by positivity, by rw [div_le_one hpos]; linarith⟩, rfl⟩
  have hxj : x ∈ Q.edge j := by
    rw [hx', edge, segment_eq_image']
    exact ⟨r₂ / (r₁ + r₂), ⟨by positivity, by rw [div_le_one hpos]; linarith⟩, rfl⟩
  have hmem : x ∈ Q.edge i ∩ Q.edge (Q.next i) := ⟨hxi, hxj⟩
  rw [hQ.adj i, mem_singleton_iff] at hmem
  have : (r₁ / (r₁ + r₂)) • (Q.v i - Q.v j) = 0 := by
    have := hmem; simp only [x] at this
    exact add_eq_left.mp this
  rcases smul_eq_zero.mp this with h | h
  · exact (div_pos h₁ hpos).ne' h
  · exact hu h

/-- The point at local coordinate `a` on piece `i`. -/
lemma param_local (i : Fin (Q.n + 1)) {a : ℝ} (ha0 : 0 ≤ a) (ha1 : a ≤ 1) :
    Q.param (((i : ℝ) + a) / (Q.n + 1)) = Q.v i + a • (Q.v (Q.next i) - Q.v i) := by
  have hN : (0 : ℝ) < Q.n + 1 := by positivity
  rw [Q.param_piece i (div_le_div_of_nonneg_right (by linarith) hN.le)
    (div_le_div_of_nonneg_right (by linarith) hN.le)]
  congr 2
  field_simp
  ring

lemma min_abs_le_half (x : ℝ) : min |x| (1 - |x|) ≤ 1 / 2 := by
  rcases le_total |x| (1 / 2) with h | h
  · exact (min_le_left _ _).trans h
  · exact (min_le_right _ _).trans (by linarith)

/-- **The parametrization of a simple polygon is bi-Lipschitz** for the circle distance. -/
theorem IsSimple.exists_param_lower (hQ : Q.IsSimple) :
    ∃ c > 0, ∀ s t : ℝ, 0 ≤ s → s ≤ 1 → 0 ≤ t → t ≤ 1 →
      c * min |s - t| (1 - |s - t|) ≤ ‖Q.param s - Q.param t‖ := by
  classical
  have hN : (0 : ℝ) < Q.n + 1 := by positivity
  set d : Fin (Q.n + 1) → E := fun i => Q.v (Q.next i) - Q.v i
  -- edge lengths
  obtain ⟨e, he0, he⟩ := exists_pos_forall_le_of_finite (fun i => ‖d i‖) fun i =>
    norm_pos_iff.mpr (sub_ne_zero.mpr (hQ.1.ne (Q.next_ne i)))
  -- angles
  have hang : ∀ i, ∃ κ > 0, ∀ α β : ℝ, 0 ≤ α → 0 ≤ β →
      κ * (α * ‖Q.v i - Q.v (Q.next i)‖ + β * ‖Q.v (Q.next (Q.next i)) - Q.v (Q.next i)‖) ≤
        ‖α • (Q.v i - Q.v (Q.next i)) - β • (Q.v (Q.next (Q.next i)) - Q.v (Q.next i))‖ :=
    fun i => exists_pos_mul_le_norm_smul_sub
      (sub_ne_zero.mpr (hQ.1.ne (Q.next_ne i).symm))
      (sub_ne_zero.mpr (hQ.1.ne (Q.next_ne (Q.next i)))) (hQ.not_sameRay i)
  choose κf hκf hκ using hang
  obtain ⟨κ, hκ0, hκle⟩ := exists_pos_forall_le_of_finite κf hκf
  -- separation of non-consecutive edges
  have hsep : ∀ p : Fin (Q.n + 1) × Fin (Q.n + 1), ∃ D > 0,
      p.1 ≠ p.2 → p.2 ≠ Q.next p.1 → p.1 ≠ Q.next p.2 →
        ∀ a b : ℝ, 0 ≤ a → a ≤ 1 → 0 ≤ b → b ≤ 1 →
          D ≤ ‖(Q.v p.1 + a • d p.1) - (Q.v p.2 + b • d p.2)‖ := by
    rintro ⟨i, j⟩
    by_cases hc : i ≠ j ∧ j ≠ Q.next i ∧ i ≠ Q.next j
    · set K : Set (ℝ × ℝ) := Icc 0 1 ×ˢ Icc 0 1
      have hK : IsCompact K := isCompact_Icc.prod isCompact_Icc
      have hKne : K.Nonempty := ⟨(0, 0), ⟨left_mem_Icc.mpr zero_le_one,
        left_mem_Icc.mpr zero_le_one⟩⟩
      set F : ℝ × ℝ → ℝ := fun q => ‖(Q.v i + q.1 • d i) - (Q.v j + q.2 • d j)‖
      have hF : ContinuousOn F K := by
        apply Continuous.continuousOn; simp only [F]; fun_prop
      obtain ⟨q, hq, hmin⟩ := hK.exists_isMinOn hKne hF
      have hdisj := hQ.disj hc.1 hc.2.1 hc.2.2
      have hpos : 0 < F q := by
        refine norm_pos_iff.mpr (sub_ne_zero.mpr fun h => ?_)
        have h1 : Q.v i + q.1 • d i ∈ Q.edge i := by
          rw [edge, segment_eq_image']; exact ⟨q.1, hq.1, rfl⟩
        have h2 : Q.v i + q.1 • d i ∈ Q.edge j := by
          rw [h, edge, segment_eq_image']; exact ⟨q.2, hq.2, rfl⟩
        exact Set.disjoint_left.mp hdisj h1 h2
      exact ⟨F q, hpos, fun _ _ _ a b ha0 ha1 hb0 hb1 =>
        hmin (show ((a, b) : ℝ × ℝ) ∈ K from ⟨⟨ha0, ha1⟩, ⟨hb0, hb1⟩⟩)⟩
    · exact ⟨1, one_pos, fun h1 h2 h3 => absurd ⟨h1, h2, h3⟩ hc⟩
  choose Df hDf hD using hsep
  obtain ⟨D, hD0, hDle⟩ := exists_pos_forall_le_of_finite Df hDf
  set c := min (min ((Q.n + 1) * e) (κ * e * (Q.n + 1))) (2 * D)
  have hc0 : 0 < c := by positivity
  have hc1 : c ≤ (Q.n + 1) * e := (min_le_left _ _).trans (min_le_left _ _)
  have hc2 : c ≤ κ * e * (Q.n + 1) := (min_le_left _ _).trans (min_le_right _ _)
  have hc3 : c ≤ 2 * D := min_le_right _ _
  -- consecutive pieces, in order
  have hadj : ∀ (i : Fin (Q.n + 1)) (a b : ℝ), 0 ≤ a → a < 1 → 0 ≤ b → b < 1 →
      ∀ s t : ℝ, s = ((i : ℝ) + a) / (Q.n + 1) → t = (((Q.next i : ℕ) : ℝ) + b) / (Q.n + 1) →
        c * min |s - t| (1 - |s - t|) ≤ ‖Q.param s - Q.param t‖ := by
    intro i a b ha0 ha1 hb0 hb1 s t hs ht
    have hcd : min |s - t| (1 - |s - t|) ≤ (1 - a + b) / (Q.n + 1) := by
      have hnext := coe_finRotate i
      simp only [Nat.succ_eq_add_one] at hnext
      have hnx : ((Q.next i : ℕ) : ℝ) = if i = Fin.last Q.n then 0 else (i : ℝ) + 1 := by
        rw [next, hnext]; split_ifs <;> simp
      rw [hnx] at ht
      split_ifs at ht with hl
      · have hi : (i : ℝ) = Q.n := by rw [hl]; simp
        rw [hi] at hs
        have hst0 : s - t = (Q.n + a - b) / (Q.n + 1) := by rw [hs, ht]; ring
        have hst : |s - t| = (Q.n + a - b) / (Q.n + 1) := by
          rw [hst0, abs_of_nonneg]
          apply div_nonneg _ hN.le
          have : (2 : ℝ) ≤ Q.n := by exact_mod_cast Q.two_le
          linarith
        rw [hst]
        refine (min_le_right _ _).trans (le_of_eq ?_)
        field_simp; ring
      · have hst0 : t - s = (1 - a + b) / (Q.n + 1) := by rw [hs, ht]; ring
        have hst : |s - t| = (1 - a + b) / (Q.n + 1) := by
          rw [abs_sub_comm, hst0, abs_of_nonneg]
          apply div_nonneg _ hN.le
          linarith
        rw [hst]; exact min_le_left _ _
    have hps : Q.param s = Q.v i + a • d i := by rw [hs]; exact Q.param_local i ha0 ha1.le
    have hpt : Q.param t = Q.v (Q.next i) + b • d (Q.next i) := by
      rw [ht]; exact Q.param_local (Q.next i) hb0 hb1.le
    have hval : Q.param s - Q.param t = (1 - a) • (Q.v i - Q.v (Q.next i)) -
        b • (Q.v (Q.next (Q.next i)) - Q.v (Q.next i)) := by
      rw [hps, hpt]; simp only [d]; module
    rw [hval]
    have h1 := hκ i (1 - a) b (by linarith) hb0
    have hu : e ≤ ‖Q.v i - Q.v (Q.next i)‖ := by rw [norm_sub_rev]; exact he i
    have hw : e ≤ ‖Q.v (Q.next (Q.next i)) - Q.v (Q.next i)‖ := he (Q.next i)
    have h2 : κ * e * (1 - a + b) ≤ κf i * ((1 - a) * ‖Q.v i - Q.v (Q.next i)‖ +
        b * ‖Q.v (Q.next (Q.next i)) - Q.v (Q.next i)‖) := by
      have := hκle i
      have h3 : e * (1 - a + b) ≤ (1 - a) * ‖Q.v i - Q.v (Q.next i)‖ +
          b * ‖Q.v (Q.next (Q.next i)) - Q.v (Q.next i)‖ := by
        nlinarith [mul_le_mul_of_nonneg_left hu (by linarith : (0 : ℝ) ≤ 1 - a),
          mul_le_mul_of_nonneg_left hw hb0]
      calc κ * e * (1 - a + b) = κ * (e * (1 - a + b)) := by ring
        _ ≤ κf i * (e * (1 - a + b)) :=
          mul_le_mul_of_nonneg_right this (mul_nonneg he0.le (by linarith))
        _ ≤ _ := mul_le_mul_of_nonneg_left h3 (hκf i).le
    calc c * min |s - t| (1 - |s - t|) ≤ (κ * e * (Q.n + 1)) * ((1 - a + b) / (Q.n + 1)) :=
          (mul_le_mul_of_nonneg_left hcd hc0.le).trans
            (mul_le_mul_of_nonneg_right hc2 (div_nonneg (by linarith) hN.le))
      _ = κ * e * (1 - a + b) := by field_simp
      _ ≤ _ := h2.trans h1
  have hloc : ∀ (i : Fin (Q.n + 1)) (a x : ℝ), 0 ≤ a → a < 1 → x = ((i : ℝ) + a) / (Q.n + 1) →
      Q.param x = Q.v i + a • d i := by
    intro i a x ha0 ha1 hx; rw [hx]; exact Q.param_local i ha0 ha1.le
  have hmain : ∀ s t : ℝ, 0 ≤ s → s < 1 → 0 ≤ t → t < 1 →
      c * min |s - t| (1 - |s - t|) ≤ ‖Q.param s - Q.param t‖ := by
    intro s t hs0 hs1 ht0 ht1
    obtain ⟨i, a, ha0, ha1, hs⟩ := Q.exists_piece hs0 hs1
    obtain ⟨j, b, hb0, hb1, ht⟩ := Q.exists_piece ht0 ht1
    by_cases hij : i = j
    · subst hij
      have hst0 : s - t = (a - b) / (Q.n + 1) := by rw [hs, ht]; ring
      have hst : |s - t| = |a - b| / (Q.n + 1) := by rw [hst0, abs_div, abs_of_pos hN]
      rw [hloc i a s ha0 ha1 hs, hloc i b t hb0 hb1 ht,
        show Q.v i + a • d i - (Q.v i + b • d i) = (a - b) • d i by module, norm_smul,
        Real.norm_eq_abs]
      calc c * min |s - t| (1 - |s - t|) ≤ ((Q.n + 1) * e) * (|a - b| / (Q.n + 1)) :=
            (mul_le_mul_of_nonneg_left ((min_le_left _ _).trans hst.le) hc0.le).trans
              (mul_le_mul_of_nonneg_right hc1 (by positivity))
        _ = e * |a - b| := by field_simp
        _ ≤ |a - b| * ‖d i‖ := by
          rw [mul_comm]; exact mul_le_mul_of_nonneg_left (he i) (abs_nonneg _)
    by_cases hji : j = Q.next i
    · subst hji; exact hadj i a b ha0 ha1 hb0 hb1 s t hs ht
    by_cases hij' : i = Q.next j
    · subst hij'
      have := hadj j b a hb0 hb1 ha0 ha1 t s ht hs
      rwa [abs_sub_comm, norm_sub_rev] at this
    · rw [hloc i a s ha0 ha1 hs, hloc j b t hb0 hb1 ht]
      have h1 := hD (i, j) hij hji hij' a b ha0 ha1.le hb0 hb1.le
      have h2 := hDle (i, j)
      calc c * min |s - t| (1 - |s - t|) ≤ c * (1 / 2) :=
            mul_le_mul_of_nonneg_left (min_abs_le_half _) hc0.le
        _ ≤ (2 * D) * (1 / 2) := mul_le_mul_of_nonneg_right hc3 (by norm_num)
        _ = D := by ring
        _ ≤ _ := h2.trans h1
  refine ⟨c, hc0, fun s t hs0 hs1 ht0 ht1 => ?_⟩
  rcases hs1.lt_or_eq with hs1 | rfl <;> rcases ht1.lt_or_eq with ht1 | rfl
  · exact hmain s t hs0 hs1 ht0 ht1
  · have := hmain s 0 hs0 hs1 le_rfl one_pos
    rw [Q.param_one]
    rw [sub_zero, abs_of_nonneg hs0] at this
    rwa [abs_sub_comm, abs_of_nonneg (by linarith), sub_sub_cancel, min_comm]
  · have := hmain 0 t le_rfl one_pos ht0 ht1
    rw [Q.param_one]
    rw [zero_sub, abs_neg, abs_of_nonneg ht0] at this
    rwa [abs_of_nonneg (by linarith), sub_sub_cancel, min_comm]
  · simp only [sub_self, abs_zero, sub_zero]
    rw [min_eq_left zero_le_one, mul_zero]; exact norm_nonneg _

lemma param_fract (x : ℝ) : Q.param (Int.fract x) = Q.param x := by
  simp [param, Int.fract_fract]

lemma param_sub_int (x : ℝ) (k : ℤ) : Q.param (x - k) = Q.param x := by
  simp [param, Int.fract_sub_intCast]

/-- **Separation in time gives separation in space.** Two times whose difference lies in
`[γ, 1 - γ]` (with `0 ≤ γ`) are sent at least `c * γ` apart. -/
theorem IsSimple.exists_param_sep (hQ : Q.IsSimple) :
    ∃ c > 0, ∀ γ s t : ℝ, 0 ≤ γ → γ ≤ t - s → t - s ≤ 1 - γ → c * γ ≤ ‖Q.param s - Q.param t‖ := by
  obtain ⟨c, hc0, hc⟩ := hQ.exists_param_lower
  refine ⟨c, hc0, fun γ s t hγ h1 h2 => ?_⟩
  have key : ∀ z : ℝ, γ ≤ z → z ≤ 1 - γ → γ ≤ min |z| (1 - |z|) := by
    intro z hz1 hz2
    rcases le_total 0 z with hz | hz
    · rw [abs_of_nonneg hz]; exact le_min hz1 (by linarith)
    · rw [abs_of_nonpos hz]; exact le_min (by linarith) (by linarith)
  set s' := Int.fract s
  set t' := t - ⌊s⌋
  have hs0 : 0 ≤ s' := Int.fract_nonneg s
  have hs1 : s' < 1 := Int.fract_lt_one s
  have hts : t' - s' = t - s := by simp only [t', s', Int.fract]; ring
  have hps : Q.param s = Q.param s' := (Q.param_fract s).symm
  have hpt : Q.param t = Q.param t' := (Q.param_sub_int t ⌊s⌋).symm
  rw [hps, hpt]
  rcases lt_or_ge t' 1 with ht | ht
  · have h := hc s' t' hs0 hs1.le (by linarith) ht.le
    refine le_trans ?_ h
    refine mul_le_mul_of_nonneg_left ?_ hc0.le
    rw [abs_sub_comm]; exact key _ (by linarith) (by linarith)
  · have hpt' : Q.param t' = Q.param (t' - 1) := by
      have := Q.param_sub_int t' 1; push_cast at this; exact this.symm
    rw [hpt']
    have h := hc s' (t' - 1) hs0 hs1.le (by linarith) (by linarith)
    refine le_trans ?_ h
    refine mul_le_mul_of_nonneg_left ?_ hc0.le
    exact key _ (by linarith) (by linarith)

end Polygon

end QOU.MathlibExt.PL
