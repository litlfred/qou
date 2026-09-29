import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.BigOperators.Group.Finset.Powerset
import Mathlib.Data.Finset.Powerset
import Mathlib.Data.Fintype.Card
import Mathlib.Tactic

/-!
# The hook column of the Magnus tr-decay is the elementary-symmetric tower (qou-o6ov)

**Context (numerically established, not formalizable here).** For the atom braid word `ρ`, the
hook Hecke characters obey, exact to 139 digits (A=2,3;
`computations/deltalambda/magnus_hook_exterior_power_probe.py`):
```
tr_{(k,1ⁿ⁻ᵏ)}(ρ) = q^{L(1−j)} · e_j( eigenvalues of ρ in the reduced-Burau rep (n−1,1) ),
                   j = n − k,
```
i.e. the hooks are the (q-)exterior powers `Λʲ(V)` of the reduced Burau rep `V`, and the whole
hook column is the tower of **elementary symmetric functions** `e_j` of the Burau spectrum
(`e_j = [tʲ] det(1 + t·ρ^V)`, the characteristic / Alexander polynomial). The seminormal
Hecke construction, the specific word `ρ`, and the `q`-twist are outside Mathlib, so what is
formalized here is the **algebraic core that packages all orders `j` at once**: the
elementary-symmetric generating function. It is general over any `CommRing`.

`prod_one_add_mul_eq_sum_powerset` is the all-orders identity
`∏ᵢ (1 + t·μᵢ) = Σ_{S} t^{|S|} ∏_{i∈S} μᵢ`; `prod_one_add_mul_eq_sum_esymm` regrades it by
degree into `Σ_j tʲ · e_j(μ)` with `e_j` the `j`-th elementary symmetric sum — the generating
function whose `j`-th coefficient is (up to the numerically-verified twist) the hook-`j`
character.
-/

namespace QOU.MassTheory

open Finset BigOperators

variable {ι : Type*} [Fintype ι] [DecidableEq ι] {R : Type*} [CommRing R]

/-- **All-orders generating function (subset form).** `∏ᵢ (1 + t·μᵢ) = Σ_S t^{|S|} ∏_{i∈S} μᵢ`,
the sum over all subsets `S`. This packages every exterior-power degree `j = |S|` into one
identity: the coefficient of `t^j` is the `j`-th elementary symmetric sum of `μ`, which the
probe identifies (up to the `q`-twist) with the hook-`(n−j,1ʲ)` character of the reduced
Burau. General `CommRing`. -/
theorem prod_one_add_mul_eq_sum_powerset (t : R) (μ : ι → R) :
    ∏ i, (1 + t * μ i) = ∑ S ∈ (univ : Finset ι).powerset, t ^ S.card * ∏ i ∈ S, μ i := by
  have hcomm : ∀ i, (1 : R) + t * μ i = t * μ i + 1 := fun i => add_comm _ _
  simp_rw [hcomm]
  rw [Finset.prod_add]
  refine Finset.sum_congr rfl ?_
  intro S _
  rw [Finset.prod_const_one, mul_one, Finset.prod_mul_distrib, Finset.prod_const]

/-- The `j`-th elementary symmetric sum of `μ`: `e_j = Σ_{|S|=j} ∏_{i∈S} μᵢ`. -/
noncomputable def esymm (j : ℕ) (μ : ι → R) : R :=
  ∑ S ∈ (univ : Finset ι).powersetCard j, ∏ i ∈ S, μ i

/-- **All-orders generating function (degree-graded form).**
`∏ᵢ (1 + t·μᵢ) = Σ_{j=0}^{|ι|} tʲ · e_j(μ)`. The right side is the elementary-symmetric tower;
its `j`-th term is the reduced-Burau `Λʲ` trace, i.e. (up to the numerically-verified `q`-twist)
the hook-`(n−j,1ʲ)` character of the Magnus decay. General `CommRing`. -/
theorem prod_one_add_mul_eq_sum_esymm (t : R) (μ : ι → R) :
    ∏ i, (1 + t * μ i) = ∑ j ∈ range (Fintype.card ι + 1), t ^ j * esymm j μ := by
  -- regroup the powerset sum by card `j = |S|` (`Finset.sum_powerset`; `card_univ`
  -- turns `univ.card` into `Fintype.card ι` to match the range bound)
  rw [prod_one_add_mul_eq_sum_powerset t μ,
      Finset.sum_powerset (univ : Finset ι) (fun S => t ^ S.card * ∏ i ∈ S, μ i),
      Finset.card_univ]
  refine Finset.sum_congr rfl ?_
  intro j _
  rw [esymm, Finset.mul_sum]
  refine Finset.sum_congr rfl ?_
  intro S hS
  rw [(Finset.mem_powersetCard.mp hS).2]

end QOU.MassTheory
