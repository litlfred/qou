import Mathlib.Tactic

/-!
# QOU.Common.FormalResidue — residue of an exact form, library version

Library home for the formal-residue calculus first proved inline in the
content-block sibling `brings-surface/sw-classical-jet-exactness.lean`
(`prop:sw-classical-jet-exactness`). A local Laurent expansion is modelled by
its coefficient function `f : ℤ → R`; the residue is the coefficient of
`t⁻¹`; the termwise derivative shifts every exponent down by one. The
load-bearing invariant is `fresidue_fderiv`: **the residue of an exact form
vanishes** — `d(anything)` has no residue, anywhere, ever.

Beyond the block-level statement, this module adds the library API:

* linearity of `fderiv` and `fresidue` (`fderiv_add`, `fresidue_add`, …);
* vanishing residues for all positive-order jets (`fresidue_jet_succ`);
* the **converse** over a characteristic-zero field
  (`exists_antideriv_iff_fresidue_eq_zero`): a formal Laurent expansion has a
  termwise antiderivative *iff* its residue vanishes — the residue is the
  complete obstruction to exactness in the formal model.

The core stays over a generic `CommRing R` (§7c wall-safe); the converse
needs division by exponents, hence `Field K` + `CharZero K` — an algebraic
hypothesis, not an archimedean one.
-/

namespace QOU.FormalResidue

section CommRing

variable {R : Type*} [CommRing R]

/-- Formal residue of a local Laurent expansion, presented as its coefficient
function `f : ℤ → R`: the coefficient of `t⁻¹`. -/
def fresidue (f : ℤ → R) : R := f (-1)

/-- Termwise derivative of a formal Laurent expansion:
`(Σ c_e tᵉ)' = Σ (e+1)·c_{e+1} tᵉ`. -/
def fderiv (f : ℤ → R) : ℤ → R := fun e => (e + 1) • f (e + 1)

@[simp] theorem fresidue_zero : fresidue (0 : ℤ → R) = 0 := rfl

theorem fresidue_add (f g : ℤ → R) :
    fresidue (f + g) = fresidue f + fresidue g := rfl

theorem fresidue_smul (r : R) (f : ℤ → R) :
    fresidue (r • f) = r * fresidue f := rfl

theorem fderiv_add (f g : ℤ → R) : fderiv (f + g) = fderiv f + fderiv g := by
  funext e
  simp [fderiv, smul_add]

theorem fderiv_smul (r : R) (f : ℤ → R) : fderiv (r • f) = r • fderiv f := by
  funext e
  simp [fderiv]
  ring

/-- **The residue of an exact form vanishes**: the `t⁻¹` coefficient of a
termwise derivative is `((−1)+1)·f(0) = 0`. -/
@[simp] theorem fresidue_fderiv (f : ℤ → R) : fresidue (fderiv f) = 0 := by
  show ((-1 : ℤ) + 1) • f (-1 + 1) = 0
  norm_num

/-- The `n`-th classical jet of a local expansion: `n`-fold termwise
derivative (the coefficient-level face of `X^{(n)} = dⁿX/dzⁿ` on the curve). -/
def jet (X : ℤ → R) : ℕ → ℤ → R
  | 0 => X
  | n + 1 => fderiv (jet X n)

@[simp] theorem jet_zero (X : ℤ → R) : jet X 0 = X := rfl

theorem jet_succ (X : ℤ → R) (n : ℕ) : jet X (n + 1) = fderiv (jet X n) := rfl

/-- Every positive-order classical jet is exact, so its residue vanishes at
every point. -/
@[simp] theorem fresidue_jet_succ (X : ℤ → R) (n : ℕ) :
    fresidue (jet X (n + 1)) = 0 :=
  fresidue_fderiv _

end CommRing

section CharZeroField

variable {K : Type*} [Field K] [CharZero K]

/-- Candidate termwise antiderivative: `(t⁻¹ ↦ dropped, tᵉ⁻¹ ↦ tᵉ/e)`.
Only its values at `e ≠ 0` matter; the value at `0` is a free integration
constant, set to `0`. -/
noncomputable def antideriv (f : ℤ → K) : ℤ → K :=
  fun e => if e = 0 then 0 else (e : K)⁻¹ * f (e - 1)

/-- **The residue is the complete obstruction to exactness** (char-0 field):
a formal Laurent expansion is a termwise derivative iff its residue
vanishes. Forward direction is `fresidue_fderiv`; the converse divides each
coefficient by its shifted exponent, which is where `CharZero` enters. -/
theorem exists_antideriv_iff_fresidue_eq_zero (f : ℤ → K) :
    (∃ g : ℤ → K, fderiv g = f) ↔ fresidue f = 0 := by
  constructor
  · rintro ⟨g, rfl⟩
    exact fresidue_fderiv g
  · intro hres
    refine ⟨antideriv f, funext fun e => ?_⟩
    by_cases he : e = -1
    · subst he
      have h0 : f (-1) = 0 := hres
      show ((-1 : ℤ) + 1) • antideriv f (-1 + 1) = f (-1)
      rw [h0]
      norm_num
    · have he1 : e + 1 ≠ 0 := fun h => he (by omega)
      have hK : ((e + 1 : ℤ) : K) ≠ 0 := Int.cast_ne_zero.mpr he1
      show ((e + 1 : ℤ)) • antideriv f (e + 1) = f e
      rw [zsmul_eq_mul, antideriv, if_neg he1, add_sub_cancel_right,
        mul_inv_cancel_left₀ hK]

end CharZeroField

end QOU.FormalResidue
