/-
  The confluent-limit obstruction to a bounded-depth q-difference kernel on
  the raw binding coefficients.

  Formalizes docs/audits/2026-07-20-qdifference-kernel-confluent-narrowing.md
  §§3–4: for the conditional q-difference form of
  `prop:binding-genfun-qdifference`
      G(qx;q) = R(q,x)·G(x;q),   R ∈ Q(q)[x,x⁻¹] bounded depth,
  the first-order-in-(q−1) coefficient relation is
      n·Bₙ = Σⱼ sⱼ·B_{n−j}      (∗∗)
  (the ∂_q Bₙ terms cancel identically — `first_order_cancellation`), and
  (∗∗) is unsatisfiable when the classical coefficients grow super-
  geometrically: for eventually-positive, eventually-monotone `B` it forces
  `n ≤ Σⱼ |sⱼ|` for every large `n`, which is absurd
  `no_bounded_depth_first_order_kernel`). The corpus instantiation is
  `B n = I(n)/n` (involution numbers, `QOU.Mass.BindingGevreyHalf`); the
  doubling lemma feeding its eventual monotonicity is proved here
  ABSTRACTLY over any sequence satisfying the involution recurrence
  (`doubling_of_involution_recurrence`), so this file needs no package
  import.

  HONEST SCOPE. This excludes one carrier normalization — a bounded-depth
  Laurent kernel acting on the ORDINARY generating function of the raw
  coefficients. It does not touch the prolongation-symbol identification
  itself, which is re-targeted at the Gevrey-normalized (q-Borel) transform
  (audit §5) where the obstruction vanishes. The `(∗∗)` hypothesis is taken
  as the first-order data of the kernel relation (derivation in audit §3);
  the zeroth-order rigidity R(1,x) = 1 (audit §2) enters through the
  `s`-free left side.

  `first_order_cancellation` is generic-`R` (§7c); the exclusion lemma is
  wall-side (ℝ — uses ordering and the archimedean property).

  -- Ref: [manuscript] mass-theory, prop:binding-genfun-qdifference;
  --      docs/audits/2026-07-20-qdifference-kernel-confluent-narrowing.md
-/

import Mathlib.Tactic

namespace QOU.Mass.QDifferenceConfluentObstruction

open Finset

/-- **First-order cancellation (audit §3).** Expanding
    `qⁿ·Bₙ(q) = Σⱼ rⱼ(q)·B_{n−j}(q)` to first order at `q = 1` with the
    zeroth order rigid (`rⱼ(1) = δⱼ₀`), the `∂_q Bₙ` contributions appear
    identically on both sides and cancel: writing `B` for the classical
    values, `B'` for the q-derivatives at 1, and `s j` for `∂_q rⱼ|₁`, the
    first-order relation `n·Bₙ + Bₙ' = Bₙ' + Σⱼ sⱼ·B_{n−j}` collapses to a
    constraint on CLASSICAL data only. Generic commutative ring. -/
