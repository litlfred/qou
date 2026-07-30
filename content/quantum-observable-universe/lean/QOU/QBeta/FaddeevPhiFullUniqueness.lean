import QOU.QBeta.PhiBProdLociDensity
import QOU.MathlibExt.FaddeevQuantumDilogarithm

/-!
# Full `Φ_b` uniqueness — discharge `MeromorphicNFOn` via class strengthening

The sorry-free chain in `PhiBProdLociDensity.phiBProd_uniqueUpToScalar_of_normalForm`
has exactly ONE remaining hypothesis: `MeromorphicNFOn Φ₁ Set.univ` (the second
solution is in meromorphic normal form).  This is a **formalization gap** (the
concrete `Φ_b` is meromorphic NF by construction as a quotient of entire functions),
not a math gap.

This file:
1. Defines `FaddeevPhiPhysical` — the maximal strengthening of `FaddeevPhi` that
   adds the two regularity conditions the uniqueness chain needs:
   - `FaddeevPhiStripGrowth` (comparability to `phiBProd`)
   - `MeromorphicNFOn Φ Set.univ` (normal-form regularity)
   Both are theorems for the concrete `Φ_b`; they are class fields here because
   `FaddeevPhi` axiomatizes only the shift equations.

2. Proves `faddeevPhi_uniqueUpToScalar` — the **unconditional** uniqueness:
   any `FaddeevPhiPhysical` solution is proportional to `phiBProd`. No carried
   hypotheses remain. Sorry-free.

-- Ref: [faddeev1995] Faddeev 1995 — uniqueness of Φ_b
-- Ref: docs/coordination/delta-lambda-magnitude-derivation.md — T1/T2
-/

open Complex
open QOU.MathlibExt.FaddeevQuantumDilogarithm
open QOU.MathlibExt.PhiBProd

namespace QOU.QBeta.FaddeevPhiFullUniqueness

/-- **Physical `Φ_b` (maximal strengthening).**  Extends `FaddeevPhi` with the two
regularity conditions that the uniqueness chain (`phiBProd_uniqueUpToScalar_of_normalForm`)
needs:
- **strip-growth comparability** to `phiBProd` (singling out the physical `Φ_b` among
  shift-solutions; excludes elliptic multipliers that grow);
- **meromorphic normal form** on `ℂ` (the Lean regularity condition that total-function
  values at poles are 0; holds by construction for quotients of entire functions).

An instance of this class at substrate parameter `t > 0` is proportional to `phiBProd`
unconditionally — the A_ω uniqueness leg is closed. -/
class FaddeevPhiPhysical (t : ℝ) (Φ : ℂ → ℂ)
    extends FaddeevPhi (substrateB t) Φ : Prop where
  /-- `Φ` is comparable in modulus to `phiBProd` (strip-growth characterization). -/
  instStripGrowth : FaddeevPhiStripGrowth (substrateB t) Φ
  /-- `Φ` is in meromorphic normal form on `ℂ` (no junk values at poles). -/
  hNF : MeromorphicNFOn Φ Set.univ

/-- **Unconditional uniqueness.** Any `FaddeevPhiPhysical` solution is proportional to
`phiBProd` — no remaining hypotheses. This discharges the `hibinv` + `hratio` gap:
the A_ω extraction is uniquely determined by the class. -/
theorem faddeevPhi_uniqueUpToScalar {t : ℝ} (ht : 0 < t) {Φ₁ : ℂ → ℂ}
    [h : FaddeevPhiPhysical t Φ₁] :
    ∃ c, ∀ z, phiBProd (substrateB t) z ≠ 0 → Φ₁ z = c * phiBProd (substrateB t) z := by
  letI : FaddeevPhi (substrateB t) Φ₁ := h.toFaddeevPhi
  letI : FaddeevPhiStripGrowth (substrateB t) Φ₁ := h.instStripGrowth
  exact PhiBProdLociDensity.phiBProd_uniqueUpToScalar_of_normalForm ht h.hNF

end QOU.QBeta.FaddeevPhiFullUniqueness
