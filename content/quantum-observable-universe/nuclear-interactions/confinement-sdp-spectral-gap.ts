import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:confinement-sdp",
  label: "rem:confinement-sdp-spectral-gap",
  title: "SDP feasibility as Hecke spectral-gap condition",
  uses: ["prop:confinement-sdp"],
  tags: [
    "interpretation",
    "sdp-feasibility",
    "spectral-gap",
    "deconfinement",
    "kauffman-bracket",
  ],
});
