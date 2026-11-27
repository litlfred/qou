import QOU.BraidsAndKnots.RationalAssociator.HexagonAction
import Mathlib.RingTheory.Nilpotent.Basic

/-!
# The unit hypotheses are discharged by nilpotence

Bean `qou-3fdg` (stage 3d(a) of the rational-associator plan, epic `qou-dk7p`).

The action theorems of `TransportedDK4.lean`, `FarRelation.lean` and `HexagonAction.lean` take
the coface evaluations `g(a, b)` as units `G`. Here they are constructed.

* `NilIdeal S`: a `ℚ`-submodule `S` of `R` that is a two-sided ideal and consists of nilpotent
  elements.
* `eval_sub_mem`: for `a, b ∈ S`, `eval a b p − ε(p) ∈ S`, where `ε` is the augmentation
  (constant term) `FreeAlgebra.algebraMapInv`.
* `evalUnit`: if moreover `ε(g) = 1`, then `eval a b g = 1 + (element of S)` is a unit.
* `nilIdeal_Fil`: in `U4 N`, `Fil N 1` is such an ideal, because `x ∈ Fil N 1` gives
  `x ^ N ∈ Fil N N = 0`.
* `pentagon_act_U4`, `hexagon_act_U4`: the pentagon and hexagon action theorems in `U4 N`, with
  every unit built by `evalUnit`. The only hypotheses on `g` are `ε(g) = 1`, its pentagon,
  (5.13), (5.14) and `TCompat`.

Nothing analytic is used.
-/

namespace QOU.BraidsAndKnots.RationalAssociator

section Generic

variable {R : Type*} [Ring R] [Algebra ℚ R]

/-- A `ℚ`-submodule that is a two-sided ideal of nilpotent elements. -/
structure NilIdeal (S : Submodule ℚ R) : Prop where
  mul_left : ∀ (x : R) {y : R}, y ∈ S → x * y ∈ S
  mul_right : ∀ {x : R} (y : R), x ∈ S → x * y ∈ S
  nil : ∀ x ∈ S, IsNilpotent x

/-- The augmentation `ε = FreeAlgebra.algebraMapInv` (constant term). For `a, b ∈ S`,
`eval a b p − ε(p) ∈ S`. -/
theorem eval_sub_mem {S : Submodule ℚ R} (hS : NilIdeal S) {a b : R} (ha : a ∈ S) (hb : b ∈ S)
    (p : FreeAlgebra ℚ (Fin 2)) :
    eval a b p - algebraMap ℚ R (FreeAlgebra.algebraMapInv p) ∈ S := by
  induction p using FreeAlgebra.induction with
  | grade0 r => simp
  | grade1 i =>
    fin_cases i
    · simpa [FreeAlgebra.algebraMapInv] using ha
    · simpa [FreeAlgebra.algebraMapInv] using hb
  | mul p q hp hq =>
    have e : eval a b (p * q) - algebraMap ℚ R (FreeAlgebra.algebraMapInv (p * q)) =
        (eval a b p - algebraMap ℚ R (FreeAlgebra.algebraMapInv p)) * eval a b q +
          algebraMap ℚ R (FreeAlgebra.algebraMapInv p) *
            (eval a b q - algebraMap ℚ R (FreeAlgebra.algebraMapInv q)) := by
      simp only [map_mul]; noncomm_ring
    rw [e]
    exact add_mem (hS.mul_right _ hp) (hS.mul_left _ hq)
  | add p q hp hq =>
    have e : eval a b (p + q) - algebraMap ℚ R (FreeAlgebra.algebraMapInv (p + q)) =
        (eval a b p - algebraMap ℚ R (FreeAlgebra.algebraMapInv p)) +
          (eval a b q - algebraMap ℚ R (FreeAlgebra.algebraMapInv q)) := by
      simp only [map_add]; abel
    rw [e]; exact add_mem hp hq

