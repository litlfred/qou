import { remark } from "../../schema/builders";

export default remark({
  label: "rem:mass-spectrum-generating-function",
  title:
    "Confined Laurent polynomial $P_K(q)$ as mass-spectrum generating function: functorial equivalence to scalar mass via aether evaluation",
  interprets: "rem:two-tier-scaling-pq",
  uses: [
    "rem:two-tier-scaling-pq",
    "rem:categorical-mass-positivity",
  ],
  cites: [
    "khovanovlauda2009",
    "brundankleshchev2009",
  ],
  tags: [
    "mass-spectrum",
    "generating-function",
    "partition-function",
    "graded-hecke-energy",
    "microstate-degeneracy",
    "substrate-evaluation",
    "functorial-equivalence",
    "categorical-mass",
  ],
});
