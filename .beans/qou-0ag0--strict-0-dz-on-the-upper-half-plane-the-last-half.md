---
# qou-0ag0
title: STRICT 0 < D(z) on the upper half plane — the last half of qou-f8lit item 3
status: completed
type: task
priority: normal
created_at: 2026-08-30T14:30:07Z
updated_at: 2026-08-30T14:54:38Z
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


---

## 2026-08-30 — CLOSED, and the route this bean predicted was the expensive one

`QOU/Archimedean/BlochWignerPositive.lean` and `QOU/MathlibExt/ManifoldVolumePositive.lean`
(#6263), all six declarations `lean`-direct exit 0 and axiom-clean:

    lob_sum_pos             0 < Λα + Λβ + Λγ
    volume_pos              0 < T.volume
    blochWigner_lob_pos     0 < D(z)  for  0 < z.im
    triangulation_volume_pos  0 < n → 0 < T.volume
    vol_pos_of_realises       0 < n → Realises T m → 0 < vol m
    vol_ne_zero_of_realises

**Correcting this bean's own prediction.** It said the cost would be in *"hitting the
boundary — constructing the two exit points of a line through an arbitrary interior point
and showing each lands in `closedSimplex ∖ angleSimplex`"*, and told the next agent to
budget for that. **None of it was needed.** Keep both chord endpoints strictly *interior*,
at `t = ∓ε` with `ε = min(α, γ)/2`, and bound them below with the **non-strict**
`lob_sum_nonneg` — their angle triples are still positive and still sum to `π`. The target
is the midpoint, so strict concavity does the rest. The strictness comes from the
concavity, not from the endpoint values, so the endpoints never need to be the places
where the sum vanishes.

`volChart_eq_zero_of_not_mem` — the boundary-vanishing lemma this bean identified as the
load-bearing input — is **not used at all**.

**Third instance of the same error class in one session**, and worth naming as such:

| claim | where | what was actually true |
|---|---|---|
| `qou-f8lit` item 2 "blocked on 16-digit bounds", then "blocked by the method" | the bean | the chord route never approximates a constant; no digit bound needed |
| "strictness needs the angles bounded away from the corners, or a strict subadditivity" | `BlochWignerNonneg` header, written the same day | needs neither |
| "the cost is in constructing the boundary exit points" | this bean | the boundary is never touched |

Each named an obstacle to the *route being attempted* and stated it as an obstacle to the
*problem*. All three were mine, and all three would have sent the next agent the long way
round.

**Downstream payoff.** `MathlibExt/ManifoldVolumeBridge.lean` deliberately declines to
carry positivity as a fourth class field, calling the alternative *"the easy and dishonest
move"*. That judgement is **vindicated**: it was derivable, so assuming it would have been
assuming a theorem. Note the genuine side condition — `0 < n` cannot be dropped, because
`IdealTriangulation 0` is legitimate and its volume is the empty sum.
