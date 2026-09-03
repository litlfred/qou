import Mathlib.Algebra.BigOperators.Intervals
import Mathlib.Tactic
import QOU.Mathlib.LagrangeCoeffSum

/-!
# QOU.Mathlib.VandermondeUpdateRatio — scaling one node of a Vandermonde pair product

`∏_{i<j}(x_i − x_j)`, with one node replaced.  Adding a box to row `a` of a partition sends the
shifted part `x_a = Q^{β_a}` to `Q·x_a` and fixes every other node, so the effect of a box on the
level-`r` principal specialisation is the effect of a single-node update on this product.

| | |
|---|---|
| `vandPairProd n x` | `∏_{i<j<n} (x_i − x_j)` |
| `inner_prod_update` | one row of the double product under `Function.update` |
| `vandPairProd_update` | `V(x[a↦y]) · ∏_{j≠a}(x_a − x_j) = ∏_{j≠a}(y − x_j) · V(x)` |
| `vandPairProd_update_div` | the same as a ratio, when the denominator is invertible |
| `sum_vandPairProd_scale` | **branching**: `∑_a V(x[a ↦ Q·x_a]) = [n]_Q · V(x)` |

**The signs cancel, and that is the only subtle point.**  For `j > a` the pair is `(a,j)` and the
factor `x_a − x_j` becomes `y − x_j`.  For `j < a` the pair is `(j,a)` and `x_j − x_a` becomes
`x_j − y` — the *opposite* orientation.  But `(x_j − y)/(x_j − x_a) = (y − x_j)/(x_a − x_j)`, so both
halves contribute the same shape and the `(−1)^a` from the lower rows cancels between the two sides.
Hence the update ratio is the **unordered** `∏_{j ≠ a}`, which is exactly the shape
`QOU.Mathlib.sum_prod_qratio` sums over.

The statement is division-free so that it holds over any commutative ring and needs no
non-vanishing hypothesis; `vandPairProd_update_div` is the field-valued corollary.

## Base ring (§7c)

Generic `[CommRing F]` (the ratio form needs `[Field F]`).  No ordering, no `ℝ`.

LaTeX label: `lem:vandermonde-update-ratio`
-/

namespace QOU.Mathlib

open Finset

variable {F : Type*} [CommRing F]

/-- `∏_{i<j<n} (x i − x j)`. -/
def vandPairProd (n : ℕ) (x : ℕ → F) : F :=
  ∏ i ∈ Finset.range n, ∏ j ∈ Finset.Ico (i + 1) n, (x i - x j)

theorem prod_erase_range_split {M : Type*} [CommMonoid M] (n a : ℕ) (ha : a < n) (g : ℕ → M) :
    ∏ j ∈ (Finset.range n).erase a, g j
      = (∏ j ∈ Finset.range a, g j) * ∏ j ∈ Finset.Ico (a + 1) n, g j := by
  have hu : (Finset.range n).erase a = Finset.range a ∪ Finset.Ico (a + 1) n := by
    ext j
    simp only [Finset.mem_erase, Finset.mem_range, Finset.mem_union, Finset.mem_Ico]
    omega
  have hd : Disjoint (Finset.range a) (Finset.Ico (a + 1) n) := by
    rw [Finset.disjoint_left]
    intro j hj hj2
    rw [Finset.mem_range] at hj
    rw [Finset.mem_Ico] at hj2
    omega
  rw [hu, Finset.prod_union hd]

/-- Row `i ≠ a` of the double product, under a single-node update.  The updated node shows up as the
single factor `x i − y` when `i < a`, and not at all when `i > a`. -/
theorem inner_prod_update (n a i : ℕ) (ha : a < n) (hia : i ≠ a) (x : ℕ → F) (y : F) :
    ∏ j ∈ Finset.Ico (i + 1) n,
        (Function.update x a y i - Function.update x a y j)
      = (if i < a then (x i - y) else 1)
        * ∏ j ∈ (Finset.Ico (i + 1) n).erase a, (x i - x j) := by
  have hui : Function.update x a y i = x i := Function.update_of_ne hia _ _
  rcases lt_or_gt_of_ne hia with hlt | hgt
  · have hmem : a ∈ Finset.Ico (i + 1) n := Finset.mem_Ico.mpr ⟨by omega, ha⟩
    rw [← Finset.mul_prod_erase _ _ hmem, if_pos hlt, hui, Function.update_self]
    congr 1
    refine Finset.prod_congr rfl fun j hj => ?_
    rw [Function.update_of_ne (Finset.ne_of_mem_erase hj)]
  · have hnm : a ∉ Finset.Ico (i + 1) n := by
      simp only [Finset.mem_Ico]; omega
    rw [Finset.erase_eq_of_notMem hnm, if_neg (by omega), one_mul]
    refine Finset.prod_congr rfl fun j hj => ?_
    rw [Finset.mem_Ico] at hj
    rw [hui, Function.update_of_ne (by omega : j ≠ a)]

