import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:x5-bring-weight-identification",
  label: "rem:x5-bring-weight-geometric-content",
  title: "Geometric content of the weight-$(-1)$ identification",
  uses: [
    "prop:x5-bring-weight-identification",
    "rem:u1-phase-tube",
    "rem:x5-bring-prym-jacobian",
  ],
});
