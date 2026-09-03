import QOU.BraidKnot.HeckeBoundedGenerators

/-!
# Porting the Jucys–Murphy theory onto the bounded presentation

`HeckeBoundedGenerators.lean` introduced `HeckeGeneratorsBelow R A q n` — the `H_n(q)` relations,
required only for the generator indices that occur there — because
`HeckeStableScalarCascade.stdTwo_no_stable_extension` shows the unbounded `HeckeGenerators` cannot
host an irreducible representation.

This file ports the Jucys–Murphy theory onto it.

## The port GENERALIZES; it does not fork

`HeckeGenerators.toBelow` downcasts every unbounded presentation to a bounded one at **every** `n`,
and `jmRawB_toBelow` / `jmB_toBelow` say the JM elements agree on the nose.  So a theorem proved on
`HeckeGeneratorsBelow` implies its unbounded counterpart immediately — the bounded statement is
strictly stronger, and each ported result below is followed by the recovery of the original as a
corollary rather than a copy.

That is the whole reason to spend the bound bookkeeping: it buys a strictly larger class of models
(now including the 2-dimensional `stdTwoBelow3`) at no loss of theorems.

## What the bounds cost

Each relation is now conditional, so every use carries an index side-condition:

| relation | needs |
|---|---|
| `hecke i` | `i + 1 < n` |
| `braid i` | `i + 2 < n` |
| `far i j` | `i + 1 < j` and `j + 1 < n` |

The side-conditions are what the port has to thread; the algebra is unchanged.

Refs:
- [jones1987] V. Jones, Hecke algebra representations of braid groups and link polynomials.
- [wenzl1988] H. Wenzl, Hecke algebras of type A_n and subfactors.
-/

namespace QOU.BraidKnot.Hecke

variable {R : Type*} [Field R] {A : Type*} [Ring A] [Algebra R A] {q : R} {n : ℕ}

/-! ## §1  The unbounded presentation is a bounded one at every `n` -/

/-- **Downcast.**  `H_∞(q)`'s relations hold at every index, so in particular at every index below
`n`.  This is what makes the bounded class a generalization rather than a parallel development. -/
def HeckeGenerators.toBelow (H : HeckeGenerators R A q) (n : ℕ) :
    HeckeGeneratorsBelow R A q n where
  σ := H.σ
  hecke i _ := H.hecke i
  braid i _ := H.braid i
  far i j hij _ := H.far i j hij

@[simp] theorem toBelow_σ (H : HeckeGenerators R A q) (n i : ℕ) :
    (H.toBelow n).σ i = H.σ i := rfl

/-- The JM elements of the downcast are the original JM elements. -/
@[simp] theorem jmRawB_toBelow (H : HeckeGenerators R A q) (n : ℕ) :
    ∀ k, jmRawB (H.toBelow n) k = jmRaw H k
  | 0 => rfl
  | (i + 1) => by rw [jmRawB_succ, jmRaw_succ, jmRawB_toBelow H n i, toBelow_σ]

/-! ## §2  The `q`-normalized JM elements -/

/-- **`q`-normalized JM elements** on the bounded presentation: `L_{i+1} = q⁻¹ σᵢ Lᵢ σᵢ`. -/
noncomputable def jmB (H : HeckeGeneratorsBelow R A q n) : ℕ → A
  | 0 => 1
  | (i + 1) => q⁻¹ • (H.σ i * jmB H i * H.σ i)

@[simp] theorem jmB_zero (H : HeckeGeneratorsBelow R A q n) : jmB H 0 = 1 := rfl

theorem jmB_succ (H : HeckeGeneratorsBelow R A q n) (i : ℕ) :
    jmB H (i + 1) = q⁻¹ • (H.σ i * jmB H i * H.σ i) := rfl

@[simp] theorem jmB_toBelow (H : HeckeGenerators R A q) (n : ℕ) :
    ∀ k, jmB (H.toBelow n) k = jm H k
  | 0 => rfl
  | (i + 1) => by rw [jmB_succ, jm_succ, jmB_toBelow H n i, toBelow_σ]

/-! ## §3  `L₂` in closed form -/

/-- **`L₂ = (q − q⁻¹)σ₀ + 1`.**  Needs `σ₀` to be a generator of `H_n(q)`, i.e. `1 < n`. -/
theorem jmRawB_closed_two (H : HeckeGeneratorsBelow R A q n) (hn : 1 < n) :
    jmRawB H 1 = algebraMap R A (q - q⁻¹) * H.σ 0 + 1 := by
  rw [jmRawB_succ, jmRawB_zero, mul_one, H.hecke 0 hn]

