import Mathlib.Tactic

/-!
# `sign(y_λ)` is a content-threshold parity

The Jones–Markov central coefficient is `y_λ = s_λ / Z`, with `s_λ` the Wenzl principal
specialisation

    s_λ  =  Q^{n(λ)} · ∏_{x ∈ λ} (1 − Q^r·Q^{c(x)}) / (1 − Q^{h(x)}),      Q = q².

**Convention scope (added 2026-08-24).**  The premise below — that the corpus records `y_λ`
only qualitatively as *"sign-indefinite for n ≥ 4"*
(`docs/audits/2026-05-19-weight-factor-audit.md` §W3) — is a **convention-C** statement, and C
was excised on 2026-08-09.  Under the production convention D there is nothing indefinite to
resolve: `y_λ ≥ 0` on the two-row stratum and `y_λ = 0` identically for `ℓ(λ) ≥ 3`
(`QOU.QBeta.TemperleyLiebTower`, sorry-free), measured zero-negative over `n = 4 … 12` at `q₀`.
The content block `mass-theory/y-lambda-sign-pattern` withdrew the indefiniteness claim on
2026-08-09; this file was not updated with it.

The motivating clause below is affected the same way: `Mu3SlotExclusion.door_mechanism_dichotomy`
does make the μ₃ door depend on `sign(y_λ)`, but under D its "negative weight on supermodular
geometry" branch is **vacuous**, so that mechanism has no budget for the reason opposite to the
one stated — not because the sign rule is unknown, but because the sign is known and never
negative.

**What survives, and why this file is kept.**  The combinatorial rule derived here is a
statement about the Wenzl principal specialisation itself, not about which convention selects
`z`, so the derivation stands as-is and remains the sharp form of the qualitative claim. Read it
as characterising `sign(s_λ)` in general; do not read the motivation as a live μ₃-door opening.

This file upgrades the qualitative record to a **combinatorial rule**, because
`Mu3SlotExclusion.door_mechanism_dichotomy` makes the μ₃ door depend on exactly this sign: one of
its two mechanisms is "negative weight on supermodular geometry", and without a rule for
`sign(y_λ)` that mechanism has no budget.

## The derivation

For `q > 1` (so `Q > 1`):

* every hook length satisfies `h(x) ≥ 1`, hence `Q^{h(x)} > 1` and **every denominator factor
  `1 − Q^{h(x)}` is negative** — the denominator contributes the fixed sign `(−1)^{|λ|}`
  (`wenzl_den_factor_neg`, `wenzl_den_sign`);
* a numerator factor `1 − Q^r·Q^{c(x)}` is negative **exactly** when `Q^r·Q^{c(x)} > 1`, i.e.
  exactly when the cell's content lies *above* the threshold `c* = −log_Q(Q^r)`.

Writing `P(λ)` for the number of cells *below* the threshold, the two contributions combine —
`(−1)^{#above} · (−1)^{|λ|} = (−1)^{#below}` since `#above + #below = |λ|` — to give

    sign(s_λ) = (−1)^{P(λ)}                                  (`wenzl_sign`)

The `Q^{n(λ)}` prefactor is positive and drops out.

## What this buys

At `q₀` the threshold is `c* ≈ −2.5995`, so `P(λ)` counts cells of content `≤ −3`.  A cell of
content `≤ −3` requires `≥ 4` rows, so **every `λ` with `ℓ(λ) ≤ 3` carries a positive weight**
(`shallow_of_no_deep_cells`).  That is why `(8,1)` is positive — the case that refutes the
naive "`ℓ`-parity" reading of the measured data.

Machine-verified on **all 270 partitions for n = 2..12**
(`computations/deltalambda/ylambda_sign_content_threshold_probe.py`, witness
`ylambda-sign-content-threshold.witness.json`; smallest threshold margin `8.0e-2`, far from
the `1e-12` degeneracy guard).

## Honest scope

This determines `sign(s_λ)`.  Since `y_λ = s_λ / Z` with a single global `Z` per `n`, it
determines `sign(y_λ)` **up to that one global sign**; the probe verifies `sign(Z) = +1` for
`n = 2..12` but this file does not derive it.  The parity rule itself is `q`-independent for
`q > 1` — only the *location* of the cut `c*` moves with `q`.

Verified `lean`-direct exit 0, sorry-free.

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01393695
-/

namespace QOU.MassTheory.YLambdaSignThreshold

open Finset

variable {α : Type*} [DecidableEq α]

/-! ### The sign of a finite product is the parity of its negative factors -/

