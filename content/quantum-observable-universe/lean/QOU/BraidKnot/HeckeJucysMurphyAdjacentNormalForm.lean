import QOU.BraidKnot.HeckeJucysMurphyReduction

/-!
# The adjacent commutator as ONE word identity

`HeckeJucysMurphyReduction.lean` showed that all JM commutativity reduces to the adjacent case, and
that the adjacent case is proved only at `i = 1`.  This file reduces the adjacent case itself to a
single concrete identity between two braid words, at every index.

## The normal forms

Write `u := σ_k`, `v := σ_{k+1}`, `N := L_k`.  Then `L_{k+1} = uNu` and `L_{k+2} = vuNuv`, and

    L_{k+1} L_{k+2} = (uv) N (uv) N (uv)          `jmRaw_adjacent_left`
    L_{k+2} L_{k+1} = (uvu) N (uv) N u            `jmRaw_adjacent_right`

Each is **two rewrites**: one braid relation `uvu = vuv`, and one use of `N`'s commutation with `v`
(`jmRaw_comm_sigma_far`, since `k < k+1`).  The Hecke relation is not used.

So adjacent commutativity at index `k+1` is *exactly* the assertion that these two words agree.

## Why this is progress

The previous formulation, `LᵢL_{i+1} = L_{i+1}Lᵢ`, hides `Lᵢ` inside itself — every attempt
unfolded the recursion again and reproduced a commutator of the same shape (recorded in
`qou-u9o1`).  In the normal forms **`N` appears twice, opaquely, and the only structure left is
braid-word bookkeeping around it.**  Both sides start with `uv`, so after cancelling that unit the
question is

    N (uv) N (uv)  =?=  u N (uv) N u

with `N` an arbitrary element commuting with `v`.  That is a self-contained question about one
unknown, not about the JM recursion.

## Consistency at k = 0

At `k = 0`, `N = L₀ = 1` and the forms collapse to `(uv)³` and `(uvu)(uv)u`
(`jmRaw_adjacent_left_zero`, `jmRaw_adjacent_right_zero`).  Those are exactly the two words
`jmRaw_prod_three` and `jmRaw_two_mul_one` identify with `(σ₀σ₁)³` and `(σ₁σ₀)³`, which
`fullTwist3_symm` proves equal.  So the `i = 1` case is recovered as the `N = 1` specialisation —
the normal forms are consistent with the one case already known.

## Still open

The identity above for general `N` — i.e. adjacent commutativity at `k ≥ 1`.  Nothing here proves
it; what is gained is that it is now one word identity in one unknown rather than a recursion that
regenerates itself.  Consequently general `∏Lᵢ = Δ²` and the general-`λ` twist remain open and
conditional respectively.

Refs:
- [wenzl1988] Hecke algebra representations.
-/

namespace QOU.BraidKnot.Hecke

variable {R : Type*} [Field R] {A : Type*} [Ring A] [Algebra R A] {q : R}

/-- **Left normal form**: `L_{k+1} L_{k+2} = (uv) N (uv) N (uv)` with `u = σ_k`, `v = σ_{k+1}`,
`N = L_k`.  One braid move, one commutation of `N` past `v`. -/
theorem jmRaw_adjacent_left (H : HeckeGenerators R A q) (k : ℕ) :
    jmRaw H (k + 1) * jmRaw H (k + 2)
      = (H.σ k * H.σ (k + 1)) * jmRaw H k * (H.σ k * H.σ (k + 1)) * jmRaw H k
          * (H.σ k * H.σ (k + 1)) := by
  have hb : H.σ k * H.σ (k + 1) * H.σ k = H.σ (k + 1) * H.σ k * H.σ (k + 1) := H.braid k
  have hNv : H.σ (k + 1) * jmRaw H k = jmRaw H k * H.σ (k + 1) :=
    jmRaw_comm_sigma_far H k (k + 1) (by omega)
  show H.σ k * jmRaw H k * H.σ k
      * (H.σ (k + 1) * (H.σ k * jmRaw H k * H.σ k) * H.σ (k + 1)) = _
  calc H.σ k * jmRaw H k * H.σ k
        * (H.σ (k + 1) * (H.σ k * jmRaw H k * H.σ k) * H.σ (k + 1))
      = H.σ k * jmRaw H k * (H.σ k * H.σ (k + 1) * H.σ k) * jmRaw H k
          * H.σ k * H.σ (k + 1) := by noncomm_ring
    _ = H.σ k * jmRaw H k * (H.σ (k + 1) * H.σ k * H.σ (k + 1)) * jmRaw H k
          * H.σ k * H.σ (k + 1) := by rw [hb]
    _ = H.σ k * (jmRaw H k * H.σ (k + 1)) * H.σ k * H.σ (k + 1) * jmRaw H k
          * H.σ k * H.σ (k + 1) := by noncomm_ring
    _ = H.σ k * (H.σ (k + 1) * jmRaw H k) * H.σ k * H.σ (k + 1) * jmRaw H k
          * H.σ k * H.σ (k + 1) := by rw [hNv]
    _ = _ := by noncomm_ring

