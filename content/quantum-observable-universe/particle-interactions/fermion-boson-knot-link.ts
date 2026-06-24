import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:fermion-boson-knot-link",
  proofs: ["prf:fermion-boson-knot-link"],
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
  lean: { ref: "qou:QOU.Braiding.fermion_boson_knot_link",
    validation: "not_checked",
  },
  uses: ["def:borromean-baryon"],
});
