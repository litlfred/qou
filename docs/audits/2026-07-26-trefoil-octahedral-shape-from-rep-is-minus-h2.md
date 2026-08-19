# The trefoil octahedral tetrahedron shape, from the pinned rep, is exactly −h² — cracking the #4315 "need the shapes" wall

**Date:** 2026-07-26 · **Branch:** `claude/pinched-octahedral-e2-r-attempt-2026-07-26` ·
**Axis:** Δ_λ binding — μ₀ −9% closure, the octahedral shapes / `e₂` / `r` · **Owner steer:** *"Both"*
(attempt the #4315 pinched-limit `e₂`) + *"Quaternion acting"* · **Tier:** rigorous shape (exact) +
honest quaternion assessment (scope-(a); no fit; nothing wired).

## 0. The obstacle, and the way through

#4315 reduced `g₂` to the octahedral `e₂` finite part but needed the four per-crossing tetrahedron
shapes; SnapPy gives only the degenerate 2-tet `{½, 2}` (torus knot), not the octahedral
decomposition. This note gets the shape **from the boundary representation** instead — fully pinned by
`m = q₀`, no free parameter.

## 1. The rigorous shape (exact, from the rep)

The four strand-endpoints at a crossing are the fixed points on `ℂP¹` of the meridian holonomies:
`ρ(u) = [[m,1],[0,1/m]]` fixes `{∞, a = 1/(1/m−m)}`; `ρ(v) = [[m,0],[c,1/m]]` fixes `{0, b = (m−1/m)/c}`
(`c = −(m⁴−m²+1)/m²`, the pinned coloring). Their cross-ratio gives the tetrahedron shape triple
`(z, z' = 1/(1−z), z'' = (z−1)/z)` with **product `−1`** (a genuine ideal tetrahedron):

| form | value | at `q₀` |
|---|---|---|
| `z` | `(m⁴−m²+1)/(m²−1)² = −c/(m−1/m)²` | `23.88` |
| **`z' = 1/(1−z)`** | **`−(m−1/m)² = c+1 = −h²`** (exact) | **`−0.04371`** |
| `z''` | `m²/(m⁴−m²+1)` | `0.958` |

**So the octahedral tetrahedron shape (the `z'` form) *is* the bar-even `−h²`, proven from the
boundary rep** — not asserted. The octahedral geometry and the bar-even coloring `c+1 = −h²` (#4319)
are the **same object**. This cracks the #4315 "need the shapes" wall from the representation side:
the shape is a definite, pinned, forward quantity.

## 2. The quaternion steer — honest assessment

The ideal octahedron's symmetry group is the **binary octahedral group `2O ⊂ SU(2)`** (unit
quaternions), and the meridian holonomy lies on the boost hyperbola `barEven² − barOdd² = 4` (a rotor
norm — exact). Two honest observations:

- The substrate **meridian trace `barEven = m + 1/m = 2.0109` is a *deformation of the parabolic*
  (trace 2)**, not a clean `2O` trace (`√2, 1, 0, 2`). So the meridian is not literally a
  binary-octahedral element; it is the near-identity deformation.
- A `log|z|` proxy for the pairwise `e₂` does **not** give `g₂` (ratio `−227`). The real octahedral
  `e₂` requires the **geometric quantum-dilogarithm amplitude** `a_j = log Λ(z_j)` (2509.02354 §5.2,
  the pinched regular part), not `log|z_j|`.

So the `2O` / quaternion octahedral symmetry is the natural structure for *combining* the four
tetrahedra into `e₂`, but the `e₂ → r` closure needs that quantum-dilog amplitude — which remains the
open computation. The steer names the right symmetry; it does not, by itself, supply the amplitude.

## 3. Scope (honest) and net

**scope-(a).** Derived: the octahedral tetrahedron shape from the rep, `z' = −h²` exactly (fully
pinned). **Not** derived: `r` = the `e₂` finite part (needs the geometric quantum-dilog amplitude +
the octahedral/quaternion combination of the four tetrahedra). Anti-laundering stands.

**Net (the whole g₂ chain).** `g₂ = 1 + r`: the leading `1` is exact (real coloring, #4339); the
octahedral tetrahedron shape carrying the bar-even structure is exactly `−h²` (this note, from the
rep); `r` is the pinched-limit `e₂` of the four dilog amplitudes, combined by the `2O` octahedral
(quaternion) symmetry — a single, well-posed, non-fishing object, still open. The remaining step is
the geometric quantum-dilogarithm on the pinned shape `z' = −h²` and its octahedral partners.

Refs: probe [`trefoil_octahedral_shape_from_rep_probe.py`](../../computations/deltalambda/trefoil_octahedral_shape_from_rep_probe.py);
#4339 (`g₂_leading=1`); #4315 (octahedral `e₂` wall); #4319 (`c+1=−h²`);
`library/arxiv-2509.02354v2/2509.02354v2.pdf` §5.2 (pinched geometric quantum dilog).
