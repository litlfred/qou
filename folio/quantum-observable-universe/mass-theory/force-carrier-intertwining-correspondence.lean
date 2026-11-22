/-
The force-carrier intertwining correspondence:
  T_{p,q} (genus-4 torus knot) acting on an n-strand braid lands on
  Wedderburn channel λ = (p, 1, ..., 1) of H_n(q).

LaTeX label: `conj:force-carrier-intertwining-correspondence`
Computational evidence:
  computations/delta-q-decoration.witness.json
-/

import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Tactic

namespace QOU.BraidKnot

/- The intertwining-pattern partition: T_{p,q} applied to an n-strand
braid lands on the partition (p, 1, ..., 1) ⊢ n.

The combinatorial principle is straightforward: a p-strand braid
embedded in B_n via natural inclusion intertwines exactly p strands
and leaves (n-p) strands fixed.  The corresponding Hecke / symmetric-
group irrep is V_{(p, 1^{n-p})}.

Verified computationally for p ∈ {2, 3}, n = 4 (the H_2 molecular
case) in delta_q_decoration.py: the dominant Wedderburn weights of
the bare molecular braid σ_1·σ_2·σ_3 ∈ B_4 are at λ ∈ {(3,1), (2,1,1)},
matching the predictions for T_{3,5} and T_{2,9} respectively.

A full Lean proof of the proposition requires:
  - The q-deformed Specht module construction over R = ℤ[q^±1/2, ...]
  - The seminormal-basis representation matrices
  - The natural-inclusion functor B_p → B_n
  - Verification that χ_{(p, 1^{n-p})} carries the dominant weight
    of the inclusion-extended T_{p,q}.

These are downstream of the Mathlib representation-theory roadmap.
For now we formalise the combinatorial core that the full
categorical correspondence asserts: the intertwining-pattern shape
`(p, 1, …, 1)` (one part `p` and `n − p` parts equal to `1`) is a
genuine partition of `n` — i.e. its parts sum to `n`. This is the
arithmetic content that the conjectural Wedderburn-channel selection
`T_{p,q} ↦ V_{(p, 1^{n-p})}` requires; the categorical selection
itself is downstream of `conj:e-hartree-categorical-derivation`.

-- Ref: [leitner2026] §round-18 of conj:e-hartree-categorical-derivation
-/

/-- The intertwining-pattern shape of `T_{p,q}` on `n` strands is the
    partition `(p, 1, …, 1)` with one part `p` and `n − p` unit parts.
    Its parts sum to `n`, so it is a genuine partition of `n` — the
    arithmetic precondition for the Wedderburn channel
    `V_{(p, 1^{n-p})}`. (Coprimality `gcd p q = 1` selects the torus
    knot `T(p,q)`; it is recorded as a hypothesis but not needed for
    the partition-sum fact.) -/
theorem force_carrier_intertwining_correspondence
    (n p q : ℕ) (hp : p ≤ n) (hq : Nat.gcd p q = 1) :
    p + (n - p) * 1 = n := by
  rw [Nat.mul_one]
  omega

end QOU.BraidKnot
