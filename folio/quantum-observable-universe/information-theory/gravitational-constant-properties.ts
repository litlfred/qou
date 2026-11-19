import { remark } from "../../schema/builders";

export default remark({
  label: "rem:gravitational-constant-properties",
  interprets: "def:gravitational-constant",
  title: "Variational origin and Hausdorff-dimension prediction of $G_q$",
  tags: [
    "gravitational-constant",
    "information-theory",
    "jacobson",
    "entropy-area",
    "emergent-gravity",
  ],
  uses: [
    "def:gravitational-constant",
    "def:information-speed-of-light",
    "def:operational-entropy",
    "rem:gr-substrate-geometry",
    "rem:jet-planck-steps",
    "prop:descent-eigenspaces",
    "rem:julia-hausdorff-dimension-prediction",
  ],
  foreshadows: ["rem:julia-hausdorff-dimension-prediction"],
  cites: [
    "jacobson1995",
    "bekenstein1981",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/chirality_avg_content_atomic.py",
    witness: "computations/chirality-avg-content-atomic.witness.json",
    status: "verified",
  },
});
