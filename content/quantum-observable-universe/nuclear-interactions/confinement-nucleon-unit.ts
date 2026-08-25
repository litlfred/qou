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
  uses: ["prop:confinement-topological"],
  interprets: "prop:confinement-lp",
});
