import QOU.MathlibExt.QIntegerCanonical

/-!
# QOU.Archimedean.rj_canonical_inner_product — Rosso–Jones inner product, convention D

**Proposition** ([`prop:rj-canonical-inner-product`](../../../predicted-spectra/rj-canonical-inner-product.md)).

Hecke relation `(σ − q)(σ + q⁻¹) = 0`, `[n] = (qⁿ − q⁻ⁿ)/(q − q⁻¹)` (`qIntBal`),
Markov parameter `z = q³/(q² + 1) = q²/[2]` (convention D).

## What this file proves (sorry-free, over a generic field `R`)

* `markovZD_eq` — the block's `z = q²/[2]` is `z_D = q³/(q²+1)`.
* `hookContent_row` — the hook-content product of the one-row shape `(r)`:
  `∏_{i<r} [2+i] = [r+1] · ∏_{i<r} [r−i]`, i.e. `d_(r) = [r+1]` (denominators
  cleared, so no non-vanishing hypothesis is needed).
* `hookContent_hook` — the same for the two-row hook `(m,1)`: `d_(m,1) = [m]`.
  These are the two hook dimensions that survive in part (iii).
* `h2Trace_rossoJones` — part (iii) at `r = 2`, for **every** `s`, computed in
  `H₂(q)` itself (basis `{1, σ}`, `σ² = (q − q⁻¹)σ + 1`) with the Markov trace
  `tr(1) = 1`, `tr(σ) = z_D`:
  `[2]² · tr_M(σˢ) = [3] qˢ + (−q⁻¹)ˢ`.
  For odd `s` (the torus knots `τ(2,s)`) this is the block's
  `[r+1] q^{s(r−1)} − [r−1] q^{s(r−3)}` at `r = 2` (`h2Trace_rossoJones_odd`).
