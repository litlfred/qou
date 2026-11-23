import { remark } from "../../schema/builders";

/**
 * Interpretive follow-on to prop:shell-filling-rule: discrete electron-count
 * LP shadow slopes mu_+ and mu_-, Mulliken electronegativity, Parr-Pearson
 * chemical hardness as the Perdew-Parr-Levy-Balduz derivative discontinuity,
 * noble-gas hardness peaks at cumulative 2n^2 period closures, and Hund
 * generator alternation.
 */
export default remark({
  label: "rem:shell-filling-electronegativity-ilp",
  title:
    "Electronegativity, Parr–Pearson shadow-price hardness, and ILP generator alternation",
  interprets: "prop:shell-filling-rule",
  lean: {
    ref: "qou:QOU.MathlibInfra.ConfinementLayerTower.parr_pearson_hardness_eq_shadow_jump",
    validation: "not_checked",
  },
  uses: [
    "def:electron-shell-braid-capacity",
    "prop:shell-capacity-self-square",
    "prop:shell-filling-rule",
  ],
  cites: [
    "mulliken1934",
    "perdew-parr-levy-balduz1982",
    "parr-pearson1983",
  ],
  computation: {
    engine: "python",
    script:
      "computations/probes/confinement_layer_tower_chem/confinement_layer_tower_chem_probe.py",
    witness: [
      "computations/probes/confinement_layer_tower_chem/confinement-layer-tower-chem.witness.json",
    ],
    status: "experimental",
  },
  tags: [
    "electronegativity",
    "chemical-hardness",
    "ILP",
    "Hund",
    "generator-alternation",
    "LP-dual",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-23",
      body:
        "Layer-3 shadow-price identities (`parr_pearson_hardness_eq_shadow_jump`, " +
        "`two_mul_mulliken_eq_neg_shadow_sum`, `parr_pearson_hardness_nonneg_iff_convex`, " +
        "`noble_gas_magic_closures_eq`) are proved over generic `[CommRing K]` / `[Field K]` " +
        "in `QOU.MathlibInfra.ConfinementLayerTower` (bean qou-5lct).",
    },
  ],
});