/-- **Sign of a finite product.**  Multiplying a product of nonzero reals by `(−1)` raised to
the number of negative factors makes it positive.  This is the combinatorial engine behind the
whole file: it turns "count the negative factors" into an actual sign statement. -/
theorem neg_one_pow_card_neg_mul_prod_pos {f : α → ℝ} :
    ∀ {s : Finset α}, (∀ x ∈ s, f x ≠ 0) →
      0 < (-1 : ℝ) ^ (s.filter fun x => f x < 0).card * ∏ x ∈ s, f x := by
  intro s
  induction s using Finset.induction_on with
  | empty => intro _; simp
  | insert a s ha ih =>
    intro hne
    have hane : f a ≠ 0 := hne a (mem_insert_self a s)
    have hs : ∀ x ∈ s, f x ≠ 0 := fun x hx => hne x (mem_insert_of_mem hx)
    have hprev := ih hs
    rw [Finset.prod_insert ha, Finset.filter_insert]
    by_cases hlt : f a < 0
    · rw [if_pos hlt, Finset.card_insert_of_notMem (fun h => ha (mem_of_mem_filter a h))]
      have : (-1 : ℝ) ^ ((s.filter fun x => f x < 0).card + 1) * (f a * ∏ x ∈ s, f x)
          = (-f a) * ((-1 : ℝ) ^ (s.filter fun x => f x < 0).card * ∏ x ∈ s, f x) := by
        ring
      rw [this]
      exact mul_pos (by linarith) hprev
    · rw [if_neg hlt]
      have hpos : 0 < f a := lt_of_le_of_ne (not_lt.mp hlt) (Ne.symm hane)
      have : (-1 : ℝ) ^ (s.filter fun x => f x < 0).card * (f a * ∏ x ∈ s, f x)
          = f a * ((-1 : ℝ) ^ (s.filter fun x => f x < 0).card * ∏ x ∈ s, f x) := by
        ring
      rw [this]
      exact mul_pos hpos hprev

/-! ### The Wenzl denominator: every hook factor is negative -/

/-- **Every denominator factor is negative.**  A hook length is at least `1`, and `Q > 1`, so
`Q^{h} > 1` and `1 − Q^{h} < 0`.  No cell escapes this — which is what makes the denominator's
sign depend only on the *number* of cells. -/
theorem wenzl_den_factor_neg {Q : ℝ} (hQ : 1 < Q) {h : ℕ} (hh : 1 ≤ h) :
    1 - Q ^ h < 0 := by
  have : (1 : ℝ) < Q ^ h := one_lt_pow₀ hQ (by omega)
  linarith

/-- **The denominator contributes the fixed sign `(−1)^{|λ|}`** — it depends on the cell
*count* alone, not on the shape of the diagram. -/
theorem wenzl_den_sign {Q : ℝ} (hQ : 1 < Q) (cells : Finset α) (hgt : α → ℕ)
    (hh : ∀ x ∈ cells, 1 ≤ hgt x) :
    0 < (-1 : ℝ) ^ cells.card * ∏ x ∈ cells, (1 - Q ^ hgt x) := by
  have hfil : (cells.filter fun x => 1 - Q ^ hgt x < 0) = cells :=
    Finset.filter_true_of_mem fun x hx => wenzl_den_factor_neg hQ (hh x hx)
  have := neg_one_pow_card_neg_mul_prod_pos
    (f := fun x => 1 - Q ^ hgt x) (s := cells)
    (fun x hx => ne_of_lt (wenzl_den_factor_neg hQ (hh x hx)))
  rwa [hfil] at this

/-! ### The numerator: the content threshold -/

/-- **The threshold criterion.**  A numerator factor is negative exactly when the cell sits
*above* the threshold, i.e. when `Q^r·Q^{c(x)} > 1`.  This is the only place the content
enters, and it enters through a single scalar comparison. -/
theorem wenzl_num_factor_neg_iff {v : ℝ} : 1 - v < 0 ↔ 1 < v := by
  constructor <;> intro h <;> linarith

omit [DecidableEq α] in
/-- **Above-threshold and below-threshold cells partition the diagram.**  Given no cell sits
exactly *on* the threshold, the two counts sum to the number of cells — the bookkeeping that
lets the denominator's `(−1)^{|λ|}` be absorbed into the numerator's parity. -/
theorem card_above_add_card_below (cells : Finset α) (v : α → ℝ)
    (hnd : ∀ x ∈ cells, v x ≠ 1) :
    (cells.filter fun x => 1 < v x).card + (cells.filter fun x => v x < 1).card
      = cells.card := by
  classical
  have heq : (cells.filter fun x => ¬ (1 < v x)) = cells.filter fun x => v x < 1 := by
    apply Finset.filter_congr
    intro x hx
    constructor
    · intro h; exact lt_of_le_of_ne (not_lt.mp h) (hnd x hx)
    · intro h; exact not_lt.mpr (le_of_lt h)
  rw [← heq]
  exact Finset.filter_card_add_filter_neg_card_eq_card (p := fun x => 1 < v x)

/-! ### The main result -/

/-- **`sign(s_λ) = (−1)^{P(λ)}`, `P(λ)` the number of BELOW-threshold cells.**

The Wenzl principal specialisation `Q^{n(λ)}·∏(1 − Q^r·Q^{c})/∏(1 − Q^{h})` has sign exactly
`(−1)` to the number of cells whose content lies *below* the threshold `c* = −log_Q(Q^r)`.

