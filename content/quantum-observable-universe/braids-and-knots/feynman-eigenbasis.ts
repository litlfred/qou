import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:braid-action-tensor",
  label: "rem:feynman-eigenbasis",
  title: "Feynman path integrals, eigenbases, and finiteness",
  computation: {
    engine: "mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: "computations/q-pinning-50-digit.witness.json",
    status: "verified",
  },
  tags: ["path-integral", "feynman", "categorical-trace", "mass"],
  uses: [
    "prop:knot-eigenbasis-complete",
    "rem:skein-mass-relation",
    "rem:r-matrix-braiding",
  ],
});
