---
# qou-hq3m
title: 'Mathlib infra: the volume of a hyperbolic 3-manifold as a quotient of H^3'
status: completed
type: task
priority: high
parent: qou-8mtd
tags:
    - hyperbolic-volume
    - mathlib-gap
    - lean
created_at: 2026-08-29T18:40:00Z
updated_at: 2026-08-29T18:40:00Z
---

Child of `qou-8mtd`, taking its open half: "hyperbolic 3-manifolds in Mathlib,
Mostow rigidity, Thurston hyperbolisation — add needed Mathlib infra."

## What the corpus ALREADY has (measured, not assumed)

`qou-8mtd`'s framing — and the header I wrote for `ManifoldVolumeBridge` — says
Mathlib has no hyperbolic 3-manifolds. True of Mathlib. **Badly misleading about
this corpus**, which carries a substantial `QOU/Archimedean/` hyperbolic layer:

| module | state |
|---|---|
| `HyperbolicVolumeMeasure` | `upperHalfSpace`, `hypDensity = 1/z³`, `hypVolume`, **0 sorries** |
| `IdealTetrahedronRegion` | chimney regions, **0 sorries** |
| `TotallyGeodesicFaces` | vertical planes + hemispheres totally geodesic, **0 sorries** |
| `HyperbolicMetric` | `dH` path metric, `IsDHIsometry`, 3 sorries |
| `MostowIdealTetVolume` | 7 sorries |
| `IdealTriangulation` | shape triple `param_prod = -1`, `param_im_pos`, `volume_rotate` — all proved |

So the ideal-tetrahedron and volume-density sides are largely DONE. Anyone
starting here from `qou-8mtd`'s wording would rebuild a lot of it.

## The actual gap

There is a measure on H³ and there are individual isometries. There is **no
group acting, no discrete subgroup, and no quotient.** That is the whole
distance between "we have H³" and "we have a hyperbolic 3-manifold":

    H³  --(Γ acts, discrete, free)-->  H³/Γ  =  the manifold

and it is why `MostowRigidity.volume` has to be an *entered literal* and why
`HyperbolicVolumeBridge.vol` has to be an assumed field. Neither has anything to
attach to.

## The target, and why it is provable rather than assumable

Mathlib has `MeasureTheory.IsAddFundamentalDomain.measure_eq`: two fundamental
domains for a countable group acting by measure-preserving maps have equal
measure. Its hypotheses are exactly `[AddGroup G] [AddAction G α]
[MeasurableVAdd G α] [VAddInvariantMeasure G α μ] [Countable G]`.

And the corpus already proves the hard input: `hypVolume_add_left` says
`hypVolume ((v + ·) ⁻¹' s) = hypVolume s` whenever `v 2 = 0` — which IS the
`VAddInvariantMeasure` condition for horizontal translations.

So the volume of the quotient can be **derived** rather than posited:

1. `horizontal : AddSubgroup (Fin 3 → ℝ)` — the zero-height vectors.
2. `VAddInvariantMeasure Γ (Fin 3 → ℝ) hypVolume` for `Γ ≤ horizontal`,
   proved from `hypVolume_add_left`. **This is the content.**
3. The quotient volume, well-defined: any two fundamental domains agree.

That gives "the volume of a hyperbolic 3-manifold" an actual referent in at
least one genuine case, instead of a class field.

## What this will NOT do

Mostow rigidity and Thurston hyperbolisation stay open, and no route here
touches them. A horizontal-translation quotient is a real hyperbolic 3-manifold
but a very special one (a cusp); it is not a knot complement, and nothing here
makes `Vol(4_1)` computable. The point is to replace *assumed* volume with
*derived* volume in one honest case, and to leave the general bridge conditional
exactly as it is.


---

## DONE 2026-08-29 — landed, sorry-free

`QOU/Archimedean/HyperbolicQuotient.lean`, 19 declarations, all
`[propext, Classical.choice, Quot.sound]`, zero `sorryAx`, all pinned in the axiom
guard and verified against freshly-rebuilt oleans.

The load-bearing result is `vaddInvariantMeasure`: a horizontal translation group
**preserves hyperbolic volume**, discharged by the corpus's own `hypVolume_add_left`
rather than assumed. That is what makes the quotient volume *derived*. Alongside it:
the action is on H³ and not merely on ℝ³ (`vadd_mem_upperHalfSpace`), it is **free**
(`eq_zero_of_vadd_eq`) which is what makes the quotient a manifold rather than an
orbifold, and the quotient volume is **well defined**
(`hypVolume_eq_of_isAddFundamentalDomain`).

