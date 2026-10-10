import QOU.Mathlib.HeckeAlgebra
import Mathlib.LinearAlgebra.Dimension.Constructions

/-!
# `QOU.BringsSurface.EulerCharacteristicSix` — the cohomological axioms force `χ = −6`

`χ(A) = −6` is used as a constant across the corpus — `MathlibExt.SubstrateRegime`
("the `A₅` geometry that fixes the genus-4 / `χ(A) = -6` obstruction"),
`AlgebraicSubstrate.collatz_obstruction_link` ("Descartes-universe-specific
(Bring's surface `Σ₄`, genus 4)"), `FluidDynamics.qou_ns_in_qou` (which carries an
`eulerChar : ℤ` field). The **derivation** of that constant existed only in prose,
in `prop:cohomological-embedding` (iv). This file is the derivation.

## The chain

`prop:cohomological-embedding` (i) says a torus knot `T_{r,s}` with `gcd(r,s) = 1`
is representable on the moduli surface `Σ_g` exactly when its Seifert rank embeds
in `H¹(Σ_g)`:

    rank H₁(Seifert(T_{r,s})) = (r−1)(s−1)/2 ≤ g

Clause (iv) supplies the two cohomological constraints — `T_{2,9}` **must** embed
and `T_{2,11}` **must not** — and asserts they pin `g` uniquely. They do:

    seifertRank 2 9  = 4  ≤ g      (so 4 ≤ g)
    seifertRank 2 11 = 5  ≰ g      (so g < 5)

giving `g = 4` (`genus_forced`), hence `χ(Σ₄) = 2 − 2·4 = −6`
(`eulerChar_forced`). Neither step is deep; the point is that the constant the
corpus quotes is now *derived from the stated axioms* rather than asserted
alongside them, so a change to either constraint moves `χ` visibly.

## The `H₃(q)` coincidence, stated as exactly that

`|χ| = 6` and `dim_R H₃(q) = 3! = 6` (`finrank_H3Carrier`). The two numbers are
equal, and `abs_eulerChar_eq_finrank_H3` records the equality — machine-checked.

What is **not** claimed is a reason. Nothing here derives the Hecke dimension
from the cohomology, or the reverse; `6 = 2·4 − 2` and `6 = 3!` arrive by
unrelated routes and are equal. Recording it as a proved numerical identity, with
the absence of a mechanism stated, is the honest form: it is a hypothesis worth
holding, not a theorem about why. If a mechanism is found, this is the statement
it has to reproduce.
-/

-- Declarations here are nested one namespace deeper than the module's
-- parent so this module and QOU.BringsSurface
-- can be imported together: both declared the same fully-qualified
-- name(s), and Lean rejects the second import with "environment already
-- contains" (bean `qou-kfcl`). Nothing imports this module, so the
-- nesting costs no consumer.
namespace QOU.BringsSurface.EulerCharacteristicSix

open QOU.Mathlib.HeckeAlgebra

/-! ## Seifert rank and embeddability -/

/-- Seifert rank of the torus knot `T_{r,s}`: `rank H₁(Seifert(T_{r,s})) = (r−1)(s−1)/2`.
Clause (i) of `prop:cohomological-embedding`. -/
def seifertRank (r s : ℕ) : ℕ := (r - 1) * (s - 1) / 2

@[simp] theorem seifertRank_two_three : seifertRank 2 3 = 1 := rfl
@[simp] theorem seifertRank_two_nine : seifertRank 2 9 = 4 := rfl
@[simp] theorem seifertRank_two_eleven : seifertRank 2 11 = 5 := rfl

/-- `T_{r,s}` embeds on `Σ_g` when its Seifert rank fits in `H¹(Σ_g)`. -/
def Embeds (r s g : ℕ) : Prop := seifertRank r s ≤ g

instance (r s g : ℕ) : Decidable (Embeds r s g) := Nat.decLe _ _

/-! ## The two cohomological constraints pin the genus -/

/-- **`g = 4` is forced.** `T_{2,9}` embedding gives `4 ≤ g`; `T_{2,11}` failing to
embed gives `g < 5`. Clause (iv) of `prop:cohomological-embedding`, as a theorem. -/
theorem genus_forced {g : ℕ} (h9 : Embeds 2 9 g) (h11 : ¬ Embeds 2 11 g) : g = 4 := by
  simp only [Embeds, seifertRank_two_nine, seifertRank_two_eleven, Nat.not_le] at h9 h11
  omega

/-- The trefoil `T_{2,3}` also embeds at the forced genus — the axioms are
consistent, not merely restrictive. -/
theorem trefoil_embeds_at_forced_genus : Embeds 2 3 4 := by decide

/-- Both constraints hold at `g = 4`, so `genus_forced`'s hypotheses are
satisfiable and the theorem is not vacuous. -/
theorem constraints_satisfiable : Embeds 2 9 4 ∧ ¬ Embeds 2 11 4 := by
  constructor
  · decide
  · decide

/-! ## …hence the Euler characteristic -/

/-- Euler characteristic of a closed orientable genus-`g` surface, `χ = 2 − 2g`. -/
def eulerChar (g : ℕ) : ℤ := 2 - 2 * (g : ℤ)

@[simp] theorem eulerChar_four : eulerChar 4 = -6 := by norm_num [eulerChar]

/-- **`χ = −6`, from the cohomological constraints alone.** This is the constant
`SubstrateRegime`, `collatz_obstruction_link` and `qou_ns_in_qou` quote. -/
theorem eulerChar_forced {g : ℕ} (h9 : Embeds 2 9 g) (h11 : ¬ Embeds 2 11 g) :
    eulerChar g = -6 := by
  rw [genus_forced h9 h11, eulerChar_four]

/-! ## `H₃(q)` is six-dimensional -/

/-- `dim_R H₃(q) = 6 = 3!`. The carrier is `R⁶`, so this is the product formula;
it is stated here because the corpus lost its copy when `QOU.Hecke.InstanceH3`
was retired (bean qou-ti7p) and nothing else records it. -/
theorem finrank_H3Carrier (R : Type*) [Field R] :
    Module.finrank R (H3Carrier R) = 6 := by
  simp [Module.finrank_prod, Module.finrank_self]

theorem finrank_H3Carrier_eq_factorial (R : Type*) [Field R] :
    Module.finrank R (H3Carrier R) = Nat.factorial 3 := by
  rw [finrank_H3Carrier]; rfl

/-! ## The two sixes agree

Proved as a numerical identity. No mechanism is claimed — see the module
docstring. -/

theorem abs_eulerChar_eq_finrank_H3 (R : Type*) [Field R] {g : ℕ}
    (h9 : Embeds 2 9 g) (h11 : ¬ Embeds 2 11 g) :
    (eulerChar g).natAbs = Module.finrank R (H3Carrier R) := by
  rw [eulerChar_forced h9 h11, finrank_H3Carrier]
  rfl

/-- The same identity with both sides shown: `|χ(Σ₄)| = 6 = 3! = dim H₃(q)`. -/
theorem abs_eulerChar_four_eq_factorial_three :
    (eulerChar 4).natAbs = Nat.factorial 3 := by
  rw [eulerChar_four]; rfl

/-- **`dim_R H₃(q) = |χ|`**, with the genus discharged rather than hypothesised.

`constraints_satisfiable` supplies both cohomological constraints at `g = 4`, so
this is `abs_eulerChar_eq_finrank_H3` with nothing left to assume: the two
quantities are equal, full stop. Still no mechanism — see the module docstring. -/
theorem finrank_H3_eq_abs_eulerChar (R : Type*) [Field R] :
    Module.finrank R (H3Carrier R) = (eulerChar 4).natAbs :=
  (abs_eulerChar_eq_finrank_H3 R constraints_satisfiable.1 constraints_satisfiable.2).symm

end QOU.BringsSurface.EulerCharacteristicSix
