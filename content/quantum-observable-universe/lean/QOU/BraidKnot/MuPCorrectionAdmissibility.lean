/-
Copyright (c) 2026 litlfred. All rights reserved.

# μ–p residual on the muon carrier: the bar-even small-height monomial class is empty

Bean `qou-6gf9` (consolidation of the GAP-A-4 muon-correction prunes).
Companion audits:
`docs/audits/2026-08-08-mu-p-residual-carrier-order-and-bar-parity-prune.md`,
`docs/audits/2026-08-01-mu-p-tension-attack-recon-floor-verdict.md`.
Probe: `docs/audits/scripts/mu_p_carrier_order_window_probe.py`.
Prune halves consolidated here:
`QOU/BraidKnot/MuPCarrierBarParity.lean` (generic bar-parity algebra) and
`QOU/BraidKnot/MuPCarrierOrderWindow.lean` (archimedean order window).

## Context

The muon carrier `m_μ/m_e = Vol(4₁)/ℏ_q²` overshoots CODATA at the experimental
(proton) pin `q₀ = 1.10997858275138` by `+209.755 ppb = 9.534 σ`, so a first
correction to the carrier would have to supply a multiplicative factor `1 − t`
with `t = 2.09754920524e-7` (`ℏ_{q₀} = 0.09908171604`). The corpus's standing
precondition on that correction is that it be **bar-even** (fixed by
`q ↦ q⁻¹`), argued from the amphichirality of `4₁`.

The two prune files each prove one *half* of an exclusion:

* `MuPCarrierBarParity` — the bar-even part of the `ℏ_q`-monomial family
  `ℏ_q^k · q^m` is the `w`-tower, `w := q·ℏ_q² = q + q⁻¹ − 2`
  (**positive half only**: `k = 2m` ⇒ bar-even; the converse is shown there
  only on the single witness `(k, m) = (6, 1)`).
* `MuPCarrierOrderWindow` — a small-height monomial `|c|·ℏ_q^k` carrying the
  residual has `k ∈ {6, 7}` (`order_window`) — an `ℏ_q`-tower statement, which
  says nothing about the `w`-tower on its own.

The probe then *measured* that the `w`-tower admits no order with a
small-height coefficient (`t/w³ = 0.16211 < 1/5`, `t/w⁴ = 14.877 > 5`), but
that measurement was never proved.

## What this file proves

1. `bar_even_monomial_iff` — **the converse half of the selection rule**, over
   `ℝ` with `1 < q`: `ℏ_q^k · q^m` is bar-even *iff* `k = 2m`. (The forward
   direction is `hbarGen_monomial_bar_even`; the new content is that nothing
   else in the family is bar-even.)
2. `wGen_lower_bound`, `wGen_upper_bound` — on the pin window
   `q ∈ [1.1099, 1.11]` (which contains `q₀`), `w ∈ [0.0108, 0.011]`, in exact
   rationals (the probe measures `w(q₀) = 0.010897`).
3. `no_small_height_w_monomial` — **the Lean form of the measured
   "`w`-tower admits no order with a small-height coefficient"**: for every
   `j`, `|c|·w^j` with `|c| ∈ [1/5, 5]` misses the residual window
   `t ∈ [1.8e-7, 2.4e-7]`. Orders `j ≤ 3` give at least
   `(1/5)·0.0108³ ≈ 2.52e-7`; orders `j ≥ 4` give at most
   `5·0.011⁴ ≈ 7.3e-8`.
4. `no_bar_even_small_height_monomial` — **capstone**: no bar-even monomial
   `|c|·ℏ_q^k·q^m` with a small-height coefficient carries the residual at any
   pin in the window. Proof: (1) forces `k = 2m`, the positive half turns the
   monomial into `w^m`, and (3) excludes every `m`.
5. `no_bar_even_small_height_monomial_hbarQ` — the capstone restated against
   the production substrate `hbarQ` through the bridge
   `MuPCarrierOrderWindow.hbarGen_eq_hbarQ`.
6. `GapA4CorrectionAdmissible` + `monomial_not_admissible` — the admissibility
   class as a content-bearing `structure … : Prop` (pin in the window, bar-even
   as a function, residual carried at the pin), and the statement that no
   member of the monomial family `q ↦ c·ℏ_q^k·q^m`, `|c| ∈ [1/5, 5]`, belongs
   to it.

