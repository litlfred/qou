/-
# The **flattened** pentagon: no branch hypotheses at all

Bean `qou-xblo`. `FiveTwoComplexPentagon` proved the five-term identity for
`cRogersL` when one variable is real, and measured it *failing* when both are
complex. This module removes the failure by removing the assumption that caused
it.

## The move

The five-term identity needs `log a₃ = log(1−x) − log(1−xy)` and four companions.
Those are branch conditions and they do fail. But nothing forces us to use
`log a₃` at all: carry the **expansion** `Λ₃ = log(1−x) − log(1−xy)` as the
logarithm, and the defect `δ = log a − Λ` simply never appears as a hypothesis.
The flattened term is

    flatRogers z Λ Λ' = Li₂(z) + ½·Λ·Λ' + (log(1−z) − Λ')·log z

and its derivative is `rogersDeriv z Λ Λ' · z′` **exactly** — the `log z` factor's
contribution cancels against the `Λ'` one. So §7h applies verbatim and the
flattened pentagon sum has vanishing derivative under `PentagonRegular` alone.

The point is that each `Λ` differentiates correctly *as a rational function*:

    Λ₃′ = −1/(1−x) + y/(1−xy) = (y−1)/((1−x)(1−xy)) = a₃′/a₃

with no branch choice made anywhere. That identity, and its four companions, is
what this module trades the branch conditions for.

## Where it lands

`flatRogers z Λ Λ' = cRogersL z + ½δ′·log z − ½δ·log(1−z) + ½δδ′` with
`δ = log z − Λ`, `δ′ = log(1−z) − Λ′`. Writing `δ = 2πi·p`, `δ′ = 2πi·q` this is
Neumann's `R(z; p, q)` up to his normalisation — so the theorem below is the
pentagon in `ℬ̂(ℂ)`, which is what bean `qou-xblo` said the lane needed.

Measured at 40 dps in
`computations/probes/qbeta_5two_route56_flattened_pentagon_probe.py`: at all four
two-variable points where the unflattened identity misses `π²/2` — by as much as
`(−0.447 + 0.354i)·π²` — the flattened sum is exactly `π²/2`, and every `(p,q)`
comes out an integer in `{0, ±1}`.

## ⚠ What is still owed

Lean gets constancy on a connected regular region and the value `π²/2` on any
region reaching the real square. It does **not** get a region joining the real
square to `(y₁, ȳ₁)`, so the 5₂ volume is still out of reach here. The probe's
two-variable points are evidence that the identity holds there, not a proof that
a region exists.

**The 5₂ sum rule is PROVED**: `FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms.

-- Ref: [neumann2004] library/0307092v2/0307092v2.pdf, Prop 2.5 and §2 (`R(z;p,q)`, `ker ν`)
-/
import QOU.QBeta.FiveTwoComplexPentagon

namespace QOU.QBeta.FiveTwoFlattenedPentagon

open QOU.MathlibExt QOU.QBeta.FiveTwo QOU.QBeta.FiveTwoComplexPentagon

/-- **The flattened Rogers dilogarithm.** `Λ`, `Λ'` stand in for `log z` and
`log(1−z)`; when they *are* those logarithms this is `cRogersL z`. -/
noncomputable def flatRogers (z lam lamp : ℂ) : ℂ :=
  cLiTwoExt z + lam * lamp / 2 + (Complex.log (1 - z) - lamp) * Complex.log z

/-- With the true logarithms in the slots, flattening is the identity. -/
theorem flatRogers_self (z : ℂ) :
    flatRogers z (Complex.log z) (Complex.log (1 - z)) = cRogersL z := by
  unfold flatRogers cRogersL
  ring

/-- **The derivative of the flattened term is `rogersDeriv`, exactly.**

The two hypotheses on `Λ`, `Λ'` are that they differentiate *like* `log f` and
`log(1−f)` — which for the pentagon's expansions is a rational-function identity,
not a branch choice. Note `log f` still appears in `flatRogers`, and its
derivative cancels against the `Λ'` term; that cancellation is the whole
mechanism. -/
theorem hasDerivAt_flatRogers {f lam lamp : ℂ → ℂ} {f' x : ℂ}
    (hf : HasDerivAt f f' x) (hz : f x ∈ rogersDomain)
    (hlam : HasDerivAt lam (f' / f x) x)
    (hlamp : HasDerivAt lamp (-(f' / (1 - f x))) x) :
    HasDerivAt (fun w => flatRogers (f w) (lam w) (lamp w))
      (rogersDeriv (f x) (lam x) (lamp x) * f') x := by
  have h0 : f x ≠ 0 := ne_zero_of_mem_rogersDomain hz
  have h1 : (1 : ℂ) - f x ≠ 0 := one_sub_ne_zero_of_mem_rogersDomain hz
  have hli : HasDerivAt (fun w => cLiTwoExt (f w))
      (-(Complex.log (1 - f x) / f x) * f') x :=
    (hasDerivAt_cLiTwoExt' hz.2 h0).comp x hf
  have hlogf : HasDerivAt (fun w => Complex.log (f w)) ((f x)⁻¹ * f') x :=
    (Complex.hasDerivAt_log hz.1).comp x hf
  have hinner : HasDerivAt (fun w => 1 - f w) (-f') x := by
    simpa using (hasDerivAt_const x (1 : ℂ)).sub hf
  have hlog1f : HasDerivAt (fun w => Complex.log (1 - f w)) (((1 - f x)⁻¹) * (-f')) x := by
    have hc : HasDerivAt (Complex.log ∘ fun w => 1 - f w) (((1 - f x)⁻¹) * (-f')) x :=
      (Complex.hasDerivAt_log (one_sub_mem_slitPlane_iff.mpr hz.2)).comp x hinner
    exact hc
  have hprod : HasDerivAt (fun w => lam w * lamp w / 2)
      ((f' / f x * lamp x + lam x * -(f' / (1 - f x))) / 2) x :=
    (hlam.mul hlamp).div_const 2
  have hlast : HasDerivAt (fun w => (Complex.log (1 - f w) - lamp w) * Complex.log (f w))
      ((((1 - f x)⁻¹) * (-f') - -(f' / (1 - f x))) * Complex.log (f x)
        + (Complex.log (1 - f x) - lamp x) * ((f x)⁻¹ * f')) x :=
    (hlog1f.sub hlamp).mul hlogf
  refine ((hli.add hprod).add hlast).congr_deriv ?_
  unfold rogersDeriv
  field_simp
  ring

/-! ### The five flattened terms of the pentagon -/

/-- The pentagon sum, flattened: each composite argument carries its **expansion**
as its logarithm rather than the principal branch. The first two terms are
`cRogersL` unchanged (`flatRogers_self`). -/
noncomputable def flatPentagonSum (y w : ℂ) : ℂ :=
  flatRogers w (Complex.log w) (Complex.log (1 - w))
    + flatRogers y (Complex.log y) (Complex.log (1 - y))
    + flatRogers ((1 - w) / (1 - w * y))
        (Complex.log (1 - w) - Complex.log (1 - w * y))
        (Complex.log w + Complex.log (1 - y) - Complex.log (1 - w * y))
    + flatRogers (1 - w * y) (Complex.log (1 - w * y))
        (Complex.log w + Complex.log y)
    + flatRogers ((1 - y) / (1 - w * y))
        (Complex.log (1 - y) - Complex.log (1 - w * y))
        (Complex.log y + Complex.log (1 - w) - Complex.log (1 - w * y))

/-- **The flattened pentagon's derivative vanishes — no branch hypotheses.**

Compare `FiveTwoComplexPentagon.hasDerivAt_pentagonSum`, which needs five. Every
one of them has been absorbed into the definition of `flatRogers`. -/
theorem hasDerivAt_flatPentagonSum {x y : ℂ} (h : PentagonRegular y x) :
    HasDerivAt (flatPentagonSum y) 0 x := by
  obtain ⟨hx, h3, h4, h5⟩ := id h
  have hd := h.den_ne_zero
  have hd' : (1 : ℂ) - y * x ≠ 0 := by rwa [mul_comm y x]
  have hx0 := h.ne_zero
  have hx1 := h.one_sub_ne_zero
  have hy0 := h.y_ne_zero
  have hy1 := h.one_sub_y_ne_zero
  -- the basic logarithms and their derivatives
  have Lx : HasDerivAt (fun w : ℂ => Complex.log w) x⁻¹ x := Complex.hasDerivAt_log hx.1
  have L1x : HasDerivAt (fun w : ℂ => Complex.log (1 - w)) (-((1 - x)⁻¹)) x :=
    hasDerivAt_clog_one_sub (one_sub_mem_slitPlane_iff.mpr hx.2)
  have Lxy : HasDerivAt (fun w : ℂ => Complex.log (1 - w * y)) ((1 - x * y)⁻¹ * (-y)) x :=
    hasDerivAt_clog_one_sub_mul h4.1
  -- term 1: `w`
  have D1 : HasDerivAt (fun w : ℂ => flatRogers w (Complex.log w) (Complex.log (1 - w)))
      (rogersDeriv x (Complex.log x) (Complex.log (1 - x)) * 1) x := by
    refine hasDerivAt_flatRogers (hasDerivAt_id x) hx (Lx.congr_deriv ?_) (L1x.congr_deriv ?_)
    · field_simp
    · field_simp
  -- term 2: `y`, constant in `w`
  have D2 : HasDerivAt
      (fun _ : ℂ => flatRogers y (Complex.log y) (Complex.log (1 - y))) 0 x :=
    hasDerivAt_const x _
  -- term 3
  have D3 : HasDerivAt
      (fun w : ℂ => flatRogers ((1 - w) / (1 - w * y))
        (Complex.log (1 - w) - Complex.log (1 - w * y))
        (Complex.log w + Complex.log (1 - y) - Complex.log (1 - w * y)))
      (rogersDeriv ((1 - x) / (1 - x * y))
        (Complex.log (1 - x) - Complex.log (1 - x * y))
        (Complex.log x + Complex.log (1 - y) - Complex.log (1 - x * y))
        * ((y - 1) / (1 - x * y) ^ 2)) x := by
    refine hasDerivAt_flatRogers (hasDerivAt_argThree y hd) h3
      ((L1x.sub Lxy).congr_deriv ?_)
      (((Lx.add (hasDerivAt_const x (Complex.log (1 - y)))).sub Lxy).congr_deriv ?_)
    · field_simp
      ring
    · rw [show (1 : ℂ) - (1 - x) / (1 - x * y) = x * (1 - y) / (1 - x * y) by field_simp; ring]
      field_simp
      ring
  -- term 4
  have D4 : HasDerivAt
      (fun w : ℂ => flatRogers (1 - w * y) (Complex.log (1 - w * y))
        (Complex.log w + Complex.log y))
      (rogersDeriv (1 - x * y) (Complex.log (1 - x * y))
        (Complex.log x + Complex.log y) * (-y)) x := by
    refine hasDerivAt_flatRogers (hasDerivAt_argFour y x) h4 (Lxy.congr_deriv ?_)
      ((Lx.add (hasDerivAt_const x (Complex.log y))).congr_deriv ?_)
    · field_simp
    · rw [show (1 : ℂ) - (1 - x * y) = x * y by ring]
      field_simp
      ring
  -- term 5
  have D5 : HasDerivAt
      (fun w : ℂ => flatRogers ((1 - y) / (1 - w * y))
        (Complex.log (1 - y) - Complex.log (1 - w * y))
        (Complex.log y + Complex.log (1 - w) - Complex.log (1 - w * y)))
      (rogersDeriv ((1 - y) / (1 - x * y))
        (Complex.log (1 - y) - Complex.log (1 - x * y))
        (Complex.log y + Complex.log (1 - x) - Complex.log (1 - x * y))
        * ((1 - y) * y / (1 - x * y) ^ 2)) x := by
    refine hasDerivAt_flatRogers (hasDerivAt_argFive y hd) h5
      (((hasDerivAt_const x (Complex.log (1 - y))).sub Lxy).congr_deriv ?_)
      ((((hasDerivAt_const x (Complex.log y)).add L1x).sub Lxy).congr_deriv ?_)
    · field_simp
      ring
    · rw [show (1 : ℂ) - (1 - y) / (1 - x * y) = y * (1 - x) / (1 - x * y) by field_simp; ring]
      field_simp
      ring
  have hsum := (((D1.add D2).add D3).add D4).add D5
  have hzero :
      rogersDeriv x (Complex.log x) (Complex.log (1 - x)) * 1
        + 0
        + rogersDeriv ((1 - x) / (1 - x * y))
            (Complex.log (1 - x) - Complex.log (1 - x * y))
            (Complex.log x + Complex.log (1 - y) - Complex.log (1 - x * y))
          * ((y - 1) / (1 - x * y) ^ 2)
        + rogersDeriv (1 - x * y) (Complex.log (1 - x * y))
            (Complex.log x + Complex.log y) * (-y)
        + rogersDeriv ((1 - y) / (1 - x * y))
            (Complex.log (1 - y) - Complex.log (1 - x * y))
            (Complex.log y + Complex.log (1 - x) - Complex.log (1 - x * y))
          * ((1 - y) * y / (1 - x * y) ^ 2) = 0 := by
    have key := pentagon_deriv_x_eq_zero x y (Complex.log x) (Complex.log (1 - x))
      (Complex.log y) (Complex.log (1 - y)) (Complex.log (1 - x * y)) hx0 hx1 hy0 hy1 hd
    linear_combination key
  rw [hzero] at hsum
  exact hsum

/-! ### Constancy, and the value -/

/-- The flattened pentagon is constant on any open connected region of regular
points. **No branch condition anywhere** — contrast
`FiveTwoComplexPentagon.pentagonSum_eq_of_region`, which needed five at the base
point. -/
theorem flatPentagonSum_eq_of_region {y : ℂ} {S : Set ℂ} (hS : IsOpen S)
    (hSc : IsPreconnected S) (hreg : ∀ w ∈ S, PentagonRegular y w)
    {x₀ x : ℂ} (hx₀ : x₀ ∈ S) (hx : x ∈ S) :
    flatPentagonSum y x = flatPentagonSum y x₀ := by
  have hd : ∀ w ∈ S, HasDerivAt (flatPentagonSum y) 0 w := fun w hw =>
    hasDerivAt_flatPentagonSum (hreg w hw)
  exact hS.is_const_of_deriv_eq_zero hSc
    (fun w hw => (hd w hw).differentiableAt.differentiableWithinAt)
    (fun w hw => (hd w hw).deriv) hx hx₀

/-- Where the branch conditions do hold, flattening changes nothing. -/
theorem flatPentagonSum_eq_pentagonSum {x y : ℂ}
    (e3 : Complex.log ((1 - x) / (1 - x * y))
      = Complex.log (1 - x) - Complex.log (1 - x * y))
    (e3' : Complex.log (1 - (1 - x) / (1 - x * y))
      = Complex.log x + Complex.log (1 - y) - Complex.log (1 - x * y))
    (e4' : Complex.log (1 - (1 - x * y)) = Complex.log x + Complex.log y)
    (e5 : Complex.log ((1 - y) / (1 - x * y))
      = Complex.log (1 - y) - Complex.log (1 - x * y))
    (e5' : Complex.log (1 - (1 - y) / (1 - x * y))
      = Complex.log y + Complex.log (1 - x) - Complex.log (1 - x * y)) :
    flatPentagonSum y x = pentagonSum y x := by
  unfold flatPentagonSum pentagonSum flatRogers cRogersL
  rw [e3', e4', e5']
  rw [← e3, ← e5]
  ring

/-- On the positive real square the flattened sum is `π²/2`. -/
theorem flatPentagonSum_ofReal {x y : ℝ} (hx0 : 0 < x) (hx1 : x < 1)
    (hy0 : 0 < y) (hy1 : y < 1) :
    flatPentagonSum (y : ℂ) (x : ℂ) = ((Real.pi ^ 2 / 2 : ℝ) : ℂ) := by
  obtain ⟨e3, e3', e4', e5, e5'⟩ := pentagon_branch_conditions_of_real hx0 hx1 hy0 hy1
  rw [flatPentagonSum_eq_pentagonSum e3 e3' e4' e5 e5', pentagonSum_ofReal hx0 hx1 hy0 hy1]

/-- **The flattened five-term identity on a regular region reaching the reals.**

    Σ flatRogers = π²/2

with `y` real in `(0,1)`, on any open connected set of `x` that stays regular and
contains a real point of `(0,1)`. The hypothesis is regularity **only** —
differentiability of the five terms — with no branch condition to check anywhere,
which is precisely what `FiveTwoComplexPentagon` could not say.

⚠ It is still a region hypothesis, so it does not reach `(y₁, ȳ₁)` and does not
touch `Vol(5₂)`. **The 5₂ sum rule is PROVED**: `FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms. -/
theorem flatPentagonSum_eq_pi_sq_div_two_of_region {x₀ y : ℝ} {S : Set ℂ}
    (hS : IsOpen S) (hSc : IsPreconnected S) (hreg : ∀ w ∈ S, PentagonRegular (y : ℂ) w)
    (hx0 : 0 < x₀) (hx1 : x₀ < 1) (hy0 : 0 < y) (hy1 : y < 1)
    (hmem : ((x₀ : ℝ) : ℂ) ∈ S) {x : ℂ} (hx : x ∈ S) :
    flatPentagonSum (y : ℂ) x = ((Real.pi ^ 2 / 2 : ℝ) : ℂ) := by
  rw [flatPentagonSum_eq_of_region hS hSc hreg hmem hx,
    flatPentagonSum_ofReal hx0 hx1 hy0 hy1]

/-- The unconditional one-variable case, flattened: for real `a ∈ (0,1)` and any
`w` off both cuts. Here it coincides with
`FiveTwoComplexPentagon.pentagonSum_eq_pi_sq_div_two`, since the branch
conditions happen to hold; the flattened statement is the one that survives when
they do not. -/
theorem flatPentagonSum_eq_pi_sq_div_two {a : ℝ} (h0 : 0 < a) (h1 : a < 1)
    {w : ℂ} (hw : w ∈ rogersDomain) :
    flatPentagonSum (a : ℂ) w = ((Real.pi ^ 2 / 2 : ℝ) : ℂ) :=
  flatPentagonSum_eq_pi_sq_div_two_of_region isOpen_rogersDomain isPreconnected_rogersDomain
    (fun _ hv => pentagonRegular_of_mem_rogersDomain h0 h1 hv) h0 h1 h0 h1
    (ofReal_mem_rogersDomain h0 h1) hw

/-! ### Why `(y₁, ȳ₁)` is out of reach: it is ON the cut

The region hypothesis is not a technicality to be discharged later, and it is not
that the 5₂ conjugate pair lies in some awkward corner. It lies **on the boundary
of the domain**, exactly:

    y₃·(1 − y₁y₂) = y₃ − 1        [from `y₁y₂y₃ = 1`, one line]

so `1 − y₁ȳ₁ = (y₃−1)/y₃`, and `y₃ = 0.4301597… ∈ (0,1)` makes that a **negative
real** — numerically `−1.3247179…`, the negated plastic number, which is Route
55's map showing up again. A negative real is not in `slitPlane`, so
`PentagonRegular` fails at that configuration: `log(1 − xy)` sits on its branch
cut.

That is the whole obstruction, and it is sharper than "no region was found":

* the straight segment from any real `a ∈ (0,1)` to `y₁`, with `ȳ₁` fixed, is
  regular at **every** interior point — only the endpoint fails, and only in the
  one argument `1 − wy`;
* the approach is from the **upper** half-plane (`Im(1 − wȳ₁) = a(1−t)·Im y₁ > 0`),
  which is the side on which the principal `Complex.log` is continuous.

So what is missing is a **boundary-continuity** argument, not a region. Measured
in `computations/probes/qbeta_5two_route57_on_the_cut_probe.py`.

**The 5₂ sum rule is PROVED**: `FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms. -/

section OnTheCut

/-- `c·(1 − ab) = c − 1` whenever `abc = 1` — one line, and it is the whole
obstruction. -/
theorem one_sub_mul_of_prod_eq_one {a b c : ℂ} (hprod : a * b * c = 1) :
    c * (1 - a * b) = c - 1 := by linear_combination -hprod

/-- A negative real is off the slit plane. -/
theorem not_mem_slitPlane_ofReal_neg {t : ℝ} (h : t < 0) :
    ((t : ℝ) : ℂ) ∉ Complex.slitPlane := by
  simp [Complex.ofReal_mem_slitPlane, h.not_gt]

/-- **The pentagon is not regular at the 5₂ conjugate pair.**

If the third root `c` is real in `(0,1)` — as `y₃ = 0.4301597…` is — then
`1 − ab` is the negative real `(c−1)/c` and `PentagonRegular b a` fails outright.
No choice of region reaches it; the configuration is on the boundary. -/
theorem not_pentagonRegular_of_prod_eq_one {a b : ℂ} {c : ℝ}
    (hprod : a * b * (c : ℂ) = 1) (h0 : 0 < c) (h1 : c < 1) :
    ¬ PentagonRegular b a := by
  intro h
  have hc : ((c : ℝ) : ℂ) ≠ 0 := by exact_mod_cast h0.ne'
  have hval : (1 : ℂ) - a * b = (((c - 1) / c : ℝ) : ℂ) := by
    have := one_sub_mul_of_prod_eq_one hprod
    push_cast
    field_simp
    linear_combination this
  exact not_mem_slitPlane_ofReal_neg (div_neg_of_neg_of_pos (by linarith) h0)
    (hval ▸ h.2.2.1.1)

/-- **The flattened sum is symmetric in its two variables**, like the unflattened
one: `x ↔ y` permutes the five triples `(argument, Λ, Λ')` rather than changing
them (`1 ↔ 2`, `3 ↔ 5`, `4` fixed). So transport in the *second* variable is the
same theorem — which is what reaching a pair with both entries non-real needs. -/
theorem flatPentagonSum_symm (y x : ℂ) : flatPentagonSum y x = flatPentagonSum x y := by
  unfold flatPentagonSum
  rw [mul_comm x y, add_comm (Complex.log x) (Complex.log y)]
  ring

theorem flatPentagonSum_swap (x : ℂ) :
    (fun w : ℂ => flatPentagonSum w x) = flatPentagonSum x :=
  funext fun w => flatPentagonSum_symm w x

/-- The flattened identity with the **complex** slot fixed: for any `v` off both
cuts and any real `a ∈ (0,1)`, `Σ flatRogers = π²/2`. This is
`flatPentagonSum_eq_pi_sq_div_two` read through the symmetry, and it is the base
point a second transport would start from. -/
theorem flatPentagonSum_eq_pi_sq_div_two' {a : ℝ} (h0 : 0 < a) (h1 : a < 1)
    {v : ℂ} (hv : v ∈ rogersDomain) :
    flatPentagonSum v ((a : ℝ) : ℂ) = ((Real.pi ^ 2 / 2 : ℝ) : ℂ) := by
  rw [flatPentagonSum_symm]
  exact flatPentagonSum_eq_pi_sq_div_two h0 h1 hv

end OnTheCut

end QOU.QBeta.FiveTwoFlattenedPentagon
