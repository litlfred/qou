import Mathlib.GroupTheory.Perm.Sign
import Mathlib.GroupTheory.Abelianization.Defs
import Mathlib.Data.ZMod.Basic
import Mathlib.Data.Complex.Basic
import Mathlib.Tactic

/-!
# `thm:pontryagin-dual-coxeter-character` — Pontryagin self-duality on $S_n^{\mathrm{ab}}$

For every `n ≥ 2`:
1. The sign homomorphism `Equiv.Perm.sign : Equiv.Perm (Fin n) →* ℤˣ` vanishes on every
   commutator and therefore factors through the abelianisation
   `Abelianization (Equiv.Perm (Fin n))` via
   `abelianizedSignHom n : Abelianization (Equiv.Perm (Fin n)) →* ℤˣ`,
   which is surjective (witnessed by `Equiv.swap 0 1`).
2. `ℤˣ` (multiplicative `{±1}`) and `Multiplicative (ZMod 2)` are canonically isomorphic via
   `zmodTwoMulEquivIntUnits : Multiplicative (ZMod 2) ≃* ℤˣ` (`0 ↦ 1`, `1 ↦ -1`).
3. The Pontryagin character group `(ZMod 2 →+ ZMod 2)` (and multiplicatively
   `(Multiplicative (ZMod 2) →* ℤˣ)`, embedding injectively into `ℂˣ` via `{±1} ⊂ ℂˣ`) is
   canonically isomorphic to `ZMod 2` / `ℤˣ` via evaluation at the generator `1 : ZMod 2`,
   identifying the unique non-trivial character with the sign character and matching the
   `ℤ/2` parity of any involutive bar-automorphism `bar ∘ bar = id` (`barEven` = `+1`,
   `barOdd` = `-1`).

Refs:
- [pontryagin1934] Pontryagin, "The theory of topological commutative groups"
- [hewitt-ross1979] Hewitt–Ross, "Abstract Harmonic Analysis" Vol. I
- [leitner2026] braids-and-knots/pontryagin-dual-coxeter-character.md
-/

namespace QOU.BraidsAndKnots

/-- The non-trivial additive character of `ZMod 2`: `0 ↦ 0`, `1 ↦ 1`. -/
def zmodTwoSignChar : ZMod 2 →+ ZMod 2 := AddMonoidHom.id _

/-- Evaluation at `1 : ZMod 2` gives a canonical additive-group isomorphism
    `(ZMod 2 →+ ZMod 2) ≃+ ZMod 2` (Pontryagin self-duality of `ℤ/2`). -/
def zmodTwoPontryaginDualEquiv : (ZMod 2 →+ ZMod 2) ≃+ ZMod 2 where
  toFun φ := φ 1
  invFun a := a • AddMonoidHom.id (ZMod 2)
  left_inv φ := by
    ext x
    fin_cases x
    · simp
    · change (φ 1) • (1 : ZMod 2) = φ 1
      generalize φ 1 = y
      fin_cases y <;> decide
  right_inv a := by
    change (a • AddMonoidHom.id (ZMod 2)) 1 = a
    fin_cases a <;> decide
  map_add' _ _ := rfl

/-- Every additive homomorphism `ZMod 2 →+ ZMod 2` is determined by its value at `1`. -/
theorem zmodTwo_pontryagin_self_dual_via_value_at_one
    (φ : ZMod 2 →+ ZMod 2) (ψ : ZMod 2 →+ ZMod 2) :
    φ 1 = ψ 1 → φ = ψ :=
  fun h => zmodTwoPontryaginDualEquiv.injective h

/-- Canonical multiplicative isomorphism `Multiplicative (ZMod 2) ≃* ℤˣ` (`0 ↦ 1`, `1 ↦ -1`). -/
def zmodTwoMulEquivIntUnits : Multiplicative (ZMod 2) ≃* ℤˣ where
  toFun x := if Multiplicative.toAdd x = 0 then 1 else -1
  invFun u := Multiplicative.ofAdd (if u = 1 then 0 else 1)
  left_inv := by decide
  right_inv u := by
    rcases Int.units_eq_one_or u with rfl | rfl <;> decide
  map_mul' := by decide

/-- Canonical multiplicative embedding `ℤˣ →* ℂˣ` realizing `{±1} ⊂ ℂˣ`. -/
noncomputable def intUnitsToComplexUnits : ℤˣ →* ℂˣ :=
  Units.map (Int.castRingHom ℂ).toMonoidHom

