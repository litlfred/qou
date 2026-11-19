import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:substrate-parameter",
  label: "rem:substrate-gm-torsion",
  title:
    "The aether parameter as a $\\mathbb{G}_m$-section: torsion, specialisation, and the $q = 1$ boundary",
  uses: ["prop:ns-obstruction-tower"],
  tags: [
    "multiplicative-group",
    "torsion",
    "specialisation",
    "projective",
    "not-root-of-unity",
  ],
});
