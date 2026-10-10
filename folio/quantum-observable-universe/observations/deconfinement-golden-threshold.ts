import { remark } from "../../schema/builders";

export default remark({
  interprets: "rem:golden-ratio-degeneration",
  label: "rem:deconfinement-golden-threshold",
  title:
    "Quark-gluon plasma deconfinement as the golden ratio phase transition",
  tags: [
    "deconfinement",
    "quark-gluon-plasma",
    "phase-transition",
    "golden-ratio",
    "first-order",
    "color-confinement",
    "nodal-degeneration",
  ],
  uses: [
    "rem:golden-ratio-degeneration",
    "rem:q-chromaticity",
    "prop:strangelet-crossing-energy",
  ],
});
