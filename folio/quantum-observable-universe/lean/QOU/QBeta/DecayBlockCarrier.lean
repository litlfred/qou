/-
# The convention-D decay carrier is a SINGLE block

Formalises the exact identities measured in
`computations/qbeta/qbeta_d_frame_two_block_forced_weights_probe.py`
(bean `qou-cds1`).

## What is defined here, and what is taken as data

The H₃(q) normal-form basis is `[γ, σ₀, σ₁, L₊, L₋, e⁻]` with word lengths
`(0,1,1,2,2,3)`. Two of the three irreducible characters are *defined* here by
their defining evaluations on that basis (`T_w ↦ q^len w` for the trivial block,
`T_w ↦ (-q⁻¹)^len w` for the sign block). The **regular** character's values on
the basis are taken as DATA — they come from the trace of left multiplication in
the corpus's own `qbeta_net_trace_invariance_probe`, and reproducing that
computation in Lean would mean formalising the H₃ multiplication table, which is
not what these results turn on. `χ^(2,1)` is then the standard complement
`(reg − χ^(3) − χ^(1³))/2`, which is forced by `reg = Σ_λ dim_λ χ^λ` with
dimensions `(1,2,1)`.

So the theorems below are exactly: *given those regular-character values, these
identities hold*. That is the honest scope; the provenance of the values is the
probe, cited above.

## The decay element

`Δ_S` is the N=0 nucleon Hecke NF difference. Its trace signature is affine in
the Markov parameter, `tr_M(Δ_S)(z) = h²/2 − h·z`, which pins its NF support to
`{γ, σ₀, σ₁}` with `c_γ = h²/2` and `c_{σ₀} + c_{σ₁} = −h`. How that `−h` splits
is NOT determined — so it is carried as a free parameter `a`, and every theorem
below is stated `∀ a`, which is the formal content of "the block characters do
not depend on the split".

## The result

`χ^(2,1)(Δ_S) = 0` **exactly, at every z**. The 2-dimensional block never
carries the decay. Since convention D also annihilates the 3-row block
(`y_(1³)(z_D) = 0`), the decay under D is carried by a single 1-dimensional
block — the two-row cap takes the carrier from 2 blocks to 1, not from 3 to 2.

Base ring: generic `[Field R]` per AGENTS.md §7c. Nothing here is archimedean —
no ordering, no `Real.sqrt`, no substrate pin.

-- Ref: [leitner2026] bean `qou-cds1`; probe
--      computations/qbeta/qbeta_d_frame_two_block_forced_weights_probe.py
-- Ref: [wenzl1988] Wenzl, "Hecke algebras of type A_n and subfactors",
--      Invent. Math. 92 (1988) 349-383.
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace QOU.QBeta.DecayBlockCarrier

-- `CharZero` because `chi21` and `deltaS` both divide by 2; in
-- characteristic 2 that is division by zero and the statements are false.
variable {R : Type*} [Field R] [CharZero R]

/-- `h = q − q⁻¹`, the Hecke parameter. -/
def hq (q : R) : R := q - q⁻¹

/-- Word lengths of the H₃ normal-form basis `[γ, σ₀, σ₁, L₊, L₋, e⁻]`. -/
def nfLen : Fin 6 → ℕ := ![0, 1, 1, 2, 2, 3]

/-- `χ^(3)`, the trivial block: `T_w ↦ q^len w`, extended linearly. -/
def chi3 (q : R) (v : Fin 6 → R) : R := ∑ i, v i * q ^ (nfLen i)

/-- `χ^(1³)`, the sign block: `T_w ↦ (−q⁻¹)^len w`, extended linearly. -/
def chi111 (q : R) (v : Fin 6 → R) : R := ∑ i, v i * (-q⁻¹) ^ (nfLen i)

/-- Regular-character values on the NF basis. DATA, from the trace of left
multiplication (see the module docstring). -/
def regVal (q : R) : Fin 6 → R :=
  ![6, 3 * (q ^ 2 - 1) / q, 3 * (q ^ 2 - 1) / q,
    (q ^ 2 - 1) ^ 2 / q ^ 2, (q ^ 2 - 1) ^ 2 / q ^ 2,
    (q ^ 2 - 1) * (q ^ 2 - q + 1) * (q ^ 2 + q + 1) / q ^ 3]

