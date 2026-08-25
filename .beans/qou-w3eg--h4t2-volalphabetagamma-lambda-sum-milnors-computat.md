---
# qou-w3eg
title: 'H4/T2: Vol(alpha,beta,gamma) = Lambda-sum — Milnor''s computation, decomposed into H4-1..H4-5'
status: in-progress
type: task
priority: medium
created_at: 2026-08-08T17:40:00Z
updated_at: 2026-08-08T17:40:00Z
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
> [`OrthoschemeWedgePair.lean`](../content/quantum-observable-universe/lean/QOU/Archimedean/OrthoschemeWedgePair.lean)
> and
> [`OrthoschemeRotation.lean`](../content/quantum-observable-universe/lean/QOU/Archimedean/OrthoschemeRotation.lean).
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
> [`OrthoschemeTiling.lean`](../content/quantum-observable-universe/lean/QOU/Archimedean/OrthoschemeTiling.lean).
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