**A fundamental domain is exhibited** (`isAddFundamentalDomain_slab`), deliberately.
§4 is a statement about fundamental domains and would be worth nothing over an empty
hypothesis — the exact trap the sibling `ManifoldVolumeBridge` fell into, where the
class admitted `Realises := fun _ _ => False` and every theorem held vacuously.
Exhibiting the model is the only way to know. The unit slab is proved to be one, with
`Int.floor_eq_iff` supplying the unique representative.

### Two overclaims of my own, caught before commit

1. **`H³/ℤ` is NOT a cusp.** A cusp cross-section is a torus and needs a **rank-2**
   lattice; the exhibited one is rank 1. `isHorizontal_closure` is therefore stated for
   a general generating set, so a rank-2 group satisfies §1–§4 — but only rank 1 gets a
   fundamental domain here.
2. **The volume is not computed.** §4/§6 establish it is WELL DEFINED (every
   fundamental domain gives the same element of `ℝ≥0∞`), which is weaker than knowing
   which element. `∫ dz/z³` diverges at `z → 0` so the slab is *expected* to have
   volume `⊤` — **not proved**.

### Still open (follow-ups, not blockers)

- `hypVolume slab = ⊤` — the divergence, unproved.
- A rank-2 fundamental domain, giving an actual cusp.
- Finite-volume quotients, which need truncation and are where a *number* would appear.

Mostow rigidity and Thurston hyperbolisation are untouched, and nothing here is a step
toward either.

---

## 2026-08-29 — TWO CORRECTIONS to my own claims, both caught by the author

Both appear in PR #6056's body and in my end-of-turn reports, so they need naming here.

### 1. "Nothing here makes `Vol(4₁)` computable" — WRONG

Measured on main. The corpus has the figure-eight volume **exactly, and sorry-free**:

| declaration | file | state |
|---|---|---|
| `VOL_4_1 := 2 * Cl_2 (π/3)` | `Knot/FigureEightVolume.lean:88` | exact constant |
| `figureEightTriangulation : IdealTriangulation 2` | `Knot/FigureEightTriangulation.lean:97` | 2 regular ideal tets |
| `figureEightTriangulation_volume` | same, **0 sorries** | `= VOL_4_1`, proved |
| `edge_zero` / `edge_one` | same | gluing equations, proved |
| `Cl_2_pi_div_three_pos` | `Knot/Clausen.lean:490` | `0 < Cl₂(π/3)` |

So the 4₁ analogue of `FiveTwoVolumeConstant` already existed, and the constant is a
closed form, not a decimal.

**What I should have said**, and it is much narrower: nothing connects the *knot
complement as a topological object* to `figureEightTriangulation`. The proved statement
is "this triangulation of two regular ideal tetrahedra has volume `2·Cl₂(π/3)`" — not
"the complement `S³ ∖ 4₁` has that volume". That step is Thurston. The number was never
the gap; the identification was.

Note also there is **no knot 4₂** — 4₁ is the only 4-crossing knot. The knot with the
full exact treatment in `FiveTwoVolumeConstant.lean` is **5₂**.

### 2. "There is no group acting" — TOO BROAD

Measured: **8 files** carry `MulAction`/`AddAction` (`BraidKnot/Specht`,
`SpechtIrreducible`, `HeckeBoundedSeminormalWeight`, `QBeta/MarkovTraceQuotient`,
`Substrate/ColorAntisymmetric`, `BraidsAndKnots/ClosureComponentsSignInvariant`,
`BringsSurface/OctonionInvariantObstruction`, `MathlibExt/RegularHom`), and
`MobiusEnergy.lean` discusses a `PSL(2,ℂ)` Möbius action.

The claim is true only **scoped to ℍ³**: of the 10 files touching
`upperHalfSpace`/`upperH`, exactly one carries an action, and it is
`Archimedean/HyperbolicQuotient.lean` — the one added by this bean. Stated without that
scope it reads as "this corpus has no group actions", which is false and would mislead
anyone auditing the representation-theory side.

### The lesson worth keeping

Both errors have the same shape as the `ManifoldVolumeBridge` vacuity trap they sit
beside: **a claim about absence that was never measured.** "Mathlib has no hyperbolic
3-manifolds" is a fact about Mathlib that I carried across into a claim about this
corpus without running the corpus-grep, which is the very checklist AGENTS.md gates
"open" declarations on. The checklist is not only for declaring items open — it applies
to any assertion that the corpus *lacks* something.
