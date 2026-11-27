import QOU.BraidsAndKnots.RationalAssociator.AssociatorRealign

/-!
# The obstruction to lifting a rational associator one degree

Bean `qou-3fdg` (epic `qou-dk7p`), audit §17h.

Let `Φ ∈ ℚ⟨X, Y⟩` have constant term `1` and let `d ≥ 1`. The question of the degree-by-degree
construction is whether there is `x ∈ FF d` (words of length `≥ d`) with `Φ + x` a group-like
associator modulo degree `d + 1`, i.e. `AssocU4 (d + 1) E (Φ + x)` and `GL (d + 1) (Φ + x)`.
This file states that question as one inhomogeneous `ℚ`-linear equation and records what is
known about it.

* `glDefect Φ = Δ Φ − Φ ⊗ Φ`, and `GL_add_iff`: `Φ + x` is group-like modulo `FF2 (d + 1)` iff
  `glDefect Φ + primDef x ∈ FF2 (d + 1)`. Group-likeness of the correction is linear, like the
  associator equations (`assocU4_add_iff`).
* `obsLin d : ℚ⟨X, Y⟩ →ₗ[ℚ] ObsTarget d`, `x ↦ (assocLin (d + 1) x, [primDef x])`, the
  linearised pentagon, hexagon and inversion together with the linearised coproduct condition,
  the latter in `(F2 ⊗ F2) ⧸ FF2 (d + 1)`. `obstruction d E Φ` is the pair
  `(−assocDefect (d + 1) E Φ, [−glDefect Φ])`, built from the degree-`d` defects of `Φ`.
* `lift_iff_obsLin`: **a lift exists iff the obstruction lies in the image of `obsLin d` on
  `FF d`.** `lift_iff_homog`: the solution may be taken homogeneous of degree `d`, because
  `obsLin d` kills `FF (d + 1)`.
* `lift_iff_primitive`: if `Φ` is already group-like modulo `FF2 (d + 1)`, a lift exists iff
  there is a **homogeneous primitive** `h` of degree `d` with `assocLin (d + 1) h = −D`, `D` the
  associator defect of `Φ`.
* `liftSolvableOver_iff`: the existence question is **field-independent**: the same equation is
  solvable over `ℚ` iff it is solvable after base change to any nontrivial commutative
  `ℚ`-algebra `K` (`Descent.exists_of_baseChange`, no finiteness used).
  `liftSolvableOver_of_groupLikeK`: a group-like `K`-associator modulo `N ≥ d + 1` agreeing with
  `1 ⊗ Φ` modulo `FFK d` makes the obstruction vanish.
* `AssociatorObstructionVanishes E`: the precise open statement, as a `Prop` (not an axiom):
  for every `d ≥ 1` and every rational group-like associator `Φ` modulo degree `d`, the
  obstruction lies in the image of `obsLin d`. `compatible_of_obstructionVanishes`: it implies a
  compatible sequence of rational group-like associators, with no field `K` anywhere.

## What is not proved

`AssociatorObstructionVanishes E` itself. Drinfeld's argument (1991, §5) proves it from the
existence of one associator over `ℂ` (the KZ associator) and the transitivity of `GRT₁` (Prop.
5.5). A purely algebraic proof would show the obstruction class is a cocycle in the
Drinfeld–Kohno / `grt` deformation complex and that the relevant cohomology vanishes in degree
`d + 1`; Bar-Natan (1998) notes that no such proof is known. Nothing here attempts it. The
converse direction (a `GroupLikeKAssociatorTower` implies `AssociatorObstructionVanishes`) needs
`AssocU4 M ⟹ AssocU4 N` for `N ≤ M`, which is not in this repository.

No analysis and no numerical value is used.
-/

namespace QOU.BraidsAndKnots.RationalAssociator

open TensorProduct Friedrichs

local notation "F2" => FreeAlgebra ℚ (Fin 2)

/-! ### Group-likeness of the correction is linear -/

/-- The group-likeness defect `Δ Φ − Φ ⊗ Φ`. `GL m Φ` says it lies in `FF2 m`. -/
noncomputable def glDefect (Φ : F2) : F2 ⊗[ℚ] F2 := cop Φ - Φ ⊗ₜ Φ

