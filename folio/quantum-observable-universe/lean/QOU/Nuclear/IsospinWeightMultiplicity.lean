import Mathlib.Tactic

/-!
# QOU.Nuclear.IsospinWeightMultiplicity — the `1/A` in the isospin multiplicity

Bean `qou-o8lo` (ledger gap G2), epic `qou-myts`. Follow-up to
`QOU.Nuclear.IsospinTwistWrithe`, which shows that the braid-channel `T(T+1)` term is
exactly `0` on γγ-selected words. This file looks at the other place a `1/A` comes out of
the representation theory: how many states the `N`-strand space has at a given isospin.

Two counts, both pure combinatorics:

* **Block count** `twoRowDim N k = C(N,k) − C(N,k−1)`, the dimension of the two-row Hecke
  block with `k` cells in its second row (`twoRowDim_hook`: equal to the hook-length value
  `C(N,k)(N−2k+1)/(N−k+1)`). Its isospin is `T = (N − 2k)/2`.
* **Weight count** `C(N,k)`: the number of states with `T_z = (N − 2k)/2`. The telescoping
  `sum_twoRowDim` says it is the sum of the block counts with `T ≥ |T_z|`. This is the
  count at fixed `(Z, N)`, i.e. what a nucleus actually fixes.

The weight count has **no** `ln(2T+1)` piece. Its suppression away from the balanced point is
Gaussian with variance `∝ N`:

* `weight_step`: `C(2M, M−s−1)·(M+s+1) = C(2M, M−s)·(M−s)`;
* `weight_le`: `C(2M, M−s)·(M+s+s²) ≤ C(2M, M)·(M+s)` for `s ≤ M`.

So `C(2M, M−s)/C(2M, M) ≤ 1/(1 + s²/(M+s))`: the scale of `s` is `√M`, and with `N = 2M = 3A`
any energy linear in `ln` of this count is a function of `s²/N ∝ (N_n − Z)²/A`. No log, no
real number, and no measured value is used. Which energy map turns a count into an energy
is **not** settled here.

Scope: `ℕ`/`ℚ`/`ℤ` combinatorics; §7c does not apply.
-/

namespace QOU.Nuclear.IsospinWeightMultiplicity

/-- Dimension of the two-row block of `N` boxes with `k` boxes in the second row,
as `C(N,k) − C(N,k−1)` (with `C(N,−1) = 0`). -/
def twoRowDim (N k : ℕ) : ℤ := (N.choose k : ℤ) - (if k = 0 then 0 else (N.choose (k - 1) : ℤ))

/-- **The weight count is the sum of the block counts**: `Σ_{j ≤ k} d(N, j) = C(N, k)`. -/
theorem sum_twoRowDim (N k : ℕ) :
    ∑ j ∈ Finset.range (k + 1), twoRowDim N j = (N.choose k : ℤ) := by
  induction k with
  | zero => simp [twoRowDim]
  | succ k ih =>
    rw [Finset.sum_range_succ, ih]
    simp [twoRowDim]

/-- **Hook-length form**: `d(N, k)·(N − k + 1) = C(N, k)·(N − 2k + 1)` for `k ≤ N`. -/
theorem twoRowDim_hook (N k : ℕ) (hk : k ≤ N) :
    twoRowDim N k * ((N : ℤ) - k + 1) = (N.choose k : ℤ) * ((N : ℤ) - 2 * k + 1) := by
  rcases k with _ | j
  · simp [twoRowDim]
  · have h := Nat.choose_succ_right_eq N j
    have hj : j ≤ N := by omega
    have h' : ((N.choose (j + 1) : ℕ) : ℤ) * (j + 1) = (N.choose j : ℤ) * ((N : ℤ) - j) := by
      have := congrArg (fun x : ℕ => (x : ℤ)) h
      push_cast [Nat.cast_sub hj] at this
      linarith
    simp only [twoRowDim, Nat.add_one_ne_zero, if_false, Nat.add_sub_cancel]
    push_cast
    linear_combination h'

/-- **One step away from balance**: `C(2M, M−s−1)·(M+s+1) = C(2M, M−s)·(M−s)`. -/
theorem weight_step (M s : ℕ) (hs : s < M) :
    (2 * M).choose (M - (s + 1)) * (M + s + 1) = (2 * M).choose (M - s) * (M - s) := by
  have h := Nat.choose_succ_right_eq (2 * M) (M - (s + 1))
  have e1 : M - (s + 1) + 1 = M - s := by omega
  have e2 : 2 * M - (M - (s + 1)) = M + s + 1 := by omega
  rw [e1, e2] at h
  exact h.symm

