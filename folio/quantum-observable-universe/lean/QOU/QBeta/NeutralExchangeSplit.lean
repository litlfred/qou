import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination

/-!
# The unbroken neutral exchange splits into a photon (Coulomb) part and a `Z` part

Between two particles with weak isospin `T₃`, `T₃'` and hypercharge `Y`, `Y'`, the exchange of
the unbroken neutral bosons `W³` (coupling `g`) and `B` (coupling `g'`) has charge factor
`g²·T₃T₃' + g'²·(Y/2)(Y'/2)`. This is the shape of the invariant Gaudin coupling of audit §28:
no `T₃ ⊗ Y` cross term.

`neutralExchange_split` is the algebraic identity behind electroweak mixing: with
`e² = g²g'²/(g² + g'²)`, `s² = g'²/(g² + g'²)` and `g_Z² = g² + g'²`, the same tensor is
`e²·Q Q' + g_Z²·(T₃ − s²Q)(T₃' − s²Q')`, where `Q = T₃ + Y/2`. The first term is the
Coulomb charge factor. So a Coulomb pair term appears only once the `Z` part is removed, which in
the Standard Model is done by the `Z` mass (a Yukawa factor at long distance). The identity holds
over any field; it fixes neither `s²` nor the `Z` mass.

`nucleon_unbroken_isospin`: for three-quark blocks (`Y = B = 1`, `T₃ = ±1/2`) the unbroken
exchange gives the same value on the proton pair and the neutron pair, as the probe found.
-/

namespace QOU.QBeta.NeutralExchange

variable {K : Type*} [Field K]

/-- Electric charge `T₃ + Y/2`. -/
def charge (T Y : K) : K := T + Y / 2

theorem neutralExchange_split (g2 gp2 T Y T' Y' : K) (hs : g2 + gp2 ≠ 0) (h2 : (2 : K) ≠ 0) :
    g2 * T * T' + gp2 * (Y / 2) * (Y' / 2) =
      (g2 * gp2 / (g2 + gp2)) * charge T Y * charge T' Y' +
        (g2 + gp2) * (T - gp2 / (g2 + gp2) * charge T Y) *
          (T' - gp2 / (g2 + gp2) * charge T' Y') := by
  unfold charge
  field_simp
  ring

/-- Unbroken neutral exchange between two three-quark blocks (`Y = 1`), proton `T₃ = 1/2`,
neutron `T₃ = −1/2`: the proton pair and the neutron pair give the same value. -/
theorem nucleon_unbroken_isospin (g2 gp2 : K) :
    g2 * (1 / 2) * (1 / 2) + gp2 * (1 / 2) * (1 / 2) =
      g2 * (-1 / 2) * (-1 / 2) + gp2 * (1 / 2) * (1 / 2) := by
  ring

/-- The photon part on the same blocks is Coulomb: zero whenever a neutron is involved. -/
theorem nucleon_photon_coulomb (e2 : K) (h2 : (2 : K) ≠ 0) :
    e2 * charge (-1 / 2 : K) 1 * charge (1 / 2 : K) 1 = 0 ∧
      e2 * charge (1 / 2 : K) 1 * charge (1 / 2 : K) 1 = e2 := by
  unfold charge
  constructor
  · ring
  · field_simp; ring

end QOU.QBeta.NeutralExchange
