/-
# `Im(q)` cannot supply the elliptic generator route 5 needs

Beans `qou-pdix` (route 5) / `qou-cds1` (branch 3). Sequel to
`QOU.QBeta.HolonomySpectrumSignObstruction`, which showed that a holonomy whose
generator has **real** spectrum has normalised character `cosh a ≥ 1`, while the
measured correction is strictly below 1 — so route 5 needs an **elliptic**
generator, and the imaginarity has to come from somewhere.

`conj:im-q-physical-role` is the corpus's name for that somewhere: *"a substrate
moduli parameter **not constrained by current QOU observables**, with three
candidate roles (chirality / phase coordinate / non-Hermitian deformation)."*
Two of those three are the ones that could bear on this. Both fail, and this file
proves the first.

## Route A — `Im(q) ≠ 0` as a phase coordinate

The Kohno–Drinfeld generator eigenvalues are `±ln q`. Purely imaginary would need
`|q| = 1`; but the substrate's `Re q = 1.10998 > 1`, so `|q|² = x² + y² > 1` for
**every** `y`. A purely elliptic generator is therefore impossible outright, and
the only remaining move is to allow a complex character and keep its real part.

That move is what `character_im_zero_iff` kills. Writing `q = x + iy`,

    Re[(q + q⁻¹)/2] = (x/2)(1 + 1/s)      Im[(q + q⁻¹)/2] = (y/2)(1 − 1/s),
    s := x² + y²

and `Q_β` is real, so the imaginary part must vanish. With `x > 1` we have `s > 1`
hence `1 − 1/s > 0`, so it vanishes **only** at `y = 0` — `q` real — and then the
real part is `(x + x⁻¹)/2 ≥ 1`, which
`HolonomySpectrumSignObstruction.kd_holonomy_cannot_realise_subunit_correction`
already excludes. `no_complex_q_gives_real_subunit_character` is that chain.

The measurement says the same thing quantitatively (probe
`qbeta-imq-elliptic-generator-refutation`): forcing `Re[character]` onto the
required `0.998399` needs `Im q = ±0.139956`, **12.61 %** of `Re q` — and leaves
`Im[character] = 0.014069`, which is **8.40×** the entire deviation being
explained and **18074 σ** on the measurement. Tuning the real part costs an
imaginary part an order of magnitude larger than the effect.

## Route B — a non-Hermitian deformation

An elliptic generator has spectrum `±iλ`, so the braiding eigenvalues
`exp(±iħλ/2)` lie on the **unit circle**. But Kohno–Drinfeld fixes the scale
precisely by matching the Hecke eigenvalues `{q, −q⁻¹}`, and for `q > 1` neither
has modulus 1 (`hecke_eigenvalues_not_unit_modulus`). So an elliptic generator and
the Hecke-matching that makes the construction Kohno–Drinfeld at all are mutually
exclusive at real `q`. Route B does not fail on the data — it fails by dissolving
the scale-fixing that the whole route depends on.

## What this does and does not settle

It does **not** refute `conj:im-q-physical-role`; the conjecture's chirality role
is untouched, and `Im q` may well be physical for other reasons. What it settles
is that `Im q` is **not** the source of the elliptic generator: the conjecture's
"phase coordinate" role cannot do this job, and its "non-Hermitian deformation"
role cannot do it without discarding the Drinfeld–Kohno matching.

Nor does it show no connection exists. It removes the one place the corpus had
already named as a candidate source of imaginarity, which is what a reader
following the trail from `HolonomySpectrumSignObstruction` would try next.

Scope-(b): structural exclusions citing proved inequalities. Nothing derived,
proposed, wired or readmitted.
-/
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity
import QOU.QBeta.HolonomySpectrumSignObstruction

namespace QOU.QBeta

/-- With `x > 1`, the modulus-squared `s = x² + y²` exceeds 1 whatever `y` is.
Hence `ln q` is never purely imaginary on the substrate branch, and a purely
elliptic Kohno–Drinfeld generator is impossible outright. -/
theorem abs_sq_gt_one {x y : ℝ} (hx : 1 < x) : 1 < x ^ 2 + y ^ 2 := by
  nlinarith [sq_nonneg y, sq_nonneg (x - 1)]

/-- **The character's imaginary part vanishes only for real `q`.** Writing
`q = x + iy`, `Im[(q + q⁻¹)/2] = (y/2)(1 − 1/s)` with `s = x² + y²`; for `x > 1`
we have `s > 1`, so the factor `1 − 1/s` is strictly positive and the product is
zero exactly when `y = 0`. -/
theorem character_im_zero_iff {x y : ℝ} (hx : 1 < x) :
    (y / 2) * (1 - 1 / (x ^ 2 + y ^ 2)) = 0 ↔ y = 0 := by
  have hs : 1 < x ^ 2 + y ^ 2 := abs_sq_gt_one hx
  have hs0 : (0 : ℝ) < x ^ 2 + y ^ 2 := lt_trans one_pos hs
  have hpos : 0 < 1 - 1 / (x ^ 2 + y ^ 2) := by
    have : 1 / (x ^ 2 + y ^ 2) < 1 := by
      rw [div_lt_one hs0]; exact hs
    linarith
  constructor
  · intro hEq
    rcases mul_eq_zero.mp hEq with h | h
    · linarith
    · exact absurd h (ne_of_gt hpos)
  · rintro rfl; simp

/-- **No complex `q` gives a real character below 1.** If the character is real —
which `Q_β` being real forces — then `q` is real, and the character is then
`(x + x⁻¹)/2 ≥ 1`. So allowing `Im q ≠ 0` and keeping the real part does not
rescue the holonomy reading; it only trades a wrong-sided real number for a
complex one. -/
theorem no_complex_q_gives_real_subunit_character {x y κ : ℝ} (hx : 1 < x)
    (hreal : (y / 2) * (1 - 1 / (x ^ 2 + y ^ 2)) = 0) (hκ : κ < 1) :
    κ ≠ (x / 2) * (1 + 1 / (x ^ 2 + y ^ 2)) := by
  have hy : y = 0 := (character_im_zero_iff hx).mp hreal
  subst hy
  have hx0 : 0 < x := lt_trans one_pos hx
  have hxne : x ≠ 0 := ne_of_gt hx0
  have hform : (x / 2) * (1 + 1 / (x ^ 2 + (0 : ℝ) ^ 2)) = (x + x⁻¹) / 2 := by
    field_simp
    ring
  rw [hform]
  exact kd_holonomy_cannot_realise_subunit_correction hx0 hκ

/-- **Route B dissolves the scale-fixing.** An elliptic generator forces
unit-modulus braiding eigenvalues, but Kohno–Drinfeld fixes `ħ = 2 ln q` by
matching the Hecke pair `{q, −q⁻¹}`, and for `q > 1` neither member has modulus
one. So a non-Hermitian deformation buys ellipticity at the cost of the matching
that made the construction Kohno–Drinfeld in the first place. -/
theorem hecke_eigenvalues_not_unit_modulus {q : ℝ} (hq : 1 < q) :
    q ≠ 1 ∧ |(-q⁻¹)| ≠ 1 := by
  refine ⟨ne_of_gt hq, ?_⟩
  have hq0 : 0 < q := lt_trans one_pos hq
  have hinv : |(-q⁻¹)| = q⁻¹ := by
    rw [abs_neg, abs_of_pos (inv_pos.mpr hq0)]
  rw [hinv]
  have : q⁻¹ < 1 := by
    rw [inv_lt_one_iff₀]; right; exact hq
  exact ne_of_lt this

end QOU.QBeta
