import QOU.BraidKnot.StaircaseHookMultiset

/-!
# The hook sum is a quadratic form, and the staircase is its unique minimiser

`two_mul_sum_hookZ_betaForm` puts the hook sum in β-coordinates as a one-body sum minus a pair
sum, and `sum_pair_betaR_sub` collapses that pair sum — for a **descending** β-set — to a single
row sum `Σ_i (L − 1 − 2i) β_i`.  Composing them says something the `REV_n` arc had not noticed:

    2 H(μ)  =  Σ_{i<L} [ β_i(β_i + 1) − 2(L − 1 − 2i) β_i ] ,

so `H` is **separable and quadratic** in the β-coordinates, with no interaction term left at all.

The consequence is the point of this file.  Compare two shapes of the same size in one `L`-row
frame and write `u_i = β_i(ν) − β_i(μ)`.  Expanding the square,

    2(H(ν) − H(μ))  =  Σ_i u_i · r_i  +  Σ_i u_i² ,    r_i := 2β_i(μ) + 1 − 2(L − 1 − 2i) ,

and the staircase is exactly the shape that makes `r` harmless.  On `δ_k`,

    r_i  =  (2k + 1)  +  2·(i − k)        (truncated subtraction, so the second term is 0 for
                                           i ≤ k) —  `staircase_bracket`,

which does not depend on `L` at all.  Equal size forces `Σ_i u_i = 0` (`two_mul_sum_betaR`), so
the constant part of `r` contributes nothing; and where the remaining part is nonzero — rows
`i > k`, which the staircase does not reach — `u_i` is just `ν`'s own row length, hence `≥ 0`.
Both surviving terms are therefore non-negative:

    2(H(ν) − H(δ_k))  =  Σ_{i>k} 2(i − k) λ_i(ν)  +  Σ_i u_i²  ≥  0 .

| | |
|---|---|
| `two_mul_sum_hookZ_separable` | `H` is a separable quadratic in β; no pair term survives |
| `staircase_two_mul_hookSum_sub` | the deficiency, exactly, in any frame |
| `staircase_hookSum_le` | the staircase **minimises** the hook sum at its own size |
| `staircase_hookSum_eq_iff` | and **uniquely**: equality forces `λ(ν) = δ_k` row by row |
| `staircase_two_mul_hookSum_sub_of_le` | in a frame of `k+1` rows the first term vanishes and the deficiency is a bare sum of squares |

## Why the arc wanted this

`REV_n`'s objective is `Σ_c ε(h(c)) − ln q₀ · H(μ)` (`betaSide_eq_hookSum`, #7294), so `H` is the
whole of its cost term.  Everything else in the objective is built from `ε(m) ~ q₀^(−2m)` and is
therefore **exponentially screened** — a short-range gain, range `1/(2 ln q₀) ≈ 4.8` sites.  This
file says the cost it is weighed against is `ln q₀ · (1/2) Σ u_i²`: a local, quadratic penalty on
displacement away from the staircase lattice, with no long-range piece at all.  The excess
`e_k = M_n − V(δ_k)`, the arc's one remaining open quantity, is thus the ground state of
short-range repulsion against a harmonic restoring term — and since `Σ u_i² ∈ 2ℤ` whenever
`Σ u_i = 0`, that cost moves only in whole steps of `ln q₀`.

Measured: `rev_exact_maximiser_small_n_probe.py` enumerates **every** partition of `n = T_k`,
checks the identity as exact integers (0 violations), and confirms the split of `e_k` into
screened gain minus quadratic cost to 1e-40.

## What this does NOT claim

Nothing here bounds `e_k`.  That needs the gain side — the `ε` terms — which is not in this
file, and which is what `qou-hok7` is still open on.  The minimality is also stated for the
`hookZ`-sum over a frame containing both shapes; `betaSide_padding_invariant` is why choosing
that frame costs nothing.

## Base ring (§7c)

`ℤ` throughout, and only because hook sums are doubled to avoid halving; no archimedean
construct, nothing past the substrate wall.

-- Ref: [leitner2026] computations/deltalambda/rev_exact_maximiser_small_n_probe.py
-/

namespace QOU.BraidKnot.HookSum

open Finset QOU.BraidKnot.PieceA

/-- **The hook sum is separable in β-coordinates.**  No pair term survives:

    2 Σ_{c∈μ} h(c) = Σ_{i<L} [ β_i(β_i + 1) − 2(L − 1 − 2i) β_i ] .

