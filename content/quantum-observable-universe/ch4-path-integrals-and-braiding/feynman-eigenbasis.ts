import { remark } from "../../schema/builders";

export default remark({
  label: "rem:feynman-eigenbasis",
  title: "Feynman path integrals, eigenbases, and finiteness",
  tags: ["path-integral", "feynman", "categorical-trace", "mass"],
  uses: [
    "prop:braid-action-tensor",
    "prop:knot-eigenbasis-complete",
    "rem:skein-decomposition",
    "def:mass-identity",
    "rem:skein-mass-relation",
    "rem:r-matrix-braiding",
  ],
});
