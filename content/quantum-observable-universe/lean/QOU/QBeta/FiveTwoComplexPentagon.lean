/-
# The complex pentagon — and the 5₂ saddle sum rule

Bean `qou-xblo`. This module carries the 5₂ lane's analytic input from
"absent from Mathlib" to a **proof of the sum rule**.

## The two headline theorems

`fiveTwo_saddle_sum_rule` — there are three roots of `X³ − 2X² + 3X − 1`, one
real in `(0,1)` and a conjugate pair, and

    Σ Li₂(yⱼ) = −π²/6 − ½·log²y₃ + (2/3)·(arg y₁ − π)²

`fiveTwoSaddleSumRule_holds` — the same, in the form of the corpus's own
conjecture class `QOU.QBeta.FiveTwo.FiveTwoSaddleSumRule`, which is declared
there with **no instance** and the comment "the statement is open". With
`Vⱼ = 3·Li₂(yⱼ) + (log yⱼ + bⱼπi)²` and `b = (−1,+1,+1)`,

    Σⱼ Vⱼ = −3π²/2 + 2π·log(y₃)·i        so    Σⱼ Re Vⱼ = −3π²/2

Both sorry-free, axioms `[propext, Classical.choice, Quot.sound]`.

## The chain

1. **The five-term identity on `ℂ`.** `pentagonSum_eq_pi_sq_div_two`: for every
   real `a ∈ (0,1)` and every `w` off both real cuts,
   `L(a) + L(w) + L((1−a)/(1−aw)) + L(1−aw) + L((1−w)/(1−aw)) = π²/2`, with
   `L = cRogersL`. The derivative vanishes by §7h's algebra; the branch defects
   are holomorphic with vanishing derivative, so they travel from a real base
   point; and for real `a` the whole of `rogersDomain` is regular.
2. **The anharmonic group on `cRogersL`.** Reflection (`cRogersL_add_one_sub`),
   inversion (`MathlibExt.cRogersL_add_inv`), and the four one-log forms — the
   `log²` terms cancel completely, leaving `π²` plus `π` times one logarithm.
3. **The branch equations.** `y² = (1−y)³` *is* the cubic, so
   `exp(2 log y − 3 log(1−y)) = 1`; a `4π`-wide window pins `ε = (+1,−1,0)`.
4. **The root data.** `SaddleRoots` bundles the cubic's root structure and is
   inhabited (`ofRealRoot`, from the intermediate value theorem and an explicit
   square root); everything else is derived from it.

## What is *not* claimed

The 5₂ **volume** conjecture is untouched. `Vol(5₂) = 3·D(y₁)` involves the
Bloch–Wigner `D`, which cancels on Galois sums (see the bean) — nothing here
speaks to it.

-- Ref: [neumann2004] library/0307092v2/0307092v2.pdf, Prop 2.5 and §2
-- Ref: [neumann2004] library/0307092v2/0307092v2.pdf, Prop 2.5
-/
import QOU.MathlibExt.ComplexRogersDilog
import QOU.QBeta.FiveTwoSaddleSumRule
import QOU.QBeta.FiveTwoAbelFiveTerm

namespace QOU.QBeta.FiveTwoComplexPentagon

open QOU.MathlibExt QOU.QBeta.FiveTwo

/-! ### The three composite arguments and their derivatives

§7h took the chain-rule factors `1`, `0`, `(y−1)/(1−xy)²`, `−y`,
`(1−y)·y/(1−xy)²` as given. Here they are proved. -/

/-- `a₄(w) = 1 − wy`, derivative `−y`. -/
theorem hasDerivAt_argFour (y x : ℂ) :
    HasDerivAt (fun w : ℂ => 1 - w * y) (-y) x := by
  simpa using (hasDerivAt_const x (1 : ℂ)).sub ((hasDerivAt_id x).mul_const y)

/-- `a₃(w) = (1−w)/(1−wy)`, derivative `(y−1)/(1−xy)²`. -/
theorem hasDerivAt_argThree (y : ℂ) {x : ℂ} (hxy : (1 : ℂ) - x * y ≠ 0) :
    HasDerivAt (fun w : ℂ => (1 - w) / (1 - w * y)) ((y - 1) / (1 - x * y) ^ 2) x := by
  have hnum : HasDerivAt (fun w : ℂ => 1 - w) (-1) x := by
    simpa using (hasDerivAt_const x (1 : ℂ)).sub (hasDerivAt_id x)
  have h := hnum.div (hasDerivAt_argFour y x) hxy
  convert h using 1
  field_simp
  ring

/-- `a₅(w) = (1−y)/(1−wy)`, derivative `(1−y)·y/(1−xy)²`. -/
theorem hasDerivAt_argFive (y : ℂ) {x : ℂ} (hxy : (1 : ℂ) - x * y ≠ 0) :
    HasDerivAt (fun w : ℂ => (1 - y) / (1 - w * y)) ((1 - y) * y / (1 - x * y) ^ 2) x := by
  have h := (hasDerivAt_const x ((1 : ℂ) - y)).div (hasDerivAt_argFour y x) hxy
  convert h using 1
  field_simp
  ring

/-! ### The pentagon sum, and its vanishing derivative -/

/-- The five-term sum, as a function of the differentiation variable. -/
noncomputable def pentagonSum (y w : ℂ) : ℂ :=
  cRogersL w + cRogersL y + cRogersL ((1 - w) / (1 - w * y))
    + cRogersL (1 - w * y) + cRogersL ((1 - y) / (1 - w * y))

/-- **The complex pentagon's `x`-derivative vanishes.**

