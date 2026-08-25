import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:confinement-sdp",
  label: "rem:confinement-misdp",
  title: "Mixed-integer SDP for integer-rank confinement levels",
  uses: ["prop:confinement-sdp"],
  tags: [
    "interpretation",
    "misdp",
    "branch-and-cut",
    "integer-constraints",
    "confinement-hierarchy",
  ],
});
