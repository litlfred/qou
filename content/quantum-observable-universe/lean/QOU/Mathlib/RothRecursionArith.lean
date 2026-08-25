/-
  **The arithmetic core of Roth's-lemma recursion** — Mahler §13's case split.

  Bean `qou-4lbh`.  ⚠ Mathlib-style, Mathlib imports only, no QOU dependency: liftable
  verbatim.  Pure `ℚ` arithmetic; no polynomial machinery appears.

  ═══ WHY THIS EXISTS ═══

  `QOU/Mathlib/RothInductionStep.lean` proves the induction step's inequality by combining
  the pieces **linearly** and dividing through, and the sixth correction recorded that the
  resulting error term is too large to be useful.

  Reading Mahler, *Lectures on Diophantine Approximations*, Ch. 5 §13 showed why: the argument
  is **not linear**.  It sets `N = ⌊(J(A)−t)·r⌋ + 1`, splits on `n ≤ N` versus `n > N`, and in
  the second case extracts a **square-root** bound.  A linear combination cannot produce that
  shape, which is why the linear form looked hopeless.

  This module is that case's arithmetic, isolated from the polynomial content.

  ═══ WHAT THE CASE SPLIT ACTUALLY BUYS ═══

  ⚠ Worth noting, because it is easy to misread the source: the first case's conclusion
  `J ≤ t + S` holds **unconditionally**, not just when `n ≤ N`.  It is just the `ν = 0` term of
  the sum, since every term is non-negative.  So the case split's real content is entirely in
  the second case — the quadratic bound `sq_mul_le_two_mul_of_sum_le` below.

  ═══ ⚠ PROVENANCE ═══

  Reconstructed from a **partly illegible scan** (`uploads/roth_lemma.pdf`, added in commit
  `ca1ae1a2eb`).  The structure — truncated arithmetic progression, ceiling cut-off, quadratic
  conclusion — is legible; several constants in the original are not.

  What is below is **Lean-checked and therefore true**.  What is *not* established is that its
  constants match Mahler's exactly.  Anyone wiring this into the recursion should re-derive the
  constants against a clean copy rather than trusting this transcription.
-/
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Order.Floor.Defs
import Mathlib.Algebra.Order.Floor.Ring
import Mathlib.Data.Rat.Floor
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.BigOperators.Intervals
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp

open Finset

namespace RothArith

/-- Gauss's sum, divided through. -/
theorem sum_range_div (r : ℚ) (K : ℕ) :
    ∑ ν ∈ range K, ((ν : ℚ) / r) = (K : ℚ) * ((K : ℚ) - 1) / (2 * r) := by
  rcases eq_or_ne r 0 with rfl | hr
  · simp
  · induction K with
    | zero => simp
    | succ p ih =>
        rw [Finset.sum_range_succ, ih]
        field_simp
        push_cast
        ring

/-- **The truncated sum bound.**  For any cut-off `K ≤ n`, the sum of `max 0 (θ − ν/r)` over
`ν < n` is at least the untruncated arithmetic progression over `ν < K`.

Two slacknesses, both free: the tail `K ≤ ν < n` is dropped because every term is
non-negative, and `max 0 x ≥ x` is used on the retained terms.  No hypothesis relating `K` to
`θ` or `r` is needed — the caller chooses `K` to make the bound sharp. -/
theorem sum_max_sub_ge (θ r : ℚ) (n K : ℕ) (hK : K ≤ n) :
    (K : ℚ) * θ - ((K : ℚ) * ((K : ℚ) - 1)) / (2 * r)
      ≤ ∑ ν ∈ range n, max 0 (θ - (ν : ℚ) / r) := by
  have hss : range K ⊆ range n := by
    intro x hx
    simp only [Finset.mem_range] at hx ⊢
    omega
  have hsub : ∑ ν ∈ range K, max 0 (θ - (ν : ℚ) / r)
      ≤ ∑ ν ∈ range n, max 0 (θ - (ν : ℚ) / r) :=
    Finset.sum_le_sum_of_subset_of_nonneg hss (fun i _ _ => le_max_left _ _)
  refine le_trans ?_ hsub
  have hterm : ∑ ν ∈ range K, (θ - (ν : ℚ) / r)
      ≤ ∑ ν ∈ range K, max 0 (θ - (ν : ℚ) / r) :=
    Finset.sum_le_sum fun i _ => le_max_right _ _
  refine le_trans (le_of_eq ?_) hterm
  rw [Finset.sum_sub_distrib, Finset.sum_const, card_range, nsmul_eq_mul, sum_range_div]

