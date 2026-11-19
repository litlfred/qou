import { remark } from "../../schema/builders";

export default remark({
  label: "rem:em-coupling-fixed-point-derivation-status",
  title: "Component assembly, derivation, and open-input status of the $\\alpha_{EM}$ fixed point",
  interprets: "prop:em-coupling-fixed-point",
  uses: [
    "prop:em-coupling-fixed-point",
    "prop:em-coupling-projection",
    "prop:alpha-em-categorical-trace-ratio",
    "prop:em-coupling-bring-zero-mode",
    "prop:photon-ir-zero-mode-bring",
  ],
  tags: ["alpha-em", "fine-structure", "fixed-point", "bloch-group", "formalization-status"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-19",
      body: "Formalization provenance moved from prose (`em-coupling-fixed-point.lean`): `AlphaEmFixedPointNormalization.b3_normalization` axiomatises the $B_3(\\mathbb{C})$ $\\mathcal{O}(\\alpha^2)$ normalization hypothesis, `QOU.ArchimedeanUniverse.fixedPoint_iff_cubic` proves the equivalence between the fixed-point equation and the cubic root for $\\alpha \\neq 0$, and `QOU.ArchimedeanUniverse.alpha_em_is_fixed_point_root` composes them without fabricated `sorry` instances.",
    },
  ],
});
