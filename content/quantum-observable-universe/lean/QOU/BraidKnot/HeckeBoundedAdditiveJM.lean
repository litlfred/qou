import QOU.BraidKnot.HeckeBoundedTheta
import QOU.BraidKnot.HeckeAdditiveJucysMurphy

/-!
# The additive Jucys–Murphy family on the bounded presentation

Tranche 1 of porting `jmRaw_comm` — the one item left on `qou-t1kv`.

## Why the additive family is the route

`jmRaw_comm` is not proved directly.  `HeckeTranspositionExpansion` proves it by identifying the
multiplicative and additive families, `L_k = 1 + A_k` at `d = q − q⁻¹`, and doing the real work on
the **additive** side, where the corresponding statement `addJM_comm` holds for *every* `d`.  So
the port has to carry `addJM` first.

## The bounds here are uniform

Every relation-using lemma in this file bottoms out in `hecke_smul` at index `k`, so all of them
carry the same hypothesis `k + 1 < n` — "`σ_k` is a generator of `H_n(q)`".  That is the cheapest
case; the transposition machinery in the next tranche is where the bounds stop being uniform.

`addJM H d k` itself is a word in `σ₀ … σ_{k−1}`, so it is well-formed for `k < n`; the lemmas need
one more because they multiply by `σ_k`.
-/

namespace QOU.BraidKnot.Hecke

variable {R : Type*} [Field R] {A : Type*} [Ring A] [Algebra R A] {q : R} {n : ℕ}

/-- **Additive Jucys–Murphy family** on a bounded presentation: `A₀ = 0`,
`A_{k+1} = σ_k A_k σ_k + d·σ_k`.  The scalar `d` is free, exactly as in the unbounded development. -/
def addJMB (H : HeckeGeneratorsBelow R A q n) (d : R) : ℕ → A
  | 0 => 0
  | (k + 1) => H.σ k * addJMB H d k * H.σ k + d • H.σ k

@[simp] theorem addJMB_zero (H : HeckeGeneratorsBelow R A q n) (d : R) : addJMB H d 0 = 0 := rfl

theorem addJMB_succ (H : HeckeGeneratorsBelow R A q n) (d : R) (k : ℕ) :
    addJMB H d (k + 1) = H.σ k * addJMB H d k * H.σ k + d • H.σ k := rfl

@[simp] theorem addJMB_toBelow (H : HeckeGenerators R A q) (n : ℕ) (d : R) :
    ∀ k, addJMB (H.toBelow n) d k = addJM H d k
  | 0 => rfl
  | (k + 1) => by rw [addJMB_succ, addJM_succ, addJMB_toBelow H n d k, toBelow_σ]

/-- The Hecke relation in scalar-action form.  Needs `σ_i` to be a generator. -/
theorem heckeB_smul (H : HeckeGeneratorsBelow R A q n) (i : ℕ) (hi : i + 1 < n) :
    H.σ i * H.σ i = (q - q⁻¹) • H.σ i + 1 := by
  rw [H.hecke i hi, Algebra.smul_def]

/-- **Exchange relation, left**: `σ_k A_{k+1} = h·A_{k+1} + A_k σ_k + d`. -/
theorem addJMB_sigma_left (H : HeckeGeneratorsBelow R A q n) (d : R) (k : ℕ) (hk : k + 1 < n) :
    H.σ k * addJMB H d (k + 1)
      = (q - q⁻¹) • addJMB H d (k + 1) + addJMB H d k * H.σ k + d • (1 : A) := by
  rw [addJMB_succ]
  calc H.σ k * (H.σ k * addJMB H d k * H.σ k + d • H.σ k)
      = (H.σ k * H.σ k) * addJMB H d k * H.σ k + d • (H.σ k * H.σ k) := by
        rw [mul_add, mul_smul_comm]; noncomm_ring
    _ = ((q - q⁻¹) • H.σ k + 1) * addJMB H d k * H.σ k
          + d • ((q - q⁻¹) • H.σ k + 1) := by rw [heckeB_smul H k hk]
    _ = _ := by
        simp only [add_mul, one_mul, smul_add, smul_smul, smul_mul_assoc]
        rw [mul_comm d (q - q⁻¹)]
        abel

