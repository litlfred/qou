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

  -- Ref: [leitner2026] mass-theory, prop:binding-genfun-qdifference;
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

/-- **The survivor kernel exists at q = 1 (audit §5) — the classical fibre
    of the re-targeted keystone, proved.** On the Gevrey-normalized (EGF)
    carrier `b n = f n / n!`, the involution recurrence becomes the EXACT
    depth-2 kernel relation
        `(n+2)·b_{n+2} = b_{n+1} + b_n` ,
    i.e. the q-difference keystone's confluent (q → 1) shadow is a
    bona-fide bounded-depth (d = 2) kernel — precisely where the raw-OGF
    obstruction above vanishes. This salvages the depth-2 recurrence
    instinct of the reverted #4129 wiring on its correct carrier: the open
    content that remains is the q-LIFT (a `[n+2]_q`-type relation on the
    q-Borel transform) and the identification of its kernel with the
    SW prolongation symbol — stated as `conj:qdifference-kernel-
    prolongation-symbol`, which stays a conjecture. -/
theorem normalized_classical_kernel_exists (f : ℕ → ℕ)
    (hrec : ∀ n, f (n + 2) = f (n + 1) + (n + 1) * f n) (n : ℕ) :
    ((n : ℚ) + 2) * ((f (n + 2) : ℚ) / (n + 2).factorial)
      = (f (n + 1) : ℚ) / (n + 1).factorial + (f n : ℚ) / n.factorial := by
  have hfac2 : ((n + 2).factorial : ℚ)
      = ((n : ℚ) + 2) * ((n + 1).factorial : ℚ) := by
    rw [Nat.factorial_succ (n + 1)]; push_cast; ring
  have hfac1 : ((n + 1).factorial : ℚ)
      = ((n : ℚ) + 1) * (n.factorial : ℚ) := by
    rw [Nat.factorial_succ n]; push_cast; ring
  have hne0 : (n.factorial : ℚ) ≠ 0 := by
    exact_mod_cast Nat.factorial_ne_zero n
  have hne1 : ((n + 1).factorial : ℚ) ≠ 0 := by
    exact_mod_cast Nat.factorial_ne_zero (n + 1)
  have hne2 : ((n + 2).factorial : ℚ) ≠ 0 := by
    exact_mod_cast Nat.factorial_ne_zero (n + 2)
  have hcast : (f (n + 2) : ℚ) = (f (n + 1) : ℚ) + ((n : ℚ) + 1) * (f n : ℚ) := by
    rw [hrec n]; push_cast; ring
  rw [← mul_div_assoc, div_add_div _ _ hne1 hne0,
    div_eq_div_iff hne2 (mul_ne_zero hne1 hne0), hcast, hfac2, hfac1]
  ring

/-- q-integer `[k]_q = Σ_{i<k} qⁱ` (polynomial form — no division, generic). -/
def qint {K : Type*} [Field K] (q : K) (k : ℕ) : K := ∑ i ∈ range k, q ^ i

/-- q-factorial `[k]_q! = ∏ [j]_q`. -/
def qfact {K : Type*} [Field K] (q : K) : ℕ → K
  | 0 => 1
  | k + 1 => qint q (k + 1) * qfact q k

/-- **The q-lift exists (probe `qlift_kernel_candidate_crosscheck` → proved).**
    Over any field with nonvanishing q-integers, any sequence satisfying the
    q-involution recurrence `f(n+2) = f(n+1) + [n+1]_q·f(n)` has, on the
    q-factorial-normalized carrier `b_n = f_n/[n]_q!`, the EXACT depth-2
    q-difference kernel `[n+2]_q·b_{n+2} = b_{n+1} + b_n` — the q-lift of
    `normalized_classical_kernel_exists` with `c(q) = 1`, no free constant.
    At `q = 1` (`qint 1 k = k`) this specializes to the classical fibre.
    The identification of THIS kernel with the GGM eq-49 / prolongation-
    symbol carrier remains open (`conj:qdifference-kernel-prolongation-
    symbol`); the diagonal-gauge comparison is the sibling probe's scope. -/
