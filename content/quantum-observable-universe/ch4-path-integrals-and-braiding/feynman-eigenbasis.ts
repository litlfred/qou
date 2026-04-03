import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:braid-action-tensor",
  label: "rem:feynman-eigenbasis",
  title: "Feynman path integrals, eigenbases, and finiteness",
  tags: ["path-integral", "feynman", "categorical-trace", "mass"],
  uses: [
    "prop:knot-eigenbasis-complete",
    "rem:skein-mass-relation",
    "rem:r-matrix-braiding",
  ],
});
