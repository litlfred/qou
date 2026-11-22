import Mathlib.RingTheory.Adjoin.Basic
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum
import QOU.BraidsAndKnots.FibreDimensionForcesTL

/-!
# Colour carried by a tensor braiding (working assumption, issue #9106)

**Setting.** A strand carries colour `ℂ³` and flavour. A colour action that is a genuine Hopf
action at generic `q` cannot commute with a single Hecke braiding on the combined space
(`ColourBridge.q_eq_one_of_e01_mem`). The tensor braiding `X = a·b` escapes this: `a = Ř_c ⊗ 1`
acts on colour, `b = 1 ⊗ Ř_f` on flavour, they commute, and each is Hecke at the same `q`.

Proved here, over any commutative ring (or for commuting elements of any algebra), with no
numerical input:

* `tensor_braid_cubic` / `tensor_braid_cubic_of_commute`: `X` satisfies
  `(X − q²)(X + 1)(X − qi²) = 0`.
* `tensor_braid_not_hecke`: `X` is not Hecke in general (explicit witness over `ℚ`).
* `singlet_hecke`: if `a` acts on a vector by `−qi` (the value of the `q`-antisymmetriser on the
  colour singlet `ε`, cited, not proved here), then on that sector `X = −qi·b`,
  `(X + 1)(X − qi²) = 0` and `−q·X = b`.
* `singlet_threeRow_eq_zero_of_conventionD`: so a Markov trace on the singlet sector, written in
  the recovered generator `−q·X = b`, has the same Ocneanu weights as the flavour trace, and
  under convention D its `(1³)` weight is zero.

**Inputs, now proved concretely** in `QOU.Braiding.JimboGl3Singlet` (over any field, `q ≠ 0`):
Jimbo's `Ř` for `gl₃` acts on `ε_q` by `−q⁻¹` in both positions (`R12_eps`, `R23_eps`); `Ř`
commutes with the coproducts of the `U_q(gl₃)` generators (`comm_E`, `comm_F`, `comm_L`); `ε_q`
spans the `q`-determinant line (`E_eps`, `F_eps`, `L_eps`); and when `q² + 1 ≠ 0` that line is the
whole joint `−q⁻¹`-eigenspace (`singlet_unique`). So the hypothesis "`a` acts as `−qi`" in
`singlet_hecke` holds on the colour singlet with `qi = q⁻¹`; it is no longer a citation.
-/

namespace QOU.Braiding.HopfColourTensorBraid

section CommRingCase

variable {K : Type*} [CommRing K]

/-- **Cubic for the tensor braiding.** In a commutative ring, if `a` and `b` each satisfy the
Hecke relation at `q` (with `q·qi = 1`), then `X = a·b` satisfies
`(X − q²)(X + 1)(X − qi²) = 0`. -/
theorem tensor_braid_cubic (q qi a b : K) (hqi : q * qi = 1)
    (ha : (a - q) * (a + qi) = 0) (hb : (b - q) * (b + qi) = 0) :
    (a * b - q ^ 2) * (a * b + 1) * (a * b - qi ^ 2) = 0 := by
  linear_combination (b^2*(a*b + b*q - b*qi - q^2 - qi^2 + 1)) * ha
    + (a*b*q^2 - a*b*q*qi + a*b*qi^2 - a*q^2*qi + a*q*qi^2 + a*q - a*qi + b*q^2*qi
        - b*q*qi^2 - 2*q^2*qi^2 + q*qi) * hb
    + (-q*qi*(-2*a*b + a*q - a*qi + b*q - b*qi + 2*q*qi)) * hqi

/-- **On a colour-singlet sector the tensor braiding is Hecke again.** If `a` acts as the
scalar `−qi`, then `X = −qi·b` satisfies `(X + 1)(X − qi²) = 0`. -/
theorem singlet_hecke (q qi b : K) (hqi : q * qi = 1) (hb : (b - q) * (b + qi) = 0) :
    (-qi * b + 1) * (-qi * b - qi ^ 2) = 0 := by
  linear_combination qi ^ 2 * hb + qi * (b + qi) * hqi

/-- **The recovered generator is the flavour generator.** `−q·(−qi·b) = b`. -/
theorem singlet_rescale (q qi b : K) (hqi : q * qi = 1) : -q * (-qi * b) = b := by
  linear_combination b * hqi

