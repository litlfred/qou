import { remark } from "../../schema/builders";

export default remark({
  label: "rem:x5-bring-prym-jacobian",
  title: "Parallel structure at the Jacobian level",
  tags: ["jacobian", "prym", "z5", "bring", "hyperelliptic"],
  uses: ["prop:x5-bring-weight-identification"],
  interprets: "prop:x5-bring-weight-identification",
  cites: ["edge1978", "riera-rodriguez-1992", "braden-northover-2012"],
});
