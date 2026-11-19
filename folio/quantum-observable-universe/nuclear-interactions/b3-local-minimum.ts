import { remark } from "../../schema/builders";

export default remark({
  label: "rem:b3-local-minimum",
  title:
    "$\\mathcal{B}_3$ is a local minimum of the categorical action",
  interprets: "prop:confinement-lp",
  tags: [
    "b3",
    "local-minimum",
    "gram-matrix",
    "eigenvalue",
    "confinement",
  ],
  uses: [
    "prop:confinement-lp",
  ],
  computation: {
    engine: "numpy",
    script: "computations/gram-matrix-dual.py",
    witness: "computations/gram-matrix-dual.witness.json",
    status: "verified",
  },
});