/-- For `a, b ∈ S` and `ε(g) = 1`, `eval a b g` is a unit. -/
theorem isUnit_eval {S : Submodule ℚ R} (hS : NilIdeal S) {a b : R} (ha : a ∈ S) (hb : b ∈ S)
    {g : FreeAlgebra ℚ (Fin 2)} (hg : FreeAlgebra.algebraMapInv g = 1) :
    IsUnit (eval a b g) := by
  have h := eval_sub_mem hS ha hb g
  rw [hg, map_one] at h
  have := (hS.nil _ h).isUnit_one_add
  simpa using this

/-- The unit `g(a, b)`. -/
noncomputable def evalUnit {S : Submodule ℚ R} (hS : NilIdeal S) {a b : R} (ha : a ∈ S)
    (hb : b ∈ S) {g : FreeAlgebra ℚ (Fin 2)} (hg : FreeAlgebra.algebraMapInv g = 1) : Rˣ :=
  (isUnit_eval hS ha hb hg).unit

@[simp] theorem val_evalUnit {S : Submodule ℚ R} (hS : NilIdeal S) {a b : R} (ha : a ∈ S)
    (hb : b ∈ S) {g : FreeAlgebra ℚ (Fin 2)} (hg : FreeAlgebra.algebraMapInv g = 1) :
    (evalUnit hS ha hb hg : R) = eval a b g :=
  IsUnit.unit_spec _

end Generic

section U4

variable {N : ℕ}

theorem pow_mem_Fil {x : U4 N} (hx : x ∈ Fil N 1) (k : ℕ) : x ^ k ∈ Fil N k := by
  induction k with
  | zero => exact mem_Fil_zero _
  | succ k ih => rw [pow_succ]; exact mul_mem_Fil ih hx

/-- In `U4 N`, `Fil N 1` is a two-sided ideal of nilpotent elements. -/
theorem nilIdeal_Fil : NilIdeal (Fil N 1) where
  mul_left := fun x {_} hy => by simpa using mul_mem_Fil (mem_Fil_zero x) hy
  mul_right := fun {_} y hx => by simpa using mul_mem_Fil hx (mem_Fil_zero y)
  nil x hx := ⟨N, eq_zero_of_mem_Fil (pow_mem_Fil hx N)⟩

/-- A sum of generators of `U4 N`. -/
noncomputable def genSum (N : ℕ) (l : List (Fin 6)) : U4 N := (l.map (t N)).sum

theorem genSum_mem (l : List (Fin 6)) : genSum N l ∈ Fil N 1 := by
  induction l with
  | nil => simp [genSum]
  | cons i l ih => simpa [genSum] using add_mem (t_mem_Fil_one (N := N) i) ih

/-- The unit `g(Σ_{i∈l} tᵢ, Σ_{j∈m} tⱼ)` of `U4 N`, for `g` with constant term `1`. -/
noncomputable def gU (N : ℕ) {g : FreeAlgebra ℚ (Fin 2)} (hg : FreeAlgebra.algebraMapInv g = 1)
    (l m : List (Fin 6)) : (U4 N)ˣ :=
  evalUnit nilIdeal_Fil (genSum_mem l) (genSum_mem m) hg

@[simp] theorem val_gU {g : FreeAlgebra ℚ (Fin 2)} (hg : FreeAlgebra.algebraMapInv g = 1)
    (l m : List (Fin 6)) : (gU N hg l m : U4 N) = eval (genSum N l) (genSum N m) g := by
  simp [gU]

