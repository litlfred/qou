import QOU.BraidsAndKnots.RationalAssociator.TransportedDK4

/-!
# The far relation `[s₁₃, s₂₄] = 0` from t-compatibility

Bean `qou-3fdg` (stage 3d of the rational-associator plan, epic `qou-dk7p`). Builds on
`TransportedDK4.lean`, whose `transported_dk4` and `pentagon_act_universal` take the far relation
`hfar : [s₁₃, s₂₄] = 0` as a hypothesis.

* `TCompat`: the t-compatibility identity of `g` at a three-strand family `(u, v, w)`,
  `g(v,w) · v · g(v,w)⁻¹ = g(u,w) · (v + w) · g(u,w)⁻¹ − w`.
* `DK4.swap23`: relabelling strands 2 and 3 of a `DK4` family gives a `DK4` family.
* `far_of_tcompat`: `hfar` follows from two instances of `TCompat`, two instances of (5.13)
  `g(Y,X) g(X,Y) = 1`, the pentagon of `g`, and the pentagon of `g` at the 2↔3-relabelled family.
* `swap23Hom`, `pentagon_swap23`: in `U4 N` the relabelled pentagon is the image of the pentagon
  under the algebra map `lift N (t ∘ π)`, so it need not be assumed.
* `pentagon_act_universal_of_tcompat`: `pentagon_act_universal` with `hfar` replaced by the
  t-compatibility and (5.13) hypotheses.

**`TCompat` is a defining condition of `GRT₁`.** It is Drinfeld's (5.14),
`A + g(A,B)⁻¹ B g(A,B) + g(A,C)⁻¹ C g(A,C) = 0` for `A + B + C = 0` (Drinfeld 1991, §5). This
file's "(5.13)" and "(5.14)" are Drinfeld's (5.12) and (5.13). So for `g ∈ GRT₁`, `TCompat` holds
by definition and does not need to be derived (`docs/audits/2026-11-27-grt-action-pentagon-derivation.md`
§9). Nothing analytic is used.
-/

namespace QOU.BraidsAndKnots.RationalAssociator

section General

variable {R : Type*} [Ring R] [Algebra ℚ R]

/-- **t-compatibility** of `g` at a three-strand family `(u, v, w) = (t_ab, t_ac, t_bc)`, stated
through the units `Guw = g(u, w)` and `Gvw = g(v, w)` (so `u` enters only through `Guw`):
`Gvw · v · Gvw⁻¹ = Guw · (v + w) · Guw⁻¹ − w`. -/
def TCompat (v w : R) (Guw Gvw : Rˣ) : Prop :=
  (Gvw : R) * v * ↑Gvw⁻¹ = (Guw : R) * (v + w) * ↑Guw⁻¹ - w

omit [Algebra ℚ R] in
/-- Relabelling strands 2 and 3 of a `DK4` family. -/
theorem DK4.swap23 {t12 t13 t14 t23 t24 t34 : R} (h : DK4 t12 t13 t14 t23 t24 t34) :
    DK4 t13 t12 t14 t23 t34 t24 where
  f12_34 := h.f13_24
  f13_24 := h.f12_34
  f14_23 := h.f14_23
  n12_3 := h.n13_2
  n13_2 := h.n12_3
  n23_1 := by rw [add_comm]; exact h.n23_1
  n12_4 := h.n13_4
  n14_2 := h.n14_3
  n24_1 := h.n34_1
  n13_4 := h.n12_4
  n14_3 := h.n14_2
  n34_1 := h.n24_1
  n23_4 := by rw [add_comm]; exact h.n23_4
  n24_3 := h.n34_2
  n34_2 := h.n24_3

omit [Algebra ℚ R] in
theorem conj_conj (u : Rˣ) (x : R) : (↑u⁻¹ : R) * ((u : R) * x * ↑u⁻¹) * u = x := by
  simp [mul_assoc]

