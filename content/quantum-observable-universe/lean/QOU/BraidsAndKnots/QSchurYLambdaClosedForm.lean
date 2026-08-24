import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import QOU.MathlibExt.QIntegerCanonical

/-!
# QOU.BraidsAndKnots.QSchurYLambdaClosedForm

q-Schur Plancherel weights `y_λ(q)` closed-form via q-content principal
specialization:

```
y_λ(q) = q^{c(λ)} / [n]_q!
  where c(λ) = Σ_{(i,j) ∈ λ} (j − i) is the content sum
        [n]_q! = Π_{k=1}^n (q^k − q^{-k})/(q − q^{-1})
```

This file is the `qou` Lake package canonical Lean for content block
[`prop:q-schur-y-lambda-closed-form`](../../../../braids-and-knots/q-schur-y-lambda-closed-form.md)
introduced in [PR #1259](https://github.com/litlfred/qou/pull/1259).

**Why this matters for 1ppb**: per the
[1ppb status dashboard](../../../../../../computations/per-observable-100x-status.witness.json),
q-Schur Plancherel is the convention used by `Q_β` at N=3 categorical,
which is **the only observable currently meeting Subgoal-1**
(6.02 ppb pred vs 7.80 ppb target). Formalising the closed-form
identity establishes the structural backbone for the Q_β derivation
chain at Lean level.

## What's defined (Lean-typed, sorry-free)

- `contentSum λ` — Σ_{cells (i,j) ∈ λ} (j − i)
- `qBracket k q` — `[k]_q = (q^k − q^{-k}) / (q − q^{-1})`
- `qFactorial n q` — `[n]_q! = Π_{k=1}^n [k]_q`
- `ySchurClosedForm λ q` — `q^{c(λ)} / [n]_q!`

## What's conjectural (axiomatised as class — §3b-cond)

- `QSchurYLambdaClosedFormClaim`: the closed form ACTUALLY IS the
  q-Schur Markov-trace Plancherel weight at every n and every q.
  Axiomatised as a class with an abstract `qSchurWeight` field
  (the categorical weight, awaiting Mathlib's q-Schur algebra
  formalisation) and an extensional identity
  `closed_form_holds : ∀ λ q, ySchurClosedForm λ q = qSchurWeight λ q`.
  This is a known theorem in q-Schur duality (Lusztig 1990,
  Beilinson-Lusztig-MacPherson); the class deviates from the
  repo's vacuous-`True` §3b-cond convention because PR #1720
  review (Gemini) flagged the placeholder as semantically
  degenerate.

- `qSchur_H2_top`, `qSchur_H2_bottom`, `qSchur_H2_normalization`:
  the H_2 case explicit identities, **sorry-free** via
  `unfold + decide + qFactorial + qBracket + field_simp + ring`.
  These are concrete `q`-bracket identities — the class
  `QSchurYLambdaClosedFormClaim` above carries the categorical
  content extensionally (`∀ λ q, ySchurClosedForm λ q = qSchurWeight λ q`);
  see the class docstring.

- `qSchur_H3_top`, `qSchur_H3_mid`, `qSchur_H3_bottom`:
  the H_3 case explicit identities for partitions `(3)`, `(2,1)`,
  `(1,1,1)`, **sorry-free** via the same H_2 pattern. Helper lemmas
  `q_add_inv_ne_zero` and `q_sq_add_one_add_inv_sq_ne_zero` factor
  the non-vanishing side-conditions. Unlike H_2 there is no clean
  "normalization" theorem at H_3 because the unweighted partition
  sum is not 1 — Plancherel weighting by `dim_q(λ)²` would be
  required, deferred to the q-Schur algebra formalisation that
  discharges `QSchurYLambdaClosedFormClaim`.

## H_2 cross-check (numerically verified in PR #1259 audit)

  y_(2)(q) = q · q^0 / ([1]_q · [2]_q)
           = q / (q + q⁻¹)              (since [1]_q = 1, [2]_q = q + q⁻¹)

  y_{(1,1)}(q) = q^{-1} / [2]_q!
              = q⁻¹ / (q + q⁻¹)

  Sum: (q + q⁻¹) / (q + q⁻¹) = 1   ✓ Plancherel normalization

The audit's H_2 cross-check (`docs/audits/2026-05-25-markov-trace-convention-audit.md`)
confirms this numerically against `pn.trace_weights_n_q_schur(2, q)`.

-- Ref: [wenzl1988] Wenzl, "Hecke algebra traces of the symmetric group", Invent. Math. 92 (1988)
-- Ref: [jones1987] Jones, "Hecke algebra representations of braid groups and link polynomials", Ann. Math. 126 (1987)
-- Ref: [blm1990] Beilinson, Lusztig, MacPherson, "A geometric setting for the
--   quantum deformation of GL_n", Duke Math. J. 61 (1990) — the q-Schur source.
-- Ref: [lusztig1990] Lusztig, "Canonical bases arising from quantized enveloping
--   algebras", J. Amer. Math. Soc. 3 (1990). Retained for the canonical-basis
--   material only. It is NOT the source of the q-Schur weight identity below;
--   see bean qou-2joi.
-/

namespace QOU.BraidsAndKnots

/-- Row contribution to content sum for a row of length `row` starting at
    row-index `i`: `Σ_{j=0}^{row-1} (j - i)`.

    Defined by structural recursion on `row` (rather than `Finset.range`)
    so that closed evaluations `rowContentSum r i` reduce in the kernel —
    used by the `decide` proofs of the H_2 / H_3 content sums below. -/
def rowContentSum : ℕ → ℕ → ℤ
  | 0, _ => 0
  | (row + 1), i => rowContentSum row i + ((row : ℤ) - (i : ℤ))

/-- Content sum `c(λ) = Σ_{(i,j) ∈ λ} (j − i)` for a partition `λ`
    represented as a list of row lengths.

    Row index `i` (0-based) and column index `j` (0-based); each cell
    `(i, j)` contributes `j - i` to the sum. -/
def contentSum (lam : List ℕ) : ℤ :=
  go lam 0
where
  go : List ℕ → ℕ → ℤ
  | [], _ => 0
  | (row :: rest), i => rowContentSum row i + go rest (i + 1)

/-- q-integer `[k]_q = (q^k − q^{-k}) / (q − q^{-1})` for `k : ℕ`.

    Returns `0` if `q − q⁻¹ = 0` (i.e. `q = ±1`, the degenerate case
    where the bracket is not well-defined). For valid `q`:
    - `[0]_q = 0`
    - `[1]_q = 1`
    - `[2]_q = q + q⁻¹`
    - `[n]_q = q^{n-1} + q^{n-3} + ... + q^{-(n-1)}` (n terms) -/
noncomputable def qBracket (k : ℕ) (q : ℝ) : ℝ :=
  if _h : q - q⁻¹ = 0 then 0
  else (q ^ (k : ℤ) - q ^ (-(k : ℤ))) / (q - q⁻¹)

/-- **Bridge to the canonical balanced bracket, and the guard is redundant.**

This site guards the singular locus `q − q⁻¹ = 0` and returns `0` there — which
is exactly what the *unguarded* `qIntBal` already returns, since Lean's
`x / 0 = 0`.  So unlike the sites that guard to `n`, this one is not a
classical extension at all: it agrees with the plain canonical bracket
everywhere, and needs no hypothesis. -/
theorem qBracket_eq_canonical (k : ℕ) (q : ℝ) :
    qBracket k q = QOU.QInteger.qIntBal q k := by
  unfold qBracket
  split_ifs with h
  · simp [QOU.QInteger.qIntBal, QOU.Mass.QHookDimensionBalanced.qIntBal, h]
  · simp [QOU.QInteger.qIntBal, QOU.Mass.QHookDimensionBalanced.qIntBal, zpow_neg,
      zpow_natCast, inv_pow]

/-- q-factorial `[n]_q! = Π_{k=1}^{n} [k]_q`. At `n = 0` returns 1. -/
noncomputable def qFactorial : ℕ → ℝ → ℝ
  | 0, _ => 1
  | (n + 1), q => qBracket (n + 1) q * qFactorial n q

/-- q-Schur Plancherel weight closed form: `y_λ(q) = q^{c(λ)} / [n]_q!`
    where `n = |λ|` is the partition size. -/
noncomputable def ySchurClosedForm (lam : List ℕ) (q : ℝ) : ℝ :=
  q ^ (contentSum lam) / qFactorial lam.sum q

/-- **Conjecture (axiomatised as class per AGENTS.md §3b-cond)**.

    For every partition `λ` and every valid `q : ℝ`, the q-Schur
    Markov-trace Plancherel weight `y_λ^{qSchur}(q)` equals the
    closed form `ySchurClosedForm λ q = q^{c(λ)} / [n]_q!`.

    This is a known theorem in q-Schur duality (Lusztig 1990,
    Beilinson–Lusztig–MacPherson) but its Lean formalisation from
    Mathlib axioms requires the q-Schur algebra structure not
    currently in Mathlib. The class axiomatises this via an abstract
    `qSchurWeight` field (the categorical weight, awaiting the
    Mathlib formalisation) and an extensional `closed_form_holds`
    identity asserting equality with `ySchurClosedForm` everywhere.
    Downstream theorems depending on this closed form take this
    class as an `[Instance]` hypothesis per §3b-cond.

    Convention deviation note: most §3b-cond classes in the
    repository (~80-100, registered under
    `lean-section-3b-cond-classes-permanent`) use a vacuous
    `True` placeholder field. This class uses the stronger
    extensional form per PR #1720 review (Gemini, 2026-06-03);
    the repo-wide convention is unchanged. -/
class QSchurYLambdaClosedFormClaim where
  /-- The categorical q-Schur Markov-trace Plancherel weight,
      awaiting Mathlib's q-Schur algebra formalisation. Until then
      this field is provided abstractly by any instance of the
      class; the conjecture is `closed_form_holds` below. -/
  qSchurWeight : List ℕ → ℝ → ℝ
  /-- **The conjecture**: the closed form `ySchurClosedForm` agrees
      with the q-Schur weight `qSchurWeight` at every partition and
      every valid q, i.e. `y_λ^{qSchur}(q) = q^{c(λ)} / [n]_q!`. Any
      instance of this class commits to that extensional identification.

      **Provenance corrected 2026-08-24 (bean `qou-2joi`).** This read
      "the Lusztig 1990 / BLM identity" and carried a single
      `-- Ref: [lusztig1990]`. That key is *Canonical bases arising from
      quantized enveloping algebras* (JAMS 3), which is not where a
      q-Schur Markov-trace weight identity lives; the q-Schur source is
      BLM, now `[blm1990]`. Two further cautions before anyone treats
      this as settled-in-the-literature rather than open here:

      * `blm1990` is **UNVERIFIED** — added from recall because the
        bibliography had zero q-Schur entries, and neither paper is in
        `library/`, so nothing in this repo can check the identity as
        stated. `lusztig1990` has no entry in
        `content/bib-qa-verifications.json` either.
      * The corpus asserts **two different DOIs** for `lusztig1990`:
        `10.2307/1990961` in `content/schema/references.ts`, and
        `10.2307/2152736` in `QOU/OptionE/CrystalDeltaLambdaScaffold.lean`
        and `QOU/IwahoriHecke/TypeA.lean`. Not resolved here — guessing
        which is right is exactly what produced the discrepancy. -/
  closed_form_holds : ∀ lam q, ySchurClosedForm lam q = qSchurWeight lam q

/-! ## q-bracket and q-factorial closed-form values

The H_2 / H_3 identities below are cleanest when the `qBracket` /
`qFactorial` denominators are first reduced to their closed forms.
These value lemmas isolate the `field_simp + ring` work onto a single
bracket at a time (mirrors `YLambdaQSchur.qInt_two_eq_q_plus_q_inv`),
so the downstream theorems are pure rewrites. -/

/-- **`[1]_q = 1`** (for valid `q`, i.e. `q − q⁻¹ ≠ 0`). -/
theorem qBracket_one (q : ℝ) (h2 : q - q⁻¹ ≠ 0) : qBracket 1 q = 1 := by
  unfold qBracket
  rw [dif_neg h2]
  norm_num
  exact div_self h2

/-- **`[2]_q = q + q⁻¹`**. -/
theorem qBracket_two (q : ℝ) (hq : q ≠ 0) (h2 : q - q⁻¹ ≠ 0) :
    qBracket 2 q = q + q⁻¹ := by
  unfold qBracket
  rw [dif_neg h2, div_eq_iff h2]
  simp only [zpow_neg, zpow_natCast]
  field_simp
  ring

/-- **`[3]_q = q² + 1 + q⁻²`** — difference of cubes over `q − q⁻¹`. -/
theorem qBracket_three (q : ℝ) (hq : q ≠ 0) (h2 : q - q⁻¹ ≠ 0) :
    qBracket 3 q = q ^ 2 + 1 + (q⁻¹) ^ 2 := by
  unfold qBracket
  rw [dif_neg h2, div_eq_iff h2]
  simp only [zpow_neg, zpow_natCast]
  field_simp
  ring

/-- **`[2]_q! = q + q⁻¹`** (`= [2]_q · [1]_q`). -/
theorem qFactorial_two (q : ℝ) (hq : q ≠ 0) (h2 : q - q⁻¹ ≠ 0) :
    qFactorial 2 q = q + q⁻¹ := by
  show qBracket 2 q * (qBracket 1 q * 1) = q + q⁻¹
  rw [qBracket_one q h2, qBracket_two q hq h2]
  ring

/-- **`[3]_q! = (q² + 1 + q⁻²)(q + q⁻¹)`** (`= [3]_q · [2]_q!`). -/
theorem qFactorial_three (q : ℝ) (hq : q ≠ 0) (h2 : q - q⁻¹ ≠ 0) :
    qFactorial 3 q = (q ^ 2 + 1 + (q⁻¹) ^ 2) * (q + q⁻¹) := by
  show qBracket 3 q * qFactorial 2 q = (q ^ 2 + 1 + (q⁻¹) ^ 2) * (q + q⁻¹)
  rw [qBracket_three q hq h2, qFactorial_two q hq h2]

/-! ## H_2 explicit identities

The audit `docs/audits/2026-05-25-markov-trace-convention-audit.md`
verifies these at H_2 numerically. The Lean theorems below discharge
the algebraic identities sorry-free via the `qFactorial`/`qBracket`
value lemmas above plus a single `zpow` reduction of the numerator.
-/

/-- **H_2 case for `(2)`**: `y_(2)(q) = q / (q + q⁻¹)`. -/
theorem qSchur_H2_top (q : ℝ) (hq : q ≠ 0) (h2 : q - q⁻¹ ≠ 0) :
    ySchurClosedForm [2] q = q / (q + q⁻¹) := by
  unfold ySchurClosedForm
  have hc : contentSum [2] = 1 := by decide
  have hs : ([2] : List ℕ).sum = 2 := by decide
  rw [hc, hs, qFactorial_two q hq h2, zpow_one]

/-- **H_2 case for `(1,1)`**: `y_{(1,1)}(q) = q⁻¹ / (q + q⁻¹)`. -/
theorem qSchur_H2_bottom (q : ℝ) (hq : q ≠ 0) (h2 : q - q⁻¹ ≠ 0) :
    ySchurClosedForm [1, 1] q = q⁻¹ / (q + q⁻¹) := by
  unfold ySchurClosedForm
  have hc : contentSum [1, 1] = -1 := by decide
  have hs : ([1, 1] : List ℕ).sum = 2 := by decide
  rw [hc, hs, qFactorial_two q hq h2]
  simp only [zpow_neg, zpow_one]

/-- **H_2 Plancherel normalization**: `y_(2)(q) + y_{(1,1)}(q) = 1`. -/
theorem qSchur_H2_normalization (q : ℝ) (hq : q ≠ 0) (h2 : q - q⁻¹ ≠ 0) :
    ySchurClosedForm [2] q + ySchurClosedForm [1, 1] q = 1 := by
  rw [qSchur_H2_top q hq h2, qSchur_H2_bottom q hq h2]
  -- q/(q + q⁻¹) + q⁻¹/(q + q⁻¹) = (q + q⁻¹)/(q + q⁻¹) = 1
  have hsum_ne : q + q⁻¹ ≠ 0 := by
    intro heq
    -- If q + q⁻¹ = 0, then q² = -1, but q : ℝ so impossible (unless q complex)
    -- For real q ≠ 0: q + 1/q = 0 ⇒ q² = -1, impossible.
    have : q * (q + q⁻¹) = 0 := by rw [heq]; ring
    rw [mul_add, mul_inv_cancel₀ hq] at this
    -- this: q * q + 1 = 0, i.e. q² = -1
    have hq2 : q * q = -1 := by linarith
    -- q² ≥ 0 contradicts q² = -1
    have hsq : 0 ≤ q * q := mul_self_nonneg q
    linarith
  field_simp

/-! ## H_3 explicit identities

For partitions of `n = 3`:

  c((3))     =  3  ⇒  y_(3)(q)     = q^3 / [3]_q!
  c((2,1))   =  0  ⇒  y_{(2,1)}(q) = 1   / [3]_q!
  c((1,1,1)) = -3  ⇒  y_{(1,1,1)}(q) = q⁻³ / [3]_q!

with `[3]_q! = [3]_q · [2]_q · 1 = (q² + 1 + q⁻²)(q + q⁻¹)`.

Unlike `H_2`, the analogue of `qSchur_H2_normalization` requires
weighting by `dim_q(λ)²` (q-Schur Plancherel measure on the dual
chain) — `dim((2,1)) = 2` makes the un-weighted sum
`y_(3) + y_{(2,1)} + y_{(1,1,1)}` not equal to 1.  We therefore
state the three identities only; a full Plancherel statement is
left to the future `q-Schur algebra` development that will
discharge `QSchurYLambdaClosedFormClaim`.
-/

/-- Non-vanishing of `q + q⁻¹` for any real `q ≠ 0` (since `q² = -1`
    has no real solution).  Helper shared across the H_3 identities. -/
lemma q_add_inv_ne_zero {q : ℝ} (hq : q ≠ 0) : q + q⁻¹ ≠ 0 := by
  intro heq
  have : q * (q + q⁻¹) = 0 := by rw [heq]; ring
  rw [mul_add, mul_inv_cancel₀ hq] at this
  have hsq : 0 ≤ q * q := mul_self_nonneg q
  linarith

/-- Strict positivity of `q² + 1 + (q⁻¹)²` for any real `q` (sum of
    two squares plus 1).  Helper shared across the H_3 identities. -/
lemma q_sq_add_one_add_inv_sq_pos (q : ℝ) : 0 < q^2 + 1 + (q⁻¹)^2 := by
  have h_q : 0 ≤ q^2 := sq_nonneg q
  have h_iq : 0 ≤ (q⁻¹)^2 := sq_nonneg q⁻¹
  linarith

/-- Non-vanishing of `q² + 1 + (q⁻¹)²`, via strict positivity. -/
lemma q_sq_add_one_add_inv_sq_ne_zero (q : ℝ) : q^2 + 1 + (q⁻¹)^2 ≠ 0 :=
  ne_of_gt (q_sq_add_one_add_inv_sq_pos q)

/-- **H_3 case for `(3)`**: `y_(3)(q) = q^3 / ((q + q⁻¹)(q^2 + 1 + q⁻²))`. -/
theorem qSchur_H3_top (q : ℝ) (hq : q ≠ 0) (h2 : q - q⁻¹ ≠ 0) :
    ySchurClosedForm [3] q = q^3 / ((q + q⁻¹) * (q^2 + 1 + (q⁻¹)^2)) := by
  unfold ySchurClosedForm
  have hc : contentSum [3] = 3 := by decide
  have hs : ([3] : List ℕ).sum = 3 := by decide
  rw [hc, hs, qFactorial_three q hq h2, show (3 : ℤ) = ((3 : ℕ) : ℤ) from rfl,
    zpow_natCast]
  rw [div_eq_div_iff
    (mul_ne_zero (q_sq_add_one_add_inv_sq_ne_zero q) (q_add_inv_ne_zero hq))
    (mul_ne_zero (q_add_inv_ne_zero hq) (q_sq_add_one_add_inv_sq_ne_zero q))]
  ring

/-- **H_3 case for `(2,1)`**: `y_{(2,1)}(q) = 1 / ((q + q⁻¹)(q^2 + 1 + q⁻²))`. -/
theorem qSchur_H3_mid (q : ℝ) (hq : q ≠ 0) (h2 : q - q⁻¹ ≠ 0) :
    ySchurClosedForm [2, 1] q = 1 / ((q + q⁻¹) * (q^2 + 1 + (q⁻¹)^2)) := by
  unfold ySchurClosedForm
  have hc : contentSum [2, 1] = 0 := by decide
  have hs : ([2, 1] : List ℕ).sum = 3 := by decide
  rw [hc, hs, qFactorial_three q hq h2, zpow_zero]
  rw [div_eq_div_iff
    (mul_ne_zero (q_sq_add_one_add_inv_sq_ne_zero q) (q_add_inv_ne_zero hq))
    (mul_ne_zero (q_add_inv_ne_zero hq) (q_sq_add_one_add_inv_sq_ne_zero q))]
  ring

/-- **H_3 case for `(1,1,1)`**: `y_{(1,1,1)}(q) = (q⁻¹)^3 / ((q + q⁻¹)(q^2 + 1 + q⁻²))`. -/
theorem qSchur_H3_bottom (q : ℝ) (hq : q ≠ 0) (h2 : q - q⁻¹ ≠ 0) :
    ySchurClosedForm [1, 1, 1] q = (q⁻¹)^3 / ((q + q⁻¹) * (q^2 + 1 + (q⁻¹)^2)) := by
  unfold ySchurClosedForm
  have hc : contentSum [1, 1, 1] = -3 := by decide
  have hs : ([1, 1, 1] : List ℕ).sum = 3 := by decide
  rw [hc, hs, qFactorial_three q hq h2,
    show (-3 : ℤ) = -((3 : ℕ) : ℤ) from rfl, zpow_neg, zpow_natCast]
  rw [div_eq_div_iff
    (mul_ne_zero (q_sq_add_one_add_inv_sq_ne_zero q) (q_add_inv_ne_zero hq))
    (mul_ne_zero (q_add_inv_ne_zero hq) (q_sq_add_one_add_inv_sq_ne_zero q))]
  ring

end QOU.BraidsAndKnots