/-- **Right normal form**: `L_{k+2} L_{k+1} = (uvu) N (uv) N u`.  Same two rewrites, applied to the
mirrored word — note it ends in `u`, not `uv`, which is the whole difference from the left form. -/
theorem jmRaw_adjacent_right (H : HeckeGenerators R A q) (k : ℕ) :
    jmRaw H (k + 2) * jmRaw H (k + 1)
      = (H.σ k * H.σ (k + 1) * H.σ k) * jmRaw H k * (H.σ k * H.σ (k + 1)) * jmRaw H k
          * H.σ k := by
  have hb : H.σ k * H.σ (k + 1) * H.σ k = H.σ (k + 1) * H.σ k * H.σ (k + 1) := H.braid k
  have hNv : H.σ (k + 1) * jmRaw H k = jmRaw H k * H.σ (k + 1) :=
    jmRaw_comm_sigma_far H k (k + 1) (by omega)
  show H.σ (k + 1) * (H.σ k * jmRaw H k * H.σ k) * H.σ (k + 1)
      * (H.σ k * jmRaw H k * H.σ k) = _
  calc H.σ (k + 1) * (H.σ k * jmRaw H k * H.σ k) * H.σ (k + 1)
        * (H.σ k * jmRaw H k * H.σ k)
      = H.σ (k + 1) * H.σ k * jmRaw H k * (H.σ k * H.σ (k + 1) * H.σ k) * jmRaw H k
          * H.σ k := by noncomm_ring
    _ = H.σ (k + 1) * H.σ k * jmRaw H k * (H.σ (k + 1) * H.σ k * H.σ (k + 1)) * jmRaw H k
          * H.σ k := by rw [hb]
    _ = H.σ (k + 1) * H.σ k * (jmRaw H k * H.σ (k + 1)) * H.σ k * H.σ (k + 1) * jmRaw H k
          * H.σ k := by noncomm_ring
    _ = H.σ (k + 1) * H.σ k * (H.σ (k + 1) * jmRaw H k) * H.σ k * H.σ (k + 1) * jmRaw H k
          * H.σ k := by rw [hNv]
    _ = (H.σ (k + 1) * H.σ k * H.σ (k + 1)) * jmRaw H k * (H.σ k * H.σ (k + 1)) * jmRaw H k
          * H.σ k := by noncomm_ring
    _ = _ := by rw [← hb]

/-! ## Consistency at `k = 0`, where `N = 1` -/

/-- At `k = 0` the left form collapses to `(σ₀σ₁)³` — matching `jmRaw_prod_three`. -/
theorem jmRaw_adjacent_left_zero (H : HeckeGenerators R A q) :
    jmRaw H 1 * jmRaw H 2 = (H.σ 0 * H.σ 1) ^ 3 := by
  rw [jmRaw_adjacent_left H 0, jmRaw_zero]
  noncomm_ring

/-- At `k = 0` the right form collapses to `(σ₀σ₁σ₀)(σ₀σ₁)σ₀`, which `fullTwist3_symm` identifies
with the left one — recovering `jmRaw_comm_adjacent_one` as the `N = 1` specialisation. -/
theorem jmRaw_adjacent_right_zero (H : HeckeGenerators R A q) :
    jmRaw H 2 * jmRaw H 1
      = (H.σ 0 * H.σ 1 * H.σ 0) * (H.σ 0 * H.σ 1) * H.σ 0 := by
  rw [jmRaw_adjacent_right H 0, jmRaw_zero]
  noncomm_ring

/-- **The open question, stated once.**  Adjacent commutativity at `k+1` holds exactly when the two
normal forms agree.  This is a restatement, not a proof — but it isolates the problem as a single
word identity in the one unknown `N = L_k`, with no recursion left to unfold. -/
theorem jmRaw_adjacent_iff_normal_forms (H : HeckeGenerators R A q) (k : ℕ) :
    jmRaw H (k + 1) * jmRaw H (k + 2) = jmRaw H (k + 2) * jmRaw H (k + 1)
      ↔ (H.σ k * H.σ (k + 1)) * jmRaw H k * (H.σ k * H.σ (k + 1)) * jmRaw H k
            * (H.σ k * H.σ (k + 1))
        = (H.σ k * H.σ (k + 1) * H.σ k) * jmRaw H k * (H.σ k * H.σ (k + 1)) * jmRaw H k
            * H.σ k := by
  rw [jmRaw_adjacent_left H k, jmRaw_adjacent_right H k]

end QOU.BraidKnot.Hecke