* `old_form_ii_false_r2` — the formerly carried field `claim_unique_up_to_scalar`
  ("every diagonal form normalised at the trivial class is a scalar multiple of
  `d_λ`") is **false** already at `r = 2`.

## What it does NOT prove — stated here so the gap stays visible

* Part (iii) for general `r` (the hook/Adams-sign Rosso–Jones formula) is
  **not** formalised. It is cited (`[rosso-jones1993]`) and re-verified in exact
  arithmetic over `ℚ(q)` for every coprime `(r,s)` tested at `r = 2, 3, 4` by
  `computations/probes/rj_inner_product_conventionD_torus_probe.py`. It is
  deliberately **not** encoded as a class field: a class whose torus-trace datum
  is unconstrained data is inhabited by defining that datum to be the right-hand
  side, which is the self-assuming pattern AGENTS.md §1a forbids. Formalising it
  honestly needs the Markov trace on `H_r(q)` for general `r`
  (`QOU.IwahoriHecke.MarkovTrace`), which is open infrastructure.
* Part (ii)'s positive content — the form is `[2]^r tr_M(p_λ p_μ)` and is fixed
  because the Markov trace with `tr_M(1) = 1` is unique for given `z` — rests on
  Markov uniqueness, not formalised here for general `r`.

## History

Until 2026-10-10 this file carried a self-assuming `HeckeRepRingContext` class
whose fields `claim_unique_up_to_scalar` (false, see `old_form_ii_false_r2`) and
`jonesPoly_eq_eval` (the convention-C sum `Σ_{λ⊢r} d_λ q^{c_λ s}`, which agrees
with the trace only for `r = 2`, `s` even) were projected out as "theorems".
Both are removed; bean `qou-q425`.

-- Ref: [rosso-jones1993] Rosso–Jones, *J. Knot Theory Ramifications* 2 (1993)
-/

namespace QOU.Archimedean

open QOU.QInteger Finset

variable {R : Type*} [Field R]

/-! ### Small quantum integers -/

theorem qIntBal_one (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) : qIntBal q 1 = 1 := by
  have h : q - q⁻¹ ≠ 0 := by
    intro h; apply hq2; field_simp at h; linear_combination h
  simp [qIntBal_def, h]

theorem qIntBal_two (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) :
    qIntBal q 2 = q + q⁻¹ := by
  have h : q - q⁻¹ ≠ 0 := by
    intro h; apply hq2; field_simp at h; linear_combination h
  rw [qIntBal_def, div_eq_iff h]; ring

theorem qIntBal_three (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) :
    qIntBal q 3 = q ^ 2 + 1 + q⁻¹ ^ 2 := by
  have h : q - q⁻¹ ≠ 0 := by
    intro h; apply hq2; field_simp at h; linear_combination h
  rw [qIntBal_def, div_eq_iff h]; field_simp; ring

/-! ### The Markov parameter -/

/-- Convention-D Markov parameter `z_D = q³/(q²+1)`. -/
noncomputable def markovZD (q : R) : R := q ^ 3 / (q ^ 2 + 1)

/-- The block's `z = q²/[2]` is `z_D`. -/
theorem markovZD_eq (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (hq1 : q ^ 2 + 1 ≠ 0) :
    markovZD q = q ^ 2 / qIntBal q 2 := by
  rw [qIntBal_two q hq hq2, markovZD]
  have : q + q⁻¹ ≠ 0 := by
    intro h; apply hq1; field_simp at h; linear_combination h
  field_simp

/-! ### Hook-content dimensions `d_λ = ∏ [2 + c(□)] / [h(□)]` of the surviving hooks -/

/-- Telescoping core: `∏_{i<r} [i+2] = [r+1] · ∏_{i<r} [i+1]`. -/
theorem prod_shift (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (r : ℕ) :
    ∏ i ∈ range r, qIntBal q (i + 2) = qIntBal q (r + 1) * ∏ i ∈ range r, qIntBal q (i + 1) := by
  induction r with
  | zero => rw [range_zero, prod_empty, prod_empty, mul_one, zero_add, qIntBal_one q hq hq2]
  | succ n ih =>
    rw [prod_range_succ, prod_range_succ, ih]
    ring

/-- **One-row shape `(r)`**: contents `0,…,r−1`, hooks `r,…,1`. The hook-content
product, denominators cleared, gives `d_(r) = [r+1]`. -/
theorem hookContent_row (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (r : ℕ) :
    ∏ i ∈ range r, qIntBal q (2 + i) = qIntBal q (r + 1) * ∏ i ∈ range r, qIntBal q (r - i) := by
  have hrefl : ∏ i ∈ range r, qIntBal q (r - i) = ∏ i ∈ range r, qIntBal q (i + 1) := by
    rw [← prod_range_reflect]
    refine prod_congr rfl fun i hi => ?_
    have := mem_range.mp hi
    congr 1; omega
  rw [hrefl]
  simp_rw [add_comm 2]
  exact prod_shift q hq hq2 r

/-- **Two-row hook `(m,1)`, `m ≥ 1`** (so `r = m+1`): first-row cells have
contents `0,…,m−1` and hooks `m+1` (corner) then `m−1,…,1`; the second-row cell
has content `−1` and hook `1`. Denominators cleared, `d_(m,1) = [m]`. -/
theorem hookContent_hook (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (m : ℕ) (hm : 1 ≤ m) :
    qIntBal q 1 * ∏ j ∈ range m, qIntBal q (2 + j)
      = qIntBal q m *
        (qIntBal q (m + 1) * qIntBal q 1 * ∏ j ∈ range (m - 1), qIntBal q (m - 1 - j)) := by
  obtain ⟨k, rfl⟩ : ∃ k, m = k + 1 := ⟨m - 1, by omega⟩
  have hrow := hookContent_row q hq hq2 (k + 1)
  have hrefl : ∏ j ∈ range k, qIntBal q (k - j) = ∏ i ∈ range k, qIntBal q (i + 1) := by
    rw [← prod_range_reflect]
    refine prod_congr rfl fun i hi => ?_
    have := mem_range.mp hi
    congr 1; omega
  have hrefl' : ∏ i ∈ range (k + 1), qIntBal q (k + 1 - i)
      = ∏ i ∈ range (k + 1), qIntBal q (i + 1) := by
    rw [← prod_range_reflect]
    refine prod_congr rfl fun i hi => ?_
    have := mem_range.mp hi
    congr 1; omega
  simp only [Nat.add_sub_cancel] at *
  rw [hrow, hrefl', hrefl, prod_range_succ]
  ring

/-! ### Part (iii) at `r = 2`, computed in `H₂(q)` -/

/-- Coordinates `(a, b)` of `σˢ = a + bσ` in `H₂(q)`, basis `{1, σ}`.
Multiplying `a + bσ` by `σ` and using `σ² = (q − q⁻¹)σ + 1` gives
`b + (a + (q − q⁻¹) b) σ`. -/
noncomputable def h2Pow (q : R) : ℕ → R × R
  | 0 => (1, 0)
  | s + 1 => ((h2Pow q s).2, (h2Pow q s).1 + (q - q⁻¹) * (h2Pow q s).2)

/-- The Markov trace on `H₂(q)`: `tr(1) = 1`, `tr(σ) = z_D`. -/
noncomputable def h2Trace (q : R) (s : ℕ) : R := (h2Pow q s).1 + (h2Pow q s).2 * markovZD q

/-- `σ` acts on its two eigenlines by `q` and `−q⁻¹`. -/
theorem h2Pow_eigen (q : R) (hq : q ≠ 0) (s : ℕ) :
    (h2Pow q s).1 + (h2Pow q s).2 * q = q ^ s ∧
      (h2Pow q s).1 + (h2Pow q s).2 * (-q⁻¹) = (-q⁻¹) ^ s := by
  induction s with
  | zero => simp [h2Pow]
  | succ n ih =>
    obtain ⟨h1, h2⟩ := ih
    simp only [h2Pow]
    constructor
    · rw [pow_succ, ← h1]; field_simp; ring
    · rw [pow_succ, ← h2]; field_simp; ring

/-- **Rosso–Jones at `r = 2`, every `s`**: `[2]² · tr_M(σˢ) = [3] qˢ + (−q⁻¹)ˢ`.
The weights are `d_(2)/[2]² = [3]/[2]²` and `d_(1,1)/[2]² = [1]/[2]²`. -/
theorem h2Trace_rossoJones (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (hq1 : q ^ 2 + 1 ≠ 0)
    (s : ℕ) :
    qIntBal q 2 ^ 2 * h2Trace q s = qIntBal q 3 * q ^ s + (-q⁻¹) ^ s := by
  obtain ⟨h1, h2⟩ := h2Pow_eigen q hq s
  rw [← h1, ← h2, qIntBal_two q hq hq2, qIntBal_three q hq hq2, h2Trace, markovZD]
  field_simp
  ring

/-- **Torus knots `τ(2, s)`, `s` odd**: the block's formula
`[r+1] q^{s(r−1)} − [r−1] q^{s(r−3)}` at `r = 2`. -/
theorem h2Trace_rossoJones_odd (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1)
    (hq1 : q ^ 2 + 1 ≠ 0) (s : ℕ) (hs : Odd s) :
    qIntBal q 2 ^ 2 * h2Trace q s = qIntBal q 3 * q ^ s - qIntBal q 1 * q⁻¹ ^ s := by
  rw [h2Trace_rossoJones q hq hq2 hq1, qIntBal_one q hq hq2, neg_pow, hs.neg_one_pow]
  ring

/-! ### The old part (ii) is false -/

/-- The field formerly carried as `claim_unique_up_to_scalar` — every diagonal
form normalised at the trivial class is a scalar multiple of `d_λ` — fails at
`r = 2` (classes `(2) ↦ 0`, `(1,1) ↦ 1`, `d = ([3], [1])`): the diagonal form
`diag(1, 0)` is not a multiple of it. A diagonal form has one free entry per
two-row class; only the Markov trace (unique for given `z`) fixes the form. -/
theorem old_form_ii_false_r2 (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) :
    ¬ ∀ φ : Fin 2 → Fin 2 → R, (∀ i j, i ≠ j → φ i j = 0) → φ 0 0 = 1 →
        ∃ c : R, ∀ i, φ i i = c * ![qIntBal q 3, qIntBal q 1] i := by
  intro h
  obtain ⟨c, hc⟩ := h (fun i j => if i = 0 ∧ j = 0 then 1 else 0)
    (fun i j hij => by simp only [ite_eq_right_iff, and_imp]; intro hi hj; exact absurd (hi.trans hj.symm) hij)
    (by simp)
  have h1 : (0 : R) = c * 1 := by
    have := hc 1
    rw [qIntBal_one q hq hq2] at this
    simpa using this
  have h0 : (1 : R) = c * qIntBal q 3 := by
    have := hc 0
    simpa using this
  rw [mul_one] at h1
  rw [← h1, zero_mul] at h0
  exact one_ne_zero h0

/-- **Top-level bundle** for `prop:rj-canonical-inner-product`, the part that is
formalised: the Markov parameter is `z_D`, the surviving hook dimensions are
`[r+1]` and `[r−1]`, and part (iii) holds at `r = 2` for every `s`. -/
theorem rj_canonical_inner_product (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1)
    (hq1 : q ^ 2 + 1 ≠ 0) :
    markovZD q = q ^ 2 / qIntBal q 2 ∧
    (∀ r : ℕ, ∏ i ∈ range r, qIntBal q (2 + i)
        = qIntBal q (r + 1) * ∏ i ∈ range r, qIntBal q (r - i)) ∧
    (∀ s : ℕ, qIntBal q 2 ^ 2 * h2Trace q s = qIntBal q 3 * q ^ s + (-q⁻¹) ^ s) :=
  ⟨markovZD_eq q hq hq2 hq1, hookContent_row q hq hq2, h2Trace_rossoJones q hq hq2 hq1⟩

end QOU.Archimedean
