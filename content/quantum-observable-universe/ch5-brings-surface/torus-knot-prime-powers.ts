import { remark } from "../../schema/builders";

export default remark({
  label: "rem:torus-knot-prime-powers",
  title: "Prime-power structure of $T_{3,p^k}$ generators",
  interprets: "prop:torus-embeddable-complete",
  tags: [
    "torus-knot",
    "prime-power",
    "genus",
    "mass-hierarchy",
    "trefoil",
    "top-quark",
    "self-intersection",
  ],
  uses: [
    "prop:torus-embeddable-complete",
    "prop:torus-knot-generators",
    "rem:unmapped-torus-knots",
    "def:up-quark",
    "def:electron-knot",
  ],
});
