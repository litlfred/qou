| Definition / theorem | Content |
|---|---|
| `pentagonRelationGenerators : Set (PreBlochGroup F)` | ansatz generator set |
| `pentagonSubgroup` | `AddSubgroup.closure` of the generators |
| `BlochGroup F` | `PreBlochGroup F ⧸ pentagonSubgroup` |
| `instance : AddCommGroup (BlochGroup F)` | inherited from `QuotientAddGroup` |
| `quot : PreBlochGroup F →+ BlochGroup F` | canonical projection |
| `quot_zero`, `quot_add` | standard projection lemmas |
| `quot_universal_property` | quotient lifts via Mathlib's `QuotientAddGroup.lift` |
| `hasPentagonRelation_real`, `hasBlochGroup_real` | concrete instances on `F = ℝ` |
