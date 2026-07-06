# Phase transitions + H₂O build + knot-symmetry hierarchy of matter

**Branch:** `claude/gallant-bohr-w9f6a6`
**Date:** 2026-06-08
**Status:** WIP — workplan stub (PR opened first per AGENTS.md branch+PR policy)

## Owner request (verbatim intent)

> Update the **phase transitions** part with the new compute and proven
> math. Build **H₂O explicitly** (analogous to benzene in the organic
> chapter) to fully understand how it is composed. Then use the phase
> transition machinery from QOU and q₀ to see if we can reproduce
> **freezing / boiling / sublimation** points.
>
> This needs to build on **lattice** structure (particularly for ice).
> The missing bit: connect to the **confinement levels** and how that
> incorporates into symmetry/structure on H₂O specifically — what
> symmetry corresponds to the ice lattice? There is the lattice
> symmetry AND each H₂O's internal symmetries; they are intertwined.
>
> **Suggestion (owner hypothesis):** hierarchies of structures for
> phase transitions / types of matter for each atom are based on the
> **knot symmetries of the constituent parts**.
>
> Related: what happens to **electron shells** in a lattice?
>
> Start/fix H₂O explorations at **q₀** (or `q > 1` and less than the
> quantum-universe value, up to the golden/silver ratio — upper bound of
> q before a big behaviour-change transition, e.g. 3d→2d anyons, extreme
> q, or linear/optical-fibre systems) to keep things tractable.

## Findings (2026-06-08 survey — 3 Explore agents)

**Phase-transition machinery already exists** (information-theory Ch 8,
`sec:phase-transitions`) and is partly Lean-proven:
- [`prop:phase-transition-boundary`](../../content/quantum-observable-universe/information-theory/phase-transition-boundary.md)
  (+ `.lean`): gas↔liquid `T_q^{g→l}=S_q^∂/[2]_q`, liquid↔solid
  `T_q^{l→s}=S_q^∂/([2]_q·[n_K]_q)`, sublimation = non-split Hecke
  extension `Ext¹≅ℤ` (Hopf invariant of π₃(S²)).
- [`rem:phase-transition-interpretation`](../../content/quantum-observable-universe/information-theory/phase-transition-interpretation.md):
  three phases = symmetric / mixed / antisymmetric Hecke channels.
- **Temperature IS calibrated**:
  [`def:quantum-temperature`](../../content/quantum-observable-universe/information-theory/quantum-temperature.md)
  `T_q = ℏ_q = (q−1)/q`; Boltzmann + gas-constant blocks give the Kelvin
  bridge. **But no numerical evaluation at q₀ yet.**

**Molecular-construction chapter exists** (Ch 12) with the full template:
[`def:molecular-braid`](../../content/quantum-observable-universe/molecular-construction/molecular-braid.md),
benzene / CH₄ / CO₂ / CO / H₂ built; oxygen valence = 2 + 2 lone pairs
already specified ([`valence-from-braid`](../../content/quantum-observable-universe/molecular-construction/valence-from-braid.md)).
**No H₂O block yet** — clean new target. ⚠ Owner flags this chapter as
**VERY OLD** → currency + compute-wiring audit launched
([`2026-06-08-molecular-chapter-currency-wiring-audit.md`](../audits/2026-06-08-molecular-chapter-currency-wiring-audit.md),
in flight).

**Knot-symmetry hierarchy backbone exists**:
[`cor:knot-factor-borromean-composite`](../../content/quantum-observable-universe/mass-theory/knot-factor-borromean-composite.md)
— composite knot factor = product of constituent factors (Brunnian
decoupling). This is the proven core of the owner's "hierarchies ←
constituent knot symmetries" hypothesis.

**Confinement filtration ladder exists**:
[`def:confinement-level`](../../content/quantum-observable-universe/particle-interactions/confinement-level.md)
`J^ℓ(q)`, with phase transitions at LP boundary `E(λ,q*)=0`.

**Electron shells** = Hopf-linked trefoils
([`def:electron-shell`](../../content/quantum-observable-universe/predicted-spectra/electron-shells-hopf.md),
`def:electron-shell-braid-capacity`); shell capacity `2n²`.

**GAP — lattice / crystal symmetry**: the framework is *topologically*
periodic (Chebyshev / transfer-matrix), with **no space-group / crystal-
lattice content**. This is exactly the owner's ice-lattice question and
is the genuine new structure to design.

**Headline science — scale-free phase ratio** (formalize-first, see
[`2026-06-08-phase-transition-ratio-formalize-first.md`](../audits/2026-06-08-phase-transition-ratio-formalize-first.md)):
`T_boil/T_freeze = [n_K]_q` (S_q^∂ cancels). Cheap test over the 6
chapter-12 molecules: measured ratios cluster in (1.20, 1.45); the
**integer-crossing reading is refuted** (integer `n_K≥2` over-predicts
~50%). Points at the self-referential `T_q=ℏ_q` running-q fixed point —
resolve structurally before any numerical phase build.

## Workplan (reprioritized 2026-06-08)

0. **[lead] Validate + currency-fix the molecular chapter** (owner's
   newest ask — foundational). Audit in flight; then apply (i) mechanical
   fixes, (ii) framework-currency rewrites (purged λ_scale / Geom_full /
   scalar ρ_q), (iii) compute rewiring (canonical pkgs + LP duals +
   witnesses). H₂O is built on the *fixed* chapter, not the stale one.
1. **Build H₂O** (`def:h2o-molecular-braid` + siblings) against the
   current framework — O(8,8) + 2 H, bent geometry from lone-pair
   repulsion, in the molecular-construction chapter §"Water".
2. **Phase-ratio fixed point** — derive the running-q form of
   `T_boil/T_freeze`; re-test; only then absolute temps (needs Kelvin
   scale). Witnessed compute routed through `qou_substrate`.
3. **Knot-symmetry hierarchy of matter** — promote the owner hypothesis
   to a proposition built on `cor:knot-factor-borromean-composite` +
   `def:confinement-level`: matter-state ladder ← constituent knot
   symmetries.
4. **Ice lattice symmetry** (the gap) — design the lattice-symmetry
   object: lattice space group × internal H₂O symmetry (intertwined);
   connect to confinement levels.
5. **Electron shells in lattice** — what the Hopf-trefoil shell model
   says happens to shells under lattice bonding.

## Discipline notes (AGENTS.md)

- Report numerical predictions **tiered** (proved / near-match /
  fitted), never binary; use `$\approx$` for q₀-derived values.
- **Formalize-first**: before any wide numerical search over phase
  points, state the hypothesis class + find the pruning invariant.
- **Corpus-grep** before declaring anything "open" / "missing".
- New compute → matching `alg:` appendix block + witness JSON.
- Primary content links point to the `.md` sibling.

## Open questions for the owner (to resolve before deep build)

- Scope of phase-transition predictions: qualitative ordering
  (solid < liquid < gas confinement) vs quantitative temperatures?
- q upper-bound regime: fix everything at q₀, or sweep q up to a
  golden/silver-ratio "anyonic" bound?
