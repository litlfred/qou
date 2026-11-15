import QOU.SchurWeyl.MolienSymmetrisingTrace
import QOU.BraidKnot.HookSumClosedForm
import QOU.MathlibExt.QIntegerCanonical

/-!
# QOU.SchurWeyl.MolienBalancedForm — `M_μ(q²) = q^{−κ(μ)} / ∏_x [h(x)]_q`

`MolienSymmetrisingTrace` defines the Molien weight in the geometric variable `Q = q²`,

```
M_μ(Q) = Q^{n(μ)} · ∏_{x ∈ μ} (1 − Q) / (1 − Q^{h(x)}),
```

and proves it is the weight of the symmetrising trace.  This file proves the **balanced form**
quoted in that module's docstring:

```
M_μ(q²) = q^{−κ(μ)} / ∏_{x ∈ μ} [h(x)]_q,      [h]_q = (q^h − q^{−h}) / (q − q^{−1}),
```

with `κ(μ) = Σ_x c(x)` the content sum.

## Proof

* **One cell.** `(1 − q²)/(1 − q^{2h}) = q^{1−h} / [h]_q` (`molien_cell`).  When `q^{2h} = 1`
  both sides are `0` in Lean's division convention, so no genericity on the hooks is needed.
* **Exponents.** Multiplying out gives `q^{2 n(μ) + |μ| − Σ_x h(x)}`.  The hook-sum identity
  `Σ_x h(x) = Σ_x j + Σ_x i + |μ|` (`BraidKnot.HookSum.sum_hookZ_eq`, with `n(μ) = Σ_x i` and
  `κ(μ) = Σ_x j − Σ_x i`) makes the exponent `−κ(μ)` (`sum_hook_eq`).

## Base ring (§7c)

Generic `[Field F]`; the only hypotheses are `q ≠ 0` and `q² ≠ 1` (so that `[h]_q` is defined by
the usual quotient).  Nothing archimedean.

LaTeX label: `thm:molien-balanced-form`
-/

namespace QOU.SchurWeyl

open YoungDiagram Finset QOU.QBeta.WenzlWeight QOU.QInteger

variable {F : Type*} [Field F]

/-- The **content sum** `κ(μ) = Σ_{x ∈ μ} c(x)`. -/
def molienContentSum (μ : YoungDiagram) : ℤ := ∑ x ∈ μ.cells, content x

/-- The natural-number hook of a cell agrees with the integer hook `hookZ`. -/
theorem hook_cast_eq_hookZ (μ : YoungDiagram) {x : ℕ × ℕ} (hx : x ∈ μ.cells) :
    (hook μ x : ℤ) = QOU.BraidKnot.PieceA.hookZ μ x := by
  have h1 : x.2 < μ.rowLen x.1 := (μ.mem_iff_lt_rowLen).mp hx
  have h2 : x.1 < μ.colLen x.2 := (μ.mem_iff_lt_colLen).mp hx
  simp only [hook, QOU.BraidKnot.PieceA.hookZ, QOU.BraidKnot.PieceA.armZ, QOU.BraidKnot.PieceA.legZ]
  omega

/-- **Hook sum in terms of `n(μ)` and `κ(μ)`**: `Σ_x h(x) = κ(μ) + 2 n(μ) + |μ|`. -/
theorem sum_hook_eq (μ : YoungDiagram) :
    ((∑ x ∈ μ.cells, hook μ x : ℕ) : ℤ)
      = molienContentSum μ + 2 * (nPart μ : ℤ) + (μ.cells.card : ℤ) := by
  rw [Nat.cast_sum, Finset.sum_congr rfl fun x hx => hook_cast_eq_hookZ μ hx,
    QOU.BraidKnot.HookSum.sum_hookZ_eq, molienContentSum, nPart]
  simp only [content, Finset.sum_sub_distrib, Nat.cast_sum]
  ring

/-- A product of integer powers of `q ≠ 0` is the power of the sum. -/
theorem prod_zpow_eq_zpow_sum' {α : Type*} (q : F) (hq : q ≠ 0) (s : Finset α) (f : α → ℤ) :
    ∏ x ∈ s, q ^ f x = q ^ (∑ x ∈ s, f x) := by
  induction s using Finset.cons_induction with
  | empty => simp
  | cons a s ha ih => rw [Finset.prod_cons, Finset.sum_cons, ih, zpow_add₀ hq]

/-- **One cell**: `(1 − q²)/(1 − q^{2h}) = q^{1−h} / [h]_q`. -/
theorem molien_cell (q : F) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (h : ℕ) :
    (1 - q ^ 2) / (1 - (q ^ 2) ^ h) = q ^ (1 - (h : ℤ)) / qIntBal q h := by
  have hd : q - q⁻¹ ≠ 0 := by
    intro h0
    apply hq2
    have : q * (q - q⁻¹) = 0 := by rw [h0, mul_zero]
    rw [mul_sub, mul_inv_cancel₀ hq, sub_eq_zero] at this
    rw [sq]; exact this
  have hz : q ^ (1 - (h : ℤ)) = q / q ^ h := by
    rw [zpow_sub₀ hq, zpow_one, zpow_natCast]
  rw [hz, qIntBal_def]
  have hqh : q ^ h ≠ 0 := pow_ne_zero _ hq
  by_cases h0 : (q ^ 2) ^ h = 1
  · have hnum : q ^ h - q⁻¹ ^ h = 0 := by
      rw [inv_pow, sub_eq_zero]
      rw [← pow_mul, mul_comm, pow_mul, sq] at h0
      exact (eq_inv_of_mul_eq_one_left h0)
    rw [h0, sub_self, div_zero, hnum, zero_div, div_zero]
  · rw [← pow_mul, mul_comm, pow_mul, inv_pow]
    rw [← pow_mul, mul_comm, pow_mul] at h0
    have hA : (q ^ h) ^ 2 - 1 ≠ 0 := sub_ne_zero.mpr h0
    have h1 : 1 - (q ^ h) ^ 2 ≠ 0 := sub_ne_zero.mpr (Ne.symm h0)
    have hQ : q ^ 2 - 1 ≠ 0 := sub_ne_zero.mpr hq2
    have ea : q ^ h - (q ^ h)⁻¹ = ((q ^ h) ^ 2 - 1) / q ^ h := by
      field_simp
    have eq' : q - q⁻¹ = (q ^ 2 - 1) / q := by
      field_simp
    rw [ea, eq']
    field_simp
    ring

/-- **The balanced form of the Molien weight**:
`M_μ(q²) = q^{−κ(μ)} / ∏_{x ∈ μ} [h(x)]_q`. -/
theorem molienWeight_eq_balanced (q : F) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (μ : YoungDiagram) :
    molienWeight (q ^ 2) μ = q ^ (-molienContentSum μ) / ∏ x ∈ μ.cells, qIntBal q (hook μ x) := by
  unfold molienWeight
  rw [Finset.prod_congr rfl fun x _ => molien_cell q hq hq2 (hook μ x), Finset.prod_div_distrib,
    ← mul_div_assoc]
  congr 1
  rw [prod_zpow_eq_zpow_sum' q hq, ← pow_mul, ← zpow_natCast, ← zpow_add₀ hq]
  congr 1
  have hs := sum_hook_eq μ
  push_cast at hs ⊢
  rw [Finset.sum_sub_distrib, Finset.sum_const, nsmul_eq_mul, mul_one]
  linarith

end QOU.SchurWeyl
