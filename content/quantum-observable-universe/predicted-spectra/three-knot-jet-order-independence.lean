/-!
# QOU.Archimedean.JetOrderIndependence — conjectural sibling stub

**Sibling-resolution stub** for content block
[`conj:three-knot-jet-order-independence`](three-knot-jet-order-independence.md):
*Jet-order algebraic independence (QOU-attackable reduction)*.

The full §3b-cond formalisation — the two QOU-native conjectural
classes (`JetOrderIndependence`, `SurrealParallelTransportBound`) plus
the **gap-closing reduction** `hyperbolicVolumeIndependence_of_reduction`
deriving the deep `HyperbolicVolumeIndependence` from them — lives at
[`../lean/QOU/Archimedean/JetOrderIndependence.lean`](../lean/QOU/Archimedean/JetOrderIndependence.lean)
under the `qou` Lake package. That file documents the surreal
parallel-transport bound on the projective state fibre `ℂP¹` and its
three open issues (uniformity in jet order, archimedean projection,
monodromy separation at the root-of-unity limit). The reduction is
fully Lean-verified modulo the two conjectural class instances.

-- Ref: [manuscript] quantum-observable-universe/predicted-spectra/three-knot-jet-order-independence.ts
-/

namespace QOU.Archimedean

/-- **CONJECTURE (weak, QOU-attackable).** Jet-order algebraic
    independence of the three coloured-Jones series. -/
class JetOrderIndependence where
  holds : Prop
  -- Ref: [manuscript] conj:three-knot-jet-order-independence

end QOU.Archimedean
