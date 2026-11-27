import QOU.BraidsAndKnots.RationalAssociator.NilpotentUnits

/-!
# The hexagon action theorem from the universal hexagon

Bean `qou-3fdg` (stage 3d of the rational-associator plan, epic `qou-dk7p`).

`hexagon_act_U4` (`NilpotentUnits.lean`) takes the hexagon of `φ` at the transported family
`s = (t₁₂, G₁ t₁₃ G₁⁻¹, G₃⁻¹ t₂₃ G₃)`. Here that hypothesis is derived from the hexagon of `φ`
at the universal family `(t₁₂, t₁₃, t₂₃)` of `U4 N`, so no 3-strand universal algebra is needed.

* `DK3.toDK4`: a `DK3` family `(a, b, c)` extends to the `DK4` family `(a, b, 0, c, 0, 0)`.
* `hexagon_of_universal`: the hexagon of `φ` at `(t₁₂, t₁₃, t₂₃)` in `U4 N` implies the hexagon
  of `φ` at every `DK3` family of `U4 N` lying in `Fil N 1`. The map is `lift` applied to the
  extended family.
* `hexagon_act_U4_universal`: in `U4 N`, for `g` with constant term `1` satisfying (5.12),
  (5.13) and (5.14) in Drinfeld's numbering, the hexagon of `φ` implies the hexagon of
  `φ̃ = φ(g A g⁻¹, B) · g`.

**Numbering.** Drinfeld (1991, §5) numbers the defining conditions of `GRT₁` as (5.12)
`g(B,A) = g(A,B)⁻¹`, (5.13) `g(C,A) g(B,C) g(A,B) = 1`, (5.14)
`A + g(A,B)⁻¹ B g(A,B) + g(A,C)⁻¹ C g(A,C) = 0` (all for `A + B + C = 0`), and (5.15) the
pentagon. Earlier files of this directory call the first two "(5.13)" and "(5.14)"; the third is
`TCompat`. So `TCompat` is one of Drinfeld's defining conditions of `GRT₁`, not an extra
hypothesis. Nothing analytic is used.
-/

namespace QOU.BraidsAndKnots.RationalAssociator

section Extend

variable {R : Type*} [Ring R]

/-- A `DK3` family extends by zeros to a `DK4` family. -/
theorem DK3.toDK4 {a b c : R} (h : DK3 a b c) : DK4 a b 0 c 0 0 where
  f12_34 := Commute.zero_right a
  f13_24 := Commute.zero_right b
  f14_23 := Commute.zero_left c
  n12_3 := h.n12_3
  n13_2 := h.n13_2
  n23_1 := h.n23_1
  n12_4 := by simp
  n14_2 := Commute.zero_left _
  n24_1 := Commute.zero_left _
  n13_4 := by simp
  n14_3 := Commute.zero_left _
  n34_1 := Commute.zero_left _
  n23_4 := by simp
  n24_3 := Commute.zero_left _
  n34_2 := Commute.zero_left _

end Extend

section U4

variable {N : ℕ}

/-- **The universal hexagon specialises to every nilpotent `DK3` family of `U4 N`.** -/
theorem hexagon_of_universal (φ E : FreeAlgebra ℚ (Fin 2))
    (hφ : Hexagon φ E (t N 0) (t N 1) (t N 3)) {s12 s13 s23 : U4 N} (hs : DK3 s12 s13 s23)
    (h12 : s12 ∈ Fil N 1) (h13 : s13 ∈ Fil N 1) (h23 : s23 ∈ Fil N 1) :
    Hexagon φ E s12 s13 s23 := by
  set sf : Fin 6 → U4 N := ![s12, s13, 0, s23, 0, 0] with hsf
  have hdk : DK4 (sf 0) (sf 1) (sf 2) (sf 3) (sf 4) (sf 5) := hs.toDK4
  have hmem : ∀ i, sf i ∈ Fil N 1 := by
    intro i
    fin_cases i
    · exact h12
    · exact h13
    · exact zero_mem _
    · exact h23
    · exact zero_mem _
    · exact zero_mem _
  have hw := word_eq_zero_of_Fil_one sf hmem
  have key := congrArg (lift N sf hdk hw) hφ
  simp only [map_mul, map_eval, map_add, lift_t, map_zero] at key
  exact key

/-- **The hexagon action theorem in `U4 N`, from the universal hexagon.** For `g` with constant
term `1` satisfying `g(t₂₃,t₁₂) g(t₁₂,t₂₃) = 1`, `g(t₂₃,t₁₃) g(t₁₂,t₂₃) g(t₁₃,t₁₂) = 1` and
`TCompat` at `(t₂₃, t₁₃, t₁₂)`, the hexagon of `φ` at `(t₁₂, t₁₃, t₂₃)` implies the hexagon of
`φ̃` there. -/
theorem hexagon_act_U4_universal (φ g E : FreeAlgebra ℚ (Fin 2))
    (hg1 : FreeAlgebra.algebraMapInv g = 1)
    (h513 : eval (t N 3) (t N 0) g * eval (t N 0) (t N 3) g = 1)
    (h514 : eval (t N 3) (t N 1) g * eval (t N 0) (t N 3) g * eval (t N 1) (t N 0) g = 1)
    (htc : TCompat (t N 1) (t N 0) (gU N hg1 [3] [0]) (gU N hg1 [1] [0]))
    (hφ : Hexagon φ E (t N 0) (t N 1) (t N 3)) :
    eval (t N 1 + t N 3) 0 E =
      actEval φ (t N 1) (t N 0) (gU N hg1 [1] [0]) * eval (t N 1) 0 E *
        actEval φ (t N 3) (t N 1) (gU N hg1 [3] [1]) * eval (t N 3) 0 E *
          actEval φ (t N 0) (t N 3) (gU N hg1 [0] [3]) := by
  have hDK := (dk4 N).d4
  have h1 : (gU N hg1 [1] [0] : U4 N) = eval (t N 1) (t N 0) g := by simp [genSum]
  have h3 : (gU N hg1 [0] [3] : U4 N) = eval (t N 0) (t N 3) g := by simp [genSum]
  have hK : (gU N hg1 [3] [0] : U4 N) = eval (t N 3) (t N 0) g := by simp [genSum]
  have hsum := transported3_sum g hDK (gU N hg1 [1] [0]) (gU N hg1 [0] [3]) (gU N hg1 [3] [0])
    h3 hK h513 htc
  refine hexagon_act_U4 φ g E hg1 h513 h514 htc ?_
  refine hexagon_of_universal φ E hφ
    (transported3_dk3 g hDK (gU N hg1 [1] [0]) (gU N hg1 [0] [3]) h1 h3 hsum)
    (t_mem_Fil_one 0) ?_ (conj_mem_Fil_one _ (t_mem_Fil_one 3))
  simpa using conj_mem_Fil_one (gU N hg1 [1] [0])⁻¹ (t_mem_Fil_one (N := N) 1)

end U4

end QOU.BraidsAndKnots.RationalAssociator