Immediate from `two_mul_sum_hookZ_betaForm` and `sum_pair_betaR_sub`; the content is entirely in
the latter, which is where the descending order of the β-set is used. -/
theorem two_mul_sum_hookZ_separable (μ : YoungDiagram) {L : ℕ} (hL : μ.colLen 0 ≤ L) :
    2 * ∑ c ∈ μ.cells, hookZ μ c
      = ∑ i ∈ range L,
          (((QOU.SchurWeyl.betaR L μ i : ℕ) : ℤ) * (((QOU.SchurWeyl.betaR L μ i : ℕ) : ℤ) + 1)
            - 2 * (((L : ℤ) - 1 - 2 * (i : ℤ))
                * ((QOU.SchurWeyl.betaR L μ i : ℕ) : ℤ))) := by
  rw [two_mul_sum_hookZ_betaForm μ hL (le_refl _), sum_pair_betaR_sub μ L, Finset.mul_sum,
    ← Finset.sum_sub_distrib]

/-- **The difference of two hook sums, in the displacement `u = β(ν) − β(μ)`.**  A linear term
against `r_i = 2β_i(μ) + 1 − 2(L − 1 − 2i)` plus a bare sum of squares — the expansion of the
separable quadratic, with nothing dropped and no hypothesis beyond a common frame. -/
theorem two_mul_sum_hookZ_sub (μ ν : YoungDiagram) {L : ℕ}
    (hLμ : μ.colLen 0 ≤ L) (hLν : ν.colLen 0 ≤ L) :
    2 * ((∑ c ∈ ν.cells, hookZ ν c) - ∑ c ∈ μ.cells, hookZ μ c)
      = ∑ i ∈ range L,
          ((((QOU.SchurWeyl.betaR L ν i : ℕ) : ℤ) - ((QOU.SchurWeyl.betaR L μ i : ℕ) : ℤ))
              * (2 * ((QOU.SchurWeyl.betaR L μ i : ℕ) : ℤ) + 1
                  - 2 * ((L : ℤ) - 1 - 2 * (i : ℤ)))
            + (((QOU.SchurWeyl.betaR L ν i : ℕ) : ℤ)
                - ((QOU.SchurWeyl.betaR L μ i : ℕ) : ℤ)) ^ 2) := by
  rw [mul_sub, two_mul_sum_hookZ_separable ν hLν, two_mul_sum_hookZ_separable μ hLμ,
    ← Finset.sum_sub_distrib]
  exact Finset.sum_congr rfl fun i _ => by ring

/-- **Equal size makes the displacement traceless.**  `2 Σ_{i<L} β_i = 2n + L(L−1)`
(`two_mul_sum_betaR`), and the second term does not see the shape, so two diagrams of the same
size in the same frame have `Σ_i u_i = 0`. -/
theorem sum_betaR_sub_eq_zero (μ ν : YoungDiagram) {L : ℕ}
    (hLμ : μ.colLen 0 ≤ L) (hLν : ν.colLen 0 ≤ L)
    (hcard : ν.cells.card = μ.cells.card) :
    ∑ i ∈ range L,
        (((QOU.SchurWeyl.betaR L ν i : ℕ) : ℤ) - ((QOU.SchurWeyl.betaR L μ i : ℕ) : ℤ)) = 0 := by
  have hμ := two_mul_sum_betaR μ hLμ
  have hν := two_mul_sum_betaR ν hLν
  rw [hcard] at hν
  rw [Finset.sum_sub_distrib]
  linarith

/-- The displacement is frame-free: the `(L − 1 − i)` in `β_i = λ_i + (L − 1 − i)` cancels, so
`u_i` is the difference of row lengths and does not depend on the padding. -/
theorem betaR_sub_eq_rowLen_sub (μ ν : YoungDiagram) {L i : ℕ} (hi : i < L) :
    ((QOU.SchurWeyl.betaR L ν i : ℕ) : ℤ) - ((QOU.SchurWeyl.betaR L μ i : ℕ) : ℤ)
      = (ν.rowLen i : ℤ) - (μ.rowLen i : ℤ) := by
  rw [betaR_cast ν hi, betaR_cast μ hi]
  ring

/-! ## The staircase's bracket -/

