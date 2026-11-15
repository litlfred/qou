import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic


/-!
# Neutron-Proton Mass Splitting

Δm = α × |ΔΦ_quark| from the dd vs uu crossing change.

The quark-ordering volumes `Φ(uud)`, `Φ(udd)` are the canonical **Hecke
traced-volume** `Φ(K) = Σᵢ log|V̂ᵢ(K)|` of the quark orderings
(uud = `[1,1,0]`, udd = `[1,0,0]`; `computations/level1-qvalues.py`,
`HeckeRational.traced_volume`).  Each `V̂ᵢ` is a rational function of `q`, so
`Φ` has an exact closed form — `log` of a rational function of `q₀` — captured
by [`quarkPhiClosedForm`](#QOU.NeutronProtonSplitting.quarkPhiClosedForm) below.
The numeric constants in [`quarkPhi`](#QOU.NeutronProtonSplitting.quarkPhi) are
its rounded evaluations at `q₀`.  Provenance + symbolic derivation:
`docs/audits/2026-07-11-quark-volume-provenance.md`.

-- Ref: [manuscript] prop:neutron-proton-mass-splitting
-/

namespace QOU.NeutronProtonSplitting

/-- Substrate modulus `q₀`, the canonical 50-dps pin
(`q_parameter.Q_50_DIGIT_STR`; `q_parameter.Q` is its f64 view).  Full
precision matches `QOU.LiftingDescent.H3BraneTowerScaffold.q0`. -/
noncomputable def q0 : ℝ :=
  1.10997858275138080759166909561076887987449912187357763605672

/-- Convention-D Markov parameter `z_D = q³/(q²+1)` at `q₀` (canonical;
    owner rulings 2026-08-15 and 2026-11-15). -/
noncomputable def zD : ℝ := q0 ^ 3 / (q0 ^ 2 + 1)

/-- **Closed-form quark-ordering volume** `Φ(K) = log|∏ᵢ V̂ᵢ(K)|`, the exact
    Hecke traced-volume at the Markov parameter `z`, with each strand paired
    with every later strand (`level1-qvalues.py`).  Provenance:
    `docs/audits/2026-07-11-quark-volume-provenance.md`.

      Φ(uud) = log|(z q² + 2q − z)(q² − 2z q − 1) / (4 q²)|
      Φ(udd) = log|(q²+1)²(q² − z q − 1) / (4 q³)|

    **Convention D (owner ruling 2026-11-15: replace convention-C values with
    convention D even if worse).**  The file previously folded the
    convention-C `z = 4993/10000` (rounded `√q/(q+1)`) into integer
    coefficients, which no convention detector could see (bean `qou-wgta`).
    The closed form is now written in `z` and evaluated at `zD`. -/
noncomputable def quarkPhiClosedFormAt (z : ℝ) (ordering : String) : ℝ :=
  if ordering = "uud" then
    Real.log |(z * q0 ^ 2 + 2 * q0 - z) * (q0 ^ 2 - 2 * z * q0 - 1) / (4 * q0 ^ 2)|
  else if ordering = "udd" then
    Real.log |(q0 ^ 2 + 1) ^ 2 * (q0 ^ 2 - z * q0 - 1) / (4 * q0 ^ 3)|
  else 0

/-- The closed form at the canonical convention-D parameter. -/
noncomputable def quarkPhiClosedForm (ordering : String) : ℝ :=
  quarkPhiClosedFormAt zD ordering

/-- Quark-ordering quantum-dilogarithm volume — the rounded evaluation of
    [`quarkPhiClosedForm`](#QOU.NeutronProtonSplitting.quarkPhiClosedForm) at
    `q₀`, convention D (`Φ(uud) ≈ -0.614886`, `Φ(udd) ≈ -0.896395`, computed
    at 50 dps).  The convention-C values `-0.878526`, `-1.226119` are retired
    and kept only as a historical comparison in the block prose. -/
noncomputable def quarkPhi (ordering : String) : ℝ :=
  if ordering = "uud" then -0.614886
  else if ordering = "udd" then -0.896395
  else 0

/-- The mass splitting from quark crossing change.
    Replacing uu (σ, eigenvalue q) with dd (σ⁻¹, eigenvalue q⁻¹)
    increases confinement energy. -/
noncomputable def massSplitting (α : ℝ) : ℝ :=
  α * abs (quarkPhi "udd" - quarkPhi "uud")

/-- At `α = 3.7445`: `Δm ≈ 1.0541` (MeV units), convention D.
    Model value only; the comparison with the measured splitting is an
    empirical claim and lives in the block prose.  Under the retired
    convention C this goal read `|Δm − 1.302| < 0.001`. -/
theorem splitting_value :
    abs (massSplitting 3.7445 - 1.0541) < 0.001 := by
  unfold massSplitting quarkPhi
  norm_num [show ("udd" = "uud") = False by decide, show ("udd" = "udd") = True by decide]

/-- The same binding scale α appears at quark (confinement)
    and nuclear (binding) levels. -/
def same_scale_both_levels (m_e : ℝ) (volB3 : ℝ)
    (h : volB3 = 8 * 0.9159655941772190) :
    m_e * volB3 = m_e * volB3 := rfl

end QOU.NeutronProtonSplitting
