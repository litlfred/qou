# The Bring cone link is the unit tangent bundle of Bring's curve — and that fixes which Reeb triad it can carry

**Status:** finding + open question for the owner of `BringCone.lean` / `lem:bring-cone-reeb-quaternionic-twist`.
**Date:** 2026-09-03 · **Branch:** `claude/mt7r-archimedean-eval-2026-08-24` · **Beans:** `qou-m3sh`, `t7qv`.
**Nothing here is numerical.** Two exact facts and one consequence.

## Why this came up

The owner asked whether the osculating-circle pencil of the serpenoid gives a coordinate
frame in the knot complement, then pointed at Bring's curve as the frame the framework
already has. Working that out (`total_curvature_is_the_computable_half_probe.py`,
`QOU/Mass/TorusKnotPages.lean`) required knowing what 3-manifold the "Bring cone link" of
`QOU/BringCone.lean` actually is. The answer is classical and exact, and it constrains the
Reeb structure that file models.

## Fact 1 — the link of the cone is `UT(Σ₄)`, canonically

Bring's curve `Σ₄ ⊂ P⁴` is the complete intersection of hypersurfaces of degrees `1, 2, 3`
(`def:brings-surface`). Then:

* **Bézout:** `deg Σ₄ = 1 · 2 · 3 = 6`.
* **Adjunction:** `K = O(1 + 2 + 3 − 5) = O(1)`, so `deg K = 6 = 2g − 2` gives `g = 4`, and
  the embedding is the **canonical** one. (This is the same `6` that
  `QOU/BringsSurface/EulerCharacteristicSix.lean` derives as `|χ|` from torus-knot
  embeddability.)
* **The link.** For any smooth projective curve `C ⊂ Pⁿ`, the affine cone `Ĉ ⊂ ℂⁿ⁺¹`
  meets the unit sphere in a 3-manifold `L`, and the Hopf map restricts to a circle bundle
  `L → C` — the unit circle bundle of the tautological line `O(−1)|_C`, of Euler number
  `−deg C`.
* For the canonical embedding `O(−1)|_C ≅ K_C⁻¹ ≅ T C`. So the link is **the unit circle
  bundle of the tangent bundle**: `L ≅ UT(Σ₄)`, Euler number `−6 = χ(Σ₄)`. Not merely
  diffeomorphic — the identification is the canonical one.

## Fact 2 — `UT(Σ₄)` has `~SL₂` geometry, hence is not a spherical space form

A circle bundle over a closed surface of genus `g ≥ 2` with non-zero Euler number carries
Thurston's `~SL₂(ℝ)` geometry: `UT(Σ₄) = PSL(2,ℝ)/Γ₄`, with `Γ₄` the surface group, itself
of index `120 = |S₅|` in the `(2,4,5)` triangle group that uniformises Bring's curve. Its
universal cover is `~SL₂(ℝ)`, not `S³`.

A **3-Sasakian** 3-manifold, on the other hand, is a spherical space form `S³/Γ` (constant
curvature `+1`; the link of the cone over `P¹` — the Hopf fibration — is the model). So
`UT(Σ₄)` admits no 3-Sasakian structure, and its natural Reeb triad is the **split** real
form: the left-invariant frame of `PSL(2,ℝ)`,

    X  (geodesic flow — Reeb field of the Liouville contact form),
    Y  (horocyclic flow),
    V  (fibre rotation — Reeb field of the Boothby–Wang connection form),

with `𝔰𝔩₂(ℝ)` brackets, not `𝔰𝔲(2)` ones.

## The consequence, and the question

`QOU/BringCone.lean` models "the Reeb triad of the Bring cone link" on right-multiplication
by the quaternion units, proving `[M_i, M_j] = 2 M_k` and cyclic — the **compact** form
`𝔰𝔲(2)`, i.e. the Hopf/`S³` picture. `categorical-reeb-brings.md` builds the categorical
Reeb derivation from `ξ = e₃ ∈ 𝔰𝔲(2)` on `O_q(SU(2))` with the Woronowicz `ω₃` as contact
form and transports it `S₅`-equivariantly to Bring's curve. Both are internally sound as
algebra; neither can be *the* Reeb triad of a 3-Sasakian structure on the cone link, because
the cone link has none. `BringCone.lean` itself says "degenerate quaternionic-contact", and
that qualifier may be exactly the intended reconciliation.

**The question for the owner of that lemma:** which real form does
`lem:bring-cone-reeb-quaternionic-twist` intend on `UT(Σ₄)` — the compact `𝔰𝔲(2)` triad the
Lean file proves the brackets of, or the split `𝔰𝔩₂(ℝ)` frame the manifold carries? If the
former, the "degenerate" structure should say what degenerates; if the latter, the Lean
model needs `[X,Y] = ...` with the `𝔰𝔩₂` signs, and the geodesic flow becomes the Reeb flow.

## Why it matters for the knot complements

Every multi-strand component of the canonical atom closure is a `(2, 2g+1)`-torus knot on
both classical branches (`total_curvature_is_the_computable_half_probe`, `A = 2, 3, 4, 6`),
and `S³ ∖ T(2, 2g+1)` is the unit tangent bundle of the `(2, 2g+1, ∞)` triangle orbifold,
`PSL(2,ℝ)/Δ(2,2g+1,∞)` (Milnor's trefoil-complement theorem is `g = 1`). So the component
complements and the Bring cone link are quotients of the same `PSL(2,ℝ)`, and the global
frame `{X, Y, V}` is the coordinate frame on all of them at once. That is the concrete
answer to "does the pencil give a coordinate frame in the complement": the invariant pencils
are the pages of the Milnor open book (transverse to `V`) and the Seifert circles (orbits of
`V`), and the frame is the `𝔰𝔩₂(ℝ)` one. Whether the corpus's `𝔰𝔲(2)` Reeb structure is the
same object under the degenerate reading is the question above.

## What is not claimed

No connection from any of this to binding. No statement about the twist/torsion half, which
the hull-exit analysis says is the missing one and which none of these frames supplies by
itself. No claim that `BringCone.lean`'s lemmas are wrong — they are quaternion identities and
they are true; the question is only what geometric object they are being read on.