/-- **The staircase's bracket, in any frame:** `r_i = (2k + 1) + 2·(i − k)`, with truncated
subtraction, so the second term vanishes for `i ≤ k`.  The `L` cancels — which is the reason the
minimality below needs no restriction on the padding. -/
theorem staircase_bracket (k i L : ℕ) (hi : i < L) :
    2 * ((QOU.SchurWeyl.betaR L (staircaseYD k) i : ℕ) : ℤ) + 1
        - 2 * ((L : ℤ) - 1 - 2 * (i : ℤ))
      = 2 * (k : ℤ) + 1 + 2 * (((i - k : ℕ)) : ℤ) := by
  rw [betaR_cast (staircaseYD k) hi, staircaseYD_rowLen]
  omega

/-- The staircase reaches exactly `k` rows, so every frame with `k ≤ L` contains it. -/
theorem staircase_colLen_zero (k : ℕ) : (staircaseYD k).colLen 0 = k := by
  rw [staircaseYD_colLen]
  omega

/-- Where the staircase's bracket is not constant — the rows `i > k`, which `δ_k` does not
reach — the displacement is `ν`'s own row length, hence non-negative.  Elsewhere the factor is
zero.  Either way the product is `≥ 0`. -/
theorem staircase_bracket_term_nonneg (k : ℕ) (ν : YoungDiagram) {L i : ℕ} (hi : i < L) :
    0 ≤ 2 * (((i - k : ℕ)) : ℤ)
        * (((QOU.SchurWeyl.betaR L ν i : ℕ) : ℤ)
            - ((QOU.SchurWeyl.betaR L (staircaseYD k) i : ℕ) : ℤ)) := by
  rw [betaR_sub_eq_rowLen_sub (staircaseYD k) ν hi, staircaseYD_rowLen]
  rcases le_or_gt i k with h | h
  · have : (i - k : ℕ) = 0 := by omega
    rw [this]
    simp
  · have hik : (k - i : ℕ) = 0 := by omega
    rw [hik]
    have h1 : (0 : ℤ) ≤ 2 * (((i - k : ℕ)) : ℤ) := by positivity
    have h2 : (0 : ℤ) ≤ ((ν.rowLen i : ℤ) - ((0 : ℕ) : ℤ)) := by
      simp
    exact mul_nonneg h1 h2

/-! ## The deficiency -/

/-- **The hook sum's deficiency above the staircase, exactly.**  For every `ν` of the staircase's
size, in any frame containing both,

    2 ( H(ν) − H(δ_k) )  =  Σ_{i<L} 2(i − k)·u_i  +  Σ_{i<L} u_i² ,

with `u_i = β_i(ν) − β_i(δ_k) = λ_i(ν) − λ_i(δ_k)` and truncated subtraction in `(i − k)`.  An
identity, not a bound: no term of the expansion is discarded and `ν` may be arbitrarily far from
the staircase. -/
theorem staircase_two_mul_hookSum_sub (k : ℕ) (ν : YoungDiagram) {L : ℕ}
    (hLν : ν.colLen 0 ≤ L) (hk : k ≤ L)
    (hcard : ν.cells.card = (staircaseYD k).cells.card) :
    2 * ((∑ c ∈ ν.cells, hookZ ν c)
          - ∑ c ∈ (staircaseYD k).cells, hookZ (staircaseYD k) c)
      = (∑ i ∈ range L, 2 * (((i - k : ℕ)) : ℤ)
            * (((QOU.SchurWeyl.betaR L ν i : ℕ) : ℤ)
                - ((QOU.SchurWeyl.betaR L (staircaseYD k) i : ℕ) : ℤ)))
        + ∑ i ∈ range L,
            (((QOU.SchurWeyl.betaR L ν i : ℕ) : ℤ)
              - ((QOU.SchurWeyl.betaR L (staircaseYD k) i : ℕ) : ℤ)) ^ 2 := by
  have hLs : (staircaseYD k).colLen 0 ≤ L := by rw [staircase_colLen_zero]; exact hk
  rw [two_mul_sum_hookZ_sub (staircaseYD k) ν hLs hLν]
  have hterm : ∀ i ∈ range L,
      (((QOU.SchurWeyl.betaR L ν i : ℕ) : ℤ)
            - ((QOU.SchurWeyl.betaR L (staircaseYD k) i : ℕ) : ℤ))
          * (2 * ((QOU.SchurWeyl.betaR L (staircaseYD k) i : ℕ) : ℤ) + 1
              - 2 * ((L : ℤ) - 1 - 2 * (i : ℤ)))
        + (((QOU.SchurWeyl.betaR L ν i : ℕ) : ℤ)
            - ((QOU.SchurWeyl.betaR L (staircaseYD k) i : ℕ) : ℤ)) ^ 2
      = (((QOU.SchurWeyl.betaR L ν i : ℕ) : ℤ)
            - ((QOU.SchurWeyl.betaR L (staircaseYD k) i : ℕ) : ℤ)) * (2 * (k : ℤ) + 1)
        + (2 * (((i - k : ℕ)) : ℤ)
            * (((QOU.SchurWeyl.betaR L ν i : ℕ) : ℤ)
                - ((QOU.SchurWeyl.betaR L (staircaseYD k) i : ℕ) : ℤ))
          + (((QOU.SchurWeyl.betaR L ν i : ℕ) : ℤ)
              - ((QOU.SchurWeyl.betaR L (staircaseYD k) i : ℕ) : ℤ)) ^ 2) := by
    intro i hi
    rw [staircase_bracket k i L (mem_range.mp hi)]
    ring
  rw [Finset.sum_congr rfl hterm, Finset.sum_add_distrib, ← Finset.sum_mul,
    sum_betaR_sub_eq_zero (staircaseYD k) ν hLs hLν hcard, zero_mul, zero_add,
    Finset.sum_add_distrib]

