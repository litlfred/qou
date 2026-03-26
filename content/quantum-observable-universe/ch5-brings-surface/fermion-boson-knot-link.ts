import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:fermion-boson-knot-link",
  title:
    "Fermions are knots, bosons are links",
  tags: [
    "fermion",
    "boson",
    "knot",
    "link",
    "torus-knot",
    "component",
    "reeb-flow",
    "vertical",
  ],
  lean: {
    decl: "QOU.Descartes.fermion_boson_knot_link",
    validation: "not_checked",
  },
  uses: [
    "def:fermion-boson-decomposition",
    "def:categorical-reeb",
    "prop:torus-knot-generators",
    "conj:borromean-quark",
    "rem:knot-notation-convention",
  ],
});
