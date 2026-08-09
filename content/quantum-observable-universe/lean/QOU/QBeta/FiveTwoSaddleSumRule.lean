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

/-! ### The real root's contribution is a ROGERS dilogarithm

Zagier's *The Dilogarithm Function* §II.1 A defines the Rogers dilogarithm on
`(0,1)` as

    L(x) = Li₂(x) + ½·log(x)·log(1 − x)

which takes its values most naturally in `ℝ/(π²/2)ℤ`. The 5₂ saddle's real
root contributes to the sum rule exactly

    Re V₃ = 3·L(y₃) − π²

— verified to 40 dps with difference `0.0`, and proved below. The whole content
is the branch relation `2·log y₃ = 3·log(1 − y₃)` (the real-root case `k = 0` of
`y² = (1−y)³`), which turns `Re Log(−y₃)² = log²y₃ − π²` into
`(3/2)·log y₃·log(1−y₃) − π²`, i.e. into Rogers' correction term.

**Why record it.** It identifies one of the three summands as a standard object
with a known functional-equation theory, rather than an ad-hoc combination. It
does **not** evaluate anything: `L(y₃)/(π²/6) = 0.441033…` is not rational, as
expected for a cubic-field argument, so no ladder value drops out. The sum rule
remains a statement about the *combination*, which is exactly what one expects
if only the Bloch-group class is well defined.

Stated with the dilogarithm value as a free real `L₂`, so the file stays
Mathlib-only: the identity is purely about the logarithmic terms. Bean
`qou-0yqu`. -/

/-- **The branch relation converts `Re Log(−y)²` into Rogers' correction.**

Given `2·log y = 3·log(1 − y)` — the real-root case of `y² = (1−y)³` — the
`Log²` term of `V` is `(3/2)·log y·log(1−y) − π²`. -/
theorem re_log_neg_sq_of_branch_relation {y : ℝ} (hy : 0 < y)
    (hrel : 2 * Real.log y = 3 * Real.log (1 - y)) :
    (Complex.log (-(y : ℂ)) ^ 2).re
      = 3 / 2 * (Real.log y * Real.log (1 - y)) - Real.pi ^ 2 := by
  rw [re_log_neg_sq_of_pos_real hy]
  linear_combination (Real.log y / 2) * hrel

/-- **`Re V₃ = 3·L(y₃) − π²`**, with `L` the Rogers dilogarithm.

`L₂` stands for `Li₂(y)`; the identity is about the logarithmic terms only, so
no dilogarithm theory is needed and this file stays Mathlib-only. -/
theorem re_V_real_root_eq_rogers {y L₂ : ℝ} (hy : 0 < y)
    (hrel : 2 * Real.log y = 3 * Real.log (1 - y)) :
    (3 * (L₂ : ℂ) + Complex.log (-(y : ℂ)) ^ 2).re
      = 3 * (L₂ + Real.log y * Real.log (1 - y) / 2) - Real.pi ^ 2 := by
  rw [Complex.add_re, re_log_neg_sq_of_branch_relation hy hrel]
  simp only [Complex.mul_re, Complex.ofReal_re, Complex.ofReal_im]
  norm_num
  ring

/-! ### §7d — the distribution (Kubert) route: the algebraic skeleton

The header records the identified route to the missing second equation as the
Kubert/distribution relation applied to `Li₂(y²) = Li₂((1−y)³)`, and says it is
"not formalized here". The **algebraic** half is formalized below, sorry-free;
the analytic half — a complex `Li₂` carrying the distribution identity —
remains open, and nothing here closes the sum rule.

The route runs through the **cube root**. If `u³ + u² = 1` then `y := u³`
solves the saddle cubic and `1 − y = u²`, so the single parameter `u` presents
`y` and its reflection *simultaneously*; the branch equation `y² = (1−y)³`
becomes `u⁶ = u⁶` (`branch_trivial_in_cubeRoot`). That is the reason to prefer
`u`, and it is why the distribution relation is the natural next input.

