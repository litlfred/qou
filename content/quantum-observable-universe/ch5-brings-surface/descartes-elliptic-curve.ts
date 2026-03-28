import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:descartes-elliptic-curve",
  title:
    "The Descartes elliptic curve $E_q$",
  tags: [
    "elliptic-curve",
    "descartes",
    "chiral-fibration",
    "substrate-parameter",
    "golden-ratio",
    "weierstrass",
  ],
  lean: {
    decl: "QOU.Descartes.descartes_elliptic_curve",
    validation: "not_checked",
  },
  uses: [
    "prop:chiral-elliptic",
    "def:substrate-parameter",
    "def:brings-surface",
    "rem:color-tube-cubic",
    "prop:local-substrate-q",
  ],
});
