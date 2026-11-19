import { remark } from "../../schema/builders";

export default remark({
  label: "rem:chirality-period-pairing",
  title:
    "Chirality structure on Goncharov period classes via the bar involution",
  interprets: "prop:hecke-baer-star-generic",
  uses: ["conj:bring-trilog-depth-3-witness"],
  cites: ["bloch2000"],
  tags: [
    "chirality",
    "amphichirality",
    "bar-involution",
    "period-pairing",
    "chern-simons",
    "tate-twist",
    "graded-mikusinski",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/hyperbolic_volumes.py",
    witness: "computations/hyperbolic-volumes.witness.json",
    status: "verified",
  },
});
