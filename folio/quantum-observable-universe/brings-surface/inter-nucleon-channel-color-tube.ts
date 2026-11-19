import { conjecture } from "../../schema/builders";

export default conjecture({
  authorNotes: [
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
  computation: {
    engine: "python+mpmath",
    script: "computations/habiro/habiro_exact_mass_endomorphism.py",
    witness: [
      "computations/habiro/habiro-exact-mass-endomorphism.witness.json",
      "computations/m-p-borromean-verification-50dps.witness.json",
      "computations/probes/h2_gg_electron/h2-gg-electron.witness.json",
    ],
    status: "verified",
  },
});
