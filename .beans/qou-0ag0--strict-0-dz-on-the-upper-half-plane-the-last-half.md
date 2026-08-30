---
# qou-0ag0
title: STRICT 0 < D(z) on the upper half plane — the last half of qou-f8lit item 3
status: todo
type: task
priority: normal
created_at: 2026-08-30T14:30:07Z
updated_at: 2026-08-30T14:30:49Z
---

Splits off the remaining half of `qou-f8lit` item 3. The **non-strict** `0 ≤ D(z)` landed
in #6234 (`QOU/Archimedean/BlochWignerNonneg.lean`). This bean is the **strict** one, and
strict is the half that matters: it is what `MathlibExt/ManifoldVolumeBridge.lean`
declines to assume as a class field, and what a general `vol_ne_zero_of_realises` would
need. `Encounter/FiveTwoVolumeBridge` gets `≠ 0` at its own shape only via the chord
comparison, not from any general lemma.

## Why nonneg does not upgrade

`blochWigner_lob_nonneg` descends from `LobMonotonicity.lob_sum_nonneg`, which descends
from **subadditivity** of `Λ` on `[0, π/2]` — not strict. And the Λ-sum genuinely tends to
`0` as the tetrahedron degenerates, so no argument that ignores the boundary can give
strictness.

## The route, and every piece of it is ALREADY IN THE CORPUS

Measured 2026-08-30 — these are read off the files, not guessed:

1. **The chart.** `QOU/Archimedean/LobachevskyMaximum.lean` carries `volChart p =
   Λ(p.1) + Λ(p.2) + Λ(π − p.1 − p.2)` over `closedSimplex` / `angleSimplex` (open).
2. **The boundary is exactly zero, not merely ≥ 0.**
   `volChart_eq_zero_of_not_mem : p ∈ closedSimplex → p ∉ angleSimplex → volChart p = 0`,
   proved face-by-face from `Lob_zero` and `Lob_pi_sub` (`Λ(π−t) = −Λ(t)`).
3. **Strict concavity along a line.** `QOU/Knot/RivinConcavity.lean`
   `strictConcaveOn_tetVolLine (hsum : α + β + γ = π) (htan : u + v + w = 0)
   (hne : ¬(u = 0 ∧ v = 0)) : StrictConcaveOn ℝ (tetLineDomain …) (tetVolLine …)` — the
   same lemma the 5₂ chord used, at a different instantiation.
4. **Milnor + the angle facts**, for transporting a `volChart` statement back to `D(z)`:
   `MathlibExt/IdealTriangulation.lean`'s `volume_eq_lob_sum` (`rfl`), `angle_sum`,
   `angleᵢ_mem`.

**The argument.** Take `p` in the open simplex. Run a line through it; it leaves through
two boundary points `b₀`, `b₁`, and `p` is a strict convex combination of them. Strict
concavity gives `volChart p > t·volChart b₀ + (1−t)·volChart b₁`, and by (2) the right
side is `t·0 + (1−t)·0 = 0`. So `volChart p > 0`, hence `0 < D(z)` for every `0 < z.im`
after (4). Note this needs the boundary value to be **exactly 0** — "≥ 0" would not close
it — which is why (2) rather than the nonneg lemma is the load-bearing input.

## Expected work, and the one place it may bite

The mathematical content is done; this is a parameterisation exercise. The likely cost is
in **hitting the boundary**: constructing the two exit points of a line through an
arbitrary interior point of a 2-simplex, and showing each lands in `closedSimplex ∖
angleSimplex`, is fiddly in Lean even though it is obvious on paper. The 5₂ chord had it
easy — both endpoints were named points chosen in advance. Budget for that, not for the
concavity.

An alternative worth a look before committing to the above: `LobachevskyMaximum` already
proves `exists_isMaxOn_angleSimplex` by pushing the maximiser off the boundary with
exactly these two facts. Whether the same compactness argument gives a *positive lower
bound* on the interior — rather than only locating the max — is not established here and
should be checked first; if it does, it is likely the cheaper route.
