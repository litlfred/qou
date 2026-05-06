import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:kazhdan-lusztig-classical-limit",
  title:
    "As $q \\to 1$, the KLR canonical basis flattens to the Kazhdan–Lusztig basis of $S_n$, recovering Pauli/Bose statistics",
  uses: [
    "conj:hecke-anyonic-substrate",
    "conj:crystal-graph-realization",
    "def:observation",
  ],
  cites: [
    "kassel1995",
    "khovanovlauda2009",
    "kashiwara1991",
    "lecouvey2007",
  ],
  tags: [
    "classical-limit",
    "kazhdan-lusztig-basis",
    "klr-canonical-basis",
    "symmetric-group",
    "pauli-exclusion",
    "bose-einstein",
    "decategorification",
  ],
});
