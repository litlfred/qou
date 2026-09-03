import QOU.BraidKnot.HeckeJucysMurphyAdjacentNormalForm

/-!
# The ADDITIVE Jucys–Murphy elements, and where Prop 3.24 actually breaks

Every route tried on the multiplicative elements `jmRaw` failed (five refuted leads, bean
`qou-u9o1`).  Reading the classical source explained why: **`jmRaw` is not the Jucys–Murphy
element.**

Mathas (*Iwahori–Hecke Algebras and Schur Algebras of the Symmetric Group*, Prop. 3.24) defines
them **additively** — a sum of transpositions, `L₁ = 0`, with recursion
`L_k = q⁻¹(T_{k−1} + T_{k−1} L_{k−1} T_{k−1})`.  Note the extra `+ T_{k−1}`, absent from
`jmRaw (k+1) = σ_k · jmRaw k · σ_k`.

This file builds the additive family in **this corpus's** Hecke convention
(`σ² = (q − q⁻¹)σ + 1`) rather than transcribing formulas across conventions — Mathas works with
`T² = (q−1)T + q`, so his coefficients are not ours.

## What the recursion gives (proved)

Writing `A_{k+1} := σ_k A_k σ_k + d·σ_k` for a **free scalar** `d` and `h := q − q⁻¹`:

* `addJM_sigma_left`  : `σ_k A_{k+1} = h·A_{k+1} + A_k σ_k + d`
* `addJM_sigma_right` : `A_{k+1} σ_k = h·A_{k+1} + σ_k A_k + d`
* **`addJM_sigma_comm_add`** : `σ_k` commutes with `A_k + A_{k+1}` — **for every `d`**.

The two exchange relations differ only by swapping `A_k σ_k` and `σ_k A_k`, which is exactly why
those terms cancel in the **sum**.  This is Mathas 3.24(iii)'s sum half, and it comes out cleaner
here than the multiplicative analogue did: no constraint on `d` at all.

## Where 3.24 breaks — the product half does NOT follow from the recursion

Mathas 3.24(iii) also asserts `T_i` commutes with the **product** `L_i L_{i+1}`, and derives
commutativity (iv) from it.  From the recursion alone one gets only

* `addJM_sigma_prod_swap` : `σ_k (A_k A_{k+1}) = (A_{k+1} A_k) σ_k`

— **with the operands swapped on the right**, which is genuine commutation *only if* `A_k` and
`A_{k+1}` already commute.  So (iii)'s product half and (iv) are entangled, and the recursion does
not separate them.

This is the same obstruction found on the multiplicative side (`sigma_mul_jm_prod`), and it is now
located precisely: **it survives the change of convention.**  Mathas's "follows easily using the
relations" must use the explicit sum-of-transpositions expansion, not just the recursion — which
this file does not have, because an abstract presentation has no transposition elements.

## Honest scope

Nothing here proves commutativity, and `JucysMurphySpectrum` is untouched.  What is established is
that the additive convention **does** improve the sum half (unconditionally, for free `d`) and
**does not** rescue the product half — so the next attempt needs the transposition expansion, not
another convention change.

Refs:
- [macdonald1995] Symmetric Functions and Hall Polynomials, I.1.
- [wenzl1988] Hecke algebra representations.
-/

namespace QOU.BraidKnot.Hecke

variable {R : Type*} [Field R] {A : Type*} [Ring A] [Algebra R A] {q : R}

/-- **Additive Jucys–Murphy family**, by Mathas's recursion in this corpus's convention:
`A₀ = 0`, `A_{k+1} = σ_k A_k σ_k + d·σ_k`.

The scalar `d` is left **free**: every result below holds for all `d`, which is stronger than
fixing Mathas's `q⁻¹` and makes clear that the sum-commutation owes nothing to the normalisation. -/
def addJM (H : HeckeGenerators R A q) (d : R) : ℕ → A
  | 0 => 0
  | (k + 1) => H.σ k * addJM H d k * H.σ k + d • H.σ k

@[simp] theorem addJM_zero (H : HeckeGenerators R A q) (d : R) : addJM H d 0 = 0 := rfl

theorem addJM_succ (H : HeckeGenerators R A q) (d : R) (k : ℕ) :
    addJM H d (k + 1) = H.σ k * addJM H d k * H.σ k + d • H.σ k := rfl

/-- The Hecke relation in scalar-action form. -/
theorem hecke_smul (H : HeckeGenerators R A q) (i : ℕ) :
    H.σ i * H.σ i = (q - q⁻¹) • H.σ i + 1 := by
  rw [H.hecke i, Algebra.smul_def]

