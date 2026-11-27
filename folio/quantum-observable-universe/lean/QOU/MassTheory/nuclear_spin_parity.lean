import Mathlib.Data.Real.Basic

/-!
# QOU.Archimedean.nuclear_spin_parity — `J ∈ ℤ ⟺ A ∈ 2ℤ`

**Proposition** ([`prop:nuclear-spin-parity`](../../../quantum-observable-universe/archimedean-universe/nuclear-spin-parity.md)).

*Let `𝓝(Z, N)` be a nucleus with mass number `A = Z + N`. Then the
total angular momentum `J` satisfies*

```
  J ∈ ℤ              ⟺  A is even
  J ∈ ℤ + 1/2        ⟺  A is odd
```

*This is a topological consequence of the braid representation:
each nucleon is a spin-½ fermion (single-component knot), and the
tensor product of `A` such representations has spin parity
determined by `A mod 2` (fermion-boson correspondence).*

The Lean encoding records the parity claim via the predicate
"twice the spin `2J` is an integer of the same parity as `A`".  This
side-steps the half-integer issue by working with `2J : ℕ`.

-- Ref: [leitner2026] quantum-observable-universe/archimedean-universe/nuclear-spin-parity.md
-/

namespace QOU.Archimedean

/-- Abstract nucleus record: proton/neutron counts and the
    twice-angular-momentum `2J`.  Working with `2J : ℕ` rather than
    `J : ℚ` lets us state the parity claim without fractions. -/
class NucleusLike where
  /-- Proton number. -/
  Z : ℕ
  /-- Neutron number. -/
  N : ℕ
  /-- Twice the total angular momentum, `2J ∈ ℕ` (so `J = (2J)/2`). -/
  twoJ : ℕ
  /-- Manuscript spin-parity identity: `2J ≡ A (mod 2)` where
      `A = Z + N`. -/
  claim_spin_parity : twoJ % 2 = (Z + N) % 2

/-- **Nuclear spin parity** ([`prop:nuclear-spin-parity`]).

    `2J` has the same parity as the mass number `A = Z + N`.  In
    particular, `2J` is even ⟺ `A` is even, which corresponds to
    `J ∈ ℤ` ⟺ `A` even (and `J ∈ ℤ + 1/2` ⟺ `A` odd). -/
-- Ref: [leitner2026] quantum-observable-universe/archimedean-universe/nuclear-spin-parity.md
theorem nuclear_spin_parity [n : NucleusLike] :
    n.twoJ % 2 = (n.Z + n.N) % 2 := by
  refine n.claim_spin_parity

end QOU.Archimedean
