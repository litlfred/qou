/-!
# Borel partial resolution of the keystone sharpness target

`prop:borel-partial-resolution` from
`borel-partial-resolution.md`. Borel's rank theorem for
`K_{2n-1}^{ind}(F) ⊗ ℚ` provides an *unconditional upper bound*
on the dimensions involved in the keystone B1 (Mikusiński depth =
Goncharov period depth) for fields F embeddable in ℂ.

Scaffolding only; full version uses Borel rank rather than
restating it.
-/

import Mathlib.Tactic

namespace QOU.AppendixSurreals.BorelPartialResolution

/-- **Proposition (`prop:borel-partial-resolution`).**
    For any number field F embeddable in ℂ and any n ≥ 2,
    Borel's rank theorem gives
       rk K_{2n-1}^{ind}(F) = r_1 + r_2          (n even)
       rk K_{2n-1}^{ind}(F) = r_2                (n odd)
    where (r_1, r_2) are the real/complex embeddings of F.  This
    *unconditionally* bounds the genuinely-new depth-n content
    over F from above (with Beilinson conjectural for saturation
    at n ≥ 3). -/
theorem borel_partial : True := by
  -- Ref: [bloch2000] Bloch, Higher regulators, K-theory, and
  --   zeta functions.
  -- Ref: [suslin1991] Suslin, K_3 of a field, and the Bloch group.
  -- Ref: Borel (1977) "Cohomologie réelle stable de groupes
  --   S-arithmétiques classiques" — the rank theorem.
  -- Ref: [manuscript] §prop:borel-partial-resolution — explicit
  --   dimension table for cyclotomic and Bring-natural fields.
  -- Ref: Beilinson conjecture (conditional for lower-bound
  --   saturation at n ≥ 3).
  trivial

end QOU.AppendixSurreals.BorelPartialResolution
