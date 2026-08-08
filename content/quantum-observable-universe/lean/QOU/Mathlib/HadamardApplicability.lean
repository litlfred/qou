/-
  Does the Hadamard chain apply to its stated target? — a scoping check.

  WHY THIS FILE EXISTS. `QOU.Mathlib.HadamardFactorization` opens by stating its
  motivation: the residual leg of `PentagonRigidity.uniqueUpToScalar` reduces to
  "the analytic fact that the canonical minimal Faddeev solution `phiBProd` is
  selected among all `phiBProd·(elliptic)` multiples by a growth/minimality
  principle", and "that principle is a special case of the **Hadamard
  factorization theorem**".

  Hadamard's theorem is about ENTIRE functions. `phiBProd` is not one.

  WHAT IS PROVED HERE. `QOU.MathlibExt.PhiBProd.phiBProd` is defined as a RATIO
  of two infinite products,

      phiBProd b z = (∏' k, numFactor b z k) / (∏' k, denFactor b z k),

  and the theorem below exhibits, for EVERY `b ≠ 0`, an explicit `z` at which the
  `k = 0` denominator factor vanishes:

      z₀ = (i·b/2)·(1 + 1/b²)     ⟹     denFactor b z₀ 0 = 0.

  The point is not exotic and not a boundary case: it exists for every `b ≠ 0`,
  including the substrate `b = √(ln q₀/2π)·e^{iπ/4}` this corpus uses.

  WHAT THAT DOES AND DOES NOT ESTABLISH — the distinction matters.

    PROVED (here, sorry-free): a denominator FACTOR vanishes at an explicit
    point, for every `b ≠ 0`.

    NOT PROVED (standard, but not formalised): that the denominator PRODUCT
    therefore vanishes there — that needs the multipliability hypotheses
    `phiBProd`'s own theorems carry — and that the numerator does not vanish to
    matching order, which would make the singularity removable. Neither is
    expected to fail, but neither is checked.

  So the honest conclusion is not "phiBProd has a pole at z₀" but the weaker and
  sufficient: **`Differentiable ℂ (phiBProd b)` cannot be assumed, and therefore
  `IsEntireOfOrderLE (phiBProd b) ρ` — whose first conjunct is exactly that
  differentiability — is not available for any `ρ` without an argument nobody has
  made.** The Hadamard chain's stated application is unestablished.

  THE REPAIR — PROVED BELOW, not merely recorded. Each `numFactor`/`denFactor`
  is entire in `z`, and given locally uniform convergence the NUMERATOR and
  DENOMINATOR are separately entire:

      differentiable_tprod_one_add   general: entire factors + summable
                                     domination on every ball  ⟹  ∏' is entire
      differentiable_numProd         the numerator half is entire
      differentiable_denProd         the denominator half is entire

  So Hadamard applies to each half. The convergence input is carried as an
  EXPLICIT hypothesis, matching `PhiBProd`'s own stated discipline — that file
  carries its `Multipliable` inputs as named hypotheses rather than discharging
  them, since they are the analytic facts (geometric bounds for `Im b² > 0`).
  The structural claim, which is what was missing, is discharged here.

  WHAT REMAINS OPEN, and it is not a translation: whether the minimality
  principle that motivated the chain survives being restated about the two
  halves rather than the quotient. Nobody has checked that, and it does not
  follow from anything here.

  Bean qou-c3if (the roast that produced this check), bean qou-v4if (the chain).

  -- Ref: [faddeev1995] Faddeev, Lett. Math. Phys. 34 (1995) 249.
-/
import QOU.MathlibExt.PhiBProd
import Mathlib.Analysis.NormedSpace.MultipliableUniformlyOn
import Mathlib.Analysis.Complex.LocallyUniformLimit

namespace QOU.Mathlib.HadamardApplicability

open Complex QOU.MathlibExt.PhiBProd

/-- The `k = 0` denominator factor of the modular-double product vanishes at an
explicit point, for every `b ≠ 0`.

