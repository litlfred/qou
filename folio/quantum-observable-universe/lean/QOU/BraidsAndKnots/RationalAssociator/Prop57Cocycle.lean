import QOU.BraidsAndKnots.RationalAssociator.Prop57

/-!
# Drinfeld Prop. 5.7, step 1: the cocycle identity

Drinfeld proves (5.17), (5.18), (5.20) ⇒ (5.19) for `ψ ∈ grt` by showing that
`s(B, C) = [B, ψ(A, B)] + [C, ψ(A, C)]`, `A = -B - C`, is a symmetric cocycle (5.24) and then
that a symmetric cocycle vanishes. The vanishing half is `vanishing_of_cocycle` in `Prop57`.
This file proves the algebraic identity behind the cocycle half.

Write `e a b` for `ψ(a, b)` and
`S(A, B, C) = [B, e A B] + [C, e A C]`. At a four-strand Drinfeld–Kohno family put

`u = S(t₁₂, t₁₄, t₂₄) - S(t₁₂+t₁₃, t₁₄, t₂₄+t₃₄) + S(t₁₃+t₂₃, t₁₄+t₂₄, t₃₄) - S(t₂₃, t₂₄, t₃₄)`

and let `μ^{abcd}` be the linearised pentagon defect (5.20) on strands `a, b, c, d`:

`μ^{abcd} = e(t_ab, t_bc+t_bd) + e(t_ac+t_bc, t_cd) - e(t_bc, t_cd) - e(t_ab+t_ac, t_bd+t_cd) - e(t_ab, t_bc)`.

`cocycle_identity`: if `e` is antisymmetric (5.17) on a submodule containing the generators,
satisfies the linearised hexagon (5.18) at every Drinfeld–Kohno triple in it, and `e a b`
commutes with everything that commutes with `a` and `b`, then

`u = -[t₁₂+t₁₃+t₂₃, μ^{1234}] - [t₁₄+t₂₄, μ^{1243}] + [t₁₄, μ^{1423}]`.

So the pentagon (5.20) at the three strand orders forces `u = 0`. No Lie hypothesis on `ψ` and
no central shift is used. The relation list (four hexagon instances bracketed with `t₁₄` or
`t₁₄+t₂₄`, ten commuting facts) was found by solving a linear system over ℚ; the proof checks it
with `noncomm_ring`.
-/

namespace QOU.BraidsAndKnots.RationalAssociator

namespace DK3

variable {R : Type*} [Ring R] {a b c : R}

theorem swap12 (h : DK3 a b c) : DK3 b a c :=
  ⟨h.n13_2, h.n12_3, by rw [add_comm]; exact h.n23_1⟩

theorem rot (h : DK3 a b c) : DK3 c a b :=
  ⟨h.n23_1, by rw [add_comm]; exact h.n12_3, by rw [add_comm]; exact h.n13_2⟩

end DK3

