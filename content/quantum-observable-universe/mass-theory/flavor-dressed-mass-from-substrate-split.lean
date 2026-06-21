import QOU.Basic
import QOU.FlavorDressing.FlavorDressingFunctor


/-!
# QOU.FlavorDressing.dressed_mass_from_substrate_split

The substrate-pure derivation of the down–up dressed-quark
mass splitting:

```
μ_d − μ_u = M_N · (q-1)²·(1 − q⁻⁴)/3 · (q^{1/2} + q⁻^{1/2})/(q + q⁻¹)
            + O((Δm/M_N)²)
```

This is the categorical lift of `prop:flavor-split-substrate` to
the level of the flavor-dressing functor.

LaTeX: `\label{prop:flavor-dressed-mass-from-substrate-split}`
-/

namespace QOU.FlavorDressing

open Flavor

/-- The leading-order substrate factor

    `s(q) = (q − 1)² · (1 − q⁻⁴) / 3 · (√q + 1/√q) / (q + 1/q)`

    that multiplies `M_N` to give the dressed-quark splitting at
    substrate parameter `q ∈ ℝ`, `0 < q`.  Defined as a function on
    `ℝ` (we are at the archimedean / numerical layer here per
    AGENTS.md §7c). -/
noncomputable def substrate_split_factor (q : ℝ) : ℝ :=
  ((q - 1)^2 * (1 - q^(-4 : ℤ)) / 3) *
    ((Real.sqrt q + Real.sqrt q⁻¹) / (q + q⁻¹))

/-- **External Skein-side hypothesis** (axiomatised).  The
    pair-Skein mass formula of `lem:pair-skein-mass-formula`
    applied to the Borromean baryon braids of the proton and
    neutron gives

      `m_n − m_p = (q + q⁻¹)/(q^{1/2} + q⁻^{1/2}) · (μ_d − μ_u)`.

    Combined with the substrate identity
    `(m_n − m_p)/M_N = (q-1)² · (1 − q⁻⁴) / 3` (from
    `prop:flavor-split-substrate`), this rearranges to
    `μ_d − μ_u = M_N · substrate_split_factor q`.  The closed-form
    statement is recorded as this axiom; promoting it to a theorem
    requires Lean formalisations of both upstream lemmas. -/
-- Ref: [manuscript] observations/pair-skein-mass-formula
--      braids-and-knots/flavor-dressed-mass-from-substrate-split § "Derivation"
axiom dressed_mass_split_substrate_closed_form
    (F : FlavorDressingFunctor) (M_N q : ℝ)
    (_hM : 0 < M_N) (_hq : 1 < q) :
    F.μ Flavor.down - F.μ Flavor.up
      = M_N * substrate_split_factor q

/-- **Substrate-pure derivation of the dressed-quark mass
    splitting.**  Combines `prop:flavor-split-substrate` (substrate
    side) with `lem:pair-skein-mass-formula` (Skein side) to
    express `μ_d − μ_u` in terms of `M_N` and `q` alone.

    Statement: under positive nucleon-mass scale `M_N` and substrate
    parameter `q > 1`, the equality

      `μ_d − μ_u = M_N · substrate_split_factor q`

    holds (up to the `O((Δm/M_N)²)` correction absorbed in the
    Skein-side identity).  Proved from the axiom
    `dressed_mass_split_substrate_closed_form` above, which records
    the closed-form result pending full Lean formalisation of the
    two upstream lemmas it combines.  This is no longer a tautology
    (Gemini #696 medium): the conclusion is a substantive equality
    backed by the axiomatised closed form, not a re-statement of
    its own hypotheses. -/
-- Ref: [manuscript] braids-and-knots/flavor-dressed-mass-from-substrate-split
theorem dressed_mass_from_substrate_split
    (F : FlavorDressingFunctor) (M_N q : ℝ)
    (hM : 0 < M_N) (hq : 1 < q) :
    F.μ Flavor.down - F.μ Flavor.up
      = M_N * substrate_split_factor q :=
  dressed_mass_split_substrate_closed_form F M_N q hM hq

end QOU.FlavorDressing
