import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:skein-generation",
  label: "rem:skein-generation-hadron-reading",
  title: "Fundamental knots, the Hopf link and the hadron reading of skein generation",
  tags: ["skein", "hadron", "torus-knot", "interpretation"],
  uses: ["prop:skein-generation", "lem:skein-mass-from-linking"],
});
