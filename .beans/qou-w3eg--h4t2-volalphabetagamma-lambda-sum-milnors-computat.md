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
Needs H3 (the region) and the product-measure Fubini for `withDensity`. The
`Mathlib.MeasureTheory.Constructions.Prod.*` modules were **absent from the
restored olean cache** (2026-08-08) — re-seed or fetch before starting, or this
tier stalls on a missing import rather than on mathematics.

**H4-3 — the base integral over one triangle.** Reduce
`∫∫_T dA/(2(R²−d²))` over the Euclidean triangle inscribed in the circle of
radius `R`. Milnor's route: cut `T` at the circumcentre into 6 right triangles
and evaluate each. This is where `−log|2 sin|` first appears, i.e. where `Λ'`
(T1, already proved) enters.

**H4-4 — the orthoscheme value `= ½Λ(θ)`.** The analytic core: each of the 6
pieces integrates to half a Lobachevsky value. Uses T1's
`hasDerivAt_Lob : Λ' = −log(2 sin t)` as the antiderivative — already in the
tree, which is the one piece of luck here.

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
