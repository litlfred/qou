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

## Why the branch conditions are hypotheses — and how far they travel

They are not identities. `log a₃ = log(1−x) − log(1−xy)` fails whenever the two
sides land on different sheets, and Route 45 measured the pentagon sum drifting
by exactly that amount. So they enter as hypotheses. But they are not *stuck*
there, and that is the second half of this module:

* `pentagon_branch_conditions_of_real` — all five hold on the positive real
  square `0 < x, y < 1`. This is first of all a **non-vacuity** check: an
  unsatisfiable hypothesis set would make `hasDerivAt_pentagonSum` prove
  anything, and nothing in its statement rules that out.
* each **defect** `d₃ = log a₃ − log(1−w) + log(1−wy)` and its four companions is
  holomorphic where the logarithms are, with derivative identically `0`
  (`hasDerivAt_defectThree` …). Hence `eq_zero_of_hasDerivAt_zero`: a defect that
  vanishes at one point of an open connected region vanishes on all of it.
* so `pentagonSum_eq_of_region_of_real` — on **any** open connected set of `x` on
  which the pentagon stays regular and which contains a real point of `(0,1)`,
  the complex five-term sum is constant.

And the constant is a number. `cRogersL` at a real point of `(0,1)` **is** the
corpus's real `rogersL` (`cRogersL_ofReal` — the complex and real `Li₂` series
are literally the same series), and the real pentagon sum is `π²/2`
(`rogersL_pentagon`, from `FiveTwoAbelFiveTerm.rogersL_fiveTerm` plus three
reflections). So `pentagonSum_eq_pi_sq_div_two_of_region` is a **complex
five-term identity**, at every point of the region including points where
nothing is real.

The branch bookkeeping is therefore reduced to a single geometric question:
*does such a region exist?* That is the honest residue of Routes 45–46 — no
longer bookkeeping, but a statement about a region.

## ⚠ What this does NOT do

It exhibits **no** region for the 5₂ saddle values `y₁, y₂`, and that is not an
oversight: a regular region reaching the real square *forces* the naive log
expansions, so where the flattening is non-trivial no such region can exist. The
obstruction (Neumann's `ker ν`) and the missing region are the same fact seen
twice.

The **real** five-term identity on `(0,1)` is separately proved, sorry-free, in
`QOU/QBeta/FiveTwoAbelFiveTerm.lean` (`rogersL_fiveTerm`); what this lane needs
and does not have is the complex one *at the saddle*, because the 5₂ saddle roots
`y₁, y₂` are complex with `|y₁| = 1.52 > 1`.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

-- Ref: [neumann2004] uploads/0307092v2.pdf, Prop 2.5
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

⚠ The hypothesis `hreg` is the whole difficulty. Nothing here produces such a
set for the 5₂ saddle values. **The 5₂ sum rule remains verified to 80 dps,
unproved.** -/
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

**The 5₂ sum rule remains verified to 80 dps, unproved.** -/
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

end QOU.QBeta.FiveTwoComplexPentagon
