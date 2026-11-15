import { remark } from "../../schema/builders";

export default remark({
  label: "rem:weight-identification-consequences",
  title: "Consequences of the weight identification",
  tags: ["weight-grading", "z5", "consolidation", "interpretation"],
  uses: [
    "rem:x5-bring-prym-jacobian",
    "thm:hyperelliptic-z5-classification",
    "rem:u1-phase-tube",
  ],
  interprets: "prop:x5-bring-weight-identification",
});
