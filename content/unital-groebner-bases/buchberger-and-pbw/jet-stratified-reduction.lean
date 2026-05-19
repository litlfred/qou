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

-- Ref: [fred2005] §3, Proposition 3.8
-- Ref: [bergman1978] Bergman, "The diamond lemma for ring theory," Adv. Math. 29 (1978)

export UGB.GrobnerShirshov
  ( jet_stratified_gs_criterion
    jet_stratified_correct
    descended_gs_inherited
    spolyCountNaive
    spolyCountStratified
    spolySavings
    DegreeBucket
    bucketize )
