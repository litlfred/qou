import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

/-!
# QOU.MassTheory.ReebLinkingCWF

Conjecture carrier for the CWF linking normalization
([reeb-linking-cwf-normalization.md](reeb-linking-cwf-normalization.md)):
the physical pn-bond linking amplitude is the unit-normalized
exchange-channel component of the bond direction `(1, z)` — square-root
free: `ℓ(z)² · (1 + z²) = z²`.

**Primary conjecture** (§3b-tax): no other conjecture class appears as a
hypothesis, the class field carries the conjecture's *content* (a
parameter-quantified equation in the shape of the claim, not `True`), and
**no instance is provided** — the open state is honest. Per the
Anti-Laundering rule this class is not a proof and does not authorize
production wiring; the MeV unit anchor of the ²H linear law remains open.

The downstream theorem `amplitude_bond_criticality` is fully verified
modulo the class: the amplitude at the Markov bond factor `z = 1/[2]_v`
satisfies the deformed-criticality equation
`g² · (1 + [2]_v²) = 1` of
`QOU.MassTheory.ReebPnMagnitude.ss_det_zero_at_criticality`.

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/

namespace QOU
namespace MassTheory

/-- **Conjecture (CWF linking normalization).**  A linking-amplitude
assignment on bond factors whose square is the unit-normalized transverse
component: `ℓ(z)²·(1+z²) = z²` for every bond factor `z`.  The physical
claim is that the Reeb linking amplitude of the pn bond is this `ℓ`
evaluated at the Markov bond factor.  No instance is provided (open). -/
class ReebLinkingCWF (K : Type*) [Field K] where
  /-- The linking amplitude as a function of the bond factor. -/
  amplitude : K → K
  /-- Unit-tangent (CWF) normalization, square-root free. -/
  amplitude_normalized : ∀ z : K, amplitude z ^ 2 * (1 + z ^ 2) = z ^ 2

/-- **Conditional on `ReebLinkingCWF`** — at the Markov bond factor
`z = t⁻¹` (with `t = [2]_v ≠ 0`) the amplitude satisfies the
deformed-criticality equation `g²·(1 + t²) = 1`: the conjectural CWF
amplitude lands exactly on the marginal-stability point of
`ReebPnMagnitude.ss_det_zero_at_criticality`. -/
theorem amplitude_bond_criticality {K : Type*} [Field K] [ReebLinkingCWF K]
    (t : K) (ht : t ≠ 0) :
    ReebLinkingCWF.amplitude (t⁻¹ : K) ^ 2 * (1 + t ^ 2) = 1 := by
  have h := ReebLinkingCWF.amplitude_normalized (K := K) t⁻¹
  have hinv : t ^ 2 * t⁻¹ ^ 2 = 1 := by
    rw [← mul_pow, mul_inv_cancel₀ ht, one_pow]
  linear_combination t ^ 2 * h
    - (ReebLinkingCWF.amplitude (t⁻¹ : K) ^ 2 - 1) * hinv

end MassTheory
end QOU