## Scope of the negative

**(b)**, structural, relative to a stated class: {single monomial in
`(ℏ_q, q)`, bar-even, coefficient of height `|c| ∈ [1/5, 5]`} as a carrier of
the μ–p residual at any pin in `[1.1099, 1.11]`. The two named invariants are
**bar parity under `q ↦ q⁻¹`** (`hbarGen_bar`: `ℏ_{q⁻¹} = −q·ℏ_q`, so
bar-evenness forces `k = 2m`) and **exact interval arithmetic** on the pin
window (the `w`-bounds and the two `norm_num` inequalities). Nothing outside
the class is excluded: a sum of monomials, a coefficient outside `[1/5, 5]`, a
non-monomial function of `q`, or an operator-valued correction are all
untouched — and the `[1/2, 2]` sub-class the order-window file deliberately
leaves unformalised is not revisited here.

## What this file does NOT do

It **constructs nothing**. No correction is derived, no candidate is proposed,
and nothing is wired. It does not touch the s5-so3 / `Σ(2,3,5)` WRT route
(deflationary terminus 2026-06-22, bean `s5bb`: WRT data and `W_λ` are
Schur–Weyl dual, not equal) nor the Beasley–Witten `S³/2I` localization wall
(bean `qou-2v7k`, carried as a class with no instance). The bar-even
precondition itself is *argued* in the corpus, not proved; the exclusion is
conditional on it exactly as the two prune files are
(AGENTS.md §"Conditional-proved ≠ premise-established"). `GapA4CorrectionAdmissible`
encodes that precondition as a hypothesis on the class, not as a theorem.

AGENTS.md §7c: `ℝ` is genuinely required throughout — the results are about
ordering (`1 < q`, the windows), absolute values, and magnitudes at the pin.
-/
import Mathlib.Tactic
import Mathlib.Data.Real.Basic
import QOU.BraidKnot.MuPCarrierBarParity
import QOU.BraidKnot.MuPCarrierOrderWindow

namespace QOU.BraidKnot.MuPCorrectionAdmissibility

open QOU.BraidKnot.MuPCarrier
open QOU.BraidKnot.MuPCarrierOrderWindow

/-! ## 1. Bar-even monomials are exactly the `w`-tower (converse half) -/

/-- On `1 < q` the substrate is positive: `ℏ_q = 1 − q⁻¹ > 0`. -/
theorem hbarGen_pos (q : ℝ) (hq : 1 < q) : (0 : ℝ) < hbarGen q := by
  have : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
  unfold hbarGen
  linarith

/-- **Selection rule, both halves.** Over `ℝ` with `1 < q`, the monomial
`ℏ_q^k · q^m` is bar-even — `ℏ_{q⁻¹}^k · (q⁻¹)^m = ℏ_q^k · q^m` — **iff**
`k = 2m`.