The analytic content of §7h. The four `rogersDomain` hypotheses are what makes
each term differentiable; the five `e…` hypotheses are the branch conditions,
and they are exactly the unproved input — see
`pentagon_branch_conditions_of_real` for a region where they hold. -/
theorem hasDerivAt_pentagonSum {x y : ℂ}
    (hx : x ∈ rogersDomain) (hxy : (1 : ℂ) - x * y ≠ 0)
    (h3 : (1 - x) / (1 - x * y) ∈ rogersDomain)
    (h4 : (1 : ℂ) - x * y ∈ rogersDomain)
    (h5 : (1 - y) / (1 - x * y) ∈ rogersDomain)
    (e3 : Complex.log ((1 - x) / (1 - x * y))
      = Complex.log (1 - x) - Complex.log (1 - x * y))
    (e3' : Complex.log (1 - (1 - x) / (1 - x * y))
      = Complex.log x + Complex.log (1 - y) - Complex.log (1 - x * y))
    (e4' : Complex.log (1 - (1 - x * y)) = Complex.log x + Complex.log y)
    (e5 : Complex.log ((1 - y) / (1 - x * y))
      = Complex.log (1 - y) - Complex.log (1 - x * y))
    (e5' : Complex.log (1 - (1 - y) / (1 - x * y))
      = Complex.log y + Complex.log (1 - x) - Complex.log (1 - x * y)) :
    HasDerivAt (pentagonSum y) 0 x := by
  -- every non-vanishing condition §7h needs is already inside the domain data
  have hx0 : x ≠ 0 := ne_zero_of_mem_rogersDomain hx
  have hx1 : (1 : ℂ) - x ≠ 0 := one_sub_ne_zero_of_mem_rogersDomain hx
  have hxy0 : x * y ≠ 0 := by
    have h := one_sub_ne_zero_of_mem_rogersDomain h4
    simpa using h
  have hy0 : y ≠ 0 := fun h => hxy0 (by simp [h])
  have hy1 : (1 : ℂ) - y ≠ 0 := fun h =>
    ne_zero_of_mem_rogersDomain h5 (by rw [h]; simp)
  -- the five differentiations
  have D1 : HasDerivAt (fun w : ℂ => cRogersL w)
      (rogersDeriv x (Complex.log x) (Complex.log (1 - x)) * 1) x := by
    have h := hasDerivAt_cRogersL_comp (hasDerivAt_id x) hx
    simpa only [rogersDeriv, id] using h
  have D2 : HasDerivAt (fun _ : ℂ => cRogersL y) 0 x := hasDerivAt_const x _
  have D3 : HasDerivAt (fun w : ℂ => cRogersL ((1 - w) / (1 - w * y)))
      (rogersDeriv ((1 - x) / (1 - x * y))
          (Complex.log (1 - x) - Complex.log (1 - x * y))
          (Complex.log x + Complex.log (1 - y) - Complex.log (1 - x * y))
        * ((y - 1) / (1 - x * y) ^ 2)) x := by
    have h := hasDerivAt_cRogersL_comp (hasDerivAt_argThree y hxy) h3
    rw [e3, e3'] at h
    simpa only [rogersDeriv] using h
  have D4 : HasDerivAt (fun w : ℂ => cRogersL (1 - w * y))
      (rogersDeriv (1 - x * y) (Complex.log (1 - x * y))
        (Complex.log x + Complex.log y) * (-y)) x := by
    have h := hasDerivAt_cRogersL_comp (hasDerivAt_argFour y x) h4
    rw [e4'] at h
    simpa only [rogersDeriv] using h
  have D5 : HasDerivAt (fun w : ℂ => cRogersL ((1 - y) / (1 - w * y)))
      (rogersDeriv ((1 - y) / (1 - x * y))
          (Complex.log (1 - y) - Complex.log (1 - x * y))
          (Complex.log y + Complex.log (1 - x) - Complex.log (1 - x * y))
        * ((1 - y) * y / (1 - x * y) ^ 2)) x := by
    have h := hasDerivAt_cRogersL_comp (hasDerivAt_argFive y hxy) h5
    rw [e5, e5'] at h
    simpa only [rogersDeriv] using h
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
      (Complex.log y) (Complex.log (1 - y)) (Complex.log (1 - x * y)) hx0 hx1 hy0 hy1 hxy
    linear_combination key
  rw [hzero] at hsum
  exact hsum

/-! ### The hypotheses are satisfiable: the positive real square

`hasDerivAt_pentagonSum` would be worth nothing if its ten hypotheses could not
hold together — a contradictory hypothesis set proves anything. They all hold on
`0 < x, y < 1`, where every pentagon argument is a positive real in `(0,1)` and
every logarithm is the cast of a real one. That is also the base region for the
continuation that is still owed.

⚠ It is **only** a non-vacuity check plus a base region. The real five-term
identity on `(0,1)` is already proved elsewhere
(`FiveTwoAbelFiveTerm.rogersL_fiveTerm`); what the 5₂ lane needs is the complex
one, off this square, and nothing here reaches it. -/

section RealSquare

variable {x y : ℝ}

/-- The pentagon's arguments, as reals in `(0,1)`, on the positive real square. -/
theorem pentagon_args_mem_Ioo (hx0 : 0 < x) (hx1 : x < 1) (hy0 : 0 < y) (hy1 : y < 1) :
    x * y < 1 ∧ 0 < 1 - x * y ∧ 1 - x * y < 1
      ∧ 0 < (1 - x) / (1 - x * y) ∧ (1 - x) / (1 - x * y) < 1
      ∧ 0 < (1 - y) / (1 - x * y) ∧ (1 - y) / (1 - x * y) < 1 := by
  have hxy : x * y < 1 := by nlinarith
  have hd : (0 : ℝ) < 1 - x * y := by linarith
  refine ⟨hxy, hd, by nlinarith, div_pos (by linarith) hd, ?_,
    div_pos (by linarith) hd, ?_⟩
  · rw [div_lt_one hd]; nlinarith [mul_pos hx0 (sub_pos.mpr hy1)]
  · rw [div_lt_one hd]; nlinarith [mul_pos hy0 (sub_pos.mpr hx1)]

/-- **The five branch conditions hold on the positive real square.**

Each side is the cast of a real logarithm of a positive real, so the expansions
are `Real.log_mul` and `Real.log_div` and no branch is chosen. This is what makes
`hasDerivAt_pentagonSum` non-vacuous. -/
theorem pentagon_branch_conditions_of_real
    (hx0 : 0 < x) (hx1 : x < 1) (hy0 : 0 < y) (hy1 : y < 1) :
    Complex.log (((1 : ℂ) - (x : ℂ)) / (1 - (x : ℂ) * (y : ℂ)))
        = Complex.log ((1 : ℂ) - (x : ℂ)) - Complex.log (1 - (x : ℂ) * (y : ℂ))
      ∧ Complex.log (1 - ((1 : ℂ) - (x : ℂ)) / (1 - (x : ℂ) * (y : ℂ)))
        = Complex.log (x : ℂ) + Complex.log ((1 : ℂ) - (y : ℂ))
          - Complex.log (1 - (x : ℂ) * (y : ℂ))
      ∧ Complex.log (1 - ((1 : ℂ) - (x : ℂ) * (y : ℂ)))
        = Complex.log (x : ℂ) + Complex.log (y : ℂ)
      ∧ Complex.log (((1 : ℂ) - (y : ℂ)) / (1 - (x : ℂ) * (y : ℂ)))
        = Complex.log ((1 : ℂ) - (y : ℂ)) - Complex.log (1 - (x : ℂ) * (y : ℂ))
      ∧ Complex.log (1 - ((1 : ℂ) - (y : ℂ)) / (1 - (x : ℂ) * (y : ℂ)))
        = Complex.log (y : ℂ) + Complex.log ((1 : ℂ) - (x : ℂ))
          - Complex.log (1 - (x : ℂ) * (y : ℂ)) := by
  obtain ⟨hxy, hd, -, h3p, -, h5p, -⟩ := pentagon_args_mem_Ioo hx0 hx1 hy0 hy1
  have h1x : (0 : ℝ) < 1 - x := by linarith
  have h1y : (0 : ℝ) < 1 - y := by linarith
  have hdC : (1 : ℂ) - (x : ℂ) * (y : ℂ) ≠ 0 := by
    rw [show (1 : ℂ) - (x : ℂ) * (y : ℂ) = ((1 - x * y : ℝ) : ℂ) by push_cast; ring]
    exact_mod_cast hd.ne'
  -- the three casts of `x`, `1−x`, `1−y`, `1−xy` and the two composite arguments
  have cx : ((x : ℝ) : ℂ) = ((x : ℝ) : ℂ) := rfl
  have cA : (1 : ℂ) - (x : ℂ) = ((1 - x : ℝ) : ℂ) := by push_cast; ring
  have cB : (1 : ℂ) - (y : ℂ) = ((1 - y : ℝ) : ℂ) := by push_cast; ring
  have cD : (1 : ℂ) - (x : ℂ) * (y : ℂ) = ((1 - x * y : ℝ) : ℂ) := by push_cast; ring
  have c3 : ((1 : ℂ) - (x : ℂ)) / (1 - (x : ℂ) * (y : ℂ))
      = (((1 - x) / (1 - x * y) : ℝ) : ℂ) := by push_cast; ring
  have c5 : ((1 : ℂ) - (y : ℂ)) / (1 - (x : ℂ) * (y : ℂ))
      = (((1 - y) / (1 - x * y) : ℝ) : ℂ) := by push_cast; ring
  have hdne : (1 : ℝ) - x * y ≠ 0 := hd.ne'
  -- `field_simp` normalises `x * y` to `y * x`, so it needs both orientations
  have hdne' : (1 : ℝ) - y * x ≠ 0 := by rwa [mul_comm y x]
  have c3' : (1 : ℂ) - ((1 : ℂ) - (x : ℂ)) / (1 - (x : ℂ) * (y : ℂ))
      = ((x * (1 - y) / (1 - x * y) : ℝ) : ℂ) := by
    have hr : (1 : ℝ) - (1 - x) / (1 - x * y) = x * (1 - y) / (1 - x * y) := by
      field_simp; ring
    rw [c3, ← hr]
    push_cast
    ring
  have c5' : (1 : ℂ) - ((1 : ℂ) - (y : ℂ)) / (1 - (x : ℂ) * (y : ℂ))
      = ((y * (1 - x) / (1 - x * y) : ℝ) : ℂ) := by
    have hr : (1 : ℝ) - (1 - y) / (1 - x * y) = y * (1 - x) / (1 - x * y) := by
      field_simp; ring
    rw [c5, ← hr]
    push_cast
    ring
  have c4' : (1 : ℂ) - ((1 : ℂ) - (x : ℂ) * (y : ℂ)) = ((x * y : ℝ) : ℂ) := by
    push_cast; ring
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · rw [clog_of_eq_ofReal h3p c3, clog_of_eq_ofReal h1x cA, clog_of_eq_ofReal hd cD,
      Real.log_div h1x.ne' hd.ne']
    push_cast; ring
  · rw [clog_of_eq_ofReal (div_pos (mul_pos hx0 h1y) hd) c3',
      clog_of_eq_ofReal hx0 cx, clog_of_eq_ofReal h1y cB, clog_of_eq_ofReal hd cD,
      Real.log_div (mul_pos hx0 h1y).ne' hd.ne', Real.log_mul hx0.ne' h1y.ne']
    push_cast; ring
  · rw [clog_of_eq_ofReal (mul_pos hx0 hy0) c4', clog_of_eq_ofReal hx0 cx,
      clog_of_eq_ofReal hy0 rfl, Real.log_mul hx0.ne' hy0.ne']
    push_cast; ring
  · rw [clog_of_eq_ofReal h5p c5, clog_of_eq_ofReal h1y cB, clog_of_eq_ofReal hd cD,
      Real.log_div h1y.ne' hd.ne']
    push_cast; ring
  · rw [clog_of_eq_ofReal (div_pos (mul_pos hy0 h1x) hd) c5',
      clog_of_eq_ofReal hy0 rfl, clog_of_eq_ofReal h1x cA, clog_of_eq_ofReal hd cD,
      Real.log_div (mul_pos hy0 h1x).ne' hd.ne', Real.log_mul hy0.ne' h1x.ne']
    push_cast; ring

/-- **`hasDerivAt_pentagonSum` instantiated: every hypothesis discharged.**

No branch condition survives as a hypothesis, so the theorem above is not
vacuous. It is *only* that — the region is the one where the real five-term
identity was already available. -/
theorem hasDerivAt_pentagonSum_of_real
    (hx0 : 0 < x) (hx1 : x < 1) (hy0 : 0 < y) (hy1 : y < 1) :
    HasDerivAt (pentagonSum (y : ℂ)) 0 (x : ℂ) := by
  obtain ⟨-, hd, hdlt, h3p, h3lt, h5p, h5lt⟩ := pentagon_args_mem_Ioo hx0 hx1 hy0 hy1
  obtain ⟨e3, e3', e4', e5, e5'⟩ := pentagon_branch_conditions_of_real hx0 hx1 hy0 hy1
  have cD : (1 : ℂ) - (x : ℂ) * (y : ℂ) = ((1 - x * y : ℝ) : ℂ) := by push_cast; ring
  have c3 : ((1 : ℂ) - (x : ℂ)) / (1 - (x : ℂ) * (y : ℂ))
      = (((1 - x) / (1 - x * y) : ℝ) : ℂ) := by push_cast; ring
  have c5 : ((1 : ℂ) - (y : ℂ)) / (1 - (x : ℂ) * (y : ℂ))
      = (((1 - y) / (1 - x * y) : ℝ) : ℂ) := by push_cast; ring
  refine hasDerivAt_pentagonSum (ofReal_mem_rogersDomain hx0 hx1) ?_ ?_ ?_ ?_ e3 e3' e4' e5 e5'
  · rw [cD]; exact_mod_cast hd.ne'
  · rw [c3]; exact ofReal_mem_rogersDomain h3p h3lt
  · rw [cD]; exact ofReal_mem_rogersDomain hd hdlt
  · rw [c5]; exact ofReal_mem_rogersDomain h5p h5lt

end RealSquare

/-! ### Continuing the branch conditions

The branch conditions are the delicate input, and the reason is that they are
**not** identities — `log a₃ = log(1−x) − log(1−xy)` compares two sheets and
Route 45 measured the pentagon drifting when they disagree. But the *defect*

    d₃(w) = log a₃(w) − log(1−w) + log(1−wy)

is holomorphic wherever all three logarithms are, and its derivative vanishes
identically: `a₃′/a₃ + 1/(1−w) − y/(1−wy) = 0` as a rational function. So `d₃` is
locally constant, hence constant on any open connected region, hence `0`
throughout a region containing one point where it vanishes.

All five defects behave the same way, so the whole branch bookkeeping reduces to
**one** geometric question: is there an open connected set of `x` on which the
pentagon's arguments stay off both cuts and which reaches a base point? That is
the honest residue of Routes 45–46 — not bookkeeping any more, but a statement
about a region, and for the 5₂ saddle it is exactly where flattening can fail.

⚠ No such region is exhibited here for the 5₂ saddle values. What is proved is
the propagation principle and the base point. -/

/-- The pentagon's analytic side conditions at `w`, for a fixed `y`: all four
`x`-dependent arguments avoid both real cuts. Everything else the pentagon needs
— `w ≠ 0`, `1−w ≠ 0`, `y ≠ 0`, `1−y ≠ 0`, `1−wy ≠ 0`, and slit-plane membership
for each logarithm — is a consequence. -/
def PentagonRegular (y w : ℂ) : Prop :=
  w ∈ rogersDomain ∧ (1 - w) / (1 - w * y) ∈ rogersDomain
    ∧ (1 : ℂ) - w * y ∈ rogersDomain ∧ (1 - y) / (1 - w * y) ∈ rogersDomain

namespace PentagonRegular

variable {y w : ℂ}

theorem ne_zero (h : PentagonRegular y w) : w ≠ 0 := ne_zero_of_mem_rogersDomain h.1

theorem one_sub_ne_zero (h : PentagonRegular y w) : (1 : ℂ) - w ≠ 0 :=
  one_sub_ne_zero_of_mem_rogersDomain h.1

theorem den_ne_zero (h : PentagonRegular y w) : (1 : ℂ) - w * y ≠ 0 :=
  ne_zero_of_mem_rogersDomain h.2.2.1

theorem mul_ne_zero' (h : PentagonRegular y w) : w * y ≠ 0 := by
  have := one_sub_ne_zero_of_mem_rogersDomain h.2.2.1
  simpa using this

theorem y_ne_zero (h : PentagonRegular y w) : y ≠ 0 :=
  fun hy => h.mul_ne_zero' (by simp [hy])

theorem one_sub_y_ne_zero (h : PentagonRegular y w) : (1 : ℂ) - y ≠ 0 :=
  fun hy => ne_zero_of_mem_rogersDomain h.2.2.2 (by rw [hy]; simp)

/-- On the positive real square, every point is regular. -/
theorem of_real {x y : ℝ} (hx0 : 0 < x) (hx1 : x < 1) (hy0 : 0 < y) (hy1 : y < 1) :
    PentagonRegular (y : ℂ) (x : ℂ) := by
  obtain ⟨-, hd, hdlt, h3p, h3lt, h5p, h5lt⟩ := pentagon_args_mem_Ioo hx0 hx1 hy0 hy1
  have cD : (1 : ℂ) - (x : ℂ) * (y : ℂ) = ((1 - x * y : ℝ) : ℂ) := by push_cast; ring
  have c3 : ((1 : ℂ) - (x : ℂ)) / (1 - (x : ℂ) * (y : ℂ))
      = (((1 - x) / (1 - x * y) : ℝ) : ℂ) := by push_cast; ring
  have c5 : ((1 : ℂ) - (y : ℂ)) / (1 - (x : ℂ) * (y : ℂ))
      = (((1 - y) / (1 - x * y) : ℝ) : ℂ) := by push_cast; ring
  exact ⟨ofReal_mem_rogersDomain hx0 hx1, by rw [c3]; exact ofReal_mem_rogersDomain h3p h3lt,
    by rw [cD]; exact ofReal_mem_rogersDomain hd hdlt,
    by rw [c5]; exact ofReal_mem_rogersDomain h5p h5lt⟩

end PentagonRegular

/-- **The propagation principle.** A defect that is holomorphic with vanishing
derivative on an open connected set and vanishes somewhere on it vanishes
everywhere on it. This is what turns a branch condition checked at one point into
one that holds on a whole region. -/
theorem eq_zero_of_hasDerivAt_zero {f : ℂ → ℂ} {S : Set ℂ} (hS : IsOpen S)
    (hSc : IsPreconnected S) (hf : ∀ w ∈ S, HasDerivAt f 0 w)
    {x₀ x : ℂ} (hx₀ : x₀ ∈ S) (hx : x ∈ S) (h0 : f x₀ = 0) : f x = 0 := by
  have hd : DifferentiableOn ℂ f S := fun w hw => (hf w hw).differentiableAt.differentiableWithinAt
  have hz : Set.EqOn (deriv f) 0 S := fun w hw => (hf w hw).deriv
  rw [hS.is_const_of_deriv_eq_zero hSc hd hz hx hx₀, h0]

/-! #### The five defects -/

/-- `log a₃ − log(1−w) + log(1−wy)`; the branch condition `e3` is its vanishing. -/
noncomputable def defectThree (y w : ℂ) : ℂ :=
  Complex.log ((1 - w) / (1 - w * y)) - Complex.log (1 - w) + Complex.log (1 - w * y)

/-- `log(1−a₃) − log w − log(1−y) + log(1−wy)`; the branch condition `e3'`. -/
noncomputable def defectThree' (y w : ℂ) : ℂ :=
  Complex.log (1 - (1 - w) / (1 - w * y)) - Complex.log w - Complex.log (1 - y)
    + Complex.log (1 - w * y)

/-- `log(wy) − log w − log y`; the branch condition `e4'`. -/
noncomputable def defectFour' (y w : ℂ) : ℂ :=
  Complex.log (1 - (1 - w * y)) - Complex.log w - Complex.log y

/-- `log a₅ − log(1−y) + log(1−wy)`; the branch condition `e5`. -/
noncomputable def defectFive (y w : ℂ) : ℂ :=
  Complex.log ((1 - y) / (1 - w * y)) - Complex.log (1 - y) + Complex.log (1 - w * y)

/-- `log(1−a₅) − log y − log(1−w) + log(1−wy)`; the branch condition `e5'`. -/
noncomputable def defectFive' (y w : ℂ) : ℂ :=
  Complex.log (1 - (1 - y) / (1 - w * y)) - Complex.log y - Complex.log (1 - w)
    + Complex.log (1 - w * y)

section Defects

variable {y x : ℂ}

/-- `d/dw log(1−w) = −(1−x)⁻¹`. -/
theorem hasDerivAt_clog_one_sub (h : (1 : ℂ) - x ∈ Complex.slitPlane) :
    HasDerivAt (fun w : ℂ => Complex.log (1 - w)) (-((1 - x)⁻¹)) x := by
  have hinner : HasDerivAt (fun w : ℂ => 1 - w) (-1) x := by
    simpa using (hasDerivAt_const x (1 : ℂ)).sub (hasDerivAt_id x)
  have h1 : HasDerivAt (Complex.log ∘ fun w : ℂ => 1 - w) ((1 - x)⁻¹ * (-1)) x :=
    (Complex.hasDerivAt_log h).comp x hinner
  simpa using h1

/-- `d/dw log(1−wy) = (1−xy)⁻¹·(−y)`. -/
theorem hasDerivAt_clog_one_sub_mul (h : (1 : ℂ) - x * y ∈ Complex.slitPlane) :
    HasDerivAt (fun w : ℂ => Complex.log (1 - w * y)) ((1 - x * y)⁻¹ * (-y)) x := by
  have h1 : HasDerivAt (Complex.log ∘ fun w : ℂ => 1 - w * y) ((1 - x * y)⁻¹ * (-y)) x :=
    (Complex.hasDerivAt_log h).comp x (hasDerivAt_argFour y x)
  exact h1

theorem hasDerivAt_defectThree (h : PentagonRegular y x) :
    HasDerivAt (defectThree y) 0 x := by
  have hd := h.den_ne_zero
  have hd' : (1 : ℂ) - y * x ≠ 0 := by rwa [mul_comm y x]
  have hx1 := h.one_sub_ne_zero
  obtain ⟨hx, h3, h4, -⟩ := h
  have L3 := (Complex.hasDerivAt_log h3.1).comp x (hasDerivAt_argThree y hd)
  have L1 := hasDerivAt_clog_one_sub (one_sub_mem_slitPlane_iff.mpr hx.2)
  have L2 := hasDerivAt_clog_one_sub_mul h4.1
  refine ((L3.sub L1).add L2).congr_deriv ?_
  field_simp
  ring

theorem hasDerivAt_defectThree' (h : PentagonRegular y x) :
    HasDerivAt (defectThree' y) 0 x := by
  have hd := h.den_ne_zero
  have hd' : (1 : ℂ) - y * x ≠ 0 := by rwa [mul_comm y x]
  have hx0 := h.ne_zero
  have hx1 := h.one_sub_ne_zero
  have hy1 := h.one_sub_y_ne_zero
  obtain ⟨hx, h3, h4, -⟩ := h
  have hinner : HasDerivAt (fun w : ℂ => 1 - (1 - w) / (1 - w * y))
      (-((y - 1) / (1 - x * y) ^ 2)) x := by
    simpa using (hasDerivAt_const x (1 : ℂ)).sub (hasDerivAt_argThree y hd)
  have L3' := (Complex.hasDerivAt_log (one_sub_mem_slitPlane_iff.mpr h3.2)).comp x hinner
  have L0 := Complex.hasDerivAt_log hx.1
  have L2 := hasDerivAt_clog_one_sub_mul h4.1
  refine (((L3'.sub L0).sub (hasDerivAt_const x (Complex.log (1 - y)))).add L2).congr_deriv ?_
  rw [show (1 : ℂ) - (1 - x) / (1 - x * y) = x * (1 - y) / (1 - x * y) by field_simp; ring]
  field_simp
  ring

theorem hasDerivAt_defectFour' (h : PentagonRegular y x) :
    HasDerivAt (defectFour' y) 0 x := by
  have hx0 := h.ne_zero
  have hy0 := h.y_ne_zero
  obtain ⟨hx, -, h4, -⟩ := h
  have hinner : HasDerivAt (fun w : ℂ => 1 - (1 - w * y)) y x :=
    ((hasDerivAt_const x (1 : ℂ)).sub (hasDerivAt_argFour y x)).congr_deriv (by ring)
  have L4' := (Complex.hasDerivAt_log (one_sub_mem_slitPlane_iff.mpr h4.2)).comp x hinner
  have L0 := Complex.hasDerivAt_log hx.1
  refine ((L4'.sub L0).sub (hasDerivAt_const x (Complex.log y))).congr_deriv ?_
  rw [show (1 : ℂ) - (1 - x * y) = x * y by ring]
  field_simp
  ring

theorem hasDerivAt_defectFive (h : PentagonRegular y x) :
    HasDerivAt (defectFive y) 0 x := by
  have hd := h.den_ne_zero
  have hd' : (1 : ℂ) - y * x ≠ 0 := by rwa [mul_comm y x]
  have hy1 := h.one_sub_y_ne_zero
  obtain ⟨-, -, h4, h5⟩ := h
  have L5 := (Complex.hasDerivAt_log h5.1).comp x (hasDerivAt_argFive y hd)
  have L2 := hasDerivAt_clog_one_sub_mul h4.1
  refine ((L5.sub (hasDerivAt_const x (Complex.log (1 - y)))).add L2).congr_deriv ?_
  field_simp
  ring

theorem hasDerivAt_defectFive' (h : PentagonRegular y x) :
    HasDerivAt (defectFive' y) 0 x := by
  have hd := h.den_ne_zero
  have hd' : (1 : ℂ) - y * x ≠ 0 := by rwa [mul_comm y x]
  have hx1 := h.one_sub_ne_zero
  have hy0 := h.y_ne_zero
  have hy1 := h.one_sub_y_ne_zero
  obtain ⟨hx, -, h4, h5⟩ := h
  have hinner : HasDerivAt (fun w : ℂ => 1 - (1 - y) / (1 - w * y))
      (-((1 - y) * y / (1 - x * y) ^ 2)) x := by
    simpa using (hasDerivAt_const x (1 : ℂ)).sub (hasDerivAt_argFive y hd)
  have L5' := (Complex.hasDerivAt_log (one_sub_mem_slitPlane_iff.mpr h5.2)).comp x hinner
  have L1 := hasDerivAt_clog_one_sub (one_sub_mem_slitPlane_iff.mpr hx.2)
  have L2 := hasDerivAt_clog_one_sub_mul h4.1
  refine ((((L5'.sub (hasDerivAt_const x (Complex.log y))).sub L1).add L2)).congr_deriv ?_
  rw [show (1 : ℂ) - (1 - y) / (1 - x * y) = y * (1 - x) / (1 - x * y) by field_simp; ring]
  field_simp
  ring

end Defects

/-! #### The payoff: a regular region reaching a base point -/

/-- **The pentagon's derivative vanishes throughout a regular region that reaches
a point where the branch conditions hold.**

No branch condition is assumed at `x` itself — only at the base point `x₀`, and
they are *transported* by `eq_zero_of_hasDerivAt_zero`. This is what the phrase
"continue the branch conditions" reduces to. -/
theorem hasDerivAt_pentagonSum_of_region {y : ℂ} {S : Set ℂ} (hS : IsOpen S)
    (hSc : IsPreconnected S) (hreg : ∀ w ∈ S, PentagonRegular y w)
    {x₀ x : ℂ} (hx₀ : x₀ ∈ S) (hx : x ∈ S)
    (b3 : defectThree y x₀ = 0) (b3' : defectThree' y x₀ = 0)
    (b4' : defectFour' y x₀ = 0) (b5 : defectFive y x₀ = 0)
    (b5' : defectFive' y x₀ = 0) :
    HasDerivAt (pentagonSum y) 0 x := by
  have e3 := eq_zero_of_hasDerivAt_zero hS hSc
    (fun w hw => hasDerivAt_defectThree (hreg w hw)) hx₀ hx b3
  have e3' := eq_zero_of_hasDerivAt_zero hS hSc
    (fun w hw => hasDerivAt_defectThree' (hreg w hw)) hx₀ hx b3'
  have e4' := eq_zero_of_hasDerivAt_zero hS hSc
    (fun w hw => hasDerivAt_defectFour' (hreg w hw)) hx₀ hx b4'
  have e5 := eq_zero_of_hasDerivAt_zero hS hSc
    (fun w hw => hasDerivAt_defectFive (hreg w hw)) hx₀ hx b5
  have e5' := eq_zero_of_hasDerivAt_zero hS hSc
    (fun w hw => hasDerivAt_defectFive' (hreg w hw)) hx₀ hx b5'
  unfold defectThree at e3
  unfold defectThree' at e3'
  unfold defectFour' at e4'
  unfold defectFive at e5
  unfold defectFive' at e5'
  obtain ⟨h1, h3, h4, h5⟩ := hreg x hx
  exact hasDerivAt_pentagonSum h1 (ne_zero_of_mem_rogersDomain h4) h3 h4 h5
    (by linear_combination e3) (by linear_combination e3') (by linear_combination e4')
    (by linear_combination e5) (by linear_combination e5')

/-- **The complex pentagon sum is constant on such a region.**

This is as far as the derivative argument reaches. What it still does not give is
a *region*: for the 5₂ saddle values `y₁, y₂` none is exhibited, and exhibiting
one is exactly where flattening — Neumann's `ker ν` — can obstruct. -/
theorem pentagonSum_eq_of_region {y : ℂ} {S : Set ℂ} (hS : IsOpen S)
    (hSc : IsPreconnected S) (hreg : ∀ w ∈ S, PentagonRegular y w)
    {x₀ x : ℂ} (hx₀ : x₀ ∈ S) (hx : x ∈ S)
    (b3 : defectThree y x₀ = 0) (b3' : defectThree' y x₀ = 0)
    (b4' : defectFour' y x₀ = 0) (b5 : defectFive y x₀ = 0)
    (b5' : defectFive' y x₀ = 0) :
    pentagonSum y x = pentagonSum y x₀ := by
  have hd : ∀ w ∈ S, HasDerivAt (pentagonSum y) 0 w := fun w hw =>
    hasDerivAt_pentagonSum_of_region hS hSc hreg hx₀ hw b3 b3' b4' b5 b5'
  exact hS.is_const_of_deriv_eq_zero hSc
    (fun w hw => (hd w hw).differentiableAt.differentiableWithinAt)
    (fun w hw => (hd w hw).deriv) hx hx₀

/-- **A real base point supplies all five base values.** `0 < x₀, y < 1` makes
every defect vanish, by `pentagon_branch_conditions_of_real`. -/
theorem defects_eq_zero_of_real {x y : ℝ} (hx0 : 0 < x) (hx1 : x < 1)
    (hy0 : 0 < y) (hy1 : y < 1) :
    defectThree (y : ℂ) (x : ℂ) = 0 ∧ defectThree' (y : ℂ) (x : ℂ) = 0
      ∧ defectFour' (y : ℂ) (x : ℂ) = 0 ∧ defectFive (y : ℂ) (x : ℂ) = 0
      ∧ defectFive' (y : ℂ) (x : ℂ) = 0 := by
  obtain ⟨e3, e3', e4', e5, e5'⟩ := pentagon_branch_conditions_of_real hx0 hx1 hy0 hy1
  unfold defectThree defectThree' defectFour' defectFive defectFive'
  exact ⟨by linear_combination e3, by linear_combination e3', by linear_combination e4',
    by linear_combination e5, by linear_combination e5'⟩

/-- **The statement the 5₂ lane actually wants, with its one remaining input
named.** Give an open connected set of `x` on which the pentagon stays regular
and which contains a real point of `(0,1)`, and the complex five-term sum is
constant on it — equal to the value it has on the real square, where the real
five-term identity already pins it.

The hypothesis `hreg` was the whole difficulty when this was written. It is
discharged below: `pentagonRegular_of_mem_rogersDomain` supplies the regularity
and `isPreconnected_rogersDomain` the connectedness, so `rogersDomain` **is**
such a set — which is what turns this conditional statement into the
unconditional `pentagonSum_eq_pi_sq_div_two`.

**The 5₂ sum rule is PROVED**:
`QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms. -/
theorem pentagonSum_eq_of_region_of_real {x₀ y : ℝ} {S : Set ℂ} (hS : IsOpen S)
    (hSc : IsPreconnected S) (hreg : ∀ w ∈ S, PentagonRegular (y : ℂ) w)
    (hx0 : 0 < x₀) (hx1 : x₀ < 1) (hy0 : 0 < y) (hy1 : y < 1)
    (hmem : ((x₀ : ℝ) : ℂ) ∈ S) {x : ℂ} (hx : x ∈ S) :
    pentagonSum (y : ℂ) x = pentagonSum (y : ℂ) ((x₀ : ℝ) : ℂ) := by
  obtain ⟨b3, b3', b4', b5, b5'⟩ := defects_eq_zero_of_real hx0 hx1 hy0 hy1
  exact pentagonSum_eq_of_region hS hSc hreg hmem hx b3 b3' b4' b5 b5'

/-! ### Pinning the constant

"Constant on the region" is only worth something once the constant is a number.
It is `π²/2`, and the corpus already has every ingredient:

* `cRogersL` at a real point of `(0,1)` **is** the corpus's real `rogersL`
  (`cRogersL_ofReal`) — the complex and real `Li₂` series are literally the same
  series, and both logarithms are real there;
* the real pentagon sum is `π²/2` (`rogersL_pentagon`), from Abel's relation
  `FiveTwoAbelFiveTerm.rogersL_fiveTerm` plus three applications of Rogers
  reflection, since `1 − (1−x)/(1−xy) = x(1−y)/(1−xy)` and its two companions
  turn the pentagon's arguments into Abel's.

So `pentagonSum_eq_pi_sq_div_two_of_region` is a **complex five-term identity**,
conditional on exactly one thing: the region. -/

section Constant

open QOU.QPochhammer QOU.QBeta.FiveTwoRogersReflection QOU.QBeta.FiveTwoAbelFiveTerm

/-- The complex `Li₂` series at a real argument is the real one — same series,
termwise. -/
theorem cLiTwo_ofReal (t : ℝ) : cLiTwo (t : ℂ) = ((LiTwo t : ℝ) : ℂ) := by
  unfold cLiTwo LiTwo
  rw [Complex.ofReal_tsum]
  refine tsum_congr fun k => ?_
  push_cast
  ring

/-- `cLiTwoExt` at a real point of `(−1,1)` is the corpus's real `LiTwo`. -/
theorem cLiTwoExt_ofReal {t : ℝ} (h : |t| < 1) :
    cLiTwoExt (t : ℂ) = ((LiTwo t : ℝ) : ℂ) := by
  rw [cLiTwoExt_eq_cLiTwo (by simpa using h), cLiTwo_ofReal]

/-- **`cRogersL` is the corpus's real Rogers dilogarithm on `(0,1)`.**

This is the bridge the lane was missing between the complex pentagon and the
real five-term identity that was already proved. -/
theorem cRogersL_ofReal {t : ℝ} (h0 : 0 < t) (h1 : t < 1) :
    cRogersL (t : ℂ) = ((rogersL t : ℝ) : ℂ) := by
  unfold cRogersL rogersL
  rw [cLiTwoExt_ofReal (by rw [abs_of_pos h0]; exact h1), clog_of_eq_ofReal h0 rfl,
    clog_of_eq_ofReal (show (0 : ℝ) < 1 - t by linarith)
      (show (1 : ℂ) - (t : ℂ) = ((1 - t : ℝ) : ℂ) by push_cast; ring)]
  push_cast
  ring

/-- **The real pentagon sum is `π²/2`.**

Abel's relation gives the sum over `x, y, xy, x(1−y)/(1−xy), y(1−x)/(1−xy)`;
reflection turns the last three into the pentagon's `1−xy`, `(1−x)/(1−xy)`,
`(1−y)/(1−xy)`, at the cost of `3 · π²/6`. -/
theorem rogersL_pentagon {x y : ℝ} (hx0 : 0 < x) (hx1 : x < 1)
    (hy0 : 0 < y) (hy1 : y < 1) :
    rogersL x + rogersL y + rogersL ((1 - x) / (1 - x * y)) + rogersL (1 - x * y)
      + rogersL ((1 - y) / (1 - x * y)) = Real.pi ^ 2 / 2 := by
  obtain ⟨hxy, hd, -, -, -, -, -⟩ := pentagon_args_mem_Ioo hx0 hx1 hy0 hy1
  have hdne : (1 : ℝ) - x * y ≠ 0 := hd.ne'
  have hdne' : (1 : ℝ) - y * x ≠ 0 := by rwa [mul_comm y x]
  have hb3 : (0 : ℝ) < x * (1 - y) / (1 - x * y) := div_pos (by nlinarith) hd
  have hb3' : x * (1 - y) / (1 - x * y) < 1 := by rw [div_lt_one hd]; nlinarith
  have hb5 : (0 : ℝ) < y * (1 - x) / (1 - x * y) := div_pos (by nlinarith) hd
  have hb5' : y * (1 - x) / (1 - x * y) < 1 := by rw [div_lt_one hd]; nlinarith
  have r3 := rogersL_one_sub hb3 hb3'
  have r5 := rogersL_one_sub hb5 hb5'
  have r4 := rogersL_one_sub (mul_pos hx0 hy0) hxy
  rw [show (1 : ℝ) - x * (1 - y) / (1 - x * y) = (1 - x) / (1 - x * y) by
    field_simp; ring] at r3
  rw [show (1 : ℝ) - y * (1 - x) / (1 - x * y) = (1 - y) / (1 - x * y) by
    field_simp; ring] at r5
  have hab := rogersL_fiveTerm hx0 hx1 hy0 hy1
  linarith [hab, r3, r4, r5]

/-- **The constant, as a number.** On the positive real square the complex
pentagon sum is `π²/2`. -/
theorem pentagonSum_ofReal {x y : ℝ} (hx0 : 0 < x) (hx1 : x < 1)
    (hy0 : 0 < y) (hy1 : y < 1) :
    pentagonSum (y : ℂ) (x : ℂ) = ((Real.pi ^ 2 / 2 : ℝ) : ℂ) := by
  obtain ⟨-, hd, hdlt, h3p, h3lt, h5p, h5lt⟩ := pentagon_args_mem_Ioo hx0 hx1 hy0 hy1
  have cD : (1 : ℂ) - (x : ℂ) * (y : ℂ) = ((1 - x * y : ℝ) : ℂ) := by push_cast; ring
  have c3 : ((1 : ℂ) - (x : ℂ)) / (1 - (x : ℂ) * (y : ℂ))
      = (((1 - x) / (1 - x * y) : ℝ) : ℂ) := by push_cast; ring
  have c5 : ((1 : ℂ) - (y : ℂ)) / (1 - (x : ℂ) * (y : ℂ))
      = (((1 - y) / (1 - x * y) : ℝ) : ℂ) := by push_cast; ring
  unfold pentagonSum
  rw [c3, c5, cD, cRogersL_ofReal hx0 hx1, cRogersL_ofReal hy0 hy1,
    cRogersL_ofReal h3p h3lt, cRogersL_ofReal hd hdlt, cRogersL_ofReal h5p h5lt,
    ← rogersL_pentagon hx0 hx1 hy0 hy1]
  push_cast
  ring

/-- **A complex five-term identity — conditional on the region.**

On any open connected set `S` of `x` that stays `PentagonRegular` for a real
`y ∈ (0,1)` and contains a real point of `(0,1)`,

    L(x) + L(y) + L((1−x)/(1−xy)) + L(1−xy) + L((1−y)/(1−xy)) = π²/2

for the complex Rogers dilogarithm `L = cRogersL`, at **every** point of `S` —
including points where nothing is real.

⚠ The hypothesis `hreg` is the entire remaining difficulty, and it is not a
technicality: a regular region reaching the real square *forces* the naive log
expansions, so where the flattening is non-trivial no such region can exist.
That is the obstruction and the missing region seen twice.

**The 5₂ sum rule is PROVED**: `FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms. -/
theorem pentagonSum_eq_pi_sq_div_two_of_region {x₀ y : ℝ} {S : Set ℂ} (hS : IsOpen S)
    (hSc : IsPreconnected S) (hreg : ∀ w ∈ S, PentagonRegular (y : ℂ) w)
    (hx0 : 0 < x₀) (hx1 : x₀ < 1) (hy0 : 0 < y) (hy1 : y < 1)
    (hmem : ((x₀ : ℝ) : ℂ) ∈ S) {x : ℂ} (hx : x ∈ S) :
    pentagonSum (y : ℂ) x = ((Real.pi ^ 2 / 2 : ℝ) : ℂ) := by
  rw [pentagonSum_eq_of_region_of_real hS hSc hreg hx0 hx1 hy0 hy1 hmem hx,
    pentagonSum_ofReal hx0 hx1 hy0 hy1]

end Constant

/-! ### The `x ↔ y` symmetry

The pentagon's five arguments are permuted, not changed, by `x ↔ y`
(`[x, y, a₃, a₄, a₅] ↦ [y, x, a₅, a₄, a₃]`), so the sum is symmetric. Transport
in the *second* variable is therefore the same theorem, not a new one — which
matters because reaching the 5₂ saddle needs both variables to move. -/

theorem pentagonSum_symm (y x : ℂ) : pentagonSum y x = pentagonSum x y := by
  unfold pentagonSum
  rw [mul_comm x y]
  ring

theorem pentagonSum_swap (x : ℂ) : (fun w : ℂ => pentagonSum w x) = pentagonSum x :=
  funext fun w => pentagonSum_symm w x

/-- Transport in `y`, for free from the symmetry. -/
theorem hasDerivAt_pentagonSum_snd_of_region {x : ℂ} {S : Set ℂ} (hS : IsOpen S)
    (hSc : IsPreconnected S) (hreg : ∀ w ∈ S, PentagonRegular x w)
    {y₀ y : ℂ} (hy₀ : y₀ ∈ S) (hy : y ∈ S)
    (b3 : defectThree x y₀ = 0) (b3' : defectThree' x y₀ = 0)
    (b4' : defectFour' x y₀ = 0) (b5 : defectFive x y₀ = 0)
    (b5' : defectFive' x y₀ = 0) :
    HasDerivAt (fun w : ℂ => pentagonSum w x) 0 y := by
  rw [pentagonSum_swap]
  exact hasDerivAt_pentagonSum_of_region hS hSc hreg hy₀ hy b3 b3' b4' b5 b5'

/-! ### The region exists — an unconditional complex five-term identity

The region the previous section asks for is not exotic. It is `rogersDomain`
itself, and the reason is a two-line computation: for a **real** `a ∈ (0,1)` in
the other slot, every one of the four `w`-dependent arguments has non-zero
imaginary part as soon as `w` does. Writing `w = u + iv`,

    Im(1 − wa) = −av,        Im[(1−w)·conj(1−wa)] = v(a−1),
    Im[(1−a)·conj(1−wa)] = (1−a)av

and a point with non-zero imaginary part is off **both** cuts automatically. Where
`v = 0` the point is real in `(0,1)` and `PentagonRegular.of_real` applies. So the
whole of `rogersDomain` is regular, it is open, and it is connected (upper
half-plane and lower half-plane, joined through the strip `0 < re < 1`).

Hence `pentagonSum_eq_pi_sq_div_two`: **unconditional**, no region hypothesis.

⚠ This is the *one-variable* statement, and that is exactly its limit. Move the
**second** variable off the reals as well and it fails — checked numerically at
`(2+0.5i, 1.5−0.9i)`, where the pentagon misses `π²/2` by `(−0.0780 + 0.2303i)π²`.
That failure is the flattening, and it is why the 5₂ sum rule does not follow:
`Vol(5₂)` needs the pair `(y₁, ȳ₁)`, both non-real.

What it *does* reach is the pair `(y₃, y₁)` — the 5₂ cubic's real root
`y₃ = 0.4301597…` against a complex one — since `y₃ ∈ (0,1)` and
`Im y₁ ≠ 0`. Verified to 40 dps in
`computations/probes/qbeta_5two_route54_complex_pentagon_probe.py`.

**The 5₂ sum rule is PROVED**: `FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms. -/

section Unconditional

/-- Non-zero imaginary part puts a point off both cuts. -/
theorem mem_rogersDomain_of_im_ne_zero {z : ℂ} (h : z.im ≠ 0) : z ∈ rogersDomain :=
  ⟨Or.inr h, Or.inl h⟩

/-- `Im(p/q) ≠ 0` from the numerator of `Complex.div_im`. -/
theorem im_div_ne_zero {p q : ℂ} (hq : q ≠ 0)
    (h : p.im * q.re - p.re * q.im ≠ 0) : (p / q).im ≠ 0 := by
  rw [Complex.div_im, div_sub_div_same]
  exact div_ne_zero h fun hc => hq (Complex.normSq_eq_zero.mp hc)

/-- `rogersDomain` is the union of two convex-joined pieces: each half-plane
glued to the strip `0 < re < 1`. -/
theorem rogersDomain_eq_union :
    rogersDomain = ({w : ℂ | 0 < w.im} ∪ {w : ℂ | 0 < w.re ∧ w.re < 1})
      ∪ ({w : ℂ | w.im < 0} ∪ {w : ℂ | 0 < w.re ∧ w.re < 1}) := by
  ext w
  simp only [rogersDomain, Set.mem_inter_iff, Complex.mem_slitPlane_iff, mem_notCut_iff,
    Set.mem_union, Set.mem_setOf_eq]
  constructor
  · rintro ⟨ha, hb⟩
    rcases eq_or_ne w.im 0 with hz | hz
    · exact Or.inl (Or.inr ⟨ha.resolve_right (not_not_intro hz),
        hb.resolve_left (not_not_intro hz)⟩)
    · rcases hz.lt_or_gt with h | h
      · exact Or.inr (Or.inl h)
      · exact Or.inl (Or.inl h)
  · rintro ((h | ⟨h, h'⟩) | (h | ⟨h, h'⟩))
    · exact ⟨Or.inr h.ne', Or.inl h.ne'⟩
    · exact ⟨Or.inl h, Or.inr h'⟩
    · exact ⟨Or.inr h.ne, Or.inl h.ne⟩
    · exact ⟨Or.inl h, Or.inr h'⟩

theorem isPreconnected_rogersDomain : IsPreconnected rogersDomain := by
  have hstrip : Convex ℝ {w : ℂ | 0 < w.re ∧ w.re < 1} := by
    have := (convex_halfSpace_re_gt (0 : ℝ)).inter (convex_halfSpace_re_lt (1 : ℝ))
    simpa [Set.inter_def, and_comm] using this
  have hA : IsPreconnected ({w : ℂ | 0 < w.im} ∪ {w : ℂ | 0 < w.re ∧ w.re < 1}) :=
    IsPreconnected.union (⟨1 / 2, 1⟩ : ℂ) (by norm_num) (by norm_num)
      (convex_halfSpace_im_gt (0 : ℝ)).isPreconnected hstrip.isPreconnected
  have hB : IsPreconnected ({w : ℂ | w.im < 0} ∪ {w : ℂ | 0 < w.re ∧ w.re < 1}) :=
    IsPreconnected.union (⟨1 / 2, -1⟩ : ℂ) (by norm_num) (by norm_num)
      (convex_halfSpace_im_lt (0 : ℝ)).isPreconnected hstrip.isPreconnected
  rw [rogersDomain_eq_union]
  exact IsPreconnected.union (⟨1 / 2, 0⟩ : ℂ) (Or.inr (by norm_num)) (Or.inr (by norm_num)) hA hB

/-- **Every point of `rogersDomain` is regular, against a real `a ∈ (0,1)`.**

Two cases, and neither is delicate: `Im w ≠ 0` propagates to all four arguments,
and `Im w = 0` puts `w` in `(0,1)` where `PentagonRegular.of_real` applies. -/
theorem pentagonRegular_of_mem_rogersDomain {a : ℝ} (h0 : 0 < a) (h1 : a < 1)
    {w : ℂ} (hw : w ∈ rogersDomain) : PentagonRegular (a : ℂ) w := by
  rcases eq_or_ne w.im 0 with hz | hz
  · have hre : w = ((w.re : ℝ) : ℂ) := by
      apply Complex.ext <;> simp [hz]
    rw [hre]
    exact PentagonRegular.of_real (hw.1.resolve_right (not_not_intro hz))
      (hw.2.resolve_left (not_not_intro hz)) h0 h1
  · have hq : ((1 : ℂ) - w * (a : ℂ)).im = -(w.im * a) := by
      simp [Complex.sub_im, Complex.mul_im]
    have hqre : ((1 : ℂ) - w * (a : ℂ)).re = 1 - w.re * a := by
      simp [Complex.sub_re, Complex.mul_re]
    have hqim : ((1 : ℂ) - w * (a : ℂ)).im ≠ 0 := by
      rw [hq]; simpa using mul_ne_zero hz h0.ne'
    have hqne : (1 : ℂ) - w * (a : ℂ) ≠ 0 :=
      ne_zero_of_mem_rogersDomain (mem_rogersDomain_of_im_ne_zero hqim)
    have hnum3 : ((1 : ℂ) - w).im * ((1 : ℂ) - w * (a : ℂ)).re
        - ((1 : ℂ) - w).re * ((1 : ℂ) - w * (a : ℂ)).im = w.im * (a - 1) := by
      rw [hq, hqre]
      simp only [Complex.sub_im, Complex.sub_re, Complex.one_re, Complex.one_im]
      ring
    have hnum5 : ((1 : ℂ) - (a : ℂ)).im * ((1 : ℂ) - w * (a : ℂ)).re
        - ((1 : ℂ) - (a : ℂ)).re * ((1 : ℂ) - w * (a : ℂ)).im = (1 - a) * (w.im * a) := by
      rw [hq, hqre]
      simp only [Complex.sub_im, Complex.sub_re, Complex.one_re, Complex.one_im,
        Complex.ofReal_re, Complex.ofReal_im]
      ring
    exact ⟨mem_rogersDomain_of_im_ne_zero hz,
      mem_rogersDomain_of_im_ne_zero (im_div_ne_zero hqne
        (by rw [hnum3]; exact mul_ne_zero hz (sub_ne_zero.mpr h1.ne))),
      mem_rogersDomain_of_im_ne_zero hqim,
      mem_rogersDomain_of_im_ne_zero (im_div_ne_zero hqne
        (by rw [hnum5]
            exact mul_ne_zero (sub_ne_zero.mpr h1.ne') (mul_ne_zero hz h0.ne')))⟩

/-- **The complex five-term identity, unconditionally, in one variable.**

    L(a) + L(w) + L((1−a)/(1−aw)) + L(1−aw) + L((1−w)/(1−aw)) = π²/2

for `L = cRogersL`, every real `a ∈ (0,1)` and **every** `w` off both real cuts —
`w` complex, `|w|` arbitrarily large, either side of either cut.

⚠ One variable. With both variables non-real it is false; see the section
header. -/
theorem pentagonSum_eq_pi_sq_div_two {a : ℝ} (h0 : 0 < a) (h1 : a < 1)
    {w : ℂ} (hw : w ∈ rogersDomain) :
    pentagonSum (a : ℂ) w = ((Real.pi ^ 2 / 2 : ℝ) : ℂ) := by
  rw [pentagonSum_eq_of_region_of_real isOpen_rogersDomain isPreconnected_rogersDomain
      (fun v hv => pentagonRegular_of_mem_rogersDomain h0 h1 hv) h0 h1 h0 h1
      (ofReal_mem_rogersDomain h0 h1) hw,
    pentagonSum_ofReal h0 h1 h0 h1]

end Unconditional

/-! ### What the theorem says at the 5₂ pair it reaches

At `(y₃, y₁)` — the saddle cubic's real root against a complex one, the one pair
`pentagonSum_eq_pi_sq_div_two` covers — the five arguments are not generic. Every
statement below is an **exact** algebraic identity, verified symbolically before
being written down and recorded numerically to 60 dps in
`computations/probes/qbeta_5two_route55_saddle_is_plastic_probe.py`.

The first is the one that matters, and it is not about the pentagon at all:

    ((y−1)/y)³ − (y−1)/y + 1 = (y³ − 2y² + 3y − 1) / y³

an identity of *rational functions*, no reduction modulo anything. So the
anharmonic map `y ↦ 1 − 1/y` carries the 5₂ saddle cubic **onto** `X³ − X + 1`,
whose roots are the negatives of the plastic numbers. The saddle orbit and the
plastic orbit are one orbit of the anharmonic group `⟨z ↦ 1−z, z ↦ 1/z⟩`.

⚠ **That is a negative for the rank programme**, and it should be read as one.
Routes 41, 47 and 48 closed their alphabets under exactly `1−z` and `1/z`, so
every relation the pentagon produces at `(y₃, y₁)` was already inside those
alphabets — and their rank gap was exactly 1 every time. The new theorem does not
add rank. What it does is *explain* why the plastic tower kept surfacing in
Routes 40–48: it was never a coincidence, it is the same orbit.

**The 5₂ sum rule is PROVED**: `FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms. -/

section SaddleStructure

/-- **The 5₂ saddle cubic is the plastic cubic, transported by `y ↦ 1 − 1/y`.**

An identity of rational functions — nothing is reduced modulo the cubic. -/
theorem saddle_to_plastic {y : ℂ} (hy : y ≠ 0) :
    ((y - 1) / y) ^ 3 - (y - 1) / y + 1 = (y ^ 3 - 2 * y ^ 2 + 3 * y - 1) / y ^ 3 := by
  field_simp
  ring

/-- A root of the saddle cubic maps to a root of `X³ − X + 1`, whose roots are
the negatives of the plastic numbers. -/
theorem plastic_of_saddle {y : ℂ} (hy : y ≠ 0) (h : y ^ 3 - 2 * y ^ 2 + 3 * y - 1 = 0) :
    ((y - 1) / y) ^ 3 - (y - 1) / y + 1 = 0 := by
  rw [saddle_to_plastic hy, h, zero_div]

/-- The inverse transport: a root of `X³ − X + 1` maps back under `x ↦ 1/(1−x)`. -/
theorem saddle_of_plastic {x : ℂ} (hx : (1 : ℂ) - x ≠ 0) (h : x ^ 3 - x + 1 = 0) :
    (1 / (1 - x)) ^ 3 - 2 * (1 / (1 - x)) ^ 2 + 3 * (1 / (1 - x)) - 1 = 0 := by
  have hrw : (1 / (1 - x)) ^ 3 - 2 * (1 / (1 - x)) ^ 2 + 3 * (1 / (1 - x)) - 1
      = (x ^ 3 - x + 1) / (1 - x) ^ 3 := by field_simp; ring
  rw [hrw, h, zero_div]

/-- **The two composite pentagon arguments at the saddle are reciprocal.**

`a₅ = 1/a₃`, i.e. `(1−a)(1−b) = (1−ab)²`, for any two roots `a, b` of the saddle
cubic — and the identity *is* the cubic, satisfied by the third root `c`. This is
why the degree-6 elements `a₃, a₅` drop out of the relation: `L(a₃) + L(1/a₃)` is
elementary by inversion, leaving only the degree-3 orbit. -/
theorem pentagon_arg_reciprocal {a b c : ℂ} (hsum : a + b + c = 2) (hprod : a * b * c = 1)
    (hcube : c ^ 3 - 2 * c ^ 2 + 3 * c - 1 = 0) (hc : c ≠ 0) :
    (1 - a) * (1 - b) = (1 - a * b) ^ 2 := by
  have h : c ^ 2 * ((1 - a) * (1 - b) - (1 - a * b) ^ 2) = 0 := by
    linear_combination (3 * c - a * b * c - 1) * hprod + (-c ^ 2) * hsum + hcube
  have h2 : (1 - a) * (1 - b) - (1 - a * b) ^ 2 = 0 :=
    (mul_eq_zero.mp h).resolve_left (pow_ne_zero 2 hc)
  linear_combination h2

/-- **The angle identity's algebraic core.** For two roots `a`, `c` of the saddle
cubic (`hR` says the third root is `1/(ac)`),

    ((1−c)/(1−ca))³ · a = −c

i.e. `a₃³·y₁ = −y₃`. Taking arguments gives `3·arg a₃ + arg y₁ = π`, which is the
angle identity `arg a₃ = (π − arg y₁)/3` that Route 58's inversion evaluation
rests on. The identity is *not* a consequence of `hR` alone — the cubic is needed
too, and the cofactors below are what a Gröbner reduction against both returns. -/
theorem saddle_arg_cube {a c : ℂ}
    (hR : a ^ 2 * c + a * c ^ 2 - 2 * (a * c) + 1 = 0)
    (hC : c ^ 3 - 2 * c ^ 2 + 3 * c - 1 = 0) :
    (1 - c) ^ 3 * a + c * (1 - c * a) ^ 3 = 0 := by
  linear_combination (-(a * c ^ 3) + c ^ 4 - 2 * c ^ 3 + 3 * c ^ 2) * hR
    + (-(a * c ^ 3) + 2 * a * c ^ 2 - a - c) * hC

/-- The same in the form the pentagon uses: the cube of the composite argument
times the other root is minus the real root. -/
theorem saddle_arg_cube' {a c : ℂ}
    (hR : a ^ 2 * c + a * c ^ 2 - 2 * (a * c) + 1 = 0)
    (hC : c ^ 3 - 2 * c ^ 2 + 3 * c - 1 = 0) (hne : (1 : ℂ) - c * a ≠ 0) :
    ((1 - c) / (1 - c * a)) ^ 3 * a = -c := by
  field_simp
  linear_combination saddle_arg_cube hR hC

/-- **Link G3's branch pinning, assembled.** `saddle_arg_cube'` gives
`a₃³·y₁ = −y₃`; `MathlibExt.clog_cube_mul` turns that into

    3·log a₃ + log y₁ = log y₃ + iπ

with **no** branch correction, given only three crude sign conditions on the
arguments. Those three are what remains of Route 58's link G3 — facts about the
specific algebraic numbers (`Re a₃ = 1/2 > 0`, `Im a₃ > 0`, `Im y₁ > 0`), not
about dilogarithms.

⚠ Stated with the sign conditions as hypotheses. They are **not** discharged
here. -/
theorem saddle_clog_cube {a : ℂ} {t : ℝ} (ht : 0 < t)
    (hR : a ^ 2 * (t : ℂ) + a * (t : ℂ) ^ 2 - 2 * (a * (t : ℂ)) + 1 = 0)
    (hC : (t : ℂ) ^ 3 - 2 * (t : ℂ) ^ 2 + 3 * (t : ℂ) - 1 = 0)
    (hne : (1 : ℂ) - (t : ℂ) * a ≠ 0) (ha : a ≠ 0)
    (ha0 : (1 - (t : ℂ)) / (1 - (t : ℂ) * a) ≠ 0)
    (harg1 : 0 ≤ ((1 - (t : ℂ)) / (1 - (t : ℂ) * a)).arg)
    (harg2 : ((1 - (t : ℂ)) / (1 - (t : ℂ) * a)).arg ≤ Real.pi / 2)
    (hbarg : 0 ≤ a.arg) :
    3 * Complex.log ((1 - (t : ℂ)) / (1 - (t : ℂ) * a)) + Complex.log a
      = ((Real.log t : ℝ) : ℂ) + (Real.pi : ℂ) * Complex.I := by
  refine clog_cube_mul ha0 ha ht ?_ harg1 harg2 hbarg
  rw [saddle_arg_cube' hR hC hne]
  push_cast
  ring

/-! #### The bounds, algebraically

Route 61 reduced link G3 to three sign conditions — `Im a₃ ≥ 0`, `Re a₃ ≥ 0`,
`Im y₁ ≥ 0`. The second is the only one with content, and it is exact:
`Re a₃ = 1/2`. What follows is that fact and the two relations it needs, all by
`linear_combination` with cofactors a Gröbner reduction returns. -/

/-- The pair relation `a²c + ac² − 2ac + 1 = 0` — "the third root is `1/(ac)` and
the three sum to `2`" — from the symmetric functions. -/
theorem saddle_pair_rel {a b c : ℂ} (hsum : a + b + c = 2) (hprod : a * b * c = 1) :
    a ^ 2 * c + a * c ^ 2 - 2 * (a * c) + 1 = 0 := by
  linear_combination (a * c) * hsum - hprod

/-- `1 − cb = (a−1)/a`, since `cb = 1/a`. -/
theorem one_sub_mul_third {a b c : ℂ} (hprod : a * b * c = 1) (ha : a ≠ 0) :
    (1 : ℂ) - c * b = (a - 1) / a := by
  field_simp
  linear_combination -hprod

/-- **`a₃` and its partner sum to `1`.**

    (1−c)/(1−ca) + (1−c)/(1−cb) = 1

for the three roots. With `b = conj a` and `c` real this says `Re a₃ = 1/2`,
which is the one sign condition of link G3 with any content. -/
theorem saddle_argThree_add_eq_one {a b c : ℂ} (hsum : a + b + c = 2)
    (hprod : a * b * c = 1) (hC : c ^ 3 - 2 * c ^ 2 + 3 * c - 1 = 0)
    (ha : a ≠ 0) (h1 : (1 : ℂ) - c * a ≠ 0) (h2 : a - 1 ≠ 0) :
    (1 - c) / (1 - c * a) + (1 - c) / (1 - c * b) = 1 := by
  have hR := saddle_pair_rel hsum hprod
  rw [one_sub_mul_third hprod ha]
  field_simp
  linear_combination c * hR - a * hC

/-- `z.re = 1/2` from `z + conj z = 1`. -/
theorem re_eq_half_of_add_conj {z w : ℂ} (hw : w = (starRingEnd ℂ) z) (h : z + w = 1) :
    z.re = 1 / 2 := by
  rw [hw] at h
  have := congrArg Complex.re h
  simp [Complex.add_re, Complex.conj_re] at this
  linarith

/-- **The three sign conditions of link G3, discharged from the root data.**

`Re a₃ = 1/2 > 0` gives `arg a₃ ≤ π/2`; `Im a₃ ≥ 0` and `Im y₁ ≥ 0` give the two
non-negativity conditions. Nothing numeric is needed — the only quantitative
input is that `Re a₃` is exactly `1/2`, which is `saddle_argThree_add_eq_one`. -/
theorem saddle_arg_bounds {a b c : ℂ} (hsum : a + b + c = 2) (hprod : a * b * c = 1)
    (hC : c ^ 3 - 2 * c ^ 2 + 3 * c - 1 = 0) (ha : a ≠ 0) (h1 : (1 : ℂ) - c * a ≠ 0)
    (h2 : a - 1 ≠ 0)
    (hconj : (1 - c) / (1 - c * b) = (starRingEnd ℂ) ((1 - c) / (1 - c * a)))
    (him3 : 0 ≤ ((1 - c) / (1 - c * a)).im) (hima : 0 ≤ a.im) :
    0 ≤ ((1 - c) / (1 - c * a)).arg ∧ ((1 - c) / (1 - c * a)).arg ≤ Real.pi / 2
      ∧ 0 ≤ a.arg := by
  refine ⟨arg_nonneg_of_im_nonneg him3, arg_le_pi_div_two_of_re_nonneg ?_,
    arg_nonneg_of_im_nonneg hima⟩
  rw [re_eq_half_of_add_conj hconj (saddle_argThree_add_eq_one hsum hprod hC ha h1 h2)]
  norm_num

/-- **Link G3's angle identity, with the argument bounds discharged.**

    3·log a₃ + log y₁ = log y₃ + iπ

from root data alone — the symmetric functions, the cubic, three non-vanishing
conditions, the conjugate-pair structure, and two `Im ≥ 0` facts. **No `arg`
hypothesis survives**, and nothing numeric enters: the only quantitative input is
`Re a₃ = 1/2`, which is `saddle_argThree_add_eq_one`. -/
theorem saddle_clog_cube_of_roots {a b : ℂ} {t : ℝ} (ht : 0 < t)
    (hsum : a + b + (t : ℂ) = 2) (hprod : a * b * (t : ℂ) = 1)
    (hC : (t : ℂ) ^ 3 - 2 * (t : ℂ) ^ 2 + 3 * (t : ℂ) - 1 = 0)
    (ha : a ≠ 0) (h1 : (1 : ℂ) - (t : ℂ) * a ≠ 0) (h2 : a - 1 ≠ 0)
    (ha0 : (1 - (t : ℂ)) / (1 - (t : ℂ) * a) ≠ 0)
    (hconj : (1 - (t : ℂ)) / (1 - (t : ℂ) * b)
      = (starRingEnd ℂ) ((1 - (t : ℂ)) / (1 - (t : ℂ) * a)))
    (him3 : 0 ≤ ((1 - (t : ℂ)) / (1 - (t : ℂ) * a)).im) (hima : 0 ≤ a.im) :
    3 * Complex.log ((1 - (t : ℂ)) / (1 - (t : ℂ) * a)) + Complex.log a
      = ((Real.log t : ℝ) : ℂ) + (Real.pi : ℂ) * Complex.I := by
  obtain ⟨b1, b2, b3⟩ := saddle_arg_bounds hsum hprod hC ha h1 h2 hconj him3 hima
  exact saddle_clog_cube ht (saddle_pair_rel hsum hprod) hC h1 ha ha0 b1 b2 b3

/-- **`y² = (1−y)³` IS the saddle cubic.** `(1−y)³ − y² = −(y³−2y²+3y−1)`
identically, so the multiplicative relation the branch equation needs is the
cubic itself and nothing extra is assumed. -/
theorem saddle_sq_eq_one_sub_cube {y : ℂ} (h : y ^ 3 - 2 * y ^ 2 + 3 * y - 1 = 0) :
    y ^ 2 = (1 - y) ^ 3 := by
  linear_combination h

/-- **The saddle branch equation, integer pinned.**

    2·log y − 3·log(1−y) = 2πi·n

from the cubic alone plus a window on `2·arg y − 3·arg(1−y)`. The window has
width `4π`, so the bounds needed are crude: for the real root both arguments
vanish (`n = 0`); for `y₁` the expression lies in `(0, 7π/2) ⊂ (0, 4π)` from
`Im y₁ > 0` and `Re y₁ < 1` alone (`n = 1`); for `y₂` it is the mirror
(`n = −1`). -/
theorem saddle_branch_eq {y : ℂ} {n : ℤ} (hy : y ≠ 0) (h1y : (1 : ℂ) - y ≠ 0)
    (hcube : y ^ 3 - 2 * y ^ 2 + 3 * y - 1 = 0)
    (hlo : (2 * (n : ℝ) - 2) * Real.pi < 2 * y.arg - 3 * ((1 : ℂ) - y).arg)
    (hhi : 2 * y.arg - 3 * ((1 : ℂ) - y).arg < (2 * (n : ℝ) + 2) * Real.pi) :
    2 * Complex.log y - 3 * Complex.log (1 - y)
      = 2 * (Real.pi : ℂ) * Complex.I * (n : ℂ) := by
  refine branch_eq_of_window hy h1y (saddle_sq_eq_one_sub_cube hcube) ?_ ?_ <;>
    rwa [branch_im]

/-- **The branch integer at the real root is `0`** — both arguments vanish, so no
window argument is needed at all. -/
theorem saddle_branch_eq_real {t : ℝ} (h0 : 0 < t) (h1 : t < 1)
    (hcube : (t : ℂ) ^ 3 - 2 * (t : ℂ) ^ 2 + 3 * (t : ℂ) - 1 = 0) :
    2 * Complex.log (t : ℂ) - 3 * Complex.log (1 - (t : ℂ)) = 0 := by
  have hy : ((t : ℝ) : ℂ) ≠ 0 := by exact_mod_cast h0.ne'
  have h1y : (1 : ℂ) - ((t : ℝ) : ℂ) ≠ 0 := by
    rw [show (1 : ℂ) - ((t : ℝ) : ℂ) = ((1 - t : ℝ) : ℂ) by push_cast; ring]
    exact_mod_cast (by linarith : (0 : ℝ) < 1 - t).ne'
  have hargy : ((t : ℝ) : ℂ).arg = 0 := by
    rw [Complex.arg_ofReal_of_nonneg h0.le]
  have harg1 : ((1 : ℂ) - ((t : ℝ) : ℂ)).arg = 0 := by
    rw [show (1 : ℂ) - ((t : ℝ) : ℂ) = ((1 - t : ℝ) : ℂ) by push_cast; ring,
      Complex.arg_ofReal_of_nonneg (by linarith : (0 : ℝ) ≤ 1 - t)]
  have h := saddle_branch_eq (n := 0) hy h1y hcube
    (by rw [hargy, harg1]; simpa using Real.pi_pos)
    (by rw [hargy, harg1]; simpa using Real.pi_pos)
  simpa using h

/-- **The branch integer at the upper complex root is `1`**, from two crude sign
conditions: `Im y > 0` and `Re y ≤ 1`.

Those give `arg y ∈ (0, π)` and `arg(1−y) ∈ (−π/2, 0)`, so the branch expression
lies in `(0, 7π/2) ⊂ (0, 4π)` — inside the window, with room. Nothing numeric,
and no fact about the cubic beyond the cubic itself. -/
theorem saddle_branch_eq_upper {y : ℂ} (hy : y ≠ 0) (h1y : (1 : ℂ) - y ≠ 0)
    (hcube : y ^ 3 - 2 * y ^ 2 + 3 * y - 1 = 0)
    (him : 0 < y.im) (hre : y.re ≤ 1) :
    2 * Complex.log y - 3 * Complex.log (1 - y) = 2 * (Real.pi : ℂ) * Complex.I := by
  have hpi : (0 : ℝ) < Real.pi := Real.pi_pos
  have hargy_pos : 0 < y.arg := by
    refine lt_of_le_of_ne (Complex.arg_nonneg_iff.mpr him.le) ?_
    intro hc
    exact absurd (Complex.arg_eq_zero_iff.mp hc.symm).2 (ne_of_gt him)
  have hargy_lt : y.arg < Real.pi := Complex.arg_lt_pi_iff.mpr (Or.inr (ne_of_gt him))
  have him1 : ((1 : ℂ) - y).im < 0 := by
    simpa [Complex.sub_im] using him
  have hre1 : 0 ≤ ((1 : ℂ) - y).re := by
    simp only [Complex.sub_re, Complex.one_re]
    linarith
  have harg1_neg : ((1 : ℂ) - y).arg < 0 := Complex.arg_neg_iff.mpr him1
  have harg1_gt : -(Real.pi / 2) ≤ ((1 : ℂ) - y).arg :=
    Complex.neg_pi_div_two_le_arg_iff.mpr (Or.inl hre1)
  have h := saddle_branch_eq (n := 1) hy h1y hcube (by push_cast; nlinarith)
    (by push_cast; nlinarith)
  simpa using h

/-- **The branch integer at the lower complex root is `−1`** — the mirror of
`saddle_branch_eq_upper`, from `Im y < 0` and `Re y ≤ 1`. The expression lies in
`(−7π/2, 0) ⊂ (−4π, 0)`. -/
theorem saddle_branch_eq_lower {y : ℂ} (hy : y ≠ 0) (h1y : (1 : ℂ) - y ≠ 0)
    (hcube : y ^ 3 - 2 * y ^ 2 + 3 * y - 1 = 0)
    (him : y.im < 0) (hre : y.re ≤ 1) :
    2 * Complex.log y - 3 * Complex.log (1 - y) = -(2 * (Real.pi : ℂ) * Complex.I) := by
  have hpi : (0 : ℝ) < Real.pi := Real.pi_pos
  have hargy_neg : y.arg < 0 := Complex.arg_neg_iff.mpr him
  have hargy_gt : -Real.pi < y.arg := Complex.neg_pi_lt_arg y
  have him1 : 0 < ((1 : ℂ) - y).im := by simpa [Complex.sub_im] using him
  have hre1 : 0 ≤ ((1 : ℂ) - y).re := by
    simp only [Complex.sub_re, Complex.one_re]; linarith
  have harg1_pos : 0 < ((1 : ℂ) - y).arg := by
    refine lt_of_le_of_ne (Complex.arg_nonneg_iff.mpr him1.le) ?_
    intro hc
    exact absurd (Complex.arg_eq_zero_iff.mp hc.symm).2 (ne_of_gt him1)
  have harg1_le : ((1 : ℂ) - y).arg ≤ Real.pi / 2 :=
    Complex.arg_le_pi_div_two_iff.mpr (Or.inl hre1)
  have h := saddle_branch_eq (n := -1) hy h1y hcube (by push_cast; nlinarith)
    (by push_cast; nlinarith)
  push_cast at h
  linear_combination h

/-! #### The root data, packaged

Every hypothesis Route 64's capstone still carries is a consequence of one
bundle: the saddle cubic has a real root in `(0,1)` and a conjugate pair. Stating
that once and deriving the rest keeps the inputs auditable — each field is a
checkable fact about the cubic, and nothing numeric appears. -/

/-- **The 5₂ saddle cubic's roots as data**: a real root `t ∈ (0,1)` and a
conjugate pair whose upper member is `a`. The three symmetric functions are the
cubic `X³ − 2X² + 3X − 1`. -/
structure SaddleRoots where
  /-- the real root -/
  t : ℝ
  /-- the root in the upper half plane -/
  a : ℂ
  ht0 : 0 < t
  ht1 : t < 1
  hsum : a + (starRingEnd ℂ) a + (t : ℂ) = 2
  hp2 : a * (starRingEnd ℂ) a + a * (t : ℂ) + (starRingEnd ℂ) a * (t : ℂ) = 3
  hprod : a * (starRingEnd ℂ) a * (t : ℂ) = 1
  him : 0 < a.im

namespace SaddleRoots

variable (S : SaddleRoots)

theorem cubic_t : (S.t : ℂ) ^ 3 - 2 * (S.t : ℂ) ^ 2 + 3 * (S.t : ℂ) - 1 = 0 := by
  linear_combination (S.t : ℂ) ^ 2 * S.hsum - (S.t : ℂ) * S.hp2 + S.hprod

theorem cubic_a : S.a ^ 3 - 2 * S.a ^ 2 + 3 * S.a - 1 = 0 := by
  linear_combination S.a ^ 2 * S.hsum - S.a * S.hp2 + S.hprod

theorem cubic_conj_a : ((starRingEnd ℂ) S.a) ^ 3 - 2 * ((starRingEnd ℂ) S.a) ^ 2
    + 3 * ((starRingEnd ℂ) S.a) - 1 = 0 := by
  have h := congrArg (starRingEnd ℂ) S.cubic_a
  simpa [map_ofNat] using h

theorem ne_zero : S.a ≠ 0 := fun hc => absurd (by rw [hc]; simp : S.a.im = 0) (ne_of_gt S.him)

theorem one_sub_ne_zero : (1 : ℂ) - S.a ≠ 0 := by
  intro hc
  have : ((1 : ℂ) - S.a).im = 0 := by rw [hc]; simp
  simp only [Complex.sub_im, Complex.one_im, zero_sub, neg_eq_zero] at this
  exact absurd this (ne_of_gt S.him)

/-- `2·Re a = 2 − t`, from the trace. -/
theorem two_re : 2 * S.a.re = 2 - S.t := by
  have h := congrArg Complex.re S.hsum
  simp only [Complex.add_re, Complex.conj_re, Complex.ofReal_re] at h
  norm_num at h
  linarith

theorem re_le_one : S.a.re ≤ 1 := by
  have := S.two_re
  have := S.ht0
  linarith

/-- **The branch integer at the real root is `0`.** -/
theorem branch_real :
    2 * Complex.log (S.t : ℂ) - 3 * Complex.log (1 - (S.t : ℂ)) = 0 :=
  saddle_branch_eq_real S.ht0 S.ht1 S.cubic_t

/-- **The branch integer at the upper root is `+1`** — the value the corpus
records as `ε₁`, now proved rather than measured. -/
theorem branch_upper :
    2 * Complex.log S.a - 3 * Complex.log (1 - S.a) = 2 * (Real.pi : ℂ) * Complex.I :=
  saddle_branch_eq_upper S.ne_zero S.one_sub_ne_zero S.cubic_a S.him S.re_le_one

/-- The pair relation the angle identity needs. -/
theorem pair_rel :
    S.a ^ 2 * (S.t : ℂ) + S.a * (S.t : ℂ) ^ 2 - 2 * (S.a * (S.t : ℂ)) + 1 = 0 :=
  saddle_pair_rel S.hsum S.hprod

/-- `|a|²·t = 1` — the modulus fact, immediate from the norm. -/
theorem normSq_mul : ((Complex.normSq S.a : ℝ) : ℂ) * (S.t : ℂ) = 1 := by
  rw [← Complex.mul_conj]
  linear_combination S.hprod

/-- **The branch integer at the lower root is `−1`.** With `branch_upper` and
`branch_real` this is the full branch datum `ε = (+1, −1, 0)` the corpus records
for the 5₂ saddle — **proved**, where it had been measured. -/
theorem branch_lower :
    2 * Complex.log ((starRingEnd ℂ) S.a) - 3 * Complex.log (1 - (starRingEnd ℂ) S.a)
      = -(2 * (Real.pi : ℂ) * Complex.I) := by
  have hcube : ((starRingEnd ℂ) S.a) ^ 3 - 2 * ((starRingEnd ℂ) S.a) ^ 2
      + 3 * ((starRingEnd ℂ) S.a) - 1 = 0 := by
    have h := congrArg (starRingEnd ℂ) S.cubic_a
    simpa [map_ofNat] using h
  have hne : ((starRingEnd ℂ) S.a) ≠ 0 := by
    simpa using S.ne_zero
  have h1ne : (1 : ℂ) - (starRingEnd ℂ) S.a ≠ 0 := by
    intro hc
    apply S.one_sub_ne_zero
    have := congrArg (starRingEnd ℂ) hc
    simpa using this
  refine saddle_branch_eq_lower hne h1ne hcube (by simpa using S.him) ?_
  simpa using S.re_le_one

/-! ##### From the root data to the two pentagon instances -/

/-- The upper composite argument `A₃ = (1−t)/(1−a·t)`. -/
noncomputable def A3 : ℂ := (1 - (S.t : ℂ)) / (1 - S.a * (S.t : ℂ))

theorem one_sub_t_pos : (0 : ℝ) < 1 - S.t := by linarith [S.ht1]

theorem one_sub_t_cast : (1 : ℂ) - (S.t : ℂ) = ((1 - S.t : ℝ) : ℂ) := by push_cast; ring

theorem den_ne_zero : (1 : ℂ) - S.a * (S.t : ℂ) ≠ 0 := by
  intro hc
  have h : ((1 : ℂ) - S.a * (S.t : ℂ)).im = 0 := by rw [hc]; simp
  simp only [Complex.sub_im, Complex.one_im, zero_sub, neg_eq_zero, Complex.mul_im,
    Complex.ofReal_re, Complex.ofReal_im, mul_zero, zero_add] at h
  exact absurd h (mul_ne_zero (ne_of_gt S.him) (ne_of_gt S.ht0))

theorem den_im_neg : ((1 : ℂ) - S.a * (S.t : ℂ)).im < 0 := by
  simp only [Complex.sub_im, Complex.one_im, zero_sub, Complex.mul_im, Complex.ofReal_re,
    Complex.ofReal_im, mul_zero, zero_add]
  have := mul_pos S.him S.ht0
  linarith

/-- `Im A₃ > 0`: positive real numerator over a denominator below the axis. -/
theorem A3_im_pos : 0 < S.A3.im := by
  have h : S.A3 = ((1 - S.t : ℝ) : ℂ) / (1 - S.a * (S.t : ℂ)) := by
    show (1 - (S.t : ℂ)) / (1 - S.a * (S.t : ℂ)) = _
    rw [S.one_sub_t_cast]
  rw [h]
  exact im_div_ofReal_pos S.one_sub_t_pos S.den_ne_zero S.den_im_neg

theorem mem_a : S.a ∈ rogersDomain := mem_rogersDomain_of_im_ne_zero (ne_of_gt S.him)

theorem mem_A3 : S.A3 ∈ rogersDomain :=
  mem_rogersDomain_of_im_ne_zero (ne_of_gt S.A3_im_pos)

/-- `(1−a)/(1−at) = A₃⁻¹` — Route 55's `(1−a)(1−b) = (1−ab)²` with the pair
`(a, t)` and third root `conj a`. -/
theorem inv_A3 : (1 - S.a) / (1 - S.a * (S.t : ℂ)) = S.A3⁻¹ := by
  have hq := S.den_ne_zero
  have hnum : (1 : ℂ) - (S.t : ℂ) ≠ 0 := by
    rw [S.one_sub_t_cast]; exact_mod_cast S.one_sub_t_pos.ne'
  have hc : (starRingEnd ℂ) S.a ≠ 0 := by simpa using S.ne_zero
  have hcube : ((starRingEnd ℂ) S.a) ^ 3 - 2 * ((starRingEnd ℂ) S.a) ^ 2
      + 3 * ((starRingEnd ℂ) S.a) - 1 = 0 := by
    have h := congrArg (starRingEnd ℂ) S.cubic_a
    simpa [map_ofNat] using h
  have hrec : (1 - S.a) * (1 - (S.t : ℂ)) = (1 - S.a * (S.t : ℂ)) ^ 2 :=
    pentagon_arg_reciprocal (a := S.a) (b := (S.t : ℂ)) (c := (starRingEnd ℂ) S.a)
      (by linear_combination S.hsum) (by linear_combination S.hprod) hcube hc
  show (1 - S.a) / (1 - S.a * (S.t : ℂ)) = ((1 - (S.t : ℂ)) / (1 - S.a * (S.t : ℂ)))⁻¹
  rw [inv_div]
  field_simp
  linear_combination -hrec + (-2 * (S.t : ℂ)) * S.pair_rel + (2 * S.a) * S.cubic_t

/-- `1 − b⁻¹ = 1 − a·t`, since `a·b·t = 1`. -/
theorem one_sub_inv_conj : (1 : ℂ) - ((starRingEnd ℂ) S.a)⁻¹ = 1 - S.a * (S.t : ℂ) := by
  have hb : (starRingEnd ℂ) S.a ≠ 0 := by simpa using S.ne_zero
  field_simp
  linear_combination S.hprod

/-- **The first pentagon instance**, in the capstone's shape. -/
theorem pentagon_upper :
    cRogersL (S.t : ℂ) + cRogersL S.a + cRogersL S.A3
      + cRogersL (1 - ((starRingEnd ℂ) S.a)⁻¹) + cRogersL S.A3⁻¹
      = ((Real.pi ^ 2 / 2 : ℝ) : ℂ) := by
  have h := pentagonSum_eq_pi_sq_div_two S.ht0 S.ht1 S.mem_a
  unfold pentagonSum at h
  rw [S.one_sub_inv_conj, ← S.inv_A3]
  show cRogersL (S.t : ℂ) + cRogersL S.a
      + cRogersL ((1 - (S.t : ℂ)) / (1 - S.a * (S.t : ℂ)))
      + cRogersL (1 - S.a * (S.t : ℂ))
      + cRogersL ((1 - S.a) / (1 - S.a * (S.t : ℂ))) = _
  linear_combination h

/-- The lower composite argument, `B₃ = conj A₃` — the same expression at the
conjugate root, since `t` is real. -/
noncomputable def B3 : ℂ := (starRingEnd ℂ) S.A3

theorem B3_eq : S.B3 = (1 - (S.t : ℂ)) / (1 - (starRingEnd ℂ) S.a * (S.t : ℂ)) := by
  show (starRingEnd ℂ) ((1 - (S.t : ℂ)) / (1 - S.a * (S.t : ℂ))) = _
  simp [map_div₀, map_sub, Complex.conj_ofReal]

theorem B3_im_neg : S.B3.im < 0 := by
  show ((starRingEnd ℂ) S.A3).im < 0
  simpa using S.A3_im_pos

theorem mem_conj_a : (starRingEnd ℂ) S.a ∈ rogersDomain :=
  mem_rogersDomain_of_im_ne_zero (by simpa using ne_of_gt S.him)

theorem inv_B3 :
    (1 - (starRingEnd ℂ) S.a) / (1 - (starRingEnd ℂ) S.a * (S.t : ℂ)) = S.B3⁻¹ := by
  have h := congrArg (starRingEnd ℂ) S.inv_A3
  simpa [map_div₀, map_sub, map_inv₀, Complex.conj_ofReal, SaddleRoots.B3] using h

theorem one_sub_inv_a : (1 : ℂ) - S.a⁻¹ = 1 - (starRingEnd ℂ) S.a * (S.t : ℂ) := by
  have h := congrArg (starRingEnd ℂ) S.one_sub_inv_conj
  simpa [map_sub, map_inv₀, Complex.conj_ofReal] using h

/-- **The second pentagon instance**, the mirror of `pentagon_upper`. -/
theorem pentagon_lower :
    cRogersL (S.t : ℂ) + cRogersL ((starRingEnd ℂ) S.a) + cRogersL S.B3
      + cRogersL (1 - S.a⁻¹) + cRogersL S.B3⁻¹ = ((Real.pi ^ 2 / 2 : ℝ) : ℂ) := by
  have h := pentagonSum_eq_pi_sq_div_two S.ht0 S.ht1 S.mem_conj_a
  unfold pentagonSum at h
  rw [S.one_sub_inv_a, ← S.inv_B3, S.B3_eq]
  linear_combination h


/-! ##### The four logarithms, evaluated

`log a`, `log b`, `log t`, `log A₃`, `log B₃` in terms of `log t` and `arg a`
alone. With these, Route 68's capstone becomes the sum rule's stated form. -/

theorem norm_sq_eq : ‖S.a‖ ^ 2 * S.t = 1 := by
  have h' : Complex.normSq S.a * S.t = 1 := by exact_mod_cast S.normSq_mul
  rwa [← Complex.normSq_eq_norm_sq]

theorem norm_pos : 0 < ‖S.a‖ := norm_pos_iff.mpr S.ne_zero

theorem log_norm : Real.log ‖S.a‖ = -(Real.log S.t) / 2 := by
  have hns := S.norm_sq_eq
  have h := congrArg Real.log hns
  rw [Real.log_mul (pow_pos S.norm_pos 2).ne' S.ht0.ne', Real.log_pow] at h
  simp only [Real.log_one, Nat.cast_ofNat] at h
  linarith

/-- `log a = −½·log t + i·arg a`. -/
theorem log_a : Complex.log S.a
    = -((Real.log S.t : ℝ) : ℂ) / 2 + ((S.a.arg : ℝ) : ℂ) * Complex.I := by
  rw [Complex.log, S.log_norm]
  push_cast
  ring

/-- `log t` is real. -/
theorem log_t : Complex.log (S.t : ℂ) = ((Real.log S.t : ℝ) : ℂ) :=
  clog_of_eq_ofReal S.ht0 rfl

/-- `log (conj a) = −½·log t − i·arg a`. -/
theorem log_conj_a : Complex.log ((starRingEnd ℂ) S.a)
    = -((Real.log S.t : ℝ) : ℂ) / 2 - ((S.a.arg : ℝ) : ℂ) * Complex.I := by
  rw [Complex.log_conj _ (arg_ne_pi_of_im_ne_zero (ne_of_gt S.him)), S.log_a]
  simp only [map_add, map_div₀, map_neg, map_mul, map_ofNat, Complex.conj_ofReal,
    Complex.conj_I]
  ring

theorem den_comm : (1 : ℂ) - (S.t : ℂ) * S.a = 1 - S.a * (S.t : ℂ) := by ring

theorem A3_alt : (1 - (S.t : ℂ)) / (1 - (S.t : ℂ) * S.a) = S.A3 := by
  rw [S.den_comm]; rfl

/-- `3·log A₃ + log a = log t + iπ` — Route 61's angle identity, instantiated. -/
theorem three_log_A3 : 3 * Complex.log S.A3 + Complex.log S.a
    = ((Real.log S.t : ℝ) : ℂ) + (Real.pi : ℂ) * Complex.I := by
  have h := saddle_clog_cube_of_roots (a := S.a) (b := (starRingEnd ℂ) S.a) (t := S.t)
    S.ht0 S.hsum S.hprod S.cubic_t S.ne_zero
    (by rw [S.den_comm]; exact S.den_ne_zero)
    (fun hc => S.one_sub_ne_zero (by linear_combination -hc))
    (by rw [S.A3_alt]; exact ne_zero_of_mem_rogersDomain S.mem_A3)
    (by
      have e1 : (1 : ℂ) - (S.t : ℂ) * ((starRingEnd ℂ) S.a)
          = 1 - ((starRingEnd ℂ) S.a) * (S.t : ℂ) := by ring
      rw [e1, ← S.B3_eq, S.A3_alt]
      rfl)
    (by rw [S.A3_alt]; exact S.A3_im_pos.le) S.him.le
  rwa [S.A3_alt] at h

/-- `log A₃ = ½·log t + i·(π − arg a)/3`. -/
theorem log_A3 : Complex.log S.A3
    = ((Real.log S.t : ℝ) : ℂ) / 2 + (((Real.pi - S.a.arg) / 3 : ℝ) : ℂ) * Complex.I := by
  have h := S.three_log_A3
  rw [S.log_a] at h
  push_cast
  linear_combination h / 3

/-- `log B₃ = ½·log t − i·(π − arg a)/3`. -/
theorem log_B3 : Complex.log S.B3
    = ((Real.log S.t : ℝ) : ℂ) / 2 - (((Real.pi - S.a.arg) / 3 : ℝ) : ℂ) * Complex.I := by
  have harg : S.A3.arg ≠ Real.pi := arg_ne_pi_of_im_ne_zero (ne_of_gt S.A3_im_pos)
  show Complex.log ((starRingEnd ℂ) S.A3) = _
  rw [Complex.log_conj _ harg, S.log_A3]
  simp only [map_add, map_div₀, map_mul, map_ofNat, Complex.conj_ofReal, Complex.conj_I]
  ring


/-! ##### Inhabitation — the cubic really has these roots

Everything above is a theorem about `SaddleRoots`, so it is worth exactly what
the inhabitation is worth. Here it is: the real root by the intermediate value
theorem, the conjugate pair by an explicit square root, and the three symmetric
functions by `Complex.ext`. -/

/-- The saddle cubic has a real root in `(0,1)`: `f(0) = −1 < 0 < 1 = f(1)`. -/
theorem exists_real_root :
    ∃ t : ℝ, 0 < t ∧ t < 1 ∧ t ^ 3 - 2 * t ^ 2 + 3 * t - 1 = 0 := by
  have hcont : ContinuousOn (fun x : ℝ => x ^ 3 - 2 * x ^ 2 + 3 * x - 1) (Set.Icc 0 1) := by
    fun_prop
  have hmem : (0 : ℝ) ∈ Set.Ioo ((0 : ℝ) ^ 3 - 2 * (0 : ℝ) ^ 2 + 3 * (0 : ℝ) - 1)
      ((1 : ℝ) ^ 3 - 2 * (1 : ℝ) ^ 2 + 3 * (1 : ℝ) - 1) := by norm_num
  obtain ⟨t, ht, hft⟩ := intermediate_value_Ioo (by norm_num : (0 : ℝ) ≤ 1) hcont hmem
  exact ⟨t, ht.1, ht.2, hft⟩

/-- The discriminant of the residual quadratic is negative — unconditionally, not
just on `(0,1)`: `3t² − 4t + 8` has discriminant `16 − 96 < 0`. -/
theorem disc_pos (t : ℝ) : 0 < 3 * t ^ 2 - 4 * t + 8 := by nlinarith [sq_nonneg (3 * t - 2)]

/-- **From a real root, a `SaddleRoots`.** The conjugate pair is
`(2−t)/2 ± i·√(3t²−4t+8)/2`, the roots of the residual quadratic
`x² + (t−2)x + (t²−2t+3)`. -/
noncomputable def ofRealRoot {t : ℝ} (h0 : 0 < t) (h1 : t < 1)
    (hc : t ^ 3 - 2 * t ^ 2 + 3 * t - 1 = 0) : SaddleRoots where
  t := t
  a := (((2 - t) / 2 : ℝ) : ℂ) + ((Real.sqrt (3 * t ^ 2 - 4 * t + 8) / 2 : ℝ) : ℂ) * Complex.I
  ht0 := h0
  ht1 := h1
  hsum := by
    simp only [map_add, map_mul, Complex.conj_ofReal, Complex.conj_I]
    push_cast
    ring
  hp2 := by
    have hsq : Real.sqrt (3 * t ^ 2 - 4 * t + 8) ^ 2 = 3 * t ^ 2 - 4 * t + 8 :=
      Real.sq_sqrt (disc_pos t).le
    have hI : Complex.I ^ 2 = -1 := Complex.I_sq
    simp only [map_add, map_mul, Complex.conj_ofReal, Complex.conj_I]
    have hsq' : ((Real.sqrt (3 * t ^ 2 - 4 * t + 8) : ℝ) : ℂ) ^ 2
        = ((3 * t ^ 2 - 4 * t + 8 : ℝ) : ℂ) := by exact_mod_cast hsq
    push_cast at hsq' ⊢
    linear_combination ((1 : ℂ) / 4) * hsq'
      + (-(((Real.sqrt (3 * t ^ 2 - 4 * t + 8) : ℝ) : ℂ) ^ 2) / 4) * hI
  hprod := by
    have hsq : Real.sqrt (3 * t ^ 2 - 4 * t + 8) ^ 2 = 3 * t ^ 2 - 4 * t + 8 :=
      Real.sq_sqrt (disc_pos t).le
    have hI : Complex.I ^ 2 = -1 := Complex.I_sq
    have hsq' : ((Real.sqrt (3 * t ^ 2 - 4 * t + 8) : ℝ) : ℂ) ^ 2
        = ((3 * t ^ 2 - 4 * t + 8 : ℝ) : ℂ) := by exact_mod_cast hsq
    have hcC : ((t : ℝ) : ℂ) ^ 3 - 2 * ((t : ℝ) : ℂ) ^ 2 + 3 * ((t : ℝ) : ℂ) - 1 = 0 := by
      exact_mod_cast hc
    simp only [map_add, map_mul, Complex.conj_ofReal, Complex.conj_I]
    push_cast at hsq' hcC ⊢
    linear_combination ((t : ℂ) / 4) * hsq'
      + (-(((Real.sqrt (3 * t ^ 2 - 4 * t + 8) : ℝ) : ℂ) ^ 2 * (t : ℂ)) / 4) * hI + hcC
  him := by
    simp only [Complex.add_im, Complex.ofReal_im, Complex.mul_im, Complex.ofReal_re,
      Complex.I_re, Complex.I_im, mul_zero, mul_one, zero_add, add_zero]
    exact div_pos (Real.sqrt_pos.mpr (disc_pos t)) two_pos

instance : Nonempty SaddleRoots := by
  obtain ⟨t, h0, h1, hc⟩ := exists_real_root
  exact ⟨ofRealRoot h0 h1 hc⟩

end SaddleRoots

end SaddleStructure

/-! ### Complex Rogers reflection

The corpus had `Li₂` **inversion** on `ℂ` but no complex **reflection**. It is
now available, and cheaply: `L′(z) − L′(1−z) = 0` *identically* as a rational
expression — the Rogers half is exactly what makes reflection differentiate to
nothing — and `rogersDomain` is invariant under `z ↦ 1−z` (it is `ℂ` minus both
real cuts, and the involution swaps them). So constancy is immediate on an open
connected set, and the constant is pinned at the real point `1/2` by the real
reflection already proved in the corpus.

With inversion (`MathlibExt.cRogersL_add_inv`) this makes the whole anharmonic
group act on `cRogersL`, which is what Route 58's links G3 and G4 are
evaluations in. -/

section Reflection

open QOU.QBeta.FiveTwoRogersReflection

/-- `rogersDomain` is invariant under `z ↦ 1 − z`: the involution swaps the two
cuts `(−∞,0]` and `[1,∞)`. -/
theorem one_sub_mem_rogersDomain_iff {z : ℂ} :
    (1 : ℂ) - z ∈ rogersDomain ↔ z ∈ rogersDomain := by
  have key : (1 : ℂ) - ((1 : ℂ) - z) = z := by ring
  have h1 : z ∈ Complex.slitPlane ↔ ((1 : ℂ) - z ∈ notCut) := by
    have h := one_sub_mem_slitPlane_iff (z := (1 : ℂ) - z)
    rwa [key] at h
  constructor
  · rintro ⟨hs, hn⟩
    exact ⟨h1.mpr hn, one_sub_mem_slitPlane_iff.mp hs⟩
  · rintro ⟨hs, hn⟩
    exact ⟨one_sub_mem_slitPlane_iff.mpr hn, h1.mp hs⟩

/-- **`L(z) + L(1−z)` has vanishing derivative** — identically, with no branch
condition. This is the Rogers normalisation's whole point. -/
theorem hasDerivAt_cRogersL_reflect {z : ℂ} (hz : z ∈ rogersDomain) :
    HasDerivAt (fun w : ℂ => cRogersL w + cRogersL (1 - w)) 0 z := by
  have hz' : (1 : ℂ) - z ∈ rogersDomain := one_sub_mem_rogersDomain_iff.mpr hz
  have h0 : z ≠ 0 := ne_zero_of_mem_rogersDomain hz
  have h1 : (1 : ℂ) - z ≠ 0 := one_sub_ne_zero_of_mem_rogersDomain hz
  have hinner : HasDerivAt (fun w : ℂ => 1 - w) (-1) z := by
    simpa using (hasDerivAt_const z (1 : ℂ)).sub (hasDerivAt_id z)
  have d1 := hasDerivAt_cRogersL_of_mem hz
  have d2 := hasDerivAt_cRogersL_comp hinner hz'
  refine (d1.add d2).congr_deriv ?_
  rw [show (1 : ℂ) - (1 - z) = z by ring]
  field_simp
  ring

/-- **Complex Rogers reflection.** `L(z) + L(1−z) = π²/6` on all of
`rogersDomain` — every `z` off both real cuts, no branch hypothesis.

The constant is pinned at `z = 1/2`, where `cRogersL_ofReal` and the corpus's
real `rogersL_reflection` give it outright. -/
theorem cRogersL_add_one_sub {z : ℂ} (hz : z ∈ rogersDomain) :
    cRogersL z + cRogersL (1 - z) = ((Real.pi ^ 2 / 6 : ℝ) : ℂ) := by
  have hbase : ((1 / 2 : ℝ) : ℂ) ∈ rogersDomain :=
    ofReal_mem_rogersDomain (by norm_num) (by norm_num)
  have hconst := isOpen_rogersDomain.is_const_of_deriv_eq_zero isPreconnected_rogersDomain
    (fun w hw => (hasDerivAt_cRogersL_reflect hw).differentiableAt.differentiableWithinAt)
    (fun w hw => (hasDerivAt_cRogersL_reflect hw).deriv) hz hbase
  rw [hconst, show (1 : ℂ) - ((1 / 2 : ℝ) : ℂ) = ((1 / 2 : ℝ) : ℂ) by push_cast; ring,
    cRogersL_ofReal (by norm_num) (by norm_num)]
  have hr := rogersL_reflection (x := (1 / 2 : ℝ)) (by norm_num) (by norm_num)
  rw [show (1 : ℝ) - 1 / 2 = 1 / 2 by norm_num] at hr
  rw [← Complex.ofReal_add, hr]

/-- **The anharmonic relation, evaluated.** Reflection at `1/z` minus inversion:

    L(1 − 1/z) − L(z) = π²/3 + ½·log(−z)² − ½·log z·log(−z)

`z ↦ 1 − 1/z` is the order-3 element of the anharmonic group, and Route 55 showed
it carries the 5₂ saddle cubic onto `X³ − X + 1`. This is that map read on `L`,
and it is the analytic content of Route 58's link G4 — what remains there is
evaluating the two logarithms, i.e. branch pinning. -/
theorem cRogersL_one_sub_inv_sub {z : ℂ} (hz : z ∈ invDomain) (harg : z.arg ≠ Real.pi)
    (hzi : z⁻¹ ∈ rogersDomain) :
    cRogersL (1 - z⁻¹) - cRogersL z
      = ((Real.pi ^ 2 / 3 : ℝ) : ℂ) + Complex.log (-z) ^ 2 / 2
        - Complex.log z * Complex.log (-z) / 2 := by
  have h1 := cRogersL_add_one_sub hzi
  have h2 := cRogersL_add_inv hz harg
  push_cast at h1 h2 ⊢
  linear_combination h1 - h2

/-- A point off the real axis has its inverse off both cuts. -/
theorem inv_mem_rogersDomain_of_im_ne_zero {z : ℂ} (h : z.im ≠ 0) : z⁻¹ ∈ rogersDomain := by
  refine mem_rogersDomain_of_im_ne_zero ?_
  rw [Complex.inv_im]
  have hz : z ≠ 0 := fun hc => h (by rw [hc]; simp)
  exact div_ne_zero (neg_ne_zero.mpr h) (fun hc => hz (Complex.normSq_eq_zero.mp hc))

/-- **The anharmonic relation, with the `log(−z)` eliminated.**

    L(1 − 1/z) − L(z) = −π²/6 + (iπ/2)·log z          for `Im z < 0`

As with inversion, the `log²` terms cancel completely: below the real axis the
order-3 anharmonic step costs `π²` plus `π` times a single logarithm. This is the
form Route 58's link G4 uses — its value has no `log²` for the same reason G3's
does not. -/
theorem cRogersL_one_sub_inv_sub_of_im_neg {z : ℂ} (h : z.im < 0) :
    cRogersL (1 - z⁻¹) - cRogersL z
      = -((Real.pi ^ 2 / 6 : ℝ) : ℂ)
        + ((Real.pi : ℂ) * Complex.I / 2) * Complex.log z := by
  have hne : z.im ≠ 0 := ne_of_lt h
  rw [cRogersL_one_sub_inv_sub (mem_invDomain_of_im_ne_zero hne)
      (arg_ne_pi_of_im_ne_zero hne) (inv_mem_rogersDomain_of_im_ne_zero hne),
    clog_neg_of_im_neg h]
  have hI : Complex.I ^ 2 = -1 := Complex.I_sq
  push_cast
  linear_combination (((Real.pi : ℂ) ^ 2) / 2) * hI

/-- **The anharmonic relation above the real axis.** The mirror of
`cRogersL_one_sub_inv_sub_of_im_neg`:

    L(1 − 1/z) − L(z) = −π²/6 − (iπ/2)·log z      for `Im z > 0`

With the four one-log forms — inversion and the anharmonic step, each on both
sides of the axis — the anharmonic group's action on `cRogersL` is completely
tabulated, and every evaluation Route 58 needs is a substitution. -/
theorem cRogersL_one_sub_inv_sub_of_im_pos {z : ℂ} (h : 0 < z.im) :
    cRogersL (1 - z⁻¹) - cRogersL z
      = -((Real.pi ^ 2 / 6 : ℝ) : ℂ)
        - ((Real.pi : ℂ) * Complex.I / 2) * Complex.log z := by
  have hne : z.im ≠ 0 := ne_of_gt h
  rw [cRogersL_one_sub_inv_sub (mem_invDomain_of_im_ne_zero hne)
      (arg_ne_pi_of_im_ne_zero hne) (inv_mem_rogersDomain_of_im_ne_zero hne),
    clog_neg_of_im_pos h]
  have hI : Complex.I ^ 2 = -1 := Complex.I_sq
  push_cast
  linear_combination (((Real.pi : ℂ) ^ 2) / 2) * hI

/-! ### The assembly: `Σ L` over the saddle orbit, from two pentagon instances

Route 58's chain, as one lemma. The two pentagon instances are `Route 54` at
`(y₃, y₁)` and `(y₃, y₂)`; the four evaluations are the one-log forms above; and
what comes out is the orbit sum in terms of **four logarithms and `π²`** — no
dilogarithm on the right.

Nothing here is about the 5₂ cubic in particular: it is bookkeeping over the
anharmonic toolkit, and the caller supplies the geometry (`a₅ = 1/a₃`,
`a₄ = 1 − 1/b`, and which root sits above the axis). -/

/-- **The orbit sum, from two pentagon instances and the four one-log
evaluations.**

    2·(L(c) + L(a) + L(b)) = 2π²/3 − (iπ/2)·(log A₃ − log B₃ + log b − log a)

With `b = conj a`, `B₃ = conj A₃` and `c` real, the bracket is `2i·(arg A₃ −
arg a)` and this reads `Σ L = π²/3 + (π/2)(arg A₃ − arg a)`. Route 61's
`saddle_clog_cube_of_roots` then supplies `arg A₃`, and Route 47's closed form
follows.

⚠ The two pentagon values are hypotheses here. They are theorems —
`pentagonSum_eq_pi_sq_div_two` — but stating them as inputs keeps this lemma pure
bookkeeping. -/
theorem saddle_sum_cRogersL {a b c A3 B3 : ℂ}
    (P1 : cRogersL c + cRogersL a + cRogersL A3 + cRogersL (1 - b⁻¹) + cRogersL A3⁻¹
      = ((Real.pi ^ 2 / 2 : ℝ) : ℂ))
    (P2 : cRogersL c + cRogersL b + cRogersL B3 + cRogersL (1 - a⁻¹) + cRogersL B3⁻¹
      = ((Real.pi ^ 2 / 2 : ℝ) : ℂ))
    (hA3 : 0 < A3.im) (hB3 : B3.im < 0) (ha : 0 < a.im) (hb : b.im < 0) :
    2 * (cRogersL c + cRogersL a + cRogersL b)
      = ((2 * Real.pi ^ 2 / 3 : ℝ) : ℂ)
        - ((Real.pi : ℂ) * Complex.I / 2)
          * (Complex.log A3 - Complex.log B3 + Complex.log b - Complex.log a) := by
  have e1 := cRogersL_add_inv_of_im_pos hA3
  have e2 := cRogersL_add_inv_of_im_neg hB3
  have e3 := cRogersL_one_sub_inv_sub_of_im_neg hb
  have e4 := cRogersL_one_sub_inv_sub_of_im_pos ha
  push_cast at P1 P2 e1 e2 e3 e4 ⊢
  linear_combination P1 + P2 - e1 - e2 - e3 - e4

/-! ### The bridge from `Σ L` to `A` — Route 58's link G6

`cRogersL` differs from `cLiTwoExt` by `½·log z·log(1−z)`, so the orbit sums
differ by `½·Σ log y·log(1−y)`. That sum is **not** obviously elementary — but the
saddle branch equation `2·log y − 3·log(1−y) = 2πi·ε` makes it so, because it
turns each `log(1−y)` into a multiple of `log y`.

The lemma below is stated for *any* three branch equations, with the `ε` free: it
is the branch equation doing the work, not anything about the 5₂ cubic. -/

/-- **The log·log sum, from three branch equations.**

    Σ lⱼ·mⱼ = (2/3)·Σ lⱼ² − (2πi/3)·Σ εⱼ·lⱼ        given 2lⱼ − 3mⱼ = 2πi·εⱼ

`lⱼ` stands for `log yⱼ` and `mⱼ` for `log(1−yⱼ)`. Nothing quadratic in `m`
survives — that is the whole point, and it is why `A` inherits `Σ L`'s
elementary shape. -/
theorem sum_log_mul_log_one_sub {l₁ l₂ l₃ m₁ m₂ m₃ e₁ e₂ e₃ : ℂ}
    (h₁ : 2 * l₁ - 3 * m₁ = 2 * (Real.pi : ℂ) * Complex.I * e₁)
    (h₂ : 2 * l₂ - 3 * m₂ = 2 * (Real.pi : ℂ) * Complex.I * e₂)
    (h₃ : 2 * l₃ - 3 * m₃ = 2 * (Real.pi : ℂ) * Complex.I * e₃) :
    l₁ * m₁ + l₂ * m₂ + l₃ * m₃
      = (2 / 3) * (l₁ ^ 2 + l₂ ^ 2 + l₃ ^ 2)
        - (2 * (Real.pi : ℂ) * Complex.I / 3) * (e₁ * l₁ + e₂ * l₂ + e₃ * l₃) := by
  linear_combination (-(l₁ / 3)) * h₁ + (-(l₂ / 3)) * h₂ + (-(l₃ / 3)) * h₃

/-- `Σ Li₂ = Σ L − ½·Σ log·log`, by the definition of `cRogersL`. This is the
whole of the `Σ L` ↔ `A` conversion; the content is in evaluating the second sum. -/
theorem sum_cLiTwoExt_eq_sum_cRogersL_sub {a b c : ℂ} :
    cLiTwoExt a + cLiTwoExt b + cLiTwoExt c
      = (cRogersL a + cRogersL b + cRogersL c)
        - (Complex.log a * Complex.log (1 - a) + Complex.log b * Complex.log (1 - b)
            + Complex.log c * Complex.log (1 - c)) / 2 := by
  unfold cRogersL
  ring

/-- **`A` from the orbit sum and the branch data**, with no dilogarithm on the
right beyond the orbit sum itself:

    2·Σ Li₂(yⱼ) = 2·Σ L(yⱼ) − (2/3)·Σ log²yⱼ + (2πi/3)·Σ εⱼ·log yⱼ

Combined with `saddle_sum_cRogersL` this expresses `A` in **logarithms and `π²`
alone** — which is Route 58's chain, end to end, modulo the branch equations
themselves. -/
theorem sum_cLiTwoExt_of_branch {a b c e₁ e₂ e₃ : ℂ}
    (h₁ : 2 * Complex.log a - 3 * Complex.log (1 - a)
      = 2 * (Real.pi : ℂ) * Complex.I * e₁)
    (h₂ : 2 * Complex.log b - 3 * Complex.log (1 - b)
      = 2 * (Real.pi : ℂ) * Complex.I * e₂)
    (h₃ : 2 * Complex.log c - 3 * Complex.log (1 - c)
      = 2 * (Real.pi : ℂ) * Complex.I * e₃) :
    2 * (cLiTwoExt a + cLiTwoExt b + cLiTwoExt c)
      = 2 * (cRogersL a + cRogersL b + cRogersL c)
        - (2 / 3) * (Complex.log a ^ 2 + Complex.log b ^ 2 + Complex.log c ^ 2)
        + (2 * (Real.pi : ℂ) * Complex.I / 3)
          * (e₁ * Complex.log a + e₂ * Complex.log b + e₃ * Complex.log c) := by
  have hbridge := sum_cLiTwoExt_eq_sum_cRogersL_sub (a := a) (b := b) (c := c)
  have hll := sum_log_mul_log_one_sub h₁ h₂ h₃
  linear_combination 2 * hbridge + (-1 : ℂ) * hll

/-- **Route 58's chain, end to end.**

    2·Σ Li₂(yⱼ) = 2π²/3 − (iπ/2)·(log A₃ − log B₃ + log b − log a)
                  − (2/3)·Σ log²yⱼ + (2πi/3)·Σ εⱼ·log yⱼ

The left side is twice the sum rule's `A`. The right side has **no dilogarithm in
it at all** — only `π²` and logarithms of the roots. Everything on the way here is
proved: the two pentagon instances are `pentagonSum_eq_pi_sq_div_two`, the four
evaluations are the one-log forms, and the bridge is the branch equations.

⚠ The inputs that remain are the two pentagon values (theorems), the branch
equations (`hε`), and — to turn the right side into `−π²/6 − ½log²y₃ +
(2/3)(θ−π)²` — the root-data facts `|y₁|²y₃ = 1`, `y₂ = conj y₁`, and
`arg A₃ = (π − arg y₁)/3` (`saddle_clog_cube_of_roots`). None of the latter is
discharged here.

**The 5₂ sum rule is PROVED**: `FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms. -/
theorem sum_cLiTwoExt_eval {a b c A3 B3 e₁ e₂ e₃ : ℂ}
    (P1 : cRogersL c + cRogersL a + cRogersL A3 + cRogersL (1 - b⁻¹) + cRogersL A3⁻¹
      = ((Real.pi ^ 2 / 2 : ℝ) : ℂ))
    (P2 : cRogersL c + cRogersL b + cRogersL B3 + cRogersL (1 - a⁻¹) + cRogersL B3⁻¹
      = ((Real.pi ^ 2 / 2 : ℝ) : ℂ))
    (hA3 : 0 < A3.im) (hB3 : B3.im < 0) (ha : 0 < a.im) (hb : b.im < 0)
    (h₁ : 2 * Complex.log a - 3 * Complex.log (1 - a)
      = 2 * (Real.pi : ℂ) * Complex.I * e₁)
    (h₂ : 2 * Complex.log b - 3 * Complex.log (1 - b)
      = 2 * (Real.pi : ℂ) * Complex.I * e₂)
    (h₃ : 2 * Complex.log c - 3 * Complex.log (1 - c)
      = 2 * (Real.pi : ℂ) * Complex.I * e₃) :
    2 * (cLiTwoExt a + cLiTwoExt b + cLiTwoExt c)
      = ((2 * Real.pi ^ 2 / 3 : ℝ) : ℂ)
        - ((Real.pi : ℂ) * Complex.I / 2)
          * (Complex.log A3 - Complex.log B3 + Complex.log b - Complex.log a)
        - (2 / 3) * (Complex.log a ^ 2 + Complex.log b ^ 2 + Complex.log c ^ 2)
        + (2 * (Real.pi : ℂ) * Complex.I / 3)
          * (e₁ * Complex.log a + e₂ * Complex.log b + e₃ * Complex.log c) := by
  have h := saddle_sum_cRogersL P1 P2 hA3 hB3 ha hb
  have k := sum_cLiTwoExt_of_branch h₁ h₂ h₃
  linear_combination k + h

/-- **Route 64's capstone, with every hypothesis discharged from the root data.**

    2·Σ Li₂ = 2π²/3 − (iπ/2)(log A₃ − log B₃ + log b − log a)
              − (2/3)·Σ log² + (2πi/3)·Σ εⱼ·log yⱼ

The pentagon values are `pentagon_upper` / `pentagon_lower`, the imaginary-part
conditions are `A3_im_pos` / `B3_im_neg`, and the three branch equations are
`branch_upper` / `branch_lower` / `branch_real` — all theorems about
`SaddleRoots`. **Nothing is assumed beyond the structure.**

⚠ The right side is still logarithms, not `−π²/6 − ½log²t + (2/3)(θ−π)²`. Turning
it into that needs `arg A₃ = (π − arg a)/3` (`saddle_clog_cube_of_roots`, proved
from root data) and `log a = −½log t + i·arg a` (`normSq_mul`, proved, plus the
argument). Those substitutions are not made here.

**The 5₂ sum rule is PROVED**: `FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms. -/
theorem SaddleRoots.sum_cLiTwoExt_root_data (S : SaddleRoots) :
    2 * (cLiTwoExt S.a + cLiTwoExt ((starRingEnd ℂ) S.a) + cLiTwoExt (S.t : ℂ))
      = ((2 * Real.pi ^ 2 / 3 : ℝ) : ℂ)
        - ((Real.pi : ℂ) * Complex.I / 2)
          * (Complex.log S.A3 - Complex.log S.B3
              + Complex.log ((starRingEnd ℂ) S.a) - Complex.log S.a)
        - (2 / 3) * (Complex.log S.a ^ 2 + Complex.log ((starRingEnd ℂ) S.a) ^ 2
            + Complex.log (S.t : ℂ) ^ 2)
        + (2 * (Real.pi : ℂ) * Complex.I / 3)
          * ((1 : ℂ) * Complex.log S.a + (-1 : ℂ) * Complex.log ((starRingEnd ℂ) S.a)
              + (0 : ℂ) * Complex.log (S.t : ℂ)) := by
  refine sum_cLiTwoExt_eval S.pentagon_upper S.pentagon_lower S.A3_im_pos S.B3_im_neg
    S.him (by simpa using S.him) ?_ ?_ ?_
  · rw [S.branch_upper]; ring
  · rw [S.branch_lower]; ring
  · rw [S.branch_real]; ring

/-- **The sum rule's stated form, from the root data.**

    Σ Li₂ = −π²/6 − ½·log²t + (2/3)·(arg a − π)²

Every logarithm in Route 68's capstone has been evaluated: `log a`, `log b` from
the modulus relation `‖a‖²·t = 1`, and `log A₃`, `log B₃` from Route 61's angle
identity. What is left is `π²`, `log t` and `arg a`.

This is the sum rule's **shape**, reached from `SaddleRoots` — a structure whose
fields are facts about the cubic. On its own it would say nothing about the
actual 5₂ saddle sum `A`; that needs `SaddleRoots` to be inhabited by the actual
roots, which `SaddleRoots.ofRealRoot` and `instance : Nonempty SaddleRoots`
establish (below, from the intermediate value theorem and an explicit square
root). `fiveTwo_saddle_sum_rule` is this theorem with that instance supplied.

**The 5₂ sum rule is PROVED**:
`QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms. -/
theorem SaddleRoots.sum_cLiTwoExt_closed (S : SaddleRoots) :
    2 * (cLiTwoExt S.a + cLiTwoExt ((starRingEnd ℂ) S.a) + cLiTwoExt (S.t : ℂ))
      = ((2 * (-(Real.pi ^ 2 / 6) - Real.log S.t ^ 2 / 2
          + (2 / 3) * (S.a.arg - Real.pi) ^ 2) : ℝ) : ℂ) := by
  have h := S.sum_cLiTwoExt_root_data
  rw [S.log_A3, S.log_B3, S.log_a, S.log_conj_a, S.log_t] at h
  rw [h]
  have hI : Complex.I ^ 2 = -1 := Complex.I_sq
  push_cast
  linear_combination (-((Real.pi : ℂ) ^ 2) / 3 + (8 / 3) * (Real.pi : ℂ) * (S.a.arg : ℂ)
    - (4 / 3) * (S.a.arg : ℂ) ^ 2) * hI

/-! ### The 5₂ saddle sum rule, for the actual roots

`SaddleRoots` is inhabited (`ofRealRoot`, from the intermediate value theorem),
so the closed form is a statement about the **actual** roots of
`X³ − 2X² + 3X − 1` and not merely about a structure. -/

/-- **The 5₂ saddle sum rule.**

There are three roots of `X³ − 2X² + 3X − 1` — one real in `(0,1)` and a
conjugate pair — and

    Σ Li₂(yⱼ) = −π²/6 − ½·log²y₃ + (2/3)·(arg y₁ − π)²

with `Li₂` the corpus's integral continuation `cLiTwoExt`, which agrees with the
principal branch off `[1,∞)`. This is the quantity the lane calls `A`, and the
right side is the expression the corpus records as the sum rule's target.

The chain: the complex five-term identity (Route 54) at `(y₃, y₁)` and
`(y₃, y₂)`; the anharmonic evaluations (59, 60, 62, 63); the branch equations
from `y² = (1−y)³` (65); the root data (66–68); and the logarithm evaluations
(69). Every step is sorry-free with the standard axioms. -/
theorem fiveTwo_saddle_sum_rule :
    ∃ (t : ℝ) (a : ℂ), 0 < t ∧ t < 1 ∧ 0 < a.im
      ∧ (t : ℂ) ^ 3 - 2 * (t : ℂ) ^ 2 + 3 * (t : ℂ) - 1 = 0
      ∧ a ^ 3 - 2 * a ^ 2 + 3 * a - 1 = 0
      ∧ ((starRingEnd ℂ) a) ^ 3 - 2 * ((starRingEnd ℂ) a) ^ 2
          + 3 * ((starRingEnd ℂ) a) - 1 = 0
      ∧ cLiTwoExt a + cLiTwoExt ((starRingEnd ℂ) a) + cLiTwoExt (t : ℂ)
        = ((-(Real.pi ^ 2 / 6) - Real.log t ^ 2 / 2
            + (2 / 3) * (a.arg - Real.pi) ^ 2 : ℝ) : ℂ) := by
  obtain ⟨t, h0, h1, hc⟩ := SaddleRoots.exists_real_root
  set S := SaddleRoots.ofRealRoot h0 h1 hc with hS
  refine ⟨t, S.a, h0, h1, S.him, ?_, S.cubic_a, S.cubic_conj_a, ?_⟩
  · exact S.cubic_t
  · have hst : S.t = t := rfl
    have h := S.sum_cLiTwoExt_closed
    rw [hst] at h
    push_cast at h ⊢
    linear_combination h / 2

/-- **The corpus's own conjecture, proved.**

`QOU.QBeta.FiveTwo.FiveTwoSaddleSumRule` is stated there as a class with no
instance — "numerically verified, not proved". With `Vⱼ = 3·Li₂(yⱼ) +
(log yⱼ + bⱼπi)²` and `b = (−1, +1, +1)` on `(y₁, y₂, y₃)`,

    Σⱼ Vⱼ = −3π²/2 + 2π·log(y₃)·i

so `Σⱼ Re Vⱼ = −3π²/2`, which is the class's field. Both halves are elementary,
as the lane's probes measured — the real part is the conjecture, the imaginary
part `2π·log y₃`. -/
theorem fiveTwo_sum_V :
    ∃ (t : ℝ) (a : ℂ), 0 < t ∧ t < 1 ∧ 0 < a.im
      ∧ (t : ℂ) ^ 3 - 2 * (t : ℂ) ^ 2 + 3 * (t : ℂ) - 1 = 0
      ∧ a ^ 3 - 2 * a ^ 2 + 3 * a - 1 = 0
      ∧ ((starRingEnd ℂ) a) ^ 3 - 2 * ((starRingEnd ℂ) a) ^ 2
          + 3 * ((starRingEnd ℂ) a) - 1 = 0
      ∧ (3 * cLiTwoExt a + (Complex.log a + (-1 : ℂ) * (Real.pi : ℂ) * Complex.I) ^ 2)
        + (3 * cLiTwoExt ((starRingEnd ℂ) a)
            + (Complex.log ((starRingEnd ℂ) a) + (1 : ℂ) * (Real.pi : ℂ) * Complex.I) ^ 2)
        + (3 * cLiTwoExt (t : ℂ)
            + (Complex.log (t : ℂ) + (1 : ℂ) * (Real.pi : ℂ) * Complex.I) ^ 2)
        = ((-3 * (Real.pi ^ 2 / 2) : ℝ) : ℂ)
          + ((2 * Real.pi * Real.log t : ℝ) : ℂ) * Complex.I := by
  obtain ⟨t, h0, h1, hc⟩ := SaddleRoots.exists_real_root
  set S := SaddleRoots.ofRealRoot h0 h1 hc with hS
  have hst : S.t = t := rfl
  refine ⟨t, S.a, h0, h1, S.him, ?_, S.cubic_a, S.cubic_conj_a, ?_⟩
  · exact S.cubic_t
  · have hsum := S.sum_cLiTwoExt_closed
    have hla := S.log_a
    have hlb := S.log_conj_a
    have hlt := S.log_t
    rw [hst] at hsum hla hlb hlt
    rw [hla, hlb, hlt]
    have hI : Complex.I ^ 2 = -1 := Complex.I_sq
    push_cast at hsum ⊢
    linear_combination (3 / 2 : ℂ) * hsum
      + (2 * (S.a.arg : ℂ) ^ 2 - 4 * (Real.pi : ℂ) * (S.a.arg : ℂ)
          + 3 * (Real.pi : ℂ) ^ 2) * hI

/-- **`FiveTwoSaddleSumRule`, instantiated.**

`QOU.QBeta.FiveTwo.FiveTwoSaddleSumRule` is declared there as a class with no
instance, with the comment "No instance is provided: the statement is open".
Here is the instance, for `Li = cLiTwoExt`, `y = (y₁, y₂, y₃)` the three roots of
the saddle cubic, and `b = (−1, +1, +1)`. -/
theorem fiveTwoSaddleSumRule_holds :
    ∃ (t : ℝ) (a : ℂ), 0 < t ∧ t < 1 ∧ 0 < a.im
      ∧ (t : ℂ) ^ 3 - 2 * (t : ℂ) ^ 2 + 3 * (t : ℂ) - 1 = 0
      ∧ a ^ 3 - 2 * a ^ 2 + 3 * a - 1 = 0
      ∧ ((starRingEnd ℂ) a) ^ 3 - 2 * ((starRingEnd ℂ) a) ^ 2
          + 3 * ((starRingEnd ℂ) a) - 1 = 0
      ∧ FiveTwoSaddleSumRule cLiTwoExt ![a, (starRingEnd ℂ) a, (t : ℂ)] ![-1, 1, 1] := by
  obtain ⟨t, a, h0, h1, him, hct, hca, hcb, hV⟩ := fiveTwo_sum_V
  refine ⟨t, a, h0, h1, him, hct, hca, hcb, ⟨?_⟩⟩
  rw [Fin.sum_univ_three]
  simp only [Matrix.cons_val_zero, Matrix.cons_val_one]
  rw [show (![a, (starRingEnd ℂ) a, (t : ℂ)] 2) = (t : ℂ) from rfl,
    show (![(-1 : ℂ), 1, 1] 2) = (1 : ℂ) from rfl, hV]
  simp only [Complex.add_re, Complex.mul_re, Complex.ofReal_re, Complex.ofReal_im,
    Complex.I_re, Complex.I_im, mul_zero, sub_zero, mul_one, add_zero]

end Reflection


end QOU.QBeta.FiveTwoComplexPentagon
