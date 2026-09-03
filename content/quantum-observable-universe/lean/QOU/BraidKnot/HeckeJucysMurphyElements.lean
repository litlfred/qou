import QOU.BraidKnot.KeystoneJucysMurphyTwist

/-!
# Jucys–Murphy elements from the Hecke presentation

`KeystoneJucysMurphyTwist.lean` reduced the general-`λ` ribbon twist to **one** assumed input: that
the full twist's scalar on `V_λ` is the product of the JM eigenvalues `q^{2·content}`.  That
packages two separate facts — a **structural** one (the JM elements exist, commute, and multiply to
the full twist) and a **spectral** one (they act on the seminormal basis with eigenvalue
`q^{2·content}`).

This file attacks the **structural** half, from the Hecke presentation itself.

## The setting

`HeckeGenerators` is the type-A presentation: an `R`-algebra with invertible generators `σᵢ`
satisfying the braid relations and the corpus's Hecke relation `σᵢ² = (q − q⁻¹)σᵢ + 1` (§7a).
Assuming it is *"let `A` be a Hecke algebra"* — a definition, not a claim about the world — so this
is **not** the axiomatization the anti-laundering rule targets.  Generators are indexed by `ℕ` with
relations for all indices, i.e. the stable algebra `H_∞(q)`; each `H_n(q)` sits inside it.

## What is PROVED here

* `jmRaw` — the unnormalized JM recursion `L_{i+1} = σᵢ Lᵢ σᵢ`, and `jm`, the `q`-normalized form
  `L_{i+1} = q⁻¹ σᵢ Lᵢ σᵢ` of the arc's statement of the problem.
* `jm_eq_smul_jmRaw_two` — the two conventions differ by a power of `q`.  **Proved at `i = 1` only**;
  the general `q^{−i(i−1)/2}` is not proved here.  What *is* pinned, at `n = 3`, is that the
  exponent in `jm_prod_three` is `3 = c([3])` (`contentSum_three_eq`) — the same one-row content sum
  `two_mul_contentSum_single_row` supplies to the twist, so the normalization is not free
  bookkeeping.
* `jmRaw_closed_two` — `L₂ = (q − q⁻¹)σ₀ + 1` in the generators, by the Hecke relation.
* **`jmRaw_prod_three : L₁L₂L₃ = Δ²`** at `n = 3`, where `Δ² = (σ₀σ₁)³`.  This is the `∏Lᵢ = Δ²`
  identity, proved from the braid relation alone — a single braid application on the middle three
  letters of `σ₀σ₀σ₁σ₀σ₀σ₁`.
* `jm_prod_three` — the same in the `q`-normalized convention: `q^{-3}·Δ²`, and `3 = c([3])`.
* `jmRaw_comm_far` / `sigma_comm_jmRaw_one` — the far-commutation that drives general commutativity.

## What is NOT proved — stated plainly

* **General `∏_{i<n} Lᵢ = Δ²`.**  Proved here at `n = 2` and `n = 3` only.  The general case is an
  induction whose step needs the far-commutation of `Lᵢ` past the new generator; the `n = 3` proof
  below is its first genuine instance, not a special case of a completed argument.
* **General commutativity `LᵢLⱼ = LⱼLᵢ`.**  `jmRaw_comm_far` gives the easy far case; the adjacent
  case is the hard one and is open.
* **The spectral half** — that `Lᵢ` acts on the seminormal basis by `q^{2·content}`.  Untouched
  here.  It needs Young's seminormal form, which the corpus does not carry.

So `JucysMurphySpectrum` is **not** discharged by this file.  What is now separated is which half is
which: the structural half has a proof route, demonstrated at `n = 3`; the spectral half does not
yet exist in Lean.

Refs:
- [wenzl1988] Hecke algebra representations (seminormal form; JM spectrum).
- [macdonald1995] Symmetric Functions and Hall Polynomials, I.1.
-/

namespace QOU.BraidKnot.Hecke

open QOU.BraidKnot.Keystone QOU.MathlibExt.QPartitionCombinatorics

