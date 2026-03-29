import { definition } from "../../schema/builders";

export default definition({
  label: "def:notation-conventions",
  title:
    "Notation conventions for knots, atoms, and operators",
  tags: [
    "notation",
    "convention",
    "knot",
    "atom",
    "hecke-algebra",
    "transfer-matrix",
    "groebner-basis",
    "torus-knot",
    "borromean",
    "skein",
  ],
  lean: {
    decl: "QOU.Descartes.notation_conventions",
    validation: "not_checked",
  },
  uses: [
    "prop:nuclear-groebner-reduction",
    "def:transfer-matrix-operator",
    "def:stable-nucleus",
    "def:up-quark",
    "def:down-quark",
    "def:electron-knot",
  ],
});