/-- **The far relation from t-compatibility.** Let `g` satisfy the pentagon at a `DK4` family `t`
and at its 2↔3 relabelling (`hg'`), and (5.13) at `(t₃₄, t₂₃)` and `(t₂₄, t₂₃)`. If `g` is
t-compatible at `(t₁₂, t₁₃, t₂₃)` and at `(t₃₄, t₂₄, t₂₃)`, then the transported family satisfies
`[s₁₃, s₂₄] = 0`. -/
theorem far_of_tcompat (g : FreeAlgebra ℚ (Fin 2)) {t12 t13 t14 t23 t24 t34 : R}
    (hDK : DK4 t12 t13 t14 t23 t24 t34) (Ga Gb Gc Gd Ge K H M W J L : Rˣ)
    (ha : (Ga : R) = eval t12 t23 g) (hb : (Gb : R) = eval (t13 + t23) t34 g)
    (hc : (Gc : R) = eval t12 (t23 + t24) g) (hd : (Gd : R) = eval (t12 + t13) (t24 + t34) g)
    (he : (Ge : R) = eval t23 t34 g)
    (hK : (K : R) = eval t13 t23 g) (hH : (H : R) = eval t23 t24 g)
    (hM : (M : R) = eval t13 (t23 + t34) g) (hW : (W : R) = eval (t12 + t23) t24 g)
    (hJ : (J : R) = eval t34 t23 g) (hL : (L : R) = eval t24 t23 g)
    (hg : Pentagon g t12 t13 t23 t24 t34) (hg' : Pentagon g t13 t12 t23 t34 t24)
    (hu1 : eval t34 t23 g * eval t23 t34 g = 1) (hu2 : eval t24 t23 g * eval t23 t24 g = 1)
    (hA : TCompat t13 t23 Ga K) (hB : TCompat t24 t23 J L) :
    let s := transported t12 t13 t23 t24 t34 Ga Gb Gc
    Commute s.2.1 s.2.2.2.1 := by
  simp only [transported]
  -- (5.13) as unit equalities
  have eJ : J = Ge⁻¹ := eq_inv_of_mul_eq_one_left (Units.ext (by simp [hJ, he, hu1]))
  have eL : L = H⁻¹ := eq_inv_of_mul_eq_one_left (Units.ext (by simp [hL, hH, hu2]))
  subst eJ eL
  -- the two pentagons as unit equalities
  have P : Gc * Gb = Ge * (Gd * Ga) := Units.ext (by
    simp only [Units.val_mul, ha, hb, hc, hd, he]; rw [← mul_assoc]; exact hg)
  have P' : M * W = H * Gd * K := Units.ext (by
    simp only [Units.val_mul, hM, hW, hH, hd, hK]
    rw [add_comm t12 t13, add_comm t24 t34]; exact hg')
  -- s₁₃ = Y⁻¹ t₁₃ Y
  set Y := K⁻¹ * Ga with hY
  have S13 : t13 + t23 - (↑Ga⁻¹ : R) * t23 * Ga = (↑Y⁻¹ : R) * t13 * Y := by
    have e : (↑Y⁻¹ : R) * t13 * Y = (↑Ga⁻¹ : R) * ((K : R) * t13 * ↑K⁻¹) * Ga := by
      simp only [hY, mul_inv_rev, inv_inv, Units.val_mul]; noncomm_ring
    rw [e, hA, mul_sub, sub_mul, conj_conj]
  -- commutations of `Gd`, `M`, `W`
  have cd : Commute (Gd : R) t23 := hd ▸ commute_eval hDK.n23_1.symm hDK.n23_4.symm g
  have cM : Commute (M : R) t24 := hM ▸ commute_eval hDK.f13_24 hDK.n24_3.symm g
  have cW : Commute (W : R) t13 := hW ▸ commute_eval hDK.n13_2.symm hDK.f13_24.symm g
  -- s₂₄ = Y⁻¹ (W⁻¹ t₂₄ W) Y
  have S24 : (↑(Gc * Gb)⁻¹ : R) * (t23 + t24) * ↑(Gc * Gb) - (↑Ga⁻¹ : R) * t23 * Ga =
      (↑Y⁻¹ : R) * ((↑W⁻¹ : R) * t24 * W) * Y := by
    -- Ge⁻¹ (t₂₃ + t₂₄) Ge = H⁻¹ t₂₄ H + t₂₃, from `hB`
    have hB' : (↑Ge⁻¹ : R) * (t23 + t24) * Ge = (↑H⁻¹ : R) * t24 * H + t23 := by
      unfold TCompat at hB
      simp only [inv_inv] at hB
      rw [hB, add_comm t24 t23]; abel
    have e1 : (↑(Gc * Gb)⁻¹ : R) * (t23 + t24) * ↑(Gc * Gb) =
        (↑(Gd * Ga)⁻¹ : R) * ((↑Ge⁻¹ : R) * (t23 + t24) * Ge) * ↑(Gd * Ga) := by
      rw [P]; simp only [mul_inv_rev, Units.val_mul]; noncomm_ring
    have e2 : (↑Ga⁻¹ : R) * t23 * Ga = (↑(Gd * Ga)⁻¹ : R) * t23 * ↑(Gd * Ga) :=
      (conj_mul_of_commute cd).symm
    have e3 : (↑Y⁻¹ : R) * ((↑W⁻¹ : R) * t24 * W) * Y =
        (↑(H * Gd * Ga)⁻¹ : R) * t24 * ↑(H * Gd * Ga) := by
      have hZ : H * Gd * Ga = M * W * Y := by rw [P', hY]; simp [mul_assoc]
      rw [hZ, mul_assoc M W Y, conj_mul_of_commute cM]
      simp only [mul_inv_rev, Units.val_mul]; noncomm_ring
    rw [e1, hB', e2, e3]
    simp only [mul_inv_rev, Units.val_mul]; noncomm_ring
  rw [S13, S24]
  apply Commute.unitsConj
  have := Commute.unitsConj W hDK.f13_24
  rwa [show (↑W⁻¹ : R) * t13 * W = t13 from conj_of_commute cW] at this

end General

section Universal

variable {N : ℕ}

/-- The relabelling of strands 2 and 3 on the six generator indices
`(t₁₂, t₁₃, t₁₄, t₂₃, t₂₄, t₃₄) = (0, 1, 2, 3, 4, 5)`. -/
def swap23Idx : Fin 6 → Fin 6 := ![1, 0, 2, 3, 5, 4]

/-- The algebra endomorphism of `U4 N` relabelling strands 2 and 3, obtained from `lift`. -/
noncomputable def swap23Hom (N : ℕ) : U4 N →ₐ[ℚ] U4 N :=
  lift N (fun i => t N (swap23Idx i)) (by simpa [swap23Idx] using (dk4 N).swap23)
    (fun w hw => by
      rw [← Function.comp_def, ← List.map_map]
      exact word_eq_zero N (w.map swap23Idx) (by simpa using hw))

/-- In `U4 N`, the pentagon of `g` implies its pentagon at the 2↔3-relabelled family. -/
theorem pentagon_swap23 (g : FreeAlgebra ℚ (Fin 2))
    (hg : Pentagon g (t N 0) (t N 1) (t N 3) (t N 4) (t N 5)) :
    Pentagon g (t N 1) (t N 0) (t N 3) (t N 5) (t N 4) := by
  have key := congrArg (swap23Hom N) hg
  simp only [swap23Hom, map_mul, map_eval, map_add, lift_t] at key
  simpa [Pentagon, swap23Idx] using key

/-- **The `GRT` action preserves the pentagon in `U4 N`, given t-compatibility.** As
`pentagon_act_universal`, with the far relation replaced by (5.13) at `(t₃₄, t₂₃)` and
`(t₂₄, t₂₃)` and t-compatibility of `g` at `(t₁₂, t₁₃, t₂₃)` and `(t₃₄, t₂₄, t₂₃)`. -/
theorem pentagon_act_universal_of_tcompat (φ g : FreeAlgebra ℚ (Fin 2))
    (Ga Gb Gc Gd Ge K H M W J L : (U4 N)ˣ)
    (ha : (Ga : U4 N) = eval (t N 0) (t N 3) g)
    (hb : (Gb : U4 N) = eval (t N 1 + t N 3) (t N 5) g)
    (hc : (Gc : U4 N) = eval (t N 0) (t N 3 + t N 4) g)
    (hd : (Gd : U4 N) = eval (t N 0 + t N 1) (t N 4 + t N 5) g)
    (he : (Ge : U4 N) = eval (t N 3) (t N 5) g)
    (hK : (K : U4 N) = eval (t N 1) (t N 3) g) (hH : (H : U4 N) = eval (t N 3) (t N 4) g)
    (hM : (M : U4 N) = eval (t N 1) (t N 3 + t N 5) g)
    (hW : (W : U4 N) = eval (t N 0 + t N 3) (t N 4) g)
    (hJ : (J : U4 N) = eval (t N 5) (t N 3) g) (hL : (L : U4 N) = eval (t N 4) (t N 3) g)
    (hg : Pentagon g (t N 0) (t N 1) (t N 3) (t N 4) (t N 5))
    (hφ : Pentagon φ (t N 0) (t N 1) (t N 3) (t N 4) (t N 5))
    (hu1 : eval (t N 5) (t N 3) g * eval (t N 3) (t N 5) g = 1)
    (hu2 : eval (t N 4) (t N 3) g * eval (t N 3) (t N 4) g = 1)
    (hA : TCompat (t N 1) (t N 3) Ga K) (hB : TCompat (t N 4) (t N 3) J L) :
    actEval φ (t N 0) (t N 3 + t N 4) Gc * actEval φ (t N 1 + t N 3) (t N 5) Gb =
      actEval φ (t N 3) (t N 5) Ge * actEval φ (t N 0 + t N 1) (t N 4 + t N 5) Gd *
        actEval φ (t N 0) (t N 3) Ga :=
  pentagon_act_universal φ g Ga Gb Gc Gd Ge ha hb hc hd he hg hφ
    (far_of_tcompat g (dk4 N) Ga Gb Gc Gd Ge K H M W J L ha hb hc hd he hK hH hM hW hJ hL hg
      (pentagon_swap23 g hg) hu1 hu2 hA hB)

end Universal

end QOU.BraidsAndKnots.RationalAssociator
