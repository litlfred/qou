---
# qou-fm7s
title: 'NS vector 1: geometric depletion (Constantin–Fefferman) mapped to the QOU direction/Levi field'
status: in-progress
type: task
priority: normal
created_at: 2026-10-12T20:57:48Z
updated_at: 2026-10-12T20:57:48Z
parent: qou-vo9t
---

Owner (2026-10-12): pursue NS attack vectors 1, 2, 3 and 5 (unforced NS). This bean is v1. Formalize first: a genuine Lean core lemma where one exists, honest conditional statements otherwise, and an audit doc.

## 2026-10-13 — v1 delivered on branch `ns-v1` (status stays in-progress: the mapping question is open)

- **Lean [sorry-free]:** `QOU/FluidDynamics/GeometricDepletion.lean`. It holds the kernel algebra D(e₁,e₂,e₃) = (e₁·e₃)det(e₁,e₂,e₃): D = 0 on e₃ = ±e₂; D is even in e₃ and odd under a global flip; and for unit vectors D² ≤ |e₂×e₃|² ≤ min(|e₃−e₂|², |e₃+e₂|²). Verified with lean-direct, exit 0; axioms are propext, Classical.choice and Quot.sound. No PDE statement or carrier.
- **Mapping verdict:** no QOU quantity is the Constantin–Fefferman hypothesis.
  - On a 3D contact manifold the corpus forces ker Θ = ξ^⊥ only on the filament.
  - The Levi data is one scalar, ξ·curl ξ, so the two eigenvalues and cond in core-levi-form are undefined in dimension 3.
  - Under that reading, branch (A) "non-degenerate ⇒ singular" is false: u = e^{−νt}(sin z, cos z, 0) on T³ is a counterexample.
- **True conditional statement (contrapositive of Beirão da Veiga–Berselli):** a smooth-solution blowup forces the vorticity line field to lose ½-Hölder coherence. The corpus's anti-parallel argument never addresses filament bending.
- **Audit:** `docs/audits/2026-10-12-ns-v1-geometric-depletion.md`.
- **Next:** filament-curvature probe; owner decision on what Θ is off the filament; ingest the literature.