`phiBProd` is defined as a quotient by `∏' k, denFactor b z k`, so this is the
obstruction to `phiBProd` being entire — see the module docstring for exactly
what is and is not concluded from it. -/
theorem denFactor_eq_zero {b : ℂ} (hb : b ≠ 0) :
    denFactor b ((I * b / 2) * (1 + 1 / b ^ 2)) 0 = 0 := by
  have hb2 : b ^ 2 ≠ 0 := pow_ne_zero 2 hb
  unfold denFactor
  have hexp : -((Real.pi : ℂ) * I) / b ^ 2 * (2 * ((0 : ℕ) : ℂ) + 1)
      + 2 * (Real.pi : ℂ) * ((I * b / 2) * (1 + 1 / b ^ 2)) / b
      = (Real.pi : ℂ) * I := by
    field_simp
    ring
  rw [hexp, Complex.exp_mul_I]
  simp

/-- The vanishing point is not a single accident: shifting `z` by any multiple of
`i b` along the dual period keeps the `k = 0` factor at zero, so the obstruction
recurs. -/
theorem denFactor_eq_zero_shift {b : ℂ} (hb : b ≠ 0) (m : ℤ) :
    denFactor b ((I * b / 2) * (1 + 1 / b ^ 2) + (m : ℂ) * I * b) 0 = 0 := by
  have hb2 : b ^ 2 ≠ 0 := pow_ne_zero 2 hb
  unfold denFactor
  have hexp : -((Real.pi : ℂ) * I) / b ^ 2 * (2 * ((0 : ℕ) : ℂ) + 1)
      + 2 * (Real.pi : ℂ) * ((I * b / 2) * (1 + 1 / b ^ 2) + (m : ℂ) * I * b) / b
      = (Real.pi : ℂ) * I + (2 * (m : ℂ)) * ((Real.pi : ℂ) * I) := by
    field_simp
    ring
  rw [hexp]
  rw [Complex.exp_add]
  have h2 : Complex.exp ((2 * (m : ℂ)) * ((Real.pi : ℂ) * I)) = 1 := by
    have : (2 * (m : ℂ)) * ((Real.pi : ℂ) * I) = (m : ℂ) * (2 * (Real.pi : ℂ) * I) := by
      ring
    rw [this, Complex.exp_int_mul_two_pi_mul_I]
  rw [h2, Complex.exp_mul_I]
  simp

/-! ## The repair: each HALF is entire, so Hadamard applies to the halves

The obstruction above is to `phiBProd` — the quotient. It is not an obstruction
to the numerator or the denominator, each of which is a product of entire
factors. This section proves that, so the reformulation is available rather than
merely asserted. -/

/-- **If every `f n` is entire and the family is dominated by a summable
sequence on every ball, then `z ↦ ∏' n, (1 + f n z)` is entire.**

