import { remark } from "../../schema/builders";

export default remark({
  label: "rem:operator-valued-mass-split",
  title:
    "Operator-valued crossing structure separates topology from mass splitting",
  interprets: "prop:markov-trace-ratio-exact",
  uses: [
    "rem:archimedean-image-table",
    "prop:markov-trace-ratio-exact",
    "prop:markov-trace-axiomatic-closed-form",
    "def:archimedean-realization-functor",
  ],
  cites: [
    "bilsonthompson2005",
    "bilsonthompson2007",
    "reshetikhin1991",
    "joyce1982",
    "matveev1982",
    "jones1987",
  ],
  tags: [
    "amphicheirality",
    "operator-valued",
    "mass-split",
    "proton-neutron",
    "quandle",
    "colored-invariant",
    "precision-gap",
  ],
});
