import { remark } from "../../schema/builders";

export default remark({
  label: "rem:sdp-strictly-beats-ilp",
  title:
    "SDP on H_A 3-channel strictly beats ILP on H_{3A} Plancherel for nuclear binding",
  interprets: "prop:tower-binding-energy",
  uses: [
    "prop:tower-binding-energy",
    "prop:confinement-sdp",
    "prop:mass-endomorphism-tower",
  ],
  tags: [
    "sdp",
    "ilp",
    "framework-comparison",
    "binding-energy",
    "mass-prediction",
  ],
});
