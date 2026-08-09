/-
# The complex pentagon, assembled: `d/dx Σ L = 0` for `cRogersL`

Bean `qou-xblo`. This is the **chain-rule assembly** — the piece that turns the
algebra of `FiveTwoSaddleSumRule.pentagon_deriv_x_eq_zero` (§7h) into a statement
about the actual analytic function `MathlibExt.cRogersL`.

## What is proved

`pentagonSum y` is the five-term sum

    L(x) + L(y) + L((1−x)/(1−xy)) + L(1−xy) + L((1−y)/(1−xy))

with `L = cRogersL` the Rogers dilogarithm on `ℂ ∖ ((−∞,0] ∪ [1,∞))`. Given

* membership of `rogersDomain` at the four `x`-dependent arguments, and
* the five **branch conditions** — the log expansions of the composite arguments —

its `x`-derivative is `0` (`hasDerivAt_pentagonSum`). The three chain-rule
factors `(y−1)/(1−xy)²`, `−y`, `(1−y)y/(1−xy)²` that §7h assumed are now proved
(`hasDerivAt_argThree/Four/Five`), so nothing about the differentiation is taken
on faith any more.

## Why the branch conditions stay as hypotheses

They are not identities. `log a₃ = log(1−x) − log(1−xy)` fails whenever the two
sides land on different sheets, and Route 45 measured the pentagon sum drifting
by exactly that amount. Making them hypotheses is the honest encoding: this
module proves the pentagon is locally constant *wherever they hold*, and says
nothing about where that is.

`pentagon_branch_conditions_of_real` then shows the hypothesis set is
**satisfiable** — every one of them holds on the positive real square
`0 < x, y < 1`. That matters because an unsatisfiable hypothesis set would make
`hasDerivAt_pentagonSum` vacuous, and nothing in its statement rules that out.

## ⚠ What this does NOT do

It does not prove the five-term identity for `cRogersL`. Two things are still
owed: continuation of the branch conditions off the real square (Neumann's
`ker ν` again, not a formality), and pinning the constant. The **real** five-term
identity on `(0,1)` is separately proved, sorry-free, in
`QOU/QBeta/FiveTwoAbelFiveTerm.lean` (`rogersL_fiveTerm`); what this lane needs
and does not have is the complex one, because the 5₂ saddle roots `y₁, y₂` are
complex with `|y₁| = 1.52 > 1`.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

-- Ref: [neumann2004] uploads/0307092v2.pdf, Prop 2.5
-/
import QOU.MathlibExt.ComplexRogersDilog
import QOU.QBeta.FiveTwoSaddleSumRule

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

end QOU.QBeta.FiveTwoComplexPentagon
