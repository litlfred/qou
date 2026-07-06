import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic

/-!
# QOU.Torsion.neutron_proton_splitting — neutron-proton mass splitting

**Proposition** ([`prop:neutron-proton-splitting`](../../../quantum-observable-universe/particle-interactions/neutron-proton-splitting.md)).

*The neutron–proton mass difference is*

```
  Δm = m_n − m_p = α · |Φ(udd) − Φ(uud)| ≈ 1.302 MeV
```

*where `Φ(uud)` and `Φ(udd)` are the quantum-dilogarithm volumes of the
proton and neutron quark orderings respectively, and `α = m_e · 8G` is the
same binding scale as the atomic mass formula.  CODATA value:
`Δm = 1.293 MeV` (error 0.63 %).*

This is a quantitative physical prediction: the splitting equals the binding
scale times the absolute difference of two **quantum-dilogarithm volumes**
`Φ(udd)`, `Φ(uud)`, and the resulting number matches CODATA to 0.63 %.
Concretising `Φ` requires the Faddeev quantum-dilogarithm `Φ_q` evaluated on
the proton/neutron braid words at `q₀` — not yet in Lean.  The real
proposition (framework formula + CODATA agreement) is stated faithfully and
discharged by `sorry`.

-- Ref: [manuscript] quantum-observable-universe/particle-interactions/neutron-proton-splitting.md
-/

namespace QOU.Torsion

/-- The CODATA-derived neutron-proton mass difference in MeV (CODATA 2022:
    `939.56542194 − 938.27208816 = 1.29333378 MeV`; manuscript rounds to
    `1.293`). -/
def codataNeutronProtonSplittingMeV : ℝ := 1.293

/-- Inputs for the neutron-proton splitting: the binding scale `α = m_e·8G`,
    the proton/neutron quantum-dilogarithm volumes `Φ(uud)`, `Φ(udd)`, and
    the physical masses `m_p`, `m_n`. -/
class NeutronProtonSplittingContext where
  /-- Binding scale `α = m_e · 8G`. -/
  α : ℝ
  /-- Quantum-dilogarithm volume of the proton (uud) braid. -/
  Φ_uud : ℝ
  /-- Quantum-dilogarithm volume of the neutron (udd) braid. -/
  Φ_udd : ℝ
  /-- Proton rest mass (MeV). -/
  m_p : ℝ
  /-- Neutron rest mass (MeV). -/
  m_n : ℝ

/-- The framework-predicted neutron-proton mass difference in MeV
    (`α · |Φ(udd) − Φ(uud)|` per the manuscript). -/
def predictedNeutronProtonSplitting [ctx : NeutronProtonSplittingContext] : ℝ :=
  ctx.α * |ctx.Φ_udd - ctx.Φ_uud|

/-- **Neutron-proton mass splitting** ([`prop:neutron-proton-splitting`]).

    The mass difference `m_n − m_p` equals the binding scale `α` times the
    absolute difference of the quark-ordering quantum-dilogarithm volumes,
    matching CODATA `1.293 MeV` within the 0.63 % manuscript tolerance:

      (1) framework formula  `m_n − m_p = α · |Φ(udd) − Φ(uud)|`,
      (2) CODATA agreement   `|(m_n − m_p) − 1.293| ≤ 0.01 · 1.293`.

    Honest `sorry`: both parts depend on the Faddeev quantum-dilogarithm
    `Φ_q` evaluated on the proton/neutron braid words at `q₀`, which is not
    yet formalised in Lean (compute: the dilog-volume pipeline in
    `computations/`). -/
-- Ref: [manuscript] quantum-observable-universe/particle-interactions/neutron-proton-splitting.md
theorem neutron_proton_splitting [ctx : NeutronProtonSplittingContext] :
    (ctx.m_n - ctx.m_p = ctx.α * |ctx.Φ_udd - ctx.Φ_uud|) ∧
    (|ctx.m_n - ctx.m_p - codataNeutronProtonSplittingMeV|
      ≤ 0.01 * codataNeutronProtonSplittingMeV) := by
  -- Ref: [faddeev1994] https://doi.org/10.1007/BF02101594
  -- Ref: [manuscript] quantum-observable-universe/particle-interactions/neutron-proton-splitting.md
  -- Missing infra: Faddeev quantum-dilogarithm Φ_q on the proton (uud) /
  -- neutron (udd) braid words at q₀, and the binding scale α = m_e·8G.
  -- Not yet in Lean (compute: dilog-volume pipeline in computations/).
  sorry

end QOU.Torsion
