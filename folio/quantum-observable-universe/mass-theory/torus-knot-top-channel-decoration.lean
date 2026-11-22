/-
Top-channel decoration of a positive torus knot on its braid index.

LaTeX label: `def:torus-knot-top-channel-decoration`

  δ_q^top(T_{m,p}) := q^w − q^{−w},   w = (m−1)p   (m ≤ p).

Base ring (AGENTS.md §7c): a generic commutative ring with the modulus
carried as a unit `q : Rˣ`; no division and no ordering.
-/

import Mathlib.Algebra.Ring.Parity

namespace QOU.TorusKnotTopChannel

variable {R : Type*} [CommRing R]

/-- The top-channel decoration `q^w − q^{−w}` at writhe `w = (m−1)p`.
    The braid-index condition `m ≤ p` is a hypothesis on the presentation
    and is recorded in the narrative definition, not in this function. -/
def topChannelDecoration (q : Rˣ) (m p : ℕ) : R :=
  (q : R) ^ ((m - 1) * p) - (↑q⁻¹ : R) ^ ((m - 1) * p)

/-- For `m = 2` and odd `p` the top-channel decoration equals the sum of the
    two 2-strand Hecke characters `q^p + (−q⁻¹)^p`. (For even `p` it does not.) -/
theorem topChannelDecoration_two_eq_char_sum (q : Rˣ) {p : ℕ} (hp : Odd p) :
    topChannelDecoration q 2 p = (q : R) ^ p + (-(↑q⁻¹ : R)) ^ p := by
  unfold topChannelDecoration
  rw [hp.neg_pow]
  simp [sub_eq_add_neg]

end QOU.TorusKnotTopChannel
