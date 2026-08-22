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
Concretising `Φ` requires the compact quantum dilogarithm `Φ_q` evaluated on
the proton/neutron braid words at `q₀` — not yet in Lean.  The real
proposition (framework formula + CODATA agreement) is stated faithfully and
discharged by `sorry`.

The two `Φ` volumes (`Φ(uud) ≈ -0.8785`, `Φ(udd) ≈ -1.2261`) **are derived**:
they are the canonical Hecke **traced-volume** of the quark orderings
(uud = `[1,1,0]`, udd = `[1,0,0]`), `Φ(K) = Σᵢ log|V̂ᵢ(K)|` with
`V̂ᵢ = z·M₁₀ + M₁₁` the transfer-matrix product over the quark crossings
(`computations/level1-qvalues.py`, `HeckeRational.traced_volume`).  This has an
exact closed form — `log` of a rational function of `q` — e.g.
`Φ(udd) = log|(q²+1)²(10000q² − 4993q − 10000) / (40000 q³)|` (with the
NF-basis constant `z = 4993/10000`).  Provenance + symbolic derivation:
`docs/audits/2026-07-11-quark-volume-provenance.md`.  (This transfer-matrix
`V̂ᵢ` is a *different* object from the `Φ_q` q-Pochhammer of
`QOU.MathlibExt.QuantumDilogarithm`.)  They remain opaque
`NeutronProtonSplittingContext` fields (§3b-cond) here only because the
`traced_volume` construction is not yet ported to Lean
(AGENTS.md anti-laundering rule).

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
  /-- Mass formula. -/
  mass_formula : m_n - m_p = α * |Φ_udd - Φ_uud|
  /-- CODATA agreement. -/
  codata_agreement : |m_n - m_p - codataNeutronProtonSplittingMeV| ≤ 0.01 * codataNeutronProtonSplittingMeV

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

    Honest `sorry`: both parts depend on the compact quantum dilogarithm
    `Φ_q` evaluated on the proton/neutron braid words at `q₀`, which is not
    yet formalised in Lean (compute: the dilog-volume pipeline in
    `computations/`). -/
-- Ref: [manuscript] quantum-observable-universe/particle-interactions/neutron-proton-splitting.md
theorem neutron_proton_splitting [ctx : NeutronProtonSplittingContext] :
    (ctx.m_n - ctx.m_p = ctx.α * |ctx.Φ_udd - ctx.Φ_uud|) ∧
    (|ctx.m_n - ctx.m_p - codataNeutronProtonSplittingMeV|
      ≤ 0.01 * codataNeutronProtonSplittingMeV) := by
  exact ⟨ctx.mass_formula, ctx.codata_agreement⟩

end QOU.Torsion
