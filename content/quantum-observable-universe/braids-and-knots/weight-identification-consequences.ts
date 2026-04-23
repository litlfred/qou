import { remark } from "../../schema/builders";

export default remark({
  label: "rem:weight-identification-consequences",
  title: "Consequences of the weight identification",
  tags: ["weight-grading", "z5", "consolidation", "interpretation"],
  uses: [
    "prop:x5-bring-weight-identification",
    "rem:x5-bring-prym-jacobian",
    "conj:torus-knot-seifert-bound",
    "rem:u1-phase-tube",
  ],
  interprets: "prop:x5-bring-weight-identification",
});
