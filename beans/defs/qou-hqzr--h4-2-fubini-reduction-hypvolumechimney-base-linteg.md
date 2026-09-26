---
# qou-hqzr
title: 'H4-2: Fubini reduction — hypVolume(chimney) = base lintegral of the fibre mass'
status: completed
type: task
parent: qou-w3eg
created_at: 2026-08-08T21:35:28Z
updated_at: 2026-08-08T21:55:00Z
---

**DONE, sorry-free.** `qou-w3eg` H4-2 / `qou-5gai` H4-2.

    hypVolume (chimney T R)  =  ∫∫_T dA / (2(R² − x² − y²))

File: `content/quantum-observable-universe/lean/QOU/Archimedean/HyperbolicVolumeFubini.lean`,
registered in `QOU.lean`. 7 declarations, `#print axioms` =
`[propext, Classical.choice, Quot.sound]` on all of them, 0 `sorry`.

## What it cost — the bean's two predictions, both confirmed

`qou-w3eg` predicted exactly two costs for this tier and named them before the
work. Both were real, and neither was larger than predicted:

1. **The Pi/Prod split.** H1's carrier is `Fin 3 → ℝ` (forced: only Pi carries
   `IsAddHaarMeasure`, which H2's dilation invariance needs), while Tonelli is
   stated for a product. `splitEquiv : (Fin 3 → ℝ) ≃ᵐ ℝ × (ℝ × ℝ)` bridges it,
   height split off FIRST so `lintegral_prod_symm` leaves the base integral
   outermost — the order Milnor's computation uses. Measure-preserving from
   `volume_preserving_piFinSuccAbove` + `volume_preserving_finTwoArrow`. The
   three coordinate lemmas are all `rfl`. **One definition, paid once**; the
   carrier-choice worry recorded in `qou-5gai` is now closed on both sides.
2. **The `lintegral`/Bochner bridge.** `hypVolume` is a `withDensity` measure so
   its integrals are `ℝ≥0∞`-valued `∫⁻`; H4-1 is a Bochner `∫`. `fibreMass_eq`
   reconciles them via `ofReal_integral_eq_lintegral_ofReal`, which needs
   genuine integrability (`integrableOn_Ioi_rpow_of_lt`, valid exactly because
   `−3 < −1`) — so H4-1's *convergence* is what licenses the bridge, not a
   formality.

## Two findings that were not predicted

**`fibreMass_eq_top` — the disk hypothesis is the exact finiteness boundary.**
Proved, not assumed: on or outside the circle `Real.sqrt` of a non-positive
number is `0`, the chimney floor degenerates to `z > 0`, and the fibre carries
**infinite** mass. (Tail bound at `ε = 1/(1+r)`, giving `1/(2ε²) = (1+r)²/2 ≥ r`
for every `r : ℝ≥0`.)

**That converse then dictates the shape of the usable statement — and a
pointwise hypothesis would have been WRONG for H4-3.** Milnor's base triangle is
*inscribed* in the circle, so its three **vertices lie exactly ON** it, where the
fibre mass is `⊤`. A pointwise `∀ w ∈ T, w.1² + w.2² < R²` therefore excludes the
closed triangle — precisely the case H4-3 needs. The main statement is hence
a.e.:

| declaration | hypothesis |
|---|---|
| `hypVolume_chimney` | **none** — both sides may be `⊤` |
| `hypVolume_chimney_of_ae_lt` | `∀ᵐ w ∂(volume.restrict T)` — **the one H4-3 consumes** |
| `hypVolume_chimney_of_subset_disk` | pointwise, open disk — corollary |

The vertices are a null set, so the a.e. form is both sufficient and honest.
**H4-3 must use `hypVolume_chimney_of_ae_lt`**, not the pointwise corollary.

## Scope — unchanged from H3, and deliberately

No triangle, no angles, no tetrahedron, **no `Λ`**. `chimney` is over an
arbitrary base; nothing here says a chimney *is* an ideal tetrahedron (that is
Milnor's geometric identification, needing hyperbolic structure Mathlib lacks).
`Λ` first appears in H4-3/H4-4, not here.

## Next

**H4-3** — evaluate `∫∫_T dA/(2(R²−x²−y²))` over a triangle inscribed in the
circle, subdividing at the circumcentre into 6 right triangles. This is where
`−log|2 sin|` (= `Λ'`, T1, already proved) enters, and where the **obtuse case**
finally bites: Milnor states the subdivision for *"if all three angles are
acute"*, and with the circumcentre outside the triangle the piece enters with a
**minus** sign. Still the flagged place to go wrong; still wanting Ratcliffe
§10.4 or full-text Thurston Ch. 7 for the sign convention.

## Links

* `qou-w3eg` — the H4 decomposition this is step 2 of
* `qou-5gai` — the H1–H5 EPIC
* `qou-idvt` T2, `qou-7y3g`, `qou-krvm` (iv) — consumers, all still blocked
  (H4-3…H4-5 open). **Nothing wired**; no mass, binding, or substrate claim.
