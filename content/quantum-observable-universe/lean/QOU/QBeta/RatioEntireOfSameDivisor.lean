import Mathlib.Analysis.Meromorphic.NormalForm
import Mathlib.Analysis.Meromorphic.Order
import Mathlib.Analysis.Complex.Basic

/-!
# Brick (c): same divisor ⇒ the ratio extends to an entire function

The genuine content of `hr_entire` — the divisor-rigidity input of the Faddeev
uniqueness leg (`FaddeevPhiUniquenessAssembly.faddeevPhi_proportional_of_ratio_entire`
takes exactly this). Two meromorphic solutions `Φ, Ψ` of the same first-order
q-difference equation are *not* forced to share a divisor by the equation alone —
their ratio is an elliptic function that may be nonconstant (Weierstrass `℘`). But
*given* that they have the **same divisor** (the analytic rigidity fact that
`Φ_b`'s explicit `PhiBProd` zero/pole lattice supplies), the ratio's normal-form
representative is **entire**.

The construction that dissolves the `0/0` junk at the shared zeros is Mathlib's
meromorphic **normal form** `toMeromorphicNFOn`: it agrees with `Ψ/Φ` on a
punctured neighborhood of every point, its `meromorphicOrderAt` equals that of
`Ψ/Φ` (which is `ord Ψ − ord Φ = 0` under same-divisor), and a normal-form
function of order `≥ 0` is analytic
(`MeromorphicNFAt.meromorphicOrderAt_nonneg_iff_analyticAt`). So the representative
is analytic at every point, i.e. entire.

This is the honest §3b-cond input: `same-divisor ⇒ entire` is *proved* here; the
same-divisor premise itself (for the concrete `Φ_b`) is the remaining `PhiBProd`
content. Verified `lean`-direct against the Meromorphic cone built from pinned
mathlib source (`Mathlib.Analysis.Meromorphic.{Order,NormalForm}`).
-/

open Filter Topology

namespace QOU.QBeta.RatioEntire

/-- **Same divisor ⇒ entire ratio.** If `Φ, Ψ` are meromorphic on `ℂ`, `Φ` is
nowhere locally zero (`meromorphicOrderAt Φ ≠ ⊤` everywhere), and they have the
**same divisor** (`meromorphicOrderAt Ψ = meromorphicOrderAt Φ` at every point),
then the normal-form representative `r := toMeromorphicNFOn (Ψ/Φ) univ` is
**entire** (`Differentiable ℂ r`) and agrees with `Ψ/Φ` on a punctured
neighbourhood of every point. This is the `hr_entire` divisor-rigidity input of
the Faddeev uniqueness leg. -/
theorem entire_toMeromorphicNFOn_div_of_same_order
    {Φ Ψ : ℂ → ℂ}
    (hΦ : MeromorphicOn Φ Set.univ) (hΨ : MeromorphicOn Ψ Set.univ)
    (hΦ0 : ∀ z, meromorphicOrderAt Φ z ≠ ⊤)
    (hsame : ∀ z, meromorphicOrderAt Ψ z = meromorphicOrderAt Φ z) :
    Differentiable ℂ (toMeromorphicNFOn (Ψ / Φ) Set.univ)
      ∧ ∀ z, toMeromorphicNFOn (Ψ / Φ) Set.univ =ᶠ[𝓝[≠] z] Ψ / Φ := by
  have hq : MeromorphicOn (Ψ / Φ) Set.univ := hΨ.div hΦ
  have hrNF : MeromorphicNFOn (toMeromorphicNFOn (Ψ / Φ) Set.univ) Set.univ :=
    meromorphicNFOn_toMeromorphicNFOn _ _
  have hord : ∀ z, meromorphicOrderAt (toMeromorphicNFOn (Ψ / Φ) Set.univ) z = 0 := by
    intro z
    rw [meromorphicOrderAt_toMeromorphicNFOn hq (Set.mem_univ z)]
    have hΨm := hΨ z (Set.mem_univ z)
    have hΦm := hΦ z (Set.mem_univ z)
    rw [div_eq_mul_inv, meromorphicOrderAt_mul hΨm hΦm.inv, meromorphicOrderAt_inv, hsame z]
    exact LinearOrderedAddCommGroupWithTop.add_neg_cancel _ (hΦ0 z)
  refine ⟨fun z => ?_, fun z => hq.toMeromorphicNFOn_eq_self_on_nhdsNE (Set.mem_univ z)⟩
  exact ((hrNF (Set.mem_univ z)).meromorphicOrderAt_nonneg_iff_analyticAt.1
    (le_of_eq (hord z).symm)).differentiableAt

end QOU.QBeta.RatioEntire
