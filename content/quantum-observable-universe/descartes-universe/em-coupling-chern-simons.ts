import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:em-coupling-chern-simons",
  title:
    "Fine structure constant with Chern-Simons correction on Bring's surface",
  lean: { ref: "qou:QOU.DescartesUniverse.em_coupling_gluon_octet",
    validation: "not_checked",
  },
  uses: [
    "prop:em-coupling-projection",
    "def:brings-surface",
    "prop:torus-knot-generators",
    "def:knot-particle-generation",
    "thm:topological-mass",
    "prop:quantum-observable-universe-exists",
    "def:substrate-parameter",
  ],
  tags: [
    "fine-structure",
    "chern-simons",
    "brings-surface",
    "genus-4",
    "torus-knot",
    "gram-matrix",
  ],
});