theorem qlift_normalized_kernel_exists {K : Type*} [Field K] (q : K)
    (f : ℕ → K) (hq : ∀ k, 1 ≤ k → qint q k ≠ 0)
    (hrec : ∀ n, f (n + 2) = f (n + 1) + qint q (n + 1) * f n) (n : ℕ) :
    qint q (n + 2) * (f (n + 2) / qfact q (n + 2))
      = f (n + 1) / qfact q (n + 1) + f n / qfact q n := by
  have hfz : ∀ m, qfact q m ≠ 0 := by
    intro m
    induction m with
    | zero => simp [qfact]
    | succ k ih =>
        exact mul_ne_zero (hq (k + 1) (Nat.succ_le_succ (Nat.zero_le k))) ih
  have hf2 : qfact q (n + 2) = qint q (n + 2) * qfact q (n + 1) := rfl
  have hf1 : qfact q (n + 1) = qint q (n + 1) * qfact q n := rfl
  rw [← mul_div_assoc, div_add_div _ _ (hfz (n + 1)) (hfz n),
    div_eq_div_iff (hfz (n + 2)) (mul_ne_zero (hfz (n + 1)) (hfz n)),
    hrec n, hf2, hf1]
  ring

/-! ### Keystone bridge: the binding period is the C1 carrier, factorial-stripped

    The binding period is `p_n = a_D^{(n)} = f_n / n` (`f` = involution numbers,
    `sw-classical-jet-exactness`). The C1 carrier proved above is
    `b_n = f_n / n!` (the involution EGF coefficient, `e^{x+x²/2}`). Since
    `n! = n·(n−1)!`, they differ by exactly the Gevrey (factorial) strip
    `b_n = p_n / (n−1)!`. Composed with `normalized_classical_kernel_exists`,
    this says the `(n−1)!`-stripped binding period satisfies the proved depth-2
    kernel — the classical NORMALIZATION leg of
    `conj:qdifference-kernel-prolongation-symbol`.

    HONEST RESIDUAL (still conjectural, NOT proved here): that this carrier is
    THE Seiberg–Witten prolongation symbol (the geometric identification). The
    bridge below discharges only the *normalization* leg (period ↔ carrier). -/

/-- **Binding period ↔ C1 carrier (the Gevrey strip).** `f_{m+1}/(m+1) =
    (f_{m+1}/(m+1)!)·m!` — the binding period at index `m+1` equals the C1
    carrier times `m! = (n−1)!`. Over ℚ (a generic field can have
    `(m+1) = 0`); indexed by `m+1` to avoid `ℕ`-subtraction. -/
theorem binding_period_is_carrier_stripped (f : ℕ → ℕ) (m : ℕ) :
    (f (m + 1) : ℚ) / (m + 1)
      = ((f (m + 1) : ℚ) / ((m + 1).factorial)) * (m.factorial : ℚ) := by
  have hm : (m.factorial : ℚ) ≠ 0 := by exact_mod_cast m.factorial_ne_zero
  have hm1 : ((m : ℚ) + 1) ≠ 0 := by positivity
  rw [Nat.factorial_succ]
  push_cast
  field_simp

/-- **The stripped binding period satisfies the C1 kernel.** For the binding
    period `p_n = f_n/n` (any `f` with the involution recurrence), its
    `(n−1)!`-strip `b_n = p_n/(n−1)! = f_n/n!` satisfies the proved depth-2
    kernel `(n+2)·b_{n+2} = b_{n+1} + b_n`. This is the classical keystone
    normalization leg: C1 governs the binding series up to the explicit Gevrey
    normalization (the geometric prolongation-symbol identification remains
    conjectural). -/
theorem binding_carrier_satisfies_kernel (f : ℕ → ℕ)
    (hrec : ∀ n, f (n + 2) = f (n + 1) + (n + 1) * f n) (n : ℕ) :
    ((n : ℚ) + 2) * ((f (n + 2) : ℚ) / ((n + 2).factorial))
      = (f (n + 1) : ℚ) / ((n + 1).factorial) + (f n : ℚ) / (n.factorial) :=
  normalized_classical_kernel_exists f hrec n

/-- Vanishing residual form of the depth-2 recurrence on factorial-normalized terms. -/
theorem normalized_classical_kernel_sub_eq_zero (f : ℕ → ℕ)
    (hrec : ∀ n, f (n + 2) = f (n + 1) + (n + 1) * f n) (n : ℕ) :
    ((n : ℚ) + 2) * ((f (n + 2) : ℚ) / (n + 2).factorial)
      - ((f (n + 1) : ℚ) / (n + 1).factorial + (f n : ℚ) / n.factorial) = 0 := by
  rw [normalized_classical_kernel_exists f hrec n, sub_self]

end QOU.Mass.QDifferenceConfluentObstruction
