import QOU.QBeta.FaddeevUniquenessBoundedCapstone
import QOU.MathlibExt.PhiBProd

/-!
# Concrete-`Φ_b` Faddeev–Volkov uniqueness (the `phiBProd` assembly)

The capstones (`FaddeevUniquenessBoundedCapstone`, `FaddeevUniquenessCapstone`) close the
Faddeev–Volkov uniqueness leg for a **generic** `FaddeevPhi` reference `Φ₂`, modulo the two
*structural* class hypotheses (`[FaddeevPhi b Φ₂]`, `(b²).im ≠ 0`) plus the single analytic
endowment (strip boundedness, or same divisor). This file discharges **both structural
hypotheses for the concrete `Φ_b = phiBProd`** on the substrate branch, using the two
`PhiBProd` substrate facts:

* `faddeevPhi_phiBProd_substrate` — `phiBProd` *is* a `FaddeevPhi` solution at `substrateB t`
  (the modular-double product, `Multipliable` discharged for `Im b² > 0`);
* `substrateB_sq_im_pos` — the substrate lattice is nondegenerate (`(b²).im > 0`).

So for the **explicit product** `Φ_b = phiBProd (substrateB t)`, Faddeev–Volkov uniqueness
reduces to exactly **one** analytic input — the state-integral strip **boundedness** of the
prefactor-cancelled ratio (`hbdd`, routed through `BoundedMeromorphicLiouville`) — plus the
ratio/density bookkeeping the capstone already isolates. No structural class hypothesis
remains open on the reference solution: it is the concrete product, not an abstract `Φ₂`.

This is the concrete-`Φ_b` end of the keystone: `qou-7xvy`'s inputs 1–2 (MeromorphicOn,
`ord ≠ ⊤`) and the inversion/σ-unitarity elliptic-freedom narrowing feed the *same-divisor*
route; this file wires the complementary *boundedness* route to the concrete product,
leaving `hbdd` as the sole analytic residual.

Verified `lean`-direct against the restored Meromorphic cone + the full Faddeev-uniqueness
QOU dep cone (`FaddeevUniquenessBoundedCapstone`, `PhiBProd`). Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-07-25-faddeev-uniqueness-keystone-state.md
-/

open Complex
open QOU.MathlibExt.FaddeevQuantumDilogarithm
open QOU.MathlibExt.PhiBProd

namespace QOU.QBeta.PhiBProdUniquenessAssembly

/-- **Concrete-`Φ_b` uniqueness (boundedness route).** For the explicit modular-double
product `Φ_b = phiBProd (substrateB t)` (`t = ln q₀ > 0`), any `FaddeevPhi` solution `Φ₁`
whose normal-form ratio to `Φ_b` is **bounded** on `ℂ` (the state-integral endowment,
`hbdd`) is a **scalar multiple** of `Φ_b` on `Φ_b`'s nonvanishing locus. The two structural
hypotheses the generic capstone leaves open — that the reference is a `FaddeevPhi` solution
and that its period lattice is nondegenerate — are **discharged here for the concrete
product** (`faddeevPhi_phiBProd_substrate`, `substrateB_sq_im_pos`); only the analytic
boundedness (plus the ratio/density bookkeeping) remains. -/
theorem phiBProd_uniqueUpToScalar_of_bounded
    {t : ℝ} (ht : 0 < t)
    {Φ₁ : ℂ → ℂ} [FaddeevPhi (substrateB t) Φ₁]
    {C : ℝ}
    (hbdd : ∀ z,
      ‖toMeromorphicNFOn (Φ₁ / phiBProd (substrateB t)) Set.univ z‖ ≤ C)
    (hr_ratio : ∀ z, phiBProd (substrateB t) z ≠ 0 →
      toMeromorphicNFOn (Φ₁ / phiBProd (substrateB t)) Set.univ z
        = Φ₁ z / phiBProd (substrateB t) z)
    {S₀ S₁ : Set ℂ} (hS₀ : Dense S₀) (hS₁ : Dense S₁)
    (hmem₀ : ∀ z ∈ S₀,
      (1 : ℂ) + Complex.exp (I * (Real.pi : ℂ) * (substrateB t) ^ 2)
          * Complex.exp (2 * (Real.pi : ℂ) * (substrateB t) * z) ≠ 0
        ∧ phiBProd (substrateB t) z ≠ 0
        ∧ phiBProd (substrateB t) (z + I * (substrateB t)) ≠ 0)
    (hmem₁ : ∀ z ∈ S₁,
      (1 : ℂ) + Complex.exp (2 * (Real.pi : ℂ) * (z + I / (2 * (substrateB t))) / (substrateB t)) ≠ 0
        ∧ phiBProd (substrateB t) z ≠ 0
        ∧ phiBProd (substrateB t) (z + I / (substrateB t)) ≠ 0) :
    ∃ c, ∀ z, phiBProd (substrateB t) z ≠ 0 → Φ₁ z = c * phiBProd (substrateB t) z := by
  haveI : FaddeevPhi (substrateB t) (phiBProd (substrateB t)) :=
    faddeevPhi_phiBProd_substrate ht
  exact FaddeevUniquenessBoundedCapstone.faddeevPhi_proportional_of_bounded_ratio
    (substrateB_sq_im_pos ht).ne' hbdd hr_ratio hS₀ hS₁ hmem₀ hmem₁

end QOU.QBeta.PhiBProdUniquenessAssembly
