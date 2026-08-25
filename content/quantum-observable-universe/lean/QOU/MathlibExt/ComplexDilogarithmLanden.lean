import QOU.MathlibExt.ComplexDilogarithmDeriv

/-!
# Landen's combination is locally constant — the analytic core the corpus lacks

`ComplexDilogarithm.lean` lists, among what it does **not** provide, "the
inversion formula `Li₂ z + Li₂ (1/z) = −π²/6 − ½·log(−z)²`". That family —
inversion and Landen — is what `qou-rstq` item 4 needs, because identifying the
piecewise `extend` with `Re` of the analytic Rogers `L` *is* those two
identities. Route 33 measures the identification at `1e-50` in all three
regimes; this file supplies the analytic half of the Landen leg.

## What is proved

    d/dz [ Li₂(z) + Li₂(z/(z−1)) + ½·log(1−z)² ] = 0

(`hasDerivAt_landenCombo`), wherever the three arguments are legal. The three
terms' derivatives are

    −log(1−z)/z ,   −log(1−z)/(z(z−1)) ,   log(1−z)/(z−1)

and they cancel because `−1/z − 1/(z(z−1)) + 1/(z−1) = 0` identically. The
middle one is where the branch enters: it needs `log(1 − z/(z−1)) = −log(1−z)`,
i.e. `log(1/(1−z)) = −log(1−z)`, which holds exactly when `1−z` avoids the
`log` cut — hence the `slitPlane` hypothesis, stated rather than assumed.

## The constant, and how it is pinned

A vanishing derivative gives Landen only up to a constant. That constant is
pinned below (`landenCombo_ofReal_eq_zero`), on the negative real axis — the
regime `extend` actually uses — closing what Route 33 G5 recorded as the one
thing still missing from this leg.

**The base point is the limit `z → 0⁻`, not `z = −1`, and that is the whole
trick.** At `z = −1` the combination is `Li₂(−1) + Li₂(½) + ½·log 2²`; those
three cancel exactly, but pinning there would need `Li₂(½) = π²/12 − ½·log 2²`,
which Mathlib does not have. At `0` every term vanishes outright
(`cLiTwoExt_zero`, `log 1 = 0`), so **no special value is needed at all**. The
endpoint costs nothing because `Ico t 0` already excludes the one point where
`hasDerivAt_landenCombo`'s hypotheses fail (`z ≠ 0`), and continuity there is
supplied separately by `continuousOn_landenCombo_ofReal`.

Route 34 G3 checks this is a real economy rather than a stylistic preference:
each of the three pieces at `z = −1` is individually nonzero.

## What is *still* not proved

The **inversion** leg (`x > 1`) is harder and is not attempted: `x > 1` lies
*on* `cLiTwoExt`'s cut, so it needs a boundary value from off the cut, not just
a constant of integration. Route 33 G5 records it as the sharper of the two, and
Route 34 G5 checks adversarially that this file does **not** reach it — the
combination is visibly nonzero at `t = 2.24698`, the one argument
`extended_sum` uses in that regime.

Nor does this close `qou-rstq` item 4. Identifying the corpus's piecewise
`extend` with `Re` of the analytic Rogers `L` still needs the real-part
bookkeeping on top of these identities. This closes one of the two analytic
legs that item rests on.

