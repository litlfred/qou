/-
# The trace floor on a PSD-feasible γγ word

Bean `qou-99qc`; probe
`computations/qbeta/qbeta_gamma_gamma_psd_trace_floor_probe.py` (7/7).

The confinement SDP of the 2026-09-08 ruling (`qou-ales`) asks every Wedderburn
projection of a candidate word to be `Matrix.PosSemidef`. Under convention D the
Frobenius pairing `tr_M(w) = Σ_λ y_λ χ_λ(w)` carries **non-negative** weights —
`y_(n−k,k) = [n−2k+1]_q/[2]_q^n` on the two-row partitions, `0` on three rows or
more. A positive semidefinite matrix has non-negative trace, so **every term of
the pairing is non-negative on a PSD-feasible word**, and the pairing is bounded
below by any single term.

The distinguished term is the trivial block. The trivial representation sends
`σᵢ ↦ q`, hence `σᵢ⁻¹ = σᵢ − h ↦ q − h = q⁻¹`, so a γγ vertex `σᵢσᵢ₊₁⁻¹ ↦ 1` and
a product of vertices to `1` — the counit twin of the sorry-free
`QOU.Mass.GammaGammaWordSelection.altChar_eq_one`, which says the same for the
*alternating* character. Its weight is `y_(n) = [n+1]_q/[2]_q^n`, so

    tr_M(w) ≥ [n+1]_q / [2]_q^n

for every PSD-feasible γγ word on `n` strands — independent of which word.

## What is proved here (sorry-free)

* `pairing_ge_weight_of_psdFeasible` — the bound itself, stated on the existing
  `WedderburnBlocks.PSDFeasible` predicate with the distinguished block's trace
  and weight as hypotheses. Falsifiable: drop the non-negativity of the weights
  and it is false.
* `qb_two_mul` — the three-term recurrence `[2]_q·[m+1]_q = [m+2]_q + [m]_q`.
* `traceFloor_strictAnti_step` — the floor `[n+1]_q/[2]_q^n` is **strictly
  decreasing** in `n` for `n ≥ 1` at any real `q > 1`, and the whole content of
  that is `[n]_q > 0`: by the recurrence the step is `[n+2]_q < [2]_q[n+1]_q =
  [n+2]_q + [n]_q`. Falsifiable, and false at `n = 0`, where the floor is `1` at
  both ends — which is why the hypothesis `n ≠ 0` is there rather than for
  convenience.

## What is NOT proved here

The floor is *derived* from three inputs and this file formalises the
combination plus the decay. It does **not** formalise that the convention-D
weights take that closed form, nor that the trivial character is `1` on γγ
words: both are measured in the probe (to `1e-40`), and the second has a
sorry-free twin one character over. They enter the theorem below as explicit
hypotheses, per §3b — a hypothesis-carrying lemma proves the implication, never
the premise.

The numerical crossing (the floor exceeds `Q_β/E₀ = 0.185059` at `n ≤ 5` and
falls below it at `n = 6`) is archimedean arithmetic at the substrate pin and
lives in the probe, not here.
-/
import QOU.Mass.GammaGammaWordSelection
import QOU.Mass.PsdDetOneTrace
import QOU.Archimedean.OcneanuTwoThreeSubstrate

namespace QOU.Archimedean.GammaGammaTraceFloor

open QOU.Mass.GammaGammaWordSelection
open QOU.Eightfold.OcneanuTwoThreeNotProportional
open QOU.Archimedean.OcneanuTwoThreeSubstrate

variable {q : ℝ}

/-! ## The bound -/

/-- **A PSD-feasible candidate's Frobenius pairing is bounded below by the
weight of any block whose character it pins at `1`.**

This is the SDP half of the ruling doing work: `PSDFeasible` forces every
`(B.proj w l).trace` to be non-negative, so with non-negative weights every
term of `Σ_l y l * χ_l(w)` is non-negative and the sum dominates the `l₀`
term, which is `y l₀ * 1`.

The hypotheses are exactly the three ingredients and no more: weight
non-negativity, PSD feasibility, and the distinguished character value. -/
theorem pairing_ge_weight_of_psdFeasible
    {W ι : Type*} {d : ι → ℕ} (B : WedderburnBlocks ℝ W ι d)
    (y : ι → ℝ) (s : Finset ι) (hy : ∀ l ∈ s, 0 ≤ y l)
    {w : W} (hw : B.PSDFeasible w)
    {l₀ : ι} (hl₀ : l₀ ∈ s) (hchi : (B.proj w l₀).trace = 1) :
    y l₀ ≤ ∑ l ∈ s, y l * (B.proj w l).trace := by
  have hterm : ∀ l ∈ s, 0 ≤ y l * (B.proj w l).trace := fun l hl =>
    mul_nonneg (hy l hl) (hw l).trace_nonneg
  have hz : y l₀ = y l₀ * (B.proj w l₀).trace := by rw [hchi, mul_one]
  rw [hz]
  exact Finset.single_le_sum hterm hl₀

/-- **The bound that supersedes the floor below: the pairing is at least `1`.**

`pairing_ge_weight_of_psdFeasible` keeps one term of the pairing and discards
the rest as merely non-negative. They are not merely non-negative: on a
determinant-one block a PSD matrix has trace at least its dimension
(`PsdDetOneTrace.card_le_trace_of_det_one`), so each term is at least
`y l * d l` — and those sum to `1`, because that sum IS the Markov
normalisation `tr_M(1) = 1`.