/-- **The quadratic bound — Mahler §13's second case.**

If the truncated sum `∑_{ν<n} max(0, θ − ν/r)` is at most `S`, and there are enough terms
(`θ·r ≤ n`), then

    θ² · r ≤ 2 · S,

i.e. `θ ≤ √(2S/r)`.  Stated squared so that no `Real.sqrt` is needed and everything stays in
`ℚ`.

The cut-off is `K = ⌈θ·r⌉`: it is at most `n` by hypothesis, at least `θ·r` by the ceiling
property, and at most `θ·r + 1` — which is exactly what makes the arithmetic progression's
correction term `K(K−1)/(2r)` at most half of `K·θ`, leaving `K·θ/2 ≥ θ²r/2`.

⚠ This is the shape a linear combination cannot produce, and its absence is what the sixth
correction was detecting. -/
theorem sq_mul_le_two_mul_of_sum_le {θ r S : ℚ} (hr : 0 < r) (hθ : 0 ≤ θ) {n : ℕ}
    (hn : θ * r ≤ (n : ℚ))
    (hS : ∑ ν ∈ range n, max 0 (θ - (ν : ℚ) / r) ≤ S) :
    θ ^ 2 * r ≤ 2 * S := by
  set K : ℕ := ⌈θ * r⌉.toNat with hKdef
  have hcnn : (0 : ℤ) ≤ ⌈θ * r⌉ := Int.ceil_nonneg (by positivity)
  have hKcast : ((K : ℤ) : ℚ) = (⌈θ * r⌉ : ℚ) := by
    rw [hKdef, Int.toNat_of_nonneg hcnn]
  have hKge : θ * r ≤ (K : ℚ) := by
    have h := Int.le_ceil (θ * r)
    rw [show ((K : ℚ)) = ((K : ℤ) : ℚ) by push_cast; ring, hKcast]
    exact h
  have hKlt : (K : ℚ) - 1 ≤ θ * r := by
    have h := Int.ceil_lt_add_one (θ * r)
    rw [show ((K : ℚ)) = ((K : ℤ) : ℚ) by push_cast; ring, hKcast]
    linarith
  have hKn : K ≤ n := by
    have hc : ⌈θ * r⌉ ≤ (n : ℤ) := Int.ceil_le.mpr (by exact_mod_cast hn)
    rw [hKdef]
    omega
  have hbase := sum_max_sub_ge θ r n K hKn
  have hKnn : (0 : ℚ) ≤ (K : ℚ) := Nat.cast_nonneg K
  have hkey : (K : ℚ) * θ - ((K : ℚ) * ((K : ℚ) - 1)) / (2 * r) ≤ S := le_trans hbase hS
  have hdiv : ((K : ℚ) * ((K : ℚ) - 1)) / (2 * r) ≤ (K : ℚ) * θ / 2 := by
    rw [div_le_iff₀ (by positivity : (0 : ℚ) < 2 * r)]
    nlinarith [mul_le_mul_of_nonneg_left hKlt hKnn]
  nlinarith [hkey, hdiv, mul_le_mul_of_nonneg_right hKge hθ]

/-- **Mahler §13, case (1) — the SHARP form.**

When the cut-off falls outside the range (`(n−1)/r ≤ θ`, so every one of the `n` terms is
unclipped), Gauss's sum eats half of them and the conclusion carries a factor `2/n`:

    θ ≤ 2S/n.

