import { remark } from "../../schema/builders";

export default remark({
  label: "rem:vassiliev-filtration-mass-tower",
  title:
    "The mass-tower $h$-expansion is a Vassiliev filtration",
  interprets: "prop:markov-trace-axiomatic-closed-form",
  uses: [
    "rem:archimedean-image-table",
    "rem:operator-valued-magnitude-budget",
  ],
  cites: [
    "birmanlin1993",
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