**A correction, recorded because the wrong version was drafted first.** An
earlier draft of this section claimed the distribution family is *vacuous* on
the Galois sum — that summing the relation over the orbit degenerates to
`A = A`, making the whole family a no-go. That claim is **false**. The reason
it is false is exactly `saddle_comp_cube_factor` and `reflected_comp_sq_factor`
below: `X⁹ − 2X⁶ + 3X³ − 1` and `X⁶ − X⁴ + 2X² − 1` are both **reducible**, so
the `Li`-sum over the nine (resp. six) numbers splits into sums over *smaller*
orbits instead of being one irreducibly new unknown. Both cubic factors
`X³ + X² − 1` and `X³ − X² + 1` have discriminant `−23` — the same field as
`y`. So the distribution relation is genuinely informative; what it is not is
*sufficient*, which is a different and much weaker statement.

Numerics for the split, to 60 dps, are in
`computations/probes/qbeta_5two_route40_distribution_factors_probe.py`.
Bean `qou-0yqu`.

**The 5₂ sum rule remains verified to 80 dps, unproved.** -/

/-- `u³ + u² = 1` gives `1 − u³ = u²`: the cube-root parameter presents the
saddle root `y = u³` and its reflection `1 − y` at once. -/
theorem one_sub_cube_of_cubeRoot {R : Type*} [CommRing R] {u : R}
    (hu : u ^ 3 + u ^ 2 - 1 = 0) : 1 - u ^ 3 = u ^ 2 := by
  linear_combination -hu

/-- **`y = u³` solves the saddle cubic.** The cofactor is the sextic factor of
`saddle_comp_cube_factor`, which is not a coincidence: it is the same
factorization seen from the other side. -/
theorem saddle_cubic_of_cubeRoot {R : Type*} [CommRing R] {u : R}
    (hu : u ^ 3 + u ^ 2 - 1 = 0) :
    (u ^ 3) ^ 3 - 2 * (u ^ 3) ^ 2 + 3 * u ^ 3 - 1 = 0 := by
  linear_combination (u ^ 6 - u ^ 5 + u ^ 4 - 2 * u ^ 3 + u ^ 2 + 1) * hu

/-- **`w = u²` solves `w³ − w² + 2w − 1`**, the minimal polynomial of `1 − y`. -/
theorem reflected_cubic_of_cubeRoot {R : Type*} [CommRing R] {u : R}
    (hu : u ^ 3 + u ^ 2 - 1 = 0) :
    (u ^ 2) ^ 3 - (u ^ 2) ^ 2 + 2 * u ^ 2 - 1 = 0 := by
  linear_combination (u ^ 3 - u ^ 2 + 1) * hu

/-- **`u⁵ = 1 − u`.** The reflection of the cube-root parameter is again a
power of it — the plastic-number identity `ρ⁻¹ + ρ⁻⁵ = 1`, where `u = ρ⁻¹`. -/
theorem pow_five_of_cubeRoot {R : Type*} [CommRing R] {u : R}
    (hu : u ^ 3 + u ^ 2 - 1 = 0) : u ^ 5 = 1 - u := by
  linear_combination (u ^ 2 - u + 1) * hu

/-- **The branch equation is trivial in the cube-root parameter.**

`y² = (1−y)³` — the content of `cubic_iff_sq_eq_cube`, and the source of every
branch subtlety in this file — collapses to `u⁶ = u⁶` once `y = u³`. -/
theorem branch_trivial_in_cubeRoot {R : Type*} [CommRing R] {u : R}
    (hu : u ^ 3 + u ^ 2 - 1 = 0) : (u ^ 3) ^ 2 = (1 - u ^ 3) ^ 3 := by
  rw [one_sub_cube_of_cubeRoot hu]; ring

/-- **`X⁹ − 2X⁶ + 3X³ − 1` is reducible.** The nine cube roots of the saddle
orbit are not a single new Galois orbit: they split as a cubic and a sextic.
This is what makes the distribution relation informative rather than vacuous. -/
theorem saddle_comp_cube_factor {R : Type*} [CommRing R] (X : R) :
    X ^ 9 - 2 * X ^ 6 + 3 * X ^ 3 - 1
      = (X ^ 3 + X ^ 2 - 1) * (X ^ 6 - X ^ 5 + X ^ 4 - 2 * X ^ 3 + X ^ 2 + 1) := by
  ring

/-- **`X⁶ − X⁴ + 2X² − 1` is reducible**, into *two* cubics — both of
discriminant `−23`, i.e. both generating the same field as `y`. -/
theorem reflected_comp_sq_factor {R : Type*} [CommRing R] (X : R) :
    X ^ 6 - X ^ 4 + 2 * X ^ 2 - 1 = (X ^ 3 - X ^ 2 + 1) * (X ^ 3 + X ^ 2 - 1) := by
  ring