theorem gl_iff_glDefect {m : ℕ} {Φ : F2} : GL m Φ ↔ glDefect Φ ∈ FF2 m := Iff.rfl

/-- `ε(Φ) = 1` puts `Φ − 1` in `FF 1`. -/
theorem sub_one_mem_FF_one {Φ : F2} (hΦ : FreeAlgebra.algebraMapInv Φ = 1) : Φ - 1 ∈ FF 1 := by
  have := sub_algebraMapInv_mem_FF Φ
  rwa [hΦ, map_one] at this

/-- For `Φ ≡ 1` modulo `FF 1` and `x ∈ FF d`, `d ≥ 1`, the group-likeness defect of `Φ + x` is
`glDefect Φ + primDef x` modulo `FF2 (d + 1)`. -/
theorem glDefect_add_sub_mem {d : ℕ} (hd : 1 ≤ d) {Φ x : F2} (hΦ : Φ - 1 ∈ FF 1)
    (hx : x ∈ FF d) : glDefect (Φ + x) - (glDefect Φ + primDef x) ∈ FF2 (d + 1) := by
  have e : glDefect (Φ + x) - (glDefect Φ + primDef x) =
      -((Φ - 1) ⊗ₜ x + x ⊗ₜ (Φ - 1) + x ⊗ₜ x) := by
    simp only [glDefect, primDef_apply, map_add, add_tmul, tmul_add, sub_tmul, tmul_sub]
    abel
  rw [e]
  refine neg_mem (add_mem (add_mem ?_ ?_) ?_)
  · exact FF2_anti (by omega) (tmul_mem_FF2 hΦ hx)
  · exact FF2_anti (by omega) (tmul_mem_FF2 hx hΦ)
  · exact FF2_anti (by omega) (tmul_mem_FF2 hx hx)

/-- **The coproduct condition one degree up is linear in the correction.** -/
theorem GL_add_iff {d : ℕ} (hd : 1 ≤ d) {Φ x : F2} (hΦ : Φ - 1 ∈ FF 1) (hx : x ∈ FF d) :
    GL (d + 1) (Φ + x) ↔ glDefect Φ + primDef x ∈ FF2 (d + 1) := by
  have h := glDefect_add_sub_mem hd hΦ hx
  rw [gl_iff_glDefect]
  constructor
  · intro h1
    have e : glDefect Φ + primDef x =
        glDefect (Φ + x) - (glDefect (Φ + x) - (glDefect Φ + primDef x)) := by abel
    rw [e]; exact sub_mem h1 h
  · intro h2
    have e : glDefect (Φ + x) =
        (glDefect (Φ + x) - (glDefect Φ + primDef x)) + (glDefect Φ + primDef x) := by abel
    rw [e]; exact add_mem h h2

/-! ### The obstruction -/

/-- The target of the linearised equations at degree `d`: the associator equations in
`U4 (d + 1)`, and the coproduct condition modulo `FF2 (d + 1)`. -/
abbrev ObsTarget (d : ℕ) : Type := AssocTarget (d + 1) × ((F2 ⊗[ℚ] F2) ⧸ FF2 (d + 1))

/-- **The linearised operator** (Drinfeld's differential at `Φ = 1`, together with the
linearised coproduct condition): `x ↦ (assocLin (d + 1) x, [Δ x − x ⊗ 1 − 1 ⊗ x])`. -/
noncomputable def obsLin (d : ℕ) : F2 →ₗ[ℚ] ObsTarget d :=
  (assocLin (d + 1)).prod ((FF2 (d + 1)).mkQ ∘ₗ primDef)

/-- **The obstruction of `Φ` at degree `d`**: minus its associator defects in `U4 (d + 1)` and
minus its group-likeness defect modulo `FF2 (d + 1)`. -/
noncomputable def obstruction (d : ℕ) (E Φ : F2) : ObsTarget d :=
  (-assocDefect (d + 1) E Φ, (FF2 (d + 1)).mkQ (-glDefect Φ))