/-- **Scaling one node of the Vandermonde pair product, division-free.**

`V(x[a ↦ y]) · ∏_{j ≠ a}(x_a − x_j) = ∏_{j ≠ a}(y − x_j) · V(x)`. -/
theorem vandPairProd_update (n a : ℕ) (ha : a < n) (x : ℕ → F) (y : F) :
    vandPairProd n (Function.update x a y) * ∏ j ∈ (Finset.range n).erase a, (x a - x j)
      = (∏ j ∈ (Finset.range n).erase a, (y - x j)) * vandPairProd n x := by
  classical
  have hmem : a ∈ Finset.range n := Finset.mem_range.mpr ha
  -- the sign flip on the rows above `a`
  have hneg : ∀ w : F, ∏ i ∈ Finset.range a, (x i - w)
      = (-1 : F) ^ a * ∏ i ∈ Finset.range a, (w - x i) := by
    intro w
    have hc : ((-1 : F)) ^ a = ∏ _i ∈ Finset.range a, (-1 : F) := by
      rw [Finset.prod_const, Finset.card_range]
    rw [hc, ← Finset.prod_mul_distrib]
    exact Finset.prod_congr rfl fun i _ => by ring
  -- the `if` product collapses to the rows above `a`
  have hif : ∀ w : F, ∏ i ∈ (Finset.range n).erase a, (if i < a then (x i - w) else 1)
      = (-1 : F) ^ a * ∏ i ∈ Finset.range a, (w - x i) := by
    intro w
    rw [prod_erase_range_split n a ha, ← hneg w]
    have h1 : ∏ i ∈ Finset.range a, (if i < a then (x i - w) else 1)
        = ∏ i ∈ Finset.range a, (x i - w) :=
      Finset.prod_congr rfl fun i hi => if_pos (Finset.mem_range.mp hi)
    have h2 : ∏ i ∈ Finset.Ico (a + 1) n, (if i < a then (x i - w) else 1) = 1 := by
      refine Finset.prod_eq_one fun i hi => ?_
      rw [Finset.mem_Ico] at hi
      exact if_neg (by omega)
    rw [h1, h2, mul_one]
  -- both Vandermonde products, split at row `a`
  have hsplit : ∀ y' : F, vandPairProd n (Function.update x a y')
      = (∏ j ∈ Finset.Ico (a + 1) n, (y' - x j))
        * ((-1 : F) ^ a * ∏ j ∈ Finset.range a, (y' - x j))
        * ∏ i ∈ (Finset.range n).erase a,
            ∏ j ∈ (Finset.Ico (i + 1) n).erase a, (x i - x j) := by
    intro y'
    unfold vandPairProd
    rw [← Finset.mul_prod_erase _ _ hmem]
    have hrow : ∏ j ∈ Finset.Ico (a + 1) n,
        (Function.update x a y' a - Function.update x a y' j)
        = ∏ j ∈ Finset.Ico (a + 1) n, (y' - x j) := by
      refine Finset.prod_congr rfl fun j hj => ?_
      rw [Finset.mem_Ico] at hj
      rw [Function.update_self, Function.update_of_ne (by omega : j ≠ a)]
    have hrest : ∏ i ∈ (Finset.range n).erase a,
        ∏ j ∈ Finset.Ico (i + 1) n,
          (Function.update x a y' i - Function.update x a y' j)
        = (∏ i ∈ (Finset.range n).erase a, (if i < a then (x i - y') else 1))
          * ∏ i ∈ (Finset.range n).erase a,
              ∏ j ∈ (Finset.Ico (i + 1) n).erase a, (x i - x j) := by
      rw [← Finset.prod_mul_distrib]
      refine Finset.prod_congr rfl fun i hi => ?_
      exact inner_prod_update n a i ha (Finset.ne_of_mem_erase hi) x y'
    rw [hrow, hrest, hif y']
    ring
  have hx : vandPairProd n x = vandPairProd n (Function.update x a (x a)) := by
    rw [Function.update_eq_self]
  rw [hsplit y, hx, hsplit (x a),
    prod_erase_range_split n a ha (fun j => x a - x j),
    prod_erase_range_split n a ha (fun j => y - x j)]
  ring

/-- The ratio form, over a field: `V(x[a ↦ y]) / V(x) = ∏_{j ≠ a} (y − x_j)/(x_a − x_j)`. -/
theorem vandPairProd_update_div {F : Type*} [Field F] (n a : ℕ) (ha : a < n) (x : ℕ → F) (y : F)
    (hne : ∀ j ∈ (Finset.range n).erase a, x a - x j ≠ 0) :
    vandPairProd n (Function.update x a y)
      = (∏ j ∈ (Finset.range n).erase a, (y - x j) / (x a - x j)) * vandPairProd n x := by
  have hden : (∏ j ∈ (Finset.range n).erase a, (x a - x j)) ≠ 0 :=
    Finset.prod_ne_zero_iff.mpr hne
  rw [Finset.prod_div_distrib]
  field_simp
  exact vandPairProd_update n a ha x y

/-- **A collided node kills the product.**

If the updated value equals the node just above it, the pair `(a−1, a)` contributes a zero factor.
Applied to a partition: adding a box to row `a` is illegal exactly when `μ_a = μ_{a−1}`, and then the
shifted parts satisfy `β_{a−1} = β_a + 1`, i.e. `x_{a−1} = Q·x_a`.  So the illegal rows contribute
nothing to the sum in `sum_vandPairProd_scale` and need no separate case. -/
theorem vandPairProd_update_eq_zero (n a : ℕ) (ha : a < n) (hpos : 0 < a) (x : ℕ → F) (y : F)
    (h : y = x (a - 1)) : vandPairProd n (Function.update x a y) = 0 := by
  have hne : a - 1 ≠ a := by omega
  refine Finset.prod_eq_zero (Finset.mem_range.mpr (by omega : a - 1 < n)) ?_
  refine Finset.prod_eq_zero (Finset.mem_Ico.mpr ⟨by omega, ha⟩) ?_
  rw [Function.update_of_ne hne, Function.update_self, h, sub_self]

/-! ## Branching for the Vandermonde pair product -/

/-- **Branching, unconditionally, for the Vandermonde pair product.**

`∑_{a<n} V(x[a ↦ Q·x_a]) = (1 + Q + ⋯ + Q^{n−1}) · V(x)`.

Scaling node `a` by `Q` is what adding a box to row `a` does to the shifted parts
`x_i = Q^{μ_i + r − i}`; `vandPairProd_update_div` turns each summand into the `a`-th `q`-ratio and
`QOU.Mathlib.sum_prod_qratio` sums those to `[n]_Q`.

Rows to which a box cannot be added need no separate treatment: there `Q·x_a = x_{a−1}`, so the
updated node collides with its neighbour and `V` vanishes — `vandPairProd_update_eq_zero` below.
Summing over all rows and summing over addable rows are therefore the same sum, which is what the
`r = 2` chain needed `rowLen_two_addCell_row2` for. -/
theorem sum_vandPairProd_scale {F : Type*} [Field F] (n : ℕ) (x : ℕ → F) (Q : F)
    (hinj : Set.InjOn x (Finset.range n)) (hx0 : ∀ i ∈ Finset.range n, x i ≠ 0)
    (hQ0 : Q ≠ 0) (hQ1 : Q ≠ 1) :
    ∑ a ∈ Finset.range n, vandPairProd n (Function.update x a (Q * x a))
      = (∑ k ∈ Finset.range n, Q ^ k) * vandPairProd n x := by
  have hstep : ∀ a ∈ Finset.range n,
      vandPairProd n (Function.update x a (Q * x a))
        = (∏ j ∈ (Finset.range n).erase a, (Q * x a - x j) / (x a - x j)) * vandPairProd n x := by
    intro a ha
    refine vandPairProd_update_div n a (Finset.mem_range.mp ha) x (Q * x a) ?_
    intro j hj
    refine sub_ne_zero.mpr fun h => ?_
    exact Finset.ne_of_mem_erase hj (hinj (Finset.mem_of_mem_erase hj) ha h.symm)
  rw [Finset.sum_congr rfl hstep, ← Finset.sum_mul,
    sum_prod_qratio hinj hx0 hQ0 hQ1, Finset.card_range]

end QOU.Mathlib