**The 5₂ sum rule is PROVED**: `QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms.
-/

namespace QOU.MathlibExt

open Complex

/-- `1 − z/(z−1) = 1/(1−z)` — the substitution Landen turns on. -/
theorem one_sub_landen {z : ℂ} (hz1 : z - 1 ≠ 0) :
    1 - z / (z - 1) = (1 - z)⁻¹ := by
  have h : (1 : ℂ) - z ≠ 0 := fun h => hz1 (by linear_combination -h)
  field_simp
  ring

/-- The derivative of the Landen substitution. -/
theorem hasDerivAt_landenArg {z : ℂ} (hz1 : z - 1 ≠ 0) :
    HasDerivAt (fun w : ℂ => w / (w - 1)) (-1 / (z - 1) ^ 2) z := by
  have h := (hasDerivAt_id z).div ((hasDerivAt_id z).sub_const 1) hz1
  simp only [id_eq] at h
  refine h.congr_deriv ?_
  field_simp
  ring

/-- `arg (1−z) ≠ π` on the slit plane — the branch condition, isolated. -/
theorem arg_ne_pi_of_slitPlane {w : ℂ} (hw : w ∈ Complex.slitPlane) :
    Complex.arg w ≠ Real.pi := by
  intro h
  obtain ⟨hre, him⟩ := Complex.arg_eq_pi_iff.mp h
  rcases hw with h1 | h1
  · linarith
  · exact h1 him

/-- **The Landen combination is locally constant.**

`d/dz [Li₂(z) + Li₂(z/(z−1)) + ½·log(1−z)²] = 0`. The `slitPlane` hypothesis is
where the branch is pinned: without it `log(1 − z/(z−1))` need not be
`−log(1−z)`, and the cancellation fails. -/
theorem hasDerivAt_landenCombo {z : ℂ} (hz : z ∈ notCut) (hz0 : z ≠ 0)
    (hz1 : z - 1 ≠ 0)
    (hu : z / (z - 1) ∈ notCut) (hu0 : z / (z - 1) ≠ 0)
    (hslit : 1 - z ∈ Complex.slitPlane) :
    HasDerivAt (fun w : ℂ => cLiTwoExt w + cLiTwoExt (w / (w - 1))
      + Complex.log (1 - w) ^ 2 / 2) 0 z := by
  have h1sub : (1 : ℂ) - z ≠ 0 := fun h => hz1 (by linear_combination -h)
  have d1 : HasDerivAt cLiTwoExt (-(Complex.log (1 - z) / z)) z :=
    hasDerivAt_cLiTwoExt' hz hz0
  have dsub : HasDerivAt (fun w : ℂ => 1 - w) (-1) z := by
    simpa using (hasDerivAt_const z (1 : ℂ)).sub (hasDerivAt_id z)
  have dlog : HasDerivAt (fun w : ℂ => Complex.log (1 - w)) (-(1 - z)⁻¹) z := by
    have h := (Complex.hasDerivAt_log hslit).comp z dsub
    simpa using h
  have d3 : HasDerivAt (fun w : ℂ => Complex.log (1 - w) ^ 2 / 2)
      (-(Complex.log (1 - z) * (1 - z)⁻¹)) z := by
    have h := (dlog.pow 2).div_const 2
    refine h.congr_deriv ?_
    ring
  have hlogu : Complex.log (1 - z / (z - 1)) = -Complex.log (1 - z) := by
    rw [one_sub_landen hz1, Complex.log_inv _ (arg_ne_pi_of_slitPlane hslit)]
  have d2raw := (hasDerivAt_cLiTwoExt' hu hu0).comp z (hasDerivAt_landenArg hz1)
  have d2 : HasDerivAt (fun w : ℂ => cLiTwoExt (w / (w - 1)))
      (-(Complex.log (1 - z) / (z * (z - 1)))) z := by
    refine d2raw.congr_deriv ?_
    rw [hlogu]
    field_simp
  have hsum := (d1.add d2).add d3
  refine hsum.congr_deriv ?_
  field_simp
  ring

/-! ## Closing the constant: Landen holds outright on the negative reals

The derivative above leaves the identity only up to a constant. Route 33 G5
recorded the connectedness step as the one thing still missing from the Landen
leg. It is closed here, on the negative real axis — the regime `extend` actually
uses.

The constant is pinned **at the limit `z → 0⁻`, not at `z = −1`.** That choice is
what makes this self-contained: at `z = −1` the combination evaluates to
`Li₂(−1) + Li₂(½) + ½·log 2²`, so pinning there would need the special value
`Li₂(½) = π²/12 − ½·log 2²`, which is not in Mathlib. At `0` every term vanishes
outright (`cLiTwoExt_zero`, and `log 1 = 0`), so no special value is needed at
all. The exceptional point costs nothing because `Ico t 0` already excludes it.
-/

/-- The Landen combination. -/
noncomputable def landenCombo (z : ℂ) : ℂ :=
  cLiTwoExt z + cLiTwoExt (z / (z - 1)) + Complex.log (1 - z) ^ 2 / 2

/-- For real `s ≤ 0` the Landen substitution lands in `[0,1)` — in particular
off `Li₂`'s cut. This is the one inequality the whole argument turns on. -/
theorem landenArg_lt_one {s : ℝ} (hs : s ≤ 0) : s / (s - 1) < 1 := by
  have hden : s - 1 < 0 := by linarith
  rw [div_lt_one_of_neg hden]
  linarith

/-- `(s : ℂ) − 1 ≠ 0` for real `s ≤ 0` — used on every branch below. -/
theorem ofReal_sub_one_ne_zero {s : ℝ} (hs : s ≤ 0) : ((s : ℂ) - 1) ≠ 0 := by
  intro h
  have hre : (s : ℝ) - 1 = 0 := by
    have := congrArg Complex.re h
    simpa using this
  linarith

/-- `s/(s-1) ∈ notCut` for real `s ≤ 0`. -/
theorem landenArg_mem_notCut {s : ℝ} (hs : s ≤ 0) :
    ((s : ℂ) / ((s : ℂ) - 1)) ∈ notCut := by
  have hcast : (s : ℂ) / ((s : ℂ) - 1) = (((s / (s - 1) : ℝ)) : ℂ) := by
    push_cast
    ring
  refine Or.inr ?_
  rw [hcast, Complex.ofReal_re]
  exact landenArg_lt_one hs

/-- `(s : ℂ) ∈ notCut` for real `s ≤ 0`. -/
theorem ofReal_mem_notCut_of_nonpos {s : ℝ} (hs : s ≤ 0) : ((s : ℂ)) ∈ notCut :=
  Or.inr (by simpa using lt_of_le_of_lt hs zero_lt_one)

/-- `1 − s` is on the slit plane for real `s ≤ 0`. -/
theorem one_sub_ofReal_mem_slitPlane {s : ℝ} (hs : s ≤ 0) :
    (1 - (s : ℂ)) ∈ Complex.slitPlane := by
  refine Or.inl ?_
  simp only [Complex.sub_re, Complex.one_re, Complex.ofReal_re]
  linarith

/-- **`landenCombo` is continuous along the closed negative axis, up to and
including `0`.** The endpoint is the point of the lemma: the derivative fails
there (`z ≠ 0` is one of `hasDerivAt_landenCombo`'s hypotheses), but continuity
does not, and continuity is all the constancy theorem needs at the endpoint.

⚠ No hypothesis on `t`. A first version carried `ht : t ≤ 0` and Lean flagged it
unused — correctly: continuity is checked pointwise on `Icc t 0`, and each point
of that set already satisfies `s ≤ 0` from its own membership. For `t > 0` the
set is empty and the statement is vacuously true, so dropping the bound
generalises rather than weakens. -/
theorem continuousOn_landenCombo_ofReal {t : ℝ} :
    ContinuousOn (fun s : ℝ => landenCombo ((s : ℝ) : ℂ)) (Set.Icc t 0) := by
  intro s hs
  have hs0 : (s : ℝ) ≤ 0 := hs.2
  -- each of the three terms is continuous AT `s`, endpoint `0` included
  have hofR : ContinuousAt (fun u : ℝ => ((u : ℝ) : ℂ)) s :=
    Complex.continuous_ofReal.continuousAt
  -- `cLiTwoExt` unfolds to `-∫ …`, so bare `.comp` lets higher-order unification
  -- pick `Neg.neg` as the outer function. Pin `g` and `f` on every composition.
  have h1 : ContinuousAt (fun u : ℝ => cLiTwoExt ((u : ℝ) : ℂ)) s :=
    ContinuousAt.comp (g := cLiTwoExt) (f := fun u : ℝ => ((u : ℝ) : ℂ))
      (analyticOnNhd_cLiTwoExt _ (ofReal_mem_notCut_of_nonpos hs0)).continuousAt hofR
  have hinner : ContinuousAt (fun u : ℝ => ((u : ℝ) : ℂ) / (((u : ℝ) : ℂ) - 1)) s :=
    hofR.div (hofR.sub continuousAt_const) (ofReal_sub_one_ne_zero hs0)
  have h2 : ContinuousAt
      (fun u : ℝ => cLiTwoExt (((u : ℝ) : ℂ) / (((u : ℝ) : ℂ) - 1))) s :=
    ContinuousAt.comp (g := cLiTwoExt)
      (f := fun u : ℝ => ((u : ℝ) : ℂ) / (((u : ℝ) : ℂ) - 1))
      (analyticOnNhd_cLiTwoExt _ (landenArg_mem_notCut hs0)).continuousAt hinner
  have hsub1 : ContinuousAt (fun u : ℝ => 1 - ((u : ℝ) : ℂ)) s :=
    continuousAt_const.sub hofR
  have hlog : ContinuousAt (fun u : ℝ => Complex.log (1 - ((u : ℝ) : ℂ))) s :=
    ContinuousAt.comp (g := Complex.log) (f := fun u : ℝ => 1 - ((u : ℝ) : ℂ))
      (Complex.hasDerivAt_log (one_sub_ofReal_mem_slitPlane hs0)).continuousAt hsub1
  have h3 : ContinuousAt
      (fun u : ℝ => Complex.log (1 - ((u : ℝ) : ℂ)) ^ 2 / 2) s :=
    (hlog.pow 2).div_const 2
  exact (((h1.add h2).add h3)).continuousWithinAt

/-- **Landen's identity on the negative reals**, constant and all:

    Li₂(t) + Li₂(t/(t−1)) + ½·log(1−t)² = 0   for every real `t < 0`.

The derivative is zero by `hasDerivAt_landenCombo`; the constant is `0` because
the combination vanishes at `0` and `Ico t 0` excludes the one point where the
derivative hypotheses fail. -/
theorem landenCombo_ofReal_eq_zero {t : ℝ} (ht : t < 0) :
    landenCombo ((t : ℝ) : ℂ) = 0 := by
  have hzero : landenCombo ((0 : ℝ) : ℂ) = 0 := by
    simp [landenCombo]
  have hderiv : ∀ s ∈ Set.Ico t 0,
      HasDerivWithinAt (fun u : ℝ => landenCombo ((u : ℝ) : ℂ)) 0 (Set.Ici s) s := by
    intro s hs
    have hsneg : s < 0 := hs.2
    have hz1 : (s : ℂ) - 1 ≠ 0 := by
      intro h
      have hre : (s : ℝ) - 1 = 0 := by
        have := congrArg Complex.re h
        simpa using this
      linarith
    have hz0 : (s : ℂ) ≠ 0 := by
      intro h
      have : (s : ℝ) = 0 := by exact_mod_cast congrArg Complex.re h
      linarith
    have hu0 : (s : ℂ) / ((s : ℂ) - 1) ≠ 0 := div_ne_zero hz0 hz1
    have hC := hasDerivAt_landenCombo (ofReal_mem_notCut_of_nonpos hsneg.le) hz0 hz1
      (landenArg_mem_notCut hsneg.le) hu0 (one_sub_ofReal_mem_slitPlane hsneg.le)
    exact (hC.comp_ofReal).hasDerivWithinAt
  have := constant_of_has_deriv_right_zero continuousOn_landenCombo_ofReal hderiv
    0 ⟨ht.le, le_rfl⟩
  rw [hzero] at this
  exact this.symm

end QOU.MathlibExt
