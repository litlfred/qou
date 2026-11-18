import QOU.BraidKnot.HeckeJucysMurphyCommutation

/-!
# All JM commutativity reduces to the ADJACENT case

`HeckeJucysMurphyCommutation.lean` proved the adjacent case at `i = 1` only, and recorded that the
exchange relations were exhausted and the half-twist argument did not extend.  This file changes the
shape of the remaining problem rather than attacking it head-on.

## The reduction

`L_{j+1} = σⱼ Lⱼ σⱼ` by definition, and `Lᵢ` commutes with `σⱼ` whenever `j > i`
(`jmRaw_comm_sigma_far`).  Sliding `Lᵢ` past both copies of `σⱼ` gives

    [Lᵢ, L_{j+1}] = σⱼ [Lᵢ, Lⱼ] σⱼ        (`jmRaw_commutator_step`, for j > i)

so the commutator of a *far* pair is a **conjugate** of the commutator one step closer.  Iterating
down to `j = i + 1`:

    [Lᵢ, Lⱼ] = 0  for every j > i   ⟺   [Lᵢ, L_{i+1}] = 0

(`jmRaw_comm_of_adjacent`).  So the adjacent case is not merely the hard case — it is the **only**
case.  Everything else is conjugation.

## Consequence: the `i = 1` row is complete

`jmRaw_comm_adjacent_one` proved `L₂L₃ = L₃L₂`.  Feeding it to the reduction gives
`jmRaw_one_comm_all` : `L₂` commutes with **every** `Lⱼ`, `j ≥ 1` — a whole row of the commutativity
matrix, from what was a single instance.

## What this does and does not settle

It does **not** prove general commutativity: `[Lᵢ, L_{i+1}] = 0` for `i ≥ 2` is still open, and the
reduction gives no purchase on it (it relates *different* `j` at fixed `i`, never different `i`).
What it does is collapse a two-parameter problem to a one-parameter one, and make the `i = 1` result
worth more than an instance.

Since general `∏Lᵢ = Δ²` and the spectral half are also still open, the general-`λ` twist remains
**conditional** — unchanged by this file.

Refs:
- [wenzl1988] Hecke algebra representations.
-/

namespace QOU.BraidKnot.Hecke

variable {R : Type*} [Field R] {A : Type*} [Ring A] [Algebra R A] {q : R}

/-- **The commutator reduction.**  For `j > i`, `[Lᵢ, L_{j+1}] = σⱼ [Lᵢ, Lⱼ] σⱼ`.

`L_{j+1} = σⱼLⱼσⱼ`, and `j > i` lets `Lᵢ` slide past both copies of `σⱼ` by far-commutation.  So a
far commutator is a conjugate of the one a step closer — no cancellation, no Hecke relation. -/
theorem jmRaw_commutator_step (H : HeckeGenerators R A q) (i j : ℕ) (hij : i < j) :
    jmRaw H i * jmRaw H (j + 1) - jmRaw H (j + 1) * jmRaw H i
      = H.σ j * (jmRaw H i * jmRaw H j - jmRaw H j * jmRaw H i) * H.σ j := by
  have hfar : H.σ j * jmRaw H i = jmRaw H i * H.σ j := jmRaw_comm_sigma_far H i j hij
  rw [jmRaw_succ]
  calc jmRaw H i * (H.σ j * jmRaw H j * H.σ j)
        - H.σ j * jmRaw H j * H.σ j * jmRaw H i
      = (jmRaw H i * H.σ j) * jmRaw H j * H.σ j
        - H.σ j * jmRaw H j * (H.σ j * jmRaw H i) := by noncomm_ring
    _ = (H.σ j * jmRaw H i) * jmRaw H j * H.σ j
        - H.σ j * jmRaw H j * (jmRaw H i * H.σ j) := by rw [← hfar, hfar]
    _ = H.σ j * (jmRaw H i * jmRaw H j - jmRaw H j * jmRaw H i) * H.σ j := by noncomm_ring

/-- **Adjacent commutativity implies all of it.**  If `Lᵢ` commutes with `L_{i+1}`, it commutes with
every `Lⱼ` for `j ≥ i`.  Induction on `j`, each step conjugating by `σⱼ` via
`jmRaw_commutator_step`. -/
theorem jmRaw_comm_of_adjacent (H : HeckeGenerators R A q) (i : ℕ)
    (hadj : jmRaw H i * jmRaw H (i + 1) = jmRaw H (i + 1) * jmRaw H i) :
    ∀ j : ℕ, i ≤ j → jmRaw H i * jmRaw H j = jmRaw H j * jmRaw H i := by
  intro j
  induction j with
  | zero => intro h; have : i = 0 := by omega
            subst this; rfl
  | succ m ih =>
      intro hm
      rcases Nat.lt_or_ge i (m + 1) with hlt | hge
      · -- i ≤ m, so the reduction applies at j = m
        rcases Nat.eq_or_lt_of_le (Nat.lt_succ_iff.mp hlt) with heq | hlt2
        · -- m = i : this is exactly the adjacent hypothesis
          subst heq; exact hadj
        · -- i < m : reduce to the commutator at m, which `ih` kills
          have hstep := jmRaw_commutator_step H i m hlt2
          have hzero : jmRaw H i * jmRaw H m - jmRaw H m * jmRaw H i = 0 := by
            rw [ih (by omega)]; exact sub_self _
          rw [hzero] at hstep
          simp only [mul_zero, zero_mul] at hstep
          have := sub_eq_zero.mp hstep
          exact this
      · -- i = m + 1
        have : i = m + 1 := by omega
        subst this; rfl

/-- **The `i = 1` row is complete**: `L₂` commutes with every `Lⱼ`.

`jmRaw_comm_adjacent_one` supplies the adjacent case at `i = 1`; the reduction propagates it to all
`j`.  This upgrades what was a single instance into a full row of the commutativity matrix. -/
theorem jmRaw_one_comm_all (H : HeckeGenerators R A q) (j : ℕ) (hj : 1 ≤ j) :
    jmRaw H 1 * jmRaw H j = jmRaw H j * jmRaw H 1 :=
  jmRaw_comm_of_adjacent H 1 (jmRaw_comm_adjacent_one H) j hj

/-- **The reduction, stated as one hypothesis.**  If every adjacent pair commutes, the whole JM
family is commutative.

When this was written the hypothesis was the open residue for `i ≥ 2`.  It is **no longer open**:
[`HeckeTranspositionExpansion.jmRaw_comm_adjacent`](HeckeTranspositionExpansion.lean) discharges it
outright, via the additive family and Jucys's telescoping, so `jmRaw_comm_all` in that file is this
conclusion with no hypothesis at all. -/
theorem jmRaw_comm_all_of_all_adjacent (H : HeckeGenerators R A q)
    (hadj : ∀ i : ℕ, jmRaw H i * jmRaw H (i + 1) = jmRaw H (i + 1) * jmRaw H i) :
    ∀ i j : ℕ, i ≤ j → jmRaw H i * jmRaw H j = jmRaw H j * jmRaw H i :=
  fun i => jmRaw_comm_of_adjacent H i (hadj i)

/-- Subtracting the reversed product from the product of the first Jucys-Murphy element with any higher element yields zero (`qou-m8s9`). -/
theorem jmRaw_one_comm_sub_eq_zero (H : HeckeGenerators R A q) (j : ℕ) (hj : 1 ≤ j) :
    jmRaw H 1 * jmRaw H j - jmRaw H j * jmRaw H 1 = 0 := by
  rw [jmRaw_one_comm_all H j hj, sub_self]

end QOU.BraidKnot.Hecke
