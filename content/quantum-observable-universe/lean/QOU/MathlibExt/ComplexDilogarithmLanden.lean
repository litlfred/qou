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

## What is *not* proved, and why it is a separate problem

A vanishing derivative gives Landen only up to a constant, and pinning the
constant needs one special value — `Li₂(−1) = −π²/12` at the natural base point
`z = −1`, where the corpus's `rogersL_reflection` already supplies the partner
value `rogersL(½) = π²/12`. Mathlib has `hasSum_zeta_two` (`π²/6`) but no
alternating analogue, so that value is not free here.

The **inversion** leg (`x > 1`) is harder still and is not attempted: `x > 1` lies
*on* `cLiTwoExt`'s cut, so it needs a boundary value from off the cut, not just
a constant of integration. Route 33 G5 records that as the sharper of the two.

**The 5₂ sum rule remains verified to 80 dps, unproved.**
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

end QOU.MathlibExt
