-- Ref: [robinson1966] Robinson, *Non-standard Analysis*, North-Holland.
-- Ref: [alling1987] Alling, *Foundations of Analysis over Surreal Number
--      Fields*, North-Holland.
--
-- Sibling stub for `def:standard-part-functor`.
--
-- The compiled formalisation lives in:
--   QOU/AppendixSurreals/StandardPart.lean
--
-- See `QOU.AppendixSurreals.standardPart`,
--     `QOU.AppendixSurreals.standardPart_spec`,
--     `QOU.AppendixSurreals.standardPart_of_infinitesimal`,
--     `QOU.AppendixSurreals.standardPart_add`,
--     `QOU.AppendixSurreals.standardPart_mul`.

namespace QOU.AppendixSurreals

/-- Standard-part functor $\\mathrm{st} : \\mathbf{No}_{\\mathrm{fin}} \\to \\mathbb{R}$ -/
def StandardPart   :=
  -- Ref: [manuscript] def:standard-part-functor
  trivial

end QOU.AppendixSurreals
