import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:chain-ring-comparison",
  label: "rem:chain-ring-comparison-interpretation",
  title: "Derivation chain, the factor of $1/2$, and open problems",
  tags: [
    "comparison",
    "experimental",
    "theoretical",
    "ring-closure",
    "substrate-parameter",
    "aromaticity",
  ],
  uses: [
    "prop:chain-ring-comparison",
    "def:substrate-parameter",
    "prop:topological-mass-formula",
    "rem:chain-ring-energy",
    "tbl:chain-ring-comparison-table1-data",
    "tbl:chain-ring-comparison-table2-data",
  ],
});