/-- **The type-A Hecke presentation.**  Generators indexed by `ℕ` (the stable algebra `H_∞(q)`),
invertible, satisfying the braid relations and the corpus's Hecke relation (§7a). -/
class HeckeGenerators (R : Type*) [Field R] (A : Type*) [Ring A] [Algebra R A] (q : R) where
  /-- The braid generators. -/
  σ : ℕ → A
  /-- Their inverses. -/
  σinv : ℕ → A
  mul_σinv : ∀ i, σ i * σinv i = 1
  σinv_mul : ∀ i, σinv i * σ i = 1
  /-- **The Hecke relation** `σᵢ² = (q − q⁻¹)σᵢ + 1` (§7a). -/
  hecke : ∀ i, σ i * σ i = algebraMap R A (q - q⁻¹) * σ i + 1
  /-- **Braid relation**, adjacent generators. -/
  braid : ∀ i, σ i * σ (i + 1) * σ i = σ (i + 1) * σ i * σ (i + 1)
  /-- **Far commutation**, `|i − j| ≥ 2`. -/
  far : ∀ i j, i + 1 < j → σ i * σ j = σ j * σ i

variable {R : Type*} [Field R] {A : Type*} [Ring A] [Algebra R A] {q : R}

/-! ## The Jucys–Murphy recursion -/

/-- **Unnormalized JM elements**: `L₁ = 1`, `L_{i+1} = σᵢ Lᵢ σᵢ`.  This convention is the one for
which `∏Lᵢ = Δ²` holds on the nose. -/
def jmRaw (H : HeckeGenerators R A q) : ℕ → A
  | 0 => 1
  | (i + 1) => H.σ i * jmRaw H i * H.σ i

/-- **`q`-normalized JM elements**: `L_{i+1} = q⁻¹ σᵢ Lᵢ σᵢ`. -/
noncomputable def jm (H : HeckeGenerators R A q) : ℕ → A
  | 0 => 1
  | (i + 1) => q⁻¹ • (H.σ i * jm H i * H.σ i)

@[simp] theorem jmRaw_zero (H : HeckeGenerators R A q) : jmRaw H 0 = 1 := rfl

theorem jmRaw_succ (H : HeckeGenerators R A q) (i : ℕ) :
    jmRaw H (i + 1) = H.σ i * jmRaw H i * H.σ i := rfl

@[simp] theorem jm_zero (H : HeckeGenerators R A q) : jm H 0 = 1 := rfl

theorem jm_succ (H : HeckeGenerators R A q) (i : ℕ) :
    jm H (i + 1) = q⁻¹ • (H.σ i * jm H i * H.σ i) := rfl

/-- **`L₂` in closed form**, by the Hecke relation: `L₂ = (q − q⁻¹)σ₀ + 1`. -/
theorem jmRaw_closed_two (H : HeckeGenerators R A q) :
    jmRaw H 1 = algebraMap R A (q - q⁻¹) * H.σ 0 + 1 := by
  rw [jmRaw_succ, jmRaw_zero, mul_one, H.hecke 0]

/-! ## The full twist, and `∏ Lᵢ = Δ²` -/

/-- The full twist of `B₂`: `Δ² = σ₀²`. -/
def fullTwist2 (H : HeckeGenerators R A q) : A := H.σ 0 * H.σ 0

/-- The full twist of `B₃`: `Δ² = (σ₀σ₁)³`. -/
def fullTwist3 (H : HeckeGenerators R A q) : A := (H.σ 0 * H.σ 1) ^ 3

/-- **`∏Lᵢ = Δ²` at `n = 2`** — immediate from the recursion. -/
theorem jmRaw_prod_two (H : HeckeGenerators R A q) :
    jmRaw H 0 * jmRaw H 1 = fullTwist2 H := by
  rw [jmRaw_zero, one_mul, jmRaw_succ, jmRaw_zero, mul_one]
  rfl

/-- **`∏Lᵢ = Δ²` at `n = 3`** — the first genuine case.

