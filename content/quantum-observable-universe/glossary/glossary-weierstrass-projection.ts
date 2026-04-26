import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-weierstrass-projection",
  title: "Weierstrass projection $\\wp_q(z)$",
  tags: [
    "glossary",
    "weierstrass",
    "elliptic-function",
    "descartes",
    "projection",
    "lattice",
  ],
  lean: { ref: "qou:QOU.Descartes.weierstrassProjection",
    validation: "not_checked",
  },
  uses: [
    "prop:descartes-elliptic-curve",
  ],
  defines: ["weierstrass-projection"],
});
