import QOU.Archimedean.DilogReflection

/-!
# Rogers reflection, from the corpus's real `LiTwo`

Bean `qou-rhyp`, item 1 — discharging four of the nine hypotheses that
`FiveTwoLevelSevenLadder.lean` takes abstractly.

`FiveTwoLevelSevenLadder.numerators_of_five_term` assumes `L (1 − x) = L1 − L x`
at four points. With Rogers `L` built from the corpus's real dilogarithm this is
not a new analytic fact: it follows from `LiTwo_reflection'`, which is already
**sorry-free** in `QOU/Archimedean/DilogReflection.lean`.

The reason it is free is a cancellation worth stating. Euler reflection carries a
correction term,

    LiTwo x + LiTwo (1 − x) = π²/6 − log x · log (1 − x),

and Rogers' two **half** `log·log` terms add to a **whole** one:

    L x + L (1 − x)
      = LiTwo x + LiTwo (1 − x) + ½·log x·log(1−x) + ½·log(1−x)·log x
      = LiTwo x + LiTwo (1 − x) + log x·log(1−x)
      = π²/6.

The correction cancels exactly. That is the whole content, and it is why the
Rogers normalisation is the one in which the level-7 ladder has rational values.

**Namespaces, since they differ and this cost a build.** `LiTwo` is declared in
`QOU.QPochhammer` (`DilogarithmArchimedeanLimit.lean`), but `LiTwo_reflection'`
and the `hasDerivAt_*` lemmas are in `QOU.Archimedean` (`DilogReflection.lean`,
which itself does `open QOU.QPochhammer`). Both `open`s are needed here.

**Scope.** This discharges *reflection only*. The inversion and Landen extensions
and the five-term relation — the other five hypotheses — remain open; see
`qou-rhyp`. **The 5₂ sum rule is PROVED**:
`QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms.
-/

namespace QOU.QBeta.FiveTwoRogersReflection

open QOU.QPochhammer QOU.Archimedean

/-- The Rogers dilogarithm, built from the corpus's real `LiTwo`. -/
noncomputable def rogersL (x : ℝ) : ℝ :=
  LiTwo x + Real.log x * Real.log (1 - x) / 2

/-- **Rogers reflection**, from `LiTwo_reflection'`.

The Euler correction term `−log x · log(1−x)` is cancelled exactly by the two
half-`log·log` terms in the Rogers normalisation. -/
theorem rogersL_reflection {x : ℝ} (hx0 : 0 < x) (hx1 : x < 1) :
    rogersL x + rogersL (1 - x) = Real.pi ^ 2 / 6 := by
  have h := LiTwo_reflection' x hx0 hx1
  have h1 : (1 : ℝ) - (1 - x) = x := by ring
  unfold rogersL
  rw [h1]
  linear_combination h

/-- The form the ladder file consumes: `L (1 − x) = L1 − L x` with `L1 = π²/6`. -/
theorem rogersL_one_sub {x : ℝ} (hx0 : 0 < x) (hx1 : x < 1) :
    rogersL (1 - x) = Real.pi ^ 2 / 6 - rogersL x := by
  have h := rogersL_reflection hx0 hx1
  linarith

/-- **The Rogers derivative**, `L'(x) = -(log(1-x)/x + log x/(1-x))/2` on `(0,1)`.

The half in the Rogers normalisation is what makes this symmetric under
`x ↦ 1 - x`, which is the analytic content of `rogersL_reflection` above and the
starting point for any proof of the five-term relation — the one input the
level-7 numerators still lack (`qou-rhyp`, `FiveTwoFiveTermArguments.lean`).

Both ingredients are already sorry-free in `QOU/Archimedean/DilogReflection.lean`;
this is a product rule and a `ring`. -/
theorem hasDerivAt_rogersL {x : ℝ} (hx0 : 0 < x) (hx1 : x < 1) :
    HasDerivAt rogersL (-(Real.log (1 - x) / x + Real.log x / (1 - x)) / 2) x := by
  have h := (hasDerivAt_LiTwo hx0 hx1).add
    ((hasDerivAt_log_mul_log_one_sub hx0 hx1).div_const 2)
  have hval : -Real.log (1 - x) / x + (Real.log (1 - x) / x - Real.log x / (1 - x)) / 2
      = -(Real.log (1 - x) / x + Real.log x / (1 - x)) / 2 := by ring
  rw [hval] at h
  exact h

/-- The derivative is invariant under `x ↦ 1 - x` up to sign — the symmetry that
makes `rogersL_reflection` true, stated so it is visible rather than implicit.

It needs no hypotheses at all: the first draft carried `0 < x < 1` by reflex and
the linter caught them unused. The symmetry is algebraic; only the *derivative
formula* it is applied to needs the interval. -/
theorem rogersL_deriv_symm (x : ℝ) :
    -(Real.log (1 - (1 - x)) / (1 - x) + Real.log (1 - x) / (1 - (1 - x))) / 2
      = -(Real.log (1 - x) / x + Real.log x / (1 - x)) / 2 := by
  rw [show (1 : ℝ) - (1 - x) = x by ring]
  ring

end QOU.QBeta.FiveTwoRogersReflection
