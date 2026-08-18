/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic

/-!
# What `/q³` in `F_Bor` actually is: a SECOND Poincaré centering

Bean `qou-24w9`. Attempt to derive the exponent in

    F_Bor(q) = |tr_M(β_Bor, q)| · [3]_q! / q³      (`m_p_substrate_identity_50dps.py:177`)

which is asserted there as "the natural categorical observable", carries 37 % of
`m_p`, and has no derivation trail.

## The candidate derivation, and what it gives

`[n]_q!` in the **unbalanced** convention is the Poincaré polynomial of `Sₙ`,

    [n]_q!^unbal = Σ_{w ∈ Sₙ} q^{ℓ(w)},     deg = ℓ(w₀) = n(n−1)/2,

so `q^{−ℓ(w₀)}` is the canonical *centering* of it. Converting to the
**balanced** convention carries exactly that factor:

    [n]_q!^balanced = q^{−n(n−1)/2} · [n]_{q²}!^unbal      (checked n = 1..6)

For `n = 3` this is `q^{−3}` — the exponent in question. So the factor has a
canonical name after all: it is `ℓ(w₀)`, the length of the longest element of
`S₃`.

## But the code already uses the balanced convention, so it centers TWICE

`m_p_substrate_identity_50dps.q_int` is `(qⁿ − q⁻ⁿ)/(q − q⁻¹)` — **balanced**.
So `qfact_three` is already the once-centered object, and `F_Bor` divides by
`q³` again:

* `balanced_is_already_centered` — `[3]_q!^bal = P(q) / q³`
* `code_form_is_doubly_centered` — `[3]_q!^bal / q³ = P(q) / q⁶`

with `P(q) = 1 + 2q² + 2q⁴ + q⁶` the Poincaré polynomial of `S₃` in `q²`. The
code's object sits at `q^{−2ℓ(w₀)}`, twice the canonical centering.

This is also why the bar-symmetry breaks (`qou-24w9`): the once-centered form
`[3]_q!^bal` **is** bar-symmetric (`balanced_is_bar_symmetric`), and the second
division destroys it.

## Verdict: NOT derived — but now precisely characterised

The exponent is not arbitrary — `3 = ℓ(w₀)` is canonical — yet applying it to an
already-balanced factorial is a **second** centering that no standard convention
calls for, and it is the step that breaks bar-symmetry. So `/q³` is identified,
not justified.

Two further facts keep this from being closed by inspection:

1. **`n = 3` is degenerate.** `ℓ(w₀) = n(n−1)/2` equals `n` *only* at `n = 3`
   (`ell_w0_eq_n_iff_three`). So the corpus's single 3-strand instance cannot
   distinguish "centering by `ℓ(w₀)`" from "one power per strand" — any 4-strand
   or 2-strand observable would, and none exists.
2. **The numerics need the doubling.** Dropping the second centering moves `m_p`
   from 938.272089427 (−2.9·10⁻¹⁰ %) to 1285.39 (+37.0 %). So the doubled form
   is what reproduces CODATA, and the open question is what *derives* it — not
   whether it is numerically load-bearing.

Scope-(a): this characterises the factor and rules out the "it is just the
balanced/unbalanced conversion" reading (that conversion is already inside
`q_int`). It does **not** refute `F_Bor`, and it does not touch the Lean-proved
`|tr_M(β_Bor)|`.
-/

namespace QOU.MassTheory.PoincareCentering

variable {K : Type*} [Field K]

/-- The Poincaré polynomial of `S₃` in the variable `q²`:
`P(q) = Σ_{w ∈ S₃} q^{2ℓ(w)} = 1 + 2q² + 2q⁴ + q⁶`. -/
def poincareS3 (q : K) : K := 1 + 2 * q ^ 2 + 2 * q ^ 4 + q ^ 6

/-- The balanced `[3]_q!`, written from the balanced integers
`[2] = q + q⁻¹` and `[3] = q² + 1 + q⁻²` (the `[1]` factor is `1`). -/
def qFactThreeBalanced (q : K) : K := (q + q⁻¹) * (q ^ 2 + 1 + (q⁻¹) ^ 2)

/-- **The balanced factorial is already the centered Poincaré polynomial.**

`[3]_q!^bal = P(q) / q³` — one factor of `q^{ℓ(w₀)}`, `ℓ(w₀) = 3`. -/
theorem balanced_is_already_centered (q : K) (hq : q ≠ 0) :
    qFactThreeBalanced q = poincareS3 q / q ^ 3 := by
  unfold qFactThreeBalanced poincareS3
  field_simp
  ring

/-- **The code's object is centered twice.**

`F_Bor` divides the balanced factorial by `q³` again, landing at
`P(q) / q⁶ = q^{−2ℓ(w₀)} · P(q)`. -/
theorem code_form_is_doubly_centered (q : K) (hq : q ≠ 0) :
    qFactThreeBalanced q / q ^ 3 = poincareS3 q / q ^ 6 := by
  rw [balanced_is_already_centered q hq]
  field_simp

/-- **The once-centered form is bar-symmetric**: `[3]_q!^bal` is invariant under
`q ↦ q⁻¹`. This is the symmetry the second division destroys. -/
theorem balanced_is_bar_symmetric (q : K) (hq : q ≠ 0) :
    qFactThreeBalanced q = qFactThreeBalanced q⁻¹ := by
  unfold qFactThreeBalanced
  field_simp
  ring

/-- **`n = 3` is the degenerate strand count.**

`ℓ(w₀) = n(n−1)/2` coincides with `n` exactly at `n = 3`, so a single 3-strand
instance cannot separate "center by `ℓ(w₀)`" from "one power per strand". -/
theorem ell_w0_eq_n_iff_three (n : ℕ) :
    n * (n - 1) = 2 * n ↔ n = 0 ∨ n = 3 := by
  cases n with
  | zero => simp
  | succ m =>
      simp only [Nat.succ_sub_one]
      constructor
      · intro h
        right
        have hm : m = 2 := by nlinarith
        omega
      · rintro (h | h)
        · omega
        · have hm : m = 2 := by omega
          subst hm; rfl

end QOU.MassTheory.PoincareCentering
