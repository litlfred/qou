import { definition } from "../../schema/builders";

export default definition({
  label: "def:weierstrass-projection",
  title: "Weierstrass projection $\\wp_q(z)$",
  tags: [
    "weierstrass",
    "elliptic-function",
    "descartes",
    "projection",
    "lattice",
  ],
  lean: {
    decl: "QOU.Descartes.weierstrassProjection",
    validation: "not_checked",
  },
  uses: [
    "prop:descartes-elliptic-curve",
  ],
});
