import QOU.BraidsAndKnots.RationalAssociator.FurushoSingleLevel

/-!
# The pentagon obstruction as a class, and the whole degree-`d` step from one associator

Bean `qou-3fdg`, audit §17n.

`PentagonObstruction.lean` leaves `PentagonLiftVanishes E d`, and `FurushoSingleLevel.lean`
shows that `FurushoGroupStep E d` (`d ≥ 3`) is one-degree existence of a rational associator
modulo `d + 1`. This file does two things.

**(1) The whole step at degree `d`, for every `E` and every `d ≥ 1`, is one-degree existence.**

* `obstructionVanishesAt_of_exists_assocK`: one group-like `K`-associator for `E` modulo `d + 1`
  gives `ObstructionVanishesAt E d`, for `d ≥ 1`. No other level, no Lie-algebra Furusho theorem.
* `obstructionVanishesAt_of_exists`, `pentagonLiftVanishes_of_exists`: the same over `ℚ`.
* `obstructionVanishesAt_iff_exists`: given one rational associator modulo `d` (group-like modulo
  `FF2 d`), `ObstructionVanishesAt E d ↔ ∃ Ψ, AssocU4 (d + 1) E Ψ ∧ GL (d + 1) Ψ`.
* `obstructionVanishesAt_of_exists_le`: existence modulo `N + 1` gives the step at every
  `1 ≤ d ≤ N`.