/-- The two cubic factors of `reflected_comp_sq_factor` are exchanged by
`X ↦ −X`, so the second orbit is the negation of the first. -/
theorem cubeRoot_factor_neg {R : Type*} [CommRing R] (X : R) :
    X ^ 3 - X ^ 2 + 1 = -((-X) ^ 3 + (-X) ^ 2 - 1) := by ring

/-! The two factorizations again in **generating-polynomial** form. For a monic
`R` of degree `d` with roots `Xᵢ`, `∏ᵢ (1 − Xᵢ z) = z^d · R(1/z)`, which is the
coefficient list of `R` read low-to-high; this is the form in which the
identity `Σᵢ Li₂(Xᵢ) = −∫₀¹ log ∏ᵢ(1 − Xᵢ z) / z dz` transports a
factorization into a relation between `Li₂` sums. (Note the direction: the
highest-first coefficient list *is already* the generating polynomial
low-to-high — reversing it is the natural-looking error, and it is wrong.) -/

/-- Generating-polynomial form of `saddle_comp_cube_factor`. -/
theorem genPoly_saddle_comp_cube {R : Type*} [CommRing R] (z : R) :
    1 - 2 * z ^ 3 + 3 * z ^ 6 - z ^ 9
      = (1 + z - z ^ 3) * (1 - z + z ^ 2 - 2 * z ^ 3 + z ^ 4 + z ^ 6) := by
  ring

/-- Generating-polynomial form of `reflected_comp_sq_factor`. -/
theorem genPoly_reflected_comp_sq {R : Type*} [CommRing R] (z : R) :
    1 - z ^ 2 + 2 * z ^ 4 - z ^ 6 = (1 - z + z ^ 3) * (1 + z - z ^ 3) := by
  ring

/-- **The distribution relation, summed over the orbit.**

With `Li` abstract and carrying only the triplication identity
`Li (z³) = 3·(Li z + Li (ωz) + Li (ω²z))`, summing over the three cube-root
parameters gives `Σⱼ Li(yⱼ) = 3·S₉`, with `S₉` the `Li`-sum over the nine
numbers `ω^k uⱼ`.

On its own this is one equation in one new unknown, and that is all this
theorem says — it is deliberately as weak as its hypothesis. Its value is that
`saddle_comp_cube_factor` then splits `S₉` along a cubic and a sextic, so the
new unknown is not irreducibly new. Turning that split into a relation between
`Li₂` sums needs the analytic input this file does not have. -/
theorem sum_distribution_of_triplication
    (Li : ℂ → ℂ) (ω : ℂ) (u : Fin 3 → ℂ)
    (htrip : ∀ z : ℂ, Li (z ^ 3) = 3 * (Li z + Li (ω * z) + Li (ω ^ 2 * z))) :
    (∑ j, Li ((u j) ^ 3))
      = 3 * ∑ j, (Li (u j) + Li (ω * u j) + Li (ω ^ 2 * u j)) := by
  rw [Finset.mul_sum]
  exact Finset.sum_congr rfl fun j _ => htrip (u j)

/-- The same for duplication on `w = u²`, giving `Σⱼ Li(1 − yⱼ) = 2·S₆`. -/
theorem sum_distribution_of_duplication
    (Li : ℂ → ℂ) (u : Fin 3 → ℂ)
    (hdup : ∀ z : ℂ, Li (z ^ 2) = 2 * (Li z + Li (-z))) :
    (∑ j, Li ((u j) ^ 2)) = 2 * ∑ j, (Li (u j) + Li (-(u j))) := by
  rw [Finset.mul_sum]
  exact Finset.sum_congr rfl fun j _ => hdup (u j)

/-! ### §7e — the sum rule **is** a flattened-Rogers statement

Probes Routes 42–45 (`qou-xblo`) measured that the sum rule sits naturally in
the *extended* Bloch group rather than the ordinary one: `Σ_σ D(σ y) = 0`
identically, so the Bloch–Wigner regulator — the ordinary group's — is blind to
it, while the flattened Rogers dilogarithm

    R̂(z; p, q) = Li₂ z + ½·log z·log(1−z) − (πi/2)·(p·log(1−z) + q·log z)

