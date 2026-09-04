import QOU.MathlibExt.WenzlSchurElement
import QOU.MathlibExt.MolienFakeDegreeGeneralN
import QOU.MathlibExt.NormalizedSumTelescopeBridge
import QOU.MathlibExt.ContentSumNStatistic

/-!
# QOU.MathlibExt.HconvConventionBridge — the per-λ convention bridge `hconv`

The last unproved input of the telescope closure of `normalizedSum n q = 1` (`qou-3quc`,
assembly `NormalizedSumClosure.normalizedSum_eq_one_of_convBridge`, #6011): the per-λ
**convention bridge**

  `q^{−κ_λ} / hookProd_q(λ) = schurElement(q², 0, λ) · (1 − q²)^{|λ|}`

(route verified exact `n≤5` in `computations/qbeta/fake_degree_via_telescope_probe.py`; audit
`docs/audits/2026-08-29-normalizedsum-closes-via-telescope.md`).

The proof is the sign/monomial `foldl` aggregation. Per cell,
`1 − q^{2h} = −q^{h}(q−q⁻¹)·[h]_q` (`NormalizedSumTelescopeBridge.one_sub_qsq_pow_eq`), so
`∏_x (1 − q^{2 h_x}) = (−1)^{|λ|} q^{Σh} (q−q⁻¹)^{|λ|} hookProd_q(λ)`. With
`schurElement(q²,0,λ) = q^{2n(λ)} · ∏_x (1 − q^{2 h_x})⁻¹`, `(1 − q²) = −q(q−q⁻¹)`, and the
**n-statistic identity** `κ_λ = Σ_x h_x − |λ| − 2 n(λ)`
(`ContentSumNStatistic.contentSum_eq_hookSum_sub`), the sign and `(q−q⁻¹)` powers cancel and the
exponent collapses to `−κ_λ`.

Base field `ℝ` (schurElement is archimedean); regime `1 < q` (the substrate regime).
-/

namespace QOU.MathlibExt.HconvConventionBridge

open Finset
open QOU.MathlibExt.QPartitionCombinatorics
open QOU.MathlibExt.MolienFakeDegreeGeneralN

/-- `((List.range n).map f).prod = ∏ i ∈ range n, f i`. -/
theorem map_range_prod {M : Type*} [CommMonoid M] (n : ℕ) (f : ℕ → M) :
    ((List.range n).map f).prod = ∏ i ∈ Finset.range n, f i := by
  induction n with
  | zero => simp
  | succ m ih =>
    rw [List.range_succ, List.map_append, List.prod_append, ih, Finset.prod_range_succ]
    simp

/-- **`hookProd` as a double `Finset.prod`.** The nested `foldl` of `qBracket`-of-hook is the
row×column cell product. -/
theorem hookProd_eq_prod (q : ℝ) (l : List ℕ) :
    hookProd q l = ∏ i ∈ Finset.range l.length,
      ∏ j ∈ Finset.range ((l[i]?).getD 0), qBracket q (Partition.hookLength l i j) := by
  rw [hookProd, QOU.BraidKnot.IdentityI.foldl_mul_range]
  refine Finset.prod_congr rfl (fun i _ => ?_)
  rw [QOU.BraidKnot.IdentityI.foldl_mul_range]

/-- **The Macdonald denominator product factorises.** `∏_x (1 − q^{2 h_x})` over the cells of `λ`
equals `(−1)^{|λ|} · q^{Σh} · (q−q⁻¹)^{|λ|} · hookProd_q(λ)`, cell by cell via the per-cell brick
`one_sub_qsq_pow_eq`. -/
theorem denomProd_factor (q : ℝ) (l : List ℕ) (hq : 1 < q) :
    (∏ i ∈ Finset.range l.length, ∏ j ∈ Finset.range ((l[i]?).getD 0),
        (1 - (q ^ 2) ^ (Partition.hookLength l i j)))
      = (-1 : ℝ) ^ l.sum
        * q ^ (∑ i ∈ Finset.range l.length, ∑ j ∈ Finset.range ((l[i]?).getD 0),
            Partition.hookLength l i j)
        * (q - q⁻¹) ^ l.sum
        * hookProd q l := by
  have hq0 : q ≠ 0 := ne_of_gt (lt_trans one_pos hq)
  have hden : q - q⁻¹ ≠ 0 :=
    sub_ne_zero.mpr (ne_of_gt (lt_trans (inv_lt_one_of_one_lt₀ hq) hq))
  have hsumN : (∑ i ∈ Finset.range l.length, ((l[i]?).getD 0)) = l.sum := by
    rw [← QOU.HookSumComplete.sum_range_getD]
    exact Finset.sum_congr rfl (fun i _ => by rw [List.getD_eq_getElem?_getD])
  -- per-cell factorisation
  have cell : ∀ i j, (1 - (q ^ 2) ^ (Partition.hookLength l i j))
      = (-1 : ℝ) * q ^ (Partition.hookLength l i j) * (q - q⁻¹)
          * qBracket q (Partition.hookLength l i j) := by
    intro i j
    rw [← pow_mul, QOU.MathlibExt.NormalizedSumTelescopeBridge.one_sub_qsq_pow_eq q hq0 hden]; ring
  -- inner row: aggregate the four factors over a row's cells
  have row : ∀ i, (∏ j ∈ Finset.range ((l[i]?).getD 0), (1 - (q ^ 2) ^ (Partition.hookLength l i j)))
      = (-1 : ℝ) ^ ((l[i]?).getD 0)
        * q ^ (∑ j ∈ Finset.range ((l[i]?).getD 0), Partition.hookLength l i j)
        * (q - q⁻¹) ^ ((l[i]?).getD 0)
        * (∏ j ∈ Finset.range ((l[i]?).getD 0), qBracket q (Partition.hookLength l i j)) := by
    intro i
    rw [Finset.prod_congr rfl (fun j _ => cell i j)]
    rw [Finset.prod_mul_distrib, Finset.prod_mul_distrib, Finset.prod_mul_distrib,
        Finset.prod_const, Finset.prod_const, Finset.card_range, Finset.prod_pow_eq_pow_sum]
  rw [Finset.prod_congr rfl (fun i _ => row i)]
  rw [Finset.prod_mul_distrib, Finset.prod_mul_distrib, Finset.prod_mul_distrib,
      Finset.prod_pow_eq_pow_sum, Finset.prod_pow_eq_pow_sum, Finset.prod_pow_eq_pow_sum,
      ← hookProd_eq_prod, hsumN]

/-- **`schurElement` at `X = 0` as `q^{2n(λ)}` over the Macdonald denominator product.**
`schurElement(q²,0,λ) = (q²)^{n(λ)} · (∏_x (1 − q^{2 h_x}))⁻¹` (the `1 − X·Q^c` numerators are `1`). -/
theorem schurElement_zero_eq (q : ℝ) (l : List ℕ) :
    WenzlSchurElement.schurElement (q ^ 2) 0 l
      = (q ^ 2) ^ (nLambda l)
        * (∏ i ∈ Finset.range l.length, ∏ j ∈ Finset.range ((l[i]?).getD 0),
            (1 - (q ^ 2) ^ (Partition.hookLength l i j)))⁻¹ := by
  rw [WenzlSchurElement.schurElement_eq_prod, map_range_prod]
  congr 1
  rw [← Finset.prod_inv_distrib]
  refine Finset.prod_congr rfl (fun i _ => ?_)
  rw [WenzlSchurElement.rowFactor, map_range_prod, ← Finset.prod_inv_distrib]
  refine Finset.prod_congr rfl (fun j _ => ?_)
  rw [WenzlSchurElement.cellFactor]
  simp [zero_mul, sub_zero, one_div]

/-- **The per-λ convention bridge `hconv`.** `q^{−κ_λ}/hookProd_q(λ) = schurElement(q²,0,λ)·(1−q²)^{|λ|}`,
for a weakly-decreasing partition `λ` in the substrate regime `1 < q`. This is the last unproved input
of the telescope closure `NormalizedSumClosure.normalizedSum_eq_one_of_convBridge`. -/
theorem hconv (q : ℝ) (l : List ℕ) (hl : l.Sorted (· ≥ ·)) (hq : 1 < q) :
    q ^ (-(contentSum l)) / hookProd q l
      = WenzlSchurElement.schurElement (q ^ 2) 0 l * (1 - q ^ 2) ^ l.sum := by
  have hq0 : q ≠ 0 := ne_of_gt (lt_trans one_pos hq)
  have hden : q - q⁻¹ ≠ 0 :=
    sub_ne_zero.mpr (ne_of_gt (lt_trans (inv_lt_one_of_one_lt₀ hq) hq))
  have hqsq : (1 - q ^ 2) = -q * (q - q⁻¹) := by field_simp; ring
  -- getElem/getD bridge for the hook double sum
  have hSb : (∑ i ∈ Finset.range l.length, ∑ j ∈ Finset.range ((l[i]?).getD 0),
        Partition.hookLength l i j)
      = (∑ i ∈ Finset.range l.length, ∑ j ∈ Finset.range (l.getD i 0),
        Partition.hookLength l i j) :=
    Finset.sum_congr rfl (fun i _ => by rw [List.getD_eq_getElem?_getD])
  -- exponent identity, as a power of q: q^{-κ}·q^{Σh} = (q²)^{n(λ)}·q^{|λ|}
  have hqpow : q ^ (-(contentSum l))
        * q ^ (∑ i ∈ Finset.range l.length, ∑ j ∈ Finset.range ((l[i]?).getD 0),
            Partition.hookLength l i j)
      = (q ^ 2) ^ (nLambda l) * q ^ l.sum := by
    rw [← zpow_natCast q (∑ i ∈ Finset.range l.length, ∑ j ∈ Finset.range ((l[i]?).getD 0),
          Partition.hookLength l i j), ← zpow_add₀ hq0, ← pow_mul,
        ← zpow_natCast q (2 * nLambda l), ← zpow_natCast q l.sum, ← zpow_add₀ hq0]
    congr 1
    have hns := ContentSumNStatistic.contentSum_eq_hookSum_sub l hl
    rw [hSb]
    push_cast [hns]
    ring
  -- the inverse-free scalar identity
  have hcross : q ^ (-(contentSum l))
        * ((-1 : ℝ) ^ l.sum
            * q ^ (∑ i ∈ Finset.range l.length, ∑ j ∈ Finset.range ((l[i]?).getD 0),
                Partition.hookLength l i j)
            * (q - q⁻¹) ^ l.sum)
      = (q ^ 2) ^ (nLambda l) * (1 - q ^ 2) ^ l.sum := by
    rw [hqsq, mul_pow, neg_pow]
    linear_combination ((-1 : ℝ) ^ l.sum * (q - q⁻¹) ^ l.sum) * hqpow
  -- nonzero of the scalar factor
  have hAne : ((-1 : ℝ) ^ l.sum
      * q ^ (∑ i ∈ Finset.range l.length, ∑ j ∈ Finset.range ((l[i]?).getD 0),
          Partition.hookLength l i j)
      * (q - q⁻¹) ^ l.sum) ≠ 0 :=
    mul_ne_zero (mul_ne_zero (pow_ne_zero _ (by norm_num)) (pow_ne_zero _ hq0)) (pow_ne_zero _ hden)
  -- assemble
  rw [schurElement_zero_eq, denomProd_factor q l hq, div_eq_mul_inv, mul_inv]
  rw [eq_div_of_mul_eq hAne hcross]
  ring

end QOU.MathlibExt.HconvConventionBridge
