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

/-! ### The bar-conjugate form, and the writhe obstruction

One theorem per derivation attempt. -/

/-- **Attempt 1, sharpest form: the code's factor is the BAR-CONJUGATE of the
Poincaré polynomial.**

`[3]_q!^bal / q³ = P(q⁻¹)`. `P` is palindromic, so one centering reaches the
symmetric point and the second overshoots it by the same amount, landing on `P`
evaluated at the inverse variable. This is exactly what "double centering"
means. -/
theorem code_form_eq_poincare_bar (q : K) (hq : q ≠ 0) :
    qFactThreeBalanced q / q ^ 3 = poincareS3 q⁻¹ := by
  rw [code_form_is_doubly_centered q hq]
  unfold poincareS3
  field_simp
  ring

/-- A braid word as a list of signed generators; only the **sign** of each entry
matters for the writhe (`+i` is `σᵢ`, `−i` is `σᵢ⁻¹`). -/
def writhe (w : List ℤ) : ℤ := (w.map (fun g => if 0 < g then (1 : ℤ) else -1)).sum

/-- `β_Bor = (σ₁⁻¹σ₂)³`, the braid word the corpus assigns to the Borromean
rings (`borromean-markov-trace-closed-form.md:2`). -/
def borromeanWord : List ℤ := [-1, 2, -1, 2, -1, 2]

/-- **`β_Bor` has writhe zero** — three negative and three positive crossings. -/
theorem borromean_writhe_zero : writhe borromeanWord = 0 := by decide

/-- **Every writhe prefactor is trivial on `β_Bor`.** -/
theorem writhe_prefactor_is_one (a : K) :
    a ^ (writhe borromeanWord) = 1 := by
  rw [borromean_writhe_zero, zpow_zero]

/-- **Attempt 2: no writhe prefactor can produce `q⁻³` on this braid.**

`markov-axioms-primitive.md` states that link invariance is restored by the
*writhe prefactor outside the trace*. Such a prefactor is a function of the
writhe alone and multiplicative in it — `w ↦ a^w`. On `β_Bor` the writhe is `0`,
so **every** such prefactor equals `1`, whatever `a` is. Hence none yields the
`q⁻³` that `F_Bor` applies, unless `q³ = 1` — and at the substrate `q₀ ≈ 1.11`
it is not.

This is the sharp form of the negative: `/q³` does not merely lack a derivation
trail, it is **unreachable** by the normalisation rule the corpus itself states,
evaluated on the corpus's own braid word. -/
theorem no_writhe_prefactor_yields_inv_cube (a q : K) (hq3 : q ^ 3 ≠ 1) :
    a ^ (writhe borromeanWord) ≠ (q ^ 3)⁻¹ := by
  rw [writhe_prefactor_is_one]
  intro h
  exact hq3 (inv_eq_one.mp h.symm)

/-! ### Resolution: `/q³` cannot be a state-dependent categorical factor

The mirror image of a link corresponds to `q ↦ q⁻¹` in the Markov trace, and the
corpus reads the bar involution as the conjugate (antiparticle) state
(`strand-twist-datum.md`). So the bar-transform of the categorical factor is what
distinguishes a state from its conjugate.

Both of `F_Bor`'s honest ingredients are blind to that:

* `trM_bar_invariant` — the Lean-proved closed form `(4+h²−3h⁴−h⁶)/(h²+4)` is
  **even in `h = q − q⁻¹`**, and `h ↦ −h` under `q ↦ q⁻¹`, so `tr_M` is
  bar-invariant.
* `balanced_is_bar_symmetric` (above) — `[3]_q!^bal` is bar-symmetric.

So the **only** bar-asymmetric step is the `/q³`, and it is asymmetric by a
definite amount:

* `fbor_mirror_ratio` — `F_Bor(q⁻¹) = q⁶ · F_Bor(q)`.

At the substrate `q₀ ≈ 1.11` that is `q₀⁶ ≈ 1.87`. Read as a *state-dependent*
categorical factor, `/q³` would therefore make a state and its conjugate differ
by 87 % — which is not a small correction but a gross asymmetry.

**The resolution.** `/q³` cannot be a categorical factor attached to the state.
It has to be a fixed normalisation applied identically to a state and its
conjugate — in which case it is, by construction, a **convention**, not
something the braid determines. That is consistent with every earlier finding
here: it is unreachable by the writhe rule (`no_writhe_prefactor_yields_inv_cube`),
it double-counts the Poincaré centering (`code_form_is_doubly_centered`), and it
breaks the bar-symmetry both ingredients have.

Interpretive caveat, stated: the identification "mirror ↦ `q ↦ q⁻¹`" is the
standard Markov/HOMFLY behaviour and matches the corpus's reading of `bar`, but
the physical step from there to a particle/antiparticle mass ratio is
interpretation, not theorem. The theorems below are the algebra. -/

/-- The Lean-proved Borromean Markov trace as a function of `q`, via
`h = q − q⁻¹`. -/
def trMBorromean (q : K) : K :=
  let h := q - q⁻¹
  (4 + h ^ 2 - 3 * h ^ 4 - h ^ 6) / (h ^ 2 + 4)

/-- **`tr_M(β_Bor)` is bar-invariant**: the closed form is even in `h`, and
`h ↦ −h` under `q ↦ q⁻¹`. So the trace does not distinguish a state from its
conjugate. -/
theorem trM_bar_invariant (q : K) (hq : q ≠ 0) :
    trMBorromean q⁻¹ = trMBorromean q := by
  unfold trMBorromean
  simp only [inv_inv]
  field_simp
  ring

/-- `F_Bor` as the code computes it. -/
def fBor (q : K) : K := trMBorromean q * qFactThreeBalanced q / q ^ 3

/-- **The whole bar-asymmetry of `F_Bor` is `q⁶`, and it comes only from `/q³`.**

Both ingredients are bar-blind, so the mirror ratio is exactly the square of the
applied normalisation. -/
theorem fbor_mirror_ratio (q : K) (hq : q ≠ 0) :
    fBor q⁻¹ = q ^ 6 * fBor q := by
  unfold fBor
  rw [trM_bar_invariant q hq, ← balanced_is_bar_symmetric q hq]
  field_simp

/-- **`q⁻³` is bar-invariant only in the degenerate case.**  So no reading of it
as a state-attached factor escapes the asymmetry except at `q⁶ = 1`. -/
theorem inv_cube_bar_invariant_iff (q : K) (hq : q ≠ 0) :
    (q⁻¹) ^ (3 : ℕ) = q ^ (3 : ℕ) ↔ q ^ (6 : ℕ) = 1 := by
  rw [inv_pow]
  constructor
  · intro h
    have hc : q ^ 3 * (q ^ 3)⁻¹ = 1 := mul_inv_cancel₀ (pow_ne_zero 3 hq)
    rw [h] at hc
    calc q ^ 6 = q ^ 3 * q ^ 3 := by ring
      _ = 1 := hc
  · intro h
    have hc : q ^ 3 * q ^ 3 = 1 := by
      calc q ^ 3 * q ^ 3 = q ^ 6 := by ring
        _ = 1 := h
    exact inv_eq_of_mul_eq_one_right hc

end QOU.MassTheory.PoincareCentering