/-- **Exchange relation, left**: `σ_k A_{k+1} = h·A_{k+1} + A_k σ_k + d`. -/
theorem addJM_sigma_left (H : HeckeGenerators R A q) (d : R) (k : ℕ) :
    H.σ k * addJM H d (k + 1)
      = (q - q⁻¹) • addJM H d (k + 1) + addJM H d k * H.σ k + d • (1 : A) := by
  rw [addJM_succ]
  calc H.σ k * (H.σ k * addJM H d k * H.σ k + d • H.σ k)
      = (H.σ k * H.σ k) * addJM H d k * H.σ k + d • (H.σ k * H.σ k) := by
        rw [mul_add, mul_smul_comm]; noncomm_ring
    _ = ((q - q⁻¹) • H.σ k + 1) * addJM H d k * H.σ k
          + d • ((q - q⁻¹) • H.σ k + 1) := by rw [hecke_smul]
    _ = _ := by
        simp only [add_mul, one_mul, smul_add, smul_smul, smul_mul_assoc]
        rw [mul_comm d (q - q⁻¹)]
        abel

/-- **Exchange relation, right**: `A_{k+1} σ_k = h·A_{k+1} + σ_k A_k + d`. -/
theorem addJM_sigma_right (H : HeckeGenerators R A q) (d : R) (k : ℕ) :
    addJM H d (k + 1) * H.σ k
      = (q - q⁻¹) • addJM H d (k + 1) + H.σ k * addJM H d k + d • (1 : A) := by
  rw [addJM_succ]
  calc (H.σ k * addJM H d k * H.σ k + d • H.σ k) * H.σ k
      = H.σ k * addJM H d k * (H.σ k * H.σ k) + d • (H.σ k * H.σ k) := by
        rw [add_mul, smul_mul_assoc]; noncomm_ring
    _ = H.σ k * addJM H d k * ((q - q⁻¹) • H.σ k + 1)
          + d • ((q - q⁻¹) • H.σ k + 1) := by rw [hecke_smul]
    _ = _ := by
        simp only [mul_add, mul_one, smul_add, smul_smul, mul_smul_comm]
        rw [mul_comm d (q - q⁻¹)]
        abel

/-- **`σ_k` commutes with `A_k + A_{k+1}`, for every `d`.**

The two exchange relations differ only in swapping `A_k σ_k` for `σ_k A_k`, so those terms cancel
in the sum.  This is the sum half of Mathas 3.24(iii), and it holds with **no** constraint on the
normalisation `d` — cleaner than the multiplicative analogue `sigma_comm_add`. -/
theorem addJM_sigma_comm_add (H : HeckeGenerators R A q) (d : R) (k : ℕ) :
    H.σ k * (addJM H d k + addJM H d (k + 1))
      = (addJM H d k + addJM H d (k + 1)) * H.σ k := by
  rw [mul_add, add_mul, addJM_sigma_left, addJM_sigma_right]
  abel

/-- **The product half only swaps.**  `σ_k (A_k A_{k+1}) = (A_{k+1} A_k) σ_k`.

Mathas 3.24(iii) asserts `T_i` commutes with `L_i L_{i+1}` outright and derives commutativity from
it.  From the **recursion alone** one gets only this swapped form, which is commutation exactly
when `A_k` and `A_{k+1}` already commute — so (iii)'s product half and (iv) are entangled.

**The obstruction survives the change of convention**: this is the same swap seen on the
multiplicative side (`sigma_mul_jm_prod`).  Closing it needs the explicit sum-of-transpositions
expansion of `L_k`, which an abstract presentation does not provide. -/
theorem addJM_sigma_prod_swap (H : HeckeGenerators R A q) (d : R) (k : ℕ) :
    H.σ k * (addJM H d k * addJM H d (k + 1))
      = (addJM H d (k + 1) * addJM H d k) * H.σ k := by
  have hl := addJM_sigma_left H d k
  have hr := addJM_sigma_right H d k
  have hsk : H.σ k * addJM H d k
      = addJM H d (k + 1) * H.σ k - (q - q⁻¹) • addJM H d (k + 1) - d • (1 : A) := by
    rw [hr]; abel
  calc H.σ k * (addJM H d k * addJM H d (k + 1))
      = (H.σ k * addJM H d k) * addJM H d (k + 1) := by noncomm_ring
    _ = (addJM H d (k + 1) * H.σ k - (q - q⁻¹) • addJM H d (k + 1) - d • (1 : A))
          * addJM H d (k + 1) := by rw [hsk]
    _ = addJM H d (k + 1) * (H.σ k * addJM H d (k + 1))
          - (q - q⁻¹) • (addJM H d (k + 1) * addJM H d (k + 1))
          - d • addJM H d (k + 1) := by
        simp only [sub_mul, smul_mul_assoc, one_mul]; noncomm_ring
    _ = addJM H d (k + 1)
          * ((q - q⁻¹) • addJM H d (k + 1) + addJM H d k * H.σ k + d • (1 : A))
          - (q - q⁻¹) • (addJM H d (k + 1) * addJM H d (k + 1))
          - d • addJM H d (k + 1) := by rw [hl]
    _ = _ := by
        simp only [mul_add, mul_smul_comm, mul_one]; noncomm_ring

end QOU.BraidKnot.Hecke
