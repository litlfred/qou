/-
  Lifted-crossing locality conjecture.

  The contribution of a lifted-crossing subset S to the categorical
  mass factorizes as a product of single-crossing local factors:

      m_GB(β|_{S lifted}) = m_GB(K) · ∏_{c ∈ S} η(c)

  where η(c) depends only on the crossing c, not on the rest of S.

  Consequence: the crossing-graded expansion collapses to

      m(K; q) = m_GB(K) · ∏_{c} (1 + ξ(q) · η(c)).

  Expected to hold at generic q (not a root of unity), enforced by
  flatness of the KZ connection (Kohno-Drinfeld).  Fails at roots
  of unity (Jones-Wenzl truncation).

  Ref: [kohno1987] https://doi.org/10.5802/aif.1075
  Ref: [manuscript] Ch 11 §8 / lifted-crossing-locality
-/

import Mathlib.Data.Real.Basic
import Mathlib.Data.List.Basic

namespace QOU.ParticleInteractions

/-- **Lifted-crossing locality** (conjectural class).
    Asserts that the GB mass of a subset of lifted crossings
    factorizes through a single-crossing local factor η. -/
class LiftedCrossingLocality
    (K : Type*)   -- atomic link configuration
    (C : Type*)   -- crossings of that link
    where
  crossings     : K → List C
  massGB        : K → ℝ                         -- base GB mass
  massGBSubset  : K → List C → ℝ                -- mass with lifted S ⊆ crossings
  localFactor   : C → ℝ                         -- η(c)
  factorization :
    ∀ (k : K) (S : List C),
      S ⊆ crossings k →
      massGBSubset k S = massGB k * (S.map localFactor).prod
  -- Ref: [kohno1987] https://doi.org/10.5802/aif.1075
  -- Flatness of the KZ connection at generic q gives the
  -- factorization; fails at roots of unity.

/-- Product-form collapse of the crossing-graded expansion under
    locality: if the locality factor η(c) is homogeneous (η ≡ 1),
    the expansion collapses to (1 + ξ)^c. -/
noncomputable def productFormCollapse
    {K C : Type*} [LiftedCrossingLocality K C]
    (k : K) (xi : ℝ) : ℝ :=
  let c := (LiftedCrossingLocality.crossings k).length
  LiftedCrossingLocality.massGB k * (1 + xi) ^ c

end QOU.ParticleInteractions
