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

## Addendum (later the same day) — does the "degenerate" conciliation work?

Owner asked to check. Three levels, and the answer is the same at each: **it works only as
the split real form.**

**1. What the corpus's own definition supplies.** `def:bring-cone-tetraplectic-structure`
puts on the cone a closed 4-form whose top power is a volume form — on a 4-manifold, just an
$S_5$-averaged volume form. A volume form on the cone induces a volume form on the link and
nothing else; it does not induce a contact form, let alone a triad. The lemma's "where the
bulk carries an invariant volume form, that link carries a 3-Sasakian (degenerate
quaternionic-contact) structure" is therefore not a consequence of the definition it cites.
The genuine geometric structure the cone carries is different and stronger: the restricted
flat metric of $\mathbb{C}^5$ is a Kähler *cone* metric, so the link is **Sasakian** with a
single Reeb field — the fibre rotation $V$ (Boyer–Galicki \cite{boyergalicki2008}). And the
cone minus its vertex is $K_C^{-1}\setminus 0 \cong T^*C \setminus 0$ (fibrewise inversion),
which carries the canonical holomorphic symplectic form. So the cone has a triple of closed
2-forms — the Kähler form and $\mathrm{Re}\,\Omega$, $\mathrm{Im}\,\Omega$ — but the
holomorphic pair has the wrong homogeneity under the cone's scaling to make a 3-Sasakian
triple. That mismatch is what "degenerate" can honestly mean.

**2. Whether an $\mathfrak{su}(2)$ Reeb triad can exist on the link at all.** A 3-Sasakian
3-manifold is a spherical space form $S^3/\Gamma$ (\cite{boyergalicki2008}, Ch. 13), and
$UT(\Sigma_4)$ is aspherical, so no. Stronger: three Reeb vector fields closing into
$\mathfrak{su}(2)$ integrate to an $SU(2)$-action; on a closed aspherical 3-manifold every
orbit of an $SU(2)$-action is a point (orbits are $S^3/\Gamma$, $S^2$, $\mathbb{RP}^2$ or
points, and the first three are excluded by asphericity and irreducibility), so the action
is trivial and the fields vanish. There is no degenerate way around this at the level of
vector fields.

**3. What triad the link does carry, and its brackets.** $UT(\Sigma_4)$ has three genuine
contact forms: the connection form (Reeb field $V$, fibre rotation), the Liouville form
(Reeb field $X$, geodesic flow), and the Liouville form pulled back by a quarter turn in
the fibre (Reeb field $X^\perp$). These are the left-invariant frame of $\mathrm{PSL}(2,\mathbb{R})$,
and with $X = H/2$, $X^\perp = (E+F)/2$, $V = (E-F)/2$:

$$
[X, X^\perp] = V,\qquad [X^\perp, V] = X,\qquad [V, X] = -X^\perp .
$$

Exactly one cyclic bracket has the opposite sign to $\mathfrak{su}(2)$'s
$[e_1,e_2]=e_3,\ [e_2,e_3]=e_1,\ [e_3,e_1]=e_2$. That is $\mathfrak{sl}_2(\mathbb{R}) \cong
\mathfrak{so}(2,1)$, and no real rescaling of the basis reaches $\mathfrak{su}(2)$.

**In the lemma's own terms.** Replace the quaternions by the *split* quaternions
($i^2=-1$, $j^2=k^2=+1$; the algebra $M_2(\mathbb{R})$, whose unit-norm elements are
$\mathrm{SL}(2,\mathbb{R})$) and run the identical right-multiplication construction.
`lean/QOU/BringConeSplit.lean` (sorry-free, same proof script as `BringCone.lean`) gives

$$
[M_i, M_j] = 2M_k,\qquad [M_j, M_k] = -2M_i,\qquad [M_k, M_i] = 2M_j ,
$$

and `split_ne_compact` records that the flipped bracket differs from the compact one in any
characteristic-zero ring. So: the lemma's identities are true, and they are the identities
of the real form that $UT(\Sigma_4)$ does **not** carry. The conciliation works if and only
if "degenerate quaternionic-contact" is read as "split" — and then the structure constants
in the lemma are $(2, -2, 2)$, not $(2, 2, 2)$, and the geodesic flow is a Reeb field.

**What survives of the $\mathfrak{su}(2)$.** The structure group of the $\mathbb{H}$-valued
resolvent bundle along the Reeb ($V$) flow — an internal symmetry, exactly as
`rem:tetraplectic-su2-gauge-reading` already reads it, and unaffected by any of this. What
does not survive is the phrase "an $\mathrm{SU}(2)$ triad of contact forms and dual Reeb
fields" on this link.

**Consequence for the knot complements.** Every component of the canonical closure is a
$(2, 2g+1)$-torus knot with complement $\mathrm{PSL}(2,\mathbb{R})/\Delta(2,2g+1,\infty)$
(`prop:canonical-closure-torus-chain`), so the split triad $\{V, X, X^\perp\}$ is the
coordinate frame on those complements as well, with the same brackets.
