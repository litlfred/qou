/-!
# QOU.BraidKnot.per_nucleon_shift_additive_linearity — `shift(Z+1, N) − shift(Z, N) = 18`

**Proposition** ([`prop:per-nucleon-shift-additive-linearity`](../../../quantum-observable-universe/braids-and-knots/per-nucleon-shift-additive-linearity.md)).

*The atomic Markov-trace denominator
`D(u) = 2^{2A+1} · u^{shift} · (1 + u²)^{3A−1}` of canonical
pppnnn ordering has shift exponent satisfying the additive-
linearity recurrence:*

```
  shift(Z+1, N) − shift(Z, N) = 18,
  shift(Z, N+1) − shift(Z, N) = 21,    for Z, N ≥ 1 (A ≥ 2)
```

*Together with the base case `shift(D) = shift(1, 1) = 40`, this
fixes the shift on the entire `A ≥ 2` triangle.*

-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/per-nucleon-shift-additive-linearity.md
-/

namespace QOU.BraidKnot

/-- Abstract context for the per-nucleon shift additive linearity. -/
class PerNucleonShiftContext where
  /-- The shift exponent `shift(Z, N) : ℤ`. -/
  shift : ℕ → ℕ → ℤ
  /-- Base case: `shift(1, 1) = 40`. -/
  shift_base : shift 1 1 = 40

/-- **Per-nucleon shift additive linearity**
    ([`prop:per-nucleon-shift-additive-linearity`]).

    Both proton-direction and neutron-direction increments are
    constant integers `18` and `21` respectively, for `Z, N ≥ 1`. -/
-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/per-nucleon-shift-additive-linearity.md
theorem per_nucleon_shift_additive_linearity
    [ctx : PerNucleonShiftContext] (Z N : ℕ) (hZ : 1 ≤ Z) (hN : 1 ≤ N) :
    ctx.shift (Z + 1) N - ctx.shift Z N = 18 ∧
    ctx.shift Z (N + 1) - ctx.shift Z N = 21 := by
  -- Manuscript proof: empirical verification across 6 atoms
  -- (A=2,3,4,5,6) of the canonical pppnnn ordering; structural
  -- proof from the Markov-trace product formula deferred.
  -- Ref: [manuscript] quantum-observable-universe/braids-and-knots/per-nucleon-shift-additive-linearity.md
  sorry

end QOU.BraidKnot
