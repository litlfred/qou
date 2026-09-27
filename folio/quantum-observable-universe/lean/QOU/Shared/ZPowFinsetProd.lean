import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.GroupWithZero.Units.Basic
import Mathlib.Algebra.Order.Field.Defs

/-!
# QOU.Shared.ZPowFinsetProd — a fixed base with varying **integer** exponents

Mathlib carries two neighbouring facts and not this one:

* `Finset.prod_pow_eq_pow_sum` — `∏ i ∈ s, a ^ f i = a ^ ∑ i ∈ s, f i` for `f : ι → ℕ`,
  the right shape but **natural** exponents;
* `Finset.prod_zpow` — `∏ a ∈ s, f a ^ n = (∏ a ∈ s, f a) ^ n`, a **fixed** integer
  exponent distributed over a varying base, which is the other direction.

Missing is the combination: one fixed base, exponents varying over `ℤ`. That is the shape
of a **gauge product** `∏_c z c ^ A c` for an integer exponent row `A`, and of a
**q-power product** `∏ q ^ f i` where `f` takes negative values — so it is needed wherever
an exponent lattice acts multiplicatively. `ℕ` will not do in either case, because lattice
rows and content functions both take negative values.

## This file exists because the repo had TWO copies already

Found by grep, after a third was written:

* `QOU.BraidKnot.Keystone.prod_zpow_eq_zpow_sum` — stated over a `Field R` with
  `q ≠ 0`, used by `KeystoneJucysMurphyTwist` and `HeckeSeminormalWeight`;
* a `CommGroup` copy inside `QOU.Eightfold.GaugeAnsatzNesting`, now removed in favour of
  this file.

Neither subsumes the other — `CommGroup` has total `zpow`, while a ring element needs the
`q ≠ 0` side condition — so both forms live here. The `₀` version is stated over
`GroupWithZero`, which is strictly more general than the `Field` it was written for.

**The two pre-existing consumers are deliberately NOT rewired.** Consolidating them is a
refactor of files this branch has no other business in, and the 2026-09-07 ask-first
ruling names "tidying an inconsistency" as *not* exempt. The duplication is recorded here
so the next agent finds it from either end rather than writing a fourth copy.
-/

namespace QOU.Shared

variable {ι : Type*}

/-- **A fixed base, integer exponents, summed over a `Finset`** — the `ℤ` companion of
Mathlib's `Finset.prod_pow_eq_pow_sum`, which covers only `ℕ`. -/
theorem prod_zpow_eq_zpow_sum {G : Type*} [CommGroup G] (s : Finset ι) (f : ι → ℤ) (a : G) :
    ∏ i ∈ s, a ^ f i = a ^ ∑ i ∈ s, f i :=
  Finset.cons_induction (by simp)
    (fun _ _ _ ih => by simp [Finset.prod_cons, Finset.sum_cons, zpow_add, ih]) s

/-- The same over a whole `Fintype`, the form a gauge product takes. -/
theorem prod_univ_zpow_eq_zpow_sum {G : Type*} [CommGroup G] [Fintype ι] (f : ι → ℤ)
    (a : G) : ∏ i, a ^ f i = a ^ ∑ i, f i :=
  prod_zpow_eq_zpow_sum Finset.univ f a

/-- **The `GroupWithZero` form**, for a base that is a ring element rather than a group
element: the side condition `q ≠ 0` replaces totality of `zpow`.

Generalises `QOU.BraidKnot.Keystone.prod_zpow_eq_zpow_sum`, which states this for a
`Field`. -/
theorem prod_zpow_eq_zpow_sum₀ {R : Type*} [CommGroupWithZero R] (s : Finset ι) (q : R)
    (hq : q ≠ 0) (f : ι → ℤ) : ∏ i ∈ s, q ^ f i = q ^ ∑ i ∈ s, f i :=
  Finset.cons_induction (by simp)
    (fun _ _ _ ih => by
      simp [Finset.prod_cons, Finset.sum_cons, zpow_add₀ hq, ih]) s

end QOU.Shared