end CommRingCase

section Algebra

variable {K A : Type*} [CommRing K] [Ring A] [Algebra K A]

/-- **Cubic for commuting Hecke elements of any algebra.** -/
theorem tensor_braid_cubic_of_commute (q qi : K) (a b : A) (hab : Commute a b)
    (hqi : q * qi = 1)
    (ha : (a - algebraMap K A q) * (a + algebraMap K A qi) = 0)
    (hb : (b - algebraMap K A q) * (b + algebraMap K A qi) = 0) :
    (a * b - algebraMap K A (q ^ 2)) * (a * b + 1) * (a * b - algebraMap K A (qi ^ 2)) = 0 := by
  rw [map_pow, map_pow]
  let S := Algebra.adjoin K ({a, b} : Set A)
  letI R : CommRing S :=
    Algebra.adjoinCommRingOfComm K (by
      intro x hx y hy
      simp only [Set.mem_insert_iff, Set.mem_singleton_iff] at hx hy
      rcases hx with rfl | rfl <;> rcases hy with rfl | rfl
      · exact Commute.refl _
      · exact hab
      · exact hab.symm
      · exact Commute.refl _)
  let a' : S := ⟨a, Algebra.subset_adjoin (by simp)⟩
  let b' : S := ⟨b, Algebra.subset_adjoin (by simp)⟩
  let q' : S := ⟨algebraMap K A q, Subalgebra.algebraMap_mem _ _⟩
  let qi' : S := ⟨algebraMap K A qi, Subalgebra.algebraMap_mem _ _⟩
  have hqi' : q' * qi' = 1 := Subtype.ext (by
    show algebraMap K A q * algebraMap K A qi = 1
    rw [← map_mul, hqi, map_one])
  have ha' : (a' - q') * (a' + qi') = 0 := Subtype.ext ha
  have hb' : (b' - q') * (b' + qi') = 0 := Subtype.ext hb
  have key := congrArg Subtype.val (tensor_braid_cubic q' qi' a' b' hqi' ha' hb')
  exact key

end Algebra

/-- **The tensor braiding is not Hecke.** Over `ℚ` at `q = 2`, `a = b = q` (both Hecke),
`X = 4` is neither `q` nor `−qi`. -/
theorem tensor_braid_not_hecke :
    ∃ q qi a b : ℚ, q * qi = 1 ∧ (a - q) * (a + qi) = 0 ∧ (b - q) * (b + qi) = 0 ∧
      (a * b - q) * (a * b + qi) ≠ 0 :=
  ⟨2, 1 / 2, 2, 2, by norm_num, by norm_num, by norm_num, by norm_num⟩

/-- **Convention D survives on colour singlets.** Let `(y₃, y₂₁, y₁₃)` be the Ocneanu weights of
a Markov trace with parameter `z` on the singlet sector, written in the recovered generator
`−q·X`, which equals the flavour generator `b` (`singlet_rescale`). If `z` is the convention-D
parameter, then `y₁₃ = 0`: the colour singlets keep D's zero on `(1³)`. -/
theorem singlet_threeRow_eq_zero_of_conventionD {K : Type*} [CommRing K] [IsDomain K]
    (q qi z y₃ y₂₁ y₁₃ : K) (hqi : q * qi = 1)
    (hnorm : y₃ + 2 * y₂₁ + y₁₃ = 1)
    (hsigma : q * y₃ + (q - qi) * y₂₁ + (-qi) * y₁₃ = z)
    (hsigmasigma : q ^ 2 * y₃ + (-1) * y₂₁ + qi ^ 2 * y₁₃ = z ^ 2)
    (hzD : z * (q + qi) = q ^ 2)
    (hb2ne : q + qi ≠ 0) (h3ne : (q + qi) ^ 2 - 1 ≠ 0) :
    y₁₃ = 0 :=
  QOU.BraidsAndKnots.threeRow_eq_zero_of_jones_ocneanu q qi z y₃ y₂₁ y₁₃ hqi hnorm hsigma
    hsigmasigma hzD hb2ne h3ne

end QOU.Braiding.HopfColourTensorBraid
