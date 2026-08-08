/-
  The `hratio` reduction is circular — `hratio` IS the conclusion.

  THE CLAIM BEING CHECKED. `QOU.MathlibExt.DoublyPeriodicLiouville` presents

      ratio_const_of_entire_ratio (hr : Differentiable ℂ (Ψ/Φ)) (hper : …)
        : ∃ c, ∀ z, Ψ z / Φ z = c

  as a REDUCTION of `PentagonRigidity.uniqueUpToScalar` to two "smaller,
  standard facts". `hper` genuinely is smaller — it is algebra
  (`QOU.Mathlib.FaddeevRatioPeriodic`). `hr` is not.

  WHAT IS PROVED HERE. Given `hper`, the hypothesis `hr` and the conclusion are
  EQUIVALENT:

      hratio_iff_conclusion :
        Differentiable ℂ (fun z => Ψ z / Φ z) ↔ ∃ c, ∀ z, Ψ z / Φ z = c

  Forward is `ratio_const_of_entire_ratio`; backward is that a constant function
  is differentiable. So discharging `hratio` is not a step towards the theorem —
  it is the theorem, wearing different clothes. The classical reason is standard:
  the ratio is elliptic, and an elliptic function is entire exactly when it is
  constant.

  WHY THIS MATTERS FOR THE WORK PLAN. Bean qou-cons is not a tractable
  sub-problem that happens to be open. Anyone who "proves `hratio`" has proved
  `uniqueUpToScalar` outright, and will have needed some input that is nowhere in
  the current chain. The reduction chain

      uniqueUpToScalar  ⟸  hratio (qou-cons) + hper (qou-rp5f)

  therefore has exactly one real edge, `hper`, now discharged, and one edge that
  is an identity.

  WHAT THE MISSING INPUT ACTUALLY IS. `QOU.Mathlib.FaddeevSolutionSet` shows the
  `FaddeevPhi` solution set absorbs any doubly-periodic factor, so the functional
  equations ALONE cannot pin a solution up to scalar — with regularity added,
  "doubly periodic" becomes "elliptic", and non-constant elliptic functions
  exist. **An extra condition is mandatory, not optional.** It has to be
  something that rules out non-constant elliptic multipliers: a growth bound, a
  minimality principle, or a pinned divisor.

  WHICH PARTIALLY REHABILITATES THE HADAMARD DIRECTION. The motivation retracted
  in `QOU.Mathlib.HadamardFactorization` — "`phiBProd` is selected among its
  elliptic multiples by a growth/minimality principle" — was reaching for exactly
  this missing input, and was right that one is needed. What was wrong was the
  execution: it aimed Hadamard at `phiBProd`, which is not entire
  (`QOU.Mathlib.HadamardApplicability`). A growth argument aimed at the two
  entire HALVES, or at a pinned divisor, remains a live candidate. That is a
  different and much smaller claim than the one retracted, and it is not proved
  anywhere yet.

  -- Ref: [faddeev1995] Faddeev, Lett. Math. Phys. 34 (1995) 249.
-/
import QOU.MathlibExt.DoublyPeriodicLiouville

namespace QOU.Mathlib.RigidityReductionScope

open QOU.MathlibExt.DoublyPeriodicLiouville Module

/-- **The reduction is an identity, not a reduction.** Given double periodicity
of the ratio, "the ratio is entire" and "the ratio is constant" are the same
statement. Forward is the Liouville step; backward is that constants are
differentiable. -/
theorem hratio_iff_conclusion {Φ Ψ : ℂ → ℂ} {b : Basis (Fin 2) ℝ ℂ}
    (hper : ∀ i, ∀ z, Ψ (z + b i) / Φ (z + b i) = Ψ z / Φ z) :
    Differentiable ℂ (fun z => Ψ z / Φ z) ↔ ∃ c, ∀ z, Ψ z / Φ z = c := by
  constructor
  · intro hr
    exact ratio_const_of_entire_ratio hr hper
  · rintro ⟨c, hc⟩
    have h : (fun z => Ψ z / Φ z) = fun _ => c := funext hc
    rw [h]
    exact differentiable_const c

/-- The pointwise corollary, in the form the application consumes: off the
divisor, `hratio` already delivers `Ψ = c·Φ`. Stated to make the circularity
concrete — this is `uniqueUpToScalar`'s own conclusion. -/
theorem eq_const_mul_of_hratio {Φ Ψ : ℂ → ℂ} {b : Basis (Fin 2) ℝ ℂ}
    (hper : ∀ i, ∀ z, Ψ (z + b i) / Φ (z + b i) = Ψ z / Φ z)
    (hr : Differentiable ℂ (fun z => Ψ z / Φ z)) :
    ∃ c, ∀ z, Φ z ≠ 0 → Ψ z = c * Φ z :=
  eq_const_mul_of_entire_ratio hr hper

end QOU.Mathlib.RigidityReductionScope
