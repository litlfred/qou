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
  uses: [
    "def:fermion-boson-decomposition",
    "prop:spectral-chart-correspondence",
    "prop:braiding-eigenvalue-extraction",
    "rem:affine-chart-origin-of-i-and-q",
    "rem:observation-fermion-action",
    "def:contact-affine-chart",
  ],
  interprets: "def:fermion-boson-decomposition",
});