/-- **In a frame of `k + 1` rows the linear term is absent outright**, and the deficiency is a
bare sum of squares:

    2 ( H(ν) − H_min )  =  Σ_{i<k+1} u_i² .

This is the sharp form the `REV_n` arc uses, and it is what makes the cost *quantised*: with
`Σ u_i = 0` the right-hand side is an even integer, so `H − H_min ∈ ℤ_{≥0}`.  It needs
`ν.colLen 0 ≤ k + 1`; a taller shape has the same hook multiset as its transpose, so the
general form above covers it. -/
theorem staircase_two_mul_hookSum_sub_of_le (k : ℕ) (ν : YoungDiagram)
    (hLν : ν.colLen 0 ≤ k + 1)
    (hcard : ν.cells.card = (staircaseYD k).cells.card) :
    2 * ((∑ c ∈ ν.cells, hookZ ν c)
          - ∑ c ∈ (staircaseYD k).cells, hookZ (staircaseYD k) c)
      = ∑ i ∈ range (k + 1),
          (((QOU.SchurWeyl.betaR (k + 1) ν i : ℕ) : ℤ)
            - ((QOU.SchurWeyl.betaR (k + 1) (staircaseYD k) i : ℕ) : ℤ)) ^ 2 := by
  rw [staircase_two_mul_hookSum_sub k ν hLν (by omega) hcard]
  have hzero : ∀ i ∈ range (k + 1),
      2 * (((i - k : ℕ)) : ℤ)
          * (((QOU.SchurWeyl.betaR (k + 1) ν i : ℕ) : ℤ)
              - ((QOU.SchurWeyl.betaR (k + 1) (staircaseYD k) i : ℕ) : ℤ)) = 0 := by
    intro i hi
    have : (i - k : ℕ) = 0 := by
      have := mem_range.mp hi
      omega
    rw [this]
    simp
  rw [Finset.sum_congr rfl hzero, Finset.sum_const_zero, zero_add]

/-! ## Minimality -/

/-- **The staircase minimises the hook sum** at its own size.  Both terms of the deficiency are
non-negative — the first by `staircase_bracket_term_nonneg`, the second because it is a sum of
squares — and no frame restriction is needed. -/
theorem staircase_hookSum_le (k : ℕ) (ν : YoungDiagram) {L : ℕ}
    (hLν : ν.colLen 0 ≤ L) (hk : k ≤ L)
    (hcard : ν.cells.card = (staircaseYD k).cells.card) :
    (∑ c ∈ (staircaseYD k).cells, hookZ (staircaseYD k) c) ≤ ∑ c ∈ ν.cells, hookZ ν c := by
  have h := staircase_two_mul_hookSum_sub k ν hLν hk hcard
  have h1 : (0 : ℤ) ≤ ∑ i ∈ range L, 2 * (((i - k : ℕ)) : ℤ)
      * (((QOU.SchurWeyl.betaR L ν i : ℕ) : ℤ)
          - ((QOU.SchurWeyl.betaR L (staircaseYD k) i : ℕ) : ℤ)) :=
    Finset.sum_nonneg fun i hi => staircase_bracket_term_nonneg k ν (mem_range.mp hi)
  have h2 : (0 : ℤ) ≤ ∑ i ∈ range L,
      (((QOU.SchurWeyl.betaR L ν i : ℕ) : ℤ)
        - ((QOU.SchurWeyl.betaR L (staircaseYD k) i : ℕ) : ℤ)) ^ 2 :=
    Finset.sum_nonneg fun i _ => sq_nonneg _
  linarith