/-- **Gaussian suppression with no logarithm**: for `s ≤ M`,
`C(2M, M−s)·(M + s + s²) ≤ C(2M, M)·(M + s)`. -/
theorem weight_le (M s : ℕ) (hs : s ≤ M) :
    ((2 * M).choose (M - s) : ℚ) * (M + s + s ^ 2) ≤ ((2 * M).choose M : ℚ) * (M + s) := by
  induction s with
  | zero => simp
  | succ s ih =>
    have hs' : s < M := by omega
    have ih := ih (by omega)
    have hstep := weight_step M s hs'
    have hstepQ : ((2 * M).choose (M - (s + 1)) : ℚ) * (M + s + 1)
        = ((2 * M).choose (M - s) : ℚ) * ((M : ℚ) - s) := by
      have := congrArg (fun x : ℕ => (x : ℚ)) hstep
      push_cast [Nat.cast_sub hs'.le] at this
      exact this
    set c := ((2 * M).choose (M - s) : ℚ)
    set c' := ((2 * M).choose (M - (s + 1)) : ℚ)
    set c0 := ((2 * M).choose M : ℚ)
    have hM : (s : ℚ) + 1 ≤ M := by exact_mod_cast hs'
    have hc : 0 ≤ c := by positivity
    have hpos : (0 : ℚ) < M + s + 1 := by positivity
    -- c' = c (M−s)/(M+s+1); reduce to a polynomial inequality
    have key : c * ((M : ℚ) - s) * ((M : ℚ) + s + 1 + (s + 1) ^ 2)
        ≤ c0 * ((M : ℚ) + s + 1) ^ 2 := by
      have hA : 0 ≤ (M : ℚ) + s + s ^ 2 := by positivity
      have poly : ((M : ℚ) + s) * ((M : ℚ) - s) * ((M : ℚ) + s + 1 + (s + 1) ^ 2)
          ≤ ((M : ℚ) + s + s ^ 2) * ((M : ℚ) + s + 1) ^ 2 := by
        nlinarith [sq_nonneg ((s : ℚ)), sq_nonneg ((M : ℚ) - s), mul_nonneg (by positivity : (0:ℚ) ≤ s) (by positivity : (0:ℚ) ≤ M)]
      have hB : 0 ≤ ((M : ℚ) - s) * ((M : ℚ) + s + 1 + (s + 1) ^ 2) := by
        apply mul_nonneg <;> nlinarith
      by_cases hz : (M : ℚ) + s + s ^ 2 = 0
      · have : (M : ℚ) = 0 := by nlinarith [sq_nonneg (s : ℚ)]
        nlinarith
      · have hApos : 0 < (M : ℚ) + s + s ^ 2 := lt_of_le_of_ne hA (Ne.symm hz)
        have hc_le : c ≤ c0 * ((M : ℚ) + s) / ((M : ℚ) + s + s ^ 2) := by
          rw [le_div_iff₀ hApos]; linarith
        calc c * ((M : ℚ) - s) * ((M : ℚ) + s + 1 + (s + 1) ^ 2)
            = c * (((M : ℚ) - s) * ((M : ℚ) + s + 1 + (s + 1) ^ 2)) := by ring
          _ ≤ c0 * ((M : ℚ) + s) / ((M : ℚ) + s + s ^ 2)
                * (((M : ℚ) - s) * ((M : ℚ) + s + 1 + (s + 1) ^ 2)) :=
              mul_le_mul_of_nonneg_right hc_le hB
          _ = c0 / ((M : ℚ) + s + s ^ 2)
                * (((M : ℚ) + s) * ((M : ℚ) - s) * ((M : ℚ) + s + 1 + (s + 1) ^ 2)) := by ring
          _ ≤ c0 / ((M : ℚ) + s + s ^ 2) * (((M : ℚ) + s + s ^ 2) * ((M : ℚ) + s + 1) ^ 2) :=
              mul_le_mul_of_nonneg_left poly (by positivity)
          _ = c0 * ((M : ℚ) + s + 1) ^ 2 := by field_simp
    push_cast
    have : c' * ((M : ℚ) + (s + 1) + (s + 1) ^ 2) * ((M : ℚ) + s + 1)
        ≤ c0 * ((M : ℚ) + (s + 1)) * ((M : ℚ) + s + 1) := by
      calc c' * ((M : ℚ) + (s + 1) + (s + 1) ^ 2) * ((M : ℚ) + s + 1)
          = (c' * ((M : ℚ) + s + 1)) * ((M : ℚ) + s + 1 + (s + 1) ^ 2) := by ring
        _ = c * ((M : ℚ) - s) * ((M : ℚ) + s + 1 + (s + 1) ^ 2) := by rw [hstepQ]
        _ ≤ c0 * ((M : ℚ) + s + 1) ^ 2 := key
        _ = c0 * ((M : ℚ) + (s + 1)) * ((M : ℚ) + s + 1) := by ring
    exact le_of_mul_le_mul_right this hpos

/-- Non-vacuity at `M = 3, s = 2` (`N = 6`): `C(6,1)·(3+2+4) = 54 ≤ C(6,3)·5 = 100`. -/
example : ((6 : ℕ).choose 1 : ℚ) * (3 + 2 + 2 ^ 2) ≤ ((6 : ℕ).choose 3 : ℚ) * (3 + 2) := by
  norm_num [Nat.choose]

/-- Non-vacuity of the telescoping: at `N = 6`, `d(6,0)+d(6,1)+d(6,2)+d(6,3) = 1+5+9+5 = 20 = C(6,3)`. -/
example : twoRowDim 6 0 + twoRowDim 6 1 + twoRowDim 6 2 + twoRowDim 6 3 = 20 := by decide

/-! ## Markov-trace (quantum-trace) weighting of a `T_z` sector

Carl, 2026-11-27: "use qCLT". Under convention D the Markov trace on `H_N(q)` is the
`U_q(sl₂)` quantum trace on `V^{⊗N}`, which weights a weight vector of `T_z = (N − 2k)/2`
by `q^{N−k} q⁻ᵏ` (up to the overall `[2]_q^N`). So the `T_z` sector weighs
`C(N,k)·q^{N−k}·qi^k`. Two exact facts, over any commutative ring with `q·qi = 1`:

* `markov_sector_sum`: the sectors add up to `(q + qi)^N = [2]_q^N`, the Markov normaliser;
* `markov_sector_mirror`: a sector times its mirror (`T_z ↔ −T_z`) is `C(N,k)²`, with no `q`.

So the `q`-weighting adds only an **odd** factor `q^{2T_z}` to each sector; the even part, the
part a symmetry energy reads, is the classical count `C(N,k)` exactly. -/

section MarkovSector

variable {R : Type*} [CommRing R]

/-- The Markov (quantum-trace) weight of the sector with `k` down-strands. -/
def markovSector (q qi : R) (N k : ℕ) : R := (N.choose k : R) * q ^ (N - k) * qi ^ k

/-- **The sectors sum to `(q + qi)^N`**, the Markov normaliser `[2]_q^N`. -/
theorem markov_sector_sum (q qi : R) (N : ℕ) :
    ∑ k ∈ Finset.range (N + 1), markovSector q qi N k = (q + qi) ^ N := by
  rw [show (q + qi) ^ N = (qi + q) ^ N by ring, add_pow]
  refine Finset.sum_congr rfl fun k _ => ?_
  unfold markovSector; ring

/-- **A sector times its mirror is the squared classical count**, with no `q` left. -/
theorem markov_sector_mirror (q qi : R) (hq : q * qi = 1) (N k : ℕ) (hk : k ≤ N) :
    markovSector q qi N k * markovSector q qi N (N - k) = ((N.choose k : R)) ^ 2 := by
  unfold markovSector
  rw [Nat.choose_symm hk, Nat.sub_sub_self hk]
  have : q ^ (N - k) * qi ^ k * (q ^ k * qi ^ (N - k)) = (q * qi) ^ N := by
    rw [mul_pow]
    calc q ^ (N - k) * qi ^ k * (q ^ k * qi ^ (N - k))
        = (q ^ (N - k) * q ^ k) * (qi ^ k * qi ^ (N - k)) := by ring
      _ = q ^ N * qi ^ N := by rw [← pow_add, ← pow_add, Nat.sub_add_cancel hk,
            Nat.add_sub_cancel' hk]
  calc (N.choose k : R) * q ^ (N - k) * qi ^ k * ((N.choose k : R) * q ^ k * qi ^ (N - k))
      = (N.choose k : R) ^ 2 * (q ^ (N - k) * qi ^ k * (q ^ k * qi ^ (N - k))) := by ring
    _ = (N.choose k : R) ^ 2 := by rw [this, hq, one_pow, mul_one]

end MarkovSector

end QOU.Nuclear.IsospinWeightMultiplicity
