/-!
# Jet-Stratified Gröbner–Shirshov Reduction

Content-block Lean sibling for `def:jet-stratified-reduction`.

The full formalization lives in `UGB/GrobnerShirshov/JetOrder.lean`.
This file re-exports the key declarations for the content pipeline.

LaTeX label: `def:jet-stratified-reduction`

## References
- [fred2005] §3, Proposition 3.8
- [bergman1978] https://doi.org/10.1016/0001-8708(78)90010-5
-/

import UGB.GrobnerShirshov.JetOrder

namespace UGB.GrobnerShirshov.JetStratified

/-! Re-export the key structures and theorems. -/

-- Ref: [fred2005] §3, Proposition 3.8
-- Ref: [bergman1978] https://doi.org/10.1016/0001-8708(78)90010-5

/-- The jet-stratified GS verification criterion.
    See `UGB.GrobnerShirshov.jet_stratified_gs_criterion`. -/
#check @jet_stratified_gs_criterion

/-- The correctness theorem for the combined algorithm.
    See `UGB.GrobnerShirshov.jet_stratified_correct`. -/
#check @jet_stratified_correct

/-- Descended GS inheritance: desc×desc S-polys are free.
    See `UGB.GrobnerShirshov.descended_gs_inherited`. -/
#check @descended_gs_inherited

/-- S-polynomial pair counts. -/
#check @spolyCountNaive
#check @spolyCountStratified
#check @spolySavings

/-- Degree buckets for filtered reduction. -/
#check @DegreeBucket
#check @bucketize

end UGB.GrobnerShirshov.JetStratified
