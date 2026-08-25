import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:confinement-sdp",
  label: "rem:confinement-sdp-vs-lp",
  title: "Relation of the confinement SDP to the scalar LP",
  uses: ["prop:confinement-sdp"],
  tags: [
    "interpretation",
    "lp-relaxation",
    "diagonal-restriction",
    "wedderburn-decoupling",
  ],
});
