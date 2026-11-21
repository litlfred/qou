import { conjecture } from "../../schema/builders";

export default conjecture({
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, item 4a): ## Lean axiomatisation (sketch)\n\n```lean\n-- Conditional on the S₅↔SO(3) fiber-action class:\nclass InterNucleonChannelColorTube\n    (M : Type*) [BrCategory M] [ColorTube M] [S5SO3Fiber M] where\n  /-- Per-arc canonical Hecke generator for (color-pair, nucleon-pair). -/\n  hecke_of_color_pair :\n    NucleonColorPair → HeckeAlgebra M\n  /-- The flavor-only projection (current production rule) is the\n      categorical average of `hecke_of_color_pair` over the 9 color\n      pairs of the (nucleon₁, nucleon₂) flavor type. -/\n  flavor_projection_compatibility :\n    ∀ (C₁ C₂ : NucleonColorContent),\n      avg_over_color_pairs (hecke_of_color_pair (C₁, C₂))\n        = flavor_only_hecke (flavor_of C₁) (flavor_of C₂)\n```\n\nThe class becomes inhabited by the $S_{5}$/SO(3) fiber data once the $S_5 \\leftrightarrow \\mathrm{SO}(3)$ fiber-action conjecture is established." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Conjecture (conditional on `conj:s5-so3-fiber-action`).**\n\nin [`isotope_record_schema.py:65{-}70, 176{-}178`](../../../computations/isotope_record_schema.py)—\n\n(conjectural class supplied by `conj:s5-so3-fiber-action`)\n\ndiagnostic ([`low-isotope-sign-flip-diagnostic.witness.json`](../../../computations/low-isotope-sign-flip-diagnostic.witness.json)) fits\n\nSee [`arc_count_diagnostic_degeneracy_probe.py`](../../../computations/probes/arc_count_diagnostic_degeneracy_probe.py).\n\nProbe scripts [`probe_pn_flavor_asymmetry.py`](../../computations/probe_pn_flavor_asymmetry.py) and [`probe_per_sheet_flavor_nonin.py`](../../computations/probe_per_sheet_flavor_nonin.py) report\n\n([`charge-symmetry-bond-probe.witness.json`](../../../computations/probes/charge-symmetry-bond-probe.witness.json))\n\n([`gg-production-bond-probe.witness.json`](../../../computations/probes/gg-production-bond-probe.witness.json))\n\nThis conjecture remains conditional on `conj:s5-so3-fiber-action` being formalised as a Lean class. Once available, the weight matrix $W_{c_1 c_2}$ derives as a tensor in the SO(3)-fiber data over Bring, with no remaining degrees of freedom. The statement then becomes unconditional: it is a conjecture only for as long as that upstream class is uninhabited.\n\n## Consumers\n\n- [`probes/charge_symmetry_bond_probe.py`](../../../computations/probes/charge_symmetry_bond_probe.py)\n- [`probes/gg_production_bond_probe.py`](../../../computations/probes/gg_production_bond_probe.py)\n- [`isotope_record_schema.py`](../../../computations/isotope_record_schema.py)\n- [`mass_table_comprehensive.py`](../../../computations/mass_table_comprehensive.py)\n- [`closed_form_tau_M.py`](../../../computations/closed_form_tau_M.py)\n\nproducing the $A \\cdot 8G$ closure observed in [`isotope_record_schema.py:186`](../../../computations/isotope_record_schema.py)?\n\nformalised as `so3_adjoint_eq_chebyshev` in [`MassVolDensity.lean`](../lean/QOU/Mass/MassVolDensity.lean) §6.\n\nstill requires the $S_5 \\leftrightarrow \\mathrm{SO}(3)$ fiber action of `conj:s5-so3-fiber-action`.\n\n[`color-tube-coordinates.md`](color-tube-coordinates.md), [`color-tube-fibers.md`](color-tube-fibers.md), [`color-tube-cubic.md`](color-tube-cubic.md)\n\n- Supplier class: `conj:s5-so3-fiber-action`\n\n- $\\mathrm{SO}(3)_q = \\mathrm{SU}(2)_q/\\mathbb{Z}_2$ level structure: [`MassVolDensity.lean`](../lean/QOU/Mass/MassVolDensity.lean) §6\n\n- Empirical probe scripts: [`probe_pn_flavor_asymmetry.py`](../../computations/probe_pn_flavor_asymmetry.py), [`probe_per_sheet_flavor_nonin.py`](../../computations/probe_per_sheet_flavor_nonin.py)" },
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "Working-channel pointers pulled out of the published prose: the " +
        "parent sign-flip analysis is `docs/audits/-sign-flip-interpretation.md`, " +
        "the ⁴He magic-shell colour-tube reading is " +
        "`docs/audits/-4he-magic-shell-color-tube-audit.md`, the λ_scale / " +
        "Faddeev-resummation match is worked out in " +
        "`docs/audits/-lambda-scale-canonical-unification.md`, and the " +
        "weighted-averaging entry sits in " +
        "`docs/canonical-derivation-cheat-sheet.md`. The supplier class " +
        "`conj:s5-so3-fiber-action` is PR #1081 Task 3.",
    },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([Existence of the atom-knot for any (Z, N)](#prop:atom-knot-exists))" },
  ],
  label: "conj:inter-nucleon-channel-color-tube",
  title: "Inter-nucleon Hecke channel assignment from Bring color-tube weighting",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.InterNucleonChannelColorTube",
    validation: "not_checked",
  },
  // Note: the s5-so3-fibre-action conjecture is cited in the narrative
  // only — it is not yet a content block, so it is omitted from uses[]
  // (an unresolved ref would fail validation). Add it here once the
  // block exists.
  uses: [
    "def:color-tube-fibers",
    "def:hecke-normal-form",
    "prop:atom-knot-exists",
  ],
  cites: [
    "kashaev1997",
    "faddeev_kashaev1994",
    "ohtsuki2002",
    "khovanovlauda2009",
    "kashiwara1991",
  ],
  tags: [
    "tier:keystone",
    "color-tube",
    "channel-assignment",
    "inter-nucleon",
    "bring-surface",
    "s5-so3-fiber",
    "axiom-class",
    "open-problem",
    "conditional-on-class",
  ],
});