/-- Membership of a sum of generators in a submodule. -/
local macro "p57_mem" : tactic => `(tactic| ((repeat' apply Submodule.add_mem) <;> assumption))

/-- The cocycle identity behind Drinfeld (5.24): `u` is a combination of brackets with the
three linearised pentagon defects. See the module docstring. -/
theorem cocycle_identity {R : Type*} [Ring R] [Algebra ℚ R] (e : R → R → R) (I : Submodule ℚ R)
    {t12 t13 t14 t23 t24 t34 : R} (h : DK4 t12 t13 t14 t23 t24 t34)
    (h12 : t12 ∈ I) (h13 : t13 ∈ I) (h14 : t14 ∈ I) (h23 : t23 ∈ I) (h24 : t24 ∈ I) (h34 : t34 ∈ I)
    (hanti : ∀ a b, a ∈ I → b ∈ I → e a b + e b a = 0)
    (hhex : ∀ a b c, a ∈ I → b ∈ I → c ∈ I → DK3 a b c → e b a + e c b + e a c = 0)
    (hcomm : ∀ m a b, Commute m a → Commute m b → Commute m (e a b)) :
    ((t14 * (e t12 t14) - (e t12 t14) * t14) + (t24 * (e t12 t24) - (e t12 t24) * t24)) - ((t14 * (e (t12 + t13) t14) - (e (t12 + t13) t14) * t14) + ((t24 + t34) * (e (t12 + t13) (t24 + t34)) - (e (t12 + t13) (t24 + t34)) * (t24 + t34))) + (((t14 + t24) * (e (t13 + t23) (t14 + t24)) - (e (t13 + t23) (t14 + t24)) * (t14 + t24)) + (t34 * (e (t13 + t23) t34) - (e (t13 + t23) t34) * t34)) - ((t24 * (e t23 t24) - (e t23 t24) * t24) + (t34 * (e t23 t34) - (e t23 t34) * t34)) =
      -((t12 + t13 + t23) * ((e t12 (t23 + t24) + e (t13 + t23) t34 - e t23 t34 - e (t12 + t13) (t24 + t34) - e t12 t23)) - ((e t12 (t23 + t24) + e (t13 + t23) t34 - e t23 t34 - e (t12 + t13) (t24 + t34) - e t12 t23)) * (t12 + t13 + t23)) - ((t14 + t24) * ((e t12 (t23 + t24) + e (t14 + t24) t34 - e t24 t34 - e (t12 + t14) (t23 + t34) - e t12 t24)) - ((e t12 (t23 + t24) + e (t14 + t24) t34 - e t24 t34 - e (t12 + t14) (t23 + t34) - e t12 t24)) * (t14 + t24)) + (t14 * ((e t14 (t24 + t34) + e (t12 + t24) t23 - e t24 t23 - e (t12 + t14) (t23 + t34) - e t14 t24)) - ((e t14 (t24 + t34) + e (t12 + t24) t23 - e t24 t23 - e (t12 + t14) (t23 + t34) - e t14 t24)) * t14) := by
  have a0 : e t24 t34 = -e t34 t24 := eq_neg_of_add_eq_zero_left (hanti _ _ (by p57_mem) (by p57_mem))
  have a1 : e t23 t34 = -e t34 t23 := eq_neg_of_add_eq_zero_left (hanti _ _ (by p57_mem) (by p57_mem))
  have a2 : e t23 t24 = -e t24 t23 := eq_neg_of_add_eq_zero_left (hanti _ _ (by p57_mem) (by p57_mem))
  have a3 : e t14 t24 = -e t24 t14 := eq_neg_of_add_eq_zero_left (hanti _ _ (by p57_mem) (by p57_mem))
  have a4 : e t14 (t24 + t34) = -e (t24 + t34) t14 := eq_neg_of_add_eq_zero_left (hanti _ _ (by p57_mem) (by p57_mem))
  have a5 : e (t14 + t24) t34 = -e t34 (t14 + t24) := eq_neg_of_add_eq_zero_left (hanti _ _ (by p57_mem) (by p57_mem))
  have a6 : e (t13 + t23) t34 = -e t34 (t13 + t23) := eq_neg_of_add_eq_zero_left (hanti _ _ (by p57_mem) (by p57_mem))
  have a7 : e (t13 + t23) (t14 + t24) = -e (t14 + t24) (t13 + t23) := eq_neg_of_add_eq_zero_left (hanti _ _ (by p57_mem) (by p57_mem))
  have a8 : e t12 t24 = -e t24 t12 := eq_neg_of_add_eq_zero_left (hanti _ _ (by p57_mem) (by p57_mem))
  have a9 : e t12 t23 = -e t23 t12 := eq_neg_of_add_eq_zero_left (hanti _ _ (by p57_mem) (by p57_mem))
  have a10 : e t12 (t23 + t24) = -e (t23 + t24) t12 := eq_neg_of_add_eq_zero_left (hanti _ _ (by p57_mem) (by p57_mem))
  have a11 : e t12 t14 = -e t14 t12 := eq_neg_of_add_eq_zero_left (hanti _ _ (by p57_mem) (by p57_mem))
  have a12 : e (t12 + t24) t23 = -e t23 (t12 + t24) := eq_neg_of_add_eq_zero_left (hanti _ _ (by p57_mem) (by p57_mem))
  have a13 : e (t12 + t14) (t23 + t34) = -e (t23 + t34) (t12 + t14) := eq_neg_of_add_eq_zero_left (hanti _ _ (by p57_mem) (by p57_mem))
  have a14 : e (t12 + t13) (t24 + t34) = -e (t24 + t34) (t12 + t13) := eq_neg_of_add_eq_zero_left (hanti _ _ (by p57_mem) (by p57_mem))
  have a15 : e (t12 + t13) t14 = -e t14 (t12 + t13) := eq_neg_of_add_eq_zero_left (hanti _ _ (by p57_mem) (by p57_mem))
  have H0 : (e t14 t12 + e t24 t14 + (-e t24 t12)) = 0 := by
    rw [← hhex t12 t14 t24 (by p57_mem) (by p57_mem) (by p57_mem) ⟨h.n12_4, h.n14_2, h.n24_1⟩]; simp only [a8]
  have H1 : ((-e t14 (t12 + t13)) + e (t24 + t34) (t12 + t13) + (-e (t24 + t34) t14)) = 0 := by
    rw [← hhex t14 (t12 + t13) (t24 + t34) (by p57_mem) (by p57_mem) (by p57_mem) h.d2.swap12]; simp only [a15, a4]
  have H2 : (e t24 t23 + e t34 t24 + (-e t34 t23)) = 0 := by
    rw [← hhex t23 t24 t34 (by p57_mem) (by p57_mem) (by p57_mem) h.d0]; simp only [a1]
  have H3 : ((-e t34 (t13 + t23)) + e (t14 + t24) (t13 + t23) + e t34 (t14 + t24)) = 0 := by
    rw [← hhex t34 (t13 + t23) (t14 + t24) (by p57_mem) (by p57_mem) (by p57_mem) h.d1.rot]; simp only [a6]
  have C0 : t12 * (e t34 (t13 + t23)) - (e t34 (t13 + t23)) * t12 = 0 := sub_eq_zero.mpr (hcomm _ _ _ h.f12_34 h.n12_3).eq
  have C1 : t23 * (e (t24 + t34) (t12 + t13)) - (e (t24 + t34) (t12 + t13)) * t23 = 0 := sub_eq_zero.mpr (hcomm _ _ _ h.n23_4 h.n23_1).eq
  have C2 : (t12 + t13 + t23) * (e t23 t12) - (e t23 t12) * (t12 + t13 + t23) = 0 := sub_eq_zero.mpr (hcomm _ _ _ (h.n23_1.symm.add_left (Commute.refl t23)) (by rw [add_assoc]; exact (Commute.refl t12).add_left h.n12_3.symm)).eq
  have C3 : t14 * (e t23 (t12 + t24)) - (e t23 (t12 + t24)) * t14 = 0 := sub_eq_zero.mpr (hcomm _ _ _ h.f14_23 h.n14_2).eq
  have C4 : t24 * (e (t23 + t34) (t12 + t14)) - (e (t23 + t34) (t12 + t14)) * t24 = 0 := sub_eq_zero.mpr (hcomm _ _ _ h.n24_3 h.n24_1).eq
  have C5 : (t23 + t24 + t34) * (e t34 t23) - (e t34 t23) * (t23 + t24 + t34) = 0 := sub_eq_zero.mpr (hcomm _ _ _ (h.n34_2.symm.add_left (Commute.refl t34)) (by rw [add_assoc]; exact (Commute.refl t23).add_left h.n23_4.symm)).eq
  have C6 : (t12 + t13 + t14) * (e t34 t23) - (e t34 t23) * (t12 + t13 + t14) = 0 := sub_eq_zero.mpr (hcomm _ _ _ (by rw [add_assoc]; exact h.f12_34.add_left h.n34_1.symm) (h.n23_1.symm.add_left h.f14_23)).eq
  have C7 : (t13 + t14 + t23 + t24 + t34) * (e t34 (t13 + t23)) - (e t34 (t13 + t23)) * (t13 + t14 + t23 + t24 + t34) = 0 := sub_eq_zero.mpr (hcomm _ _ _ (by rw [show t13 + t14 + t23 + t24 + t34 = (t13 + t14) + (t23 + t24) + t34 by abel]; exact (h.n34_1.symm.add_left h.n34_2.symm).add_left (Commute.refl _)) (by rw [show t13 + t14 + t23 + t24 + t34 = (t13 + t23) + ((t14 + t24) + t34) by abel]; exact (Commute.refl _).add_left h.d1.n12_3.symm)).eq
  have C8 : (t12 + t13 + t14 + t24 + t34) * (e (t24 + t34) (t12 + t13)) - (e (t24 + t34) (t12 + t13)) * (t12 + t13 + t14 + t24 + t34) = 0 := sub_eq_zero.mpr (hcomm _ _ _ (by rw [show t12 + t13 + t14 + t24 + t34 = (t12 + t13 + t14) + (t24 + t34) by abel]; exact h.d2.n23_1.symm.add_left (Commute.refl _)) (by rw [show t12 + t13 + t14 + t24 + t34 = (t12 + t13) + (t14 + (t24 + t34)) by abel]; exact (Commute.refl _).add_left h.d2.n12_3.symm)).eq
  have C9 : (t12 + t13 + t14 + t23 + t24) * (e (t23 + t24) t12) - (e (t23 + t24) t12) * (t12 + t13 + t14 + t23 + t24) = 0 := sub_eq_zero.mpr (hcomm _ _ _ (by rw [show t12 + t13 + t14 + t23 + t24 = (t12 + (t13 + t14)) + (t23 + t24) by abel]; exact h.d3.n23_1.symm.add_left (Commute.refl _)) (by rw [show t12 + t13 + t14 + t23 + t24 = t12 + ((t13 + t14) + (t23 + t24)) by abel]; exact (Commute.refl _).add_left h.d3.n12_3.symm)).eq
  rw [← sub_eq_zero]
  have key : (((t14 * (e t12 t14) - (e t12 t14) * t14) + (t24 * (e t12 t24) - (e t12 t24) * t24)) - ((t14 * (e (t12 + t13) t14) - (e (t12 + t13) t14) * t14) + ((t24 + t34) * (e (t12 + t13) (t24 + t34)) - (e (t12 + t13) (t24 + t34)) * (t24 + t34))) + (((t14 + t24) * (e (t13 + t23) (t14 + t24)) - (e (t13 + t23) (t14 + t24)) * (t14 + t24)) + (t34 * (e (t13 + t23) t34) - (e (t13 + t23) t34) * t34)) - ((t24 * (e t23 t24) - (e t23 t24) * t24) + (t34 * (e t23 t34) - (e t23 t34) * t34))) - (-((t12 + t13 + t23) * ((e t12 (t23 + t24) + e (t13 + t23) t34 - e t23 t34 - e (t12 + t13) (t24 + t34) - e t12 t23)) - ((e t12 (t23 + t24) + e (t13 + t23) t34 - e t23 t34 - e (t12 + t13) (t24 + t34) - e t12 t23)) * (t12 + t13 + t23)) - ((t14 + t24) * ((e t12 (t23 + t24) + e (t14 + t24) t34 - e t24 t34 - e (t12 + t14) (t23 + t34) - e t12 t24)) - ((e t12 (t23 + t24) + e (t14 + t24) t34 - e t24 t34 - e (t12 + t14) (t23 + t34) - e t12 t24)) * (t14 + t24)) + (t14 * ((e t14 (t24 + t34) + e (t12 + t24) t23 - e t24 t23 - e (t12 + t14) (t23 + t34) - e t14 t24)) - ((e t14 (t24 + t34) + e (t12 + t24) t23 - e t24 t23 - e (t12 + t14) (t23 + t34) - e t14 t24)) * t14)) =
      -(t14 * (e t14 t12 + e t24 t14 + (-e t24 t12)) - (e t14 t12 + e t24 t14 + (-e t24 t12)) * t14) - (t14 * ((-e t14 (t12 + t13)) + e (t24 + t34) (t12 + t13) + (-e (t24 + t34) t14)) - ((-e t14 (t12 + t13)) + e (t24 + t34) (t12 + t13) + (-e (t24 + t34) t14)) * t14) + ((t14 + t24) * (e t24 t23 + e t34 t24 + (-e t34 t23)) - (e t24 t23 + e t34 t24 + (-e t34 t23)) * (t14 + t24)) - ((t14 + t24) * ((-e t34 (t13 + t23)) + e (t14 + t24) (t13 + t23) + e t34 (t14 + t24)) - ((-e t34 (t13 + t23)) + e (t14 + t24) (t13 + t23) + e t34 (t14 + t24)) * (t14 + t24)) - (t12 * (e t34 (t13 + t23)) - (e t34 (t13 + t23)) * t12) + (t23 * (e (t24 + t34) (t12 + t13)) - (e (t24 + t34) (t12 + t13)) * t23) + ((t12 + t13 + t23) * (e t23 t12) - (e t23 t12) * (t12 + t13 + t23)) + (t14 * (e t23 (t12 + t24)) - (e t23 (t12 + t24)) * t14) + (t24 * (e (t23 + t34) (t12 + t14)) - (e (t23 + t34) (t12 + t14)) * t24) + ((t23 + t24 + t34) * (e t34 t23) - (e t34 t23) * (t23 + t24 + t34)) + ((t12 + t13 + t14) * (e t34 t23) - (e t34 t23) * (t12 + t13 + t14)) - ((t13 + t14 + t23 + t24 + t34) * (e t34 (t13 + t23)) - (e t34 (t13 + t23)) * (t13 + t14 + t23 + t24 + t34)) + ((t12 + t13 + t14 + t24 + t34) * (e (t24 + t34) (t12 + t13)) - (e (t24 + t34) (t12 + t13)) * (t12 + t13 + t14 + t24 + t34)) - ((t12 + t13 + t14 + t23 + t24) * (e (t23 + t24) t12) - (e (t23 + t24) t12) * (t12 + t13 + t14 + t23 + t24)) := by
    simp only [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15]; noncomm_ring
  rw [key, H0, H1, H2, H3, C0, C1, C2, C3, C4, C5, C6, C7, C8, C9]
  noncomm_ring

/-- The alternating sum `u` of `S(A, B, C) = [B, e A B] + [C, e A C]` over the four
`(A, B, C)` of (5.24). -/
def uDefect {R : Type*} [Ring R] (e : R → R → R) (t12 t13 t14 t23 t24 t34 : R) : R :=
  ((t14 * (e t12 t14) - (e t12 t14) * t14) + (t24 * (e t12 t24) - (e t12 t24) * t24)) - ((t14 * (e (t12 + t13) t14) - (e (t12 + t13) t14) * t14) + ((t24 + t34) * (e (t12 + t13) (t24 + t34)) - (e (t12 + t13) (t24 + t34)) * (t24 + t34))) + (((t14 + t24) * (e (t13 + t23) (t14 + t24)) - (e (t13 + t23) (t14 + t24)) * (t14 + t24)) + (t34 * (e (t13 + t23) t34) - (e (t13 + t23) t34) * t34)) - ((t24 * (e t23 t24) - (e t23 t24) * t24) + (t34 * (e t23 t34) - (e t23 t34) * t34))

/-- The linearised pentagon defect (5.20) on strands `a, b, c, d`, from the five generators
`t_ab, t_ac, t_bc, t_bd, t_cd` it uses. -/
def linPentDefect {R : Type*} [Ring R] (e : R → R → R) (tab tac tbc tbd tcd : R) : R :=
  e tab (tbc + tbd) + e (tac + tbc) tcd - e tbc tcd - e (tab + tac) (tbd + tcd) - e tab tbc

/-- **(5.24) from the linearised (5.17), (5.18), (5.20).** Under the hypotheses of
`cocycle_identity`, the pentagon at the strand orders `1234`, `1243`, `1423` forces `u = 0`. -/
theorem uDefect_eq_zero {R : Type*} [Ring R] [Algebra ℚ R] (e : R → R → R) (I : Submodule ℚ R)
    {t12 t13 t14 t23 t24 t34 : R} (h : DK4 t12 t13 t14 t23 t24 t34)
    (h12 : t12 ∈ I) (h13 : t13 ∈ I) (h14 : t14 ∈ I) (h23 : t23 ∈ I) (h24 : t24 ∈ I) (h34 : t34 ∈ I)
    (hanti : ∀ a b, a ∈ I → b ∈ I → e a b + e b a = 0)
    (hhex : ∀ a b c, a ∈ I → b ∈ I → c ∈ I → DK3 a b c → e b a + e c b + e a c = 0)
    (hcomm : ∀ m a b, Commute m a → Commute m b → Commute m (e a b))
    (p1 : linPentDefect e t12 t13 t23 t24 t34 = 0) (p2 : linPentDefect e t12 t14 t24 t23 t34 = 0)
    (p3 : linPentDefect e t14 t12 t24 t34 t23 = 0) :
    uDefect e t12 t13 t14 t23 t24 t34 = 0 := by
  have q1 : (e t12 (t23 + t24) + e (t13 + t23) t34 - e t23 t34 - e (t12 + t13) (t24 + t34) - e t12 t23) = 0 := by
    rw [← p1]; simp only [linPentDefect, add_comm]
  have q2 : (e t12 (t23 + t24) + e (t14 + t24) t34 - e t24 t34 - e (t12 + t14) (t23 + t34) - e t12 t24) = 0 := by
    rw [← p2]; simp only [linPentDefect, add_comm]
  have q3 : (e t14 (t24 + t34) + e (t12 + t24) t23 - e t24 t23 - e (t12 + t14) (t23 + t34) - e t14 t24) = 0 := by
    rw [← p3]; simp only [linPentDefect, add_comm]
  unfold uDefect
  rw [cocycle_identity e I h h12 h13 h14 h23 h24 h34 hanti hhex hcomm, q1, q2, q3]
  noncomm_ring

section U4

variable {N : ℕ} {y : FreeAlgebra ℚ (Fin 2)}

/-- The linearised hexagon (5.18) of `GrtU4` at every Drinfeld–Kohno triple in `Fil N 1`. -/
theorem GrtU4.hex (hy : GrtU4 N y) (a b c : U4 N) (ha : a ∈ Fil N 1) (hb : b ∈ Fil N 1)
    (hc : c ∈ Fil N 1) (h : DK3 a b c) : eval b a y + eval c b y + eval a c y = 0 := by
  have := congrArg (liftU3 a b c h ha hb hc) hy.lin513
  simpa only [map_add, map_zero, map_eval, liftU3_t0, liftU3_t1, liftU3_t3] using this

/-- **Drinfeld (5.24) for `GrtU4`.** If `y` satisfies the linearised (5.17), (5.18), (5.20) in
`U4 N` then `u = 0` at the universal family. No Lie hypothesis on `y` is used. -/
theorem GrtU4.uDefect_eq_zero (hy : GrtU4 N y) :
    uDefect (fun a b => eval a b y) (t N 0) (t N 1) (t N 2) (t N 3) (t N 4) (t N 5) = 0 := by
  have T := t_mem_Fil_one (N := N)
  have h := dk4 N
  have hd2 : DK4 (t N 0) (t N 2) (t N 1) (t N 4) (t N 3) (t N 5) :=
    ⟨h.f12_34, h.f14_23, h.f13_24, h.n12_4, h.n14_2, h.n24_1, h.n12_3, h.n13_2, h.n23_1,
      h.n14_3, h.n13_4, by rw [add_comm]; exact h.n34_1, h.n24_3, h.n23_4,
      by rw [add_comm]; exact h.n34_2⟩
  have hd3 : DK4 (t N 2) (t N 0) (t N 1) (t N 4) (t N 5) (t N 3) :=
    ⟨h.f14_23, h.f12_34, h.f13_24, h.n14_2, h.n12_4, by rw [add_comm]; exact h.n24_1,
      h.n14_3, h.n13_4, by rw [add_comm]; exact h.n34_1, h.n12_3, h.n13_2, h.n23_1,
      by rw [add_comm]; exact h.n24_3, by rw [add_comm]; exact h.n34_2, h.n23_4⟩
  have hw (s : Fin 6 → U4 N) (hs : ∀ i, s i ∈ Fil N 1) := word_eq_zero_of_Fil_one s hs
  have p2 := congrArg (lift N ![t N 0, t N 2, t N 1, t N 4, t N 3, t N 5] (by simpa using hd2)
    (hw _ (by intro i; fin_cases i <;> simp [T]))) hy.lin515
  have p3 := congrArg (lift N ![t N 2, t N 0, t N 1, t N 4, t N 5, t N 3] (by simpa using hd3)
    (hw _ (by intro i; fin_cases i <;> simp [T]))) hy.lin515
  simp only [map_add, map_eval, lift_t, Matrix.cons_val, Fin.isValue] at p2 p3
  refine RationalAssociator.uDefect_eq_zero (fun a b => eval a b y) (Fil N 1) h (T 0) (T 1) (T 2) (T 3) (T 4) (T 5)
    hy.lin512 hy.hex (fun m a b ha hb => (commute_eval ha.symm hb.symm y).symm) ?_ ?_ ?_
  · simp only [linPentDefect]; rw [hy.lin515]; abel
  · simp only [linPentDefect]; rw [p2]; abel
  · simp only [linPentDefect]; rw [p3]; abel

end U4

section SPoly

/-- Drinfeld's `s(B, C) = [B, ψ(A, B)] + [C, ψ(A, C)]` with `A = −B − C`, as an element of
`ℚ⟨B, C⟩` (`B = ι 0`, `C = ι 1`). -/
noncomputable def sPoly (y : FreeAlgebra ℚ (Fin 2)) : FreeAlgebra ℚ (Fin 2) :=
  let B := FreeAlgebra.ι ℚ (0 : Fin 2)
  let C := FreeAlgebra.ι ℚ (1 : Fin 2)
  (B * eval (-(B + C)) B y - eval (-(B + C)) B y * B) +
    (C * eval (-(B + C)) C y - eval (-(B + C)) C y * C)

/-- `s` is `LieLike` for **every** `y`, Lie or not: at commuting `x, z` both brackets vanish,
because `ψ(−x−z, x)` lies in the commutative subalgebra generated by `x` and `z`. -/
theorem sPoly_lieLike (y : FreeAlgebra ℚ (Fin 2)) : LieLike (sPoly y) := by
  refine ⟨0, 0, fun R _ _ x z hxz => ?_⟩
  have c1 : Commute x (eval (-(x + z)) x y) :=
    (commute_eval ((Commute.refl x).add_left hxz.symm).neg_left (Commute.refl x) y).symm
  have c2 : Commute z (eval (-(x + z)) z y) :=
    (commute_eval (hxz.add_left (Commute.refl z)).neg_left (Commute.refl z) y).symm
  simp only [sPoly, map_add, map_sub, map_mul, map_neg, map_eval, eval_X, eval_Y]
  rw [c1.eq, c2.eq]
  simp

/-- `s` is symmetric for every `y`: `s(C, B) = s(B, C)`. -/
theorem sPoly_symm (y : FreeAlgebra ℚ (Fin 2)) :
    eval (FreeAlgebra.ι ℚ 1) (FreeAlgebra.ι ℚ 0) (sPoly y) = sPoly y := by
  simp only [sPoly, map_add, map_sub, map_mul, map_neg, map_eval, eval_X, eval_Y]
  rw [add_comm (FreeAlgebra.ι ℚ (1 : Fin 2)) (FreeAlgebra.ι ℚ 0)]
  abel

end SPoly

end QOU.BraidsAndKnots.RationalAssociator
