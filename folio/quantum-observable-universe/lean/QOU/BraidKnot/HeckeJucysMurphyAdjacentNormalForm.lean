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

for the specific `N = L_k`.

**Do NOT read that as a question about an arbitrary `N` commuting with `v` — that reading is
FALSE.**  Taking `N = v`, which certainly commutes with `v`, the two sides differ already in the
2-dimensional irrep of `H₃(q)` at `q = 2`
([`jm_adjacent_generic_N_counterexample.py`](../../../../../computations/hecke/jm_adjacent_generic_N_counterexample.py),
exact rational arithmetic).  So adjacent commutativity genuinely needs `L_k`'s structure, not merely
its commutation with `v`; an attack that only assumes the latter cannot work.  (The `N = 1` line in
that script is a control — Lean proves that case, and a first version of the script that reported
`False` there was measuring its own bug, not the mathematics.)

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

/-! ## A proved SUFFICIENT condition

Measurement in the faithful regular representations of `H₄` and `H₅`
([`jm_adjacent_h4_structure_probe.py`](../../../../../computations/hecke/jm_adjacent_h4_structure_probe.py))
showed the identity holds for some `N` and fails for others, with the pattern **independent of `q`**
but **dependent on `k`** — `s₀` fails at `k = 1` and holds at `k = 2`.  The explanation is that at
`k = 2` the element `s₀` commutes with *both* `u = σ₂` and `v = σ₃`, and that is enough. -/

/-- **`(uv)³ = (uvu)(uv)u`** at every index — both sides are `(uvu)²`.

The left side regroups as `(uvu)(vuv)` and one braid move turns the second factor into `uvu`; the
right side is `(uvu)(uvu)` by associativity alone.  This is the index-`k` form of the half-twist
identity `fullTwist3_symm`. -/
theorem braid_cube_eq (H : HeckeGenerators R A q) (k : ℕ) :
    (H.σ k * H.σ (k + 1)) ^ 3
      = (H.σ k * H.σ (k + 1) * H.σ k) * (H.σ k * H.σ (k + 1)) * H.σ k := by
  have hb : H.σ k * H.σ (k + 1) * H.σ k = H.σ (k + 1) * H.σ k * H.σ (k + 1) := H.braid k
  calc (H.σ k * H.σ (k + 1)) ^ 3
      = (H.σ k * H.σ (k + 1) * H.σ k) * (H.σ (k + 1) * H.σ k * H.σ (k + 1)) := by noncomm_ring
    _ = (H.σ k * H.σ (k + 1) * H.σ k) * (H.σ k * H.σ (k + 1) * H.σ k) := by rw [← hb]
    _ = _ := by noncomm_ring

/-- **Sufficient condition: an `N` commuting with both `u` and `v` satisfies the identity.**

If `N` commutes with `σ_k` and `σ_{k+1}` it commutes with everything in sight, so both normal forms
collapse to `N² · (uv)³` and `N² · (uvu)(uv)u` respectively, and `braid_cube_eq` finishes.

**This is sufficient, NOT necessary** — and the distinction is measured, not guessed.  At `k = 2` in
`H₅`, `N = σ₃² = v²` satisfies the identity while *not* commuting with `u = σ₂` (they are adjacent).
So this condition explains part of the data and cannot be the characterisation.

It also does **not** apply to the case that matters: `N = L_k` does not commute with `σ_k` — the
hook word `L_k` ends in `σ_{k-1}`, adjacent to `σ_k` — which is exactly why adjacent commutativity
is hard and why this lemma does not close it. -/
theorem jmRaw_adjacent_of_comm (H : HeckeGenerators R A q) (k : ℕ) (N : A)
    (hu : N * H.σ k = H.σ k * N) (hv : N * H.σ (k + 1) = H.σ (k + 1) * N) :
    (H.σ k * H.σ (k + 1)) * N * (H.σ k * H.σ (k + 1)) * N * (H.σ k * H.σ (k + 1))
      = (H.σ k * H.σ (k + 1) * H.σ k) * N * (H.σ k * H.σ (k + 1)) * N * H.σ k := by
  have hcu : Commute N (H.σ k) := hu
  have hcv : Commute N (H.σ (k + 1)) := hv
  have hcw : Commute N (H.σ k * H.σ (k + 1)) := hcu.mul_right hcv
  have hcx : Commute N (H.σ k * H.σ (k + 1) * H.σ k) := hcw.mul_right hcu
  have e1 : (H.σ k * H.σ (k + 1)) * N = N * (H.σ k * H.σ (k + 1)) := hcw.eq.symm
  have e2 : (H.σ k * H.σ (k + 1) * H.σ k) * N = N * (H.σ k * H.σ (k + 1) * H.σ k) := hcx.eq.symm
  have hcube := braid_cube_eq H k
  have hL : (H.σ k * H.σ (k + 1)) * N * (H.σ k * H.σ (k + 1)) * N * (H.σ k * H.σ (k + 1))
      = N * N * ((H.σ k * H.σ (k + 1)) ^ 3) := by
    calc (H.σ k * H.σ (k + 1)) * N * (H.σ k * H.σ (k + 1)) * N * (H.σ k * H.σ (k + 1))
        = ((H.σ k * H.σ (k + 1)) * N) * ((H.σ k * H.σ (k + 1)) * N)
            * (H.σ k * H.σ (k + 1)) := by noncomm_ring
      _ = (N * (H.σ k * H.σ (k + 1))) * (N * (H.σ k * H.σ (k + 1)))
            * (H.σ k * H.σ (k + 1)) := by rw [e1]
      _ = (N * (H.σ k * H.σ (k + 1))) ^ 2 * (H.σ k * H.σ (k + 1)) := by noncomm_ring
      _ = (N ^ 2 * (H.σ k * H.σ (k + 1)) ^ 2) * (H.σ k * H.σ (k + 1)) := by rw [hcw.mul_pow]
      _ = _ := by noncomm_ring
  have hR : (H.σ k * H.σ (k + 1) * H.σ k) * N * (H.σ k * H.σ (k + 1)) * N * H.σ k
      = N * N * ((H.σ k * H.σ (k + 1) * H.σ k) * (H.σ k * H.σ (k + 1)) * H.σ k) := by
    calc (H.σ k * H.σ (k + 1) * H.σ k) * N * (H.σ k * H.σ (k + 1)) * N * H.σ k
        = ((H.σ k * H.σ (k + 1) * H.σ k) * N) * ((H.σ k * H.σ (k + 1)) * N)
            * H.σ k := by noncomm_ring
      _ = (N * (H.σ k * H.σ (k + 1) * H.σ k)) * (N * (H.σ k * H.σ (k + 1)))
            * H.σ k := by rw [e1, e2]
      _ = N * ((H.σ k * H.σ (k + 1) * H.σ k) * N) * (H.σ k * H.σ (k + 1))
            * H.σ k := by noncomm_ring
      _ = N * (N * (H.σ k * H.σ (k + 1) * H.σ k)) * (H.σ k * H.σ (k + 1))
            * H.σ k := by rw [e2]
      _ = _ := by noncomm_ring
  rw [hL, hR, hcube]

end QOU.BraidKnot.Hecke
