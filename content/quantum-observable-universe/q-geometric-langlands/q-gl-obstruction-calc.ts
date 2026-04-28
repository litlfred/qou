import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-gl-obstruction-calc",
  lean: { ref: "qou:QOU.q_gl_obstruction_calc", validation: "not_checked" },
  title: "Obstruction to $q$-flatness",
  proofs: ["prf:q-gl-obstruction-calc"],
  tags: ["geometric-langlands", "yekutieli", "obstruction"],
});
