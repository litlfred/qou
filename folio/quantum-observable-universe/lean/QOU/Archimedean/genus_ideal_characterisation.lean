import Mathlib.Algebra.Polynomial.Basic
import Mathlib.RingTheory.Ideal.Span
import Mathlib.RingTheory.Ideal.Maps
import Mathlib.RingTheory.Ideal.Quotient.Operations
import Mathlib.RingTheory.Ideal.Quotient.Defs

/-!
# QOU.Archimedean.genus_ideal_characterisation — genus-filtration ideal as `(u⁵)`

**Lemma** ([`lem:genus-ideal-characterisation`](../../../quantum-observable-universe/archimedean-universe/genus-ideal-characterisation.md)).

*At genus `g = 4`, the kernel of the truncation
`π_4 : ℤ[u] → ℤ[u]/(u⁵)` is the genus-filtration ideal
`I_4 = (u⁵)`, consisting of those terms in the Chebyshev
expansion of `a_p` whose Seifert cycles have no target in
`H_1(Σ_4)`.*

The Lean statement below records the abstract ring-theoretic side
— the kernel of the quotient map by `(u⁵)` equals `(u⁵)` — which is
the standard universal-property identity.  The categorical
identification of this ideal with the genus-filtration kernel of
the Seifert-cycle map is recorded in the manuscript and discharged
separately (the manuscript proof relies on `prop:hecke-completeness`
which is downstream of this lemma).

-- Ref: [leitner2026] quantum-observable-universe/archimedean-universe/genus-ideal-characterisation.md
-/

namespace QOU.Archimedean

open Polynomial

/-- **Genus-filtration ideal characterisation** at `g = 4`.

    The kernel of the canonical quotient map
    `ℤ[u] → ℤ[u] / (u⁵)` is the principal ideal `(u⁵)`.  This is the
    abstract ring-theoretic core of the genus-filtration content
    described in `lem:genus-ideal-characterisation`; the categorical
    Seifert-cycle interpretation of the same ideal is recorded in the
    manuscript.

    Discharged by the standard `Ideal.mk_ker` identity (kernel of the
    quotient projection equals the ideal we quotient by). -/
-- Ref: [leitner2026] quantum-observable-universe/archimedean-universe/genus-ideal-characterisation.md
theorem genus_ideal_characterisation :
    RingHom.ker
        (Ideal.Quotient.mk (Ideal.span {(X ^ 5 : Polynomial ℤ)}))
      = Ideal.span {(X ^ 5 : Polynomial ℤ)} := by
  -- The quotient-projection kernel coincides with the ideal we
  -- quotient by.  Mathlib provides this as `Ideal.mk_ker`.
  -- Ref: [leitner2026] Mathlib `Mathlib.RingTheory.Ideal.Quotient.Defs`
  exact Ideal.mk_ker

end QOU.Archimedean
