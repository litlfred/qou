import Mathlib.Tactic
import QOU.Archimedean.TransferMatrixOperator

/-!
# QOU.Archimedean.BreitWheelerPairProduction

**Canonical declaration** for content block at
[`quantum-observable-universe/predicted-spectra/breit-wheeler-pair-production-derivation.ts`](quantum-observable-universe/predicted-spectra/breit-wheeler-pair-production-derivation.ts).

Formalises the manuscript **bare photon pair** step of Breit–Wheeler pair
production: two identical photons give `γγ = σ₀²`, and the Hecke relation
`σ₀² = (q − q⁻¹)σ₀ + 1` puts it in normal form `(q − q⁻¹)σ₀ + γ` with net
weight `net(γγ) = 1 + (q − q⁻¹)` (§7c: archimedean over `ℝ` for the `q > 1`
sign argument).
-/

namespace QOU.Archimedean

/-- Data for the bare Breit–Wheeler photon pair `γγ = σ₀²`.

    A `definition` carrier: the substrate `q > 1`, the Hecke normal-form
    coefficients of `σ₀²` (`σ₀`-part `q − q⁻¹`, constant `1`), and the net
    weight `net = 1 + (q − q⁻¹)`, the sum of the normal-form coefficients. -/
structure BreitWheelerPairProduction where
  /-- Substrate parameter `q`. -/
  q : ℝ
  /-- QOU regime `q > 1`. -/
  hq : 1 < q
  /-- The `σ₀`-coefficient of `NF(σ₀²)`. -/
  nfSigma : ℝ
  /-- The constant coefficient of `NF(σ₀²)`. -/
  nfConst : ℝ
  /-- The net weight of `γγ`. -/
  net : ℝ
  /-- `σ₀`-coefficient is `q − q⁻¹` (from `σ₀² = (q−q⁻¹)σ₀ + 1`). -/
  nfSigma_def : nfSigma = q - q⁻¹
  /-- Constant coefficient is `1`. -/
  nfConst_def : nfConst = 1
  /-- `net(γγ) = nfConst + nfSigma = 1 + (q − q⁻¹)`. -/
  net_def : net = nfConst + nfSigma

-- Ref: [leitner2026] quantum-observable-universe/predicted-spectra/breit-wheeler-pair-production-derivation.ts

/-- In the QOU regime `q > 1` the bare pair carries net weight `> 1`
    (the `q`-deformation raises it above the classical value), since
    `q − q⁻¹ > 0`. -/
theorem net_gt_one (P : BreitWheelerPairProduction) :
    1 < P.net := by
  have hq0 : (0 : ℝ) < P.q := lt_trans one_pos P.hq
  have h1 : P.q⁻¹ < 1 := by
    rw [inv_eq_one_div]; exact (div_lt_one hq0).mpr P.hq
  rw [P.net_def, P.nfConst_def, P.nfSigma_def]
  linarith [h1, P.hq]

/-- **De-axiomatisation (bean `h2yz`).** The bare-pair NF coefficients are not
    free: they are the Hecke reduction of `σ₀·σ₀` computed by a
    `TransferMatrixOperator` `T` at the same `q`. `T.reduce_sigma_squared`
    proves `reduceA 1 0 1 0 = q − q⁻¹` and `reduceB 1 0 1 0 = 1`, so `γγ = σ₀²`
    genuinely reduces to `(q−q⁻¹)σ₀ + 1` — the coefficients are derived, not
    asserted. -/
noncomputable def BreitWheelerPairProduction.ofHecke
    (q : ℝ) (hq : 1 < q) (T : TransferMatrixOperator ℝ) (hT : T.q = q) :
    BreitWheelerPairProduction where
  q := q
  hq := hq
  nfSigma := T.reduceA 1 0 1 0
  nfConst := T.reduceB 1 0 1 0
  net := T.reduceB 1 0 1 0 + T.reduceA 1 0 1 0
  nfSigma_def := by rw [(T.reduce_sigma_squared).1, hT]
  nfConst_def := (T.reduce_sigma_squared).2
  net_def := rfl

end QOU.Archimedean