/-- The regular character, extended linearly from `regVal`. -/
def regChar (q : R) (v : Fin 6 → R) : R := ∑ i, v i * regVal q i

/-- `χ^(2,1)` as the complement forced by `reg = χ^(3) + 2·χ^(2,1) + χ^(1³)`. -/
def chi21 (q : R) (v : Fin 6 → R) : R :=
  (regChar q v - chi3 q v - chi111 q v) / 2

/-- The decay element `Δ_S`, with the `σ₀`/`σ₁` split left free as `a`. -/
def deltaS (q a : R) : Fin 6 → R :=
  ![hq q ^ 2 / 2, a, -(hq q) - a, 0, 0, 0]

section Decay
variable {q a : R} (hq0 : q ≠ 0)

include hq0

/-- **The trivial block sees `h²/2 − h·q`, independent of the split `a`.** -/
theorem chi3_deltaS : chi3 q (deltaS q a) = hq q ^ 2 / 2 - hq q * q := by
  simp [chi3, deltaS, nfLen, Fin.sum_univ_six, hq]
  field_simp
  ring

/-- **The sign block sees `h²/2 + h·q⁻¹`, independent of the split `a`.** -/
theorem chi111_deltaS : chi111 q (deltaS q a) = hq q ^ 2 / 2 + hq q * q⁻¹ := by
  simp [chi111, deltaS, nfLen, Fin.sum_univ_six, hq]
  field_simp
  ring

/-- **The two 1-dimensional blocks see exactly opposite values.**
`χ^(3)(Δ_S) + χ^(1³)(Δ_S) = 0`, because `h·(q − q⁻¹) = h²`. -/
theorem chi3_add_chi111_deltaS :
    chi3 q (deltaS q a) + chi111 q (deltaS q a) = 0 := by
  rw [chi3_deltaS hq0, chi111_deltaS hq0]
  simp [hq]
  field_simp
  ring

/-- **`Δ_S` is traceless in the regular representation.**
`reg(Δ_S) = 6·(h²/2) + 3h·a + 3h·(−h−a) = 3h² − 3h² = 0`. -/
theorem regChar_deltaS : regChar q (deltaS q a) = 0 := by
  simp [regChar, deltaS, regVal, Fin.sum_univ_six, hq]
  field_simp
  ring

/-- **THE RESULT: the 2-dimensional block does not carry the decay element.**
`χ^(2,1)(Δ_S) = 0`, exactly, for every `q ≠ 0` and every split `a`. It follows
from the two preceding facts alone — the regular trace vanishes and the two
1-dimensional characters cancel — so it holds independently of the Markov
parameter `z`. -/
theorem chi21_deltaS : chi21 q (deltaS q a) = 0 := by
  unfold chi21
  rw [regChar_deltaS hq0]
  have h : chi3 q (deltaS q a) + chi111 q (deltaS q a) = 0 :=
    chi3_add_chi111_deltaS hq0
  rw [show (0 : R) - chi3 q (deltaS q a) - chi111 q (deltaS q a)
        = -(chi3 q (deltaS q a) + chi111 q (deltaS q a)) by ring, h]
  simp

end Decay

/-! ### The convention-D weights, and the single-block consequence -/

/-- The convention-D Markov parameter `z_D = q³/(q²+1)`. -/
def zD (q : R) : R := q ^ 3 / (q ^ 2 + 1)

/-- The `(1³)` Ocneanu weight as a function of `q` and the Markov parameter. -/
def y111 (q z : R) : R :=
  q ^ 2 * (z - q) * ((q ^ 2 + 1) * z - q ^ 3) /
    ((q ^ 2 + 1) * (q ^ 2 - q + 1) * (q ^ 2 + q + 1))

/-- The `(3)` Ocneanu weight. -/
def y3 (q z : R) : R :=
  (q * z + 1) * (q ^ 3 * z + q * z + 1) /
    ((q ^ 2 + 1) * (q ^ 2 - q + 1) * (q ^ 2 + q + 1))

/-- The `(2,1)` Ocneanu weight. -/
def y21 (q z : R) : R :=
  q * (q - z) * (q * z + 1) / ((q ^ 2 - q + 1) * (q ^ 2 + q + 1))

