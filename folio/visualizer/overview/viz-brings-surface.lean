/-!
# QOU.BringsSurface.ViewportState — Bring's-surface visualiser state

**Sibling-resolution stub** for content block
[`def:viz-brings-surface`](viz-brings-surface.md).  The buildable
formalisation lives in
[`QOU/BringsSurface.lean §Viewport`](../../quantum-observable-universe/lean/QOU/BringsSurface.lean)
and is compiled by `lake build QOU`.

Canonical declarations:

```lean
inductive QOU.BringsSurface.ViewportMode
  | cp1
  | cone

structure QOU.BringsSurface.CameraState where
  theta, phi, radius : ℝ           -- spherical (θ, ϕ, r)
  lookAt             : Fin 3 → ℝ   -- in (𝔯, 𝔤, 𝔟) colour-sector coords

structure QOU.BringsSurface.ViewportState where
  q       : ℝ                              -- torsion/chirality parameter
  mode    : QOU.BringsSurface.ViewportMode
  camera  : QOU.BringsSurface.CameraState
```

These fields mirror the TypeScript `VizState` schema in
[`folio-assistant/schemas/qou-types.ts §10`](../../../folio-assistant/schemas/qou-types.ts)
so a URL-encoded viewport can be losslessly round-tripped between
the React renderer and the Lean / OCaml back-end.

-- Ref: [leitner2026] folio/visualizer/overview/viz-brings-surface.md
-/
