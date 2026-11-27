import Mathlib.GroupTheory.Perm.Sign
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Group.Action.Defs
import Mathlib.RepresentationTheory.Basic

/-!
# Sign-isotype exclusion for a totally antisymmetric `S₃`-tensor

This file mechanizes the representation-theory half of the *statement-B*
Brunnian isotype-exclusion result
(`docs/audits/2026-08-30-statement-b-brunnian-isotype-exclusion.md`, PR #6106).

The regular representation of `S₃` decomposes into its three isotypes,
`R[S₃] = Sym ⊕ Alt ⊕ Std` (trivial ⊕ sign ⊕ standard, dimensions `1 + 1 + 2`),
carried by the group-algebra projectors

* `π_Sym = (1/6) Σ_{σ} σ`             (symmetric / trivial isotype),
* `π_Alt = (1/6) Σ_{σ} sgn(σ)·σ`      (alternating / sign isotype),
* `π_Std = 1 − π_Sym − π_Alt`         (standard, `2`-dimensional isotype).

For an element `t` that **transforms in the sign representation** — a *totally
antisymmetric tensor*, `σ • t = sgn(σ)·t` for every `σ ∈ S₃` — the physics
statement is that `t` lives entirely in the `Alt` isotype:

* `π_Sym(t) = 0`,   `π_Alt(t) = t`,   `π_Std(t) = 0`.

The crux is the scalar identity `Σ_{σ ∈ S₃} sgn(σ) = 0` (three even permutations
contribute `+1`, three odd contribute `−1`), proved here by decision procedure
(`sign_sum_eq_zero`). Given it and `sgn(σ)² = 1`, the three projector identities
follow.

Two formulations are given, both **sorry-free** and both genuinely using the
antisymmetry hypothesis (they are false without it):

1. An **unnormalized, base-ring-free** version over any additive group `M`
   carrying a `DistribMulAction (Equiv.Perm (Fin 3))` (§7c: no field, no
   characteristic assumption). The symmetric sum vanishes, the signed sum equals
   `6 • t`, and the (scaled) standard combination vanishes.
2. A **normalized** version with the genuine `(1/6)` projectors, over a
   characteristic-zero field `R` and an `R`-linear representation `ρ`. Here the
   scalar `6` must be invertible, which is exactly why `[CharZero R]` is
   required and honestly stated.

## References

- [fulton-harris1991] Representation Theory: A First Course, §2 (Frobenius
  character formula; isotype projectors of `S₃`).
- [leitner2026] `docs/audits/2026-08-30-statement-b-brunnian-isotype-exclusion.md`
-/

open scoped BigOperators

namespace QOU.StandardModel

/-- **Key scalar identity.** The signs of the six permutations of `Fin 3` sum to
zero: three even permutations contribute `+1`, three odd contribute `−1`.

This is the arithmetic crux behind the vanishing of the symmetric projection of
a totally antisymmetric tensor. -/
-- Ref: [fulton-harris1991] §2.1 (sign character of `S₃`)
theorem sign_sum_eq_zero :
    (∑ σ : Equiv.Perm (Fin 3), (Equiv.Perm.sign σ : ℤ)) = 0 := by
  decide

/-- Each permutation sign squares to `1`, since `sgn σ = ±1`. -/
-- Ref: [fulton-harris1991] §2.1
theorem sign_mul_self (σ : Equiv.Perm (Fin 3)) :
    (Equiv.Perm.sign σ : ℤ) * (Equiv.Perm.sign σ : ℤ) = 1 := by
  rcases Int.units_eq_one_or (Equiv.Perm.sign σ) with h | h <;> simp [h]

/-- The signs sum to zero after casting into any ring `R`. -/
-- Ref: [fulton-harris1991] §2.1
theorem sign_sum_cast_eq_zero (R : Type*) [Ring R] :
    (∑ σ : Equiv.Perm (Fin 3), ((Equiv.Perm.sign σ : ℤ) : R)) = 0 := by
  rw [← Int.cast_sum, sign_sum_eq_zero, Int.cast_zero]

/-- The cast sign squares to `1` in any ring `R`. -/
-- Ref: [fulton-harris1991] §2.1
theorem sign_mul_self_cast (R : Type*) [Ring R] (σ : Equiv.Perm (Fin 3)) :
    ((Equiv.Perm.sign σ : ℤ) : R) * ((Equiv.Perm.sign σ : ℤ) : R) = 1 := by
  rw [← Int.cast_mul, sign_mul_self, Int.cast_one]

/-! ## Unnormalized, base-ring-free version

Over an arbitrary additive group `M` with an `S₃`-action, using only the ambient
`ℤ`-module structure (no division). These are the `6·π_·` forms of the three
projector identities. -/

section Module

variable {M : Type*} [AddCommGroup M] [DistribMulAction (Equiv.Perm (Fin 3)) M]
variable (t : M)

/-- **Symmetric projection vanishes.** For a totally antisymmetric tensor
`σ • t = sgn(σ) • t`, the unnormalized symmetric sum `Σ_σ σ • t = 6·π_Sym(t)`
vanishes — the sign identity `Σ sgn σ = 0` kills it. -/
-- Ref: [fulton-harris1991] §2 (trivial-isotype projector)
theorem symSum_eq_zero
    (hsgn : ∀ σ : Equiv.Perm (Fin 3), σ • t = (Equiv.Perm.sign σ : ℤ) • t) :
    (∑ σ : Equiv.Perm (Fin 3), σ • t) = 0 := by
  simp_rw [hsgn]
  rw [← Finset.sum_smul, sign_sum_eq_zero, zero_smul]

/-- **Alternating projection is the identity.** For a totally antisymmetric
tensor, the unnormalized signed sum `Σ_σ sgn(σ) • (σ • t) = 6·π_Alt(t)` equals
`6 • t`, because `sgn(σ)² = 1` collapses every summand to `t`. -/
-- Ref: [fulton-harris1991] §2 (sign-isotype projector)
theorem altSum_eq_card_smul
    (hsgn : ∀ σ : Equiv.Perm (Fin 3), σ • t = (Equiv.Perm.sign σ : ℤ) • t) :
    (∑ σ : Equiv.Perm (Fin 3), (Equiv.Perm.sign σ : ℤ) • (σ • t)) = (6 : ℕ) • t := by
  have h6 : Fintype.card (Equiv.Perm (Fin 3)) = 6 := by decide
  simp_rw [hsgn, smul_smul, sign_mul_self, one_smul]
  rw [Finset.sum_const, Finset.card_univ, h6]

/-- **Standard projection vanishes.** The (scaled) standard combination
`6 • t − Σ_σ σ • t − Σ_σ sgn(σ) • (σ • t) = 6·π_Std(t)` vanishes for a totally
antisymmetric tensor: `6•t − 0 − 6•t = 0`. -/
-- Ref: [fulton-harris1991] §2 (standard-isotype projector)
theorem stdCombination_eq_zero
    (hsgn : ∀ σ : Equiv.Perm (Fin 3), σ • t = (Equiv.Perm.sign σ : ℤ) • t) :
    (6 : ℕ) • t - (∑ σ : Equiv.Perm (Fin 3), σ • t)
        - (∑ σ : Equiv.Perm (Fin 3), (Equiv.Perm.sign σ : ℤ) • (σ • t)) = 0 := by
  rw [symSum_eq_zero t hsgn, altSum_eq_card_smul t hsgn, sub_zero, sub_self]

end Module

/-! ## Normalized `(1/6)` projectors over a characteristic-zero field

The genuine group-algebra projectors, over an `R`-linear representation `ρ` of
`S₃`. The scalar `6` must be invertible, so `[CharZero R]` is required. -/

section Normalized

variable {R : Type*} [Field R] [CharZero R]
variable {V : Type*} [AddCommGroup V] [Module R V]
variable (ρ : Representation R (Equiv.Perm (Fin 3)) V) (v : V)

/-- The trivial-isotype (symmetric) projector `π_Sym = (1/6) Σ_σ σ`. -/
noncomputable def piSym : V := (6⁻¹ : R) • ∑ σ : Equiv.Perm (Fin 3), ρ σ v

/-- The sign-isotype (alternating) projector `π_Alt = (1/6) Σ_σ sgn(σ)·σ`. -/
noncomputable def piAlt : V :=
  (6⁻¹ : R) • ∑ σ : Equiv.Perm (Fin 3), ((Equiv.Perm.sign σ : ℤ) : R) • ρ σ v

/-- The standard-isotype projector `π_Std = 1 − π_Sym − π_Alt`. -/
noncomputable def piStd : V := v - piSym ρ v - piAlt ρ v

-- Ref: [fulton-harris1991] §2 (trivial-isotype projector on the sign representation)
omit [CharZero R] in
/-- **`π_Sym(t) = 0`** for a totally antisymmetric tensor `ρ σ v = sgn(σ)·v`. -/
theorem piSym_eq_zero
    (hsgn : ∀ σ : Equiv.Perm (Fin 3), ρ σ v = ((Equiv.Perm.sign σ : ℤ) : R) • v) :
    piSym ρ v = 0 := by
  unfold piSym
  simp_rw [hsgn, ← Finset.sum_smul, sign_sum_cast_eq_zero R, zero_smul, smul_zero]

/-- **`π_Alt(t) = t`** for a totally antisymmetric tensor `ρ σ v = sgn(σ)·v`. -/
-- Ref: [fulton-harris1991] §2 (sign-isotype projector on the sign representation)
theorem piAlt_eq_self
    (hsgn : ∀ σ : Equiv.Perm (Fin 3), ρ σ v = ((Equiv.Perm.sign σ : ℤ) : R) • v) :
    piAlt ρ v = v := by
  unfold piAlt
  have h6 : Fintype.card (Equiv.Perm (Fin 3)) = 6 := by decide
  simp_rw [hsgn, smul_smul, sign_mul_self_cast R, one_smul]
  rw [Finset.sum_const, Finset.card_univ, h6, ← Nat.cast_smul_eq_nsmul R, smul_smul,
    show (6⁻¹ : R) * ((6 : ℕ) : R) = 1 by norm_num, one_smul]

/-- **`π_Std(t) = 0`** for a totally antisymmetric tensor `ρ σ v = sgn(σ)·v`:
`t − 0 − t = 0`. -/
-- Ref: [fulton-harris1991] §2 (standard-isotype projector on the sign representation)
theorem piStd_eq_zero
    (hsgn : ∀ σ : Equiv.Perm (Fin 3), ρ σ v = ((Equiv.Perm.sign σ : ℤ) : R) • v) :
    piStd ρ v = 0 := by
  unfold piStd
  rw [piSym_eq_zero ρ v hsgn, piAlt_eq_self ρ v hsgn, sub_zero, sub_self]

end Normalized

end QOU.StandardModel