⚠ The `2/n` is the entire content.  Dropping it — keeping only the `ν = 0` term, which gives
`θ ≤ S` unconditionally — is true but useless in the application, where `S` is of size `n·Φ`.
`2S/n` is then of size `Φ`, and `S` is of size `n·Φ`; the factor separating them is the matrix
size.  See the ninth correction in `QOU/Mathlib/RothInductionStep.lean`. -/
theorem le_two_mul_div_of_sum_le {θ r S : ℚ} (hr : 0 < r) {n : ℕ} (hn : 0 < n)
    (hge : ((n : ℚ) - 1) / r ≤ θ)
    (hS : ∑ ν ∈ range n, max 0 (θ - (ν : ℚ) / r) ≤ S) :
    θ ≤ 2 * S / (n : ℚ) := by
  have hnQ : (0 : ℚ) < (n : ℚ) := by exact_mod_cast hn
  have hterm : ∀ ν ∈ range n, max 0 (θ - (ν : ℚ) / r) = θ - (ν : ℚ) / r := by
    intro ν hν
    rw [Finset.mem_range] at hν
    refine max_eq_right ?_
    have hvn : ((ν : ℚ)) + 1 ≤ (n : ℚ) := by exact_mod_cast hν
    have h1 : ((ν : ℚ)) / r ≤ ((n : ℚ) - 1) / r :=
      div_le_div_of_nonneg_right (by linarith) hr.le
    linarith
  rw [Finset.sum_congr rfl hterm, Finset.sum_sub_distrib, Finset.sum_const,
    Finset.card_range, nsmul_eq_mul, sum_range_div] at hS
  have hgeR : (n : ℚ) - 1 ≤ θ * r := by rwa [div_le_iff₀ hr] at hge
  have hdiv : (n : ℚ) * ((n : ℚ) - 1) / (2 * r) ≤ (n : ℚ) * θ / 2 := by
    rw [div_le_div_iff₀ (by positivity : (0 : ℚ) < 2 * r) (by norm_num : (0 : ℚ) < 2)]
    nlinarith [mul_le_mul_of_nonneg_left hgeR hnQ.le]
  rw [le_div_iff₀ hnQ]
  linarith

/-- **The sharp form: case 2 kept squared, with no `√2` lost.**

`le_two_mul_max_of_sum_le` below turns case 2's `θ²·r ≤ 2S` into `θ ≤ 2q` via `S ≤ q²·r`, and
that step costs a factor `√2`: what `θ² ≤ 2q²` gives is `θ ≤ √2·q`, not `θ ≤ 2q`.

⚠ **That loss is not in the source.**  §13's display (2) reads
`J(A) ≤ t + √((2/r_m)·J(W)) ≤ t + 2·√(J(W)/n)`, and the `2` on the right is `√4`, arriving
through `2/r_m ≤ 4/n` — never through `√2 ≤ 2`.  This arc's module header had recorded "the
weakening of `√2` to `2`" as *confirmed against the source*; it is the arc's own, and it is
avoidable.

Keeping the disjunction is what makes it avoidable: the two cases are exactly display (2)'s two
branches, and a caller can carry the square through `RothLemmaStatement.radicand_weaken`
instead of taking a root here.  The proof is the same as `le_two_mul_max_of_sum_le`'s, stopping
one step earlier in each branch. -/
theorem sq_le_two_mul_max_of_sum_le {θ r S : ℚ} (hr : 0 < r) (hθ : 0 ≤ θ)
    {n : ℕ} (hn : 0 < n)
    (hS : ∑ ν ∈ range n, max 0 (θ - (ν : ℚ) / r) ≤ S) :
    θ ≤ 2 * S / (n : ℚ) ∨ θ ^ 2 * r ≤ 2 * S := by
  rcases le_or_gt (((n : ℚ) - 1) / r) θ with hge | hlt
  · exact Or.inl (le_two_mul_div_of_sum_le hr hn hge hS)
  · refine Or.inr (sq_mul_le_two_mul_of_sum_le hr hθ ?_ hS)
    rw [lt_div_iff₀ hr] at hlt
    linarith

/-- ⚠ **The sharpening bites.**  At `r = S = 1` the squared branch bounds `θ` by `√2` and the
rounded one by `2q = 2`.  `θ = 3/2` lies between them: the rounded branch admits it, the
squared branch does not.

So `sq_le_two_mul_max_of_sum_le` is strictly stronger than `le_two_mul_max_of_sum_le`'s second
case rather than a restatement of it — which is the whole point, since the factor recovered
here is the one that separates this arc's constant from §14's. -/
theorem sq_branch_strictly_sharper :
    ¬((3 / 2 : ℚ) ^ 2 * 1 ≤ 2 * 1) ∧ (3 / 2 : ℚ) ≤ 2 * 1 := by
  constructor <;> norm_num