gives `Σ_σ R̂(y_σ; ε_σ, 0) = −π²/6` at 60 dps, with `ε` the branch data that
`branch_data_of_cubic` above already proves integral.

⚠ **That numerical identity is NOT proved here and nothing below claims it.**
What *is* proved is the bridge: the corpus's `V`-form and the flattened form
differ by an **elementary** term, over an abstract `Li`, using only the branch
relation. So the two statements are equivalent, and a proof of either is a proof
of the other. That turns "they differ by an elementary term, verified to 50 dps"
into a theorem, and it is the whole of what knowing the new target buys in Lean
— the analytic content (a complex `Li₂`, the pentagon identity, `ℬ̂(ℂ)`) is
still absent from Mathlib and from this corpus. -/

/-- **The flattened Rogers dilogarithm**, with `Li` abstract.

`p` multiplies `log(1−z)` and `q` multiplies `log z`, matching Neumann's
convention and the probes. -/
noncomputable def flattenedRogers (Li : ℂ → ℂ) (z p q : ℂ) : ℂ :=
  Li z + Complex.log z * Complex.log (1 - z) / 2
    - ((Real.pi : ℂ) * I / 2) * (p * Complex.log (1 - z) + q * Complex.log z)

/-- **The V-form and the flattened form differ by an elementary term.**

For each root, given only the branch relation `2·log y − 3·log(1−y) = 2πi·ε`,

    3·Li(y) + (log y + b·πi)²
      = 3·R̂(y; ε, 0) + (3πi/2)·ε·log(1−y) + πi·(ε + 2b)·log y − π²·b²

with the correction built from logs and the branch integers alone — no
dilogarithm in it. The dilogarithm cancels identically; the content is the
`log²` bookkeeping that the branch relation controls. -/
theorem V_eq_three_flattenedRogers_add_elementary
    (Li : ℂ → ℂ) {y ε b : ℂ}
    (hbranch : 2 * Complex.log y - 3 * Complex.log (1 - y)
      = 2 * (Real.pi : ℂ) * I * ε) :
    3 * Li y + (Complex.log y + b * (Real.pi : ℂ) * I) ^ 2
      = 3 * flattenedRogers Li y ε 0
        + (3 * ((Real.pi : ℂ) * I / 2) * ε * Complex.log (1 - y)
          + (Real.pi : ℂ) * I * (ε + 2 * b) * Complex.log y
          - (Real.pi : ℂ) ^ 2 * b ^ 2) := by
  unfold flattenedRogers
  -- `ring` treats `I` as an opaque atom, so `(b·π·I)^2` never becomes `-b²π²`
  -- on its own; `Complex.I_sq` has to be supplied as a second relation.
  linear_combination (Complex.log y / 2) * hbranch
    + (b ^ 2 * (Real.pi : ℂ) ^ 2) * Complex.I_sq

/-- **The sum rule is equivalent to the flattened statement**, summed over the
three roots.

`Σ V(yⱼ) = 3·Σ R̂(yⱼ; εⱼ, 0) + (elementary)`. Since the correction contains no
`Li`, proving either side's value proves the other's — which is exactly why the
extended-Bloch reformulation is worth having rather than merely suggestive.

Still no instance: this is a bridge between two open statements, not a proof of
either. **The 5₂ sum rule remains verified to 80 dps, unproved.** -/
theorem sum_V_eq_three_sum_flattenedRogers
    (Li : ℂ → ℂ) (y ε b : Fin 3 → ℂ)
    (hbranch : ∀ j, 2 * Complex.log (y j) - 3 * Complex.log (1 - y j)
      = 2 * (Real.pi : ℂ) * I * ε j) :
    (∑ j, (3 * Li (y j) + (Complex.log (y j) + b j * (Real.pi : ℂ) * I) ^ 2))
      = 3 * (∑ j, flattenedRogers Li (y j) (ε j) 0)
        + ∑ j, (3 * ((Real.pi : ℂ) * I / 2) * ε j * Complex.log (1 - y j)
          + (Real.pi : ℂ) * I * (ε j + 2 * b j) * Complex.log (y j)
          - (Real.pi : ℂ) ^ 2 * (b j) ^ 2) := by
  have per := fun j =>
    V_eq_three_flattenedRogers_add_elementary Li (b := b j) (hbranch j)
  simp only [Fin.sum_univ_three]
  linear_combination per 0 + per 1 + per 2

end QOU.QBeta.FiveTwo
