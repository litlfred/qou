import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:gb-residue-spectral-sum",
  label: "rem:bw-empirical-misses",
  title:
    "Terms predicted by the categorical mass that empirical Bethe–Weizsäcker omits",
  tags: [
    "bethe-weizsacker",
    "predictions",
    "falsifiability",
    "residue",
    "cross-channel",
    "chirality",
    "interpretation",
  ],
  uses: [
    "prop:gb-residue-spectral-sum",
    "prop:schur-weyl-mass-decomposition",
    "prop:graded-trace-residue-split",
    "rem:bw-mass-decomposition-dictionary",
    "prop:mass-endomorphism-tower",
    "def:confinement-level",
    "def:braid-twist-flip",
  ],
});