/-- `intUnitsToComplexUnits` is injective (`1 ↦ 1`, `-1 ↦ -1` in `ℂˣ`). -/
theorem intUnitsToComplexUnits_injective :
    Function.Injective intUnitsToComplexUnits := by
  intro u v huv
  rcases Int.units_eq_one_or u with rfl | rfl <;>
    rcases Int.units_eq_one_or v with rfl | rfl
  · rfl
  · exfalso
    have hval : ((intUnitsToComplexUnits 1 : ℂˣ) : ℂ) = ((intUnitsToComplexUnits (-1) : ℂˣ) : ℂ) :=
      congrArg Units.val huv
    norm_num [intUnitsToComplexUnits] at hval
  · exfalso
    have hval : ((intUnitsToComplexUnits (-1) : ℂˣ) : ℂ) = ((intUnitsToComplexUnits 1 : ℂˣ) : ℂ) :=
      congrArg Units.val huv
    norm_num [intUnitsToComplexUnits] at hval
  · rfl

/-- Multiplicative Pontryagin self-duality `(Multiplicative (ZMod 2) →* ℤˣ) ≃* ℤˣ` via
    evaluation at the generator `Multiplicative.ofAdd 1`, mapping `1 : ℤˣ` to the trivial
    character and `-1 : ℤˣ` to `zmodTwoMulEquivIntUnits`. -/
def zmodTwoMulCharEquiv : (Multiplicative (ZMod 2) →* ℤˣ) ≃* ℤˣ where
  toFun χ := χ (Multiplicative.ofAdd (1 : ZMod 2))
  invFun u :=
    { toFun := fun x => if Multiplicative.toAdd x = 0 then 1 else u
      map_one' := rfl
      map_mul' := by
        rcases Int.units_eq_one_or u with rfl | rfl <;> decide }
  left_inv χ := by
    apply MonoidHom.ext
    intro x
    dsimp
    have ha : Multiplicative.toAdd x = 0 ∨ Multiplicative.toAdd x = 1 := by
      generalize Multiplicative.toAdd x = a
      fin_cases a <;> simp
    rcases ha with h0 | h1
    · rw [if_pos h0]
      have hx1 : x = 1 := Multiplicative.toAdd.injective h0
      rw [hx1, χ.map_one]
    · rw [if_neg (by rw [h1]; decide)]
      have hx : x = Multiplicative.ofAdd 1 := Multiplicative.toAdd.injective h1
      rw [hx]
  right_inv _ := rfl
  map_mul' _ _ := rfl

/-- Under `zmodTwoMulCharEquiv`, `-1 : ℤˣ` corresponds to the canonical isomorphism
    `zmodTwoMulEquivIntUnits` (the unique non-trivial character). -/
theorem zmodTwoMulCharEquiv_symm_neg_one :
    zmodTwoMulCharEquiv.symm (-1 : ℤˣ) = zmodTwoMulEquivIntUnits.toMonoidHom := by
  ext x
  revert x
  decide

/-- Universal descent of `Equiv.Perm.sign` to the abelianisation `S_n^{\mathrm{ab}}`
    (`Abelianization (Equiv.Perm (Fin n)) →* ℤˣ`). -/
def abelianizedSignHom (n : ℕ) : Abelianization (Equiv.Perm (Fin n)) →* ℤˣ :=
  Abelianization.lift Equiv.Perm.sign

@[simp]
theorem abelianizedSignHom_of (n : ℕ) (σ : Equiv.Perm (Fin n)) :
    abelianizedSignHom n (Abelianization.of σ) = Equiv.Perm.sign σ :=
  Abelianization.lift_apply_of Equiv.Perm.sign σ

/-- The two-cycle `swap 0 1 ∈ Equiv.Perm (Fin n)` exists for `n ≥ 2` and has sign `-1`. -/
theorem signHom_surjective_witness (n : ℕ) (hn : 2 ≤ n) :
    Equiv.Perm.sign (Equiv.swap (⟨0, by omega⟩ : Fin n) ⟨1, by omega⟩) = -1 := by
  exact Equiv.Perm.sign_swap (by
    intro h
    have : (0 : ℕ) = 1 := congrArg Fin.val h
    simp at this)