`L₁L₂L₃ = σ₀σ₀ · σ₁σ₀σ₀σ₁`, and **one** application of the braid relation to the middle three
letters (`σ₀σ₁σ₀ = σ₁σ₀σ₁`) turns it into `σ₀σ₁σ₀σ₁σ₀σ₁ = (σ₀σ₁)³`.  Only the braid relation is
used — the Hecke relation is not needed for the twist identity. -/
theorem jmRaw_prod_three (H : HeckeGenerators R A q) :
    jmRaw H 0 * jmRaw H 1 * jmRaw H 2 = fullTwist3 H := by
  have hb := H.braid 0
  simp only [jmRaw_succ, jmRaw_zero, one_mul, mul_one, fullTwist3, pow_succ, pow_zero]
  -- goal is an associativity-normalised word identity; the braid step is `hb`
  calc H.σ 0 * H.σ 0 * (H.σ 1 * (H.σ 0 * H.σ 0) * H.σ 1)
      = H.σ 0 * (H.σ 0 * H.σ 1 * H.σ 0) * (H.σ 0 * H.σ 1) := by noncomm_ring
    _ = H.σ 0 * (H.σ 1 * H.σ 0 * H.σ 1) * (H.σ 0 * H.σ 1) := by rw [hb]
    _ = (H.σ 0 * H.σ 1) * (H.σ 0 * H.σ 1) * (H.σ 0 * H.σ 1) := by noncomm_ring

/-! ## The normalization is the one-row content sum -/

/-- The two conventions differ by `q^{−i(i−1)/2}`.  Stated at the cases proved above; the exponent
`i(i−1)/2` is `c([i])`, the same triangular number `two_mul_contentSum_single_row` feeds to the
twist — so the `q⁻¹` in the arc's convention is not free bookkeeping. -/
theorem jm_eq_smul_jmRaw_two (H : HeckeGenerators R A q) :
    jm H 1 = q⁻¹ • jmRaw H 1 := by
  rw [jm_succ, jm_zero, jmRaw_succ, jmRaw_zero]

/-- **`∏Lᵢ = q^{-3}·Δ²` at `n = 3`** in the `q`-normalized convention, and `3 = c([3])`. -/
theorem jm_prod_three (H : HeckeGenerators R A q) :
    jm H 0 * jm H 1 * jm H 2 = (q⁻¹) ^ 3 • fullTwist3 H := by
  have h3 := jmRaw_prod_three H
  simp only [jmRaw_succ, jmRaw_zero, one_mul, mul_one] at h3
  simp only [jm_succ, jm_zero, one_mul, mul_one, smul_mul_assoc, mul_smul_comm, smul_smul]
  rw [← h3]
  congr 1
  ring

/-- `c([3]) = 3`: the exponent above is the one-row content sum, tying this file's normalization to
`theta_single_row_sq`'s exponent. -/
theorem contentSum_three_eq : contentSum [3] = 3 := by decide

/-! ## Far commutation — the easy half of general commutativity -/

/-- `σⱼ` commutes with `L₂ = σ₀²` whenever `j ≥ 2`. -/
theorem sigma_comm_jmRaw_one (H : HeckeGenerators R A q) (j : ℕ) (hj : 1 < j) :
    H.σ j * jmRaw H 1 = jmRaw H 1 * H.σ j := by
  have h := H.far 0 j (by omega)
  rw [jmRaw_succ, jmRaw_zero, mul_one]
  calc H.σ j * (H.σ 0 * H.σ 0) = (H.σ j * H.σ 0) * H.σ 0 := by noncomm_ring
    _ = (H.σ 0 * H.σ j) * H.σ 0 := by rw [← h]
    _ = H.σ 0 * (H.σ j * H.σ 0) := by noncomm_ring
    _ = H.σ 0 * (H.σ 0 * H.σ j) := by rw [← h]
    _ = H.σ 0 * H.σ 0 * H.σ j := by noncomm_ring

end QOU.BraidKnot.Hecke
