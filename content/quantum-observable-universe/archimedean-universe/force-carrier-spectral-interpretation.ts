import { remark } from "../../schema/builders";

export default remark({
  label: "rem:force-carrier-spectral-interpretation",
  title:
    "Force-carrier sector has no degrees of freedom",
  interprets: "prop:force-carrier-bring-uniqueness",
  uses: [
    "prop:force-carrier-bring-uniqueness",
    "rem:force-knot-identification",
  ],
  tags: [
    "interpretation",
    "force-carrier",
    "topological-invariant",
    "no-fitting",
  ],
});