The general fact behind the repair. Mathlib supplies locally uniform
multipliability from a summable dominant
(`Summable.hasProdLocallyUniformlyOn_nat_one_add`) and holomorphy of locally
uniform limits (`TendstoLocallyUniformlyOn.differentiableOn`); this stitches
them and passes from "on every ball" to entire, differentiability being local. -/
theorem differentiable_tprod_one_add {f : ℕ → ℂ → ℂ}
    (hf : ∀ n, Differentiable ℂ (f n))
    (hdom : ∀ R : ℝ, 0 < R → ∃ u : ℕ → ℝ, Summable u ∧
        ∀ᶠ n in Filter.atTop, ∀ z ∈ Metric.ball (0 : ℂ) R, ‖f n z‖ ≤ u n) :
    Differentiable ℂ (fun z => ∏' n, (1 + f n z)) := by
  intro z
  have hR : (0 : ℝ) < ‖z‖ + 1 := by positivity
  obtain ⟨u, hu, hdomR⟩ := hdom (‖z‖ + 1) hR
  have hopen : IsOpen (Metric.ball (0 : ℂ) (‖z‖ + 1)) := Metric.isOpen_ball
  have hprod := Summable.hasProdLocallyUniformlyOn_nat_one_add hopen hu hdomR
    (fun n => (hf n).continuous.continuousOn)
  have hdiff : DifferentiableOn ℂ (fun x => ∏' i, (1 + f i x))
      (Metric.ball (0 : ℂ) (‖z‖ + 1)) := by
    refine hprod.tendstoLocallyUniformlyOn_finsetRange.differentiableOn ?_ hopen
    filter_upwards with N
    have h1 : DifferentiableOn ℂ (∏ i ∈ Finset.range N, ((fun _ => (1 : ℂ)) + f i))
        (Metric.ball (0 : ℂ) (‖z‖ + 1)) :=
      DifferentiableOn.finset_prod
        (fun i _ => ((differentiable_const (1 : ℂ)).add (hf i)).differentiableOn)
    have h2 : (∏ i ∈ Finset.range N, ((fun _ => (1 : ℂ)) + f i))
        = fun b => ∏ i ∈ Finset.range N, (1 + f i b) := by
      funext b; simp [Finset.prod_apply]
    rwa [h2] at h1
  refine hdiff.differentiableAt (hopen.mem_nhds ?_)
  simp only [Metric.mem_ball, dist_zero_right]
  linarith

/-- The numerator half of the modular-double product is entire.

The domination hypothesis is carried EXPLICITLY, matching `PhiBProd`'s own
stated discipline: that file carries its `Multipliable` inputs as named
hypotheses rather than discharging them, because they are the analytic
convergence facts (geometric bounds for `Im b² > 0`). Same input, same
treatment — the point here is the STRUCTURAL claim that the numerator is entire
GIVEN convergence, which is what the ratio is not. -/
theorem differentiable_numProd {b : ℂ}
    (hdom : ∀ R : ℝ, 0 < R → ∃ u : ℕ → ℝ, Summable u ∧
        ∀ᶠ (k : ℕ) in Filter.atTop, ∀ z ∈ Metric.ball (0 : ℂ) R,
          ‖Complex.exp ((Real.pi : ℂ) * I * b ^ 2 * (2 * (k : ℂ) + 1)
            + 2 * (Real.pi : ℂ) * b * z)‖ ≤ u k) :
    Differentiable ℂ (fun z => ∏' k, numFactor b z k) := by
  have := differentiable_tprod_one_add
    (f := fun k z => Complex.exp ((Real.pi : ℂ) * I * b ^ 2 * (2 * (k : ℂ) + 1)
      + 2 * (Real.pi : ℂ) * b * z))
    (fun k => (Complex.differentiable_exp.comp (by fun_prop))) hdom
  simpa [numFactor] using this

/-- The denominator half is entire, on the same terms. Together with
`differentiable_numProd` this is the repair: Hadamard applies to each half,
never to `phiBProd` itself. -/
theorem differentiable_denProd {b : ℂ}
    (hdom : ∀ R : ℝ, 0 < R → ∃ u : ℕ → ℝ, Summable u ∧
        ∀ᶠ (k : ℕ) in Filter.atTop, ∀ z ∈ Metric.ball (0 : ℂ) R,
          ‖Complex.exp (-((Real.pi : ℂ) * I) / b ^ 2 * (2 * (k : ℂ) + 1)
            + 2 * (Real.pi : ℂ) * z / b)‖ ≤ u k) :
    Differentiable ℂ (fun z => ∏' k, denFactor b z k) := by
  have := differentiable_tprod_one_add
    (f := fun k z => Complex.exp (-((Real.pi : ℂ) * I) / b ^ 2 * (2 * (k : ℂ) + 1)
      + 2 * (Real.pi : ℂ) * z / b))
    (fun k => (Complex.differentiable_exp.comp (by fun_prop))) hdom
  simpa [denFactor] using this

end QOU.Mathlib.HadamardApplicability