/-- **And uniquely.**  Equality forces every displacement to vanish, so `ν` has the staircase's
row lengths throughout the frame — the hook sum's minimiser at triangular size is the staircase
and nothing else. -/
theorem staircase_hookSum_eq_iff (k : ℕ) (ν : YoungDiagram) {L : ℕ}
    (hLν : ν.colLen 0 ≤ L) (hk : k ≤ L)
    (hcard : ν.cells.card = (staircaseYD k).cells.card) :
    (∑ c ∈ ν.cells, hookZ ν c)
          = ∑ c ∈ (staircaseYD k).cells, hookZ (staircaseYD k) c
      ↔ ∀ i < L, ν.rowLen i = (staircaseYD k).rowLen i := by
  have h := staircase_two_mul_hookSum_sub k ν hLν hk hcard
  have h1 : (0 : ℤ) ≤ ∑ i ∈ range L, 2 * (((i - k : ℕ)) : ℤ)
      * (((QOU.SchurWeyl.betaR L ν i : ℕ) : ℤ)
          - ((QOU.SchurWeyl.betaR L (staircaseYD k) i : ℕ) : ℤ)) :=
    Finset.sum_nonneg fun i hi => staircase_bracket_term_nonneg k ν (mem_range.mp hi)
  constructor
  · intro heq i hi
    rw [heq, sub_self, mul_zero] at h
    have h2 : (0 : ℤ) ≤ ∑ i ∈ range L,
        (((QOU.SchurWeyl.betaR L ν i : ℕ) : ℤ)
          - ((QOU.SchurWeyl.betaR L (staircaseYD k) i : ℕ) : ℤ)) ^ 2 :=
      Finset.sum_nonneg fun i _ => sq_nonneg _
    have hsq : ∑ i ∈ range L,
        (((QOU.SchurWeyl.betaR L ν i : ℕ) : ℤ)
          - ((QOU.SchurWeyl.betaR L (staircaseYD k) i : ℕ) : ℤ)) ^ 2 = 0 := by linarith
    have hz := (Finset.sum_eq_zero_iff_of_nonneg
      (fun j (_ : j ∈ range L) => sq_nonneg
        (((QOU.SchurWeyl.betaR L ν j : ℕ) : ℤ)
          - ((QOU.SchurWeyl.betaR L (staircaseYD k) j : ℕ) : ℤ)))).mp hsq i (mem_range.mpr hi)
    have hu : ((QOU.SchurWeyl.betaR L ν i : ℕ) : ℤ)
        - ((QOU.SchurWeyl.betaR L (staircaseYD k) i : ℕ) : ℤ) = 0 :=
      pow_eq_zero_iff (n := 2) (by norm_num) |>.mp hz
    rw [betaR_sub_eq_rowLen_sub (staircaseYD k) ν hi] at hu
    omega
  · intro hall
    have hu : ∀ i ∈ range L, ((QOU.SchurWeyl.betaR L ν i : ℕ) : ℤ)
        - ((QOU.SchurWeyl.betaR L (staircaseYD k) i : ℕ) : ℤ) = 0 := by
      intro i hi
      rw [betaR_sub_eq_rowLen_sub (staircaseYD k) ν (mem_range.mp hi), hall i (mem_range.mp hi)]
      ring
    have hA : ∑ i ∈ range L, 2 * (((i - k : ℕ)) : ℤ)
        * (((QOU.SchurWeyl.betaR L ν i : ℕ) : ℤ)
            - ((QOU.SchurWeyl.betaR L (staircaseYD k) i : ℕ) : ℤ)) = 0 :=
      Finset.sum_eq_zero fun i hi => by rw [hu i hi]; ring
    have hB : ∑ i ∈ range L,
        (((QOU.SchurWeyl.betaR L ν i : ℕ) : ℤ)
          - ((QOU.SchurWeyl.betaR L (staircaseYD k) i : ℕ) : ℤ)) ^ 2 = 0 :=
      Finset.sum_eq_zero fun i hi => by rw [hu i hi]; ring
    rw [hA, hB, add_zero] at h
    linarith

end QOU.BraidKnot.HookSum