/-- **The pentagon action theorem in `U4 N`, units discharged.** For `g` with constant term `1`
satisfying the pentagon, (5.13) at `(t₃₄,t₂₃)` and `(t₂₄,t₂₃)`, and `TCompat` at
`(t₁₂,t₁₃,t₂₃)` and `(t₃₄,t₂₄,t₂₃)`, the pentagon of `φ` implies the pentagon of
`φ̃ = φ(g A g⁻¹, B) · g`. Indices: `t₁₂ t₁₃ t₁₄ t₂₃ t₂₄ t₃₄ = 0 1 2 3 4 5`. -/
theorem pentagon_act_U4 (φ g : FreeAlgebra ℚ (Fin 2)) (hg1 : FreeAlgebra.algebraMapInv g = 1)
    (hg : Pentagon g (t N 0) (t N 1) (t N 3) (t N 4) (t N 5))
    (hφ : Pentagon φ (t N 0) (t N 1) (t N 3) (t N 4) (t N 5))
    (hu1 : eval (t N 5) (t N 3) g * eval (t N 3) (t N 5) g = 1)
    (hu2 : eval (t N 4) (t N 3) g * eval (t N 3) (t N 4) g = 1)
    (hA : TCompat (t N 1) (t N 3) (gU N hg1 [0] [3]) (gU N hg1 [1] [3]))
    (hB : TCompat (t N 4) (t N 3) (gU N hg1 [5] [3]) (gU N hg1 [4] [3])) :
    actEval φ (t N 0) (t N 3 + t N 4) (gU N hg1 [0] [3, 4]) *
        actEval φ (t N 1 + t N 3) (t N 5) (gU N hg1 [1, 3] [5]) =
      actEval φ (t N 3) (t N 5) (gU N hg1 [3] [5]) *
          actEval φ (t N 0 + t N 1) (t N 4 + t N 5) (gU N hg1 [0, 1] [4, 5]) *
        actEval φ (t N 0) (t N 3) (gU N hg1 [0] [3]) :=
  pentagon_act_universal_of_tcompat φ g _ _ _ _ _ (gU N hg1 [1] [3]) (gU N hg1 [3] [4])
    (gU N hg1 [1] [3, 5]) (gU N hg1 [0, 3] [4]) (gU N hg1 [5] [3]) (gU N hg1 [4] [3])
    (by simp [genSum]) (by simp [genSum]) (by simp [genSum]) (by simp [genSum]) (by simp [genSum])
    (by simp [genSum]) (by simp [genSum]) (by simp [genSum]) (by simp [genSum]) (by simp [genSum])
    (by simp [genSum]) hg hφ hu1 hu2 hA hB

/-- **The hexagon action theorem in `U4 N`, units discharged**, at the three-strand family
`(t₁₂, t₁₃, t₂₃)`. For `g` with constant term `1` satisfying (5.13) at `(t₂₃,t₁₂)`, (5.14) and
`TCompat` at `(t₂₃,t₁₃,t₁₂)`, the hexagon of `φ` at the transported family
`(t₁₂, G₁ t₁₃ G₁⁻¹, G₃⁻¹ t₂₃ G₃)` implies the hexagon of `φ̃` at `(t₁₂, t₁₃, t₂₃)`. -/
theorem hexagon_act_U4 (φ g E : FreeAlgebra ℚ (Fin 2)) (hg1 : FreeAlgebra.algebraMapInv g = 1)
    (h513 : eval (t N 3) (t N 0) g * eval (t N 0) (t N 3) g = 1)
    (h514 : eval (t N 3) (t N 1) g * eval (t N 0) (t N 3) g * eval (t N 1) (t N 0) g = 1)
    (htc : TCompat (t N 1) (t N 0) (gU N hg1 [3] [0]) (gU N hg1 [1] [0]))
    (hφ : Hexagon φ E (t N 0)
      ((gU N hg1 [1] [0] : U4 N) * t N 1 * ↑(gU N hg1 [1] [0])⁻¹)
      ((↑(gU N hg1 [0] [3])⁻¹ : U4 N) * t N 3 * gU N hg1 [0] [3])) :
    eval (t N 1 + t N 3) 0 E =
      actEval φ (t N 1) (t N 0) (gU N hg1 [1] [0]) * eval (t N 1) 0 E *
        actEval φ (t N 3) (t N 1) (gU N hg1 [3] [1]) * eval (t N 3) 0 E *
          actEval φ (t N 0) (t N 3) (gU N hg1 [0] [3]) :=
  hexagon_act φ g E (dk4 N).d4 _ _ _ (gU N hg1 [3] [0])
    (by simp [genSum]) (by simp [genSum]) (by simp [genSum]) (by simp [genSum]) h513 h514 htc hφ

end U4

end QOU.BraidsAndKnots.RationalAssociator
