import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:descartes-elliptic-curve",
  title:
    "The Descartes elliptic curve $\\mathcal{E}_q$",
  tags: [
    "elliptic-curve",
    "descartes",
    "color-fibration",
    "substrate-parameter",
    "golden-ratio",
    "weierstrass",
  ],
  lean: { ref: "qou:QOU.Archimedean.descartes_elliptic_curve",
    validation: "not_checked",
  },
  uses: [
    "rem:color-tube-cubic",
  ],
});
