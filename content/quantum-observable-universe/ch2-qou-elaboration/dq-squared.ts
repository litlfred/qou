import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:dq-squared",
  title: "d_q^2 does not vanish",
  hasProof: true,
  tags: ["q-deformation", "exterior-derivative"],
  uses: ["def:q-ext-deriv"],
});
