import { remark } from "../../schema/builders";

export default remark({
  label: "rem:fermion-boson-chart-localization",
  title:
    "Fermion--boson sectors as chart-glue data of $\\mathbb{P}_q(V)$",
  tags: [
    "fermion",
    "boson",
    "affine-chart",
    "projective-line",
    "substrate-parameter",
    "interpretation",
  ],
  uses: ["rem:observation-fermion-action"],
  interprets: "def:fermion-boson-decomposition",
});
