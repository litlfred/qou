import { remark } from "../../schema/builders";
export default remark({
  interprets: "rem:schrodinger-jet-coaction",
  label: "rem:madelung-fluid",
  title: "Madelung transformation: quantum fluid, geodesics, and divisor topology",
  uses: [
    "rem:schrodinger-jet-coaction",
    "rem:gr-substrate-geometry",
    "def:mass-identity",
    "rem:algebraic-filter",
  ],
  tags: ["madelung", "fluid-dynamics", "acoustic-metric", "divisor", "vortex"],
});
