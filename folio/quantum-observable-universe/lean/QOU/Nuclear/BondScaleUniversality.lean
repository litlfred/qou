import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Tactic.Linarith

/-!
# A bond cannot carry its own energy scale if the energy reads the trace only

**The question (bean `qou-of4i`, locus (a)).** Is `E₀`, an electron-scale
quantity, the right scale for the nucleon–nucleon interface? Could the bond
carry a scale `c'` different from the scale `c` of the rest of the atom?

**What is proved.** Suppose the energy of a composite reads its Markov trace
only, i.e. it is a function `G` of the product `ε₁·ε₂` of the trace factors of
two subsystems. The corpus derives this as spectator invariance
(`docs/audits/2026-11-21-qbeta-energy-map-spectator.md` §1, §10) and the
binding law uses it (`tr_atom = tr_free · ∏ μ_k`). If each part's energy is
log-scaled with its own coefficient, `a·log ε₁ + b·log ε₂`, then trace-only
dependence forces `a = b` (`scales_equal_of_trace_only`).

So a nucleon–nucleon bond scale different from the scale of whatever else
shares the trace is excluded, as long as the energy is a function of the
trace alone. Route T of the same audit (§8–9) then fixes the common scale as
the temperature `k_B T = E₀` (`kT_eq_e0`, order zero). Under those premises
the locus of the deuteron overshoot is the interface value `μ`, i.e. the bond
word, not the scale.

**What it does not show.** It does not derive the Gibbs premise or the
tower factor, and it says nothing about an energy map that is not a function
of the trace alone. A per-bond-type scale is excluded only on that premise.

Stated over `ℝ` because `Real.log` is (AGENTS.md §7c: an archimedean
construct).
-/

namespace QOU.Nuclear.BondScaleUniversality

open Real

/-- **Trace-only dependence forces one scale.** If
`a·log x + b·log y = G (x·y)` for all `x, y > 0`, then `a = b`.
Evaluate at `(e, 1)` and at `(1, e)`: both have product `e`. -/
theorem scales_equal_of_trace_only (a b : ℝ) (G : ℝ → ℝ)
    (hG : ∀ x y : ℝ, 0 < x → 0 < y → a * Real.log x + b * Real.log y = G (x * y)) :
    a = b := by
  have he : (0 : ℝ) < Real.exp 1 := Real.exp_pos 1
  have h1 := hG (Real.exp 1) 1 he one_pos
  have h2 := hG 1 (Real.exp 1) one_pos he
  simp only [Real.log_exp, Real.log_one, mul_zero, mul_one, one_mul, add_zero,
    zero_add] at h1 h2
  linarith

/-- **The converse direction holds:** one common scale is trace-only. With
`a = b = c`, the energy `c·log x + c·log y` is `c·log(x·y)`. So the condition
is exactly "one scale", not stronger. -/
theorem trace_only_of_scales_equal (c x y : ℝ) (hx : 0 < x) (hy : 0 < y) :
    c * Real.log x + c * Real.log y = c * Real.log (x * y) := by
  rw [Real.log_mul (ne_of_gt hx) (ne_of_gt hy)]
  ring

/-- **A distinct bond scale breaks trace-only dependence.** If `a ≠ b`, no
function of the product reproduces `a·log x + b·log y`. -/
theorem no_trace_function_of_distinct_scales (a b : ℝ) (hab : a ≠ b) :
    ¬ ∃ G : ℝ → ℝ, ∀ x y : ℝ, 0 < x → 0 < y →
        a * Real.log x + b * Real.log y = G (x * y) := by
  rintro ⟨G, hG⟩
  exact hab (scales_equal_of_trace_only a b G hG)

end QOU.Nuclear.BondScaleUniversality