/-- **Mahler §13, combined — and it needs no side condition.**

    θ ≤ 2 · max (S/n, q)        for any `q` with `S ≤ q²·r`.

The case split is on whether the cut-off `θ·r` falls inside the range of columns:

* `(n−1)/r ≤ θ` — it does not, every column contributes, and `le_two_mul_div_of_sum_le` gives
  `θ ≤ 2S/n`;
* otherwise `θ·r < n−1 ≤ n`, which is exactly `sq_mul_le_two_mul_of_sum_le`'s hypothesis, and
  that gives `θ² ≤ 2q² ≤ (2q)²`, hence `θ ≤ 2q`.

⚠ Note what is **absent**: no hypothesis relating `S`, `r` and `n`.  The two branches are
complementary by construction, so the combination is unconditional.  An earlier form of this
demanded `S·r ≤ n` in order to force the second branch — see the ninth correction; that
condition is both unnecessary and false in the intended regime. -/
theorem le_two_mul_max_of_sum_le {θ r S q : ℚ} (hr : 0 < r) (hθ : 0 ≤ θ) (hq0 : 0 ≤ q)
    (hq : S ≤ q ^ 2 * r) {n : ℕ} (hn : 0 < n)
    (hS : ∑ ν ∈ range n, max 0 (θ - (ν : ℚ) / r) ≤ S) :
    θ ≤ 2 * max (S / (n : ℚ)) q := by
  have hnQ : (0 : ℚ) < (n : ℚ) := by exact_mod_cast hn
  rcases le_or_gt (((n : ℚ) - 1) / r) θ with hge | hlt
  · have h1 := le_two_mul_div_of_sum_le hr hn hge hS
    have := le_max_left (S / (n : ℚ)) q
    rw [mul_div_assoc] at h1
    linarith
  · have hn' : θ * r ≤ (n : ℚ) := by
      rw [lt_div_iff₀ hr] at hlt
      linarith
    have h2 := sq_mul_le_two_mul_of_sum_le hr hθ hn' hS
    have hsq : θ ^ 2 ≤ (2 * q) ^ 2 := by nlinarith
    have hle : θ ≤ 2 * q := by nlinarith [sq_nonneg (θ - 2 * q)]
    have := le_max_right (S / (n : ℚ)) q
    linarith

/-! ### Non-vacuity

Two guards.  The first shows the `max 0` is load-bearing rather than decorative; the second
shows the hypothesis stack of `sq_mul_le_two_mul_of_sum_le` is satisfiable at a point where
the truncation is active. -/

/-- **The truncation is doing work.**  At `θ = 1`, `r = 1`, `n = 3` the truncated sum is `1`
(terms `1, 0, 0`) while the untruncated sum `∑ (θ − ν/r)` is `0` (terms `1, 0, −1`).

They differ, so no reading of the theorem in which `max 0` is dropped is the same theorem —
and the untruncated version is the *smaller* quantity, which is the wrong direction for a
lower bound on a sum being estimated from above. -/
theorem sum_max_truncation_active :
    (∑ ν ∈ range 3, max 0 ((1 : ℚ) - (ν : ℚ) / 1) = 1) ∧
      (∑ ν ∈ range 3, ((1 : ℚ) - (ν : ℚ) / 1) = 0) := by
  constructor <;> norm_num [Finset.sum_range_succ]

/-- **Satisfiability at that instance.**  With `θ = 1`, `r = 1`, `n = 3`, `S = 1` every
hypothesis holds and the conclusion reads `1 ≤ 2`. -/
theorem sq_mul_le_two_mul_witness : (1 : ℚ) ^ 2 * 1 ≤ 2 * 1 :=
  sq_mul_le_two_mul_of_sum_le (n := 3) one_pos zero_le_one (by norm_num)
    (by norm_num [Finset.sum_range_succ])


/-! ### Next

Wiring this into `RothInductionStep`: the sum `∑_{ν<n} max(0, θ − ν/r)` has to be produced
from `index_det_ge` plus `index_le_index_pderivList_add`, with `θ = index P − t` and `r` the
degree in the split-off variable.  That is the replacement for
`index_le_of_rescaled_factor_bounds`, whose linear shape the sixth correction rejected.

⚠ And the provenance caveat in the header applies: re-derive the constants against a clean
copy of Mahler §13 before relying on them. -/

end RothArith
