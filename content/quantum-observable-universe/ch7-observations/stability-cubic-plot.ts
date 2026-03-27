import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:integer-stability",
  label: "rem:stability-cubic-plot",
  title:
    "The stability cubic at $q = 1.110$: lattice points and the nuclear chart",
  tags: [
    "stability-cubic",
    "lattice-points",
    "nuclear-chart",
    "codata",
    "plot",
  ],
  uses: [
    "prop:integer-stability",
    "rem:diophantine-valley",
    "prop:beta-stability",
    "def:substrate-parameter",
  ],
});
