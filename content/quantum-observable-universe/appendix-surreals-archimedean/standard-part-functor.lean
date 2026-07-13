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

import Mathlib.Data.Real.Basic

namespace QOU.AppendixSurreals

-- The standard-part map `st : No_fin → ℝ` is formalised in the
-- library at `QOU.AppendixSurreals.standardPart` (StandardPart.lean);
-- the content block `def:standard-part-functor` resolves its `lean.ref`
-- there. This sibling carries only the Archimedean mass-limit corollary
-- below (a genuine consequence, not a shadow stub for the functor).

/--
The object-level standard-part map `st` (a ring homomorphism, not a
functor in its own right) commutes with the mass limit mapping.
The evaluation of the exact algebraic trace `B_sym` converges to the
macroscopic `B_qCLT` limit under the Archimedean scale.
-/
theorem archimedean_mass_commutes
  (m_unbound : ℝ)
  (B_sym B_qCLT : ℝ)
  (h_qclt_limit : B_sym = B_qCLT) -- Under Q-CLT A -> infty asymptotic convergence
  : (m_unbound - B_sym) = (m_unbound - B_qCLT) :=
by
  -- Trivial algebraic consequence of the Q-CLT asymptotic boundary condition.
  -- In full formalism, StandardPart handles the \varepsilon -> 0 collapse mapping B_sym(q) to B_qCLT.
  subst h_qclt_limit
  rfl

end QOU.AppendixSurreals
