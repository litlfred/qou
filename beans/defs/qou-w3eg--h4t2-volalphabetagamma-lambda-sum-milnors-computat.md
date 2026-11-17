---
# qou-w3eg
title: 'H4/T2: Vol(alpha,beta,gamma) = Lambda-sum — Milnor''s computation, decomposed into H4-1..H4-5'
status: in-progress
type: task
priority: medium
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T17:40:00Z
updated_at: 2026-11-17T08:44:47Z
parent: b9cj
---

The hard tier of `qou-5gai`, and the same statement as `qou-idvt` **T2**:

    hypVolume (idealTetrahedron α β γ)  =  Λ(α) + Λ(β) + Λ(γ)

**Honest scale estimate: this is a multi-week formalization, not a session.**
It is recorded decomposed so it can be attacked incrementally, and so a future
agent does not re-derive the decomposition. `qou-7y3g` already judged it
"infra-scale, not a session-scale task" — that judgement stands and this bean
does not contradict it; it only makes the steps explicit.

## Why it is worth doing at all

The **whole right-hand side already exists, sorry-free**. T3/T4 (PR #4773) proved
strict concavity of the Λ-sum on the angle simplex, that the regular triple is
its unique maximiser, and that the maximum value is exactly `Cl₂(π/3)`. Every one
of those is currently labelled **analytic**, and each becomes the corresponding
**geometric** theorem the moment H4 lands — including Milnor's "the regular ideal
tetrahedron maximises volume" and the `V_tet` half of `qou-7y3g`. H4 is the
single hinge converting a finished analytic package into geometry.

## Decomposition

**H4-1 — the vertical integral. DONE (PR #4773).**
`∫_{z₀}^{∞} z^{-3} dz = 1/(2z₀²)`, and at the hemisphere height
`z₀ = √(R²−d²)` the fibre contributes `1/(2(R²−d²))`.
`QOU.Archimedean.HyperbolicVolume.integral_Ioi_rpow_neg_three` /
`integral_Ioi_hemisphere`, sorry-free. Self-contained: needs neither H3 nor
Fubini. This is the step that makes the approach work at all — the vertical
integral **converges**, collapsing 3-D volume to a 2-D base integral.

**H4-2 — Fubini: `Vol(region) = ∫∫_base dA / (2(R²−d²))`.**
Needs H3 (the region) and the product-measure Fubini for `withDensity`.

> **CORRECTION (2026-08-08, same day).** An earlier revision of this bean said
> H4-2 was blocked because `Mathlib.MeasureTheory.Constructions.Prod.*` was
> absent from the restored olean cache. **That was wrong** — I had tried the
> wrong module path. Fubini IS available:
> `Mathlib.MeasureTheory.Integral.Prod` and `Mathlib.MeasureTheory.Measure.Prod`
> are both present, giving `lintegral_prod` and `Measure.volume_eq_prod`.
> **H4-2 is not blocked on infrastructure.** Its real cost is H3 (getting the
> region definition right) plus one genuine bridge: `hypVolume` is an `ℝ≥0∞`
> `lintegral` while H4-1 is a Bochner `∫`, so the two must be reconciled
> (`ofReal` / `lintegral` ↔ `integral`) before the inner integral can be
> substituted.

> **H4-2 is DONE (2026-08-08, sorry-free) — bean `qou-hqzr`.** Both predicted
> costs were real and neither was larger than predicted (the Pi/Prod split is
> one measure-preserving definition; the `∫⁻`/`∫` bridge goes through
> `ofReal_integral_eq_lintegral_ofReal` on H4-1's integrability). **One finding
> that changes H4-3:** the fibre mass is `⊤` *on* the circle, and Milnor's base
> triangle is INSCRIBED — its three vertices lie on it. So the usable statement
> is the a.e. one, `hypVolume_chimney_of_ae_lt`; **H4-3 must consume that, not**
> the pointwise open-disk corollary. File
> `QOU/Archimedean/HyperbolicVolumeFubini.lean`.

**H4-3 — the base integral over one triangle.** Reduce
`∫∫_T dA/(2(R²−d²))` over the Euclidean triangle inscribed in the circle of
radius `R`. Milnor's route: cut `T` at the circumcentre into 6 right triangles
and evaluate each. This is where `−log|2 sin|` first appears, i.e. where `Λ'`
(T1, already proved) enters.

**H4-4 — the orthoscheme value `= ½Λ(θ)`.** The analytic core: each of the 6
pieces integrates to half a Lobachevsky value. Uses T1's
`hasDerivAt_Lob : Λ' = −log(2 sin t)` as the antiderivative — already in the
tree, which is the one piece of luck here.

> **H4-4 is DONE (2026-08-09, sorry-free) — PR #4842**, in the 1-D form the base
> integral reduces to after the elementary radial integration:
> `∫₀^ψ −¼·log((cos²φ − cos²ψ)/cos²φ) dφ = ½Λ(ψ)` for `0 < ψ < π/2`
> (`integral_orthoscheme`, file `QOU/Archimedean/OrthoschemeBaseIntegral.lean`).
> Cross-checked numerically at six angles before formalization.
>
> **Three things a later agent should not re-derive:**
> 1. **`Λ` as a primitive across the CLOSED interval** is now available:
>    `integral_neg_log_two_sin : ∫_a^b −log(2 sin t) = Λ(b) − Λ(a)` on
>    `0 ≤ a ≤ b ≤ π`, plus the `log sin` form `integral_log_sin_eq` (which
>    carries the `(b−a)·log 2` explicitly) and `Lob_eq_integral`. T1 gave only
>    the pointwise derivative on the OPEN interval; the endpoints are where the
>    orthoscheme actually lives.
> 2. **The log singularity is not a blocker.** Mathlib's
>    `intervalIntegrable_log_sin` / `intervalIntegrable_log_cos` hold on ANY
>    interval — no `0 ∉ [[a,b]]` side condition, unlike
>    `intervalIntegral.intervalIntegrable_log`. So no Jordan-inequality
>    comparison argument is needed; the split `log(2 sin t) = log 2 + log sin t`
>    costs an a.e. rewrite (`ae_sin_ne_zero`) since it fails exactly on the null
>    set where `sin` vanishes.
> 3. **The `log 2` cancellation is the normalization check.** Three `log 2`
>    terms enter with coefficients `−ψ, −ψ, +2ψ` and cancel exactly. A wrong
>    factor of 2 in the `Λ' = −log(2 sin)` normalization would leave a residual
>    `ψ·log 2` that no Λ-identity can absorb.

> **H4-3 is DONE (2026-08-09, sorry-free) — PR #4842**, file
> `QOU/Archimedean/OrthoschemePolarReduction.lean`. All three predicted costs
> were real and none larger than predicted: the polar description of the
> triangle, the radial integral, and a second `∫⁻`/`∫` bridge.
>
> **Composing H4-2 + H4-3 + H4-4 gives the tier's first three-dimensional
> statement:**
>
>     hypVolume (chimney (orthoBase R ψ) R) = ENNReal.ofReal (Lob ψ / 2)
>
> (`hypVolume_chimney_orthoBase`) — a hyperbolic volume on the left, `Λ` on the
> right. **Still not about ideal tetrahedra**: that a chimney over an inscribed
> triangle *is* the ideal tetrahedron of the matching dihedral angles is
> Milnor's geometric identification and is untouched.
>
> **Three things a later agent should not re-derive:**
> 1. **The region is defined in CARTESIAN coordinates** (`orthoBase R ψ`, the
>    open triangle with vertices `(0,0)`, `(R cos ψ, 0)`, `(R cos ψ, R sin ψ)`)
>    and its polar description is a THEOREM (`mem_orthoBase_polar`). A
>    polar-parameterised definition would have assumed the step being proved.
> 2. **A single orthoscheme needs only the POINTWISE disk hypothesis.**
>    `orthoBase_subset_disk`: the OPEN triangle lies strictly inside the disk
>    (`x² + y² < x²/cos²ψ < R²`), so H4-2's `hypVolume_chimney_of_subset_disk`
>    applies directly. The a.e. form (`hypVolume_chimney_of_ae_lt`) is still the
>    one **H4-5** will need, because the CLOSED inscribed triangle has its three
>    vertices *on* the circle.
> 3. **The base integral carries no `R`.** The radial value depends only on
>    `r₀/R = cos ψ / cos φ`. That is H2's dilation invariance surfacing, and it
>    is why H4-4 could be stated with no radius in it.

> **H4-5 is now the only open step of the tier** (H4-1 ✅ H4-2 ✅ H4-3 ✅
> H4-4 ✅). What remains: cut the inscribed triangle at the circumcentre into
> six orthoschemes, apply `hypVolume_chimney_orthoBase` to each, and pair the
> halves into `Λ(α)+Λ(β)+Λ(γ)`. Two things make it more than bookkeeping:
> (a) the six pieces must be shown to tile the triangle up to null sets, with
> the angle at the circumcentre for the two pieces adjacent to a side equal to
> the *inscribed* angle at the opposite vertex (central angle = twice inscribed
> angle) — that is the geometric input that makes the six halves pair up;
> (b) the **obtuse case** — with the circumcentre outside the triangle a piece
> enters with a **minus** sign, and Milnor states the subdivision only "if all
> three angles are acute". `ψ < π/2` in `hypVolume_chimney_orthoBase` is exactly
> where that bites. Still wanting Ratcliffe §10.4 or full-text Thurston Ch. 7
> for the sign convention.

**H4-5 — assemble.** The 6 halves pair up into `Λ(α)+Λ(β)+Λ(γ)`. Bookkeeping
once H4-4 is done, but the sign/orientation conventions are the classic place to
go wrong (obtuse triangles put the circumcentre outside `T`, and the
corresponding piece enters with a **minus** sign — Milnor handles this by signed
areas; do not assume the acute case is general).

> **H4-5b + H4-5c-i are DONE (2026-08-09, sorry-free) — PR #4864**, which also
> carries #4842's five tiers forward onto current `main` (they had drifted ~388
> commits behind). Files
> [`OrthoschemeWedgePair.lean`](../folio/quantum-observable-universe/lean/QOU/Archimedean/OrthoschemeWedgePair.lean)
> and
> [`OrthoschemeRotation.lean`](../folio/quantum-observable-universe/lean/QOU/Archimedean/OrthoschemeRotation.lean).
> H4-5 was **split**, because the "bookkeeping" framing above hid a real
> infrastructure step:
>
> | step | statement | status |
> |---|---|---|
> | **H4-5b** the PAIR | `hypVolume (chimney (wedge R ψ) R) = Λ(ψ)` — a WHOLE `Λ`: two mirror orthoschemes at `½Λ` each | ✅ |
> | **H4-5c-i** ROTATION | `hypVolume (chimney (wedgeAt R θ ψ) R) = Λ(ψ)` — the same, at ANY axis | ✅ |
> | **H4-5c-ii(a)** the Λ-SUM | `hypVolume (chimney (milnorWedges R t α β γ) R) = Λ(α)+Λ(β)+Λ(γ)` | ✅ |
> | **H4-5c-ii(b)** the TILING | `milnorWedges =ᵐ` the inscribed triangle | ✅ **(PR #4883)** |
>
> **The Λ-sum landed** — `hypVolume_chimney_milnorWedges`, the first statement
> in the tier with `Λ(α)+Λ(β)+Λ(γ)` on the right, for `0 < α,β,γ < π/2` with
> `α+β+γ = π`. It is stated on the *explicit union of the three wedges*, not on
> a triangle. The statement is falsifiable, not vacuous: the RHS is `ofReal` of
> a positive number, so an empty union would refute it.
>
> **The disjointness trick, because it is the reusable part.** Do NOT read off
> each wedge's angular interval and try to show the intervals are disjoint mod
> `2π` — that drags in `arctan`, branch choices and modular angle arithmetic.
> `inner_perp_rotL` gives
>
>     ⟨rot_θ v, (−sin(θ+ψ), cos(θ+ψ))⟩ = −v₁ sin ψ + v₂ cos ψ
>
> — **the `θ` cancels** — so each wedge lies strictly inside a half-plane through
> each of its own edges, and two wedges sharing an edge direction are separated
> by that one line. A linear inequality. `2π`-periodicity is needed in exactly
> one place, the wrap-around pair.
>
> **Acuteness is now earned rather than imported.** A wedge fits strictly inside
> a half-plane bounded by its own edge exactly when its opening `2ψ < π`. The
> half-angles ARE the inscribed angles, so "`ψ < π/2` for all three" **is** "all
> three angles acute" — Milnor's hypothesis, arrived at from the separation
> argument. (Still not evidence the identity fails otherwise; see the green note
> below.)
>
> Two things worth carrying forward:
>
> 1. **Rotation invariance was NOT bookkeeping, and is now paid for.** `ℝ × ℝ`
>    carries the PRODUCT (sup) norm, so a rotation is *not* a
>    `LinearIsometryEquiv` and Mathlib's inner-product-space volume lemmas do
>    **not** apply. The route that works is `det = 1` (norm-independent) via
>    `Measure.map_linearMap_addHaar_eq_smul_addHaar`. Do not go looking for the
>    isometry lemma — it is the wrong shelf. Note also that measure-preservation
>    alone is insufficient: `lintegral_rotL_image` carries an explicit
>    integrand-invariance hypothesis, discharged here by `rotL_normSq`.
> 2. **`wedgeAt` is defined CARTESIAN** (dot products against the rotated frame),
>    with `wedgeAt_eq_image` the theorem — same discipline as `orthoBase`. A
>    definition-as-image would have made the rotation a definition rather than a
>    theorem.
>
> What is left is **one** set identity, `milnorWedges =ᵐ` the closed inscribed
> triangle. Both inclusions are genuine work: `⊆` needs, within each wedge's
> angular range, that the *other two* chord constraints follow from its own;
> `⊇` needs that the three consecutive angular ranges close the circle (that is
> `α+β+γ = π`, already used for the wrap-around disjointness) *and* that the
> radial cut is right. The exceptional set is the three spines, hence `=ᵐ`.
>
> **It is worth proving — the lemma is TRUE, checked at the SET level.** The
> probe evaluates both memberships independently (wedges by the Lean
> definition, triangle by its three half-plane tests) over a polar grid of
> interior points for five acute triangles, boundary/spine skin excluded:
> **zero mismatches**. That is stronger than the Λ-sum agreement, which pins
> the two only to equal *measure*. Whoever takes it on is proving something
> true, not hunting a sign error.

> **🟩 The obtuse case is a scope-(a) worry about the ARGUMENT, not the
> STATEMENT (settled numerically 2026-08-09, PR #4864).** This bean and its
> siblings have repeatedly flagged the obtuse case as "the place to go wrong"
> in wording that reads as though the *identity* were acute-only. **It is not.**
> Probe
> [`milnor_subdivision_obtuse_scope_probe.py`](../computations/milnor_subdivision_obtuse_scope_probe.py)
> (witness `milnor-subdivision-obtuse-scope-probe.witness.json`, 15/15) computes
> both sides independently and finds `Λ(α)+Λ(β)+Λ(γ)` reproducing the base
> integral to `~1e-17` for obtuse triangles **and** for the right-triangle
> boundary `α = π/2` — the acute cases agree to `~2e-15`, limited by the log
> singularities at the vertices, so the obtuse agreement is if anything cleaner.
>
> **Consequence for H4-5c-ii, and it is a narrowing:** the target statement is
> **uniform in the three angles**. What the obtuse case needs is a **signed
> assembly of the same wedges** (the circumcentre leaves the triangle, so one
> wedge is subtracted rather than added), **not a different theorem**. The
> long-standing "still wanting Ratcliffe §10.4 for the sign convention" is
> therefore about *how to write the assembly*, not about *what is true* — and a
> reader who cannot get Ratcliffe is not blocked on the mathematics.
>
> Scope note per AGENTS.md §"Before declaring refuted": this is scope-(a)
> (an argument does not apply unchanged), and it **refutes** the stronger
> reading that the identity is acute-only. It wires to nothing.

> **H4-5c-ii(b) — the TILING is under attack (2026-08-09, resumed after the
> Λ-sum).** Route settled and *numerically certified before any Lean was
> written*; recorded here so it is not re-derived. Three ingredients, none of
> which needs `arctan`, barycentric coordinates, or a convex-hull API:
>
> 1. **The wedge is exactly THREE half-planes.** For `0 < ψ < π/2`,
>
>        wedgeAt R θ ψ  =  {w·u_θ < R cos ψ} ∩ {w·v_{θ−ψ} > 0} ∩ {w·v_{θ+ψ} < 0}
>
>    (`u_φ = (cos φ, sin φ)`, `v_φ = (−sin φ, cos φ)`). The two edge conditions
>    ARE `|w·v_θ| < (w·u_θ)·tan ψ`, by dividing by `cos ψ > 0`. `wedgeAt_upper` /
>    `wedgeAt_lower` (already proved, for the disjointness) are one direction of
>    this; the tiling needs the converse too.
>
> 2. **`⊆` is ONE linear identity, not a convexity argument.** For a wedge at
>    `(θ, ψ)` and the *next* chord half-plane at `(θ+ψ+ψ', ψ')`:
>
>        cos ψ · F  =  sin(ψ+ψ') · G₂  +  cos ψ' · G₃
>
>    where `F = R cos ψ' − w·u_{θ+ψ+ψ'}` (the goal), `G₂ = −(w·v_{θ+ψ})` (the
>    shared-edge slack, `> 0` by `wedgeAt_upper`) and `G₃ = R cos ψ − w·u_θ`
>    (the wedge's own chord slack, `> 0` by definition). Both coefficients are
>    positive because `0 < ψ+ψ' < π` — **which is exactly acuteness again**, the
>    same place it entered the disjointness. `sympy` certificate: the residual is
>    `−cos ψ'·(w·u_θ)·(sin²ψ+cos²ψ−1)`, i.e. **one** `linear_combination` on
>    `Real.sin_sq_add_cos_sq ψ`, and the `θ`-Pythagoras is not needed at all.
>    The mirror case (`θ−ψ−ψ'`, using `wedgeAt_lower`) has the *same* certificate.
>
> 3. **`⊇` is a sign relation, not a covering computation.** With
>    `x = w·v_t`, `y = w·v_{t+2γ}`, `z = w·v_{t+2γ+2α}`:
>
>        sin(2α)·x + sin(2β)·y + sin(2γ)·z = 0
>
>    All three coefficients are `> 0` (`2α, 2β, 2γ ∈ (0, π)` — acuteness a third
>    time), so **`x, y, z` cannot be all-positive or all-negative**. The six
>    surviving sign patterns each land in one sector, and `T ⊆ H_i` gives
>    `T ∩ S_i ⊆ W_i` for free. So the covering needs no geometry beyond this one
>    relation. Certificate: coefficient `2·cos α·sin α·(w₁ sin t − w₂ cos t)·
>    (cos²γ+sin²γ+1)` on the γ-Pythagoras.
>
> The exceptional set is the three *lines* `x=0`, `y=0`, `z=0` (not merely the
> three spine segments) — larger than needed, but null and much cheaper: each is
> the kernel of a nonzero linear functional.
>
> **Pre-Lean numerical certification** (all in this session, before writing Lean):
> both `⊆` identities and the sign relation to `< 9e-15` over 20 000 random
> parameter draws each; the half-plane triple's three vertices lie on exactly two
> chord lines each and strictly inside the third (0 violations / 300 triangles);
> and `milnorWedges` vs the half-plane triple agree at the **set** level on
> 59 999 interior grid points across 40 random acute triangles (0 mismatches),
> with 0 all-same-sign occurrences in 200 000 draws.
>
> **H4-5c-ii(b) LANDED (2026-08-09, sorry-free) — PR #4883**, file
> [`OrthoschemeTiling.lean`](../folio/quantum-observable-universe/lean/QOU/Archimedean/OrthoschemeTiling.lean).
> 22 declarations, `#print axioms` clean on every one. **The H4 tier's target
> is now a statement about a triangle:**
>
>     hypVolume (chimney (inscribedTriangle R t α β γ) R) = ofReal (Λ α + Λ β + Λ γ)
>
> All three predicted ingredients held exactly as certified; the route above
> needed no revision. Four things worth carrying forward:
>
> 1. **The `⊆` lemmas need no `0 < R`.** The wedge's own chord slack `G₃` comes
>    straight from membership, so a degenerate `R` makes the wedge empty and the
>    statement vacuous rather than false — the same strengthening H4-5b made for
>    `wedge_subset_disk`. Do not add the hypothesis back.
> 2. **The a.e. form of H4-2 is what gets spent here.** `hypVolume_chimney_of_ae_lt`,
>    not the pointwise `_of_subset_disk` — exactly as `qou-hqzr` predicted when
>    it noted the inscribed triangle has its three vertices ON the circle where
>    the fibre mass is `⊤`. The prediction was correct and cost nothing extra.
> 3. **`Measure.addHaar_submodule` is the right shelf for the null lines** —
>    each edge line is `LinearMap.ker` of a nonzero functional, and `≠ ⊤` is
>    witnessed by `(−sin φ, cos φ) ↦ 1`. Do not go looking for a graph-of-a-
>    function or a Fubini-slice argument.
> 4. **`precision-gates.sh` does not exist on this branch's base.** It is on
>    `main` but postdates #4864's base commit; it had to be run from
>    `git show origin/main:scripts/precision-gates.sh`. Its red (raw-float64,
>    39 new dirty witnesses) is **entirely pre-existing** and does not implicate
>    the new probe or witness — checked by name. A later rebase onto current
>    `main` picks the script up normally.
>
> **The honesty question this step raises, and it is NOT about the tiling.**
> Defining the inscribed triangle *as* the intersection of the three chord
> half-planes makes the tiling provable but risks assuming the geometry. The
> anchor: prove the three vertices are on the boundary in the right pattern
> (each on exactly two chord lines, strictly inside the third) — that pins the
> half-plane triple to *the* triangle with those vertices. A full
> `interior (convexHull {P₁,P₂,P₃})` identification is NOT attempted; say so.

## Prerequisites still open

* **H2** (`qou-5gai`) — the invariances. Strictly speaking H4 can be *stated*
  without H2, but until dilation-invariance is proved the object has no claim to
  the name "hyperbolic", so H4 without H2 would prove a statement about
  `dx dy dz/z³` and not about hyperbolic volume.
* **H3** — the ideal-tetrahedron region. Needed by H4-2. Getting the
  *definition* right (rather than convenient) is the real risk in this tier.

## GUARD (inherited, and it is the point)

Do **NOT** axiomatise H4 as a Lean class and consume it downstream — that is the
laundering AGENTS.md forbids, and `qou-7y3g` names it explicitly. Until H4 is
proved: `volChart` stays **defined** as the Λ-sum and labelled analytic;
`Vol(4₁) = 2·V_tet` stays **numerical, labelled numerical**. A tier that cannot
be closed gets a bean, not a `sorry`.

## 2026-08-08 UPDATE — the sources landed (commit `31264594`)

The owner uploaded four of the six wanted refs; **Ratcliffe §10.4 and Thurston
Ch. 7 stayed paywalled**. What the sources changed:

**1. Milnor 1982 full text is in `library/milnor-1982-hyperbolic-geometry-the-first-150-years/milnor-1982-hyperbolic-geometry-the-first-150-years.pdf`** — the Appendix
carries the proof. It states the target verbatim:

> "ideal hyperbolic 3-simplex … If α, β, γ are the dihedral angles along three
> edges meeting at a common vertex, then α + β + γ = π and
> volume = Λ(α) + Λ(β) + Λ(γ)."

and the route, which **confirms the H4-2/H4-3 decomposition above** rather than
revising it: *place the simplex with one face on the hemisphere
`z = (1−x²−y²)^{1/2}` and the opposite vertex at ∞, then project orthogonally to
the unit disk*. The orthoscheme computation ends
`(Λ(π/2+a) + Λ(2a) + Λ(π/2−a) − Λ(0))/4`, which the duplication identity
collapses to **`volume = Λ(a)/2`** — H4-4 exactly as scoped.

**2. H4-4's two inputs are now PROVED (sorry-free).** Milnor's proof needs `Λ`
π-periodic and `Λ(2a) = 2Λ(a) + 2Λ(a+π/2)`; both follow from Clausen lemmas
already in the tree:

| new | how |
|---|---|
| `Lob_add_pi : Λ(t+π) = Λ(t)` | `Cl_2_add_two_pi` (Λ doubles the argument) |
| `Lob_duplication : Λ(2a) = 2Λ(a) + 2Λ(a+π/2)` | `Cl_2_duplication` at `θ=2a` + `Cl_2_two_pi_sub` at `π−2a` |

Both numerically cross-checked to `1e-31` at five angles. Milnor's **general**
multiplication identity `Λ(nθ) = n Σ_{k mod n} Λ(θ + kπ/n)` is NOT proved — only
the `n=2` case the volume proof consumes. General case still open here.

**3. The AFP Poincaré Disc entry has NO volume theory — checked, not assumed.**
Source extracted from `library/afp-Poincare_Disc-current.tar.gz`: 11 theory
files, **11 289 lines**, and **0 hits** for `volume` / `area` / `lebesgue` /
`integral`. Its sections are h-lines, h-distance, h-betweenness, h-circles,
h-perpendicularity, Tarski axioms — a **synthetic** development in the
**2-dimensional disc**, not Riemannian and not `H³`.

> **Consequence, and it is the important one: there is NO prior art to port.**
> Hyperbolic *volume* appears to be unformalized in every proof assistant, not
> just Mathlib. H4 is new formalization, not a translation exercise. This
> raises confidence in the multi-week estimate rather than lowering it.

**4. `library/arxiv-1010.5321v3/1010.5321v3.pdf` = Horváth, *Formulas on hyperbolic volume*** —
orthoscheme volume via the Lobachevsky integral, explicitly avoiding the
Schläfli differential formula, with edge-lengths as parameters. Worth reading
for H4-4 if Milnor's angle-parameter route proves awkward in Lean; not yet read
past the abstract.

**5. Neumann–Zagier is `library/neumann-zagier-1985-volumes-of-hyperbolic-three-manifolds-co/neumann-zagier-1985-volumes-of-hyperbolic-three-manifolds-copy-b.pdf`** — the
filename confirms DOI `10.1016/0040-9383(85)90004-7`, so the "unverified from
memory" DOI in the table below was **correct**. Still safe to cite only after a
proper read.

**Still wanted:** Ratcliffe §10.4 (paywalled) — or any full-text Thurston Ch. 7 —
specifically for the **obtuse-triangle sign convention** in H4-3/H4-5, which
Milnor's Appendix compresses and which is the flagged place to go wrong.

## Literature wanted

DOIs below marked **[verified]** were checked online this session; the rest are
from memory and **must be verified before being added to `references.ts`** — do
not copy an unverified DOI into the bibliography.

| ref | what it is wanted for | link |
|---|---|---|
| **Milnor 1982**, *Hyperbolic geometry: the first 150 years*, Bull. AMS 6(1):9–24 | THE source for `Λ`, the ideal-simplex volume, and the regular-maximiser theorem. The proof to follow for H4-3..H4-5. **[verified]** — added to `references.ts` as `milnor1982` in PR #4773 | https://doi.org/10.1090/S0273-0979-1982-14958-8 · [Project Euclid, open](https://projecteuclid.org/journals/bulletin-of-the-american-mathematical-society-new-series/volume-6/issue-1/Hyperbolic-geometry-The-first-150-years/bams/1183548588.full) |
| **Thurston 1978**, *Geometry and Topology of Three-Manifolds*, **Ch. 7 "Computation of volume"** (the chapter is by Milnor) | the orthoscheme decomposition in its original form. Already in `references.ts` as `thurston1978` | http://library.msri.org/books/gt3m/ |
| **Ratcliffe**, *Foundations of Hyperbolic Manifolds* (Springer GTM 149), §10.4 | the most textbook-explicit ideal-tetrahedron volume derivation — likely the easiest to follow line-by-line into Lean. *DOI unverified* | — |
| **Neumann & Zagier 1985**, *Volumes of hyperbolic three-manifolds*, Topology 24(3):307–332 | the `Vol + i·CS` framing; relevant to H5 and to `Vol(4₁)`. *DOI unverified* (`10.1016/0040-9383(85)90004-7` from memory) | — |
| **Lewin 1981**, *Polylogarithms and Associated Functions* | `Λ`/`Cl₂` identities beyond what the corpus has. Already in `references.ts` as `lewin1981` | — |
| **AFP: Poincaré Disc Model** (Simić, Marić, Boutry), Isabelle/HOL | the closest existing **formalization** of hyperbolic geometry in any prover — worth reading for how they set up the model before we commit to `ℝ×ℝ×ℝ`. *Existence from memory, unverified* | https://www.isa-afp.org/entries/Poincare_Disc.html |
| **arXiv 1010.5321**, *Formulas on hyperbolic volume* | surfaced while verifying Milnor; may carry a more directly formalizable closed form. Unread | https://arxiv.org/abs/1010.5321 |

**What I actually want first:** Ratcliffe §10.4 or Thurston/Milnor Ch. 7 in
full text, to fix the H4-3..H4-5 route (in particular the obtuse-triangle sign
convention) before writing any Lean. The paper-search MCP returned empty for
every query this session — likely firewalled — so these need fetching by hand.

## Links

* `qou-5gai` — the H1–H5 EPIC this is H4 of
* `qou-idvt` T2 — the same statement from the ideal-tetrahedron side
* `qou-7y3g` — consumer; `Vol(4₁)=2·V_tet` stays numerical until this lands
* `qou-krvm` (iv) — consumer, via H5

── UNBLOCK 2026-09-03: the source the bean wanted IS in the library ──

The bean's 'what I actually want first' — Milnor Ch.7 full text for the
obtuse-triangle sign convention, thought firewalled — is HELD:
`library/milnor-1982-hyperbolic-geometry-the-first-150-years/sections/sec-000-h-upsl2c-which-is-uniquely-determined-up-to-inne.md`
(pp. 10-12), found via corpus-grep path 5. Milnor's *Hyperbolic geometry: the
first 150 years*, Lemma 2 = exactly our target: ideal 3-simplex with dihedral
angles α,β,γ at a vertex, α+β+γ=π, volume = Ji(α)+Ji(β)+Ji(γ) (Ji = our Lob).
The base integral is set up in the Beltrami upper-half-space model with
dx dy dz/z³ (matches the corpus's hypVolume), projected to the inscribed
triangle in the unit disk — i.e. exactly the HyperbolicVolumeFubini → orthoscheme
chain the corpus already formalized (acute).

**The obtuse handling, verbatim (sec-004 line 66-68):** 'If all three angles are
acute, then barycentrically subdividing from the origin, we obtain six right
triangles... (The case of an obtuse angle can be handled by *a similar argument,
or by analytic continuation*.)' So Milnor gives TWO routes, and does not spell
out a signed-subdivision sign convention — the 'similar argument' is left to the
reader; the clean route is **analytic continuation**.

**LANDED this session (PR #6045, merged e711d1fb1):** the analytic prerequisites
for the obtuse case, in QOU/Archimedean/IdealTetObtuseReduction.lean, sorry-free:
- at_most_one_obtuse; third_angle_acute_of_obtuse (γ≥π/2 ⟹ α+β≤π/2);
- lob_sum_eq_reflected: Λ(α)+Λ(β)+Λ(γ) = Λ(α)+Λ(β) − Λ(α+β), all-acute-args when
  γ obtuse (via IdealTetrahedronConcavity.Lob_pi_sub, which is Milnor's own
  π-periodic+odd fact, sec-004 lines 19-23).

**Recommended route for the remaining Lean = ANALYTIC CONTINUATION, not signed
geometry.** Both sides are functions of (α,β) on the open simplex {α>0,β>0,
α+β<π}. The Λ-sum side Λ(α)+Λ(β)+Λ(π−α−β) is real-analytic there (Lob = Cl₂(2·)/2,
Cl₂ real-analytic on (0,2π) — the corpus has hasDerivAt_Cl_2_series +
tendstoLocallyUniformlyOn as the analyticity input). The acute region
{α,β<π/2, α+β>π/2} is a nonempty open subset where hypVolume_chimney_inscribedTriangle
already proves equality with the base integral. If the base-integral side is shown
real-analytic in (α,β) (differentiation under the integral — the genuinely hard
Mathlib step, but bounded and standard), the identity theorem for real-analytic
functions (Mathlib AnalyticOn / eqOn) extends the equality to the whole simplex,
obtuse included — no signed-subdivision geometry, no sign convention needed.

So the remaining open piece is precisely: (i) Lob real-analytic on (0,π);
(ii) the base integral real-analytic in the two angle parameters; (iii) glue via
the identity theorem. (i) is short; (ii) is the multi-session core; (iii) is
mechanical. The signed-subdivision route is NOT needed and should not be attempted
— Milnor himself offers analytic continuation as the alternative.

## Step-1 (Lob real-analytic on (0,π)) cost MEASURED — 2026-09-04 (session lean-qa-backlog)

Neither route to step 1 is a bounded one-turn win; both are genuine Mathlib-gap builds. Measured against restored Mathlib v4.24.0 + corpus Archimedean tree:

**Antiderivative route (Lob' = -log(2 sin t) analytic ⇒ Lob analytic):**
- Mathlib has `AnalyticOnNhd.deriv` (analytic ⇒ deriv analytic) but NO converse (antiderivative-of-analytic-is-analytic). Not in `Analysis/Calculus/FDeriv/Analytic.lean`.
- `analyticAt_sin`/`analyticOnNhd_sin` are ℂ-ONLY (Trigonometric/Deriv.lean:61,69). No real-analyticity of `Real.sin`.
- No `Real.log` analyticity lemma anywhere in Mathlib SpecialFunctions/Log/.
- So even the input lemma (`-log(2 sin t)` analytic on Ioo 0 π) needs restrictScalars gymnastics (ofReal∘sin∘re, ofReal∘log-on-slit∘re), and the antiderivative step has no Mathlib lemma at all.

**Complex-composition route (Lob θ = Im cLiTwoExt(e^{iθ}) on the unit circle):**
- Corpus HAS `BlochWigner_lob z = Im (cLiTwoExt z) + log‖z‖·arg(1−z)` (BlochWignerLobachevsky.lean:441); on ‖z‖=1 the log term vanishes ⇒ clean `Im cLiTwoExt`.
- BUT ComplexDilogBridge proves cLiTwo analyticity only LOCALLY on `Metric.ball (1/2) (1/2)`. The arc e^{iθ}, θ∈(0,π) (upper unit circle) is NOT in that ball. Extending cLiTwoExt analyticity to a nbhd of the upper unit circle (minus the z=1 branch point) is itself a multi-step build, plus the angle-side identity Lob θ = BlochWigner_lob(e^{iθ}).

Corpus DOES have (usable inputs, not the assembly): hasDerivAt_Lob, hasDerivAt_neg_log_two_sin, deriv_deriv_Lob (LobachevskyDerivative.lean); Cl_2 defn+boundary+continuous_Cl_2 (ClausenFunctionMathlibFiller.lean); cLiTwo + local reflection via identity theorem (ComplexDilogBridge.lean, sorry-free, qou-gkco).

Conclusion: step 1 is genuinely multi-session, matching the plan's 'short but needs Cl₂ analyticity' note — the 'short' was optimistic. Recommend either (a) build the antiderivative-of-analytic Mathlib filler as a standalone reusable lemma first, or (b) extend cLiTwo analyticity to the upper unit circle. Step 2 (base integral analytic in (α,β)) remains the multi-session core regardless.

## Step 1a LANDED — Λ' analytic on (0,π) (2026-09-04, session lean-qa-backlog)

New file QOU/Archimedean/LobachevskyDerivativeAnalytic.lean, lean-direct exit 0, all decls [propext, Classical.choice, Quot.sound]:
- analyticAt_real_sin / analyticAt_real_cos — real sin/cos analytic (Mathlib has ℂ side + AnalyticAt.re_ofReal; no ℝ-side lemma existed).
- analyticAt_neg_log_two_sin — Λ'(t) = -log(2 sin t) analytic on (0,π); AnalyticOnNhd form too.

Corrects the prior step-1 cost measurement: Mathlib DOES carry Real.analyticAt_log (0<x) and analyticWithinAt_rexp in Complex/Analytic.lean (the earlier Log/-dir grep missed them), and AnalyticAt.re_ofReal is the sin/cos bridge. So Λ' analytic was a one-file win, not multi-session.

STILL OPEN (the genuine multi-session core):
- Step 1 closure: Λ analytic on (0,π). Blocked on antiderivative-of-analytic — Mathlib has AnalyticOnNhd.deriv (forward) but NO converse. Alt route: Λ θ = Im cLiTwoExt(e^{iθ}) needs cLiTwo analyticity extended from ball(1/2,1/2) to the upper unit circle.
- Step 2: base integral analytic in (α,β) (differentiation under the integral).
- Step 3: Mathlib identity theorem (AnalyticOnNhd.eqOn) to glue acute->whole simplex.

## Step-1 closure confirmed multi-session (2026-09-04, grep of main @480d030f937)

Step 1a (Λ' analytic on (0,π)) is LANDED on main (PR #6621, LobachevskyDerivativeAnalytic.lean). The CLOSURE — Λ itself analytic — is confirmed a genuine Mathlib-gap keystone, not a bounded win. Grepped Mathlib v4.24.0 + corpus:
- NO primitive/antiderivative-of-analytic lemma in Mathlib/Analysis (only the forward AnalyticOnNhd.deriv).
- NO Clausen/polylog/dilog analyticity in Mathlib (only Integrals/LogTrigonometric.lean, unrelated).
- NO Cl_2 analyticity in the corpus.

So the two routes both require a real build:
(a) antiderivative-of-analytic: theorem analyticOnNhd_of_deriv_analyticOnNhd — needs the FormalMultilinearSeries termwise antiderivative + radius preservation + HasFPowerSeriesOnBall for the primitive, ~100+ lines. Broadly reusable Mathlib infra (this is the right keystone), but multi-session and error-prone without a live LSP.
(b) Λ θ = Im cLiTwoExt(e^{iθ}): needs cLiTwo analyticity extended from ball(1/2,1/2) (all the corpus proves) to a nbhd of the upper unit circle (θ∈(0,π), e^{iθ}≠1, avoids the [1,∞) cut).

Recommend (a) when a session with a live LSP picks this up: it closes step 1 AND is reusable. Steps 2 (base integral analytic in angles) and 3 (identity theorem) remain after.


## 🛑 STEP 1 IS CLOSED — and my two prior measurements above were BOTH wrong (2026-09-05, session lean-qa-backlog)

**The claim.** `Λ` is real-analytic on `(0, π)`, sorry-free, `[propext, Classical.choice, Quot.sound]`:
- `QOU.Archimedean.analyticAt_Lob {t} (h0 : 0 < t) (hπ : t < π) : AnalyticAt ℝ Lob t`
- `QOU.Archimedean.analyticOnNhd_Lob : AnalyticOnNhd ℝ Lob (Ioo 0 π)`

New file `QOU/Archimedean/LobAnalytic.lean`; lean-direct exit 0 against the real import cone.

**The evidence, and what I got wrong.** The note directly above recommended route (a) — build the ~100-line antiderivative-of-analytic Mathlib filler — because it measured route (b) as "needs cLiTwo analyticity extended from `ball(1/2,1/2)` to a nbhd of the upper unit circle". **That measurement was scoped to the wrong file.** `ComplexDilogBridge.lean` is indeed only local, but the corpus already carries the global statement in a *different* file:

- `QOU.MathlibExt.analyticOnNhd_cLiTwoExt` (`QOU/MathlibExt/ComplexDilogarithmDeriv.lean:248`) — analytic on **all** of `notCut = ℂ ∖ [1,∞)`, proved holomorphic⇒analytic via `DifferentiableOn.analyticOnNhd` + `isOpen_notCut`.
- `QOU.Knot.Kummer.exp_mem_notCut` (`KummerDilogHalf.lean:121`) — the punctured unit circle is inside `notCut`.
- `QOU.Knot.Kummer.im_cLiTwoExt_exp` (`:188`) — `Im cLiTwoExt(e^{iθ}) = Cl₂(θ)` on `(0,2π)`.

So route (b) is a **composition**, ~45 lines, not an extension build: on `(0,π)`, `Λ t = Cl₂(2t)/2 = Im cLiTwoExt(e^{2it})/2`, and the RHS is `Im ∘ cLiTwoExt ∘ exp ∘ (ℝ-linear)`, transported by `AnalyticAt.congr`. Route (a) was never needed.

**Both earlier notes in this bean are superseded**, in opposite ways: the first ("step 1 genuinely multi-session") undercounted what the corpus held; the second ("confirmed Mathlib-gap keystone") repeated that undercount after a grep that searched Mathlib and `ComplexDilogBridge` but not `MathlibExt/ComplexDilogarithmDeriv`. The generalisable lesson is the corpus-grep one: **a clean grep of the file you expect the result in is not evidence the corpus lacks it.**

**Implications.**
- Step 1 is off the critical path. `LobachevskyDerivativeAnalytic.lean` (step 1a, PR #6621) is still a correct standalone `Λ'` statement but is no longer needed for the obtuse route; its header said "step 1 is not closed here … Mathlib has no antiderivative lemma", which is now misleading, and is corrected in the same PR.
- The antiderivative-of-analytic Mathlib filler is **not** built and is no longer recommended as this bean's keystone. It would still be reusable infra if some other item wants it — but nothing here does.
- The obtuse ideal-tetrahedron volume identity is **NOT** proved. Nothing about the volume is asserted.

**Still open — the real remaining core:**
- **Step 2** — the base integral real-analytic in the angles `(α, β)`. Differentiation under the integral sign; this is now the genuine multi-session item.
- **Step 3** — glue acute → whole open simplex with Mathlib's identity theorem (`AnalyticOnNhd.eqOn_of_preconnected_of_eventuallyEq` family). Cheap *given* steps 1+2, but needs the preconnectedness of the open simplex.

**Infra note (durable, cost me ~40 min).** `.lake/build/lib/lean/QOU/MathlibExt/ComplexDilogarithmSlit.olean` in the restored cache was **truncated** (192,512 B; correct is 279,688 B). Symptom: `lean` on anything importing it exits **139 (segfault) with zero output** — not a type error, no diagnostics, and it poisons the whole downstream cone (Kummer, dilog-deriv). Fix: recompile that one olean directly; the entire chain then imports clean.


## 🛑 STEP 2 AS THIS BEAN STATES IT IS MIS-SCOPED — and step 3 is nearly free (2026-09-05, session lean-qa-backlog)

Corpus-grep over all six paths (path 0 `corpus_search` was DOWN — `paper-assistant` MCP `ENOENT` — so every absence below is grep-scoped only, not graph-scoped).

### The finding: the technique named in step 2 does not apply to the object named in step 2

This bean says step 2 is *"the base integral real-analytic in the angles `(α,β)`"*, to be done by differentiation under the integral sign. Measured against the corpus's own formulation, that does not fit:

`QOU/Archimedean/HyperbolicVolumeFubini.lean:275`, `hypVolume_chimney_of_ae_lt`:

```lean
hypVolume (chimney T R)
  = ∫⁻ w in T, ENNReal.ofReal (1 / (2 * (R^2 - w.1^2 - w.2^2)))
```

**The angles enter ONLY through the domain `T = inscribedTriangle R t α β γ`. The integrand is parameter-free, and the value is `ℝ≥0∞`.** Consequences:

- Mathlib's entire parametric-integral family — 7 lemmas in `Analysis/Calculus/ParametricIntegral.lean` plus 4 `intervalIntegral` wrappers — **requires the parameter in the integrand over a fixed measure space.** There is no Mathlib lemma for regularity of `p ↦ μ(T p)`. The nearest shelf is the Jacobian change-of-variables family (`Jacobian.lean:1097`), which is the *technique for moving the parameter into the integrand*, not the result.
- **There is no statable target.** `grep "hypVolume.*toReal|toReal.*hypVolume"` over the whole non-`.lake` corpus returns **zero**. `AnalyticAt ℝ` of an `ℝ≥0∞`-valued function is not a statement. Before step 2 can be *stated*, someone must define `V(α,β) := (hypVolume …).toReal` and prove finiteness across the whole simplex — and the only finiteness input in the tree, `Lob_nonneg_of_lt_pi_div_two` (`OrthoschemeWedgePair.lean:204`), is itself acute-only.
- The corpus's one genuinely *parametric* integral, `integral_orthoscheme` (`OrthoschemeBaseIntegral.lean:260`), has `ψ` in both the limit and the integrand — the right shape — but is `ψ < π/2`-only and **cannot** be the continuation carrier: for `ψ > π/2`, `cos²φ − cos²ψ` changes sign inside the range and the `log` is undefined. The one usable parametric integral is exactly the piece that dies at the obtuse boundary.

### The technique is NOT a Mathlib gap — do not re-measure it as one

The corpus already runs the complete route end to end, sorry-free, in `QOU/MathlibExt/` (bean `qou-clx8`, completed): `hasDerivAt_cLiTwoExt` (`ComplexDilogarithmDeriv.lean:149`, via `intervalIntegral.hasDerivAt_integral_of_dominated_loc_of_deriv_le`) → `differentiableOn_cLiTwoExt` (`:240`) → `analyticOnNhd_cLiTwoExt` (`:248`) → identity theorem (`ComplexDilogarithmUnique.lean:85` `starConvex_zero_notCut` → `:108` `isPreconnected_notCut` → `:124/:151`). Mathlib carries an independent worked template of the identical four-step pattern in `Probability/Moments/ComplexMGF.lean:165,173,180,277`. **The gap is the object's shape, not the machinery.**

### LANDED: the RHS half of steps 2+3 is now closed

`QOU/Archimedean/TetVolAnalytic.lean` (new), lean-direct exit 0, all four `[propext, Classical.choice, Quot.sound]`, no sorry:

- `isOpen_tetSimplex` — was genuinely absent (zero hits under any spelling)
- `isPreconnected_tetSimplex` — one line from the already-proved `convex_tetSimplex`
- `analyticAt_tetVol` / `analyticOnNhd_tetVol` — `analyticOnNhd_Lob` composed onto `tetVol (α,β) = Λ(α)+Λ(β)+Λ(π−α−β)`

This gives `analyticAt_Lob` its first consumers. **It is the identity's RHS only** — `tetVol` is *defined* as the Λ-sum (`volChart`'s own docstring: "A definition, not the geometric volume"). The LHS stays open.

**Duplicate definitions, unresolved:** `tetVol`/`tetSimplex` (`IdealTetrahedronVolumeConcave.lean:75,80`, namespace `QOU.Archimedean`) and `volChart`/`angleSimplex` (`IdealTetrahedronVolumeConcavity.lean:69,76`, namespace `…IdealTetrahedronConcavity`) are **syntactically identical bodies**. I proved for the former. Someone should pick a canonical one; I did not, to keep this change minimal.

### 🛑 A FOURTH acuteness gate this bean's plan does not mention at all

`idealTet_eq_chimney` (`IdealTetEqChimney.lean:169`) — the geometric identification `idealTetrahedron P₁ P₂ P₃ = chimney (inscribedTriangle 1 t α β γ) 1` — carries `hα : α < π/2`, `hβ`, `hγ` at `:171`, and its three face lemmas at `:50,78,130` do the same. Mirrored in `MostowIdealTetVolume.region_eq_chimney`, stated only for acute triples. Also `inscribedTriangle_vertex_incidence` (`OrthoschemeTiling.lean:475`), the anchor pinning the half-plane-intersection *definition* to the triangle with those three vertices, is acute-hypothesised.

**So steps 1+2+3 complete would give "the base integral over `inscribedTriangle` equals the Λ-sum on the whole simplex" and still NOT "the obtuse ideal tetrahedron's volume is the Λ-sum".** The region-equals-chimney bridge is a **set equality**, which analytic continuation cannot touch. That is a second continuation problem the three-step plan does not account for.

### 🛑 RE-SCOPING THE SIGNED-SUBDIVISION FORECLOSURE (line ~482)

This bean states *"The signed-subdivision route is NOT needed and should not be attempted"*. Under the AGENTS.md (a)/(b) rule that is **scope-(b) language with only scope-(a) support**: its whole basis is that Milnor offers analytic continuation as an alternative, which is a fact about Milnor's paper, not a proved invariant about this formalization. **Re-scoped to (a):** *the signed-subdivision argument is not the only available route, and the analytic route avoids its sign convention.* No invariant forbids it.

Measured, the signed route now looks **cheaper**, not dearer: `lob_sum_eq_reflected` (`IdealTetObtuseReduction.lean:82`, sorry-free, PR #6045) already gives the Λ-side signed form with all arguments in `(0,π/2]`; the geometric side needs one further a.e. set identity of exactly the kind `milnorWedges_ae_eq_inscribedTriangle` (`OrthoschemeTiling.lean:402`) already is, reusing `chordHalfplane`, `wedgeAt`, `rotL`, `perp_sign_relation` and the `Measure.addHaar_submodule` null-line trick — all in the tree. Whereas the analytic route needs an object (real-analyticity of a domain-parametrised 2-D `lintegral`) that exists nowhere in Mathlib or the corpus, **and** still leaves gate 4 standing.

Note also that `IdealTetObtuseReduction.lean`'s header is stale — it still names "signed geometry" as the remaining step, written before this bean's analytic-continuation recommendation.

### What Milnor actually says (library path 5)

Milnor 1982 is held (`library/milnor-1982-hyperbolic-geometry-the-first-150-years/sections/sec-000-h-upsl2c-which-is-uniquely-determined-up-to-inne.md`, pp. 10–12; second copy correctly `duplicate_of`-marked). The obtuse handling is **one parenthesis**, verbatim: *"(The case of an obtuse angle can be handled by a similar argument, or by analytic continuation.)"* He does not say in what variable he continues, over what domain, or what the LHS is as an analytic function. **This bean's three-step route is a reconstruction of that parenthesis, not something Milnor states** — and step 2 is where the reconstruction meets the corpus's formulation and does not fit.

**Thurston Ch. 7 is NOT held** — the held copy is Chapters 1–2 (22 sections); `Chapter 7. Computation of volume` appears only as a table-of-contents line in `sec-000-introduction.md:81-82`. Ratcliffe is in neither `library/` nor `uploads/`.

**Two held sources nobody on this arc has read**, both on point: `library/arxiv-1010.5321v3/` (Horváth, *Formulas on hyperbolic volume* — has a Lobachevsky-function section with the same reflection toolkit) and **`library/arxiv-math-0502543v2/` (Rivin, *Continuity of volumes*)**, which proves regularity of hyperbolic polytope volume as a function of the dihedral angles **via the Schläfli differential formula** — a third route to the LHS that this bean does not consider, from a paper the corpus already cites Rivin for elsewhere (`QOU/Knot/RivinConcavity.lean`).

### Recommended next step (my judgement, not a finding)

Do **not** open a session on step 2 as written. Instead **cost the three LHS carriers first** (half a session, versus a multi-session build against an ill-fitting technique):

1. **Change of variables** mapping a fixed reference triangle onto `inscribedTriangle α β γ` (`Jacobian.lean:1097`) — converts domain-dependence into integrand-dependence, after which the `ComplexDilogarithmDeriv` template applies verbatim.
2. **A polar form of the full triangle valid for obtuse** — `milnor_subdivision_obtuse_scope_probe.py` already does exactly this numerically with ray-clipping (obtuse agreement ~1e-17, *better* than the acute ~2e-15), and the corpus has the polar machinery for the orthoscheme (`mem_orthoBase_polar`, `integral_radial`, `OrthoschemePolarReduction.lean:79,139`). Caveat: that probe implements its own ray-clipped triangle, not the Lean `inscribedTriangle`, so it is evidence the *identity* is true, not that the Lean *definition* is the right triangle when obtuse.
3. **Rivin's Schläfli route** from the held `arxiv-math-0502543v2`.

And put the signed route back on the table alongside them, per the re-scoping above.


## The polar route and the signed-subdivision route are the SAME route (2026-09-05, probe 21/21)

The note above lists candidate LHS carriers (1) change of variables, (2) "a polar form of the full triangle valid for obtuse", (3) Rivin/Schläfli — and separately re-scopes the signed-subdivision foreclosure. **(2) and the signed route are one route.** Measured, not argued: [`computations/milnor_polar_signed_equivalence_probe.py`](computations/milnor_polar_signed_equivalence_probe.py), 21/21, mpmath 50 dps, no float64, no witness, anchor-free.

**1. `integral_orthoscheme` IS the polar radial reduction of the base integral — it is not an independent construction.** Integrating the corpus base integrand `1/(2(R²−x²−y²))` radially out to `chordHalfplane R θ ψ`, whose boundary is `r(φ) = R·cos ψ / cos(φ−θ)`, gives in closed form

    −(1/4)·log((cos²φ − cos²ψ)/cos²φ)

which is **exactly** `integral_orthoscheme`'s integrand (`OrthoschemeBaseIntegral.lean:260`). Agreement with numeric quadrature of the Cartesian integrand: ~1e-52 across 12 `(ψ,φ)` samples. And `∫₀^ψ` of it reproduces `Lob ψ / 2` with difference **exactly 0.0** at ψ = π/6, π/4, π/3, 5π/12, 11π/24.

**2. `ψ < π/2` is the chord-offset sign condition, nothing more.** `r(φ) > 0` iff the offset `R·cos ψ > 0` iff `ψ < π/2`. At π/2 the offset is zero — the chord passes through the circumcentre. Past it the offset is negative: the circumcentre is on the **far** side and the radial ray never reaches the chord in the positive direction.

**So `integral_orthoscheme`'s `hψ : ψ < π/2` is not a technical convenience and not wedge-disjointness** (which is what the acute hypothesis is usually attributed to elsewhere in this arc). It is "the circumcentre lies on the inner side of this chord" — the same geometric fact as "the circumcentre leaves the triangle when an angle is obtuse", which is precisely what forces one piece of Milnor's subdivision to enter with a minus sign.

**Consequence.** The polar route cannot be pushed past π/2 without reintroducing exactly the sign the signed route makes explicit. Milnor's minus sign and the polar route's `cos ψ < 0` are one phenomenon in two vocabularies. Effort on either is effort on both — which removes (2) as a *distinct* option and further strengthens the (b)→(a) re-scoping above: the signed route is not a route the analytic one lets you avoid.

Scope-(a) structural observation. **Asserts nothing about the obtuse volume identity**, which remains open.

**Live options are therefore two, not four:** (A) the signed/polar route, whose Λ-side is already proved (`lob_sum_eq_reflected`, all arguments in `(0,π/2]`) and whose geometric side needs one a.e. set identity of the `milnorWedges_ae_eq_inscribedTriangle` kind; (B) change of variables moving the angle dependence into the integrand (Mathlib `Jacobian.lean:1097`), after which the `ComplexDilogarithmDeriv` template applies — but note the integrand is singular at the circle (vertices lie on it), so the dominating function needed for the dominated-convergence step must control that boundary, and corpus finiteness input is acute-only. Rivin/Schläfli (`library/arxiv-math-0502543v2`) remains unread and uncosted.

**Neither closes the case**: `idealTet_eq_chimney`'s `α,β,γ < π/2` is a set equality outside both.


## The obtuse decomposition target is FIXED — and the obvious approach is dead (2026-09-05)

Option (A)'s remaining step was "one a.e. set identity of the `milnorWedges_ae_eq_inscribedTriangle` kind". [`computations/milnor_obtuse_wedge_decomposition_probe.py`](computations/milnor_obtuse_wedge_decomposition_probe.py) fixes *which* identity, and kills the obvious guess first. mpmath 40 dps, no float64, no witness, anchor-free.

### 🛑 `wedgeAt` at an obtuse half-angle is NOT "the wedge with a minus sign"

Its body (`OrthoschemeRotation.lean:153`) is `{w | ⟨w,u⟩ < R cos p ∧ |⟨w,v⟩| < ⟨w,u⟩·tan p}`. For `p > π/2`, `tan p < 0`, so the second conjunct **forces `⟨w,u⟩ < 0`**, and the first is then unbounded below. Measured: members at `|w| = 2, 10, 100, 1000` for `p = 7π/12, 2π/3, 3π/4`, and the near-side point at `|w| = 0.1` correctly excluded.

So the obtuse `wedgeAt` is an **unbounded region opening away from the circumcentre**, not the isoceles triangle its docstring describes. Substituting an obtuse angle into the existing definition gives a *different, infinite set*. **The acute hypotheses throughout the wedge machinery are structural, not technical** — worth knowing before writing Lean rather than after.

### The decomposition that does hold

With `γ` obtuse the circumcentre lies outside, across the `γ`-chord. The replacement for the degenerate `γ`-wedge is the wedge in the **opposite direction** with the **acute** half-angle `π − γ = α + β`, and it is **subtracted**:

    inscribedTriangle R t α β γ
      =ᵐ  ( wedgeAt R (t+2γ+α) α  ∪  wedgeAt R (t+2γ+2α+β) β )
            \  wedgeAt R (t+γ+π) (π−γ)

**Zero mismatches over ~117,000 tested grid points** — 121×121 grids over `[−1.2,1.2]²`, 4 obtuse triples (`γ` = 120°, 120°, 135°, 129°) at 2 rotations, excluding points within 1e-12 of any defining line (the identity is a.e. only).

### Why this makes option (A) bounded

Every half-angle on the right — `α`, `β`, `π−γ` — is **acute** when `γ` is obtuse. That is the *set-level* analogue of `lob_sum_eq_reflected` (`IdealTetObtuseReduction.lean:82`), which already records exactly this on the Λ side and is already proved. So:

- the existing acute wedge machinery (`hypVolume_chimney_wedgeAt`, which needs `ψ < π/2`) applies to **all three pieces unchanged**;
- **the minus sign lives in the set algebra**, not in any new integral;
- no new analytic object is required — which is the contrast with option (B), whose dominating function must still tame the boundary singularity at the circle.

### Remaining work for option (A), now concretely stated

1. The a.e. set identity above, in Lean. Reuses `chordHalfplane`, `wedgeAt`, `rotL`, and the `Measure.addHaar_submodule` null-line trick already used by `milnorWedges_ae_eq_inscribedTriangle`.
2. A measure-subtraction step: `volume (X \ Y) = volume X − volume Y` needs `Y ⊆ X` and `volume Y ≠ ⊤`, so the containment `wedgeAt R (t+γ+π) (π−γ) ⊆ W_α ∪ W_β` has to be proved too (the probe confirms it pointwise but does not prove it).
3. Composition with the acute `hypVolume_chimney_wedgeAt` and `lob_sum_eq_reflected` to land `Λ(α)+Λ(β)+Λ(γ)`.

**Still does not close the case:** `idealTet_eq_chimney`'s `α,β,γ < π/2` (`IdealTetEqChimney.lean:169`) is a set equality outside all of this, and remains untouched.


## Milnor's minus sign is already inside the corpus's algebra — `perp_sign_relation` needs no acuteness (2026-09-05)

Landed in `ObtuseWedgeDegenerate.lean` (sorry-free, lean-direct exit 0, `[propext, Classical.choice, Quot.sound]`): `sin_two_mul_neg_of_obtuse`, `acute_of_obtuse_third`, `perp_coeff_signs_of_obtuse`.

**The finding is about a theorem already on `main`.** `perp_sign_relation` (`OrthoschemeTiling.lean`) carries the single linear relation among the three edge functionals, with coefficients `sin 2α, sin 2β, sin 2γ`. **Verified by reading its signature — its only hypothesis is `hsum : α + β + γ = π`. No acuteness.** So the relation holds *verbatim* in the obtuse case.

What acuteness buys is only the **positivity** of those coefficients, and the theorem's own docstring says so: *"all POSITIVE for acute angles. That positivity is the whole covering argument."*

So **the obtuse case does not need a new relation** — it needs the existing one run against a different sign pattern, now pinned down: exactly one coefficient turns negative, and it is `sin 2γ`. That lone minus is Milnor's.

### The same boundary, three times, always as a sign

This arc has now hit `π/2` in three structurally independent places, and each time it is a **sign flip**, not a difficulty:

| where | what flips at `π/2` |
|---|---|
| `integral_orthoscheme`'s `hψ : ψ < π/2` | the chord offset `R cos ψ` changes sign — circumcentre crosses the chord |
| `wedgeAt` at obtuse `ψ` | `tan ψ < 0`, so the wedge moves to the far side of the apex |
| `perp_sign_relation`'s third coefficient | `sin 2γ < 0` |

They are one phenomenon in three vocabularies. That is why the signed route keeps measuring cheaper: the corpus's machinery is *already* sign-aware; only its *hypotheses* are acute.

### Measure-subtraction hypotheses confirmed, and claim 2 shown non-vacuous

Claim 3 of [`milnor_obtuse_wedge_decomposition_probe.py`](computations/milnor_obtuse_wedge_decomposition_probe.py), over 19,881-point grids × 4 obtuse triples × 2 rotations:

- `W_α ∩ W_β = ∅` — overlap 0 everywhere
- `W_sub ⊆ W_α ∪ W_β` — 0 points outside everywhere
- **`W_sub` NONEMPTY** — 923–1088 points, comparable to `|W_α|`, `|W_β|`

The last one is the check that mattered and I had not run it: claim 2 asserts `T = (W_α ∪ W_β) \ W_sub`, which would pass **vacuously** if `W_sub` were empty, meaning something entirely different (no subtraction, no minus sign). It is not empty.

**A grid artifact recorded so it is not misread as a failure.** At `t = 0` the defining lines are axis-aligned and a symmetric grid lands many points exactly on them; every membership test is a strict `<`, so `|W_α ∪ W_β| − |W_sub|` overshoots `|T|` by ~40. At `t = π/5` essentially nothing is on a line and the counts agree **exactly** (945/945, 690/690, 452/452, 514/514). Only the off-line reading is meaningful — the identity is a.e.

### Remaining for option (A)

1. The a.e. set identity in Lean — model on `milnorWedges_ae_eq_inscribedTriangle` (two containments + `Measure.addHaar_submodule` via `volume_perpLine`). The covering half can now reuse `perp_sign_relation` unchanged with the `+ + −` pattern.
2. `W_sub ⊆ W_α ∪ W_β` and `Disjoint W_α W_β` as Lean lemmas (both measured; `disjoint_wedgeAt_adjacent` needs acute half-angles, and here all of `α`, `β`, `π−γ` are acute, so it should apply directly).
3. Compose with `hypVolume_chimney_wedgeAt` and `lob_sum_eq_reflected`.

**Unchanged:** `idealTet_eq_chimney`'s `α,β,γ < π/2` is a set equality outside all of this and still blocks the volume claim.


## 🛑 CORRECTION — the containment is A.E., not strict (2026-09-05)

Two entries above I wrote *"`W_sub ⊆ W_α ∪ W_β` — 0 points outside everywhere"* as though it were a strict set containment. **It is not, and the probe structurally could not have told me.**

`W_α` and `W_β` meet along the ray `φ = t + 2γ + 2α` — `W_α`'s upper edge *is* `W_β`'s lower edge, which is precisely the adjacency condition `θ₁+ψ₁ = θ₂−ψ₂` that makes `disjoint_wedgeAt_obtuse_pair` go through. Both wedges are **open**, so a point on that ray is in **neither**. Points of `W_sub` lie on it. So `W_sub \ (W_α ∪ W_β)` is nonempty but **null**, and the Lean obligation is

    W_sub \ (W_α ∪ W_β)  ⊆  {w | perp_{t+2γ+2α}(w) = 0}

discharged by `volume_perpLine` — the same shape `milnorWedges_ae_eq_inscribedTriangle` already uses — **not** a strict containment.

**Why the probe missed it, which is the part worth keeping.** The exceptional set is a measure-zero ray, so a rectangular grid misses it except by coincidence. And the coincidence is **undecidable numerically**: on the ray the wedge residual `|⟨w,v⟩| − ⟨w,u⟩·tan ψ` is *exactly* zero in exact arithmetic, so at any working precision it is noise at the precision floor — measured **~1e-62 at 60 dps**, with `W_α`'s coming out negative and `W_β`'s positive purely by rounding. Treating that sign as membership is the NO-FLOAT64 error one level up: agreement at the floor of the arithmetic is not evidence about the mathematics.

**What settled it was the proof, not a measurement** — `disjoint_wedgeAt_obtuse_pair` says the two wedges are disjoint, so no point is in both; on the ray both residuals vanish, so the point is in neither. A proved lemma outranking a probe, in the direction that costs me a claim.

The probe now carries `check_shared_ray()` demonstrating this; claim 3's wording is corrected; the header documents claims 3 and 4 (it previously described only 1 and 2).

### Landed alongside

`disjoint_wedgeAt_obtuse_pair` (sorry-free) — the first cash-out of the `π−γ` reformulation. `disjoint_wedgeAt_adjacent` demands `0 < ψᵢ < π/2` of **both** wedges, which is why it was unavailable to the obtuse case as originally framed; recast with the acute `α`, `β` it applies **verbatim**, adjacency closing by `ring`.

### Remaining for option (A), restated with the correction

1. The a.e. set identity. Covering half can reuse `perp_sign_relation` unchanged with the `+ + −` pattern.
2. The **null-set** obligation above (not a containment), via `volume_perpLine`.
3. Compose with `hypVolume_chimney_wedgeAt` and `lob_sum_eq_reflected`.

**Known unresolved sub-obligation**, found while drafting (2): the chord condition for `W_α` does **not** follow from `wedgeAt_lt_chord_next`/`_prev` applied to `W_sub` — the required `ψ'` comes out negative under both. The needed fact is `⟨w, u_{θ_s − β}⟩ < R cos α` for `w ∈ wedgeAt R θ_s (α+β)`, which is true (the max over the closed wedge is attained at a vertex, giving exactly `R cos α`) but has no existing helper. That is the real remaining work in step A1.


## The chord gap named above is CLOSED — `wedgeAt_lt_chord_shift` (2026-09-05)

Two sorry-free declarations, lean-direct exit 0, `[propext, Classical.choice, Quot.sound]`:

- `wedgeAt_lt_chord_shift` — for `w ∈ wedgeAt R θ ψ` and `0 ≤ δ ≤ ψ`: `⟨w, u_{θ−δ}⟩ < R cos(ψ−δ)`
- `wedgeAt_sub_lt_chord_alpha` — the instance the obtuse case needs

This is exactly the obligation the previous entry recorded as the real remaining work. `wedgeAt_lt_chord_next`/`_prev` place a wedge under its **neighbours'** chords (directions `θ ± ψ ± ψ'`); the obtuse case needs the chord of a **sub-angle of the wedge's own**, at `θ − δ`, and solving `θ − ψ − ψ' = θ − δ` forces `ψ' = δ − ψ ≤ 0` while both existing lemmas require `0 < ψ'`.

**The certificate is the same shape as theirs and simpler.** With `S = ⟨w,u_θ⟩`, `P = ⟨w,v_{θ−ψ}⟩`:

    cos ψ · (R cos(ψ−δ) − ⟨w,u_{θ−δ}⟩) = cos(ψ−δ)·(R cos ψ − S) + P·sin δ

Both right summands non-negative (first strictly): the wedge's own chord bound, and `wedgeAt_lower` times a non-negative sine. **Predicted from the derivation and confirmed by the proof — it closes by `ring`**, no Pythagorean rewrite, which `wedgeAt_lt_chord_next`/`_prev` both need.

The corollary discharges non-vacuity rather than leaving it implicit: `W_sub` has half-angle `π−γ = α+β`, and `t+2γ+α = (t+γ+π)−β`, so it is the shift at `δ = β` with bound `R cos α` — exactly `W_α`'s chord. Both hypotheses free (`α+β < π/2` from `γ` obtuse; `0 ≤ β ≤ α+β` from `α > 0`).

### Step A1 inventory — what is now in hand vs still open

| input | status |
|---|---|
| covering relation `perp_sign_relation` | **in hand** — already acuteness-free on `main`; obtuse `+ + −` pattern proved |
| disjointness of the surviving pair | **in hand** — `disjoint_wedgeAt_obtuse_pair` |
| chord bound for `W_α` | **in hand** — `wedgeAt_sub_lt_chord_alpha` |
| chord bound for `W_β` | *not yet stated* — the mirror instance (`δ = α` on the other side); expected to be the same lemma with signs mirrored, but **untested** |
| the a.e. set identity itself | **open** |
| the null-set obligation via `volume_perpLine` | **open** |
| composition with `hypVolume_chimney_wedgeAt` + `lob_sum_eq_reflected` | **open** |

Nothing here asserts anything about a volume. `idealTet_eq_chimney`'s acuteness remains a set equality outside the whole argument.


## Step A1's covering half is COMPLETE; the identity needs a SECOND null set (2026-09-05)

### Landed

`wedgeAt_lt_chord_shift'` + `wedgeAt_sub_lt_chord_beta` (sorry-free, no linter warnings). The previous entry listed the `W_β` mirror as "expected symmetric but untested". **Derived, not rewritten** — and the reason is worth keeping: the two shifts consume *different* edge bounds, so neither follows from the other. `wedgeAt_lt_chord_shift` uses `wedgeAt_lower`; the mirror uses `wedgeAt_upper`:

    cos ψ · (R cos(ψ−δ) − ⟨w,u_{θ+δ}⟩) = cos(ψ−δ)·(R cos ψ − S) + (−⟨w,v_{θ+ψ}⟩)·sin δ

The symmetry is a symmetry of the **statements**, not a derivation between them.

So the covering half's inputs are all in hand: `perp_sign_relation` (acuteness-free), `disjoint_wedgeAt_obtuse_pair`, and both chord bounds.

### 🛑 The identity is harder than the inventory suggested — a SECOND exceptional set

Working out the `RHS ⊆ T` direction before building it (rather than after):

Take `w ∈ W_α` with `w ∉ W_sub`. Two of the three triangle chords are free — `W_α`'s own is `hw.1`, and `W_β`'s comes from `wedgeAt_lt_chord_next` at `ψ' = β`. **The `γ`-chord is not**, and cannot be: `γ` is obtuse so `R cos γ < 0`, while every existing chord helper requires `ψ' < π/2`.

Worse, `W_α ⊄ chordHalfplane R (t+γ) γ`. A point of `W_α` near the origin has `⟨w,u_{t+γ}⟩ ≈ 0`, which is **not** `< R cos γ < 0`. Such points are in `W_α` but not in `T` — and they are exactly what the subtraction removes, since `W_sub` is the near-origin wedge. Consistent, but it means the `γ`-chord must be extracted *from* `w ∉ W_sub`, not proved independently.

That works, via a two-step route:

1. **Cone containment.** `W_α`'s angular sector `[t+2γ, t+2γ+2α]` sits inside `W_sub`'s `[t+2γ, t+2π]` (the gap is `2β ≥ 0`). So for `w ∈ W_α`, `w ∈ W_sub` **iff** `W_sub`'s chord condition holds.
2. `W_sub`'s chord condition is `⟨w,u_{t+γ+π}⟩ < R cos(π−γ)`, i.e. **exactly** `⟨w,u_{t+γ}⟩ > R cos γ` — the strict complement of the triangle's `γ`-chord. So `w ∉ W_sub` gives `⟨w,u_{t+γ}⟩ ≤ R cos γ`.

**`≤`, not `<`.** The equality case is the `γ`-chord line itself, which is null — so the identity carries a **second** exceptional set beyond the shared ray already recorded: the line `⟨w,u_{t+γ}⟩ = R cos γ`. Both are null, and this matches the acute proof's shape (it spends three `volume_perpLine` null sets), but the earlier inventory listed only one.

**Open sub-step, not yet proved:** the cone containment in (1). Wedge-cone membership is `perp_{θ−ψ} > 0 ∧ perp_{θ+ψ} < 0`; for `w ∈ W_α` the first is immediate (`W_α`'s lower edge *is* `t+2γ`, `W_sub`'s lower edge), but the second needs `perp_t < 0` while `wedgeAt_upper` on `W_α` only supplies `perp_{t+2γ+2α} = perp_{t−2β} < 0`. Those differ by `2β`. There is no corpus lemma for cone-containment of coapical wedges; that is the next concrete thing to build.

### Revised remaining work for A1

| item | status |
|---|---|
| both chord bounds, disjointness, covering relation | **done** |
| coapical cone containment `W_α`, `W_β` ⊆ cone(`W_sub`) | **open** — no corpus precedent, needs the `perp_t < 0` step |
| `γ`-chord from `w ∉ W_sub` (gives `≤`) | reduces to the above |
| the a.e. identity, over **two** null sets (shared ray + `γ`-chord line) | open |
| composition with `hypVolume_chimney_wedgeAt` + `lob_sum_eq_reflected` | open |


## 2026-09-08 — H4-5 obtuse CLOSED at the triangle level (PR #7163)

Three sorry-free landings in `ObtuseTiling.lean`, all `lean -DautoImplicit=false
-s 65536` exit 0:

1. **`inscribedTriangle_subset_obtuseWedges_of_ne`** — the covering.
2. **`obtuseWedges_ae_eq_inscribedTriangle`** — the tiling,
   `T =ᵐ (W_α ∪ W_β) \ W_sub`.
3. **`hypVolume_chimney_inscribedTriangle_obtuse`** —
   `Vol(chimney T R) = Λ(α) + Λ(β) + Λ(γ)` for `π/2 < γ`.

### The finding that mattered: "a similar argument" is not available

Milnor's parenthesis offers two routes and this bean recorded both. The
**"similar argument"** route turns out to be blocked in a way that is worth
recording, because it looks like an adaptation problem and is not one.

The acute covering runs entirely on `perp_sign_relation`, whose three
coefficients `sin 2α, sin 2β, sin 2γ` are positive, so two of eight sign
patterns are impossible and each of the six survivors is a sector. With `γ`
obtuse, `sin 2γ < 0` and the relation forbids only two patterns — **four** of
the six survivors put the point in neither remaining wedge. The *fact* the
acute argument establishes is insufficient; no rearrangement of it closes the
obtuse covering.

What replaces it is stronger and makes the sign relation unnecessary: `T` lies
in the cone spanned by `O→V₁` and `O→V₂`, i.e. `perp_t < 0` and
`perp_{t+2γ} > 0` on the whole triangle. Each is a **two-term certificate**
against the two chords meeting at that vertex, obtained by eliminating
`R − ⟨w,u⟩` between the two chord slacks:

    perp_t · sin α      = cos γ·(β-chord slack) − cos β·(γ-chord slack)
    perp_{t+2γ} · sin β = cos α·(γ-chord slack) − cos γ·(α-chord slack)

`R` cancels; both hold for ANY triple summing to π, acute or not. Only the sign
reading uses `cos γ < 0` — in the acute case the two terms have opposite signs
and the conclusion is false, which is the honest statement of what obtuseness
buys. The same two identities read BACKWARDS give
`wedgeAt_sub_subset_alphaBeta_of_ne`, i.e. that `W_sub` really is inside the
union it is subtracted from (without which the set difference would be
arithmetically smaller than Milnor's signed sum).

### Two things better than the acute case, one worse

- The covering needs **one** edge functional nonzero, not three.
- The subtraction never happens in `ℝ≥0∞`: reading the partition as
  `W_α ∪ W_β =ᵐ T ⊔ W_sub` makes additivity a statement about sums, and `Vol(T)`
  falls out by cancelling the finite `Vol(W_sub)`.
- Worse: the `RHS \ T` direction needs an **affine** null line (the γ-chord),
  which `volume_perpLine` cannot reach — hence `volume_chordLine`.

### What is still open — and it is now a SINGLE gate

`IdealTetEqChimney.idealTet_eq_chimney` carries `α, β, γ < π/2` and is a **set
equality**. Neither the analytic-continuation route (which is why the three-step
plan cannot finish on its own) nor anything in this tranche supplies it. This
is now the only thing between the corpus and the obtuse case of Milnor's
identity, and it is a *geometry* problem, not an analysis one.

Also corrected on main: `lob_sum_eq_reflected`'s docstring said the geometric
subdivision "stays open". It no longer does; that lemma is now what the volume
theorem spends.

### Superseded within this bean

The **analytic-continuation** route (steps 1-3: `analyticOnNhd_Lob`,
`analyticOnNhd_tetVol`, identity theorem) is NOT what closed this. Those
results stand and are on main, but they address the identity's RHS and a
hypothetical LHS carrier that does not exist — see `TetVolAnalytic.lean`'s
scope note. The obtuse case was closed by direct geometry instead. Recording
this so a later reader does not credit the continuation route with the result.


## 2026-09-08 (later) — H4-5 CLOSED on the ideal tetrahedron; the "fourth gate" did not exist

`ObtuseTiling.idealTetVolume_of_vertices_obtuse` — `Vol(idealTetrahedron P₁P₂P₃)
= Λ(α)+Λ(β)+Λ(γ)` for `π/2 < γ`, on the vertex-defined region, sorry-free.

### Retracting my own claim from earlier today

The entry above, this session's two prior commits, and four durable scope notes
all said the same thing:

> the identification of the region with the chimney
> (`IdealTetEqChimney.idealTet_eq_chimney`) still carries `α, β, γ < π/2` and is
> a **set equality**, which analytic continuation cannot supply — so it is now
> the single remaining gate, and it is a geometry problem.

**False, and cheaply falsifiable.** Those hypotheses were carried and never used.
Acuteness enters that proof at exactly one shape — `Real.sin_pos_of_pos_of_lt_pi
hX0 (by linarith)`, whose side goal is `X < π` — and `α+β+γ = π` with the other
two positive already discharges it. The strictness gap is `cos ψ′ − cos(2ψ+ψ′) =
2 sin(ψ+ψ′)·sin ψ`, positive wherever both sines are, i.e. everywhere on the open
simplex. Deleting `hα hβ hγ` from `inscribedTriangle_vertex_incidence`,
`face1/2/3` and `idealTet_eq_chimney` and fixing the three `MostowIdealTetVolume`
call sites is the entire change.

**Why the corpus-grep discipline could not catch it.** The claim was true of the
*signature* and false of the *proof*. Every check I ran — grep the topic, grep the
claim shape, read the docstring — confirmed the hypotheses were present. Only
reading the proof body settles whether they are consumed, and I asserted the gate
twice before doing that.

**What was NOT the closer.** The analytic-continuation route (steps 1-3:
`analyticOnNhd_Lob`, `analyticOnNhd_tetVol`, the identity theorem's topological
hypotheses) did not close this and is marked as not closing it in
`TetVolAnalytic.lean` and `IdealTetObtuseReduction.lean`. Those results stand;
their left half — a real-valued carrier for the LHS — is still open and is now
moot for this case. Signed subdivision closed it, which is the route this bean
had *foreclosed* early on and then re-scoped from (b) to (a). The re-scoping is
what made it available; had the (b) claim stood, this would still be open.

### Coverage

Acute (`idealTetVolume_of_vertices`) + obtuse (new) cover every admissible triple
**except `γ = π/2` exactly**, where `W_sub = wedgeAt R (t+γ+π) (π−γ)` degenerates
to a half-plane and the `ψ < π/2` wedge machinery fails on both sides. That is a
measure-zero slice of the simplex and a genuinely separate limiting argument; it
is not claimed.

### Residual, and it is shared with the acute case

Both rest on the same single cited totally-geodesic / normalized-position
identification (`geodesicPlaneThrough`, File A1 — a definition with a citation,
not an axiom or `sorry`). Nothing new is assumed by the obtuse half.

**Not closing this bean.** Whether the `γ = π/2` slice and the shared A1 citation
leave H4-5 "done" is an owner call, and per AGENTS.md rule 13a a bean is not
completed because the recording of its state is complete.


## 2026-09-11 — the `γ = π/2` slice is closed; the whole simplex is covered

`idealTetVolume_of_vertices_right` plus its chimney and tiling companions
(`ObtuseTiling.lean`, sorry-free). With the acute theorem on `main` and the
obtuse one from 2026-09-08, every admissible triple now falls in exactly one of
three cases — **acute** (`α, β, γ < π/2`), **obtuse** (`π/2 < γ`),
**right-angled** (`γ = π/2`).

### Retracting the reason I left it out

The 2026-09-08 entry says the acute and obtuse theorems "cover every admissible
triple **except `γ = π/2` exactly**, where `W_sub` degenerates to a half-plane
and the `ψ < π/2` wedge machinery fails on both sides. That slice is not
claimed." Two things wrong with that, independently:

1. **`W_sub` does not degenerate to a half-plane — it degenerates to the empty
   set.** `wedgeAt_pi_div_two_eq_empty`: Lean's `tan (π/2) = 0` makes the angular
   condition `|perp| < 0`. That is not a junk-value artifact; it is right. The
   chord bound `⟨w,u⟩ < R cos(π−γ) = 0` cuts away precisely the half-plane the
   half-turn opening would sweep.
2. **It is therefore the EASIEST of the three, not the hard leftover.** Nothing
   to subtract, and — unlike the obtuse case — no `γ`-chord null set either.

Both are the same error twice: reasoning about a degeneration from its
*description* rather than evaluating it. Structurally identical to the "fourth
acuteness gate" retracted the same week, which reasoned about a hypothesis from
its *signature* rather than reading the proof. Third instance of this class in
this bean.

### What carries it

The two certificates again, a third use. At `cos γ = 0` each collapses to one
term, and the `γ`-chord comes out **strict**:

    perp_{t+2γ}·sin β = cos α·(γ-chord slack)     W_α's lower edge ⟹ slack > 0
    perp_t·sin α      = −cos β·(γ-chord slack)    W_β's upper edge ⟹ slack > 0

In the obtuse case that chord is extracted from `w ∉ W_sub`
(`gamma_chord_of_notMem_sub`) and concludes `≤`, which is exactly what forces
`volume_chordLine`. Here `W_sub` is empty, so that hypothesis carries no
information and the certificates supply the chord directly.

Also generalised: the two cone bounds and the covering now take `π/2 ≤ γ` (they
only ever needed `cos γ ≤ 0`), with `α, β < π/2` derived inline since
`acute_of_obtuse_third`'s hypothesis is strict.

### Residual — unchanged, and it is the only one left

All three cases rest on the same single cited totally-geodesic /
normalized-position identification (`geodesicPlaneThrough`, File A1 — a
definition with a citation, not an axiom or `sorry`). The obtuse and
right-angled halves assume nothing the acute one does not.

**Still not closing this bean.** Whether that shared citation leaves H4-5 "done"
is an owner call, not mine — rule 13a. What has changed since the last entry is
that the coverage caveat I attached to that question is gone.


## 2026-09-11 (later) — the identity is UNCONDITIONAL

`ObtuseTiling.idealTetVolume_of_vertices_unconditional`, sorry-free:

    Vol(idealTetrahedron P₁ P₂ P₃) = Λ(α) + Λ(β) + Λ(γ)

for **every** positive triple summing to `π`. No acuteness, no distinguished
angle, no case hypothesis. This is H4-5's actual target rather than a
case-parametrised family, and it is the first statement in this arc that a reader
can cite without checking which branch they are in.

### A gap in my own headline claim, two hours old

The entry above says "the whole angle simplex is covered: acute, obtuse,
right-angled — every admissible triple falls in exactly one". All three theorems
are stated with **`γ`** as the distinguished angle. A triple whose non-acute
angle is `α` or `β` satisfies **none of them as written**. The claim was really
about a relabelling step, and that step had not been taken.

That is the third instance in this bean of one shape: something true of the parts
asserted of the whole without checking the join —

1. a hypothesis inherited down a chain, assumed to be needed (the "fourth
   acuteness gate");
2. a degeneration reasoned about from its description rather than evaluated
   (`W_sub` "becomes a half-plane", when it becomes `∅`);
3. three cases assumed to compose into a cover, when composing them needs a
   relabelling lemma nobody had proved.

### What closes it

The relabel is **exact**, not approximate. With `α+β+γ = π`, sending
`(α,β,γ) ↦ (β,γ,α)` and `t ↦ t+2γ` names the *same three circle points* — the
third lands on `t + 2π`. So it is literally the same region, given that
`idealTetrahedron` ignores vertex order, which reduces to one observation:

    verticalHalfSpaceThrough b c i = {p | 0 < sarea b c i * sarea b c (p 0, p 1)}

is a product of two signed areas **sharing the edge `b c`**, so swapping the
edge's endpoints negates both factors and changes nothing. Hence
`verticalHalfSpaceThrough_swap` → `idealTetrahedron_cyclic`. `Λ(α)+Λ(β)+Λ(γ)` is
symmetric outright.

New: `verticalHalfSpaceThrough_swap`, `idealTetrahedron_cyclic`,
`circlePoint_add_two_pi`, `idealTetVolume_of_vertices_nonacute` (obtuse + right
in one, `π/2 ≤ γ`), and the unconditional theorem.

`at_most_one_obtuse` turned out not to be needed — the split is by cases rather
than by exclusion, so a triple with two non-acute angles lands in a branch whose
hypotheses `linarith` refutes on its own.

### Residual — unchanged, and now genuinely the only one

The single cited totally-geodesic / normalized-position identification
(`geodesicPlaneThrough`, File A1 — a definition with a citation, not an axiom or
`sorry`). The acute theorem already rested on it; everything added in this arc
assumes nothing further.

**Still not closing this bean** (rule 13a): whether that citation leaves H4-5
"done" is an owner call. What has changed is that there is no longer any
coverage caveat attached to that question.


## MERGED to main — PR #7163 (2026-09-12), rebase-merge, 13 commits

`ac105d50e39`. All 13 commits verified on `main` by `git cherry`, and both the
headline declaration and the final binder fix confirmed present in the merged
tree.

**What landed.** H4-5 (obtuse) AND the right-angled slice, plus the
cyclic-relabel lemma that makes the coverage claim true rather than asserted:

- `obtuseWedges_ae_eq_inscribedTriangle` — the signed tiling
  `T =ᵐ (W_α ∪ W_β) \ W_sub`, the a.e. set identity `IdealTetObtuseReduction`'s
  header had anticipated.
- `hypVolume_chimney_inscribedTriangle_obtuse` / `_right`, and
  `idealTetVolume_of_vertices_obtuse` / `_right` on the vertex-defined region.
- `idealTetVolume_of_vertices_unconditional` — every positive triple summing to
  π, by `rcases le_or_gt (π/2) γ / α / β` with cyclic relabelling.

All sorry-free. `#print axioms` on all six headline declarations returns
`[propext, Classical.choice, Quot.sound]`.

**The route.** Signed subdivision, not analytic continuation. The mechanism is a
two-term certificate got by eliminating `R − ⟨w,u⟩` between the two chord slacks
at a vertex; `R` cancels and the identity holds for ANY triple summing to π.
Only reading off its SIGN uses `cos γ ≤ 0`. Read backwards it gives the
subtracted-wedge containment; at `cos γ = 0` it gives the right-angled chord
strictly.

**Three retractions of my own claims, all in the PR body.** (1) The "fourth
acuteness gate" in `idealTet_eq_chimney` did not exist — the three hypotheses
were carried and never used; dropping them carries the whole vertex-incidence →
face → region chain to obtuse triangles. (2) `W_sub` at `γ = π/2` degenerates to
the EMPTY SET, not a half-plane, making that the easiest case rather than the
hard leftover. (3) "The whole simplex is covered" needed a lemma nobody had
proved, since all three case theorems distinguish `γ`.

Findings 1 and 2 are one error class twice: reasoning about a thing from its
signature or description instead of evaluating it.

**STAYS in-progress, per AGENTS.md rule 13a.** The mathematics of H4-5 is
closed, but all three cases rest on the same single cited totally-geodesic /
normalized-position identification (`geodesicPlaneThrough`, File A1 — a
definition with a citation, not an axiom or `sorry`). Whether that shared
citation leaves H4-5 "done" is an owner call, not an agent one. The obtuse and
right-angled halves assume nothing the acute one does not; the coverage caveat
that used to sit beside that question is gone.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-12 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Round 81 Execution Note (2026-11-17T08:44:47Z)

- **Status**: `in-progress` (PR awaiting merge; no unilateral closure).
- **PR**: [`litlfred/qou#8288`](https://github.com/litlfred/qou/pull/8288) (`feat/qou-b9cj-6poy-q64u-regz-w3eg-xq3f`, HEAD `3f9d9bb7e2af7c3353cc2779b429d84aae572cda`).
- **Lean Module**: `folio/quantum-observable-universe/lean/QOU/QBeta/NeumannZagierDeterminantAndVassilievMilnorBrick.lean` (wired into `QOU.lean`, compiled with Lean 4.24.0, 0 findings across all 7 static Lean audits).
- **80-dps Probe & Witness**: `computations/probes/neumann_zagier_determinant_and_vassiliev_milnor_brick_probe.py` & `computations/probes/neumann-zagier-determinant-and-vassiliev-milnor-brick.witness.json` (`scriptCommitSha = b4b438fbfa2d06efdb0e7b096ec45a7a03973e2b`, `scriptHash = cf7e93178098`, `outputHash = c7210b5eb72906d3c61c7e19a0c46a0a3457be0f703d99c7dd7475108da381b1`).
