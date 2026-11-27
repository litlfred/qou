import { remark } from "../../schema/builders";
export default remark({
  interprets: "rem:schrodinger-jet-coaction",
  label: "rem:madelung-fluid",
  title: "Madelung transformation: quantum fluid and vortex filaments",
  uses: [
    "rem:schrodinger-jet-coaction",
    "def:mass-identity",
    "rem:algebraic-filter",
  ],
  cites: [
    "madelung1927",
    "takabayasi1952",
    "takabayasi1983",
  ],
  tags: ["madelung", "fluid-dynamics", "acoustic-metric", "divisor", "vortex"],
});