**(2) The pentagon obstruction is a well-defined class.** Let `pentObs d E Φ` be the pentagon
defect of `Φ` in `U4 (d + 1)` and `pentCob d` the image, under the linearised pentagon
(Drinfeld's (5.20)), of the homogeneous primitive (Lie) elements of degree `d` (`lieLayer d`).

* `pentagon_add_iff`: for `x ∈ FF d`, `Pentagon (Φ + x)` modulo `d + 1` iff
  `pentObs Φ + pentLin x = 0`.
* `pentagonLiftVanishes_iff_mem`: `PentagonLiftVanishes E d` iff `pentObs d E Φ ∈ pentCob d`
  for every `Φ` in its hypothesis set.
* `pentObs_sub_mem`, `pentClass_eq`: the class of `pentObs d E Φ` in `U4 (d + 1) ⧸ pentCob d`
  depends only on `Φ` modulo degree `d` (among `Φ` group-like modulo `FF2 (d + 1)`).

## What is not proved, and why

`PentagonLiftVanishes E d` for `E ≠ 1` with no existence input. In Drinfeld's set-up the class
`pentClass` lies in (the degree-`d` part of) the fourth cohomology of the pentagon complex. Two
things separate the statement here from that one, and neither is done:

* the **cocycle condition**: the defect satisfies the five-strand (Stasheff `K₅`) identity in
  `U(𝔱₅)`. That needs a five-strand universal algebra `U5` and its five coface maps
  `U4 → U5`, neither of which is in the repository;
* the **vanishing**: Drinfeld 1991, §5, p. 14 (held, `library/drinfeld1991-quasitriangular`,
  `sections/page-014.md`), after Prop. 5.8, on the fourth cohomology `H⁴` of the relevant
  complex `L̄*`: *"The author does not know whether its 4th cohomology group `H⁴` is equal to
  0."* So the route "the obstruction is a cocycle in a group that vanishes" rests, in the
  held literature, on an open question. Bar-Natan 1998 is not held; it is not cited here for
  any claim.

For `E = 1` the statement is already proved unconditionally (`pentagonLiftVanishes_one`). For
`E ≠ 1` (1) shows that what is left is exactly one-degree existence, which classically is
Drinfeld's KZ theorem plus descent. No `axiom`, no `sorry`, no analysis.
-/

namespace QOU.BraidsAndKnots.RationalAssociator

open TensorProduct Friedrichs

local notation "F2" => FreeAlgebra ℚ (Fin 2)

variable {K : Type*} [Field K] [Algebra ℚ K]

/-! ### 1. The whole degree-`d` step from one associator one degree up -/

/-- **One group-like `K`-associator for `E` modulo `d + 1` kills the lifting obstruction at
degree `d`**, for every `d ≥ 1`. -/
theorem obstructionVanishesAt_of_exists_assocK {E : F2} (hE : FreeAlgebra.algebraMapInv E = 1)
    {d : ℕ} (hd : 1 ≤ d) {Ψ : K ⊗[ℚ] F2} (hK : AssocK K (d + 1) E Ψ)
    (hGL : GLK K (d + 1) Ψ) : ObstructionVanishesAt E d := by
  intro Φ hA hG
  obtain ⟨hΦ, Ψ', hK', hGL', hm⟩ := levelInvAt_of_assoc hE hK hGL hd (by omega) hA hG
  obtain ⟨z, rfl⟩ := exists_lTensor_of_mem_FFK hm
  obtain ⟨x, hx, ha, hgx, -⟩ :=
    inductionStep_of_groupLike hd le_rfl (by omega : 2 ≤ d + 1) le_rfl hE hΦ z hK' hGL'
  exact (lift_iff_obsLin hd hE hΦ).1 ⟨x, hx, ha, hgx⟩

/-- The same from one rational associator modulo `d + 1`. -/
theorem obstructionVanishesAt_of_exists {E : F2} (hE : FreeAlgebra.algebraMapInv E = 1)
    {d : ℕ} (hd : 1 ≤ d) {Ψ : F2} (hA : AssocU4 (d + 1) E Ψ) (hG : GL (d + 1) Ψ) :
    ObstructionVanishesAt E d :=
  obstructionVanishesAt_of_exists_assocK (K := ℚ) hE hd (assocK_of_assocU4 hA) (GLK_of_GL hG)

/-- **The pentagon lift at degree `d` from one rational associator modulo `d + 1`.** -/
theorem pentagonLiftVanishes_of_exists {E : F2} (hE : FreeAlgebra.algebraMapInv E = 1)
    {d : ℕ} (hd : 1 ≤ d) {Ψ : F2} (hA : AssocU4 (d + 1) E Ψ) (hG : GL (d + 1) Ψ) :
    PentagonLiftVanishes E d :=
  pentagonLiftVanishes_of_obstructionVanishesAt hE hd (obstructionVanishesAt_of_exists hE hd hA hG)

/-- **The step at degree `d` is one-degree existence**, for every `E` and `d ≥ 1`, as soon as
its hypothesis set is non-empty. -/
theorem obstructionVanishesAt_iff_exists {E : F2} (hE : FreeAlgebra.algebraMapInv E = 1)
    {d : ℕ} (hd : 1 ≤ d) {Φ₀ : F2} (hA₀ : AssocU4 d E Φ₀) (hG₀ : GL d Φ₀) :
    ObstructionVanishesAt E d ↔ ∃ Ψ : F2, AssocU4 (d + 1) E Ψ ∧ GL (d + 1) Ψ := by
  constructor
  · intro hV
    obtain ⟨x, hx, hl⟩ := hV Φ₀ hA₀ hG₀
    obtain ⟨y, -, ha, hg⟩ := (lift_iff_obsLin hd hE hA₀.const).2 ⟨x, hx, hl⟩
    exact ⟨_, ha, hg⟩
  · rintro ⟨Ψ, hA, hG⟩
    exact obstructionVanishesAt_of_exists hE hd hA hG

/-- **Existence modulo `N + 1` gives the step at every lower degree.** -/
theorem obstructionVanishesAt_of_exists_le {E : F2} (hE : FreeAlgebra.algebraMapInv E = 1)
    {N : ℕ} {Ψ : F2} (hA : AssocU4 (N + 1) E Ψ) (hG : GL (N + 1) Ψ) {d : ℕ} (hd : 1 ≤ d)
    (hdN : d ≤ N) : ObstructionVanishesAt E d :=
  obstructionVanishesAt_of_exists hE hd (hA.trunc (by omega)) (FF2_anti (by omega) hG)

/-! ### 2. The pentagon obstruction class -/

/-- The degree-`d` Lie layer: homogeneous primitive elements of degree `d` in `FF d`. -/
noncomputable def lieLayer (d : ℕ) : Submodule ℚ F2 where
  carrier := {h | h ∈ FF d ∧ Homog d h ∧ IsPrimitive h}
  add_mem' := by
    rintro a b ⟨ha, hha, hpa⟩ ⟨hb, hhb, hpb⟩
    refine ⟨add_mem ha hb, fun r => ?_, ?_⟩
    · rw [map_add, hha r, hhb r, smul_add]
    · rw [isPrimitive_iff] at hpa hpb ⊢
      rw [map_add, hpa, hpb, add_zero]
  zero_mem' := ⟨zero_mem _, fun r => by rw [map_zero, smul_zero], (isPrimitive_iff 0).2 (map_zero _)⟩
  smul_mem' := by
    rintro c a ⟨ha, hha, hpa⟩
    refine ⟨Submodule.smul_mem _ c ha, fun r => ?_, ?_⟩
    · rw [map_smul, hha r, smul_comm]
    · rw [isPrimitive_iff] at hpa ⊢
      rw [map_smul, hpa, smul_zero]

theorem mem_lieLayer {d : ℕ} {h : F2} :
    h ∈ lieLayer d ↔ h ∈ FF d ∧ Homog d h ∧ IsPrimitive h := Iff.rfl

/-- The pentagon component of the associator target. -/
noncomputable def pentProj (N : ℕ) : AssocTarget N →ₗ[ℚ] U4 N :=
  (LinearMap.snd ℚ (U4 N) (U4 N)).comp (LinearMap.snd ℚ (InvIdx N → U4 N) (U4 N × U4 N))

@[simp] theorem pentProj_apply (N : ℕ) (z : AssocTarget N) : pentProj N z = z.2.2 := rfl

/-- The linearised pentagon (Drinfeld's (5.20)) in `U4 N`. -/
noncomputable def pentLin (N : ℕ) : F2 →ₗ[ℚ] U4 N := (pentProj N).comp (assocLin N)

/-- **The pentagon coboundaries in degree `d`**: images of degree-`d` Lie elements. -/
noncomputable def pentCob (d : ℕ) : Submodule ℚ (U4 (d + 1)) :=
  (lieLayer d).map (pentLin (d + 1))

/-- **The pentagon obstruction of `Φ` at degree `d`**: its pentagon defect in `U4 (d + 1)`. -/
noncomputable def pentObs (d : ℕ) (E Φ : F2) : U4 (d + 1) := (assocDefect (d + 1) E Φ).2.2

theorem pentagon_iff_defect {N : ℕ} {E Φ : F2} :
    Pentagon Φ (t N 0) (t N 1) (t N 3) (t N 4) (t N 5) ↔ (assocDefect N E Φ).2.2 = 0 := by
  refine ⟨assocDefect_pent_eq_zero, fun h => ?_⟩
  simp only [assocDefect] at h
  exact (sub_eq_zero.1 h).symm

/-- **The pentagon modulo `d + 1` after a degree-`d` correction is linear.** -/
theorem pentagon_add_iff {d : ℕ} (hd : 1 ≤ d) {E Φ x : F2}
    (hE : FreeAlgebra.algebraMapInv E = 1) (hΦ : FreeAlgebra.algebraMapInv Φ = 1)
    (hx : x ∈ FF d) :
    Pentagon (Φ + x) (t (d + 1) 0) (t (d + 1) 1) (t (d + 1) 3) (t (d + 1) 4) (t (d + 1) 5) ↔
      pentObs d E Φ + pentLin (d + 1) x = 0 := by
  rw [pentagon_iff_defect (E := E), assocDefect_add hd hE hΦ hx]
  rfl

/-- **`PentagonLiftVanishes` is membership of the obstruction in the coboundaries.** -/
theorem pentagonLiftVanishes_iff_mem {E : F2} (hE : FreeAlgebra.algebraMapInv E = 1) {d : ℕ}
    (hd : 1 ≤ d) :
    PentagonLiftVanishes E d ↔
      ∀ Φ : F2, AssocU4 d E Φ → GL (d + 1) Φ → pentObs d E Φ ∈ pentCob d := by
  constructor
  · intro hP Φ hA hG
    obtain ⟨h, hhF, hh, hhp, hpent⟩ := hP Φ hA hG
    have h0 := (pentagon_add_iff hd hE hA.const hhF).1 hpent
    refine ⟨-h, neg_mem ⟨hhF, hh, hhp⟩, ?_⟩
    rw [map_neg]
    exact (eq_neg_of_add_eq_zero_left h0).symm
  · intro hM Φ hA hG
    obtain ⟨h, ⟨hhF, hh, hhp⟩, he⟩ := hM Φ hA hG
    have hn : -h ∈ lieLayer d := neg_mem ⟨hhF, hh, hhp⟩
    obtain ⟨hnF, hnh, hnp⟩ := hn
    refine ⟨-h, hnF, hnh, hnp, (pentagon_add_iff hd hE hA.const hnF).2 ?_⟩
    rw [map_neg, he, add_neg_cancel]

/-- **The obstruction class depends only on `Φ` modulo degree `d`.** For `Φ, Φ'` group-like
modulo `FF2 (d + 1)` with `Φ' − Φ ∈ FF d`, `pentObs Φ' − pentObs Φ ∈ pentCob d`. -/
theorem pentObs_sub_mem {d : ℕ} (hd : 1 ≤ d) {E Φ Φ' : F2}
    (hE : FreeAlgebra.algebraMapInv E = 1) (hΦ : FreeAlgebra.algebraMapInv Φ = 1)
    (hx : Φ' - Φ ∈ FF d) (hG : GL (d + 1) Φ) (hG' : GL (d + 1) Φ') :
    pentObs d E Φ' - pentObs d E Φ ∈ pentCob d := by
  set x := Φ' - Φ with hxdef
  have hΦ' : Φ' = Φ + x := by rw [hxdef, add_sub_cancel]
  have hδ : primDef x ∈ FF2 (d + 1) :=
    primDef_mem_of_GL_add hd (sub_one_mem_FF_one hΦ) hx hG (by rwa [← hΦ'])
  obtain ⟨k, hk, hxk, hkp⟩ := exists_primitive_layer hx hδ
  have hkF : k ∈ FF d := by
    have e : k = x - (x - k) := by abel
    rw [e]; exact sub_mem hx (FF_anti (by omega) hxk)
  have hlk : pentLin (d + 1) k = pentLin (d + 1) x := by
    have e : k = x - (x - k) := by abel
    rw [e, map_sub, pentLin, LinearMap.comp_apply, LinearMap.comp_apply,
      assocLin_eq_zero_of_mem_FF hxk, map_zero, sub_zero]
  have hadd : pentObs d E Φ' = pentObs d E Φ + pentLin (d + 1) x := by
    simp only [pentObs, hΦ', assocDefect_add hd hE hΦ hx]
    rfl
  refine ⟨k, ⟨hkF, hk, hkp⟩, ?_⟩
  rw [hlk, hadd, add_sub_cancel_left]

/-- The pentagon obstruction class in `U4 (d + 1) ⧸ pentCob d`. -/
noncomputable def pentClass (d : ℕ) (E Φ : F2) : U4 (d + 1) ⧸ pentCob d :=
  Submodule.Quotient.mk (pentObs d E Φ)

/-- **The class is a function of `Φ` modulo degree `d`.** -/
theorem pentClass_eq {d : ℕ} (hd : 1 ≤ d) {E Φ Φ' : F2}
    (hE : FreeAlgebra.algebraMapInv E = 1) (hΦ : FreeAlgebra.algebraMapInv Φ = 1)
    (hx : Φ' - Φ ∈ FF d) (hG : GL (d + 1) Φ) (hG' : GL (d + 1) Φ') :
    pentClass d E Φ' = pentClass d E Φ :=
  (Submodule.Quotient.eq _).2 (pentObs_sub_mem hd hE hΦ hx hG hG')

/-- `PentagonLiftVanishes` is vanishing of the class. -/
theorem pentagonLiftVanishes_iff_class {E : F2} (hE : FreeAlgebra.algebraMapInv E = 1) {d : ℕ}
    (hd : 1 ≤ d) :
    PentagonLiftVanishes E d ↔
      ∀ Φ : F2, AssocU4 d E Φ → GL (d + 1) Φ → pentClass d E Φ = 0 := by
  rw [pentagonLiftVanishes_iff_mem hE hd]
  simp only [pentClass, Submodule.Quotient.mk_eq_zero]

end QOU.BraidsAndKnots.RationalAssociator
