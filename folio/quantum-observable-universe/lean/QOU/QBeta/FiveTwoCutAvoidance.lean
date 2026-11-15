import Mathlib.Analysis.Complex.Basic
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Polyrith

/-!
# Cut avoidance on the transport arc — the hypothesis `hcont` consumes

Bean `qou-trns`. `QOU/Archimedean/BranchIntegerPinning.lean` reduces the 5₂
transport's branch integer to one open hypothesis: that

    F φ = Σⱼ Log(1 − e^{iφ}·yⱼ) − iφ

is continuous on `[0, π]`. `Log` is continuous off `(−∞, 0]`, so what that needs
is that no factor `1 − x·yⱼ` **crosses** the cut. Route 20 measured it. This file
**proves the arithmetic core of it**, and the proof turns out to need no complex
analysis at all.

## The observation that removes the complex analysis

On `|x| = 1` the GGM curve's three elementary symmetric functions are all **real**:

    e₁ = (x²+1)/x = x + 1/x = 2c,   e₂ = (x²+x+1)/x = 1 + 2c,   e₃ = 1

with `c = cos φ`. So on the arc the cubic in `y` is `Y³ − 2cY² + (1+2c)Y − 1`,
with **real coefficients** — `ggm_eq_reduced` and `add_inv_eq_two_re` below. The
5₂ polynomial `Y³ − 2Y² + 3Y − 1` is the `c = 1` member, and the Watson cubic's
negative `Y³ + 2Y² − Y − 1` is the `c = −1` member.

A factor `1 − x·y` lands on the cut exactly when `t := x·y` is real with `t ≥ 1`.
Write `y = t/x = t·(c − is)`, `s = sin φ`, substitute into the real cubic, and
split into real and imaginary parts. That is `hre` and `him` in `xy_neg` — two
real polynomial equations, and the question has become real algebra.

## The elimination

Dividing `him` by `s·t` (legitimate for `φ ∈ (0,π)`, and `t ≠ 0` because `e₃ = 1`)
and using `s² = 1 − c²` gives two polynomials in `(t, c)`; eliminating `c`,

    Res_c = 64 · t³ · (t − 1)⁴ · (t⁵ − t³ + 1)

`eliminant` below is that identity, verified by `linear_combination` with the
Bézout cofactors, so Lean checks the elimination rather than trusting a CAS.

Each factor dies:

* `t = 0` — then `hre` reads `−1 = 0`.
* `t = 1` — then the first equation forces `c = 0`, and the second reads `−1 = 0`.
* `t⁵ − t³ + 1 = 0` — **impossible for `t > 0`**: for `t ≤ 1` it is
  `t⁵ + (1 − t³) > 0`, and for `t > 1` it exceeds `1`. (Its minimum on `t > 0` is
  `0.814…`, at `t = √(3/5)`; the two-case split needs none of that.)

So `t < 0`, and the conclusion is stronger than required: on `φ ∈ (0,π)` a factor
`1 − x·yⱼ` is not merely off the cut, it is **greater than 1** whenever it is
real at all.

## The eliminant is sharp

`t⁵ − t³ + 1` has exactly one real root, `t = −1.2365057…`, and it is negative —
which is what makes the argument work. It is not a slack bound: that value is
**attained**. At `φ/π = 0.453289155972…`, where the conjugate pair satisfies
`φ + θ = π`, the product `x·y` is real and equals `−1.2365057…` to 40 dps
(Route 21, G5). So the quintic's one real root is exactly the one real value
`x·y` takes on the open arc, and the whole question of cut avoidance is the
question of that root's sign.

That gate is also the vacuity check. `xy_neg` is a no-solution theorem, and a
no-solution theorem whose hypotheses are unsatisfiable proves nothing; G5
exhibits a point where they hold.

## Scope — what this does and does not settle

Proved here: the real-algebraic core, for `φ ∈ (0, π)`, plus the base point
`φ = 0` (`base_point_root_lt_one`).

**Not** formalised here: the passage from "`F` is continuous" to "no factor meets
the cut" — that is `Log`'s continuity off `(−∞,0]` composed with continuity of
the root multiset, and it needs the complex-analytic packaging this file exists
to avoid. And the endpoint `φ = π` is genuinely on the cut
(`1 − x·y₁ = 1 − w₁ = −1.2469796…`); continuity there is one-sided and holds by
the sign of `Im(1 − x·y) = −y·sin φ > 0` for `y < 0`, not by cut avoidance. See
the header of `BranchIntegerPinning.lean`.

