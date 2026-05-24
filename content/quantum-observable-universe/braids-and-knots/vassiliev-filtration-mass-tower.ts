import { remark } from "../../schema/builders";

export default remark({
  label: "rem:vassiliev-filtration-mass-tower",
  title:
    "The mass-tower $h$-expansion is a Vassiliev filtration",
  interprets: "prop:markov-trace-axiomatic-closed-form",
  uses: [
    "prop:markov-trace-axiomatic-closed-form",
    "rem:archimedean-image-table",
    "rem:operator-valued-mass-split",
  ],
  cites: [
    "jones1987",
    "reshetikhin1991",
  ],
  tags: [
    "vassiliev",
    "finite-type",
    "filtration",
    "mass-tower",
    "exposition",
    "optimization",
  ],
});