The determinant hypothesis is not an assumption about the candidate but a
property of the γγ construction: `σᵢ` and `σᵢ₊₁` are conjugate in the braid
group, so their block images share a determinant and every vertex — hence
every word — has determinant `1` in every block. Measured to `1e-39` in the
companion probe; it enters here as a hypothesis per §3b.

The bound is **tight**: the empty word is the identity in every block, so
every trace equals its dimension and the sum is exactly `1`. -/
theorem pairing_ge_one_of_psdFeasible
    {W ι : Type*} {d : ι → ℕ} (B : WedderburnBlocks ℝ W ι d)
    (y : ι → ℝ) (s : Finset ι) (hy : ∀ l ∈ s, 0 ≤ y l)
    (hnorm : ∑ l ∈ s, y l * (d l : ℝ) = 1)
    {w : W} (hw : B.PSDFeasible w)
    (hdet : ∀ l, (B.proj w l).det = 1) :
    1 ≤ ∑ l ∈ s, y l * (B.proj w l).trace := by
  rw [← hnorm]
  refine Finset.sum_le_sum fun l hl => ?_
  exact mul_le_mul_of_nonneg_left
    (QOU.Mass.PsdDetOneTrace.card_le_trace_of_det_one (hw l) (hdet l)) (hy l hl)

/-! ## The floor and its decay

🛑 Everything below is **superseded in strength** by `pairing_ge_one_of_psdFeasible`
above — the floor `[n+1]_q/[2]_q^n` is below `1` at every `n ≥ 2`. It is kept
because it is what the argument gives if you stop at the trivial block, which is
an easy place to stop, and because its decay lemma is the reason the *weaker*
bound's exclusion is one-sided rather than scattered. -/

/-- The floor `[n+1]_q / [2]_q^n` — the convention-D weight of the trivial
block at `n` strands. -/
noncomputable def traceFloor (q : ℝ) (n : ℕ) : ℝ := qb q (n + 1) / qb q 2 ^ n

/-- **The three-term recurrence** `[2]_q · [m+1]_q = [m+2]_q + [m]_q`.

This is what makes the decay below exactly the statement `[n]_q > 0`. -/
theorem qb_two_mul (q : ℝ) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (m : ℕ) :
    qb q 2 * qb q (m + 1) = qb q (m + 2) + qb q m := by
  have h1 : q ^ 2 - 1 ≠ 0 := sub_ne_zero.mpr hq2
  have hm : q ^ m ≠ 0 := pow_ne_zero _ hq
  have hd : q - q⁻¹ = (q ^ 2 - 1) / q := by field_simp
  simp only [qb, hd, pow_add, pow_one]
  field_simp
  ring

/-- **The floor is strictly decreasing for `n ≥ 1`.**

By the recurrence, `traceFloor q (n+1) < traceFloor q n` reduces to
`[n+2]_q < [2]_q [n+1]_q = [n+2]_q + [n]_q`, i.e. to `0 < [n]_q`.

The hypothesis `n ≠ 0` is load-bearing, not defensive: at `n = 0` both sides
are `1` and the strict inequality is false. -/
theorem traceFloor_strictAnti_step (hq : 1 < q) {n : ℕ} (hn : n ≠ 0) :
    traceFloor q (n + 1) < traceFloor q n := by
  have hq0 : q ≠ 0 := by positivity
  have hq2 : q ^ 2 ≠ 1 := q_sq_ne_one hq
  have h2pos : 0 < qb q 2 := qb_pos hq (by norm_num)
  have hpow : 0 < qb q 2 ^ n := pow_pos h2pos n
  have hpow1 : 0 < qb q 2 ^ (n + 1) := pow_pos h2pos (n + 1)
  have hnpos : 0 < qb q n := qb_pos hq hn
  have hrec : qb q 2 * qb q (n + 1) = qb q (n + 2) + qb q n :=
    qb_two_mul q hq0 hq2 n
  have key : qb q (n + 2) * qb q 2 ^ n < qb q (n + 1) * qb q 2 ^ (n + 1) := by
    have : qb q (n + 1) * qb q 2 ^ (n + 1)
        = (qb q (n + 2) + qb q n) * qb q 2 ^ n := by
      rw [pow_succ, ← hrec]; ring
    rw [this]
    have := mul_lt_mul_of_pos_right
      (show qb q (n + 2) < qb q (n + 2) + qb q n by linarith) hpow
    exact this
  simpa only [traceFloor] using (div_lt_div_iff₀ hpow1 hpow).mpr key

/-- **The floor at `n = 0` is `1`**, so the strict step above cannot start
there — recorded so the `n ≠ 0` hypothesis is checkable rather than trusted. -/
theorem traceFloor_zero (hq : 1 < q) : traceFloor q 0 = 1 := by
  have hq0 : q ≠ 0 := by positivity
  have h1 : q ^ 2 - 1 ≠ 0 := sub_ne_zero.mpr (q_sq_ne_one hq)
  have hd : q - q⁻¹ = (q ^ 2 - 1) / q := by field_simp
  simp only [traceFloor, qb, hd, zero_add, pow_zero, div_one, pow_one]
  field_simp

end QOU.Archimedean.GammaGammaTraceFloor
