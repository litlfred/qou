# Uniqueness theorems backlog — pre-publication

> Queued per owner direction (2026-05-29, #1422 thread): every "canonical X"
> claim in the QOU framework must be backed by a *proved uniqueness theorem*
> before publication / production. This document is the tracked backlog.

The QOU mass derivation chain (see [`canonical-derivation-cheat-sheet.md`](canonical-derivation-cheat-sheet.md))
asserts that several constructions are "canonical" — meaning *uniquely
determined* by the framework axioms. For each, a Lean uniqueness theorem
must accompany the construction before the framework can claim derivation
without external choice.

## Status table

| # | Construction | Cheat-sheet line | Current status | Uniqueness theorem state |
|---|---|---|---|---|
| 1 | **τ_M Markov trace** on H_n(R, q) | line 234 (`[jones1987]` cited) | ✅ **DONE (#1422)** | `qou_markov_trace_is_jones_markov` refactored from selection-by-contrast → direct uniqueness statement via `MarkovTraceUniqueness` class (Wenzl/Jones axiom, AGENTS.md §3b-cond). τ_SW + `schur-weyl-vanishing.lean` fully purged. |
| 2 | **T_w SDP-canonical knot operator** | line 69, 95 | ✅ **SCAFFOLDED** (pre-existing, surfaced by 2026-05-30 audit) | `canonical_T_w_subsingleton_under_strict_complementarity` in `mass-theory/conj-canonical-knot-id-sdp.lean:748` ALREADY proves the Subsingleton uniqueness conditional on `StrictComplementarityPair`. Underlying `sorry` is in `QOU.MathlibExt.SDP.strict_complementarity_unique` (Mathlib SDP layer — PSD-cone strict convexity). Open work: discharge the Mathlib SDP sorry, OR upgrade `class CanonicalKnotIdSDP` to include a `strictComplementarity` field so per-instance witnesses certify uniqueness. |
| 3 | **Canonical p-n averaging form** | line 124, 128 | ⚠ **OPEN — genuinely missing** | No dedicated `averaging-resonance-rule.lean` file exists; only referenced from `bar-involution.md`, `c5-involution-leibniz-decomposition.ts`, etc. Needed: `pn_averaging_unique` — any p-n averaging satisfying (a) bar-invariance, (b) color-flavor compatibility (Bring color-tube symmetry), (c) standard normalisation, is unique. Open math (the Bring color-tube weighted vs uniform bar-invariant question) AND open Lean. |
| 4 | **VolDensity(K) per-knot** | line 175, 185 | ✅ **SCAFFOLDED** (pre-existing) | `particle-interactions/geom-universality.lean` already carries `class SingleVolumeIrrational`, `class PLCorrectnessHypotheses`, `class HyperbolicVolumeIndependence` (§3b-cond axiom classes) + `theorem geom_universality_conditional` + `theorem conditional_on_HyperbolicVolumeIndependence`. Open work: close one of those classes, OR add a top-level `vol_density_per_knot_unique` theorem that consumes all three. |
| 5 | **Archimedean realization functor** at q₀ | implicit (Step 8 of chain) | ⚠ **OPEN — no dedicated block** | Referenced from `chi-minus-six-chain.md`, `thurston-relaxation.md`, `crossing-energy-decomposition.{md,lean}`, but no `archimedean-realization-functor.{md,ts,lean}` block exists. Needed: create the block with `archimedean_functor_unique` theorem — the realisation functor `R = ℚ(q) → ℝ` at `q = q₀` is unique up to the gauge of the substrate symmetry. Lower priority; standard categorical-realisation result. |

> **2026-05-30 audit finding.** Items 2 + 4 were initially flagged as "open" but the framework already carries §3b-cond scaffolds (axiom classes + conditional theorems). The genuine outstanding work is items 3 + 5 (no Lean files exist yet) plus closing the remaining `sorry`s in items 2 + 4. This re-prioritisation is the focus of the post-#1422 follow-up branches.

> **2026-05-30 progress (post-#1422 follow-up PR #1445):**
> - Item 3 (`pn-averaging-uniqueness`): **scaffolded** — new
>   `mass-theory/pn-averaging-uniqueness.{lean,md,ts}` block with
>   `BarInvariant` / `ColorFlavorCompatible` / `StandardNorm` classes
>   and theorems `pn_averaging_unique` + `pn_averaging_subsingleton`,
>   proved sorry-free conditional on the three classes.
> - Item 4 (VolDensity): **top-level theorem added** to
>   `particle-interactions/geom-universality.lean` — new classes
>   `GeomFullFunctorial`, `GeomFullCanonicalSeed`, theorems
>   `vol_density_per_knot_unique` + `vol_density_subsingleton` proved
>   sorry-free conditional on the seed class.
> - Item 5 (Archimedean realisation): **uniqueness theorems added**
>   to the existing `mass-theory/archimedean-realization-functor.lean`
>   — `archimedean_realize_determined` (immediate from the
>   `compat_integer` law) + `archimedean_realize_pointwise_unique`
>   (companion, proved sorry-free).
> - Item 2 (T_w SDP): unchanged — the existing
>   `canonical_T_w_subsingleton_under_strict_complementarity`
>   already proves the Subsingleton uniqueness; the underlying
>   sorry in `QOU.MathlibExt.SDP.strict_complementarity_unique` is
>   queued as a separate Mathlib-SDP follow-up.
>
> Each item's §3b-cond conditional-class hypothesis is now in place;
> closing the remaining axiom-class instances (the open math —
> Bring color-tube weighted for item 3; Family-A linking-weight
> extension for item 4; Mathlib `FractionField` universal property
> for the abstract Archimedean form is unnecessary since item 5
> uses the concrete `compat_integer` law structurally) is the
> per-item follow-up work.

## Notes

- **q₀ is NOT a uniqueness item** — q₀ is a *calibration choice* (pinned from CODATA m_p/m_e per #1422), not a mathematically unique value. The framework is parametric in q₀; the uniqueness items above hold for every q in the appropriate generic locus.
- **The Wedderburn decomposition + Hecke algebra** uniqueness are standard
  theorems (Mathlib / Drinfeld–Jimbo) — assumed without re-proof.
- **Class-axiomatisation pattern** (AGENTS.md §3b-cond): when the cited
  uniqueness is an established external theorem (Wenzl, Jones), the Lean
  proof axiomatizes it as a `class` with the `-- Ref:` citation, and
  downstream results are proved sorry-free *conditional on the class
  instance*. The Mathlib pattern for citing established uniqueness
  results.

## Workflow

For each item:

1. **Authoring**: add a `theorem <X>_unique` in the relevant `.lean` file,
   axiom-classed where appropriate.
2. **Narrative**: add a paired remark/proposition block in `.md` describing
   the uniqueness statement + its physical content.
3. **Compute consequence**: identify any production script that previously
   chose between candidates and prove it now picks the unique canonical
   form.
4. **Audit**: add the uniqueness theorem to the cheat sheet's reference
   column.

## See also

- [`canonical-derivation-cheat-sheet.md`](canonical-derivation-cheat-sheet.md)
- [`audits/2026-05-11-why-individual-mass-residuals-fit-not-derive.md`](audits/2026-05-11-why-individual-mass-residuals-fit-not-derive.md) §"Resolution 2026-05-29"
- `content/quantum-observable-universe/mass-theory/markov-trace-frobenius-selection.lean`
