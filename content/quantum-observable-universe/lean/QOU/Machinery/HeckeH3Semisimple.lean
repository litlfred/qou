import QOU.Machinery.HeckeH3Wedderburn
import QOU.MathlibExt.MatrixSemisimple

/-!
# QOU.Machinery.HeckeH3Semisimple — Prop-level semisimplicity of H₃(q)

The corollary unlocked by `QOU.MathlibExt.MatrixSemisimple` (which
fills the division-ring case of Mathlib's `proof_wanted
IsSemisimpleRing.matrix`): transferring `IsSemisimpleRing` along the
explicit rank-3 Wedderburn isomorphism `wedderburn₃` of
`HeckeH3Wedderburn` gives **`IsSemisimpleRing (H3A K (q - q⁻¹))`** at
every Wenzl-generic parameter — the rank-3 semisimplicity statement
the cited `WenzlCriterion` / `SchurElementCriterion` classes carry,
now *proved* rather than cited at this rank (bean `qou-vndn`,
epic `qou-otbb`).

Base ring (§7c): generic `[Field K]`; no archimedean construct.

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01404457
-/

namespace QOU.Machinery.H3

variable {K : Type*} [Field K]

/-- **H₃(q) is a semisimple ring at every Wenzl-generic parameter
    (sorry-free):** transfer along the explicit Wedderburn isomorphism,
    with the matrix factor supplied by
    `QOU.MathlibExt.MatrixSemisimple`. -/
theorem isSemisimpleRing_H3A (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    IsSemisimpleRing (H3A K (q - q⁻¹)) :=
  ((wedderburn₃ q hq h2 h3).symm.toRingEquiv).isSemisimpleRing

end QOU.Machinery.H3
