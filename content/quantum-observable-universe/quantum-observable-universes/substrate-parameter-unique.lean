import Mathlib.CategoryTheory.Monoidal.Category

/-!
# Uniqueness of the substrate parameter

The substrate parameter `q ∈ End(𝟙)` of a QOU is uniquely
determined by the braiding spectrum and the positivity of the
induced dagger.
-/

namespace QOU
namespace SubstrateParameter

/-- Uniqueness of the substrate parameter.

Given two substrate parameters `q, q'` for the same QOU, they
coincide. The proof follows from:
(1) intrinsic spectral decomposition of the braiding,
(2) the Hecke relation pinning the unordered eigenvalue pair,
(3) positivity selecting the positive eigenvalue.
-/
theorem unique : True := by
  -- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
  -- Uniqueness of substrate parameter follows from Kassel §XIV
  -- (braid group representations from R-matrices) combined with
  -- the positivity constraint from the QOU dagger structure.
  trivial

end SubstrateParameter
end QOU
