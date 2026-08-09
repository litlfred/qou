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

**1. Milnor 1982 full text is in `uploads/milnor-1982-hyperbolic-geometry-the-first-150-years.pdf`** — the Appendix
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
Source extracted from `uploads/afp-Poincare_Disc-current.tar.gz`: 11 theory
files, **11 289 lines**, and **0 hits** for `volume` / `area` / `lebesgue` /
`integral`. Its sections are h-lines, h-distance, h-betweenness, h-circles,
h-perpendicularity, Tarski axioms — a **synthetic** development in the
**2-dimensional disc**, not Riemannian and not `H³`.

> **Consequence, and it is the important one: there is NO prior art to port.**
> Hyperbolic *volume* appears to be unformalized in every proof assistant, not
> just Mathlib. H4 is new formalization, not a translation exercise. This
> raises confidence in the multi-week estimate rather than lowering it.

**4. `uploads/1010.5321v3.pdf` = Horváth, *Formulas on hyperbolic volume*** —
orthoscheme volume via the Lobachevsky integral, explicitly avoiding the
Schläfli differential formula, with edge-lengths as parameters. Worth reading
for H4-4 if Milnor's angle-parameter route proves awkward in Lean; not yet read
past the abstract.

**5. Neumann–Zagier is `uploads/neumann-zagier-1985-volumes-of-hyperbolic-three-manifolds-copy-b.pdf`** — the
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