theorem obsLin_apply (d : ℕ) (x : F2) :
    obsLin d x = (assocLin (d + 1) x, Submodule.Quotient.mk (primDef x)) := rfl

theorem obsLin_eq_obstruction_iff {d : ℕ} {E Φ x : F2} :
    obsLin d x = obstruction d E Φ ↔
      assocLin (d + 1) x = -assocDefect (d + 1) E Φ ∧ glDefect Φ + primDef x ∈ FF2 (d + 1) := by
  rw [obsLin_apply, obstruction, Prod.mk.injEq, Submodule.mkQ_apply, Submodule.Quotient.eq,
    sub_neg_eq_add, add_comm (primDef x)]

/-- `obsLin d` kills `FF (d + 1)`. -/
theorem obsLin_eq_zero_of_mem_FF {d : ℕ} {x : F2} (hx : x ∈ FF (d + 1)) : obsLin d x = 0 := by
  rw [obsLin_apply, assocLin_eq_zero_of_mem_FF hx,
    (Submodule.Quotient.mk_eq_zero _).2 (primDef_mem_FF2 hx), Prod.mk_zero_zero]

/-- **The obstruction-theory equivalence.** For `ε(E) = ε(Φ) = 1` and `d ≥ 1`, `Φ` has a
correction `x ∈ FF d` with `Φ + x` a group-like associator modulo degree `d + 1` iff its
obstruction lies in the image of `obsLin d` on `FF d`. -/
theorem lift_iff_obsLin {d : ℕ} (hd : 1 ≤ d) {E Φ : F2} (hE : FreeAlgebra.algebraMapInv E = 1)
    (hΦ : FreeAlgebra.algebraMapInv Φ = 1) :
    (∃ x ∈ FF d, AssocU4 (d + 1) E (Φ + x) ∧ GL (d + 1) (Φ + x)) ↔
      ∃ x ∈ FF d, obsLin d x = obstruction d E Φ := by
  have hΦ1 := sub_one_mem_FF_one hΦ
  refine exists_congr fun x => and_congr_right fun hx => ?_
  rw [obsLin_eq_obstruction_iff, assocU4_add_iff hd hE hΦ hx, GL_add_iff hd hΦ1 hx]

/-- The solution may be taken homogeneous of degree `d`. -/
theorem lift_iff_homog {d : ℕ} (hd : 1 ≤ d) {E Φ : F2} (hE : FreeAlgebra.algebraMapInv E = 1)
    (hΦ : FreeAlgebra.algebraMapInv Φ = 1) :
    (∃ x ∈ FF d, AssocU4 (d + 1) E (Φ + x) ∧ GL (d + 1) (Φ + x)) ↔
      ∃ x ∈ FF d, Homog d x ∧ obsLin d x = obstruction d E Φ := by
  rw [lift_iff_obsLin hd hE hΦ]
  constructor
  · rintro ⟨x, hx, hl⟩
    obtain ⟨h, hhF, hh, hxh⟩ := exists_homog_part hx
    refine ⟨h, hhF, hh, ?_⟩
    have e : h = x - (x - h) := by abel
    rw [e, map_sub, obsLin_eq_zero_of_mem_FF hxh, sub_zero, hl]
  · rintro ⟨x, hx, -, hl⟩
    exact ⟨x, hx, hl⟩

