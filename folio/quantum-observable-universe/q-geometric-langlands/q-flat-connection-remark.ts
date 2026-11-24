import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:q-flat-connection",
  label: "rem:q-flat-connection",
  title: "The $d_q^2 \\neq 0$ obstruction as curvature",
  uses: ["def:q-flat-connection", "prop:categorical-dq-squared", "def:q-local-system", "rem:kummer-filtration-obstruction"],
  tags: ["geometric-langlands", "curvature", "q-deformation"],
});