/-- **Exchange relation, right**: `A_{k+1} σ_k = h·A_{k+1} + σ_k A_k + d`. -/
theorem addJMB_sigma_right (H : HeckeGeneratorsBelow R A q n) (d : R) (k : ℕ) (hk : k + 1 < n) :
    addJMB H d (k + 1) * H.σ k
      = (q - q⁻¹) • addJMB H d (k + 1) + H.σ k * addJMB H d k + d • (1 : A) := by
  rw [addJMB_succ]
  calc (H.σ k * addJMB H d k * H.σ k + d • H.σ k) * H.σ k
      = H.σ k * addJMB H d k * (H.σ k * H.σ k) + d • (H.σ k * H.σ k) := by
        rw [add_mul, smul_mul_assoc]; noncomm_ring
    _ = H.σ k * addJMB H d k * ((q - q⁻¹) • H.σ k + 1)
          + d • ((q - q⁻¹) • H.σ k + 1) := by rw [heckeB_smul H k hk]
    _ = _ := by
        simp only [mul_add, mul_one, smul_add, smul_smul, mul_smul_comm]
        rw [mul_comm d (q - q⁻¹)]
        abel

/-- **`σ_k` commutes with `A_k + A_{k+1}`, for every `d`.**  The sum half of Mathas 3.24(iii). -/
theorem addJMB_sigma_comm_add (H : HeckeGeneratorsBelow R A q n) (d : R) (k : ℕ) (hk : k + 1 < n) :
    H.σ k * (addJMB H d k + addJMB H d (k + 1))
      = (addJMB H d k + addJMB H d (k + 1)) * H.σ k := by
  rw [mul_add, add_mul, addJMB_sigma_left H d k hk, addJMB_sigma_right H d k hk]
  abel

/-- **The product half only swaps**: `σ_k (A_k A_{k+1}) = (A_{k+1} A_k) σ_k`.

As in the unbounded development, the recursion alone gives only the swapped form; closing it needs
the transposition expansion, which is the next tranche. -/
theorem addJMB_sigma_prod_swap (H : HeckeGeneratorsBelow R A q n) (d : R) (k : ℕ) (hk : k + 1 < n) :
    H.σ k * (addJMB H d k * addJMB H d (k + 1))
      = (addJMB H d (k + 1) * addJMB H d k) * H.σ k := by
  have hl := addJMB_sigma_left H d k hk
  have hr := addJMB_sigma_right H d k hk
  have hsk : H.σ k * addJMB H d k
      = addJMB H d (k + 1) * H.σ k - (q - q⁻¹) • addJMB H d (k + 1) - d • (1 : A) := by
    rw [hr]; abel
  calc H.σ k * (addJMB H d k * addJMB H d (k + 1))
      = (H.σ k * addJMB H d k) * addJMB H d (k + 1) := by noncomm_ring
    _ = (addJMB H d (k + 1) * H.σ k - (q - q⁻¹) • addJMB H d (k + 1) - d • (1 : A))
          * addJMB H d (k + 1) := by rw [hsk]
    _ = addJMB H d (k + 1) * (H.σ k * addJMB H d (k + 1))
          - (q - q⁻¹) • (addJMB H d (k + 1) * addJMB H d (k + 1))
          - d • addJMB H d (k + 1) := by
        simp only [sub_mul, smul_mul_assoc, one_mul]; noncomm_ring
    _ = addJMB H d (k + 1)
          * ((q - q⁻¹) • addJMB H d (k + 1) + addJMB H d k * H.σ k + d • (1 : A))
          - (q - q⁻¹) • (addJMB H d (k + 1) * addJMB H d (k + 1))
          - d • addJMB H d (k + 1) := by rw [hl]
    _ = _ := by
        simp only [mul_add, mul_smul_comm, mul_one]; noncomm_ring

end QOU.BraidKnot.Hecke