Forward direction: `hbarGen_bar` turns the left side into
`(−q)^k · ℏ_q^k · (q⁻¹)^m`; cancelling `ℏ_q^k ≠ 0` and clearing `(q⁻¹)^m`
leaves `(−q)^k = q^{2m}`; taking absolute values gives `q^k = q^{2m}`, and
`n ↦ q^n` is injective for `q > 1`. Converse: `hbarGen_monomial_bar_even`. -/
theorem bar_even_monomial_iff (q : ℝ) (hq : 1 < q) (k m : ℕ) :
    hbarGen q⁻¹ ^ k * (q⁻¹) ^ m = hbarGen q ^ k * q ^ m ↔ k = 2 * m := by
  have hpos : (0 : ℝ) < q := by linarith
  have hq0 : q ≠ 0 := hpos.ne'
  have hh : (0 : ℝ) < hbarGen q := hbarGen_pos q hq
  constructor
  · intro h
    rw [hbarGen_bar q hq0, mul_pow] at h
    -- `h : (-q) ^ k * hbarGen q ^ k * q⁻¹ ^ m = hbarGen q ^ k * q ^ m`
    have h2 : (-q) ^ k * q⁻¹ ^ m * hbarGen q ^ k = q ^ m * hbarGen q ^ k := by
      linear_combination h
    have h3 : (-q) ^ k * q⁻¹ ^ m = q ^ m :=
      mul_right_cancel₀ (pow_ne_zero k hh.ne') h2
    have h4 : (-q) ^ k = q ^ (2 * m) := by
      calc (-q) ^ k = (-q) ^ k * (q⁻¹ ^ m * q ^ m) := by
              rw [inv_pow, inv_mul_cancel₀ (pow_ne_zero m hq0), mul_one]
        _ = (-q) ^ k * q⁻¹ ^ m * q ^ m := by ring
        _ = q ^ m * q ^ m := by rw [h3]
        _ = q ^ (2 * m) := by ring
    have h5 : q ^ k = q ^ (2 * m) := by
      have h6 := congrArg abs h4
      simp only [abs_pow, abs_neg, abs_of_pos hpos] at h6
      exact h6
    exact pow_right_injective₀ hpos hq.ne' h5
  · rintro rfl
    exact hbarGen_monomial_bar_even q hq0 m

/-! ## 2. `w` on the pin window, in exact rationals

The window `q ∈ [11099/10000, 111/100]` contains the proton pin
`q₀ = 1.10997858275138`. Its image under `w = q + q⁻¹ − 2` is contained in
`[108/10000, 11/1000]`; the probe measures `w(q₀) = 0.010897`. -/

/-- `w ≥ 0.0108` on the window: `q ≥ 1.1099` and `q⁻¹ ≥ 100/111` give
`w ≥ 1.1099 + 100/111 − 2 = 0.0108 + 1/1110000`. -/
theorem wGen_lower_bound (q : ℝ)
    (hq0 : (11099 : ℝ) / 10000 ≤ q) (hq1 : q ≤ (111 : ℝ) / 100) :
    (108 : ℝ) / 10000 ≤ wGen q := by
  have hqpos : (0 : ℝ) < q := by linarith
  have hinv : (100 : ℝ) / 111 ≤ q⁻¹ := by
    rw [inv_eq_one_div, le_div_iff₀ hqpos]
    linarith
  unfold wGen
  linarith

/-- `w ≤ 0.011` on the window: `q ≤ 1.11` and `q⁻¹ ≤ 10000/11099` give
`w ≤ 1.11 + 10000/11099 − 2 = 0.011 − 199/11099000`. -/
theorem wGen_upper_bound (q : ℝ)
    (hq0 : (11099 : ℝ) / 10000 ≤ q) (hq1 : q ≤ (111 : ℝ) / 100) :
    wGen q ≤ (11 : ℝ) / 1000 := by
  have hqpos : (0 : ℝ) < q := by linarith
  have hinv : q⁻¹ ≤ (10000 : ℝ) / 11099 := by
    rw [inv_eq_one_div, div_le_iff₀ hqpos]
    linarith
  unfold wGen
  linarith

/-! ## 3. The `w`-tower admits no order with a small-height coefficient -/

/-- **The `w`-tower carries no small-height residual** (Lean form of the
probe's measured `t/w³ = 0.16211 < 1/5`, `t/w⁴ = 14.877 > 5`). For every
order `j`, a monomial `|c|·w^j` with `|c| ∈ [1/5, 5]` and `q` in the pin
window misses the residual window `t ∈ [1.8e-7, 2.4e-7]`.

Orders `j ≤ 3` give at least `(1/5)·(108/10000)³ ≈ 2.52e-7`, above the top of
the window; orders `j ≥ 4` give at most `5·(11/1000)⁴ ≈ 7.32e-8`, below the
bottom. Both are contradictions; the proof mirrors `order_window`. -/
theorem no_small_height_w_monomial (q c t : ℝ) (j : ℕ)
    (hq0 : (11099 : ℝ) / 10000 ≤ q) (hq1 : q ≤ (111 : ℝ) / 100)
    (hc0 : (1 : ℝ) / 5 ≤ |c|) (hc1 : |c| ≤ 5)
    (htlo : (18 : ℝ) / 10 ^ 8 ≤ t) (hthi : t ≤ (24 : ℝ) / 10 ^ 8) :
    |c| * wGen q ^ j ≠ t := by
  have hw_lo : (108 : ℝ) / 10000 ≤ wGen q := wGen_lower_bound q hq0 hq1
  have hw_hi : wGen q ≤ (11 : ℝ) / 1000 := wGen_upper_bound q hq0 hq1
  have hw0 : (0 : ℝ) ≤ wGen q := by linarith
  have hw1 : wGen q ≤ 1 := by linarith
  have hpj : (0 : ℝ) ≤ wGen q ^ j := pow_nonneg hw0 j
  intro ht
  rcases (show j ≤ 3 ∨ 4 ≤ j by omega) with hle | hge
  · -- `j ≤ 3`: the monomial is too large.
    have hmono : wGen q ^ 3 ≤ wGen q ^ j := pow_le_pow_of_le_one hw0 hw1 hle
    have hlow : ((108 : ℝ) / 10000) ^ 3 ≤ wGen q ^ 3 := by gcongr
    have hcm : (1 : ℝ) / 5 * wGen q ^ j ≤ |c| * wGen q ^ j :=
      mul_le_mul_of_nonneg_right hc0 hpj
    have hnum : (24 : ℝ) / 10 ^ 8 < (1 : ℝ) / 5 * ((108 : ℝ) / 10000) ^ 3 := by
      norm_num
    linarith
  · -- `j ≥ 4`: the monomial is too small.
    have hmono : wGen q ^ j ≤ wGen q ^ 4 := pow_le_pow_of_le_one hw0 hw1 hge
    have hhigh : wGen q ^ 4 ≤ ((11 : ℝ) / 1000) ^ 4 := by gcongr
    have hcm : |c| * wGen q ^ j ≤ 5 * wGen q ^ j :=
      mul_le_mul_of_nonneg_right hc1 hpj
    have hnum : (5 : ℝ) * ((11 : ℝ) / 1000) ^ 4 < (18 : ℝ) / 10 ^ 8 := by
      norm_num
    linarith

/-! ## 4. Capstone -/

/-- **No bar-even small-height monomial carries the μ–p residual.** If
`ℏ_q^k · q^m` is bar-even (`hbar`), `q` lies in the pin window, `|c| ∈ [1/5, 5]`
and `t` in the residual window, then `|c|·ℏ_q^k·q^m ≠ t`.

Bar-evenness forces `k = 2m` (`bar_even_monomial_iff`), the positive half of
the selection rule rewrites the monomial as `w^m`
(`hbarGen_pow_two_mul_eq_wGen_pow`), and `no_small_height_w_monomial` excludes
every `m`. -/
theorem no_bar_even_small_height_monomial (q c t : ℝ) (k m : ℕ)
    (hq0 : (11099 : ℝ) / 10000 ≤ q) (hq1 : q ≤ (111 : ℝ) / 100)
    (hc0 : (1 : ℝ) / 5 ≤ |c|) (hc1 : |c| ≤ 5)
    (htlo : (18 : ℝ) / 10 ^ 8 ≤ t) (hthi : t ≤ (24 : ℝ) / 10 ^ 8)
    (hbar : hbarGen q⁻¹ ^ k * (q⁻¹) ^ m = hbarGen q ^ k * q ^ m) :
    |c| * (hbarGen q ^ k * q ^ m) ≠ t := by
  have hq : (1 : ℝ) < q := by linarith
  have hq0' : q ≠ 0 := by
    have : (0 : ℝ) < q := by linarith
    exact this.ne'
  have hk : k = 2 * m := (bar_even_monomial_iff q hq k m).mp hbar
  subst hk
  rw [hbarGen_pow_two_mul_eq_wGen_pow q hq0' m]
  exact no_small_height_w_monomial q c t m hq0 hq1 hc0 hc1 htlo hthi

/-- The capstone against the **production** substrate `hbarQ` (from
`MmuR9V9Closure`), via the bridge `hbarGen_eq_hbarQ`. -/
theorem no_bar_even_small_height_monomial_hbarQ (q c t : ℝ) (k m : ℕ)
    (hq0 : (11099 : ℝ) / 10000 ≤ q) (hq1 : q ≤ (111 : ℝ) / 100)
    (hc0 : (1 : ℝ) / 5 ≤ |c|) (hc1 : |c| ≤ 5)
    (htlo : (18 : ℝ) / 10 ^ 8 ≤ t) (hthi : t ≤ (24 : ℝ) / 10 ^ 8)
    (hbar : hbarQ q⁻¹ ^ k * (q⁻¹) ^ m = hbarQ q ^ k * q ^ m) :
    |c| * (hbarQ q ^ k * q ^ m) ≠ t := by
  have hq0' : q ≠ 0 := by
    have : (0 : ℝ) < q := by linarith
    exact this.ne'
  rw [← hbarGen_eq_hbarQ q hq0']
  rw [← hbarGen_eq_hbarQ q hq0', ← hbarGen_eq_hbarQ q⁻¹ (inv_ne_zero hq0')] at hbar
  exact no_bar_even_small_height_monomial q c t k m hq0 hq1 hc0 hc1 htlo hthi hbar

/-! ## 5. The admissibility class, and the monomial family's absence from it -/

/-- **Admissible GAP-A-4 correction factor.** A function `F : ℝ → ℝ` of the
substrate modulus is an admissible carrier of the μ–p residual at the pin `q₀`
when

* `pin_window` — the pin lies in the window `[1.1099, 1.11]` (which contains
  the proton pin `1.10997858275138`);
* `bar_even` — `F` is fixed by the bar involution, `F q⁻¹ = F q` for `q > 0`
  (the corpus's precondition, here a *hypothesis on the class*);
* `carries_residual` — evaluated at the pin, `F` lands in the residual window
  `[1.8e-7, 2.4e-7]` around the measured `t = 2.0975e-7`.

Every field is content-bearing; the class is not claimed non-empty. -/
structure GapA4CorrectionAdmissible (F : ℝ → ℝ) (q₀ : ℝ) : Prop where
  pin_window : (11099 : ℝ) / 10000 ≤ q₀ ∧ q₀ ≤ (111 : ℝ) / 100
  bar_even : ∀ q : ℝ, 0 < q → F q⁻¹ = F q
  carries_residual : (18 : ℝ) / 10 ^ 8 ≤ F q₀ ∧ F q₀ ≤ (24 : ℝ) / 10 ^ 8

/-- **No small-height monomial is admissible.** For every `k, m` and every
coefficient with `|c| ∈ [1/5, 5]`, the function `q ↦ c·ℏ_q^k·q^m` is not an
admissible carrier at any pin. (Bar-evenness of the function at `q₀`, after
cancelling `c ≠ 0`, is the hypothesis of the capstone; positivity of the
residual forces `c·X = |c|·X`.) -/
theorem monomial_not_admissible (c q₀ : ℝ) (k m : ℕ)
    (hc0 : (1 : ℝ) / 5 ≤ |c|) (hc1 : |c| ≤ 5) :
    ¬ GapA4CorrectionAdmissible (fun q => c * (hbarGen q ^ k * q ^ m)) q₀ := by
  intro hF
  obtain ⟨hq0, hq1⟩ := hF.pin_window
  have htlo : (18 : ℝ) / 10 ^ 8 ≤ c * (hbarGen q₀ ^ k * q₀ ^ m) := hF.carries_residual.1
  have hthi : c * (hbarGen q₀ ^ k * q₀ ^ m) ≤ (24 : ℝ) / 10 ^ 8 := hF.carries_residual.2
  have hq : (1 : ℝ) < q₀ := by linarith
  have hpos : (0 : ℝ) < q₀ := by linarith
  have hcne : c ≠ 0 := abs_pos.mp (by linarith)
  have hb : c * (hbarGen q₀⁻¹ ^ k * (q₀⁻¹) ^ m) = c * (hbarGen q₀ ^ k * q₀ ^ m) :=
    hF.bar_even q₀ hpos
  have hbar : hbarGen q₀⁻¹ ^ k * (q₀⁻¹) ^ m = hbarGen q₀ ^ k * q₀ ^ m :=
    mul_left_cancel₀ hcne hb
  have hX : (0 : ℝ) < hbarGen q₀ ^ k * q₀ ^ m :=
    mul_pos (pow_pos (hbarGen_pos q₀ hq) k) (pow_pos hpos m)
  have hFpos : (0 : ℝ) < c * (hbarGen q₀ ^ k * q₀ ^ m) := by
    have h18 : (0 : ℝ) < (18 : ℝ) / 10 ^ 8 := by norm_num
    exact lt_of_lt_of_le h18 htlo
  have hkey : |c| * (hbarGen q₀ ^ k * q₀ ^ m) = c * (hbarGen q₀ ^ k * q₀ ^ m) := by
    have h1 := abs_mul c (hbarGen q₀ ^ k * q₀ ^ m)
    rw [abs_of_pos hFpos, abs_of_pos hX] at h1
    exact h1.symm
  exact no_bar_even_small_height_monomial q₀ c _ k m hq0 hq1 hc0 hc1 htlo hthi hbar hkey

end QOU.BraidKnot.MuPCorrectionAdmissibility
