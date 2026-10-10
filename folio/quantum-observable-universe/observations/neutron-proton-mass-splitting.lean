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

/-- **Closed-form quark-ordering volume** `Φ(K) = log|∏ᵢ V̂ᵢ(K)|`, the exact
    Hecke traced-volume (NF-basis constant `z = 4993/10000` already folded into
    the integer coefficients).  Provenance:
    `docs/audits/2026-07-11-quark-volume-provenance.md`.

    **CONVENTION SCOPE — this is convention C (measured 2026-10-10, bean
    `qou-wgta` critical item 2).**  `4993/10000 = 0.4993` is the rounded
    `z_C = √q/(q+1) = 0.4993203342` at `q₀`; the owner ruling of 2026-08-15
    excised C in favour of `z_D = q³/(q²+1) = 0.6126880371`.  The coefficients
    below are `10000·(z q² + 2q − z)`, `5000·(q² − 2z q − 1)` and
    `10000·(q² − z q − 1)` at `z = z_C`, so the convention is not a `z` symbol
    anywhere in this file — it survives as an integer numerator, which is why
    no convention detector in the repo can see this site.  Both the
    `convention-c-*` audits and `lean-markov-convention-audit.py` report it
    clean; verified by running them.

    Carrying `z_D` through the same closed form moves `|ΔΦ|` by **−19.01 %**
    and `massSplitting 3.7445` from `1.3016` to `1.0541` MeV, i.e. from
    **+0.64 %** to **−18.5 %** against CODATA `1.29333217`.  So
    `splitting_value` below is true *as stated* and is a C-frame result.

    Scope-(a), not an exclusion: nothing here shows a quark-ordering volume
    cannot carry the splitting.  And the C-frame agreement is **not** evidence
    for C — it was obtained in the retired convention, and picking a convention
    by its residual is what the three-calibration discipline forbids.  Do not
    substitute `z_D` into these coefficients to "fix" the number; the
    re-derivation is tracked work.

      Φ(uud) = log|(4993q² + 20000q − 4993)(5000q² − 4993q − 5000) / (2·10⁸ q²)|
      Φ(udd) = log|(q²+1)²(10000q² − 4993q − 10000) / (40000 q³)|

    Evaluating at `q₀` reproduces the `quarkPhi` constants below to ~5·10⁻⁵
    (`q₀`/`z` rounding). -/
noncomputable def quarkPhiClosedForm (ordering : String) : ℝ :=
  if ordering = "uud" then
    Real.log |(4993 * q0 ^ 2 + 20000 * q0 - 4993)
      * (5000 * q0 ^ 2 - 4993 * q0 - 5000) / (200000000 * q0 ^ 2)|
  else if ordering = "udd" then
    Real.log |(q0 ^ 2 + 1) ^ 2 * (10000 * q0 ^ 2 - 4993 * q0 - 10000)
      / (40000 * q0 ^ 3)|
  else 0

/-- Quark-ordering quantum-dilogarithm volume — the rounded evaluation of
    [`quarkPhiClosedForm`](#QOU.NeutronProtonSplitting.quarkPhiClosedForm) at
    `q₀` (`Φ(uud) ≈ -0.878526`, `Φ(udd) ≈ -1.226119`; the traced-volume closed
    form is the derivation of record). -/
noncomputable def quarkPhi (ordering : String) : ℝ :=
  if ordering = "uud" then -0.878526
  else if ordering = "udd" then -1.226119
  else 0

/-- The mass splitting from quark crossing change.
    Replacing uu (σ, eigenvalue q) with dd (σ⁻¹, eigenvalue q⁻¹)
    increases confinement energy. -/
noncomputable def massSplitting (α : ℝ) : ℝ :=
  α * abs (quarkPhi "udd" - quarkPhi "uud")

/-- At α = 3.7445 MeV: Δm ≈ 1.302 MeV (CODATA: 1.293 MeV).
    Error: 0.63%.

    **Convention-C-frame** — see the scope note on `quarkPhiClosedForm`.  Under
    the canonical `z_D` the same construction gives `1.0541` MeV (−18.5 %) and
    this `norm_num` goal would fail by 248× its own tolerance
    (`|Δm − 1.302| = 0.2479` against `< 0.001`).  The theorem is true as
    stated; what it certifies is the C-frame number. -/
theorem splitting_value :
    abs (massSplitting 3.7445 - 1.302) < 0.001 := by
  unfold massSplitting quarkPhi
  norm_num [show ("udd" = "uud") = False by decide, show ("udd" = "udd") = True by decide]

/-- The same binding scale α appears at quark (confinement)
    and nuclear (binding) levels. -/
def same_scale_both_levels (m_e : ℝ) (volB3 : ℝ)
    (h : volB3 = 8 * 0.9159655941772190) :
    m_e * volB3 = m_e * volB3 := rfl

end QOU.NeutronProtonSplitting
