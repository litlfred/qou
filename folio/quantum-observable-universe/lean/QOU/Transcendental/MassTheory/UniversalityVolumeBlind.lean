/-
# The universality ladder is volume-blind

Thread "Derive the electron's categorical weight" (2026-11-27). This asks which convolution operator
each lepton carries under the universality ruling `e = Δ`, `μ = Δ³`, `τ = Δ⁵` (owner ruling 22:37Z,
`LeptonUniversalityLadder`). Audit: `docs/audits/2026-11-27-electron-categorical-weight.md` §14.

The full twist `Δ²` is central in `B₃`. On `V_N^{⊗3}` it acts on each spin-`J` part by a ribbon
scalar `θ_J/θ_N³ = q^{integer}` (`ColouredLadderTwist`). So the colour-`N` invariant of the closure
of `Δ^{2k+1}` is `Σ_J a_J r_J^k`, where `a_J` is the data of `Δ` alone. At `q = ζ_N` every `r_J`
is a power of `ζ_N`, so it has norm `1` (`norm_twist_eq_one`). Then:

* `universality_envelope`: `‖Σ_J a_J r_J^k‖ ≤ Σ_J ‖a_J‖` for every `k`. The bound does not
  depend on the generation.
* `universality_growth_le`: the Kashaev growth `(2π/N) log` of every generation is bounded by that
  of the same `k`-free envelope.

So adding full twists, which is all the universality ruling does between generations, cannot add
volume. The generations are volume-degenerate in the convolution picture. A hyperbolic carrier
(non-zero growth) cannot come from the ladder, so it has to come from a non-central, non-periodic
factor. No measured value enters.
-/
import Mathlib.Analysis.Complex.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic

namespace QOU.Transcendental.MassTheory.UniversalityVolumeBlind

open Real

/-- A power of a unit-norm number has norm `1`: twist scalars at roots of unity. -/
theorem norm_twist_eq_one (ζ : ℂ) (hζ : ‖ζ‖ = 1) (m : ℕ) : ‖ζ ^ m‖ = 1 := by
  rw [norm_pow, hζ, one_pow]

/-- **The ladder envelope does not depend on the generation.** -/
theorem universality_envelope {ι : Type*} [Fintype ι] (a r : ι → ℂ) (hr : ∀ J, ‖r J‖ = 1)
    (k : ℕ) : ‖∑ J, a J * r J ^ k‖ ≤ ∑ J, ‖a J‖ := by
  calc ‖∑ J, a J * r J ^ k‖ ≤ ∑ J, ‖a J * r J ^ k‖ := norm_sum_le _ _
    _ = ∑ J, ‖a J‖ := by
        refine Finset.sum_congr rfl fun J _ => ?_
        rw [norm_mul, norm_pow, hr J, one_pow, mul_one]

/-- **No generation out-grows the `k`-free envelope.** If the colour-`N` invariant of
generation `k` is `Σ_J a_J(N) r_J(N)^k` with unit-norm twists, its growth is at most the
envelope's, for every `k` and every `N`. -/
theorem universality_growth_le {ι : ℕ → Type*} [∀ N, Fintype (ι N)]
    (a r : (N : ℕ) → ι N → ℂ) (hr : ∀ N J, ‖r N J‖ = 1) (k N : ℕ)
    (hpos : 0 < ‖∑ J, a N J * r N J ^ k‖) :
    2 * π / N * Real.log ‖∑ J, a N J * r N J ^ k‖
      ≤ 2 * π / N * Real.log (∑ J, ‖a N J‖) := by
  apply mul_le_mul_of_nonneg_left _ (by positivity)
  exact Real.log_le_log hpos (universality_envelope (a N) (r N) (hr N) k)

end QOU.Transcendental.MassTheory.UniversalityVolumeBlind
