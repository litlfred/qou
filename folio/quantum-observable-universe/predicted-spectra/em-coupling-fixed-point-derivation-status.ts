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
});
