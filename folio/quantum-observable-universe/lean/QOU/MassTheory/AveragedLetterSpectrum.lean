/-
# The averaged letter is `[2]_q/2` times an involution — and that pins `Q = 1`

`atom_braid_word_3A` builds `2A+1` **averaged** letters `(σ + σ⁻¹)/2`. Using the
Hecke quadratic, `σ` has eigenvalues `q` and `−q⁻¹`, so `σ⁻¹ = σ − h` with
`h = q − q⁻¹` and the averaged letter is `σ − h/2`.

This file proves the two algebraic facts the diagnosis rests on:

1. **Its eigenvalues are `±[2]_q/2`** — symmetric about zero, so the averaged
   letter is `[2]_q/2` times an **involution**, *not* a braid generator (whose
   eigenvalues `q, −q⁻¹` are not negatives of one another for `q ≠ 1`).
2. **A scaled generator with a second parameter matches only at `Q = 1`.** The
   type-`B` extra generator satisfies `(T₀ − Q)(T₀ + Q⁻¹) = 0`, so `c·T₀` has
   eigenvalues `cQ, −cQ⁻¹`. Demanding these equal `±[2]_q/2` forces `Q² = 1`,
   and with `Q > 0`, `Q = 1` and `c = [2]_q/2`.

## Why this is worth proving, and what it does NOT establish

It is the load-bearing algebraic step of the diagnosis: the averaged letter
leaves the braid group because it is a scaled *involution*, and `σ ↦ σ⁻¹` is the
**bar involution**, so the construction is hand-rolling a bar-symmetrization —
which AGENTS.md §7b says not to do.

**It is about the COLOUR-BLIND template only (scope added 2026-08-26).** The
producer emits two non-braid templates, and the canonical one
(`pn_convention="bring_color_weighted"`, owner ruling R3) is the *unequal*-weight
`(1/2 + δ/4)σ + (1/2 − δ/4)σ⁻¹`. Its eigenvalues are **not** negatives of one
another, so `Q = 1` does **not** apply to it: measured, that letter gives
`Q = 1.0000715145…`, departing at leading order `(δ/4)h/c`
(`computations/meson/atom_letter_colour_spectrum_probe.py`). Every theorem below
is stated for a general weight and is unaffected — `averagedOn` fixes `w₊ = 1/2`
by taking `lam - heckeH q / 2`, and `second_parameter_forced` carries the
symmetric spectrum `±t` as an explicit hypothesis. What needs the scope is the
*reading*: "the averaged letter forces `Q = 1`" is true of the symmetric letter
and false of the colour-weighted one. See
`docs/audits/2026-08-25-vol-trm-division-of-labour-is-sound.md` §13.

**It does NOT establish that the atom word can be written in a type-`B` algebra.**
That prescription was measured to be unrealizable and is withdrawn: the averaged
letters sit at `2A+1` **distinct** generator indices, while type `Bₙ` has exactly
one distinguished generator. See
`docs/audits/2026-08-25-vol-trm-division-of-labour-is-sound.md` §11b. The match
proved here is **per letter, spectral**, and nothing more.

**Base ring (§7c).** Everything here is generic `[Field K] [CharZero K]` with
no archimedean construct. The one statement needing an order —
`second_parameter_is_one`, which upgrades `Q² = 1` to `Q = 1` — lives in
`AveragedLetterSpectrumOrdered.lean` so this file stays order-free.

`-- Ref: [leitner2026] docs/audits/2026-08-25-vol-trm-division-of-labour-is-sound.md`
-/
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.CharZero.Defs
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

namespace QOU.MassTheory

variable {K : Type*} [Field K] [CharZero K]

/-- `h = q − q⁻¹`, the Hecke deformation parameter. -/
noncomputable def heckeH (q : K) : K := q - q⁻¹

/-- `[2]_q = q + q⁻¹`. -/
noncomputable def qTwo (q : K) : K := q + q⁻¹

/-- The averaged letter `(σ + σ⁻¹)/2 = σ − h/2`, evaluated on an eigenvalue of
`σ`.  `CharZero` is genuinely needed: the halving is not available in
characteristic two. -/
noncomputable def averagedOn (q lam : K) : K := lam - heckeH q / 2

/-- On the `+q` eigenvalue the averaged letter takes the value `[2]_q/2`. -/
theorem averagedOn_pos (q : K) (hq : q ≠ 0) :
    averagedOn q q = qTwo q / 2 := by
  unfold averagedOn heckeH qTwo
  field_simp
  ring

/-- On the `−q⁻¹` eigenvalue it takes `−[2]_q/2`.  With the previous lemma this
is the whole point: the two values are **negatives of one another**, so the
averaged letter is `[2]_q/2` times an involution. -/
theorem averagedOn_neg (q : K) (hq : q ≠ 0) :
    averagedOn q (-q⁻¹) = -(qTwo q / 2) := by
  unfold averagedOn heckeH qTwo
  field_simp
  ring

/-- **The averaged letter squares to the scalar `([2]_q/2)²`** on each Hecke
eigenvalue — "it is a scaled involution", in eigenvalue form. -/
theorem averagedOn_sq (q : K) (hq : q ≠ 0) :
    averagedOn q q ^ 2 = (qTwo q / 2) ^ 2 ∧
    averagedOn q (-q⁻¹) ^ 2 = (qTwo q / 2) ^ 2 := by
  refine ⟨by rw [averagedOn_pos q hq], ?_⟩
  rw [averagedOn_neg q hq]; ring

omit [CharZero K] in
/-- A braid generator is **not** of this form: its eigenvalues `q` and `−q⁻¹` are
negatives of one another only when `q² = 1`.  This is precisely what the averaged
letter gives up in exchange for being an involution. -/
theorem hecke_eigenvalues_not_symmetric (q : K) (hq : q ≠ 0)
    (hsym : (-q⁻¹ : K) = -q) : q ^ 2 = 1 := by
  have h1 : q⁻¹ = q := neg_inj.mp hsym
  have h2 : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  rw [h1] at h2
  rw [sq]; exact h2

omit [CharZero K] in
/-- **The second parameter is forced.**  If a scaled generator `c·T₀`, with `T₀`
satisfying `(T₀ − Q)(T₀ + Q⁻¹) = 0` so that `c·T₀` has eigenvalues `cQ` and
`−cQ⁻¹`, is to carry the averaged letter's spectrum `±t`, then `Q² = 1`. -/
theorem second_parameter_forced (Q c t : K) (hQ : Q ≠ 0) (ht : t ≠ 0)
    (hpos : c * Q = t) (hneg : -(c * Q⁻¹) = -t) : Q ^ 2 = 1 := by
  have hinv : c * Q⁻¹ = t := neg_inj.mp hneg
  have hcne : c ≠ 0 := by
    intro h
    rw [h, zero_mul] at hpos
    exact ht hpos.symm
  have heq : c * Q = c * Q⁻¹ := by rw [hpos, hinv]
  have hQQ : Q = Q⁻¹ := mul_left_cancel₀ hcne heq
  have h2 : Q * Q⁻¹ = 1 := mul_inv_cancel₀ hQ
  rw [← hQQ] at h2
  rw [sq]; exact h2

end QOU.MassTheory