/-- Recovers `jmRaw_closed_two` from the bounded form. -/
theorem jmRaw_closed_two_of_below (H : HeckeGenerators R A q) :
    jmRaw H 1 = algebraMap R A (q - q⁻¹) * H.σ 0 + 1 := by
  have := jmRawB_closed_two (H.toBelow 2) (by omega)
  rwa [jmRawB_toBelow, toBelow_σ] at this

/-! ## §4  The full twist, and `∏ Lᵢ = Δ²` -/

/-- The full twist of `B₂`: `Δ² = σ₀²`. -/
def fullTwist2B (H : HeckeGeneratorsBelow R A q n) : A := H.σ 0 * H.σ 0

/-- The full twist of `B₃`: `Δ² = (σ₀σ₁)³`. -/
def fullTwist3B (H : HeckeGeneratorsBelow R A q n) : A := (H.σ 0 * H.σ 1) ^ 3

/-- **`∏Lᵢ = Δ²` at `n = 2`** — immediate from the recursion, no relation used at all. -/
theorem jmRawB_prod_two (H : HeckeGeneratorsBelow R A q n) :
    jmRawB H 0 * jmRawB H 1 = fullTwist2B H := by
  rw [jmRawB_zero, one_mul, jmRawB_succ, jmRawB_zero, mul_one]
  rfl

/-- **`∏Lᵢ = Δ²` at `n = 3`.**  One application of the braid relation to the middle three letters.

Only `braid 0` is used, so the hypothesis is `2 < n` — exactly "`σ₀` and `σ₁` are both generators
of `H_n(q)`".  The Hecke relation is not needed. -/
theorem jmRawB_prod_three (H : HeckeGeneratorsBelow R A q n) (hn : 2 < n) :
    jmRawB H 0 * jmRawB H 1 * jmRawB H 2 = fullTwist3B H := by
  have hb := H.braid 0 (by omega)
  simp only [jmRawB_succ, jmRawB_zero, one_mul, mul_one, fullTwist3B, pow_succ, pow_zero]
  calc H.σ 0 * H.σ 0 * (H.σ 1 * (H.σ 0 * H.σ 0) * H.σ 1)
      = H.σ 0 * (H.σ 0 * H.σ 1 * H.σ 0) * (H.σ 0 * H.σ 1) := by noncomm_ring
    _ = H.σ 0 * (H.σ 1 * H.σ 0 * H.σ 1) * (H.σ 0 * H.σ 1) := by rw [hb]
    _ = (H.σ 0 * H.σ 1) * (H.σ 0 * H.σ 1) * (H.σ 0 * H.σ 1) := by noncomm_ring

/-- Recovers `jmRaw_prod_three` from the bounded form. -/
theorem jmRaw_prod_three_of_below (H : HeckeGenerators R A q) :
    jmRaw H 0 * jmRaw H 1 * jmRaw H 2 = fullTwist3 H := by
  have := jmRawB_prod_three (H.toBelow 3) (by omega)
  simpa [fullTwist3B, fullTwist3] using this

/-! ## §5  Far commutation — the easy half of general commutativity -/

/-- `σⱼ` commutes with `L₂ = σ₀²` whenever `j ≥ 2` and `σⱼ` is a generator of `H_n(q)`. -/
theorem sigma_comm_jmRawB_one (H : HeckeGeneratorsBelow R A q n) (j : ℕ) (hj : 1 < j)
    (hjn : j + 1 < n) : H.σ j * jmRawB H 1 = jmRawB H 1 * H.σ j := by
  have h := H.far 0 j (by omega) hjn
  rw [jmRawB_succ, jmRawB_zero, mul_one]
  calc H.σ j * (H.σ 0 * H.σ 0) = (H.σ j * H.σ 0) * H.σ 0 := by noncomm_ring
    _ = (H.σ 0 * H.σ j) * H.σ 0 := by rw [← h]
    _ = H.σ 0 * (H.σ j * H.σ 0) := by noncomm_ring
    _ = H.σ 0 * (H.σ 0 * H.σ j) := by rw [← h]
    _ = H.σ 0 * H.σ 0 * H.σ j := by noncomm_ring

/-- Recovers `sigma_comm_jmRaw_one` from the bounded form. -/
theorem sigma_comm_jmRaw_one_of_below (H : HeckeGenerators R A q) (j : ℕ) (hj : 1 < j) :
    H.σ j * jmRaw H 1 = jmRaw H 1 * H.σ j := by
  have := sigma_comm_jmRawB_one (H.toBelow (j + 2)) j hj (by omega)
  rwa [jmRawB_toBelow, toBelow_σ] at this

end QOU.BraidKnot.Hecke