/-- For every `n ≥ 2`, `abelianizedSignHom n : S_n^{\mathrm{ab}} →* ℤˣ` is surjective. -/
theorem abelianizedSignHom_surjective (n : ℕ) (hn : 2 ≤ n) :
    Function.Surjective (abelianizedSignHom n) := by
  intro u
  rcases Int.units_eq_one_or u with rfl | rfl
  · exact ⟨1, map_one _⟩
  · refine ⟨Abelianization.of (Equiv.swap (⟨0, by omega⟩ : Fin n) ⟨1, by omega⟩), ?_⟩
    rw [abelianizedSignHom_of]
    exact signHom_surjective_witness n hn

/-- Complex-valued Pontryagin character `S_n^{\mathrm{ab}} →* ℂˣ` induced by `Equiv.Perm.sign`,
    whose image is `{+1, -1} ⊂ ℂˣ` for every `n ≥ 2`. -/
noncomputable def abelianizedComplexSignChar (n : ℕ) :
    Abelianization (Equiv.Perm (Fin n)) →* ℂˣ :=
  intUnitsToComplexUnits.comp (abelianizedSignHom n)

theorem abelianizedComplexSignChar_swap_eq_neg_one (n : ℕ) (hn : 2 ≤ n) :
    ((abelianizedComplexSignChar n
      (Abelianization.of (Equiv.swap (⟨0, by omega⟩ : Fin n) ⟨1, by omega⟩)) : ℂˣ) : ℂ) = -1 := by
  simp [abelianizedComplexSignChar, intUnitsToComplexUnits, signHom_surjective_witness n hn]

/-- Any ring involution `bar : R →+* R` (`bar (bar x) = x`) decomposes `2 * x = (x + bar x) + (x - bar x)`
    into `+1` (`zmodTwoMulEquivIntUnits (ofAdd 0)`) and `-1` (`zmodTwoMulEquivIntUnits (ofAdd 1)`)
    eigencomponents under the same `ℤˣ ≃* Multiplicative (ZMod 2)` grading. -/
theorem bar_involution_zmodTwo_grading {R : Type*} [CommRing R]
    (bar : R →+* R) (hinv : ∀ x : R, bar (bar x) = x) (x : R) :
    bar (x + bar x) = ((zmodTwoMulEquivIntUnits (Multiplicative.ofAdd 0) : ℤˣ) : ℤ) • (x + bar x) ∧
    bar (x - bar x) = ((zmodTwoMulEquivIntUnits (Multiplicative.ofAdd 1) : ℤˣ) : ℤ) • (x - bar x) := by
  have h0 : ((zmodTwoMulEquivIntUnits (Multiplicative.ofAdd 0) : ℤˣ) : ℤ) = 1 := by decide
  have h1 : ((zmodTwoMulEquivIntUnits (Multiplicative.ofAdd 1) : ℤˣ) : ℤ) = -1 := by decide
  rw [h0, h1, one_zsmul, neg_one_zsmul]
  refine ⟨?_, ?_⟩
  · rw [map_add, hinv x, add_comm]
  · rw [map_sub, hinv x]; ring

/-- Combined structural theorem for `thm:pontryagin-dual-coxeter-character`. -/
theorem pontryagin_dual_coxeter_character_structural (n : ℕ) (hn : 2 ≤ n) :
    (∀ (φ ψ : ZMod 2 →+ ZMod 2), φ 1 = ψ 1 → φ = ψ) ∧
    Function.Surjective (abelianizedSignHom n) ∧
    Function.Injective intUnitsToComplexUnits ∧
    Equiv.Perm.sign (Equiv.swap (⟨0, by omega⟩ : Fin n) ⟨1, by omega⟩) = -1 :=
  ⟨zmodTwo_pontryagin_self_dual_via_value_at_one,
   abelianizedSignHom_surjective n hn,
   intUnitsToComplexUnits_injective,
   signHom_surjective_witness n hn⟩

class PontryaginDualCoxeterCharacter where
  holds : ∀ (n : ℕ) (hn : 2 ≤ n),
    (∀ (φ ψ : ZMod 2 →+ ZMod 2), φ 1 = ψ 1 → φ = ψ) ∧
    Function.Surjective (abelianizedSignHom n) ∧
    Function.Injective intUnitsToComplexUnits ∧
    Equiv.Perm.sign (Equiv.swap (⟨0, by omega⟩ : Fin n) ⟨1, by omega⟩) = -1

instance : PontryaginDualCoxeterCharacter where
  holds := pontryagin_dual_coxeter_character_structural

end QOU.BraidsAndKnots