So `hcont` is not yet a theorem end to end. What was "measured, not proved" is
now "proved, except for the standard continuity packaging" — a different and much
smaller debt.

**The 5₂ sum rule is PROVED**: `QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms.
-/

namespace QOU.QBeta.FiveTwoCutAvoidance

/-! ### The reduction to a real cubic -/

/-- The GGM curve, divided by its leading coefficient. Off `x = 0` the roots in
`y` are exactly the roots of the monic cubic on the right. -/
theorem ggm_eq_reduced (x y : ℂ) (hx : x ≠ 0) :
    x * y ^ 3 - (x ^ 2 + 1) * y ^ 2 + (x ^ 2 + x + 1) * y - x
      = x * (y ^ 3 - (x + 1 / x) * y ^ 2 + (x + 1 + 1 / x) * y - 1) := by
  field_simp

/-- **On the unit circle the coefficients become real.** `x + 1/x = 2·Re x`, so
the monic cubic above is `Y³ − 2cY² + (1+2c)Y − 1` with `c = Re x = cos φ`. -/
theorem add_inv_eq_two_re {x : ℂ} (hx : ‖x‖ = 1) : x + 1 / x = (2 * x.re : ℝ) := by
  rw [one_div, Complex.inv_eq_conj hx, Complex.add_conj]

/-! ### The two special values of `c` this lane already knows -/

/-- At `c = 1` (the base point `x = 1`) the reduced cubic is the 5₂ polynomial. -/
theorem reduced_at_one (y : ℝ) :
    y ^ 3 - 2 * 1 * y ^ 2 + (1 + 2 * 1) * y - 1 = y ^ 3 - 2 * y ^ 2 + 3 * y - 1 := by ring

/-- At `c = −1` (the endpoint `x = −1`) it is the negative of the Watson cubic
`w³ − 2w² − w + 1` under `y ↦ −w` — which is why the endpoint factor is `1 − w₁`. -/
theorem reduced_at_neg_one (w : ℝ) :
    (-w) ^ 3 - 2 * (-1) * (-w) ^ 2 + (1 + 2 * (-1)) * (-w) - 1
      = -(w ^ 3 - 2 * w ^ 2 - w + 1) := by ring

/-! ### The elimination -/

/-- **The eliminant.** The two real equations force
`t³ (t−1)⁴ (t⁵ − t³ + 1) = 0`.

`linear_combination` checks the Bézout identity, so the resultant computation is
verified here rather than imported from a CAS. -/
theorem eliminant {t c : ℝ}
    (hI : -4 * c ^ 2 * t ^ 2 + 4 * c ^ 2 * t - 2 * c + t ^ 2 - 1 = 0)
    (hII : 4 * c ^ 3 * t ^ 3 - 4 * c ^ 3 * t ^ 2 + 2 * c ^ 2 * t - 3 * c * t ^ 3
             + 2 * c * t ^ 2 + c * t - 1 = 0) :
    t ^ 3 * (t - 1) ^ 4 * (t ^ 5 - t ^ 3 + 1) = 0 := by
  linear_combination (-t ^ 4 * (t - 1) ^ 4 * (2 * c ^ 2 * t ^ 2 + c - t ^ 2)) * hI
    + (-t ^ 3 * (t - 1) ^ 4 * (2 * c * t ^ 2 + 1)) * hII

/-- **The quintic is positive on `t > 0`.** Two cases, neither needing its
minimum: for `t ≤ 1` it is `t⁵ + (1 − t³)`, and for `t > 1` it exceeds `1`. -/
theorem quintic_pos {t : ℝ} (ht : 0 < t) : 0 < t ^ 5 - t ^ 3 + 1 := by
  rcases le_or_gt t 1 with h | h
  · -- `t⁵ + (1 − t³)`, both parts nonnegative and the first strictly positive
    have h1 : t ^ 3 ≤ 1 := pow_le_one₀ ht.le h
    linarith [pow_pos ht 5]
  · -- `t³·(t² − 1) > 0`, so the quintic exceeds `1`
    have h3 : (0:ℝ) < t ^ 3 := pow_pos ht 3
    have h2 : (0:ℝ) < t ^ 2 - 1 := by nlinarith
    nlinarith [mul_pos h3 h2]

/-! ### The theorem -/

/-- **No factor reaches the cut on `0 < φ < π`.**

`hre` and `him` are the real and imaginary parts of `P(y) = 0` for
`P(Y) = Y³ − 2cY² + (1+2c)Y − 1` at `y = t·(c − is)` — that is, at the root whose
product with `x = c + is` is the real number `t`. Given `s ≠ 0` and `c² + s² = 1`,
the conclusion is `t < 0`.

Since the factor in question is `1 − x·y = 1 − t`, this says it is `> 1`: not
merely off `(−∞, 0]` but bounded away from it. The same statement covers
`1 − y/x` by `s ↦ −s`, which the hypotheses are invariant under. -/
theorem xy_neg {t c s : ℝ} (hs : s ≠ 0) (hcs : c ^ 2 + s ^ 2 = 1)
    (hre : c ^ 3 * t ^ 3 - 2 * c ^ 3 * t ^ 2 + 2 * c ^ 2 * t - 3 * c * s ^ 2 * t ^ 3
             + 2 * c * s ^ 2 * t ^ 2 + c * t - 1 = 0)
    (him : s * t * (-3 * c ^ 2 * t ^ 2 + 4 * c ^ 2 * t - 2 * c + s ^ 2 * t ^ 2 - 1) = 0) :
    t < 0 := by
  -- `e₃ = 1` forbids a zero root, and here that is visible directly in `hre`
  have ht0 : t ≠ 0 := by
    rintro rfl
    norm_num at hre
  -- eliminate `s²` using `s² = 1 − c²`
  have hs2 : s ^ 2 = 1 - c ^ 2 := by linarith
  have hII : 4 * c ^ 3 * t ^ 3 - 4 * c ^ 3 * t ^ 2 + 2 * c ^ 2 * t - 3 * c * t ^ 3
      + 2 * c * t ^ 2 + c * t - 1 = 0 := by
    rw [hs2] at hre; linarith [hre]
  have hI : -4 * c ^ 2 * t ^ 2 + 4 * c ^ 2 * t - 2 * c + t ^ 2 - 1 = 0 := by
    have h := him
    rw [hs2] at h
    have hst : s * t ≠ 0 := mul_ne_zero hs ht0
    rcases mul_eq_zero.mp h with h' | h'
    · exact absurd h' hst
    · linarith [h']
  -- the eliminant, and the three ways it can vanish
  have hkey := eliminant hI hII
  by_contra hle
  push_neg at hle          -- `0 ≤ t`, and `t ≠ 0`, so `0 < t`
  have htpos : 0 < t := lt_of_le_of_ne hle (Ne.symm ht0)
  have h5 : t ^ 5 - t ^ 3 + 1 ≠ 0 := ne_of_gt (quintic_pos htpos)
  have h3 : t ^ 3 ≠ 0 := pow_ne_zero _ ht0
  -- so `(t−1)⁴ = 0`, i.e. `t = 1`
  have ht1 : t = 1 := by
    rcases mul_eq_zero.mp hkey with h | h
    · rcases mul_eq_zero.mp h with h' | h'
      · exact absurd h' h3
      · have : t - 1 = 0 := by
          have := pow_eq_zero_iff (n := 4) (by norm_num) |>.mp h'
          exact this
        linarith
    · exact absurd h h5
  -- and `t = 1` forces `c = 0` in the first equation, which the second refutes
  subst ht1
  have hc : c = 0 := by linarith [hI]
  subst hc
  norm_num at hII

/-- **The base point.** At `φ = 0` the reduced cubic is the 5₂ polynomial, whose
real root is `< 1`; so `1 − x·y = 1 − y > 0` there too.

`u = y − 1` turns it into `u³ + u² + 2u + 1`, which is `≥ 1` for `u ≥ 0`. -/
theorem base_point_root_lt_one {y : ℝ} (hy : y ^ 3 - 2 * y ^ 2 + 3 * y - 1 = 0) : y < 1 := by
  by_contra h
  push_neg at h
  nlinarith [sq_nonneg (y - 1), pow_nonneg (by linarith : (0:ℝ) ≤ y - 1) 3]

end QOU.QBeta.FiveTwoCutAvoidance
