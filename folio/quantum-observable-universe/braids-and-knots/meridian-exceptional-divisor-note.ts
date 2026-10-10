import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:meridian-holonomy-boost",
  label: "rem:meridian-exceptional-divisor-note",
  title:
    "The meridian is at the exceptional divisor; the per-operation tick is the Compton time, not the Planck time",
  uses: ["prop:meridian-holonomy-boost"],
  tags: [
    "exceptional-divisor",
    "meridian",
    "planck-time",
    "compton-time",
    "hierarchy",
    "calibration-discipline",
    "boost",
  ],
});
