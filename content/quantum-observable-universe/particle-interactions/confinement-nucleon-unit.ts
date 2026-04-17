import { remark } from "../../schema/builders";

export default remark({
  label: "rem:confinement-nucleon-unit",
  title:
    "Nucleon-as-unit justification from LP confinement proof",
  tags: [
    "confinement",
    "nucleon",
    "transfer-matrix",
    "lp-duality",
    "frobenius",
    "borromean",
  ],
  uses: [
    "prop:confinement-lp",
    "prop:confinement-topological",
    "prop:confinement-operator-selection",
    "def:transfer-matrix-operator",
  ],
  interprets: "prop:confinement-lp",
});