section Weights
variable {q : R} (hq2 : q ^ 2 + 1 ≠ 0)

include hq2

omit [CharZero R] in
/-- **The two-row cap: the 3-row block is annihilated at `z_D`.** -/
theorem y111_zD : y111 q (zD q) = 0 := by
  unfold y111 zD
  field_simp
  ring

/-- **`y_(3)` at `z_D` is `(q⁴+1)/(q²+1)²`.** -/
theorem y3_zD (h1 : q ^ 2 - q + 1 ≠ 0) (h2 : q ^ 2 + q + 1 ≠ 0) :
    y3 q (zD q) = (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2 := by
  -- Stated multiplicatively first: with no denominator on the right,
  -- `field_simp` clears everything and `ring` closes it. Going straight for the
  -- quotient leaves `(1+q^2+q^4)⁻¹` stranded inside a sum, where `ring` cannot
  -- reach it even with the non-vanishing hypothesis in scope.
  -- `div_eq_div_iff` rather than `field_simp` on the quotient directly: the
  -- latter normalises to `N * (1+q^2+q^4)⁻¹ = ...` and strands the inverse
  -- inside a sum, where `ring` cannot reach it even with non-vanishing in scope.
  have hD : (q ^ 2 + 1) * (q ^ 2 - q + 1) * (q ^ 2 + q + 1) ≠ 0 :=
    mul_ne_zero (mul_ne_zero hq2 h1) h2
  unfold y3 zD
  rw [div_eq_div_iff hD (pow_ne_zero 2 hq2)]
  field_simp
  ring

/-- **`y_(2,1)` at `z_D` is `q²/(q²+1)²`.** -/
theorem y21_zD (h1 : q ^ 2 - q + 1 ≠ 0) (h2 : q ^ 2 + q + 1 ≠ 0) :
    y21 q (zD q) = q ^ 2 / (q ^ 2 + 1) ^ 2 := by
  -- `div_eq_div_iff` rather than `field_simp` on the quotient directly: the
  -- latter normalises to `N * (1+q^2+q^4)⁻¹ = ...` and strands the inverse
  -- inside a sum, where `ring` cannot reach it even with non-vanishing in scope.
  -- y_(2,1)'s denominator carries no (q^2+1) factor, unlike y_(3)'s.
  have hD : (q ^ 2 - q + 1) * (q ^ 2 + q + 1) ≠ 0 := mul_ne_zero h1 h2
  unfold y21 zD
  rw [div_eq_div_iff hD (pow_ne_zero 2 hq2)]
  field_simp
  ring

/-- **Normalisation `Σ_λ dim_λ y_λ = 1` at `z_D`**, with dimensions `(1,2,1)`
and the 3-row weight already zero. -/
theorem norm_zD (h1 : q ^ 2 - q + 1 ≠ 0) (h2 : q ^ 2 + q + 1 ≠ 0) :
    y3 q (zD q) + 2 * y21 q (zD q) + y111 q (zD q) = 1 := by
  rw [y3_zD hq2 h1 h2, y21_zD hq2 h1 h2, y111_zD hq2]
  field_simp
  ring

end Weights

/-- **(CAPSTONE) Under convention D the decay element is carried by a SINGLE
one-dimensional block.**

Combining the two halves: `χ^(2,1)(Δ_S) = 0` kills the 2-dimensional block for
*every* Markov parameter, and `y_(1³)(z_D) = 0` kills the 3-row block at `z_D`.
What remains is one term. The trace of the decay element at `z_D` is therefore
`y_(3)(z_D) · χ^(3)(Δ_S)` — one weight, one character.

The consequence recorded in `qou-cds1`: block re-weighting cannot source the
convention-D correction, because after the cap there is only one weight left and
it is fixed by the trace axioms. An anchor can rescale it and nothing more. -/
theorem decay_carried_by_single_block
    {q a : R} (hq0 : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    y3 q (zD q) * chi3 q (deltaS q a)
      + 2 * (y21 q (zD q) * chi21 q (deltaS q a))
      + y111 q (zD q) * chi111 q (deltaS q a)
    = y3 q (zD q) * chi3 q (deltaS q a) := by
  rw [chi21_deltaS hq0, y111_zD hq2]
  ring

end QOU.QBeta.DecayBlockCarrier
