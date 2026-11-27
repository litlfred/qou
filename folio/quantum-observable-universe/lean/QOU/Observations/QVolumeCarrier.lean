/-
# One object for both electron and muon: what it must satisfy

W6, beans `qou-91w7` / `qou-6gf9`, issue #9164. Owner choice 2026-11-23: search for one
derived weight that gives the electron a finite value and the muon `Vol(4₁)/ℏ_q²`.

Two families are in the corpus or close to it.

* **Traces** (`ElectronUnitSplit`): the electron is finite (`τ_e(1) = 1/2`), but every single
  trace is finite at `q = 1`, so the muon cannot have the double pole the carrier needs
  (`EnergyScaleMap.muon_carrier_not_trace_ratio`).
* **A q-volume.** `G(z; q) = Σ_{n ≥ 1} zⁿ/(1 − q⁻ⁿ)²`, summed over the ideal tetrahedra of a
  triangulation. The factor `1 − q⁻ⁿ` is exactly `ℏ_q · [n]'` with `[n]' = Σ_{k<n} q⁻ᵏ`
  (`one_sub_inv_pow_eq`), so `ℏ_q² · G → Li₂(z)` as `q → 1` and
  `2 Im G(e^{iπ/3}; q) ~ Vol(4₁)/ℏ_q²`. This is why the carrier's `ℏ_q` is `1 − q⁻¹` and not
  `log q` or `q − q⁻¹`. But a link with no tetrahedra (the Hopf closure of the electron) gets
  the empty sum `0`.

So neither family alone is the object. The natural joint candidate is the sum
`W = T + c · G`. `sum_family_leading` computes its carrier at leading order, and
`sum_family_forces_c` shows that the carrier forces `c = T_e(1)`, the electron's classical trace
(`1/2` for the ruled electron). That is a necessary condition, not a derivation of `c`: nothing in
either family produces the coefficient `c`, and it must not be set to `1/2` because that value makes
the carrier come out. The limit `ℏ_q² G → Vol` is taken as a hypothesis here (Euler–Maclaurin;
the probe measures it). It is not formalised.
-/
import Mathlib.Algebra.Order.Field.GeomSum
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Tactic

namespace QOU.Observations.QVolumeCarrier

open Filter Topology

/-- **`1 − q⁻ⁿ = (1 − q⁻¹) · Σ_{k<n} q⁻ᵏ`**: the q-volume's denominator factors through
`ℏ_q = 1 − q⁻¹`. -/
theorem one_sub_inv_pow_eq {R : Type*} [Field R] (q : R) (n : ℕ) :
    1 - q⁻¹ ^ n = (1 - q⁻¹) * ∑ k ∈ Finset.range n, q⁻¹ ^ k := by
  have := geom_sum_mul q⁻¹ n
  linear_combination this

/-- **Leading carrier of the sum family `W = T + c·G`.** Over any topological field `R` and
filter `l` (such as `𝓝[>] (1 : ℝ)`), suppose the electron has no tetrahedra (`G_e = 0`), both
traces have finite limits along `l`, `ℏ_q → 0`, and `ℏ_q² G_μ → V`. Then
`ℏ_q² W_μ / W_e → c·V / T_e(1)`. -/
theorem sum_family_leading {α R : Type*} [Field R] [TopologicalSpace R]
    [IsTopologicalRing R] [ContinuousInv₀ R] {l : Filter α}
    (h Te Tmu Gmu : α → R) (te tmu V c : R)
    (hh : Tendsto h l (𝓝 0))
    (hTe : Tendsto Te l (𝓝 te)) (hte : te ≠ 0)
    (hTmu : Tendsto Tmu l (𝓝 tmu))
    (hG : Tendsto (fun q => h q ^ 2 * Gmu q) l (𝓝 V)) :
    Tendsto (fun q => h q ^ 2 * (Tmu q + c * Gmu q) / (Te q + c * 0))
      l (𝓝 (c * V / te)) := by
  have h2 : Tendsto (fun q => h q ^ 2 * Tmu q) l (𝓝 (0 ^ 2 * tmu)) :=
    (hh.pow 2).mul hTmu
  have hnum : Tendsto (fun q => h q ^ 2 * (Tmu q + c * Gmu q)) l
      (𝓝 (0 ^ 2 * tmu + c * V)) := by
    have := h2.add (hG.const_mul c)
    refine this.congr (fun q => ?_)
    ring
  have hden : Tendsto (fun q => Te q + c * 0) l (𝓝 te) := by
    simpa using hTe
  have := hnum.div hden hte
  simpa using this

/-- **The carrier forces `c = T_e(1)`.** If the sum family's leading carrier is `V`
(that is, `m_μ/m_e ~ V/ℏ_q²`) and `V ≠ 0`, the coefficient of the volume term must be the
electron's classical trace. A necessary condition only. -/
theorem sum_family_forces_c {α R : Type*} [Field R] [TopologicalSpace R]
    [IsTopologicalRing R] [ContinuousInv₀ R] [T2Space R] {l : Filter α} [l.NeBot]
    (h Te Tmu Gmu : α → R) (te tmu V c : R)
    (hh : Tendsto h l (𝓝 0))
    (hTe : Tendsto Te l (𝓝 te)) (hte : te ≠ 0)
    (hTmu : Tendsto Tmu l (𝓝 tmu))
    (hG : Tendsto (fun q => h q ^ 2 * Gmu q) l (𝓝 V)) (hV : V ≠ 0)
    (hcar : Tendsto (fun q => h q ^ 2 * (Tmu q + c * Gmu q) / (Te q + c * 0))
      l (𝓝 V)) :
    c = te := by
  have hlead := sum_family_leading h Te Tmu Gmu te tmu V c hh hTe hte hTmu hG
  have heq : c * V / te = V := tendsto_nhds_unique hlead hcar
  have hc : c * V = te * V := by
    rw [div_eq_iff hte] at heq
    linear_combination heq
  exact mul_right_cancel₀ hV hc

end QOU.Observations.QVolumeCarrier