/-- **The primitive form.** If `Φ` is already group-like modulo `FF2 (d + 1)`, a lift exists iff
there is a homogeneous primitive `h` of degree `d` with `assocLin (d + 1) h = −assocDefect`. -/
theorem lift_iff_primitive {d : ℕ} (hd : 1 ≤ d) {E Φ : F2}
    (hE : FreeAlgebra.algebraMapInv E = 1) (hΦ : FreeAlgebra.algebraMapInv Φ = 1)
    (hgl : GL (d + 1) Φ) :
    (∃ x ∈ FF d, AssocU4 (d + 1) E (Φ + x) ∧ GL (d + 1) (Φ + x)) ↔
      ∃ h ∈ FF d, Homog d h ∧ IsPrimitive h ∧
        assocLin (d + 1) h = -assocDefect (d + 1) E Φ := by
  rw [lift_iff_homog hd hE hΦ]
  constructor
  · rintro ⟨x, hx, hxh, hl⟩
    obtain ⟨ha, hg⟩ := obsLin_eq_obstruction_iff.1 hl
    have hδ : primDef x ∈ FF2 (d + 1) := by
      have e : primDef x = (glDefect Φ + primDef x) - glDefect Φ := by abel
      rw [e]; exact sub_mem hg hgl
    obtain ⟨h, hh, hxh', hp⟩ := exists_primitive_layer hx hδ
    have hz : x - h = 0 := eq_zero_of_homog_mem_FF (hxh.sub' hh) hxh'
    rw [sub_eq_zero.1 hz] at hx ha
    exact ⟨h, hx, hh, hp, ha⟩
  · rintro ⟨h, hF, hh, hp, ha⟩
    refine ⟨h, hF, hh, obsLin_eq_obstruction_iff.2 ⟨ha, ?_⟩⟩
    rw [(isPrimitive_iff h).1 hp, add_zero]
    exact hgl

/-! ### Field independence -/

/-- `obsLin` on the unknowns `FF d`. -/
noncomputable def obsFF (d : ℕ) : FF d →ₗ[ℚ] ObsTarget d := (obsLin d).domRestrict (FF d)

/-- The lifting equation of `Φ` at degree `d` is solvable after base change to `K`. -/
def LiftSolvableOver (K : Type*) [CommRing K] [Algebra ℚ K] (d : ℕ) (E Φ : F2) : Prop :=
  ∃ z : K ⊗[ℚ] FF d, (obsFF d).baseChange K z = (1 : K) ⊗ₜ obstruction d E Φ

/-- **Field independence.** Over any nontrivial commutative `ℚ`-algebra `K` (for instance a field
`K ⊇ ℚ`, such as `ℂ`), the lifting equation is solvable iff it is solvable over `ℚ`. -/
theorem liftSolvableOver_iff (K : Type*) [CommRing K] [Nontrivial K] [Algebra ℚ K] {d : ℕ}
    {E Φ : F2} : LiftSolvableOver K d E Φ ↔ ∃ x ∈ FF d, obsLin d x = obstruction d E Φ := by
  constructor
  · intro h
    obtain ⟨v, hv⟩ := exists_of_baseChange (obsFF d) _ h
    exact ⟨v.1, v.2, hv⟩
  · rintro ⟨x, hx, hl⟩
    refine ⟨(1 : K) ⊗ₜ ⟨x, hx⟩, ?_⟩
    rw [LinearMap.baseChange_tmul]
    exact congrArg _ hl

/-- **A rational lift exists iff the equation is solvable over some (any) nontrivial `K`.** -/
theorem lift_iff_liftSolvableOver (K : Type*) [CommRing K] [Nontrivial K] [Algebra ℚ K]
    {d : ℕ} (hd : 1 ≤ d) {E Φ : F2} (hE : FreeAlgebra.algebraMapInv E = 1)
    (hΦ : FreeAlgebra.algebraMapInv Φ = 1) :
    (∃ x ∈ FF d, AssocU4 (d + 1) E (Φ + x) ∧ GL (d + 1) (Φ + x)) ↔ LiftSolvableOver K d E Φ := by
  rw [lift_iff_obsLin hd hE hΦ, liftSolvableOver_iff]

/-- **A `K`-associator kills the obstruction.** If a group-like `K`-associator modulo some
`N ≥ d + 1` agrees with `1 ⊗ Φ` modulo `FFK d`, the obstruction of `Φ` at degree `d` lies in the
image of `obsLin d` over `ℚ`. -/
theorem obstruction_mem_range_of_groupLikeK {K : Type*} [Field K] [Algebra ℚ K] {d N : ℕ}
    (hd : 1 ≤ d) (hdN : d + 1 ≤ N) {E Φ : F2} (hE : FreeAlgebra.algebraMapInv E = 1)
    (hΦ : FreeAlgebra.algebraMapInv Φ = 1) {Ψ : K ⊗[ℚ] F2} (hK : AssocK K N E Ψ)
    (hGL : GLK K N Ψ) (hm : Ψ - (1 : K) ⊗ₜ Φ ∈ FFK K d) :
    ∃ x ∈ FF d, obsLin d x = obstruction d E Φ := by
  obtain ⟨z, rfl⟩ := exists_lTensor_of_mem_FFK hm
  obtain ⟨x, hx, ha, hg, -⟩ :=
    inductionStep_of_groupLike hd hdN (by omega : 2 ≤ N) le_rfl hE hΦ z hK hGL
  exact (lift_iff_obsLin hd hE hΦ).1 ⟨x, hx, ha, hg⟩

/-! ### The open statement, and what it gives -/

/-- **The obstruction vanishes at every degree** (the precise remaining statement; a `Prop`,
not an axiom, and not proved here). For every `d ≥ 1` and every rational associator `Φ` modulo
degree `d` for `E` that is group-like modulo `FF2 d`, the obstruction of `Φ` at degree `d` lies
in the image of `obsLin d` on `FF d`. By `lift_iff_obsLin` this says every group-like rational
associator modulo `d` extends to one modulo `d + 1`; by `liftSolvableOver_iff` it is the same
statement over any field `K ⊇ ℚ`. -/
def AssociatorObstructionVanishes (E : F2) : Prop :=
  ∀ d : ℕ, 1 ≤ d → ∀ Φ : F2, AssocU4 d E Φ → GL d Φ →
    ∃ x ∈ FF d, obsLin d x = obstruction d E Φ

/-- `1` is a group-like associator modulo degree `1` (every `tᵢⱼ` is `0` in `U4 1`). -/
theorem assocU4_one_one {E : F2} (hE : FreeAlgebra.algebraMapInv E = 1) : AssocU4 1 E 1 := by
  have ht : ∀ i, t 1 i = 0 := fun i => eq_zero_of_mem_Fil (t_mem_Fil_one i)
  have hE0 : eval (0 : U4 1) 0 E = 1 := by rw [eval_zero_zero, hE, map_one]
  refine ⟨map_one _, fun a b _ _ => by simp, ?_, ?_⟩
  · simp only [Hexagon, map_one, one_mul, ht, add_zero, hE0]
  · simp [Pentagon]

theorem GL_one_one : GL 1 (1 : F2) := by
  unfold GL
  rw [map_one, Algebra.TensorProduct.one_def, sub_self]
  exact zero_mem _

/-- **The open statement gives the compatible rational tower, with no field `K`.** -/
theorem compatible_of_obstructionVanishes {E : F2} (hE : FreeAlgebra.algebraMapInv E = 1)
    (hV : AssociatorObstructionVanishes E) :
    ∃ Φ : ℕ → F2, (∀ N, 1 ≤ N → AssocU4 N E (Φ N) ∧ GL N (Φ N)) ∧
      ∀ N, 1 ≤ N → Φ (N + 1) - Φ N ∈ FF N := by
  obtain ⟨f, -, hf⟩ := exists_seq_of_step (α := F2)
    (fun k a => AssocU4 (k + 1) E a ∧ GL (k + 1) a)
    (fun k a b => b - a ∈ FF (k + 1))
    (a₀ := 1) ⟨assocU4_one_one hE, GL_one_one⟩ (fun k a ha => by
      obtain ⟨x, hx, hl⟩ := hV (k + 1) (by omega) a ha.1 ha.2
      obtain ⟨y, hy, hA, hG⟩ :=
        (lift_iff_obsLin (by omega : 1 ≤ k + 1) hE ha.1.const).2 ⟨x, hx, hl⟩
      exact ⟨a + y, ⟨hA, hG⟩, by simpa using hy⟩)
  refine ⟨fun N => f (N - 1), fun N hN => ?_, fun N hN => ?_⟩
  · obtain ⟨k, rfl⟩ : ∃ k, N = k + 1 := ⟨N - 1, by omega⟩
    simpa using (hf k).1
  · obtain ⟨k, rfl⟩ : ∃ k, N = k + 1 := ⟨N - 1, by omega⟩
    simpa using (hf k).2

end QOU.BraidsAndKnots.RationalAssociator