Both the `Q^{n(λ)}` prefactor and the denominator's shape drop out: the former is positive,
the latter contributes `(−1)^{|λ|}` which merges with the numerator's `(−1)^{#above}` to leave
`(−1)^{#below}`.  So a *global* property of the diagram (its size) is invisible, and only the
*deep* cells matter.

Hypotheses are the honest minimum: `Q > 1` (the substrate regime `q > 1`), hooks positive
(automatic for a Young diagram), and no cell exactly on the threshold (`hnd`) — without which
the parity is genuinely undefined, not merely hard to prove. -/
theorem wenzl_sign {Q QR : ℝ} (hQ : 1 < Q) (nlam : ℕ)
    (cells : Finset α) (val : α → ℝ) (hgt : α → ℕ)
    (hh : ∀ x ∈ cells, 1 ≤ hgt x) (hnd : ∀ x ∈ cells, QR * val x ≠ 1) :
    0 < (-1 : ℝ) ^ (cells.filter fun x => QR * val x < 1).card *
      (Q ^ nlam * (∏ x ∈ cells, (1 - QR * val x)) / ∏ x ∈ cells, (1 - Q ^ hgt x)) := by
  classical
  set A := (cells.filter fun x => 1 < QR * val x).card with hA
  set B := (cells.filter fun x => QR * val x < 1).card with hB
  have hAB : A + B = cells.card := card_above_add_card_below cells (fun x => QR * val x) hnd
  -- numerator sign
  have hnum : 0 < (-1 : ℝ) ^ A * ∏ x ∈ cells, (1 - QR * val x) := by
    have hfil : (cells.filter fun x => 1 - QR * val x < 0)
        = cells.filter fun x => 1 < QR * val x := by
      apply Finset.filter_congr; intro x _; exact wenzl_num_factor_neg_iff
    have := neg_one_pow_card_neg_mul_prod_pos
      (f := fun x => 1 - QR * val x) (s := cells)
      (fun x hx => by
        have : QR * val x ≠ 1 := hnd x hx
        intro hc; apply this; linarith [sub_eq_zero.mp hc])
    rwa [hfil, ← hA] at this
  -- denominator sign
  have hden : 0 < (-1 : ℝ) ^ cells.card * ∏ x ∈ cells, (1 - Q ^ hgt x) :=
    wenzl_den_sign hQ cells hgt hh
  have hQpos : (0 : ℝ) < Q ^ nlam := pow_pos (by linarith) _
  -- assemble:  (-1)^B * (Q^n * N / D) = Q^n * ((-1)^A * N) / ((-1)^(A+B) * D)
  have hdenne : (∏ x ∈ cells, (1 - Q ^ hgt x)) ≠ 0 := by
    intro hc
    rw [hc, mul_zero] at hden
    exact lt_irrefl 0 hden
  have key : (-1 : ℝ) ^ B *
      (Q ^ nlam * (∏ x ∈ cells, (1 - QR * val x)) / ∏ x ∈ cells, (1 - Q ^ hgt x))
      = Q ^ nlam * ((-1 : ℝ) ^ A * ∏ x ∈ cells, (1 - QR * val x))
        / ((-1 : ℝ) ^ (A + B) * ∏ x ∈ cells, (1 - Q ^ hgt x)) := by
    rw [pow_add]
    field_simp
    rw [← pow_mul, mul_comm B 2, pow_mul]
    norm_num
  rw [key, hAB]
  exact div_pos (mul_pos hQpos hnum) hden

/-- **No deep cells ⇒ positive.**  If every cell sits above the threshold, `P(λ) = 0` and the
weight is positive.  At `q₀` a below-threshold cell needs content `≤ −3`, hence `≥ 4` rows — so
this is exactly the statement that every `ℓ(λ) ≤ 3` block carries a positive weight, `(8,1)`
included. -/
theorem shallow_of_no_deep_cells {Q QR : ℝ} (hQ : 1 < Q) (nlam : ℕ)
    (cells : Finset α) (val : α → ℝ) (hgt : α → ℕ)
    (hh : ∀ x ∈ cells, 1 ≤ hgt x) (hnd : ∀ x ∈ cells, QR * val x ≠ 1)
    (hshallow : ∀ x ∈ cells, 1 < QR * val x) :
    0 < Q ^ nlam * (∏ x ∈ cells, (1 - QR * val x)) / ∏ x ∈ cells, (1 - Q ^ hgt x) := by
  classical
  have hemp : (cells.filter fun x => QR * val x < 1) = ∅ := by
    apply Finset.filter_false_of_mem
    intro x hx
    exact not_lt.mpr (le_of_lt (hshallow x hx))
  have := wenzl_sign hQ nlam cells val hgt hh hnd
  rwa [hemp, Finset.card_empty, pow_zero, one_mul] at this

end QOU.MassTheory.YLambdaSignThreshold
