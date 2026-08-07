/-
# The 5₂ saddle sum rule — algebraic skeleton and the reflection reduction

Numerics (`computations/probes/qbeta_5two_saddle_sum_rule_and_provenance_probe.py`,
merged 2026-08-02) established to 80 dps that the three 5₂ saddle values satisfy

    Σⱼ Re(Vⱼ) = −3π²/2                                              (SUM)

with `Vⱼ = 3·Li₂(yⱼ) + (log yⱼ + bⱼ·πi)²` and `yⱼ` the roots of
`y³ − 2y² + 3y − 1`. That is strong evidence, **not a proof**.

## What this file does and does not prove

Mathlib carries **no polylogarithm** (no `Polylog`, no `dilog` — checked
2026-08-03). **QOU, however, has its own** (correction 2026-08-03; an earlier
revision of this header mentioned only the Mathlib gap, which read as "no
dilogarithm exists" and is misleading):

* `QOU.QPochhammer.LiTwo : ℝ → ℝ`, the series `∑' k, x^(k+1)/(k+1)²`;
* `QOU.Archimedean.LiTwo_reflection'` — **sorry-free** — the Euler reflection
  `LiTwo x + LiTwo (1−x) = π²/6 − log x · log(1−x)` for `0 < x < 1`, together
  with the derivative infra Mathlib lacks.

That is exactly the hypothesis `sum_reflection_of_branch` takes, so the
abstract `Li` below is *instantiable today for real arguments in `(0,1)`* —
which covers the real saddle root `y₃ = 0.4301597…`. It does **not** cover
`y₁, y₂` (complex, and `|y₁| = 1.52 > 1`), so (SUM) still cannot be discharged.
The missing piece is a complex `Li₂` with the complex reflection identity;
tracked as bean `qou-ph1k`.

Keeping `Li` abstract here is therefore deliberate: it makes the reduction
independent of which dilogarithm implementation eventually supplies the
hypothesis. This file:

* proves the **algebraic skeleton** sorry-free and over a generic `CommRing`
  (`cubic_iff_sq_eq_cube`);
* proves the **reflection reduction** sorry-free, with `Li` an *abstract*
  function carrying the reflection identity as an explicit hypothesis
  (`sum_reflection_of_branch`) — this is the analytic step of the paper
  derivation, and it is genuine content, not a placeholder;
* proves the two **bookkeeping consequences** that the prose asserts —
  that `π²/2` is the *unique* centering shift (`centering_constant_unique`)
  and that `V₃` is *determined* by `V₁` (`V_two_of_sum_rule`);
* records (SUM) itself as a **content-bearing conjecture carrier with no
  instance** (`FiveTwoSaddleSumRule`), which is the honest representation of
  an open statement.

The genuinely open input is isolated in `FiveTwoDilogLadder`: one further
relation between `Σ Li₂(yⱼ)` and `Σ Li₂(1−yⱼ)`. `sum_reflection_of_branch`
supplies one equation in those two unknowns; a second is needed, and the
identified route (Kubert/distribution relation on `Li₂(y²) = Li₂((1−y)³)`)
is not formalized here.

-- Ref: [manuscript] docs/coordination/1ppq-qbeta.md, 2026-08-02 row
-- Ref: [garoufalidis2020] https://arxiv.org/abs/2012.00062 eq (233)–(234)
-/
import Mathlib.Analysis.SpecialFunctions.Complex.Log
import Mathlib.Algebra.BigOperators.Fin

namespace QOU.QBeta.FiveTwo

open Complex

/-! ### Algebraic skeleton (generic commutative ring, §7c) -/

/-- The 5₂ saddle cubic **is** the branch equation `y² = (1−y)³`.

Both forms appear in the sources — GGM eq (233) at `x = 1` writes
`y² = (1−y)³`, GGMW eq (184) writes `(1−ξ)³ = ξ²`, and the corpus carries
`y³ − 2y² + 3y − 1`. They are the same equation, over any commutative ring:
no positivity, ordering, or archimedean structure is used. -/
theorem cubic_iff_sq_eq_cube {R : Type*} [CommRing R] (y : R) :
    y ^ 3 - 2 * y ^ 2 + 3 * y - 1 = 0 ↔ y ^ 2 = (1 - y) ^ 3 := by
  constructor <;> intro h <;> linear_combination h

/-! ### The branch data is a THEOREM, not an assumption

`sum_reflection_of_branch` below takes the branch relation
`2·log yⱼ − 3·log(1−yⱼ) = 2πi·εⱼ` as a hypothesis. It need not be assumed:
it follows from the cubic alone, with no dilogarithm involved. -/

/-- `exp (2·log y − 3·log(1−y)) = 1` whenever `y² = (1−y)³`.

The exponential collapses the logarithms back to `y²/(1−y)³`, which the cubic
makes `1`. No branch choice is made here — that is the point. -/
theorem exp_branch_eq_one {y : ℂ} (hy : y ≠ 0) (hy1 : (1 : ℂ) - y ≠ 0)
    (h : y ^ 2 = (1 - y) ^ 3) :
    Complex.exp (2 * Complex.log y - 3 * Complex.log (1 - y)) = 1 := by
  have e1 : Complex.exp (2 * Complex.log y) = y ^ 2 := by
    rw [show (2 : ℂ) * Complex.log y = Complex.log y + Complex.log y by ring,
      Complex.exp_add, Complex.exp_log hy]
    ring
  have e2 : Complex.exp (3 * Complex.log (1 - y)) = (1 - y) ^ 3 := by
    rw [show (3 : ℂ) * Complex.log (1 - y)
        = Complex.log (1 - y) + Complex.log (1 - y) + Complex.log (1 - y) by ring,
      Complex.exp_add, Complex.exp_add, Complex.exp_log hy1]
    ring
  rw [Complex.exp_sub, e1, e2, h]
  exact div_self (pow_ne_zero 3 hy1)

/-- **The branch data of the 5₂ cubic, derived.**

Every root of `y² = (1−y)³` satisfies `2·log y − 3·log(1−y) = k·(2πi)` for some
integer `k`. Numerically `k = (+1, −1, 0)` at the three 5₂ roots, and this is
the sole source of the `π²` in the sum rule.

This discharges the `hbranch` hypothesis of `sum_reflection_of_branch` from the
cubic alone — no dilogarithm, no analytic input. -/
theorem branch_data_of_cubic {y : ℂ} (hy : y ≠ 0) (hy1 : (1 : ℂ) - y ≠ 0)
    (h : y ^ 2 = (1 - y) ^ 3) :
    ∃ k : ℤ, 2 * Complex.log y - 3 * Complex.log (1 - y)
      = k * (2 * (Real.pi : ℂ) * I) := by
  have hexp := exp_branch_eq_one hy hy1 h
  rwa [Complex.exp_eq_one_iff] at hexp

/-! ### The reflection reduction

The analytic content of the partial derivation. `Li` is abstract: the only
thing assumed about it is the reflection identity, so this theorem is exactly
as strong as that identity and no stronger. -/

/-- **Summing the dilogarithm reflection identity over the three roots.**

Given the reflection identity `Li z + Li (1−z) = π²/6 − log z · log(1−z)` and
the branch data of the cubic — `2·log yⱼ − 3·log(1−yⱼ) = 2πi·εⱼ`, which is
what `y² = (1−y)³` gives after taking logarithms — the `Li` values at `1−yⱼ`
are eliminated in favour of log-squares:

    Σ Li(yⱼ) + Σ Li(1−yⱼ)
      = π²/2 − (2/3)·Σ(log yⱼ)² + (2πi/3)·Σ εⱼ·log yⱼ

This is **one equation in the two unknowns** `Σ Li(yⱼ)` and `Σ Li(1−yⱼ)`. It
does not close the sum rule; see `FiveTwoDilogLadder`. -/
theorem sum_reflection_of_branch
    (Li : ℂ → ℂ) (y ε : Fin 3 → ℂ)
    (hrefl : ∀ z : ℂ, Li z + Li (1 - z)
      = (Real.pi : ℂ) ^ 2 / 6 - Complex.log z * Complex.log (1 - z))
    (hbranch : ∀ j, 2 * Complex.log (y j) - 3 * Complex.log (1 - y j)
      = 2 * (Real.pi : ℂ) * I * ε j) :
    (∑ j, Li (y j)) + (∑ j, Li (1 - y j))
      = (Real.pi : ℂ) ^ 2 / 2 - (2 / 3) * ∑ j, Complex.log (y j) ^ 2
        + (2 * (Real.pi : ℂ) * I / 3) * ∑ j, ε j * Complex.log (y j) := by
  have per : ∀ j, Li (y j) + Li (1 - y j)
      = (Real.pi : ℂ) ^ 2 / 6 - (2 / 3) * Complex.log (y j) ^ 2
        + (2 * (Real.pi : ℂ) * I / 3) * (ε j * Complex.log (y j)) := by
    intro j
    have hk : Complex.log (1 - y j)
        = (2 * Complex.log (y j) - 2 * (Real.pi : ℂ) * I * ε j) / 3 := by
      linear_combination (-1 / 3 : ℂ) * hbranch j
    rw [hrefl (y j), hk]; ring
  simp only [Fin.sum_univ_three]
  linear_combination per 0 + per 1 + per 2

/-! ### Bookkeeping consequences of the sum rule

Easy algebra — recorded because they are the two claims the prose makes, and
a claim worth asserting is worth checking. -/

/-- **`π²/2` is the *unique* shift that centers the saddle values.**

Given the sum rule, `Σⱼ (Vⱼ + c) = 0` holds for exactly one `c`, namely
`π²/2`. So the corpus's "extraction convention" — long treated as an
unexplained fudge absorbed by a fit — is forced, not chosen. -/
theorem centering_constant_unique (V : Fin 3 → ℝ) (c : ℝ)
    (hsum : ∑ j, V j = -3 * (Real.pi ^ 2 / 2)) :
    (∑ j, (V j + c)) = 0 ↔ c = Real.pi ^ 2 / 2 := by
  simp only [Fin.sum_univ_three] at hsum ⊢
  constructor <;> intro h <;> linarith

/-- **`V₃` is determined by `V₁`.**

With `V₂ = conj V₁` (hence equal real parts), the sum rule forces
`V₃ = −2·V₁ − 3π²/2`. Consequently `V₃` never needs to be carried as an
independent numerical literal — which is what let the corpus keep a wrong
one (`−2.7580990292`) unnoticed for months. -/
theorem V_two_of_sum_rule (V : Fin 3 → ℝ)
    (hsum : ∑ j, V j = -3 * (Real.pi ^ 2 / 2)) (hconj : V 1 = V 0) :
    V 2 = -2 * V 0 - 3 * (Real.pi ^ 2 / 2) := by
  simp only [Fin.sum_univ_three] at hsum
  linarith

/-! ### The open statements

Both carriers below are **primary conjectures**: their signatures take no
other conjecture class as a hypothesis. Neither is given an instance, which
is the honest representation of "numerically verified, not proved". -/

/-- **CONJECTURE (verified to 80 dps, unproved).** The 5₂ saddle sum rule.

`Vⱼ = 3·Li₂(yⱼ) + (log yⱼ + bⱼπi)²` over the three roots of the saddle cubic
satisfies `Σⱼ Re Vⱼ = −3π²/2`.

Numerical status: residual `3.4e-80` at 80 dps, and **specific to the 5₂
cubic** — five control cubics of the same shape, four sharing the `Πy = 1`
constraint, miss the target by 0.16 to 2.83. So this is an arithmetic
property of the 5₂ saddle cubic, not branch bookkeeping.

No instance is provided: the statement is open. -/
class FiveTwoSaddleSumRule (Li : ℂ → ℂ) (y b : Fin 3 → ℂ) : Prop where
  /-- `Σⱼ Re Vⱼ = −3π²/2`. -/
  sum_re_eq :
    (∑ j, (3 * Li (y j) + (Complex.log (y j) + b j * (Real.pi : ℂ) * I) ^ 2)).re
      = -3 * (Real.pi ^ 2 / 2)

/-- **CONJECTURE (unproved).** The missing second relation.

`sum_reflection_of_branch` gives one equation in `A = Σ Li₂(yⱼ)` and
`B = Σ Li₂(1−yⱼ)`. Numerically `A ≈ 0.9717306815` and `B ≈ 0.3514640301`,
neither with an evident closed form, so a second independent relation is
required to close the sum rule.

The identified route is the Kubert/distribution relation
`Li₂(zⁿ) = n·Σ_{k<n} Li₂(ζₙᵏ z)` applied to `Li₂(y²) = Li₂((1−y)³)`, which
supplies one at the cost of cube-root-of-unity arguments `ω(1−y)`. That
Bloch-group computation is not formalized here.

Stated as a linear dependence between the two sums with coefficients
`α, β, γ` to be identified; no instance is provided. -/
class FiveTwoDilogLadder (Li : ℂ → ℂ) (y : Fin 3 → ℂ) : Prop where
  /-- Some nontrivial linear relation over ℚ between `Σ Li(yⱼ)`,
  `Σ Li(1−yⱼ)` and `π²`, independent of the reflection identity. -/
  ladder : ∃ α β γ : ℚ, (α, β) ≠ (0, 0) ∧
    (α : ℂ) * (∑ j, Li (y j)) + (β : ℂ) * (∑ j, Li (1 - y j))
      = (γ : ℂ) * (Real.pi : ℂ) ^ 2

/-! ### The branch data `b = (−1, +1, +1)` is not free data

The sum rule is stated with `Vⱼ = 3·Li₂(yⱼ) + (log yⱼ + bⱼπi)²` and a
hand-supplied `b = (−1, +1, +1)`, which reads like three fitted signs. It is
not: probe `qbeta_5two_route5_branch_data_probe` (gate G6, error `0.0` at
60 dps) found

    log yⱼ + bⱼπi = Log(−yⱼ)      (principal branch)

and the three lemmas below are the proof. `arg(−z) = arg z − π` above the real
axis, `arg z + π` below it, and `= π` on the positive real axis — so for a
cubic with one positive real root and one conjugate pair, `b` is *forced* to be
`(−1, +1, +1)` with no freedom whatsoever.

Consequence: `Vⱼ = 3·Li₂(yⱼ) + Log(−yⱼ)²`, and `Log(−z)²` is precisely the term
in the dilogarithm inversion formula `Li₂ z + Li₂ (1/z) = −π²/6 − ½·Log(−z)²`.
That is what makes the inversion route to the sum rule natural rather than
opportunistic. See bean `qou-0yqu`.
-/

/-- Above the real axis, negation *subtracts* `πi` from the principal log. -/
theorem log_neg_of_im_pos {z : ℂ} (hz : 0 < z.im) :
    Complex.log (-z) = Complex.log z - (Real.pi : ℂ) * Complex.I := by
  simp only [Complex.log, norm_neg, Complex.arg_neg_eq_arg_sub_pi_of_im_pos hz]
  push_cast
  ring

/-- Below the real axis, negation *adds* `πi`. -/
theorem log_neg_of_im_neg {z : ℂ} (hz : z.im < 0) :
    Complex.log (-z) = Complex.log z + (Real.pi : ℂ) * Complex.I := by
  simp only [Complex.log, norm_neg, Complex.arg_neg_eq_arg_add_pi_of_im_neg hz]
  push_cast
  ring

/-- On the positive real axis, negation adds `πi` (`arg` of a negative real is
`π`, not `−π`: the principal branch is closed from above). -/
theorem log_neg_of_pos_real {x : ℝ} (hx : 0 < x) :
    Complex.log (-(x : ℂ)) = Complex.log (x : ℂ) + (Real.pi : ℂ) * Complex.I := by
  have hneg : ((-x : ℝ) : ℂ) = -(x : ℂ) := by push_cast; ring
  rw [← hneg]
  simp only [Complex.log, Complex.norm_real, Complex.arg_ofReal_of_neg (by linarith : (-x : ℝ) < 0),
    Complex.arg_ofReal_of_nonneg hx.le]
  rw [norm_neg]
  push_cast
  ring

/-- **The three branch shifts at once.** For a positive real `y₃` and a
conjugate pair `y₁` (upper half-plane), `y₂ = conj y₁`, the shifts
`(−1, +1, +1)` are exactly `Log(−yⱼ)`.

This is the formal statement that the sum rule's `b` carries no free
parameters. -/
theorem branch_shift_eq_log_neg {y₁ y₃ : ℂ} (h₁ : 0 < y₁.im) (h₃im : y₃.im = 0)
    (h₃re : 0 < y₃.re) :
    Complex.log y₁ + (-1 : ℤ) * (Real.pi : ℂ) * Complex.I = Complex.log (-y₁)
      ∧ Complex.log (starRingEnd ℂ y₁) + (1 : ℤ) * (Real.pi : ℂ) * Complex.I
          = Complex.log (-(starRingEnd ℂ y₁))
      ∧ Complex.log y₃ + (1 : ℤ) * (Real.pi : ℂ) * Complex.I = Complex.log (-y₃) := by
  refine ⟨?_, ?_, ?_⟩
  · rw [log_neg_of_im_pos h₁]; push_cast; ring
  · rw [log_neg_of_im_neg (by simpa using h₁)]; push_cast; ring
  · have hy₃ : y₃ = ((y₃.re : ℝ) : ℂ) := by
      apply Complex.ext <;> simp [h₃im]
    rw [hy₃, log_neg_of_pos_real h₃re]
    push_cast
    ring

/-! ### The `Log²` half of the sum rule, in closed form

With `b` identified as `Log(−yⱼ)` the sum rule reads
`Σⱼ Re(3·Li₂(yⱼ) + Log(−yⱼ)²) = −3π²/2`, which splits into a dilogarithm part
and a pure `Log²` part. **The `Log²` part is elementary** — it is what this
block evaluates — so the whole content of the sum rule sits in the
dilogarithm part.

For a positive real root `y₃` and a conjugate pair `y₁`, `y₂ = conj y₁` with
`‖y₁‖² · y₃ = 1` (Vieta `e₃ = 1`, see `real_root_mul_normSq`):

    Σⱼ Re Log(−yⱼ)² = (3/2)·log²y₃ − 2(θ − π)² − π²,     θ = arg y₁.

Subtracting from `−3π²/2` gives the Route 5 closed form for the integral,

    −∫₀¹ log(1 − 2z + 3z² − z³)/z dz = −½·log²y₃ + (2/3)(θ − π)² − π²/6

exactly as recorded in bean `qou-0yqu`. So Route 5's restatement is a
*consequence* of the sum rule and this algebra — the two are equivalent given
`Σⱼ Re Li₂(yⱼ) = −∫₀¹ log P(z)/z dz`, which is the one link still open.
-/

/-- `Re(Log(−z)²)` above the real axis. -/
theorem re_log_neg_sq_of_im_pos {z : ℂ} (hz : 0 < z.im) :
    (Complex.log (-z) ^ 2).re
      = Real.log ‖z‖ ^ 2 - (Complex.arg z - Real.pi) ^ 2 := by
  have hre : (Complex.log (-z)).re = Real.log ‖z‖ := by
    rw [Complex.log_re, norm_neg]
  have him : (Complex.log (-z)).im = Complex.arg z - Real.pi := by
    rw [Complex.log_im, Complex.arg_neg_eq_arg_sub_pi_of_im_pos hz]
  rw [pow_two, Complex.mul_re, hre, him]
  ring

/-- `Re(Log(−z)²)` below the real axis. -/
theorem re_log_neg_sq_of_im_neg {z : ℂ} (hz : z.im < 0) :
    (Complex.log (-z) ^ 2).re
      = Real.log ‖z‖ ^ 2 - (Complex.arg z + Real.pi) ^ 2 := by
  have hre : (Complex.log (-z)).re = Real.log ‖z‖ := by
    rw [Complex.log_re, norm_neg]
  have him : (Complex.log (-z)).im = Complex.arg z + Real.pi := by
    rw [Complex.log_im, Complex.arg_neg_eq_arg_add_pi_of_im_neg hz]
  rw [pow_two, Complex.mul_re, hre, him]
  ring

/-- `Re(Log(−x)²)` on the positive real axis. -/
theorem re_log_neg_sq_of_pos_real {x : ℝ} (hx : 0 < x) :
    (Complex.log (-(x : ℂ)) ^ 2).re = Real.log x ^ 2 - Real.pi ^ 2 := by
  have hcast : (-(x : ℂ)) = ((-x : ℝ) : ℂ) := by push_cast; ring
  have hre : (Complex.log (-(x : ℂ))).re = Real.log x := by
    rw [Complex.log_re, norm_neg, Complex.norm_real, Real.norm_eq_abs, abs_of_pos hx]
  have him : (Complex.log (-(x : ℂ))).im = Real.pi := by
    rw [Complex.log_im, hcast, Complex.arg_ofReal_of_neg (by linarith : (-x : ℝ) < 0)]
  rw [pow_two, Complex.mul_re, hre, him]
  ring

/-- The conjugate of an upper-half-plane point contributes the *same*
`Re Log(−·)²`: `arg(conj z) = −arg z` there, and `(−θ + π)² = (θ − π)²`. -/
theorem re_log_neg_sq_conj_of_im_pos {z : ℂ} (hz : 0 < z.im) :
    (Complex.log (-(starRingEnd ℂ z)) ^ 2).re
      = Real.log ‖z‖ ^ 2 - (Complex.arg z - Real.pi) ^ 2 := by
  have harg : Complex.arg (starRingEnd ℂ z) = -Complex.arg z := by
    rw [Complex.arg_conj, if_neg]
    intro h
    exact absurd (Complex.arg_eq_pi_iff.mp h).2 (ne_of_gt hz)
  rw [re_log_neg_sq_of_im_neg (by simpa using hz), harg, RCLike.norm_conj]
  ring

/-- **The `Log²` half of the sum rule, evaluated.**

For the 5₂ saddle root configuration — one positive real root `y₃`, one
conjugate pair `y₁`, `conj y₁` — with the Vieta relation `‖y₁‖² · y₃ = 1`:

    Σⱼ Re Log(−yⱼ)² = (3/2)·log²y₃ − 2(θ − π)² − π²,   θ = arg y₁.

The hypothesis `hnorm` is exactly `real_root_mul_normSq` rearranged; it is what
eliminates `‖y₁‖` in favour of the single real algebraic number `y₃`. -/
theorem sum_re_log_neg_sq {y₁ : ℂ} {y₃ : ℝ} (h₁ : 0 < y₁.im) (h₃ : 0 < y₃)
    (hnorm : ‖y₁‖ ^ 2 * y₃ = 1) :
    (Complex.log (-y₁) ^ 2).re + (Complex.log (-(starRingEnd ℂ y₁)) ^ 2).re
        + (Complex.log (-(y₃ : ℂ)) ^ 2).re
      = 3 / 2 * Real.log y₃ ^ 2 - 2 * (Complex.arg y₁ - Real.pi) ^ 2
        - Real.pi ^ 2 := by
  have hy₁ : y₁ ≠ 0 := fun h => absurd (by rw [h]; simp : y₁.im = 0) (ne_of_gt h₁)
  have hnormpos : 0 < ‖y₁‖ := norm_pos_iff.mpr hy₁
  -- `‖y₁‖² = 1/y₃` gives `2·log‖y₁‖ = −log y₃`
  have hlog : 2 * Real.log ‖y₁‖ = -Real.log y₃ := by
    have hsq : ‖y₁‖ ^ 2 = y₃⁻¹ := by
      field_simp at hnorm ⊢
      linarith [hnorm]
    have := congrArg Real.log hsq
    rwa [Real.log_pow, Real.log_inv] at this
  have hlog' : Real.log ‖y₁‖ ^ 2 = Real.log y₃ ^ 2 / 4 := by
    have hL : Real.log ‖y₁‖ = -Real.log y₃ / 2 := by linarith
    rw [hL]; ring
  rw [re_log_neg_sq_of_im_pos h₁, re_log_neg_sq_conj_of_im_pos h₁,
    re_log_neg_sq_of_pos_real h₃, hlog']
  ring

end QOU.QBeta.FiveTwo
