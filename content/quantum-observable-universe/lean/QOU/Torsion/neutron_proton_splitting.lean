/-!
# QOU.Torsion.neutron_proton_splitting — neutron-proton mass splitting

**Proposition** ([`prop:neutron-proton-splitting`](../../../quantum-observable-universe/particle-interactions/neutron-proton-splitting.md)).

*The neutron–proton mass difference is*

```
  Δm = m_n − m_p = α · |Φ(udd) − Φ(uud)| ≈ 1.302 MeV
```

*where `Φ(uud)` and `Φ(udd)` are the quantum-dilogarithm volumes of
the proton and neutron quark orderings respectively, and
`α = m_e · 8G` is the same binding scale as the atomic mass formula.
CODATA value: `Δm = 1.293 MeV` (error 0.63 %).*

The Lean encoding records the formula as an equality between two
`ℝ`-valued quantities pinned to the empirical CODATA value within
the manuscript's 0.63 % tolerance.  Concretising `Φ` to a
quantum-dilogarithm computation against the proton / neutron braid
words is downstream work.

-- Ref: [manuscript] quantum-observable-universe/particle-interactions/neutron-proton-splitting.md
-/

namespace QOU.Torsion

/-- Abstract container for the neutron-proton splitting context:
    the binding scale `α = m_e · 8G`, the proton/neutron
    quantum-dilogarithm volumes `Φ(uud)` and `Φ(udd)`, and the
    physical masses `m_p`, `m_n`. -/
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

/-- The CODATA-derived neutron-proton mass difference in MeV. -/
def codataNeutronProtonSplittingMeV : ℝ := 1.293

/-- The framework-predicted neutron-proton mass difference in MeV
    (`α · |Φ(udd) − Φ(uud)|` per the manuscript). -/
def predictedNeutronProtonSplitting [ctx : NeutronProtonSplittingContext] : ℝ :=
  ctx.α * |ctx.Φ_udd - ctx.Φ_uud|

/-- **Neutron-proton mass splitting** ([`prop:neutron-proton-splitting`]).

    The mass difference `m_n − m_p` equals the binding scale `α`
    times the absolute difference of the quark-ordering quantum-
    dilogarithm volumes, matching the empirical CODATA value of
    `1.293 MeV` within the 0.63 % manuscript tolerance.

    Stated as a CONJUNCTION:

      (1) The framework formula holds: `m_n − m_p = α · |Φ(udd) − Φ(uud)|`.
      (2) The framework value agrees with CODATA `1.293 MeV` within
          `1 %` relative tolerance.
-/
-- Ref: [manuscript] quantum-observable-universe/particle-interactions/neutron-proton-splitting.md
theorem neutron_proton_splitting [ctx : NeutronProtonSplittingContext] :
    (ctx.m_n - ctx.m_p = ctx.α * |ctx.Φ_udd - ctx.Φ_uud|) ∧
    (|ctx.m_n - ctx.m_p - codataNeutronProtonSplittingMeV|
      ≤ 0.01 * codataNeutronProtonSplittingMeV) := by
  -- Manuscript derivation: replacing one `uu` crossing with `dd`
  -- shifts the confinement energy by `α · |Φ(udd) − Φ(uud)|`; the
  -- numerical match to CODATA is verified empirically in
  -- `folio-assistant/computations/atomic_braid_mass_table.py`.
  -- Concretisation requires Lean-translating the quark-braid
  -- representation theory.
  -- Ref: [manuscript] quantum-observable-universe/particle-interactions/neutron-proton-splitting.md
  sorry

end QOU.Torsion
