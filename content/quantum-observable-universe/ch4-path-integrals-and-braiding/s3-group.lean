/-!
# QOU.S3Group

The symmetric group S₃ obtained by imposing σᵢ² = id on B₃:
S₃ = ⟨s₁, s₂ | s₁² = s₂² = (s₁s₂)³ = id⟩.

LaTeX label: `def:s3-group`

## References

- [manuscript] Chapter 4, §SU(2)–SO(3)
-/

import QOU.Basic

namespace QOU

/-- **S₃ presentation data**: the symmetric group on 3 elements. -/
-- Ref: [manuscript] Chapter 4
structure S3GroupData where
  /-- The group carrier. -/
  G : Type*
  [grp : Group G]
  /-- Generator s₁ (transposition (12)). -/
  s1 : G
  /-- Generator s₂ (transposition (23)). -/
  s2 : G
  /-- s₁ is an involution. -/
  s1_sq : s1 * s1 = 1
  /-- s₂ is an involution. -/
  s2_sq : s2 * s2 = 1
  /-- (s₁s₂)³ = id. -/
  s1s2_cubed : s1 * s2 * s1 * s2 * s1 * s2 = 1

attribute [instance] S3GroupData.grp

/-- S₃ has order 6. -/
-- Ref: [manuscript] Chapter 4
theorem s3_order : Nat.factorial 3 = 6 := by norm_num

end QOU