theorem first_order_cancellation {R : Type*} [CommRing R] {d : ℕ}
    (B B' : ℕ → R) (s : ℕ → R) (n : ℕ)
    (h : (n : R) * B n + B' n
        = B' n + ∑ j ∈ range (d + 1), s j * B (n - j)) :
    (n : R) * B n = ∑ j ∈ range (d + 1), s j * B (n - j) := by
  have h2 : B' n + (n : R) * B n
      = B' n + ∑ j ∈ range (d + 1), s j * B (n - j) := by
    rw [add_comm (B' n)]; exact h
  exact add_left_cancel h2

/-- **The exclusion (audit §4).** The pinned first-order relation
    `n·Bₙ = Σ_{j≤d} sⱼ·B_{n−j}` cannot hold for all large `n` when `B` is
    eventually positive and eventually monotone: bounding every `B_{n−j}`
    by `Bₙ` gives `n ≤ Σⱼ |sⱼ|` for every `n ≥ N + d`, contradicting the
    archimedean property. No limits are needed — the absurdity is a single
    integer exceeding a fixed real bound. -/
theorem no_bounded_depth_first_order_kernel {d N : ℕ}
    (B : ℕ → ℝ) (s : ℕ → ℝ)
    (hpos : ∀ n, N ≤ n → 0 < B n)
    (hmono : ∀ m n, N ≤ m → m ≤ n → B m ≤ B n)
    (hrec : ∀ n, N + d ≤ n →
      (n : ℝ) * B n = ∑ j ∈ range (d + 1), s j * B (n - j)) :
    False := by
  -- the uniform bound: for every n ≥ N + d, n ≤ Σⱼ |sⱼ|
  have key : ∀ n : ℕ, N + d ≤ n → (n : ℝ) ≤ ∑ j ∈ range (d + 1), |s j| := by
    intro n hn
    have hBn : 0 < B n := hpos n (le_trans (Nat.le_add_right N d) hn)
    have hbound : (n : ℝ) * B n ≤ (∑ j ∈ range (d + 1), |s j|) * B n := by
      rw [hrec n hn, Finset.sum_mul]
      refine Finset.sum_le_sum ?_
      intro j hj
      have hjd : j ≤ d := Nat.lt_succ_iff.mp (Finset.mem_range.mp hj)
      have hNle : N ≤ n - j := by omega
      have hstep : B (n - j) ≤ B n := hmono (n - j) n hNle (Nat.sub_le n j)
      have hBnj : 0 < B (n - j) := hpos (n - j) hNle
      calc s j * B (n - j) ≤ |s j| * B (n - j) := by
            exact mul_le_mul_of_nonneg_right (le_abs_self (s j)) hBnj.le
        _ ≤ |s j| * B n :=
            mul_le_mul_of_nonneg_left hstep (abs_nonneg (s j))
    exact le_of_mul_le_mul_right hbound hBn
  -- archimedean absurdity: pick an integer above the bound
  obtain ⟨m, hm⟩ := exists_nat_gt (∑ j ∈ range (d + 1), |s j|)
  have hm' : ((max m (N + d) : ℕ) : ℝ) ≤ ∑ j ∈ range (d + 1), |s j| :=
    key _ (le_max_right m (N + d))
  have hcast : (m : ℝ) ≤ ((max m (N + d) : ℕ) : ℝ) := by
    exact_mod_cast Nat.le_max_left m (N + d)
  linarith

/-- **Doubling from the involution recurrence (abstract).** Any sequence
    satisfying `f(n+2) = f(n+1) + (n+1)·f(n)` with `f 0 ≤ f 1` doubles from
    the second step on: `2·f(n+1) ≤ f(n+2)` for `n ≥ 1`. Instantiating
    `f = involutionNumber` (which satisfies the recurrence by `rfl`) feeds
    the eventual monotonicity of `B n = I(n)/n` used by the exclusion. -/
theorem doubling_of_involution_recurrence (f : ℕ → ℕ)
    (hrec : ∀ n, f (n + 2) = f (n + 1) + (n + 1) * f n)
    (h01 : f 0 ≤ f 1) (n : ℕ) (hn : 1 ≤ n) :
    2 * f (n + 1) ≤ f (n + 2) := by
  obtain ⟨k, rfl⟩ : ∃ k, n = k + 1 := ⟨n - 1, by omega⟩
  show 2 * f (k + 2) ≤ f (k + 3)
  have hmono : ∀ m, f m ≤ f (m + 1) := by
    intro m
    cases m with
    | zero => exact h01
    | succ l => rw [hrec l]; exact Nat.le_add_right _ _
  have hkey : f (k + 2) ≤ (k + 2) * f (k + 1) := by
    have h1 : (k + 1) * f k ≤ (k + 1) * f (k + 1) :=
      Nat.mul_le_mul_left _ (hmono k)
    have h2 := hrec k
    nlinarith [h2, h1]
  -- restate hrec (k+1) with normalized indices so omega shares the
  -- product atom (k+2)·f(k+1) with hkey (definitional equality)
  have h3 : f (k + 3) = f (k + 2) + (k + 2) * f (k + 1) := hrec (k + 1)
  -- f(k+3) = f(k+2) + (k+2)·f(k+1) ≥ f(k+2) + f(k+2)
  omega

end QOU.Mass.QDifferenceConfluentObstruction
