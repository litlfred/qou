import { remark } from "../../schema/builders";

export default remark({
  label: "rem:p-bandwidth-interpretation",
  interprets: "prop:p-bandwidth-bound",
  title: "P-class as a sub-horizon information funnel",
  tags: [
    "P-class",
    "bandwidth",
    "information-flow",
    "planck-step",
    "complexity",
    "information-funnel",
  ],
  uses: [
    "prop:p-bandwidth-bound",
    "def:information-bandwidth",
    "prop:reeb-operations-per-planck",
    "def:operational-entropy",
  ],
});
